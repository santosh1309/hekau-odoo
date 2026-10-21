#!/usr/bin/env python3
"""Build the page views (and the inner-page block templates) of website_hekau.

The website builder can only add, move and edit sections that live in the
page's own view: a page made of `t-snippet-call`s would make every section edit
change the block template itself. So pages ship the blocks' HTML inline, and
this script writes them:

* Home-page blocks (views/snippets/s_hk_*.xml, hand-written) are copied as
  they are, optionally with text replacements.
* Inner-page blocks are produced by scripts/hk_render.py from the content in
  scripts/hk_content.py; their block templates (Blocks > Hekau) are written
  from the same functions with default content.

Usage (from the module folder):  python3 scripts/build_pages.py

Run it after changing a block or the content, then upgrade the module. Pages
already edited in the website builder keep their own copy.
"""
import re
import sys
from pathlib import Path

from lxml import etree

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hk_render as R  # noqa: E402
from hk_content import SERVICES, ABOUT, WORK, WORK_FILTERS, CASE  # noqa: E402

MODULE = Path(__file__).resolve().parent.parent
SNIPPETS = MODULE / 'views' / 'snippets'


# --------------------------------------------------------------------------------
# Section sources
# --------------------------------------------------------------------------------

def copy_block(block, replace=None, add_class=None, drop_id=False):
    """The <section> of a hand-written block file, marked like a dropped block."""
    source = (SNIPPETS / f'{block}.xml').read_text()
    match = re.search(r'^( *)<section\b.*?</section>', source, re.S | re.M)
    if not match:
        raise SystemExit(f'{block}: no <section> found')
    base = len(match.group(1))
    lines = match.group(0)[base:].split('\n')
    section = '\n'.join([lines[0]] + [line[base:] if line[:base].strip() == '' else line for line in lines[1:]])
    for old, new in (replace or {}).items():
        if old not in section:
            raise SystemExit(f'{block}: text to replace not found: {old!r}')
        section = section.replace(old, new)
    if add_class:
        section = re.sub(r'(<section\b[^>]*class=")([^"]*)"', lambda m: f'{m.group(1)}{m.group(2)} {add_class}"', section, count=1)
    if drop_id:
        section = re.sub(r'(<section\b[^>]*?) id="[^"]*"', r'\1', section, count=1)
    return section


def tag(section, block):
    """Add data-snippet to the section's opening tag."""
    opening = re.match(r'<section\b[^>]*>', section).group(0)
    if 'data-snippet=' in opening:
        return section
    tagged = opening.replace(' data-name=', f' data-snippet="{block}" data-name=', 1)
    return tagged + section[len(opening):]


def block_name(section):
    return re.search(r'class="(s_hk_[a-z_]+)', section).group(1)


def render(entry):
    if isinstance(entry, tuple) and len(entry) == 2 and isinstance(entry[1], dict):
        # (section, CSS custom properties: Figma spacing etc.)
        section = render(entry[0])
        opening = re.match(r'<section\b[^>]*>', section).group(0)
        props = ' '.join(f'--{k}: {v}px;' for k, v in entry[1].items() if v is not None)
        return opening[:-1] + f' style="{props}">' + section[len(opening):] if props else section
    if isinstance(entry, str):
        if entry.lstrip().startswith('<section'):
            section = entry.strip()
        else:
            section = copy_block(entry)
    else:
        section = copy_block(*entry) if not isinstance(entry, dict) else copy_block(**entry)
    etree.fromstring(section.encode())  # well-formed before it goes into a view
    return tag(section, block_name(section))


def indent(text, n):
    pad = ' ' * n
    return '\n'.join(pad + line if line else line for line in text.split('\n'))


# --------------------------------------------------------------------------------
# Writers
# --------------------------------------------------------------------------------

def write(path, xml):
    etree.fromstring(xml.encode())
    (MODULE / path).write_text(xml)
    print('wrote', path)


def write_homepage(path, comment, sections):
    body = '\n'.join(indent(render(s), 16) for s in sections)
    write(path, f'''<?xml version="1.0" encoding="utf-8"?>
<odoo>

    <!-- {comment} -->
    <template id="homepage" inherit_id="website.homepage" name="Hekau Home Page">
        <xpath expr="//div[@id='wrap']" position="replace">
            <div id="wrap" class="oe_structure hk-page">
{body}
            </div>
        </xpath>
    </template>

</odoo>
''')


def page_xml(xmlid, name, url, sections, description='', grid_top=900, pt=None, pt_m=None, props=None, grid_height=None):
    """pt / pt_m: Figma desktop / mobile spacing of each section after the first
    one; props: extra custom properties per section index."""
    if pt or pt_m or props:
        n = len(sections)
        pt = list(pt or []) + [None] * n
        pt_m = list(pt_m or []) + [None] * n
        first = (props or {}).get(0)
        out = [(sections[0], first) if first else sections[0]]
        for i, s in enumerate(sections[1:]):
            values = {'hk-pt': pt[i], 'hk-pt-m': pt_m[i]}
            values.update((props or {}).get(i + 1, {}))
            out.append((s, values))
        sections = out
    body = '\n'.join(indent(render(s), 16) for s in sections)
    style_props = (f'--hk-grid-top: {grid_top}px;' if grid_top != 900 else '') + \
        (f' --hk-grid-height: {grid_height}px;' if grid_height else '')
    style = f' style="{style_props.strip()}"' if style_props else ''
    return f'''    <template id="{xmlid}" name="{name}">
        <t t-call="website.layout">
            <div id="wrap" class="oe_structure hk-page"{style}>
{body}
            </div>
        </t>
    </template>
    <record id="{xmlid}_page" model="website.page">
        <field name="url">{url}</field>
        <field name="view_id" ref="{xmlid}"/>
        <field name="is_published">True</field>
        <field name="header_overlay">True</field>
        <field name="track">True</field>
        <field name="website_meta_description">{R.t(description)}</field>
    </record>'''


def write_pages(path, comment, pages):
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<odoo>

    <!-- {comment} -->
{chr(10).join(page_xml(**p) for p in pages)}

</odoo>
'''
    write(path, xml)


def write_block_template(block, title, description, section):
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<odoo>

    <!-- {description}
         GENERATED by scripts/build_pages.py (scripts/hk_render.py). -->
    <template id="{block}" name="{title}">
{indent(section, 8)}
    </template>

</odoo>
'''
    write(f'views/snippets/{block}.xml', xml)


# --------------------------------------------------------------------------------
# Content
# --------------------------------------------------------------------------------

SERVICE_PAGES = [
    # key, url, page name, extra blocks after the hero
    ('web', '/web-application-development', 'Web Application Development'),
    ('mobileapp', '/mobile-application-development', 'Mobile Application Development'),
    ('ux', '/ux-ui-design', 'UX/UI Design'),
    ('cloud', '/cloud-managed-services', 'Cloud-Managed Services'),
    ('bpa', '/business-process-automation', 'Business Process Automation'),
    ('ai', '/ai-solutions', 'AI Solutions'),
]

INTROS = {
    'web': R.attributes(
        'Core Attributes',
        'Web application development doesn’t end with designing a functional interface.',
        'Your application has to be:',
        ['Scalable', 'Fast-loading', 'Business App Integrated', 'Cross-Platform Responsive',
         'Inclusive & Accessible', 'SEO Friendly', 'Secure Compliant']),
    'mobileapp': R.highlight(
        'Feature-packed custom mobile app designs. Build apps your customers like using, whether they are iOS or Android users.',
        ('Become an App Owner', '/contactus'),
        [{'value': '89%', 'label': 'Of smartphone users’ time is spent on mobile apps'},
         {'value': '$35+', 'small': 'Billion', 'label': 'Is spent on and via mobile apps per quarter globally'},
         {'value': '66%', 'label': 'Of business orders come from mobile apps'},
         {'value': '99%', 'label': 'Of mobile app revenues come from free apps'}]),
    'bpa': R.highlight(
        'With Hekau’s automation strategy, you don’t do any work you don’t want to.',
        ('Schedule a Free Call', '/contactus'),
        [{'icon': 'bpa_1', 'label': 'Reduced workforce expenses'},
         {'icon': 'bpa_2', 'label': 'Lower chances of human error'},
         {'icon': 'bpa_3', 'label': 'Hours saved on repetitive tasks'},
         {'icon': 'bpa_4', 'label': 'High-quality customer service.'}],
        text='We keep your business connected, smooth running, and fast while you exercise your creative energy.',
        title_xl=True),
    'ai': R.ai_intro(
        'Intro:',
        '51% of businesses hesitate to get AI solutions due to the cost. Instead, they end up missing out on:',
        ['Smoother workflow', 'Lead generation & customer retention', 'Reduction of unnecessary operational costs.']),
}

# Pages where the partners strip follows the hero (Figma)
WITH_PARTNERS = {'web', 'ux'}

# Figma desktop spacing (padding-top) of each section after the hero, in page
# order (tools: design/tools/figma_gaps.py). None keeps the block's default.
PT = {
    'services': [None, 200, 200, 200, 280, 140, 160],
    'web': [160, 129, 150, 180, 160, 140, 140],
    'mobileapp': [160, 219, 160, 180, 160, 160],
    'ux': [160, 211, 240, 180, 160, 160],
    'cloud': [160, 249, 220, 200, 200],
    'bpa': [160, 209, 200, 180, 160, 160],
    'ai': [156, 160, 200, 180, 160, 160],
}
# Same for mobile (tools: design/tools/figma_pt_m.py)
PT_M = {
    'services': [None, 64, 128, 128, 64, 128, 128],
    'web': [204, 44, 108, 128, 64, 128, 128],
    'mobileapp': [184, 128, 128, 64, 128, 128],
    'ux': [204, 64, 128, 64, 128, 128],
    'cloud': [172, 128, 64, 128, 128],
    'bpa': [152, 128, 128, 64, 128, 128],
    'ai': [178, 108, 128, 64, 128, 128],
}
# Figma mobile line height of the hero title where it differs from 54px
TITLE_LH_M = {'cloud': 47, 'bpa': 47, 'ai': 47}
# Figma feature card layout where it differs from 12px title gap / text at 176px
CARD_LAYOUT = {
    'mobileapp': {'hk-title-gap': 20, 'hk-text-top': 166},
    'ux': {'hk-title-gap': 20, 'hk-text-top': 196},
    'cloud': {'hk-title-gap': 20},
    'bpa': {'hk-title-gap': 20, 'hk-text-top': 166},
    'ai': {'hk-title-gap': 20, 'hk-text-top': 178},
}
# Figma mobile height of the feature cards
CARD_MH = {'web': 332, 'mobileapp': 320, 'ux': 292, 'cloud': 300, 'bpa': 340, 'ai': 300}

TAIL = ['s_hk_projects', 's_hk_testimonials', 's_hk_cta']


def service_page(key, url, name):
    c = SERVICES[key]
    hero = c['hero']
    cards = [dict(card) for card in c['features']['cards']]
    if key == 'web':
        # Figma sets the last sentence of the first card in bold
        cards[0]['html'] = R.t(cards[0]['text']).replace(
            'Limited scalability means you lose more customers.',
            '<strong>Limited scalability means you lose more customers.</strong>')
    sections = [R.service_hero(hero['title'], hero['sub'], hero['text'], label=hero.get('label'), icons=hero.get('icons', ()),
                               icons_m=hero.get('icons_m', ()))]
    if key in WITH_PARTNERS:
        sections.append('s_hk_partners')
    if key in INTROS:
        sections.append(INTROS[key])
    sections.append(R.features(c['features']['heading'], cards))
    p = c['process']
    sections.append(R.process(p['heading'], p['lead'], p['steps']))
    sections += TAIL
    features_index = next(i for i, s in enumerate(sections) if isinstance(s, str) and 's_hk_features' in s[:80])
    props = {features_index: {'hk-card-mh': CARD_MH[key], **CARD_LAYOUT.get(key, {})}}
    if key in TITLE_LH_M:
        props[0] = {'hk-title-lh-m': TITLE_LH_M[key]}
    return dict(xmlid=f'page_{key}', name=name, url=url, sections=sections, description=hero['text'],
                pt=PT[key], pt_m=PT_M[key], props=props)


def services_page():
    p = SERVICES['services']['process']
    return dict(
        xmlid='page_services', name='Services', url='/services',
        description='IT services and solutions to reduce business expenses.',
        pt=PT['services'], pt_m=PT_M['services'],
        sections=[
            ('s_hk_hero', {
                'Custom Technology That Turns <span class="hk-gradient-text">Big Brands</span> <br/>Into Your Competitors':
                    'IT Services &amp; Solutions To Reduce Business Expenses',
                'Enterprise-grade technology shouldn’t be out of reach for SMBs and startups. At Hekau, we’re changing that with industry-specific, custom IT solutions.':
                    'Hekau turns complex IT solutions into smooth workflows. Our developers can design anything from web and mobile applications to AI solutions and UI/UX designs. Let us take care of the tech while you focus on expanding your business to new heights.',
                '<a href="/contactus" class="hk-btn hk-btn-quote">Quote Us</a>':
                    '<a href="#services" class="hk-btn hk-btn-hero">Check All Services</a>',
            }, 'hk-hero-services'),
            's_hk_partners',
            ('s_hk_services', None, 'hk-services-static'),
            ('s_hk_why', {
                'Why Partner With Hekau?': 'Why Hekau And Not Them?',
                'Unique Tech Solutions': 'Reduce Business Costs',
                'Automating vendor contracts benefits event companies. NGOs can better manage their inventory if their system has an access hierarchy. Hekau customises specific tech features to solve your unique business roadblocks.':
                    'We aren’t interested in offering what you don’t need. We check your business for processes that should be improved and offer services to reduce your long-term business expenses. No add-on fees, no hidden charges.',
                'Growth Without Compromise': 'Long-Term Partners',
                'SMBs and startups shouldn’t have to sacrifice efficiency due to a limited budget. Our customised solutions have the same benefits as enterprise-grade technology— while remaining cost-effective.':
                    'Once a partner, always a partner. Ongoing support is part of all our service packages. But even beyond, you can come to us any time with any tech hocus pocus you don’t understand.',
                'Cost-Effective and Reliable': 'Your Business, Your Solutions',
                'What you’re quoted is what you pay. We don’t burden you with unnecessary costs or unexpected add-ons. With failsafe mechanisms and periodic maintenance, we ensure your business reaches new heights long after our initial agreement.':
                    'Every industry faces challenges, but they amplify when you’re a small business or a startup. Hekau builds technology solutions molded to your specific business troubles, so you can compete with the giants in your niche.',
            }, None, True),
            R.process(p['heading'], p['lead'], p['steps']),
        ] + TAIL,
    )


# --------------------------------------------------------------------------------
# About Us, Projects and the case study
# --------------------------------------------------------------------------------

def about_page():
    c = ABOUT
    story = c['story']
    return dict(
        xmlid='page_about', name='About Us', url='/about-us',
        description='Hekau builds custom, innovative and industry-specific technology for startups and small businesses.',
        grid_top=0, grid_height=1708,
        sections=[
            R.page_hero(c['hero']['badge'], c['hero']['title'], c['hero']['text'], 'about/hero_icon.webp', (357, 378), 'about'),
            R.highlight(story['title'], story['button'], [], text=story['text'], title_xl=True, note=False,
                        extra='hk-highlight-banner'),
            R.team(c['team']['title'], c['team']['members']),
            R.vision(c['vision']['title'], c['vision']['items']),
            R.features(c['values']['heading'], [dict(card, icon_dir='icons') for card in c['values']['cards']],
                       extra='hk-features-values', heading_cls='hk-h2 hk-h2-sm hk-h2-bold'),
            's_hk_testimonials', 's_hk_cta',
        ],
        pt=[220, 120, 120, 120, 120, 120],
        pt_m=[128, 64, 44, 128, 128, 128],  # values: --hk-off-m of the features block is 20
        props={4: {'hk-card-h': 320, 'hk-text-top': 151, 'hk-title-gap': 20, 'hk-card-mh': 264}},
    )


def projects_page():
    c = WORK
    return dict(
        xmlid='page_projects', name='Projects', url='/projects',
        description='Hekau projects: web and mobile applications, UX/UI design, cloud, automation and AI solutions.',
        sections=[
            R.page_hero(c['hero']['badge'], c['hero']['title'], c['hero']['text'], 'about/squares.svg', (456, 456), 'work'),
            R.project_list(c['list_title'], WORK_FILTERS, c['projects']),
            's_hk_projects', 's_hk_cta',
        ],
        pt=[160, 160, 160],
        pt_m=[64, 128, 128],
    )


def case_page():
    c = CASE
    figure = lambda: R.case_figure('projects/placeholder.webp', c['caption'])  # noqa: E731
    return dict(
        xmlid='page_project_the_arc', name='The Arc', url='/projects/the-arc',
        description='Bringing order to speed: web development for The Arc, a seed-funded new-media startup.',
        grid_top=1409, grid_height=1800,
        sections=[
            R.case_hero(c['title'], c['image'], c['meta']),
            R.case_text(c['intro'], eyebrow=c['eyebrow']),
            figure(), figure(),
            R.case_text(c['outro']),
            figure(), figure(),
            's_hk_projects', 's_hk_cta',
        ],
        pt=[80, 60, 60, 60, 60, 60, 160, 160],
        pt_m=[32, 32, 32, 32, 32, 32, 128, 128],
    )


HOME = ['s_hk_hero', 's_hk_partners', 's_hk_why', 's_hk_stats', 's_hk_services',
        's_hk_domains', 's_hk_projects', 's_hk_testimonials', 's_hk_cta']


def block_templates():
    web = SERVICES['web']
    write_block_template('s_hk_service_hero', 'Hekau Service Hero',
                         'Service page hero (Figma "Frame 1686557875"): eyebrow, gold title, subtitle,\n         text and call to action over the animated hero art.',
                         R.service_hero(web['hero']['title'], web['hero']['sub'], web['hero']['text'], icons=web['hero']['icons']))
    write_block_template('s_hk_highlight', 'Hekau Highlight',
                         'Highlight panel (Figma "Frame 1686557851"): statement, call to action, note\n         and four tiles.', INTROS['mobileapp'])
    write_block_template('s_hk_features', 'Hekau Features',
                         'Feature cards (Figma "Frame 1594"): heading and 340x360 cards.',
                         R.features(web['features']['heading'], web['features']['cards']))
    write_block_template('s_hk_process', 'Hekau Process',
                         'Process timeline (Figma "Desktop - 5"): sticky heading, numbered steps\n         that light up as they scroll into view.',
                         R.process(web['process']['heading'], web['process']['lead'], web['process']['steps']))
    write_block_template('s_hk_attributes', 'Hekau Attributes',
                         'Core attributes (Figma "Frame 7829"): ring diagram leading to a list.', INTROS['web'])
    write_block_template('s_hk_ai_intro', 'Hekau Pyramid Intro',
                         'Intro panel (Figma AI page "Frame 7829"): statement and pyramid of points.', INTROS['ai'])
    a = about_page()['sections']
    write_block_template('s_hk_page_hero', 'Hekau Page Intro',
                         'Page intro (Figma About Us "Frame 1589", Projects "Frame 1686558532"): badge,\n         title and text next to an illustration.', a[0])
    write_block_template('s_hk_team', 'Hekau Team',
                         'Team cards (Figma About Us "Frame 1594"): photo and bio of each member.', a[2])
    write_block_template('s_hk_vision', 'Hekau Vision',
                         'Vision and mission (Figma About Us "Frame 5016"): squares art and stacked cards.', a[3])
    write_block_template('s_hk_project_list', 'Hekau Project List',
                         'Project list (Figma Projects "Frame 1686558536"): category filter and large\n         project cards.', projects_page()['sections'][1])
    cs = case_page()['sections']
    write_block_template('s_hk_case_hero', 'Hekau Case Hero',
                         'Case study hero (Figma "Frame 1686557860"): title, cover image and project facts.', cs[0])
    write_block_template('s_hk_case_text', 'Hekau Case Text',
                         'Case study text (Figma "Frame 15"): optional eyebrow, titled paragraphs.', cs[1])
    write_block_template('s_hk_case_figure', 'Hekau Case Image',
                         'Case study image (Figma "Frame 1686557868"): rounded picture and caption.', cs[2])


if __name__ == '__main__':
    block_templates()
    write_homepage('views/homepage.xml',
                   'Home page: Figma "Home Page" (desktop 1440px, mobile 390px), made of\n         the Hekau blocks. GENERATED by scripts/build_pages.py: edit the blocks\n         or the script, then rerun it.',
                   HOME)
    write_pages('views/pages/services.xml',
                'Services and the six service pages (Figma Dev Handoff). GENERATED by\n         scripts/build_pages.py from scripts/hk_content.py.',
                [services_page()] + [service_page(*p) for p in SERVICE_PAGES])
    write_pages('views/pages/about.xml',
                'About Us (Figma Dev Handoff "About Us Page"). GENERATED by scripts/build_pages.py\n         from scripts/hk_content.py.',
                [about_page()])
    write_pages('views/pages/projects.xml',
                'Projects list and the sample case study (Figma "Project Page" and "Individual\n         Project Page"). GENERATED by scripts/build_pages.py from scripts/hk_content.py.',
                [projects_page(), case_page()])

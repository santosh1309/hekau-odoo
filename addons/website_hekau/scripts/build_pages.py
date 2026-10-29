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
from hk_content import (  # noqa: E402
    ABOUT, BOOKING, CALENDLY_URL, CASE_BY_SLUG, CASES, CHECKLIST_LINK, CHECKLIST_URL, COMPANY, CONTACT, CTA,
    ENGAGEMENT_PROCESS, FEATURED,
    HOW, LAST_UPDATED, PRIVACY, SERVICE_CHOICES, SERVICES, TERMS, THANKS, WORK, WORK_FILTERS,
)

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


def with_spacing(sections, pt=None, pt_m=None, props=None):
    """pt / pt_m: Figma desktop / mobile spacing of each section after the first
    one; props: extra custom properties per section index."""
    if not (pt or pt_m or props):
        return sections
    n = len(sections)
    pt = list(pt or []) + [None] * n
    pt_m = list(pt_m or []) + [None] * n
    first = (props or {}).get(0)
    out = [(sections[0], first) if first else sections[0]]
    for i, s in enumerate(sections[1:]):
        values = {'hk-pt': pt[i], 'hk-pt-m': pt_m[i]}
        values.update((props or {}).get(i + 1, {}))
        out.append((s, values))
    return out


def wrap_style(grid_top=900, grid_height=None):
    style_props = (f'--hk-grid-top: {grid_top}px;' if grid_top != 900 else '') + \
        (f' --hk-grid-height: {grid_height}px;' if grid_height else '')
    return f' style="{style_props.strip()}"' if style_props else ''


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


def menu_attr(menu):
    """data-hk-menu: the main menu item to highlight on a page below it
    (static/src/js/menu_active.js)."""
    return f' data-hk-menu="{menu}"' if menu else ''


def page_xml(xmlid, name, url, sections, description='', grid_top=900, pt=None, pt_m=None, props=None,
             grid_height=None, indexed=True, menu=None):
    sections = with_spacing(sections, pt, pt_m, props)
    body = '\n'.join(indent(render(s), 16) for s in sections)
    index = '' if indexed else '\n        <field name="website_indexed" eval="False"/>'
    return f'''    <template id="{xmlid}" name="{R.a(name)}">
        <t t-call="website.layout">
            <div id="wrap" class="oe_structure hk-page"{wrap_style(grid_top, grid_height)}{menu_attr(menu)}>
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
        <field name="website_meta_description">{R.t(description)}</field>{index}
    </record>'''


def inherit_xml(xmlid, name, sections, inherit_ref=None, inherit_key=None, priority=16, pt=None, pt_m=None,
                grid_top=900, grid_height=None, menu=None):
    """Replace the content (div#wrap) of a page that Odoo owns (/contactus,
    /contactus-thank-you, /privacy)."""
    sections = with_spacing(sections, pt, pt_m)
    body = '\n'.join(indent(render(s), 16) for s in sections)
    arch = f'''<xpath expr="//div[@id='wrap']" position="replace">
            <div id="wrap" class="oe_structure hk-page"{wrap_style(grid_top, grid_height)}{menu_attr(menu)}>
{body}
            </div>
        </xpath>'''
    if inherit_ref:
        return f'''    <template id="{xmlid}" inherit_id="{inherit_ref}" name="{name}" priority="{priority}">
        {arch}
    </template>'''
    # website.page records with an inline arch (the thank-you page): their xml id
    # is the page's, so the view is found by key.
    return f'''    <record id="{xmlid}" model="ir.ui.view">
        <field name="name">{name}</field>
        <field name="type">qweb</field>
        <field name="inherit_id" search="[('key', '=', '{inherit_key}'), ('website_id', '=', False)]"/>
        <field name="priority">{priority}</field>
        <field name="arch" type="xml">
            <data>
        {arch}
            </data>
        </field>
    </record>'''


def write_views(path, comment, chunks):
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<odoo>

    <!-- {comment} -->
{(chr(10) + chr(10)).join(chunks)}

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
# Shared blocks
# --------------------------------------------------------------------------------

def featured_cards(slugs):
    out = []
    for slug in slugs:
        c = CASE_BY_SLUG[slug]
        out.append({'title': c['card_title'], 'text': c['featured_text'], 'url': c['url'], 'image': c['image']})
    return out


def featured(slugs, heading=None, lead=None):
    return R.featured_projects(heading or FEATURED['heading'], lead or FEATURED['lead'], featured_cards(slugs),
                               FEATURED['button'])


def intro(c):
    i = c.get('intro')
    if not i:
        return None
    if i['kind'] == 'highlight':
        icons = any(tile.get('icon') for tile in i['tiles'])
        return R.highlight(i['title'], CTA, i['tiles'], text=i.get('text'), title_xl=icons, note=i.get('note'))
    if i['kind'] == 'attributes':
        return R.attributes(i['badge'], i['title'], i['lead'], i['items'])
    return R.ai_intro(i['badge'], i['title'], i['items'])


# --------------------------------------------------------------------------------
# Services
# --------------------------------------------------------------------------------

SERVICE_PAGES = [
    # key, url, page name (order of the services grid)
    ('odoo', '/erp-crm-implementation', 'ERP, CRM & CMS Implementation'),
    ('bpa', '/business-process-automation', 'Workflow & Process Automation'),
    ('web', '/web-application-development', 'Custom Web Applications & B2B Portals'),
    ('ai', '/ai-solutions', 'Secure In-House AI & Data'),
    ('mobileapp', '/mobile-application-development', 'Mobile App Development'),
    ('ux', '/ux-ui-design', 'UX & Conversion-Focused Websites'),
    ('cloud', '/cloud-managed-services', 'Cloud-Managed Services'),
    ('rescue', '/project-rescue', 'Project Rescue & Dedicated Developers'),
]

# Pages where the partners strip follows the hero (Figma)
WITH_PARTNERS = {'web', 'ux'}

# Figma desktop spacing (padding-top) of each section after the hero, in page
# order (tools: design/tools/figma_gaps.py). None keeps the block's default.
# The new pages reuse the spacing of the page with the same blocks.
PT = {
    'services': [None, 200, 200, 200, 280, 140, 160],
    'web': [160, 129, 150, 180, 160, 140, 140],
    'mobileapp': [160, 219, 160, 180, 160, 160],
    'ux': [160, 211, 240, 180, 160, 160],
    'cloud': [160, 249, 220, 200, 200],
    'bpa': [160, 209, 200, 180, 160, 160],
    'odoo': [160, 209, 160, 180, 180, 160, 160],  # + preferred platform after the features
    'ai': [156, 160, 200, 180, 160, 160],
    'rescue': [160, 150, 180, 160, 140, 140],
}
# Same for mobile (tools: design/tools/figma_pt_m.py)
PT_M = {
    'services': [None, 64, 128, 128, 64, 128, 128],
    'web': [204, 44, 108, 128, 64, 128, 128],
    'mobileapp': [184, 128, 128, 64, 128, 128],
    'ux': [204, 64, 128, 64, 128, 128],
    'cloud': [172, 128, 64, 128, 128],
    'bpa': [152, 128, 128, 64, 128, 128],
    'odoo': [152, 128, 128, 128, 128, 128, 128],
    'ai': [178, 108, 128, 64, 128, 128],
    'rescue': [184, 108, 128, 64, 128, 128],
}

TAIL = ['s_hk_testimonials', 's_hk_cta']


def service_page(key, url, name):
    c = SERVICES[key]
    hero = c['hero']
    sections = [R.service_hero(hero['title'], hero['sub'], hero['text'], label=hero.get('label'),
                               icons=hero.get('icons', ()))]
    if key in WITH_PARTNERS:
        sections.append('s_hk_partners')
    panel = intro(c)
    if panel:
        sections.append(panel)
    sections.append(R.features(c['features']['heading'], c['features']['cards']))
    if c.get('preferred'):
        pref = c['preferred']
        sections.append(R.attributes(pref['badge'], pref['title'], pref['lead'], pref['items']))
    p = c['process']
    sections.append(R.process(p['heading'], p['lead'], p['steps']))
    sections.append(featured(c['featured']))
    sections += TAIL
    props = {}
    if panel and c['intro'].get('note_top'):
        props[sections.index(panel)] = {'hk-note-top': c['intro']['note_top']}
    return dict(xmlid=f'page_{key}', name=name, url=url, sections=sections, description=hero['text'],
                pt=PT[key], pt_m=PT_M[key], props=props, menu='/services')


def services_page():
    c = SERVICES['services']
    hero, why, p = c['hero'], c['why'], c['process']
    home_why = [
        ('We start with the business, not the software',
         'Before we suggest a tool, we map how work actually moves through your company: who waits on whom, where the spreadsheets live, which numbers nobody trusts. Sometimes the fix is an ERP. Sometimes it’s one automation.'),
        ('One system, one version of the truth',
         'We connect sales, operations, inventory and finance so every team works from the same numbers. Odoo where it fits, custom software where it doesn’t, and integrations that keep the two in sync.'),
        ('Accountable long after launch',
         'Your team has to actually use what we build. We train them, stay on for support, and measure success by the friction we remove, not the features we ship. What you’re quoted is what you pay.'),
    ]
    why_replace = {'Why growing companies choose Hekau': R.t(why['heading'])}
    for (old_title, old_text), (new_title, new_text) in zip(home_why, why['cards']):
        why_replace[R.t(old_title)] = R.t(new_title)
        why_replace[R.t(old_text)] = R.t(new_text)
    return dict(
        xmlid='page_services', name='Services', url='/services',
        description='ERP and CRM on Odoo, workflow automation, custom portals, private AI, mobile apps, websites, '
                    'cloud and project rescue for growing companies.',
        pt=PT['services'], pt_m=PT_M['services'],
        sections=[
            ('s_hk_hero', {
                'Fix the <span class="hk-gradient-text">fragmented systems</span> <br/>slowing down your growth': hero['title'],
                'Most $2M–$15M companies don’t have a software problem. They have a fragmented systems problem. We connect your ERP, CRM, workflows and data, so decisions run on today’s numbers, not last week’s spreadsheet.':
                    R.t(hero['text']),
                '<a href="/book-a-call" class="hk-btn hk-btn-quote">Book a free systems audit</a>':
                    f'<a href="{hero["button"][1]}" class="hk-btn hk-btn-hero">{R.t(hero["button"][0])}</a>',
                f'\n        <a href="{CHECKLIST_URL}" class="hk-hero-link" download="">{R.t(CHECKLIST_LINK)}</a>': '',
            }, 'hk-hero-services'),
            's_hk_partners',
            ('s_hk_services', None, 'hk-services-static'),
            ('s_hk_why', why_replace, None, True),
            R.process(p['heading'], p['lead'], p['steps']),
            featured(c['featured']),
        ] + TAIL,
    )


# --------------------------------------------------------------------------------
# About Us, Projects, case studies, How we work
# --------------------------------------------------------------------------------

def about_page():
    c = ABOUT
    story = c['story']
    return dict(
        xmlid='page_about', name='About Us', url='/about-us', description=c['description'],
        grid_top=0, grid_height=1708,
        sections=[
            R.page_hero(c['hero']['badge'], c['hero']['title'], c['hero']['text'], 'about/hero_icon.webp', (357, 378), 'about'),
            R.highlight(story['title'], story['button'], [], text=story['text'], title_xl=True, note=None,
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


def project_cards():
    return [{'categories': c['categories'], 'title': c['card_title'], 'url': c['url'], 'image': c['image'],
             'tags': c['tags'], 'text': c['card_text']} for c in CASES]


def projects_page():
    c = WORK
    return dict(
        xmlid='page_projects', name='Projects', url='/projects', description=c['description'],
        sections=[
            R.page_hero(c['hero']['badge'], c['hero']['title'], c['hero']['text'], 'about/squares.svg', (456, 456), 'work'),
            R.project_list(c['list_title'], WORK_FILTERS, project_cards()),
            's_hk_testimonials', 's_hk_cta',
        ],
        pt=[160, 160, 160],
        pt_m=[64, 128, 128],
    )


def case_page(c):
    xmlid = 'page_project_' + c['slug'].replace('-', '_')
    return dict(
        xmlid=xmlid, name=f'Project: {c["card_title"]}', url=c['url'],
        description=f'{c["card_title"]}. {c["card_text"]}',
        grid_top=1409, grid_height=1800,
        sections=[
            R.case_hero(c['card_title'], c['image'],
                        [('Service', c['service']), ('Client', c['client']), ('Industry', c['industry'])]),
            R.case_text([{'title': 'About the client', 'text': c['about']},
                         {'title': 'The challenge', 'text': c['challenge']}], eyebrow='Project details'),
            R.case_figure(c['quote_image'], None, alt=c['quote'], natural=True, size=(1840, 1124)),
            R.case_text([{'title': 'What we built', 'text': c['built']},
                         {'title': 'The impact', 'text': c['impact']}]),
            featured(c['related'], heading='More work like this', lead='Related projects from our portfolio.'),
            's_hk_cta',
        ],
        pt=[80, 60, 60, 160, 160],
        pt_m=[32, 32, 32, 128, 128],
    )


def how_page():
    c = HOW
    p = ENGAGEMENT_PROCESS
    return dict(
        xmlid='page_how_we_work', name='How We Work', url='/how-we-work', description=c['description'],
        sections=[
            R.page_hero(c['hero']['badge'], c['hero']['title'], c['hero']['text'], 'about/squares.svg', (456, 456), 'work'),
            R.features(c['models']['heading'], c['models']['cards']),
            R.attributes(c['audit']['badge'], c['audit']['title'], c['audit']['lead'], c['audit']['items']),
            R.process(p['heading'], p['lead'], p['steps']),
            R.case_text(c['faq'], heading=c['faq_title']),
            's_hk_cta',
        ],
        pt=[160, 160, 180, 160, 160],
        pt_m=[64, 128, 128, 128, 128],
    )


def legal_sections(doc):
    return [
        R.service_hero(doc['title'], LAST_UPDATED, doc['text'], label='Legal', button=None),
        R.case_text(doc['groups'], small=True),
    ]


def booking_page():
    c = BOOKING
    return dict(
        xmlid='page_book_a_call', name='Book a Call', url='/book-a-call', description=c['description'],
        sections=[
            R.service_hero(c['title'], c['sub'], c['text'], label=c['label'], button=None),
            R.booking(c['heading'], c['lead'], CALENDLY_URL),
            's_hk_testimonials',
        ],
        pt=[60, 160], pt_m=[40, 128],
    )


def terms_page():
    return dict(
        xmlid='page_terms', name='Terms and Conditions', url='/terms-and-conditions',
        description='Terms and conditions for using the Hekau Business Solutions website.',
        sections=legal_sections(TERMS), pt=[40], pt_m=[24],
    )


# --------------------------------------------------------------------------------
# Pages Odoo owns: contact, thank-you, privacy
# --------------------------------------------------------------------------------

def odoo_pages():
    contact = inherit_xml(
        'contactus_hekau', 'Hekau Contact Us',
        [R.contact(CONTACT, COMPANY, SERVICE_CHOICES), 's_hk_testimonials'],
        inherit_ref='website.contactus', priority=99, pt=[120], pt_m=[96])
    thanks = inherit_xml(
        'contactus_thanks_hekau', 'Hekau Contact Us Thanks',
        [R.service_hero(THANKS['title'], None, THANKS['text'], label='Message received', button=None,
                        link=THANKS['link'], link_download=True),
         R.booking(THANKS['booking_heading'], THANKS['booking_lead'], CALENDLY_URL),
         featured(SERVICES['services']['featured'])],
        inherit_key='website.contactus_thanks', priority=99, pt=[60, 160], pt_m=[40, 128], menu='/contactus')
    privacy = inherit_xml(
        'privacy_policy_hekau', 'Hekau Privacy Policy', legal_sections(PRIVACY),
        inherit_ref='website.privacy_policy', priority=99, pt=[40], pt_m=[24])
    return [contact, thanks, privacy]


HOME = ['s_hk_hero', 's_hk_partners', 's_hk_why', 's_hk_stats', 's_hk_services',
        's_hk_domains', 's_hk_projects', 's_hk_testimonials', 's_hk_cta']


def block_templates():
    odoo = SERVICES['odoo']
    web = SERVICES['web']
    write_block_template('s_hk_service_hero', 'Hekau Service Hero',
                         'Service page hero (Figma "Frame 1686557875"): eyebrow, gold title, subtitle,\n         text and call to action over the animated hero art.',
                         R.service_hero(odoo['hero']['title'], odoo['hero']['sub'], odoo['hero']['text'], label=odoo['hero']['label']))
    write_block_template('s_hk_highlight', 'Hekau Highlight',
                         'Highlight panel (Figma "Frame 1686557851"): statement, call to action, note\n         and four tiles.', intro(SERVICES['mobileapp']))
    write_block_template('s_hk_features', 'Hekau Features',
                         'Feature cards (Figma "Frame 1594"): heading and 340x360 cards.',
                         R.features(odoo['features']['heading'], odoo['features']['cards']))
    write_block_template('s_hk_process', 'Hekau Process',
                         'Process timeline (Figma "Desktop - 5"): sticky heading, numbered steps\n         that light up as they scroll into view.',
                         R.process(ENGAGEMENT_PROCESS['heading'], ENGAGEMENT_PROCESS['lead'], ENGAGEMENT_PROCESS['steps']))
    write_block_template('s_hk_attributes', 'Hekau Attributes',
                         'Core attributes (Figma "Frame 7829"): ring diagram leading to a list.', intro(web))
    write_block_template('s_hk_ai_intro', 'Hekau Pyramid Intro',
                         'Intro panel (Figma AI page "Frame 7829"): statement and pyramid of points.', intro(SERVICES['ai']))
    write_block_template('s_hk_projects', 'Hekau Projects',
                         'Featured projects (Figma "Frame 1565"): two case study cards. On mobile the\n         "View all projects" button moves below the cards and spans the full width.',
                         featured(SERVICES['services']['featured']))
    a = about_page()['sections']
    write_block_template('s_hk_page_hero', 'Hekau Page Intro',
                         'Page intro (Figma About Us "Frame 1589", Projects "Frame 1686558532"): badge,\n         title and text next to an illustration.', a[0])
    write_block_template('s_hk_team', 'Hekau Team',
                         'Team cards (Figma About Us "Frame 1594"): photo and bio of each member.', a[2])
    write_block_template('s_hk_vision', 'Hekau Vision',
                         'Vision and mission (Figma About Us "Frame 5016"): squares art and stacked cards.', a[3])
    write_block_template('s_hk_project_list', 'Hekau Project List',
                         'Project list (Figma Projects "Frame 1686558536"): category filter and large\n         project cards.', projects_page()['sections'][1])
    cs = case_page(CASE_BY_SLUG['the-arc'])['sections']
    write_block_template('s_hk_case_hero', 'Hekau Case Hero',
                         'Case study hero (Figma "Frame 1686557860"): title, cover image and project facts.', cs[0])
    write_block_template('s_hk_case_text', 'Hekau Case Text',
                         'Case study text (Figma "Frame 15"): optional eyebrow, titled paragraphs.', cs[1])
    write_block_template('s_hk_case_figure', 'Hekau Case Image',
                         'Case study image (Figma "Frame 1686557868"): rounded picture and caption.',
                         R.case_figure('projects/the_arc.webp', 'A caption for the picture.'))


if __name__ == '__main__':
    block_templates()
    write_homepage('views/homepage.xml',
                   'Home page: Figma "Home Page" (desktop 1440px, mobile 390px), made of\n         the Hekau blocks. GENERATED by scripts/build_pages.py: edit the blocks\n         or the script, then rerun it.',
                   HOME)
    write_views('views/pages/services.xml',
                'Services and the eight service pages. GENERATED by scripts/build_pages.py\n         from scripts/hk_content.py.',
                [page_xml(**services_page())] + [page_xml(**service_page(*p)) for p in SERVICE_PAGES])
    write_views('views/pages/about.xml',
                'About Us. GENERATED by scripts/build_pages.py from scripts/hk_content.py.',
                [page_xml(**about_page())])
    write_views('views/pages/projects.xml',
                'Projects list and the case studies (/projects/<slug>). GENERATED by\n         scripts/build_pages.py from scripts/hk_content.py.',
                [page_xml(**projects_page())] + [page_xml(**case_page(c)) for c in CASES])
    write_views('views/pages/how_we_work.xml',
                'How we work, Book a call and the terms. GENERATED by scripts/build_pages.py from\n         scripts/hk_content.py.',
                [page_xml(**how_page()), page_xml(**booking_page()), page_xml(**terms_page())])
    write_views('views/pages/odoo_pages.xml',
                'Content of the pages Odoo owns: /contactus (form creating a CRM lead),\n         /contactus-thank-you and /privacy. GENERATED by scripts/build_pages.py.',
                odoo_pages())

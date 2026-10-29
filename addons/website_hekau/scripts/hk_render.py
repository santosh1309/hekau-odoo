"""Markup of the Hekau blocks used by the inner pages.

Each function returns the <section> of one block. build_pages.py uses them to
write the block templates (views/snippets) with default content and the pages
(views/pages) with their own content, so both always share the same markup.
"""
from html import escape

IMG = '/website_hekau/static/src/img'


def t(text):
    """Escape text for XML; keeps the typographic characters as they are."""
    return escape(text, quote=False)


def a(text):
    return escape(text, quote=True)


def section(cls, name, body, sid=None, extra=''):
    sid_attr = f' id="{sid}"' if sid else ''
    return f'<section{sid_attr} class="{cls}{(" " + extra) if extra else ""}" data-name="{name}">\n{body}\n</section>'


def ind(text, n):
    pad = ' ' * n
    return '\n'.join(pad + line if line else line for line in text.split('\n'))


# --- Service hero ---------------------------------------------------------------

CTA = ('Book a free systems audit', '/book-a-call')


def service_hero(title, sub, text, label=None, icons=(), button=CTA, icons_m=(), link=None, download=False,
                 link_download=False):
    """Hero of the inner pages. `sub`, `button` and `link` (text link under the
    button) are optional; `download` / `link_download` mark the button / link
    as a file download."""
    if icons_m:
        # different eyebrow on mobile (Figma Mobile App page: label on desktop, icons on mobile)
        desktop = f'<span class="hk-eyebrow-label hk-only-desktop">{t(label or "Services")}</span>'
        mobile = '<span class="hk-eyebrow-icons hk-only-mobile">' + ''.join(
            f'<img src="{IMG}/tech/{f}.webp" alt="{a(alt)}" width="36" height="36"/>' for f, alt in icons_m) + '</span>'
        middle = desktop + mobile
    elif icons:
        middle = '<span class="hk-eyebrow-icons">' + ''.join(
            f'<img src="{IMG}/tech/{f}.webp" alt="{a(alt)}" width="{size}" height="{size}"/>'
            for f, alt, size in ((i[0], i[1], i[2] if len(i) > 2 else 36) for i in icons)) + '</span>'
    else:
        middle = f'<span class="hk-eyebrow-label">{t(label or "Services")}</span>'
    sub_html = f'\n    <p class="hk-service-sub">{t(sub)}</p>' if sub else ''
    dl = ' download=""' if download else ''
    button_html = f'\n    <a href="{a(button[1])}" class="hk-btn hk-btn-hero"{dl}>{t(button[0])}</a>' if button else ''
    link_dl = ' download=""' if link_download else ''
    link_html = f'\n    <a href="{a(link[1])}" class="hk-hero-link"{link_dl}>{t(link[0])}</a>' if link else ''
    body = f'''<div class="hk-hero-art hk-deco o_not_editable" aria-hidden="true">
    <div class="hk-hero-stage">
        <span class="hk-hero-ellipse"/>
        <span class="hk-hero-panel"/>
    </div>
    <span class="hk-hero-fade"/>
</div>
<div class="hk-container hk-service-hero-content">
    <div class="hk-eyebrow">
        <span class="hk-eyebrow-line hk-deco"/>
        {middle}
        <span class="hk-eyebrow-line hk-eyebrow-line-end hk-deco"/>
    </div>
    <h1 class="hk-service-title"><span class="hk-service-title-text">{t(title)}</span></h1>{sub_html}
    <p class="hk-service-text">{t(text)}</p>{button_html}{link_html}
</div>'''
    return section('s_hk_service_hero', 'Hekau Service Hero', ind(body, 4))


# --- Highlight panel --------------------------------------------------------------

def highlight(title, button, tiles, text=None, title_xl=False, note='Start your journey today.', extra=''):
    """Statement panel with tiles; without tiles and note it is the About Us
    story banner (`extra='hk-highlight-banner'`). `note`: text next to the
    hand-drawn arrow, or None."""
    tiles_html = []
    for tile in tiles:
        if tile.get('icon'):
            top = f'<p class="hk-tile-icon"><img src="{IMG}/icons/{tile["icon"]}.svg" alt="" width="55" height="55"/></p>'
            label_cls = 'hk-tile-label hk-tile-label-lg'
        else:
            small = f'<small>{t(tile["small"])}</small>' if tile.get('small') else ''
            top = f'<p class="hk-tile-value">{t(tile["value"])}{small}</p>'
            label_cls = 'hk-tile-label'
        tiles_html.append(f'''<div class="hk-highlight-tile">
    {top}
    <p class="{label_cls}">{t(tile["label"])}</p>
</div>''')
    text_html = f'\n            <p class="hk-highlight-text">{t(text)}</p>' if text else ''
    note_html = f'\n            <p class="hk-highlight-note"><img class="hk-deco" src="{IMG}/icons/doodle_arrow.svg" alt="" width="60" height="54"/><span>{t(note or "")}</span></p>' if note else ''
    tiles_block = f'''
        <div class="hk-highlight-tiles">
{ind(chr(10).join(tiles_html), 12)}
        </div>''' if tiles else ''
    body = f'''<div class="hk-container hk-container-wide">
    <div class="hk-highlight-panel">
        <div class="hk-highlight-copy">
            <h2 class="hk-highlight-title{' hk-highlight-title-xl' if title_xl else ''}">{t(title)}</h2>{text_html}
            <a href="{a(button[1])}" class="hk-btn hk-btn-primary hk-highlight-btn">{t(button[0])}</a>{note_html}
        </div>{tiles_block}
    </div>
</div>'''
    return section('s_hk_highlight hk-section', 'Hekau Highlight', ind(body, 4), extra=extra)


# --- Features ----------------------------------------------------------------------

def features(heading, cards, sid=None, extra='', heading_cls='hk-h2 hk-h2-sm'):
    cards_html = []
    for c in cards:
        style = f' style="--hk-title-w: {c["title_w"]}px;"' if c.get('title_w') and c['title_w'] != 300 else ''
        text = c.get('html') or t(c['text'])
        cards_html.append(f'''<div class="hk-feature-card">
    <img class="hk-feature-icon" src="{IMG}/{c.get('icon_dir', 'svc')}/{c["icon"]}.svg" alt="" width="44" height="44"/>
    <h3 class="hk-feature-title"{style}>{t(c["title"])}</h3>
    <p class="hk-feature-text">{text}</p>
</div>''')
    body = f'''<div class="hk-container">
    <div class="hk-section-head hk-glow-top">
        <h2 class="{heading_cls}">{t(heading)}</h2>
    </div>
    <div class="hk-feature-grid">
{ind(chr(10).join(cards_html), 8)}
    </div>
</div>'''
    return section('s_hk_features hk-section', 'Hekau Features', ind(body, 4), sid=sid, extra=extra)


# --- Process --------------------------------------------------------------------------

def process(heading, lead, steps):
    items = []
    for i, s in enumerate(steps, 1):
        items.append(f'''<li class="hk-step">
    <span class="hk-step-num">{i}</span>
    <div class="hk-step-card">
        <h3 class="hk-step-title"><img src="{IMG}/icons/{s["icon"]}.svg" alt="" width="36" height="36"/>{t(s["title"])}</h3>
        <p class="hk-step-text">{t(s["text"])}</p>
    </div>
</li>''')
    body = f'''<div class="hk-container">
    <div class="hk-process-row">
        <div class="hk-process-head">
            <h2 class="hk-h2 hk-h2-sm">{t(heading).replace(chr(10), '<br/>')}</h2>
            <p class="hk-process-lead">{t(lead)}</p>
        </div>
        <ol class="hk-steps">
{ind(chr(10).join(items), 12)}
        </ol>
    </div>
</div>'''
    return section('s_hk_process hk-section', 'Hekau Process', ind(body, 4))


# --- Attributes ------------------------------------------------------------------------

def attributes(badge, title, lead, items):
    """Ring diagram leading to the list. The Figma art connects seven items;
    other counts use art drawn by scripts/attributes_art.py."""
    lis = '\n'.join(f'<li>{t(x)}</li>' for x in items)
    art = 'attributes_art.svg' if len(items) == 7 else f'attributes_art_{len(items)}.svg'
    body = f'''<div class="hk-container hk-container-wide">
    <div class="hk-panel hk-attr-panel">
        <div class="hk-attr-head">
            <span class="hk-badge">{t(badge)}</span>
            <h2 class="hk-attr-title">{t(title)}</h2>
        </div>
        <p class="hk-attr-lead">{t(lead)}</p>
        <div class="hk-attr-diagram">
            <img class="hk-attr-art hk-deco" src="{IMG}/svc/{art}" alt="" width="923" height="564"/>
            <img class="hk-attr-rings hk-deco" src="{IMG}/svc/attributes_rings.svg" alt="" width="360" height="360"/>
            <ul class="hk-attr-list">
{ind(lis, 16)}
            </ul>
        </div>
    </div>
</div>'''
    return section('s_hk_attributes hk-section', 'Hekau Attributes', ind(body, 4))


# --- Pyramid intro -------------------------------------------------------------------------

def ai_intro(badge, title, items, button=CTA):
    lis = '\n'.join(f'<li>{t(x)}</li>' for x in items)
    body = f'''<div class="hk-container hk-container-wide">
    <div class="hk-panel hk-intro-panel">
        <div class="hk-intro-head">
            <span class="hk-badge">{t(badge)}</span>
            <h2 class="hk-intro-title">{t(title)}</h2>
        </div>
        <div class="hk-pyramid">
            <img class="hk-pyramid-art hk-deco" src="{IMG}/svc/ai_pyramid.svg" alt="" width="480" height="480"/>
            <ul class="hk-pyramid-list">
{ind(lis, 16)}
            </ul>
        </div>
        <a href="{a(button[1])}" class="hk-btn hk-btn-primary hk-intro-btn">{t(button[0])}</a>
    </div>
</div>'''
    return section('s_hk_ai_intro hk-section', 'Hekau Pyramid Intro', ind(body, 4))


# --- Shared bits ------------------------------------------------------------------------------

HERO_ART = '''<div class="hk-hero-art hk-deco o_not_editable" aria-hidden="true">
    <div class="hk-hero-stage">
        <span class="hk-hero-ellipse"/>
        <span class="hk-hero-panel"/>
    </div>
    <span class="hk-hero-fade"/>
</div>'''


def heading(text, cls='hk-h2 hk-h2-sm hk-h2-bold', lead=None):
    lead_html = f'\n    <p class="hk-lead">{t(lead)}</p>' if lead else ''
    return f'''<div class="hk-section-head hk-glow-top">
    <h2 class="{cls}">{t(text)}</h2>{lead_html}
</div>'''


def paragraphs(text, cls=None):
    attr = f' class="{cls}"' if cls else ''
    return '\n'.join(f'<p{attr}>{t(p.strip())}</p>' for p in text.split('\n\n') if p.strip())


# --- Squares art with the animated logo (Projects, How we work, About) -----------------------------

LOGO_ARM = '<span class="hk-logo-arm-{n}"><span class="hk-logo-stem"/><span class="hk-logo-bar"/></span>'


def squares_art(cls, lazy=True):
    """Figma "Group 7822": nested squares around the "Logo Animation" tile
    (styles in scss/hekau.scss). `cls` sizes it in its block."""
    return f'''<div class="{cls} hk-squares-art hk-deco o_not_editable" aria-hidden="true">
    <img src="{IMG}/about/squares_frame.svg" alt="" width="456" height="456"{' loading="lazy"' if lazy else ''}/>
    <span class="hk-logo-anim">{LOGO_ARM.format(n=1)}{LOGO_ARM.format(n=2)}</span>
</div>'''


# --- Page intro (About Us, Projects) ------------------------------------------------------------

def page_hero(badge, title, text, image, image_size, variant, alt=''):
    """Badge, title and text next to an illustration. variant: 'about' (panel
    and glow, centred on mobile) or 'work' (hero animation, squares art).
    A line break in the title only applies on mobile."""
    art = HERO_ART + '\n' if variant == 'work' else '''<div class="hk-page-hero-bg hk-deco o_not_editable" aria-hidden="true">
    <span class="hk-page-hero-glow"/>
    <span class="hk-page-hero-panel"/>
</div>
<div class="hk-page-hero-mobile-art hk-deco o_not_editable" aria-hidden="true">
''' + ind(HERO_ART, 4) + '\n</div>\n'
    w, h = image_size
    if image == 'about/squares.svg':
        picture = squares_art('hk-page-hero-img', lazy=False)
    else:
        picture = f'<img class="hk-page-hero-img" src="{IMG}/{image}" alt="{a(alt)}" width="{w}" height="{h}"/>'
    body = f'''{art}<div class="hk-container hk-page-hero-row">
    <div class="hk-page-hero-copy">
        <span class="hk-badge">{t(badge)}</span>
        <h1 class="hk-page-hero-title">{t(title).replace(chr(10), ' <br class="hk-only-mobile"/>')}</h1>
        <div class="hk-page-hero-text">
{ind(paragraphs(text), 12)}
        </div>
    </div>
{ind(picture, 4)}
</div>'''
    return section(f's_hk_page_hero hk-page-hero-{variant}', 'Hekau Page Intro', ind(body, 4))


# --- Team ----------------------------------------------------------------------------------------

def team(title, members):
    cards = []
    for m in members:
        cards.append(f'''<article class="hk-member">
    <div class="hk-member-photo">
        <img src="{IMG}/{m["photo"]}" alt="{a(m["name"])}" width="235" height="300" loading="lazy"/>
    </div>
    <div class="hk-member-card">
        <h3 class="hk-member-name">{t(m["name"])}</h3>
        <p class="hk-member-role">{t(m["role"])}</p>
        <p class="hk-member-bio">{t(m["bio"])}</p>
    </div>
</article>''')
    body = f'''<div class="hk-container">
{ind(heading(title, 'hk-h2 hk-h2-sm hk-h2-bold hk-h2-dm'), 4)}
    <div class="hk-team-grid">
{ind(chr(10).join(cards), 8)}
    </div>
</div>'''
    return section('s_hk_team hk-section', 'Hekau Team', ind(body, 4))


# --- Vision / mission -------------------------------------------------------------------------------

def vision(title, items):
    cards = []
    for it in items:
        cards.append(f'''<div class="hk-vision-card">
    <h3 class="hk-vision-title"><img src="{IMG}/icons/{it["icon"]}.svg" alt="" width="40" height="40"/>{t(it["title"])}</h3>
    <p class="hk-vision-text">{t(it["text"])}</p>
</div>''')
    body = f'''<div class="hk-container">
{ind(heading(title, 'hk-h2 hk-h2-sm hk-h2-bold hk-h2-dm'), 4)}
    <div class="hk-vision-row">
{ind(squares_art('hk-vision-art'), 8)}
        <div class="hk-vision-cards">
{ind(chr(10).join(cards), 12)}
        </div>
    </div>
</div>'''
    return section('s_hk_vision hk-section', 'Hekau Vision', ind(body, 4))


# --- Project list -----------------------------------------------------------------------------------

def project_list(title, filters, projects):
    pills = '\n'.join(f'<button type="button" class="hk-filter-pill" data-filter="{a(key)}" aria-pressed="false">{t(label)}</button>'
                      for key, label in filters)
    cards = []
    for p in projects:
        tags = ''.join(f'<span class="hk-badge">{t(x)}</span>' for x in p['tags'])
        categories = ' '.join(p['categories']) if 'categories' in p else p['category']
        cards.append(f'''<article class="hk-work-card" data-category="{a(categories)}">
    <a href="{a(p["url"])}" class="hk-work-media"><img src="{IMG}/{p["image"]}" alt="{a(p["title"])}" width="1080" height="560" loading="lazy"/></a>
    <div class="hk-work-info">
        <div class="hk-work-tags">{tags}</div>
        <div class="hk-work-body">
            <h3 class="hk-work-title"><a href="{a(p["url"])}">{t(p["title"])}</a></h3>
            <p class="hk-work-text">{t(p["text"])}</p>
        </div>
    </div>
</article>''')
    body = f'''<div class="hk-container hk-container-work">
{ind(heading(title, 'hk-h2 hk-h2-sm hk-h2-bold hk-h2-dm'), 4)}
    <div class="hk-filters" role="group" aria-label="Filter projects">
        <span class="hk-filter-icon"><img src="{IMG}/icons/filter.svg" alt="" width="20" height="20"/></span>
        <span class="hk-filter-label">Filter:</span>
{ind(pills, 8)}
    </div>
    <div class="hk-work-list">
{ind(chr(10).join(cards), 8)}
    </div>
</div>'''
    return section('s_hk_project_list hk-section', 'Hekau Project List', ind(body, 4))


# --- Case study --------------------------------------------------------------------------------------

def case_hero(title, image, meta):
    items = '\n'.join(f'''<div class="hk-case-meta-item">
    <span class="hk-badge">{t(k)}</span>
    <p class="hk-case-meta-value">{t(v)}</p>
</div>''' for k, v in meta)
    body = f'''{HERO_ART}
<div class="hk-container hk-container-case">
    <h1 class="hk-case-title">{t(title)}</h1>
    <div class="hk-case-cover">
        <img src="{IMG}/{image}" alt="{a(title)}" width="1226" height="749"/>
    </div>
    <div class="hk-case-meta">
{ind(items, 8)}
    </div>
</div>'''
    return section('s_hk_case_hero', 'Hekau Case Hero', ind(body, 4))


def case_text(groups, eyebrow=None, heading=None, small=False):
    """Titled paragraphs. `heading`: section title above them (FAQ, legal
    pages); `small`: smaller group titles (h3) for long documents."""
    parts = []
    tag = 'h3' if heading else 'h2'
    for g in groups:
        parts.append(f'''<div class="hk-case-group">
    <{tag} class="hk-case-h2{' hk-case-h2-sm' if small else ''}">{t(g["title"])}</{tag}>
{ind(paragraphs(g["text"]), 4)}
</div>''')
    eyebrow_html = f'\n    <p class="hk-case-eyebrow">{t(eyebrow)}</p>' if eyebrow else ''
    heading_html = f'\n    <h2 class="hk-h2 hk-h2-sm hk-h2-bold hk-case-heading">{t(heading)}</h2>' if heading else ''
    body = f'''<div class="hk-container hk-container-case hk-case-text">{eyebrow_html}{heading_html}
{ind(chr(10).join(parts), 4)}
</div>'''
    return section('s_hk_case_text hk-section', 'Hekau Case Text', ind(body, 4))


def case_figure(image, caption, alt='', natural=False, size=(1226, 685)):
    """Rounded picture and caption. `natural`: keep the image's own ratio on
    every screen (pictures with text, such as the pull-quote cards)."""
    cls = 'hk-case-figure hk-case-figure-natural' if natural else 'hk-case-figure'
    caption_html = f'\n        <figcaption>{t(caption)}</figcaption>' if caption else ''
    body = f'''<div class="hk-container hk-container-case">
    <figure class="{cls}">
        <img src="{IMG}/{image}" alt="{a(alt)}" width="{size[0]}" height="{size[1]}" loading="lazy"/>{caption_html}
    </figure>
</div>'''
    return section('s_hk_case_figure hk-section', 'Hekau Case Image', ind(body, 4))


# --- Featured projects ("Proof, not promises") ----------------------------------------------------

def featured_projects(heading, lead, projects, button=('View all projects', '/projects')):
    """Same markup as the hand-written Home block (views/snippets/s_hk_projects.xml).
    projects: dicts with title, text, url and image."""
    cards = []
    for p in projects:
        cards.append(f'''<article class="hk-project-card">
    <a href="{a(p["url"])}" class="hk-project-media"><img class="hk-project-img" src="{IMG}/{p["image"]}" alt="{a(p["title"])}" width="440" height="220" loading="lazy"/></a>
    <div class="hk-project-body">
        <div>
            <h3><a href="{a(p["url"])}">{t(p["title"])}</a></h3>
            <p>{t(p["text"])}</p>
        </div>
        <a href="{a(p["url"])}" class="hk-arrow-btn" aria-label="Read the case study"><img src="{IMG}/icons/arrow_right_21.svg" alt="" width="21" height="21"/></a>
    </div>
</article>''')
    body = f'''<div class="hk-container hk-container-narrow">
    <div class="hk-projects-head hk-glow-top">
        <div>
            <h2 class="hk-h2">{t(heading)}</h2>
            <p class="hk-lead">{t(lead)}</p>
        </div>
        <a href="{a(button[1])}" class="hk-btn hk-btn-primary hk-only-desktop">{t(button[0])}</a>
    </div>
    <div class="hk-projects-grid">
{ind(chr(10).join(cards), 8)}
    </div>
    <a href="{a(button[1])}" class="hk-btn hk-btn-primary hk-projects-all hk-only-mobile">{t(button[0])}</a>
</div>'''
    return section('s_hk_projects hk-section', 'Hekau Projects', ind(body, 4), sid='projects')


# --- Contact page (form creating a CRM lead) --------------------------------------------------------

# Fields follow the markup of Odoo's website form fields (label on top): every
# field has a .s_website_form_label with a .s_website_form_label_content, which
# the website builder's field options read.

def _field(fid, label, control, required=False, custom=False, model_required=False, cls='', ftype='char'):
    classes = ['s_website_form_field', 'hk-form-field']
    if custom:
        classes.append('s_website_form_custom')
    if required:
        classes.append('s_website_form_required')
    if model_required:
        classes.append('s_website_form_model_required')
    if cls:
        classes.append(cls)
    mark = '<span class="s_website_form_mark"> *</span>' if required or model_required else ''
    return f'''<div class="{' '.join(classes)}" data-type="{ftype}" data-name="Field">
    <label class="s_website_form_label" for="{fid}"><span class="s_website_form_label_content">{t(label)}</span>{mark}</label>
    {control}
</div>'''


def _check(fid, name, text_html, required=False):
    """Checkbox (Odoo "boolean" custom field); the label text sits after the box."""
    classes = 's_website_form_field s_website_form_custom hk-form-field hk-form-check'
    if required:
        classes += ' s_website_form_required'
    req = ' required=""' if required else ''
    mark = '<span class="s_website_form_mark"> *</span>' if required else ''
    return f'''<div class="{classes}" data-type="boolean" data-name="Field">
    <label class="s_website_form_label" for="{fid}"><span class="s_website_form_label_content">{text_html}</span>{mark}</label>
    <input id="{fid}" type="checkbox" value="Yes" class="s_website_form_input form-check-input" name="{a(name)}"{req}/>
</div>'''


def _select(fid, name, options, required=False, placeholder='Choose one'):
    """Drop-down list (Odoo "many2one" custom field) with a placeholder option."""
    req = ' required=""' if required else ''
    opts = ([f'<option value="" class="s_website_form_empty_option">{t(placeholder)}</option>']
            + [f'<option value="{a(o)}">{t(o)}</option>' for o in options])
    return (f'<select id="{fid}" class="form-select s_website_form_input" name="{a(name)}"{req}>'
            + ''.join(opts) + '</select>')


def contact(c, company, services):
    """Contact page: intro, contact details and the audit request form. The form
    posts to Odoo's website form controller and creates a crm.lead; answers
    that have no lead field (revenue, service, source, consents) are added to
    the lead's description."""
    fields = [
        _field('hk_contact_name', 'Name', '<input id="hk_contact_name" type="text" class="form-control s_website_form_input" name="contact_name" required="" autocomplete="name" data-fill-with="name"/>', required=True),
        _field('hk_email', 'Work email', '<input id="hk_email" type="email" class="form-control s_website_form_input" name="email_from" required="" autocomplete="email" data-fill-with="email"/>', required=True, ftype='email'),
        _field('hk_phone', 'Phone', '<input id="hk_phone" type="tel" class="form-control s_website_form_input" name="phone" autocomplete="tel" data-fill-with="phone"/>', ftype='tel'),
        _field('hk_company', 'Company', '<input id="hk_company" type="text" class="form-control s_website_form_input" name="partner_name" required="" autocomplete="organization" data-fill-with="commercial_company_name"/>', required=True),
        _field('hk_revenue', 'Annual revenue', _select('hk_revenue', 'Annual revenue', c['revenue']), custom=True, ftype='many2one'),
        _field('hk_service', 'What do you need help with?', _select('hk_service', 'Service needed', services, required=True), required=True, custom=True, ftype='many2one'),
        _field('hk_description', 'What’s slowing your business down?', '<textarea id="hk_description" class="form-control s_website_form_input" name="description" required="" rows="5"></textarea>', required=True, cls='hk-form-wide', ftype='text'),
        _field('hk_source', 'How did you hear about us?', _select('hk_source', 'Heard about us via', c['sources']), custom=True, cls='hk-form-wide', ftype='many2one'),
        _check('hk_consent', 'Contact consent', t(c['consent']).replace('the privacy policy', '<a href="/privacy">the privacy policy</a>'), required=True),
        _check('hk_newsletter', 'Newsletter opt-in', t(c['newsletter'])),
    ]
    hidden = f'''<div class="s_website_form_field s_website_form_dnone" data-type="char" data-name="Field">
    <label class="s_website_form_label"><span class="s_website_form_label_content">Lead title</span></label>
    <input type="hidden" class="form-control s_website_form_input" name="name" value="{a(c['lead_name'])}"/>
</div>'''
    phone_link = f'<a href="tel:{company["phone_href"]}">{t(company["phone"])}</a>'
    details = f'''<ul class="hk-contact-details">
    <li><span>Email</span><a href="mailto:{company["email"]}">{t(company["email"])}</a></li>
    <li><span>Phone</span>{phone_link}</li>
    <li><span>Office</span>{t(company["address"])}</li>
    <li><span>LinkedIn</span><a href="{a(company["linkedin"])}" target="_blank" rel="noopener">Hekau Business Solutions</a></li>
</ul>'''
    aside = (f'Rather pick a time now? <a href="{a(c["booking_link"][1])}">{t(c["booking_link"][0])}</a>. '
             f'Prefer to talk? Call {phone_link} or message '
             f'<a href="{a(company["linkedin_santosh"])}" target="_blank" rel="noopener">Santosh on LinkedIn</a>.')
    body = f'''{HERO_ART}
<div class="hk-container hk-contact-row">
    <div class="hk-contact-copy">
        <span class="hk-badge">{t(c["badge"])}</span>
        <h1 class="hk-contact-title">{t(c["title"])}</h1>
        <p class="hk-contact-text">{t(c["text"])}</p>
{ind(details, 8)}
    </div>
    <div class="hk-contact-panel">
        <div class="s_website_form" data-snippet="s_website_form" data-vcss="001" data-name="Form">
            <form id="contactus_form" action="/website/form/" method="post" enctype="multipart/form-data" class="o_mark_required hk-form" data-mark="*" data-model_name="crm.lead" data-success-mode="redirect" data-success-page="/contactus-thank-you" data-pre-fill="true">
                <div class="s_website_form_rows hk-form-grid">
{ind(chr(10).join(fields + [hidden]), 20)}
                    <div class="s_website_form_submit s_website_form_no_submit_label text-start hk-form-submit" data-name="Submit Button">
                        <span id="s_website_form_result"></span>
                        <a href="#" role="button" class="btn btn-primary s_website_form_send hk-btn hk-btn-primary">{t(c["button"])}</a>
                    </div>
                </div>
            </form>
        </div>
        <p class="hk-contact-aside">{aside}</p>
    </div>
</div>'''
    return section('s_hk_contact', 'Hekau Contact', ind(body, 4))


# --- Booking calendar (Calendly) -----------------------------------------------------------------------

def booking(heading, lead, url):
    """Calendly booking calendar. js/booking.js loads Calendly's widget when the
    block comes into view and fills in what the visitor typed in the contact
    form; until then (or without JavaScript) the link opens Calendly."""
    body = f'''<div class="hk-container">
    <div class="hk-section-head hk-glow-top">
        <h2 class="hk-h2 hk-h2-sm">{t(heading)}</h2>
        <p class="hk-lead">{t(lead)}</p>
    </div>
    <div class="hk-booking-embed o_not_editable" data-url="{a(url)}">
        <p class="hk-booking-fallback">Loading the booking calendar… <a href="{a(url)}" target="_blank" rel="noopener">Open it in a new tab</a></p>
    </div>
</div>'''
    return section('s_hk_booking hk-section', 'Hekau Booking', ind(body, 4))

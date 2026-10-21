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

def service_hero(title, sub, text, label=None, icons=(), button=('Book a Free Consultation', '/contactus'), icons_m=()):
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
    <h1 class="hk-service-title">{t(title)}</h1>
    <p class="hk-service-sub">{t(sub)}</p>
    <p class="hk-service-text">{t(text)}</p>
    <a href="{a(button[1])}" class="hk-btn hk-btn-hero">{t(button[0])}</a>
</div>'''
    return section('s_hk_service_hero', 'Hekau Service Hero', ind(body, 4))


# --- Highlight panel --------------------------------------------------------------

def highlight(title, button, tiles, text=None, title_xl=False, note=True, extra=''):
    """Statement panel with tiles; without tiles and note it is the About Us
    story banner (`extra='hk-highlight-banner'`)."""
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
    note_html = f'\n            <p class="hk-highlight-note"><img class="hk-deco" src="{IMG}/icons/doodle_arrow.svg" alt="" width="60" height="54"/><span>Start your journey today.</span></p>' if note else ''
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
    lis = '\n'.join(f'<li>{t(x)}</li>' for x in items)
    body = f'''<div class="hk-container hk-container-wide">
    <div class="hk-panel hk-attr-panel">
        <div class="hk-attr-head">
            <span class="hk-badge">{t(badge)}</span>
            <h2 class="hk-attr-title">{t(title)}</h2>
        </div>
        <p class="hk-attr-lead">{t(lead)}</p>
        <div class="hk-attr-diagram">
            <img class="hk-attr-art hk-deco" src="{IMG}/svc/attributes_art.svg" alt="" width="923" height="564"/>
            <img class="hk-attr-rings hk-deco" src="{IMG}/svc/attributes_rings.svg" alt="" width="360" height="360"/>
            <ul class="hk-attr-list">
{ind(lis, 16)}
            </ul>
        </div>
    </div>
</div>'''
    return section('s_hk_attributes hk-section', 'Hekau Attributes', ind(body, 4))


# --- Pyramid intro -------------------------------------------------------------------------

def ai_intro(badge, title, items, button=('Book a Free Consultation', '/contactus')):
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
    body = f'''{art}<div class="hk-container hk-page-hero-row">
    <div class="hk-page-hero-copy">
        <span class="hk-badge">{t(badge)}</span>
        <h1 class="hk-page-hero-title">{t(title).replace(chr(10), ' <br class="hk-only-mobile"/>')}</h1>
        <div class="hk-page-hero-text">
{ind(paragraphs(text), 12)}
        </div>
    </div>
    <img class="hk-page-hero-img" src="{IMG}/{image}" alt="{a(alt)}" width="{w}" height="{h}"/>
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

def vision(title, items, image='about/squares.svg'):
    cards = []
    for it in items:
        cards.append(f'''<div class="hk-vision-card">
    <h3 class="hk-vision-title"><img src="{IMG}/icons/{it["icon"]}.svg" alt="" width="40" height="40"/>{t(it["title"])}</h3>
    <p class="hk-vision-text">{t(it["text"])}</p>
</div>''')
    body = f'''<div class="hk-container">
{ind(heading(title, 'hk-h2 hk-h2-sm hk-h2-bold hk-h2-dm'), 4)}
    <div class="hk-vision-row">
        <img class="hk-vision-art" src="{IMG}/{image}" alt="" width="456" height="456" loading="lazy"/>
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
        cards.append(f'''<article class="hk-work-card" data-category="{a(p["category"])}">
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


def case_text(groups, eyebrow=None):
    parts = []
    for g in groups:
        parts.append(f'''<div class="hk-case-group">
    <h2 class="hk-case-h2">{t(g["title"])}</h2>
{ind(paragraphs(g["text"]), 4)}
</div>''')
    eyebrow_html = f'\n    <p class="hk-case-eyebrow">{t(eyebrow)}</p>' if eyebrow else ''
    body = f'''<div class="hk-container hk-container-case hk-case-text">{eyebrow_html}
{ind(chr(10).join(parts), 4)}
</div>'''
    return section('s_hk_case_text hk-section', 'Hekau Case Text', ind(body, 4))


def case_figure(image, caption, alt=''):
    body = f'''<div class="hk-container hk-container-case">
    <figure class="hk-case-figure">
        <img src="{IMG}/{image}" alt="{a(alt)}" width="1226" height="685" loading="lazy"/>
        <figcaption>{t(caption)}</figcaption>
    </figure>
</div>'''
    return section('s_hk_case_figure hk-section', 'Hekau Case Image', ind(body, 4))

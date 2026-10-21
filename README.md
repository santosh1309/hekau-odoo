# Odoo 20 Community — local dev with Docker

Official `odoo:20.0` image + PostgreSQL 16, set up for module development
(auto-reload on Python edits, live view XML, your modules mounted from `./addons`).

```
odoo20-dev/
├── docker-compose.yml        # Odoo 20 + PostgreSQL 16
├── .env                      # host ports (change if 8069/5433 are taken)
├── config/odoo.conf          # Odoo server config (master password, DB, dev settings) — not in Git
├── config/odoo.conf.example  # template for odoo.conf (copy it on a fresh clone)
└── addons/
    ├── odoo20_starter/       # working example module in Odoo 20 conventions
    └── website_hekau/        # the Hekau website (section 9)
```

---

## 1. Where to put this folder

- **Windows:** put it **inside WSL** (e.g. `\\wsl$\Ubuntu\home\<you>\odoo20-dev`), not on `C:\`.
  File-change events from the Windows filesystem don't reach Linux containers, so
  auto-reload silently stops working on `C:\` — and disk I/O is much slower there.
  Open it in VS Code with the *WSL* extension.
- **macOS / Linux:** anywhere is fine.

## 2. Start

```bash
cd odoo20-dev
docker compose up -d
docker compose logs -f odoo      # wait for "HTTP service running on 0.0.0.0:8069"
```

Open **http://localhost:8069**. You'll see the *Create Database* screen:

| Field | Value |
|---|---|
| Master Password | `change-this-master-password` (from `config/odoo.conf` — change it) |
| Database Name | e.g. `odoo20` |
| Email / Password | your admin login |
| Demo data | tick it if you want sample data (**off by default in Odoo 20**) |

Or create the database and install the starter module in one command:

```bash
docker compose exec odoo odoo -d odoo20 -i odoo20_starter --stop-after-init
# login: admin / admin
```

## 3. Install the starter module (if you created the DB in the browser)

1. Turn on developer mode: add `?debug=1` to the URL (`http://localhost:8069/odoo?debug=1`).
2. **Apps → Update Apps List**.
3. Remove the *Apps* filter in the search bar, search **Starter**, click **Activate**.
4. A **Starter** menu appears on the home screen.

---

## 4. The daily dev loop

| You changed… | What to do |
|---|---|
| Python method logic | Nothing — server auto-restarts (`--dev=reload`). Refresh browser. |
| View XML (existing view) | Just refresh the browser (`--dev=xml`). |
| New field / new model / new XML file / `__manifest__.py` / `ir.access.csv` | Upgrade the module (below), then refresh. |

Upgrade a module:

```bash
docker compose exec odoo odoo -d odoo20 -u odoo20_starter --stop-after-init
```

(or in the browser: **Apps** → open your module → **Upgrade**).

## 5. Creating your own module

**Easiest:** copy `addons/odoo20_starter`, rename the folder, and find/replace
`odoo20_starter` / `starter.task` / `starter_` with your names. Then
**Apps → Update Apps List** and install it.

**If you use `odoo scaffold`** — watch out: in the current 20.0 image it still
generates the *old* `security/ir.model.access.csv`. Odoo 20 removed that model, so
installing fails with `KeyError: 'ir.model.access'`. Replace it with
`security/ir.access.csv`:

```csv
id,name,model_id,group_id/id,operation,domain
access_my_model_user,My model: internal users,my.model,base.group_user,crud,
```

`operation` is any subset of `crud`; `domain` (optional) replaces old record rules,
e.g. `"[('user_id','=',user.id)]"`.

```bash
# scaffold from inside the container (no local Odoo install needed)
docker compose run --rm --user root odoo odoo scaffold my_module /mnt/extra-addons
# Linux only: files are created as root — take ownership back
sudo chown -R $USER:$USER addons/my_module
```

### Odoo 20 conventions worth knowing

- Security: `security/ir.access.csv` (no more `ir.model.access.csv` or `ir.rule` XML).
- List views use `<list>` (not `<tree>`); `view_mode` is `list,form`.
- Use `invisible="..."` / `readonly="..."` expressions directly on fields (no `attrs`).
- Manifest version format: `20.0.x.y.z`.

---

## 6. Handy commands

```bash
docker compose logs -f odoo                          # live server log
docker compose restart odoo                          # restart Odoo only
docker compose exec odoo odoo shell -d odoo20        # Python shell with `env`
docker compose exec db psql -U odoo -d odoo20        # SQL shell

# run a module's tests on a throwaway database
docker compose exec odoo odoo -d test_db -i my_module --test-enable

docker compose down          # stop (data kept)
docker compose down -v       # stop AND delete all databases + filestore
```

Connect pgAdmin / DBeaver to **localhost:5433**, user `odoo`, password `odoo`.

Backups / restores / duplicating databases: **http://localhost:8069/web/database/manager**.

## 7. Adding OCA or third-party modules

```bash
cd addons
git clone --depth 1 -b 20.0 https://github.com/OCA/web.git oca-web
```

Then in `config/odoo.conf`:

```ini
addons_path = /mnt/extra-addons,/mnt/extra-addons/oca-web
```

`docker compose restart odoo` → **Update Apps List**.
(Check the OCA repo actually has a `20.0` branch first — OCA ports lag behind releases.)

## 8. IDE autocomplete & reading Odoo source

The Odoo source lives inside the container at `/usr/lib/python3/dist-packages/odoo`.
For go-to-definition in VS Code / PyCharm, clone it next to this folder (don't mount it):

```bash
git clone --depth 1 -b 20.0 https://github.com/odoo/odoo.git ../odoo-src
```

and add `../odoo-src` to your editor's Python analysis paths.

## 9. Hekau website (`addons/website_hekau`)

The company website built from the Figma file "Hekau WIP (Copy)". It's a regular
module (not a theme): it sets the Hekau palette and fonts, styles Odoo's own header
(menus stay editable under **Website → Site → Menus**), replaces the footer, and
builds the pages from **Hekau blocks**. All text, images and links stay editable in
the website builder.

Install it **instead of** activating the Website app yourself (it pulls Website in and
skips the theme wizard, which would override the palette):

1. Copy `website_hekau` into `addons/`.
2. **Apps → Update Apps List**, remove the *Apps* filter, search **Hekau Website**, **Activate**.
   Or: `docker compose exec odoo odoo -d odoo20 -i website_hekau --stop-after-init`
3. Open http://localhost:8069 — the Home page is the Figma design.

Upgrading an installed copy after replacing the folder:

```bash
docker compose exec odoo odoo -d odoo20 -u website_hekau --stop-after-init
docker compose restart odoo
```

### Building pages with Hekau blocks

In the website builder (**Edit**), the **Blocks** tab has a **Hekau** category with
every section of the design (22 blocks): Hero, Partners, Why Partner, Stats, Services,
Domains, Projects, Testimonials, Call to Action, Service Hero, Highlight, Attributes,
Pyramid Intro, Features, Process, Page Intro, Team, Vision, Project List, Case Hero,
Case Text and Case Image. Drag one onto any page; each block carries its own spacing,
mobile layout and animations, so they stack in any order.
Tip: for a page that starts with a hero block, click the header in **Edit** mode and
set its visibility to **Over The Content** so the nav bar floats over the hero like on
the Home page.

Pages shipped with the module (all built from the blocks, all editable):

| URL | Page |
|---|---|
| `/` | Home |
| `/services` | Services overview |
| `/web-application-development`, `/mobile-application-development`, `/ux-ui-design`, `/cloud-managed-services`, `/business-process-automation`, `/ai-solutions` | The six service pages |
| `/about-us` | About Us (story, co-founders, vision & mission, values) |
| `/projects` | Projects list with the category filter |
| `/projects/the-arc` | Sample case study — duplicate it (**Site → Pages**) for each new project |
| `/blog` | Blog (Odoo's Blog app in the Hekau design); write posts in **Website → Blog** |

The blog came with five sample posts (Figma placeholder copy, author "Hekau Team"):
replace or unpublish them in **Website → Blog → Blog Posts**. The newest post is the
"Featured Post" at the top of the blog; each post's first tag is the category shown
above its title; the picture is the post's cover.

After editing the module:
- `.scss` / `.js` changes: refresh the page (assets rebuild in dev mode).
- New files or `__manifest__.py` changes: `docker compose restart odoo`.
- A block or page content changed: edit the hand-written blocks in `views/snippets/`
  (Home blocks) or `scripts/hk_render.py` (inner-page blocks) and the page text in
  `scripts/hk_content.py`, run `python3 scripts/build_pages.py` (from the module
  folder) to regenerate the pages, then upgrade the module.
  Blocks are copied into pages (that's what lets the builder edit and move them), so
  pages don't pick up block changes on their own.
- `views/*.xml` changes show on refresh (`--dev=xml`), **unless the page was already
  edited in the builder** — builder edits are saved as a website-specific copy of the
  view that wins over the file. To go back to the file version, delete that copy
  (developer mode → **Settings → Technical → User Interface → Views**, search the
  page name, delete the row that has a Website set).

Layout of the module:

| Path | What it holds |
|---|---|
| `static/src/scss/primary_variables.scss` | Palette (`hekau`), fonts, header/footer/button defaults |
| `static/src/scss/hk_tokens.scss` | Design tokens (colours, spacing, easing) and mixins |
| `static/src/scss/hekau.scss` | Shared styles: containers, type, buttons, heading glows, header, footer |
| `views/snippets/s_hk_*.xml` + `static/src/snippets/s_hk_*/000.scss` | One block per section (markup + desktop/mobile styles and animations) |
| `views/snippets/snippets.xml` | Registers the blocks under **Blocks → Hekau** |
| `views/homepage.xml`, `views/pages/*.xml` | Home and the other pages — generated from the blocks by `scripts/build_pages.py` |
| `scripts/hk_render.py`, `scripts/hk_content.py` | Markup of the inner-page blocks; text of the inner pages |
| `views/blog.xml`, `static/src/scss/hk_blog.scss`, `data/blog_data.xml` | Blog listing in the Hekau design; sample posts (created once) |
| `views/layout.xml` | Font loading, "Let's Talk" button (desktop + mobile bar), footer, hidden copyright bar, blog header overlay |
| `static/src/js/*.js` | Testimonial arrows, mobile swipe indicators, process timeline, project filter |
| `__init__.py`, `migrations/` | Install/upgrade hooks: logo, main menu, header options, header-over-hero, blog name |

## 10. Working with Git

The folder is a Git repository. Git tracks the **code and setup files** (modules,
`docker-compose.yml`, this README). It does **not** track:

- **The database** — everything you configure in the Odoo screens (company, users,
  settings, contacts, invoices, website edits) lives in PostgreSQL. Protect it with
  backups: **http://localhost:8069/web/database/manager → Backup**.
- `config/odoo.conf` — it holds passwords. A fresh clone needs
  `cp config/odoo.conf.example config/odoo.conf` (then set the master password).
- `design/` — the Figma file and render references (large binaries).

Getting changes made elsewhere (e.g. by Claude):

```bash
git pull
# if a module changed, upgrade it (see section 9), e.g.:
docker compose exec odoo odoo -d odoo20 -u website_hekau --stop-after-init
docker compose restart odoo
```

Saving your own code changes:

```bash
git status                 # what changed
git add -A
git commit -m "Describe the change"
git push
```

## 11. Troubleshooting

| Problem | Fix |
|---|---|
| Port 8069 or 5433 already in use | Change `ODOO_HOST_PORT` / `DB_HOST_PORT` in `.env`, then `docker compose up -d`. |
| Edits to `.py` files don't trigger a reload (Windows) | Move the folder into WSL (see step 1). |
| `KeyError: 'ir.model.access'` on install | Old security file — switch to `ir.access.csv` (see step 5). |
| Module doesn't appear in Apps | Update Apps List, remove the *Apps* filter, check `docker compose logs odoo` for manifest errors. |
| Want a clean slate | `docker compose down -v && docker compose up -d` |

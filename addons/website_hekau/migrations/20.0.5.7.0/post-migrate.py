from odoo import api, SUPERUSER_ID

SAMPLE_POSTS = ['post_grid', 'post_iot', 'post_civil', 'post_energy', 'post_ml']
SAMPLE_TAGS = ['tag_electronics_communication', 'tag_computer_science', 'tag_civil',
               'tag_electrical_electronics', 'tag_ai']
BLOG_DESCRIPTION = ('Practical articles for founders and operations leaders on connected systems, '
                    'ERP, automation and AI that actually gets used.')


def migrate(cr, version):
    """5.7: the 20 Hekau articles replace the five sample posts of the design."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    for xmlid in SAMPLE_POSTS:
        post = env.ref(f'website_hekau.{xmlid}', raise_if_not_found=False)
        if post:
            post.unlink()
    for xmlid in SAMPLE_TAGS:
        tag = env.ref(f'website_hekau.{xmlid}', raise_if_not_found=False)
        if tag and not tag.with_context(active_test=False).post_ids:
            tag.unlink()
    author = env.ref('website_hekau.blog_author', raise_if_not_found=False)
    if author and not env['blog.post'].with_context(active_test=False).search_count([('author_id', '=', author.id)]):
        author.active = False
    blog = env.ref('website_blog.blog_blog_1', raise_if_not_found=False)
    if blog and not blog.website_meta_description:
        blog.website_meta_description = BLOG_DESCRIPTION

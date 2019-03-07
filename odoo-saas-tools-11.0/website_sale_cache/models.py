# Copyright 2017 Artyom Losev
# Copyright 2018 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models
from odoo import tools
import logging

_logger = logging.getLogger(__name__)


class WebsiteCategoryCache(models.Model):

    _inherit = 'website'

    @tools.cache()
    def category_cache(self, cats, slug, keep, parent_category_ids, collapsed=False):
        if collapsed:
            template = 'website_sale_cache.categories_collapsed_cache_template'
        else:
            template = 'website_sale_cache.categories_cache_template'
        _logger.info('Product public categories were cached.')
        return self.env['ir.ui.view'].render_template(template, {'categories': cats, 'slug': slug, 'keep': keep,
                                                                 'parent_category_ids': parent_category_ids})

    def action_update_cache(self):
        _logger.info('Cache has been cleared.')
        return self.category_cache.clear_cache(self)

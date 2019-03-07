from odoo import models, api


class Product(models.Model):
    _inherit = 'product.template'

    def _extend_domain(self, domain):
        if (self.env.context.get('search_tags') and
                ('tag_ids', 'ilike', self.env.context.get('search_tags')) not in domain):
            domain.insert(domain.index(('sale_ok', '=', True)) + 1, '|')
            domain += [('tag_ids', 'ilike', self.env.context.get('search_tags'))]
        return domain

    @api.model
    def search_count(self, domain):
        domain = self._extend_domain(domain)
        return super(Product, self).search_count(domain)

    @api.model
    def search(self, domain, offset=0, limit=None, order=None, count=False):
        domain = self._extend_domain(domain)
        return super(Product, self).search(
            domain, offset=offset, limit=limit,
            order=order, count=count
        )

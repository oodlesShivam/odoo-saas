from odoo import models, fields


class Website(models.Model):
    _inherit = 'website'

    ticket_transfer_success = fields.Html(
        "Message ticket transfer: success",
        default="<h1>Ticket is transfered successfully. We will instruct receiver on further actions.</h1>")

    ticket_transfer_receiver_not_found = fields.Html(
        "Message ticket transfer: receiver not found",
        default="""<h1>User with the email is not found. The user has to <a href="/web/signup">signup</a> first.</h1>""")

    ticket_transfer_receiver_has_ticket = fields.Html(
        "Message ticket transfer: receiver already has ticket",
        default="""<h1>User already has the ticket.</h1>""")

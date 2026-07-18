from odoo import fields, models, _
from odoo.exceptions import ValidationError


class CrmLead(models.Model):
    _inherit = "crm.lead"

    customer_reference = fields.Char(string="Customer Reference")

    expected_budget = fields.Float(string="Expected Budget")

    project_category = fields.Selection(
        [
            ("erp", "ERP"),
            ("crm", "CRM"),
            ("website", "Website"),
        ], string="Project Category",)


    def action_set_won(self):
        for lead in self:
            if not lead.expected_revenue:
                raise ValidationError(
                    _("Expected Revenue must be set before marking this opportunity as Won.")
                )

            if lead.expected_revenue <= 0:
                raise ValidationError(
                    _("Expected Revenue must be greater than zero before marking this opportunity as Won.")
                )

        return super().action_set_won()


    # Make Salesperson Field Completely Readonly
    def write(self, vals):

        if "user_id" in vals:
            raise ValidationError(
                _("Salesperson cannot be changed.")
            )

        return super().write(vals)


    # Prevent Deletion of Won Opportunities
    def unlink(self):

        for lead in self:
            if lead.stage_id.is_won:
                raise ValidationError(
                    _("Won opportunities cannot be deleted.")
                )

        return super().unlink()
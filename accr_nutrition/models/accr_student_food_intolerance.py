from odoo import models, fields, api, _

class accrStudentFoodIntolerance(models.Model):
    _name = "accr.student.food.intolerance"

    food_type = fields.Many2one('accr.intolerance', string=u'Food Type', required=True, ondelete='set null', )
    nutrition_details = fields.Many2one('accr.student.nutrition.details', string=u'Nutrition Details', ondelete='set null')
    student = fields.Many2one('x_student', string=u'Student', required=True, ondelete='set null', )

    @api.multi
    @api.depends('student', 'food_type')
    def _compute_name(self):
        for record in self:
            record.name = record.student.display_name + ' - ' + record.food_type.display_name
from odoo import api, fields, models


class StarterTask(models.Model):
    _name = 'starter.task'
    _description = "Starter Task"
    _order = 'done, priority desc, deadline, id desc'

    name = fields.Char(required=True)
    description = fields.Text()
    priority = fields.Selection(
        [('0', "Normal"), ('1', "High")],
        default='0',
    )
    deadline = fields.Date()
    done = fields.Boolean()
    user_id = fields.Many2one(
        'res.users',
        string="Assigned to",
        default=lambda self: self.env.user,
    )
    days_left = fields.Integer(compute='_compute_days_left')

    @api.depends('deadline', 'done')
    def _compute_days_left(self):
        today = fields.Date.context_today(self)
        for task in self:
            if task.deadline and not task.done:
                task.days_left = (task.deadline - today).days
            else:
                task.days_left = 0

    def action_mark_done(self):
        self.done = True

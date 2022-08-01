from odoo import models, fields, api
from math import pi,sin,cos

class ToyRobotSimulator(models.Model):
    _name = 'toy.robot.simulator'

    table_x = fields.Integer('Table Width', default=5)
    table_y = fields.Integer('Table Height', default=5)

    point_x = fields.Integer('Point X')
    point_y = fields.Integer('Point Y')
    facing  = fields.Selection([
        ('NORTH', 'NORTH'),
        ('SOUTH', 'SOUTH'),
        ('WEST', 'WEST'),
        ('EAST', 'EAST'),
    ], string='Facing')

    report_x = fields.Integer('Report X')
    report_y = fields.Integer('Report Y')
    report_f = fields.Selection([
        ('NORTH', 'NORTH'),
        ('SOUTH', 'SOUTH'),
        ('WEST', 'WEST'),
        ('EAST', 'EAST'),
    ], string='Report F')

    report = fields.Char(string='Name')

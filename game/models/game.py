from odoo import _, api, fields, models, tools
from math import pi,sin,cos

class ToyRobotSimulator(models.Model):
    _name = "toy.robot.simulator"
    _description = "Audit Program"
    _order = "id asc"

    point_x = fields.Integer('Point X')
    point_y = fields.Integer('Point Y')
    facing  = fields.Selection([
        ('NORTH', 'NORTH'),
        ('SOUTH', 'SOUTH'),
        ('WEST', 'WEST'),
        ('EAST', 'EAST'),
    ], string='Facing')
    pointed = fields.Boolean('Pointed')

    report_x = fields.Integer('Report X')
    report_y = fields.Integer('Report Y')
    report_f = fields.Selection([
        ('NORTH', 'NORTH'),
        ('SOUTH', 'SOUTH'),
        ('WEST', 'WEST'),
        ('EAST', 'EAST'),
    ], string='Report F')

    report = fields.Char(string='Report',compute='_generate_report')

    def _generate_report(self):
        if self.report_x >= 0 and self.report_y >= 0 and self.report_f:
            self.report =  str(self.report_x)+", "+str(self.report_y)+", "+str(self.report_f)
        else:
            self.report = "Place a Point."

    def move(self):
        if self.report_f == "NORTH":
            self.report_y+=1
        elif self.report_f == "EAST":
            self.report_x+=1
        elif self.report_f == "SOUTH":
            self.report_y-=1
        elif self.report_f == "WEST":
            self.report_x-=1
        if self.report_x < 0 or self.report_y < 0 or self.report_x > 5 or self.report_y > 5:
                raise models.ValidationError(
                    _("Your robot will Fall.")
                ) 
    
    def left(self):
        self.report_f = self.convert_int_to_facing((self.convert_facing_to_int(self.report_f)-90)%360)
    
    def right(self):
        self.report_f = self.convert_int_to_facing((self.convert_facing_to_int(self.report_f)+90)%360)

    def place_point(self):
        if self.point_x >= 0 and self.point_y >= 0 and self.facing:
            self.report_x = self.point_x
            self.report_y = self.point_y
            self.report_f = self.facing
        else :
            raise models.ValidationError(
                _("Please ensure point X, point Y, and Facing is Correct.")
            )

    def convert_facing_to_int(self, facing):
        if facing == "NORTH":
            return 0
        if facing == "EAST":
            return 90
        if facing == "SOUTH":
            return 180
        if facing == "WEST":
            return 270
    
    def convert_int_to_facing(self, value):
        if value == 0:
            return "NORTH"
        if value == 90:
            return "EAST"
        if value == 180:
            return "SOUTH"
        if value == 270:
            return "WEST"

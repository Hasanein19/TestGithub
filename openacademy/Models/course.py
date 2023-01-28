from odoo import models, fields, api ,exceptions,_

class Course(models.Model):
  _name = 'openacademy.courses'
  _description = 'openAcademy Courses'

  name = fields.Char(string="Title",required=True)
  Description=fields.Text(string="Description")
  about=fields.Text(string="About")


  responsible_id=fields.Many2one('res.users',ondelete='set null',string="Responsible",index=True)
  session_ids=fields.One2many('openacademy.session','course_id',string="Sessions")

#sal constrains
  # _sql_constrains=[
  #     ('name_description_check',
  #      'CHECK(name!=description)',
  #      "The title must be not description"),
  #     ('name_unique',
  #      'UNIQUE(name)',
  #      "The Course must be unique"),]

class Session(models.Model):
  _name = 'openacademy.session'
  _description = 'openAcademy Session'

  name = fields.Char(string="Title",required=True)
  start_date=fields.Date(string="Sart Date", default=fields.Date.today)
  end_date=fields.Date(string="End Date")
  duration=fields.Float(digits=(7,3),help="Duration in days")
  seats=fields.Integer(string="Number of seats")
  
  instructor_id=fields.Many2one('res.partner',string="Instructor")
  course_id=fields.Many2one('openacademy.courses',ondelete='cascade',string="Course",required=True)
  attendee_ids=fields.Many2many('res.partner',string="Attendees")
  active=fields.Boolean(default=True)
  # taken_seats=fields.Float(string="Taken seats" ,compute='_taken_seats')

  # @api.depends('seats','attendee_ids')
  # def _taken_seats(self):
  #   for r in self:
  #     if not r.taken_seats:
  #       r.taken_seats=0.00
  #     else:
  #       r.taken_seats=100.0*len(r.attendee_ids)/r.seats

  # @api.onchange('seats','attendee_ids')
  # def _taken_seats(self):
   
  #     if self.seats<0:
  #       return{
  #          'warning':{
  #           'title': "Incorrect 'seats' value",
  #           'message':"The number of available seats may not be negative",
  #        },
  #        }

  #     if self.seats < len(self.attendee_ids):
  #       return {
  #          'warning':{
  #           'title': "Too many attedees",
  #           'message':"Increase seats or remove exees attendees",
  #        },

  #       }


  # @api.constrains('instructor_id','attendee_ids')
  # def _check_instructor_not_in_attendees(self):
   
  #     for r in self:

  #       if r.instructor_id  and r.instructor_id in  r.attendee_ids:
  #         raise exceptions.ValidationError("A session's instructor can't be attendee")
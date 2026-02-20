from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author')
    isbn = fields.Char(string='ISBN')
    publication_date = fields.Date(string='Publication Date')
    pages = fields.Integer(string='Number of Pages')
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)

    # new add fields
    category = fields.Selection([
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('science', 'Science'),
        ('history', 'History'),
        ('other', 'Other'),
    ], string="Category")

    price = fields.Float(string="Price")
{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Manage library books',
    'author': 'Keya Sultana',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
    ],
    'installable': True,
    'application': True,
}
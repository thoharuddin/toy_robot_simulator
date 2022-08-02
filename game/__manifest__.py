{
    "name": "Odoo Games - Toy Robot Simulator'",
    "summary": """Toy Robot Simulator.""",
    "version": "14.0.1.0.0",
    "category": "Others",
    "license": "LGPL-3",
    "author": "Thoharuddin Hanif",
    "depends": ["base"],
    'images': ['static/iconnew.png'],
    "data": [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/game_view.xml',
    ],
    "application": True,
}
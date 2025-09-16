{
    "name": "Web Hide Many2 X Option",
    "description": """This module hides the Create and Edit options in Many2One and Many2Many fields in Odoo.
    """,
    "author": "MT Tech",
    "website": "https://mttech-mm.com",
    "application": True,
    "installable": True,
    "license": "LGPL-3",
    "version": "18.0.0.0",
    "depends": ["web"],
    "assets": {
        "web.assets_backend": [
            "web_hide_many_2_x/static/src/js/many_2_one.js",
            "web_hide_many_2_x/static/src/js/many_2_many.js",
        ],
    },
}

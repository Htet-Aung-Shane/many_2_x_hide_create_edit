{
    "name": "Web Hide Many2 X Option",
    "description": """
        <h2>Web Hide Many2 X Option</h2>
        <p>This module hides the Create and Edit options in Many2One and Many2Many fields in Odoo.</p>
        <ul>
            <li>Author: MT Tech</li>
            <li>Version: 17.0.0.0</li>
            <li>License: LGPL-3</li>
        </ul>
        <p>Features:</p>
        <ul>
            <li>Removes Create and Edit options from selection fields</li>
            <li>Works with both backend and frontend views</li>
        </ul>
    """,
    "author": "MT Tech",
    "application": True,
    "installable": True,
    "license": "LGPL-3",
    "version": "17.0.0.0",
    "depends": ["web", "website_enterprise"],
    "assets": {
        "web.assets_backend": [
            "web_hide_many_2_x/static/src/js/many_2_one.js",
            "web_hide_many_2_x/static/src/js/many_2_many.js",
        ],
    },
}

{
    "name": "Web Hide Many2 X Option",
    "author":"MT Tech",
    'application':True,
    'installable': True,
    'license':'LGPL-3',
    'depends': ['web', 'website_enterprise'],
    'assets': {
        'web.assets_backend': [
            'web_hide_many_2_x/static/src/js/many_2_one.js',
            'web_hide_many_2_x/static/src/js/many_2_many.js',
        ],
    },
}

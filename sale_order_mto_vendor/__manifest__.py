# -*- coding: utf-8 -*-
{
    'name': "Vendor selection for MTO",

    'summary': """
        MTO vendor selection helper""",

    'description': """
        Having problem in specifing which vendor to make Purchase order if the product is MTO then this 
        Module will help you setting specific vendor with which the MTO will be created 
        vendor must be in purchase tab of product setup or if you need this to be modified contact us
    """,

    'author': "Cagvir",
    'website': "https://cagvir.com/",

    # Categories can be used to filter modules in modules listing
    'category': 'Extra',
    'version': '14.0.3',
    'license': 'LGPL-3',

    # "images": ["static/description/icon.png", ],
    'images': ['static/description/banner.png'],
    # any module necessary for this one to work correctly
    'depends': ['purchase_stock','sale'],

    # always loaded
    'data': [
        'views/sol_ext.xml',
    ],

    "application": True,
    "installable": True,
    "auto_install": False,

}
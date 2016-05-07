# -*- coding: utf-8 -*-
{
    'name': "GPS Tracking",

    'summary': "Provides tracking capabilities to the fleet management Module"
    'description': """
        Long description of module's purpose
    """,

    'author': "AfrikaFleet SARL",
    'website': "http://www.afrikafleet.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'GeoBI',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','fleet'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

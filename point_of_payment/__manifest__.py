# Copyright 2021 ITSur - Juan Pablo Garza <jgarza@itsur.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Point of payment",
    "summary": "Introduces concept of point of payment and accounting journal sessions",
    "version": "13.0.1.0.0",
    "category": "Accounting",
    "website": "https://github.com/itsurnqn/account-addons",
    "author": "ITSur",
    "license": "AGPL-3",
    "depends": ["account"],
    "data": [
        'security/pop_security.xml',
        'security/ir.model.access.csv',
        'views/account_payment_views.xml',        
        'views/menus.xml',
        'views/pop_config_views.xml',
        'views/pop_session_journal_line_views.xml',
        'views/pop_session_journal_views.xml',
        'views/pop_session_views.xml',
        'views/res_users_views.xml',        
        'views/templates.xml',        
        "wizards/pop_session_cash.xml"
        ],
    "development_status": "Production/Stable",        
    "installable": True,
}

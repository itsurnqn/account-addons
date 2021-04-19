# Copyright 2021 ITSur - Juan Pablo Garza <jgarza@itsur.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Integrate point of payment with payment group (by adhoc)",
    "summary": "",
    "version": "13.0.1.0.0",
    "category": "Accounting",
    "website": "https://github.com/itsurnqn/account-addons",
    "author": "ITSur",
    "license": "AGPL-3",
    "depends": ["account_payment_group","account_payment_group_document"],
    "data": [
        'views/account_payment_group_views.xml',
        ],
    "installable": True,
}

{
    'name': 'Real Estate Account',
    'application': False,
    'category': 'Marketing',
    'summary': 'Yes this is an app for an app',
    'depends': [
        'base',
        'real_estate',
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_account_menus.xml',
    ]
}

# -*- coding: utf-8 -*-
# Copyright: 2024 Hakika Strategy Into Action (Pty) Ltd

##############################################################################
#
#   Hakika Account
#   Module:     hk_account
#   Author:     Newline Software d.o.o. <office@newline.software>
#   mail:       <office@newline.software>
#   Copyright:  2024 Hakika Strategy Into Action (Pty) Ltd
#
##############################################################################

{
    'name': 'Hakika Account',
    'version': '1.0.0',
    'category': 'Account',
    'summary': 'Various modifications in accounting workflow',
    'description': """

Various modifications in accounting workflow
============================================

""",
    'author': 'Newline Software d.o.o.',
    'website': 'https://newline.software/',
    'depends': [
        'account',
        'project_account',
        'product',
    ],
    'data': [
        "security/account_security.xml",
        "views/account_journal_views.xml",
        "views/account_move_views.xml",
        "views/product_views.xml",
    ],
    # 'qweb': [],
    # 'demo': [],
    # 'css': [],
    # 'images': [],
    'installable': True,
    'application': True,
}

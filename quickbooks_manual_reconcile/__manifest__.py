# -*- coding: utf-8 -*-

{
    'name': 'Bank Reconciliation Odoo ( Community + Enterprise ) Manual - Quickbooks inspired',
    'version': '1.0.0',
    'summary': 'Odoo Reconciliation, Odoo manual reconciliation, manual reconciliation, reconcil, reconcilliation, quick books, quick book, community, odoo community, odoo sh,  quickbook, quickbooks, bank reconcile, reconcile, accounts, accounting, Reconciliation, Bank Reconciliation, Invoice Reconciliation, Payment Reconciliation, Bank Statement, Accounting Excel Reports, Odoo Excel Reports, Odoo Accounting Excel Reports, Odoo Financial Reports, Accounting Reports In Excel For Odoo 17, Financial Reports in Excel, Odoo Account Reports, inventory, banking, forecasting, cash, cashflow, cash flow, credit acount, bank, book, books, ledger, journal, journal entry, statement, statements, bank statements, transact, transaction, transactions, odoo, techfinna, ',
    'description': """
    Odoo Reconciliation, Odoo manual reconciliation, manual reconciliation, reconcil, reconcilliation, quick books, quick book, quickbook, quickbooks, bank reconcile, reconcile, accounts, accounting, Reconciliation, Bank Reconciliation, Invoice Reconciliation, Payment Reconciliation, Bank Statement, Accounting Excel Reports, Odoo Excel Reports, Odoo Accounting Excel Reports, Odoo Financial Reports, Accounting Reports In Excel For Odoo 17, Financial Reports in Excel, Odoo Account Reports, inventory, banking, forecasting, cash, cashflow, cash flow, credit acount, bank, book, books, ledger, journal, journal entry, statement, statements, bank statements, transact, transaction, transactions, odoo, techfinna, 
    """,
    'author': 'TechFinna',
    'live_test_url': 'https://www.youtube.com/watch?v=3Svyo8L5bxE&t=2s',
    'images': ['static/description/banner.gif'],
    'website': 'https://www.techfinna.com',
    'maintainer': 'Techfinna',
    'category': 'Accounting',
    'support': "info@techfinna.com",
    'license': 'LGPL-3',
    'price': 249,
    'currency': 'USD',

    'depends': [
        'base', 'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/reconcile.xml',
        'views/manual_recon.xml',
    ],
    'assets': {
        'quickbooks_manual_reconcile.reconcileAsset': [
            'quickbooks_manual_reconcile/static/*/*.js',
            'quickbooks_manual_reconcile/static/*/*.css',

        ],
    },

}

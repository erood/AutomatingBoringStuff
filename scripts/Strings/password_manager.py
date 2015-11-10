#! python3.4
# password_manager.py - An insecure password locker program
__author__ = 'm'

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python password_manager.py [account] - copy account password')
    sys.exit(1)

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

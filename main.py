#!/usr/bin/python3
import pyftpdlib.__main__ as entry
from sys import exit

try:
    entry.main()
except Exception as e:
    print(f'^{e.args[1] if e.args and len(e.args) > 1 else e}')
    exit(1)
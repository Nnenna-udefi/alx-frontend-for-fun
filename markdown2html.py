#!/usr/bin/python3
"""Script that contains markdown to html"""
import sys
import os

if len(sys.argv) < 2:
    print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
    exit(1)
if not os.path.isfile(sys.argv[1]):
    print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
    exit(1)
else:
    pass
    exit(0)

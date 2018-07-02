#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re
from collections import namedtuple

test = 'foo = 42 + 10 * 5'

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join(NAME,NUM,PLUS,TIMES,EQ,WS))

scanner = master_pat.scanner(text)
scanner.match()

def generate_token(pat,text):
  scanner = pat.scanner(text)
  Token = namedtuple('Token',['name','value'])
  for m in iter(scanner.match,None)
    yield Token(m.lastgroup,m.group())
    
    
for tok in generate_token(master_pat,text):
  print(tok)

#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def manual_iter():
  with open('/etc/passwd') as f:
    try:
      while True:
        line=next(f)
        print(line,end=' ')
        
    except StopIteration:
      pass
      
def new_iter():
  with open('/etc/passwd') as f:
    while True:
      line = next(f,None)
      if line in None:
        break
      print(line,end=' ')

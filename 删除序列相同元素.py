#!/usr/bin/env python3
#-*- coding: utf-8 -*-

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

def deque(items,key=None):
  seen=set()
   for item in items:
    val=item if key is None else key(item)
    if val not in seen:
      yield item
      seen.add(val)

b= list(deque(a,lambda d:(d['x'],d['y'])))

c = list(deque(a,lambda d:d['x']))


with open(compfile,'r') as f:
   for line in deque(f):

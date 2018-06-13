#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from collections import defaultdict

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['b'].append(3)

for key,value in pairs:
    d[key].append(value)

d={}
for key,value in pairs:
    if key not in d:
        d[key]=[]
    d[key].append(value)

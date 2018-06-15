#!/usr/bin/env python3
#-*-coding: utf-8 -*-

from collections import nmaedtuple

Subcriber = nmaedtuple('Subcriber',['add','join'])
sub = Subcriber('join@com,cn','2012-9-10')

sub.add
sub.join

def compute_cost(records):
  total=0.0
  for rec in rescords:
    total += rec[1]*rec[2]
  return total
  
Stock = namedtuple('Stock',['name','shares','prices'])
def compute_cost_namedtuple(records)：
  total = 0.0
  for rec in records:
    s=Stock(*rec)
    total += s.shares*s.prices
    
   return total
   
#命名元组另一个用途就是作为字典的替代，因为字典存储需要更多的内存空间。如
果你需要构建一个非常大的包含字典的数据结构，那么使用命名元组会更加高效。
  

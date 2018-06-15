#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#列表推导

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
[n for n in mylist if n>0]


#使用列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结
果集，占用大量内存。

pos=(n for n in mylist if n>0)
for x in pos:
  print(x)
  
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
  try:
     x=int(val)
     return True
  expect ValueError:
    return Faluse
ivals=list(filter(is_int,values))
print(ivals)

#filter() 函数创建了一个迭代器，因此如果你想得到一个列表的话，就得像示例
那样使用 list() 去转换。


'''
itertools.compress() ，它以一个 iterable
对象和一个相对应的 Boolean 选择器序列作为输入参数。然后输出 iterable 对象中对
应选择器为 True 的元素。当你需要用另外一个相关联的序列来过滤某个序列的时候，
这个函数是非常有用的。'''
addresses = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK',
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5=[n>5 for n in counts]

list(compress(address,more5))和 filter() 函数类似，compress() 也是返回的一个迭代器。因此，如果你需要得
到一个列表，那么你需要使用 list() 来将结果转换为列表类型。

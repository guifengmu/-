#!/usr bin/env python3
#-*- coding: utf-8-*-

from collections import Counter

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

word_counts=Counter(words)

top_three= word_counts.most_common

print(top_three)

for key in words:
  words_count[key]+=1
  
  #，Counter 对象在几乎所有需要制表或者计数数据的场合是非常有用的工具。
  
  

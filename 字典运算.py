#!/usr/bin/env python3
#-*- coding:utf-8 -*-

dict = {
    'one':72,
    'two':64,
    'three':89,
    'four':34
}

min_dict = min(zip(dict.values(),dict.keys()))

max_dict = max(zip(dict.values(),dict.keys()))

sort_dict = sorted(zip(dict.values(),dict.keys()))
##执行这些计算的时候，需要注意的是 zip() 函数创建的是一个只能访问一次的迭
代器

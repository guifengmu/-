#!/usr/bin/env pyhton3
# -*- coding: utf-8 -*-

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item) )"""采用三元数组的方法。
        设置一个优先级，一个条目值，一个任务值。即使当两个任务有相同优先级的时候，因为条目值不一样可以帮助cpu来裁决它们被加载的顺序。 
        """
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

# Example use
class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)
    '''一个对象本身不是str，ascii，repr格式，
        可以使用!s、!a、!r，将其转成str，ascii，repr
        '''

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print("Should be bar:", q.pop())
print("Should be spam:", q.pop())
print("Should be foo:", q.pop())
print("Should be grok:", q.pop())

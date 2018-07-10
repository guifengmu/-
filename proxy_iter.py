#!/usr/bin/env python3


class Node:
	def __init__(self,values):
		self._values=values
		self._children=[]
	def __repr__(self):
		return 'Node({!r})'.format(self._values)
	def add_children(self,node):
		self._children.append(node)
	def __iter__(self):
		return iter(self._children)

if __name__ == '__main__':
	root=Node(0)
	childr1=Node(1)
	childr2 = Node(2)
	root.add_children(childr1)
	root.add_children(childr2)
	for ch in root:
		print(ch)

from collections import deque
from min_tree import BTree
import pprint as prt

def bfs_linked_list(tree: BTree):
    q = deque()
    q.append(tree._root)
    depth = 0
    hashTable = {}

    while not len(q) == 0:
        level_size = len(q)
        for i in range(0, level_size):
            removed = q.pop()
            if depth in hashTable:
                hashTable[depth].append(removed)
            else:
                newQ = deque()
                newQ.append(removed)
                hashTable[depth] = newQ
            if removed._l:
                q.append(removed._l)
            if removed._r:
                q.append(removed._r)

        depth += 1
       
    return hashTable

tree = BTree()
tree.add_to_tree(7)
tree.add_to_tree(9)
tree.add_to_tree(3)
tree.add_to_tree(2)
tree.add_to_tree(4)
tree.add_to_tree(5)
tree.add_to_tree(8)
ht = bfs_linked_list(tree)
for k,v in ht.items():
    print(k, end=": ")
    while len(v) != 0:
        popped = v.pop()
        print(f"{popped._value}", end=", ")
    print()
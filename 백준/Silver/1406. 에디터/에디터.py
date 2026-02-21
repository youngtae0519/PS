import sys

input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

word = list(input().rstrip())
N = len(word)

for i in range(N):
    if i == 0:
        prev = None
        cur = Node(word[0])
        nex = Node(word[1])
    elif i == N - 1:
        prev, cur = cur, nex
        nex = None
    else:
        prev, cur = cur, nex
        nex = Node(word[i + 1])
    cur.prev = prev
    cur.next = nex
    
tail = Node(None)
cur.next = tail
tail.prev = cur
cur = cur.next

M = int(input())

for _ in range(M):
    command = input().rstrip().split()
    if command[0] == 'L' and cur.prev is not None:
        cur = cur.prev
    elif command[0] == 'D' and cur.next is not None:
        cur = cur.next
    elif command[0] == 'B' and cur.prev is not None:
        if cur.prev.prev is None:
            cur.prev = None
        else:
            cur.prev = cur.prev.prev
            cur.prev.next = cur
    elif command[0] == 'P':
        node = Node(command[1])
        node.next = cur
        if cur.prev is None:
            node.prev = None
        else:
            cur.prev.next = node
            node.prev = cur.prev
        cur.prev = node

while cur.prev:
    cur = cur.prev
    
while cur.next:
    print(cur.data, end = '')
    cur = cur.next
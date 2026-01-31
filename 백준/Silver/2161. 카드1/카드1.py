import sys, collections

input = sys.stdin.readline

deq = collections.deque()

N = int(input())
for i in range(1, N + 1):
    deq.append(i)

while True:
    print(deq.popleft(), end = " ")
    N -= 1
    if N == 0:
        break
    deq.append(deq.popleft())
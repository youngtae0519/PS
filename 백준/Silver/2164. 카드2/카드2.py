import collections

N = int(input())
deq = collections.deque([])

for i in range(1, N + 1):
    deq.append(i)
    
while len(deq) != 1:
    deq.popleft()
    tmp = deq[0]
    deq.popleft()
    deq.append(tmp)
    
print(deq[0])
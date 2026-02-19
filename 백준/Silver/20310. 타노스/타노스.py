import sys
from collections import deque

input = sys.stdin.readline

S = input().rstrip()

deq = deque()
num0 = 0
num1 = 0
for i in range(len(S)):
    if S[i] == '0':
        num0 += 1
    else:
        num1 += 1
    deq.append(S[i])
    
num0 = num0 // 2
num1 = num1 // 2

ans = ''
while len(deq) > 0:
    num = deq.popleft()
    if num == '0':
        if num0 > 0:
            ans += '0'
            num0 -=1
    elif num == '1':
        if num1 > 0:
            num1 -= 1
        else:
            ans += '1'
            
print(ans)
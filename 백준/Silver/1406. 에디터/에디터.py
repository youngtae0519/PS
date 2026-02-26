import sys

input = sys.stdin.readline

s = input().rstrip()
M = int(input())

left = [c for c in s]
right = []

for _ in range(M):
    cmd = input().split()
    
    if cmd[0] == 'L' and len(left) != 0:
        right.append(left.pop())
    elif cmd[0] == 'D' and len(right) != 0:
        left.append(right.pop())
    elif cmd[0] == 'B' and len(left) != 0:
        left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[1])
        
while len(right) > 0:
    left.append(right.pop())
    
print(''.join(left))
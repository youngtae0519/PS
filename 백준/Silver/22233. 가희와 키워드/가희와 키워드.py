import sys

input = sys.stdin.readline

N, M = map(int, input().split())
s = set()

for _ in range(N):
    s.add(input().rstrip())
    
ans = []
for _ in range(M):
    arr = list(map(str, input().rstrip().split(',')))
    for item in arr:
        if item in s:
            s.remove(item)
    ans.append(len(s))
    ans.append('\n')
    
print(''.join(map(str, ans)))
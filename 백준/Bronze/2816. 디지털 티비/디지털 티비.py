import sys

input = sys.stdin.readline

N = int(input())

channel = {}
for i in range(N):
    channel[input().rstrip()] = i

ans = []
for _ in range(channel['KBS1']):
    ans.append(1)
for _ in range(channel['KBS1']):
    ans.append(4)
    
if channel['KBS1'] > channel['KBS2']:
    for _ in range(channel['KBS2'] + 1):
        ans.append(1)
    for _ in range(channel['KBS2']):
        ans.append(4)
else:
    for _ in range(channel['KBS2']):
        ans.append(1)
    for _ in range(channel['KBS2'] - 1):
        ans.append(4)
        
print(''.join(map(str, ans)))
import sys

input = sys.stdin.readline

N = int(input())
S = input().strip()

ans = []

right = S.rstrip('R')
ans.append(right.count('R'))

right = S.rstrip('B')
ans.append(right.count('B'))

left = S.lstrip('R')
ans.append(left.count('R'))

left = S.lstrip('B')
ans.append(left.count('B'))

print(min(ans))
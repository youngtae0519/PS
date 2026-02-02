import sys

input = sys.stdin.readline

ans = []
while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    if max(a, b, c) >= a + b + c - max(a, b, c):
        ans.append('Invalid')
        ans.append('\n')
    elif a == b and b == c and c == a:
        ans.append('Equilateral')
        ans.append('\n')
    elif a != b and b != c and c != a:
        ans.append('Scalene')
        ans.append('\n')
    else:
        ans.append('Isosceles')
        ans.append('\n')

print(''.join(ans))
import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    n, k, t, m = map(int, input().split())
    dic = []
    for i in range(n + 1):
        dic.append([i, [0] * (k + 1), 0, 0])
    for idx in range(m):
        i, j, s = map(int, input().split())
        dic[i][1][j] = max(s, dic[i][1][j])
        dic[i][2] += 1
        dic[i][3] = idx
    dic.sort(key = lambda x : (-sum(x[1]), x[2], x[3]))
    for idx, item in enumerate(dic):
        if item[0] == t:
            ans.append(idx + 1)
            ans.append('\n')
print(''.join(map(str, ans)))
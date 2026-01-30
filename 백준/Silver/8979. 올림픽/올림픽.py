N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x : (-x[1], -x[2], -x[3]))

g, s, b = -1, -1, -1
ans = 0
dup = 1
for item in arr:
    if item[0] == K:
        if g == -1:
            ans = 1
        elif item[1] != g or item[2] != s or item[3] != b:
            ans += dup
        break
    cur = item[1 : ]
    if cur[0] == g and cur[1] == s and cur[2] == b:
        dup += 1
    else:
        ans += dup
        dup = 1
        g, s, b = cur
        
print(ans)
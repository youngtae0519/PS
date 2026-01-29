N = int(input())

num = N
cnt = 0
while num != 0:
    cnt += 1
    num //= 10

ans = 0
for i in range(1, cnt):
    ans += 9 * (10 ** (i - 1)) * i
ans += (N - (10 ** (cnt - 1)) + 1) * cnt
    
    
print(ans)
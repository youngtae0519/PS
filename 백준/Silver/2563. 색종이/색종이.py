N = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    for dy in range(10):
        for dx in range(10):
            arr[100 - y - dy][x + dx] = 1

ans = 0
for dy in range(1, 101):
    for dx in range(1, 101):
        ans += arr[dy][dx]
        
print(ans)
N = int(input())
arr = [0 for _ in range(9)]

while N != 0:
    num = N % 10
    if num == 9:
        arr[6] += 1
    else:
        arr[num] += 1
    N = N // 10
    
if arr[6] % 2 == 1:
    arr[6] += 1
arr[6] = arr[6] // 2
    
ans = arr[0]
for i in range(1, 9):
    ans = max(ans, arr[i])

print(ans)
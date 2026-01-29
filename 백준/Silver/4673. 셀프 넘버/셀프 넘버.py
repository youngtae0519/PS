arr = [False for _ in range(10001)]
cnt = 0

for i in range(1, 10001):
    if not arr[i]:
        print(i)
    arr[i] = True
    cur = i
    while True:
        num = cur
        while num != 0:
            cur += (num % 10)
            num = num // 10
        if cur > 10000 or arr[cur]:
            break
        arr[cur] = True

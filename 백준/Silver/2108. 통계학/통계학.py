N = int(input())

arr = []
dic = {}

for _ in range(N):
    num = int(input())
    arr.append(num)
    if dic.get(num) is None:
        dic[num] = 1
    else:
        dic[num] += 1

print(round(sum(arr) / N))

arr.sort()
print(arr[N // 2])

cnt = 0
ans = []

for key, value in dic.items():
    if value > cnt:
        ans = []
        ans.append(key)
        cnt = value
    elif value == cnt:
        ans.append(key)

ans.sort()
if len(ans) == 1:
    print(ans[0])
else:
    print(ans[1])
    
print(arr[-1] - arr[0])
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
arr = []
idx = 0
for _ in range(N):
    word = input().rstrip()
    if len(word) < M:
        continue
    if dic.get(word) is None:
        dic[word] = idx
        idx += 1
        arr.append([word, 1])
    else:
        arr[dic[word]][1] += 1

arr.sort(key = lambda x : (-x[1], -len(x[0]), x[0]))

ans = []
for item in arr:
    ans.append(item[0])
    ans.append('\n')
    
print(''.join(ans))
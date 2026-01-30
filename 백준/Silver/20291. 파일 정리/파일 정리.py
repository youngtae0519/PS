import sys

input = sys.stdin.readline

N = int(input())
dic = {}
for _ in range(N):
    _, typ = map(str, input().rstrip().split("."))
    if dic.get(typ) is None:
        dic[typ] = 1
    else:
        dic[typ] += 1
    
ans = []
for key, value in dic.items():
    ans.append([key, value])
    
ans.sort(key = lambda x : x[0])

for item in ans:
    print(item[0], item[1])
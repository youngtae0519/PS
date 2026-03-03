import sys
from collections import Counter

input = sys.stdin.readline

N, d, k, c = map(int, input().split())

sushi = []
for _ in range(N):
    sushi.append(int(input()))
    
dic = Counter(sushi[ : k])

tmp = len(dic.keys())

if dic[c] == 0:
    ans = tmp + 1
    have = False
else:
    ans = tmp
    have = True

for i in range(N):
    dic[sushi[i]] -= 1
    if dic[sushi[i]] == 0:
        tmp -= 1
        del dic[sushi[i]]
        
    dic[sushi[(i + k) % N]] += 1
    if dic[sushi[(i + k) % N]] == 1:
        tmp += 1
    
    if dic[c] == 0:
        ans = max(ans, tmp + 1)
    else:
        ans = max(ans, tmp)
        
print(ans)
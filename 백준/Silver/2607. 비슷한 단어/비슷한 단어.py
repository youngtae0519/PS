import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
first = input().rstrip()
ans = 0

for _ in range(N - 1):
    word = input().rstrip()
    dic = Counter(first)
    cnt = 0
    for i in range(len(word)):
        if dic[word[i]] != 0:
            dic[word[i]] -= 1
        else:
            cnt += 1
    if sum(dic.values()) <= 1 and cnt <= 1:
        ans += 1
        
print(ans)
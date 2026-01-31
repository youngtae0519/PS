import sys

input = sys.stdin.readline

S = input().rstrip()
word = input().rstrip()

idx = 0
ans = 0
while True:
    if idx >= len(S):
        break
    if S[idx] == word[0] and S[idx : idx + len(word)] == word:
        ans += 1
        idx += len(word)
    else:
        idx += 1
        
print(ans)
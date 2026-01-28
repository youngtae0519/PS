N = int(input())
M = int(input())
S = input()

idx = 0
cur = 0
ans = 0

while True:
    if idx > M - 1 - 2:
        break
    if S[idx] == 'I' and S[idx + 1] == 'O' and S[idx + 2] == 'I':
        cur += 1
        if cur >= N:
            ans += 1
        idx += 2
    else:
        cur = 0
        idx += 1
        
        
print(ans)
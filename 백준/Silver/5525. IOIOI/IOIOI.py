N = int(input())
M = int(input())
S = input()

check = False
ans = 0

for i in range(M - (2 * N + 1) + 1):
    if S[i] == 'I':
        check = False
        cur = 'I'
        for j in range(1, 2 * N + 1):
            if cur == 'I':
                if S[i + j] == 'I':
                    check = True
                    break
                else:
                    cur = 'O'
            else:
                if S[i + j] == 'O':
                    check = True
                    break
                else:
                    cur = 'I'
    if S[i] == 'I' and not check:
        ans += 1
        
print(ans)
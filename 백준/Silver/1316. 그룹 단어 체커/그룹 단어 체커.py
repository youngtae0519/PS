N = int(input())
ans = 0

for _ in range(N):
    word = input()
    cnt = [0 for _ in range(26)]
    cur = ''
    check = False
    for c in word:
        if cur != c and cnt[ord(c) - 97] == 1:
            check = True
            break
        cnt[ord(c) - 97] = 1
        cur = c
    if not check:
        ans += 1
        
print(ans)
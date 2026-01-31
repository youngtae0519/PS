import sys

input = sys.stdin.readline

S = list(input().rstrip())

ans = [0 for _ in range(30)]
arr = []
cnt = 0
for i in range(len(S)):
    if S[i] == '(' or S[i] == '[':
        arr.append([S[i], cnt])
        cnt += 1
    elif S[i] == ')':
        if len(arr) == 0 or arr[-1][0] == '[':
            ans[0] = 0
            break
        idx = arr.pop()[1]
        if ans[idx + 1] == 0:
            ans[idx] += 2
        else:
            ans[idx] = 2 * ans[idx + 1] + ans[idx]
            ans[idx + 1] = 0
        cnt -= 1
    elif S[i] == ']':
        if len(arr) == 0 or arr[-1][0] == '(':
            ans[0] = 0
            break
        idx = arr.pop()[1]
        if ans[idx + 1] == 0:
            ans[idx] += 3
        else:
            ans[idx] = 3 * ans[idx + 1] + ans[idx]
            ans[idx + 1] = 0
        cnt -=1

if len(arr) != 0:
    print(0)
else:
    print(ans[0])
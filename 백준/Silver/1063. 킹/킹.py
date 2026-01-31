import sys

input = sys.stdin.readline

arr = list(input().rstrip().split())
K = [8 - int(arr[0][1]), ord(arr[0][0]) - 65]
S = [8 - int(arr[1][1]), ord(arr[1][0]) - 65]
N = int(arr[2])

dic = {'R': [0, 1], 'L': [0, -1], 'B': [1, 0], 'T': [-1, 0]}
for _ in range(N):
    cmd = input().rstrip()
    pos = [0, 0]
    for i in range(len(cmd)):
        pos[0] += dic[cmd[i]][0]
        pos[1] += dic[cmd[i]][1]
    
    if K[0] + pos[0] < 0 or K[0] + pos[0] > 7 or K[1] + pos[1] < 0 or K[1] + pos[1] > 7:
        continue
    if K[0] + pos[0] == S[0] and K[1] + pos[1] == S[1]:
        if S[0] + pos[0] < 0 or S[0] + pos[0] > 7 or S[1] + pos[1] < 0 or S[1] + pos[1] > 7:
            continue
        K[0] += pos[0]
        K[1] += pos[1]
        S[0] += pos[0]
        S[1] += pos[1]
    else:
        K[0] += pos[0]
        K[1] += pos[1]

ans = [chr(K[1] + 65), 8 - K[0], '\n', chr(S[1] + 65), 8 - S[0]]
print(''.join(map(str, ans)))
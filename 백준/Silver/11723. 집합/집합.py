import sys

input = sys.stdin.readline

S = [0 for _ in range(21)]
M = int(input())
ans = []
for _ in range(M):
    arr = input().rstrip().split()
    cmd = arr[0]
    if cmd == 'add':
        S[int(arr[1])] = 1
    elif cmd == 'remove':
        S[int(arr[1])] = 0
    elif cmd == 'check':
        if S[int(arr[1])] == 1:
            # ans.append('1\n')
            print(1)
        else:
            # ans.append('0\n')
            print(0)
    elif cmd == 'toggle':
        if S[int(arr[1])] == 1:
            S[int(arr[1])] = 0
        else:
            S[int(arr[1])] = 1
    elif cmd == 'all':
        for i in range(1, 21):
            S[i] = 1
    elif cmd == 'empty':
        for i in range(1, 21):
            S[i] = 0
        
# print(''.join(ans))
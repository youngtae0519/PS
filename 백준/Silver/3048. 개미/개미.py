import sys

input = sys.stdin.readline

N1, N2= map(int, input().split())

arr = []
S1 = input().rstrip()
for i in range(N1 - 1, -1, -1):
    arr.append([S1[i], 1])
S2 = input().rstrip()
for i in range(N2):
    arr.append([S2[i], -1])

T = int(input())

for i in range(T):
    idx = 0
    while True:
        if idx >= N1 + N2 - 1:
            break
        if arr[idx][1] == 1:
            if arr[idx + 1][1] == -1:
                tmp = arr[idx]
                arr[idx] = arr[idx + 1]
                arr[idx + 1] = tmp
                idx += 2
            else:
                idx += 1
        else:
            idx += 1

ans = [item[0] for item in arr]
print(''.join(ans))
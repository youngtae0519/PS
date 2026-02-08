import sys

input = sys.stdin.readline

arr = input().rstrip().split()
N = int(arr[0])
game = arr[1]

dic = {'Y': 1, 'F': 2, 'O': 3}
ans = 0
if N - 1 < dic[game]:
    print(ans)
else:
    s = set()
    cnt = 0
    for _ in range(N):
        name = input().rstrip()
        if name in s:
            continue
        else:
            s.add(name)
            cnt += 1
            if cnt == dic[game]:
                ans += 1
                cnt = 0
    
    print(ans)
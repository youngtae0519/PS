import sys

input = sys.stdin.readline

T = int(input())
ans = []

for _ in range(T):
    n = int(input())
    
    cnt = 1 + n // 2

    while True:
        n -= 3
        
        if n < 0:
            break
            
        cnt += 1 + n // 2
    
    ans.append(str(cnt) + '\n')
    
print(''.join(ans))
import sys
input = sys.stdin.readline

arr = [[0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
       [4, 0, 5, 3, 2, 5, 6, 1, 5, 4,],
       [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
       [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
       [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
       [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
       [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
       [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
       [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
       [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]]

N, K, P, X = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    k = K
    p = P
    num1 = i
    num2 = X
    
    while True:
        if k == 0:
            ans += 1
            break
        
        if arr[num1 % 10][num2 % 10] <= p:
            k -= 1
            p -= arr[num1 % 10][num2 % 10]
            num1 //= 10
            num2 //= 10
        else:
            break

print(ans - 1)
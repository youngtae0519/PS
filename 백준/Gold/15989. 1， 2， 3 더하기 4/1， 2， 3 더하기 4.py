import sys

input = sys.stdin.readline

MAX_SIZE = 100001
dp = [[0 for _ in range(4)] for _ in range(MAX_SIZE)]
dp[0][1] = 1
dp[0][2] = 1
dp[0][3] = 1

for i in range(1, MAX_SIZE):
    dp[i][1] = 1
    dp[i][2] = dp[i][1] + (dp[i - 2][2] if i >= 2 else 0)
    dp[i][3] = dp[i][2] + (dp[i - 3][3] if i >= 3 else 0)
    
T = int(input())

for _ in range(T):
    n = int(input())
    
    print(dp[n][3])
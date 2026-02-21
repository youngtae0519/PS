import sys, heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    prices = list(map(int, input().rstrip().split()))
    
    max_prices = [0 for _ in range(N)]
    max_price = -1
    for i in range(N - 1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        max_prices[i] = max_price
        
    cur_price = 0
    day = 0
    ans = 0
    for i in range(N):
        if prices[i] < max_prices[i]:
            cur_price += prices[i]
            day += 1
        elif prices[i] == max_prices[i]:
            ans += max_prices[i] * day - cur_price
            cur_price = 0
            day = 0
    
    print(ans)
H, M = map(int, input().split())

if M - 45 < 0:
    H -= 1
    if H == -1:
        H = 23
    M += 15
else:
    M -= 45
    
print(H, M)
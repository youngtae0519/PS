A, B = map(int, input().split())
C = int(input())

H = A

if B + C >= 60:
    dH = (B + C) // 60
    if A + dH >= 24:
        H = A + dH - 24
    else:
        H += dH
    M = B + C - (60 * dH)
else:
    M = B + C
    
print(H, M)
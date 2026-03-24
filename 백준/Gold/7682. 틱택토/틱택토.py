import sys
input = sys.stdin.readline

ans = []
checks = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8],
         [0, 3, 6],
         [1, 4, 7],
         [2, 5, 8],
         [0, 4, 8],
         [2, 4, 6]]

while True:
    s = input().rstrip()
    
    if s == 'end':
        break
    
    cnt1 = s.count('X')
    cnt2 = s.count('O')
    
    if cnt2 > cnt1:
        ans.append('invalid\n')
        continue
    
    first = [0 for _ in range(9)]
    second = [0 for _ in range(9)]
    
    for check in checks:
        if s[check[0]] == 'X' and s[check[1]] == 'X' and s[check[2]] == 'X':
            first[check[0]] = 1
            first[check[1]] = 1
            first[check[2]] = 1
        if s[check[0]] == 'O' and s[check[1]] == 'O' and s[check[2]] == 'O':
            second[check[0]] = 1
            second[check[1]] = 1
            second[check[2]] = 1
            
    if sum(first) == 3 or sum(first) == 5:
        if sum(second) == 0 and cnt1 - cnt2 == 1:
            ans.append('valid\n')
        else:
            ans.append('invalid\n')
    elif sum(first) >= 6:
        ans.append('invalid\n')
    elif sum(first) == 0:
        if sum(second) == 0 and cnt1 == 5 and cnt2 == 4:
            ans.append('valid\n')
        elif (sum(second) == 3 or sum(second) == 5) and cnt1 == cnt2:
            ans.append('valid\n')
        else:
            ans.append('invalid\n')
    
print(''.join(ans))
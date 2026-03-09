import sys

input = sys.stdin.readline

N = int(input())
arr = [0 for _ in range(26)]
ans = []

for _ in range(N):
    menu = input().rstrip()
    
    idx = 0
    first = False
    
    for word in menu.split():
        num = ord(word[0].upper()) - 65
        
        if arr[num] == 0:
            arr[num] = 1
            first = True
            break 
            
        idx += len(word) + 1
    
    if first:
        for i in range(len(menu)):
            if i == idx:
                ans.append('[' + menu[i] + ']')
            else:
                ans.append(menu[i])
        ans.append('\n')
    else:
        second = False
        
        for i in range(len(menu)):
            if menu[i] == ' ':
                ans.append(' ')
                continue
            
            num = ord(menu[i].upper()) - 65
            
            if arr[num] == 0 and not second:
                arr[num] = 1
                ans.append('[' + menu[i] + ']')
                second = True
            else:
                ans.append(menu[i])
       
        ans.append('\n')
                
print(''.join(ans))
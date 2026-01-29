N = int(input())
dic = {}
arr = input().split()
for num in arr:
    if dic.get(num) is None:
        dic[num] = 1
    else:
        dic[num] += 1
    
M = int(input())
arr = input().split()
for num in arr:
    if dic.get(num) is None:
        print(0, end = " ")
    else:
        print(dic[num], end = " ")
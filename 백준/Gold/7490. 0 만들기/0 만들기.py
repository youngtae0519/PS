import sys
input = sys.stdin.readline

T = int(input())

def cal(operations, N):
    tmp = ""
    num = []
    op = []
    
    for i in range(1, N + 1):
        tmp += str(i)
        
        if i < N:
            if operations[i - 1] == ' ':
                continue
            else:
                op.append(operations[i - 1])
                num.append(int(tmp))
                tmp = ""
            
    num.append(int(tmp))
    total = num[0]
    
    for i in range(len(op)):
        if op[i] == '+':
            total += num[i + 1]
        else:
            total -= num[i + 1]
            
    return total

def dfs(cur, N, operations, expressions):
    if cur == N:
        if cal(operations, N) == 0:
            results.append(expressions + str(N))
        return
    
    for op in [' ', '+', '-']:
        dfs(cur + 1, N, operations + [op], expressions + str(cur) + op)

for i in range(T):
    N = int(input())
    results = []
    
    dfs(1, N, [], "")
    
    results.sort()
    for res in results:
        print(res)
    
    if i != T - 1:
        print()
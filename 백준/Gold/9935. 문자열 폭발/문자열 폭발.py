import sys
input = sys.stdin.readline

S = list(map(str, input().rstrip()))
bomb = list(map(str, input().rstrip()))
length = len(bomb)

stack = []

for i in range(len(S)):
    stack.append(S[i])
    if len(stack) >= length and stack[-1] == bomb[-1]:
        if stack[-length : ] == bomb:
            for _ in range(length):
                stack.pop()
                
print(''.join(stack) if len(stack) > 0 else 'FRULA')
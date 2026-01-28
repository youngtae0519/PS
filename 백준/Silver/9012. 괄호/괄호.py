T = int(input())

for _ in range(T):
    S = input()
    arr = []
    ans = True
    for c in S:
        if c == '(':
            arr.append(c)
        else:
            if len(arr) == 0:
                ans = False
                break
            else:
                arr.pop()
    if not ans or len(arr) != 0:
        print("NO")
    else:
        print("YES")
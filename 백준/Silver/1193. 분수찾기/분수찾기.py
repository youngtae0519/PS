X = int(input())
cnt = 1

while True:
    if X - cnt <= 0:
        break
    X -= cnt
    cnt += 1
    
if cnt % 2 == 1:
    print(cnt + 1 - X, "/", X, sep = "")
else:
    print(X, "/", cnt + 1 - X, sep = "")
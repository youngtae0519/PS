H, W = map(int, input().split())
board = [['.' for _ in range(W)] for _ in range(H)]
time = [[-1 for _ in range(W)] for _ in range(H)]
cnt = 0
for i in range(H):
    tmp = input()
    for j in range(W):
        if tmp[j] == 'c':
            cnt += 1
            board[i][j] = 'c'
            time[i][j] = 0

while cnt != 0:
    for row in range(H):
        if board[row][-1] == 'c':
            cnt -=1
            board[row][-1] = '.'
        for col in range(W - 1, 0, -1):
            if board[row][col - 1] == 'c':
                board[row][col] = 'c'
                board[row][col - 1] = '.'
                if time[row][col] == -1:
                    time[row][col] = time[row][col - 1] + 1

for row in time:
    print(*(row))
import sys

input = sys.stdin.readline

def garo(row, col):
    bingo = True
    for i in range(5):
        if not board[row][i]:
            bingo = False
            break
    return bingo

def sero(row, col):
    bingo = True
    for i in range(5):
        if not board[i][col]:
            bingo = False
            break
    return bingo

def daegak1(row, col):
    bingo = True
    for i in range(5):
        if not board[i][i]:
            bingo = False
            break
    return bingo

def daegak2(row, col):
    bingo = True
    for i in range(5):
        if not board[i][4 - i]:
            bingo = False
            break
    return bingo

dic = {}
board = [[False for _ in range(5)] for _ in range(5)]
for i in range(5):
    arr = list(map(int, input().split()))
    for j in range(5):
        dic[arr[j]] = [i, j]

num = []
for _ in range(5):
    arr = list(map(int, input().split()))
    for item in arr:
        num.append(item)

cnt = 0
for i in range(25):
    row, col = dic[num[i]]
    board[row][col] = True
    if garo(row, col):
        cnt += 1
    if sero(row, col):
        cnt += 1
    if row == col and daegak1(row, col):
        cnt += 1
    if row + col == 4 and daegak2(row, col):
        cnt += 1
    if cnt >= 3:
        print(i + 1)
        break
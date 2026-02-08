import sys

input = sys.stdin.readline

N = int(input())
matrix = []
for i in range(N):
    matrix.append([])
    arr = input().rstrip()
    for j in range(N):
        matrix[i].append(arr[j])
        
heart_row = -1
heart_col = -1
for row in range(N):
    for col in range(N):
        if matrix[row][col] == '*':
            heart_row = row + 1
            heart_col = col
            break
    if heart_row != -1:
        break
print(heart_row + 1, heart_col + 1)

left_hand = 0
right_hand = 0
for col in range(N):
    if matrix[heart_row][col] == '*':
        if col < heart_col:
            left_hand +=1
        elif col > heart_col:
            right_hand += 1

waist = 0
for row in range(heart_row + 1, N):
    if matrix[row][heart_col] == '*':
        waist +=1
        
left_leg = 0
right_leg = 0
for row in range(heart_row + waist + 1, N):
    if matrix[row][heart_col - 1] == '*':
        left_leg += 1
    if matrix[row][heart_col + 1] == '*':
        right_leg += 1
        
print(left_hand, right_hand, waist, left_leg, right_leg)
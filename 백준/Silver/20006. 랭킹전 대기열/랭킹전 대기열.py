import sys

input = sys.stdin.readline

p, m = map(int, input().split())
total_room = []

for _ in range(p):
    I, n = map(str, input().split())
    I = int(I)
    if len(total_room) == 0:
        total_room.append([[I, n]])
    else:
        is_available = False
        for room in total_room:
            if len(room) < m and room[0][0] - 10 <= I <= room[0][0] + 10:
                room.append([I, n])
                is_available = True
                break
        if not is_available:
            total_room.append([[I, n]])

ans = []
for room in total_room:
    room.sort(key = lambda x : x[1])
    if len(room) == m:
        ans.append('Started!\n')
    else:
        ans.append('Waiting!\n')
    for player in room:
        ans.append(str(player[0]) + ' ' + player[1] + '\n')
    
print(''.join(ans))
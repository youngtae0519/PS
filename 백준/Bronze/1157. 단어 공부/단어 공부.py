word = input()
arr = [0 for _ in range(26)]

for c in word:
    arr[ord(str.lower(c)) - 97]+= 1

ans = '?'
cnt = 0
dup = False
for i in range(26):
    if arr[i] == cnt:
        dup = True
    elif arr[i] > cnt:
        ans = chr(i + 65)
        cnt = arr[i]
        dup = False
        
if dup:
    ans = '?'
    
print(ans)
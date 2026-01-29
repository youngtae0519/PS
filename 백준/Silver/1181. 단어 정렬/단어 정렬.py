N = int(input())

arr = set()
for _ in range(N):
    word = input()
    arr.add(word)

arr = list(arr)
arr.sort(key = lambda x : (len(x), x))

for c in arr:
    print(c)
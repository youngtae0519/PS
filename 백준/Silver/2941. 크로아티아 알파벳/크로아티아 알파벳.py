word = input()

ans = word.replace("c=", "1")
ans = ans.replace("c-", "2")
ans = ans.replace("dz=", "3")
ans = ans.replace("d-", "4")
ans = ans.replace("lj", "5")
ans = ans.replace("nj", "6")
ans = ans.replace("s=", "7")
ans = ans.replace("z=", "8")

print(len(ans))
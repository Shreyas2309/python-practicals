l = [1,1,2,3,2,3]

res = []

for i in l:
    if i not in res:
        res.append(i)

print(res)
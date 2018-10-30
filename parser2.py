a = [[1, 2], [3, 4], [4, 5], [5, 6]]
for i in range(len(a)):
    if i == 0:
        a.pop([i])
print(a)

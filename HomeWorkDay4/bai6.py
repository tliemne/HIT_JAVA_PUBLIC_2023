listone = list(map(int, input().split(" ")))

list1 = set(listone)
list_mang = []
for i in list1:
    list2 = []
    for j in listone:
        if j == i:
            list2.append(j)
    list_mang.append(list2)

print(list_mang)
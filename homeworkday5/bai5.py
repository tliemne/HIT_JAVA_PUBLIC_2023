inset = set(map(int,input("nhap day so: ").split()))
if 11 not in inset:
    inset.add(11)
    print("them 11 vao")
print ("set sau khi kiem tra: ")
print(inset)

somm = 11
number = {(num, somm - num) for num in inset if somm - num in inset}

retuple = tuple(number)
sum1 = sum(map(sum, retuple))

print(f"Các cặp số có tổng bằng {somm}: {retuple}")
print(f"Tổng của các cặp số: {sum1}")
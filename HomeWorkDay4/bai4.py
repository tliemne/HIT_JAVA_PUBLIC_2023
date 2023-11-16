a = int(input())
b = [int(i) for i in input().split()]
even, odd = 0, 0
for i in b:
    if i % 2 == 0:
        even += i
    else: odd += i
print("kiem tra")
print("even" if even > odd else "odd")
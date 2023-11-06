k = int(input())
for i in range(1, k + 1):
    a, b, c = str(input()), int(input()), int(input())
    d = b + c
    if(d >= 190):
        print(i, a, d, "Xuất Sắc", sep = " ")
    elif(d >= 150):
        print(i, a, d, "Giỏi", sep = " ")
    elif(d >= 100):
        print(i, a, d, "Khá", sep = " ")
    else:
        print(i, a, d, "Yếu", sep = " ")

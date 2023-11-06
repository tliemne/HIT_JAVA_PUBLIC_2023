x = int(input("nhap so tien: "))
sum=0
i=1
while sum<=x:
    sum+=i
    i = i*10 + 1
if sum==x:
    print("YES")
else:
    print("NO")
        
    
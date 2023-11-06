n,m = int(input()),int(input())
for i in range(0,n):
    s = int(input())
    k = 0
    count = 0
    d = 0
    s1=s
    while s>0:
        s //= 10
        count += 1 
    d = count - m +1
    while count >= d:
        k = k*10+(s1%10)
        s1 //=10
        count -=1
    print(s1*( 10 ** m)+k)
    

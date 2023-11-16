cnt = 0
n = int(input())
str = list(map(int,input().split()))
mang=[]
for i in str:
    mod = i%10
    if mod == 1 or mod == 3 or mod == 5 or mod == 7 or mod == 9:
        cnt+=1
        mang.append(i)
mang.sort()
print (cnt)
for i in mang:
    print(i,end=" ")
print()
            
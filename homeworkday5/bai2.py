a = set(map(int,input().split()))
m = int(input())
sum = 0
res = set()
for i in a:
    if sum + i <= m:
        res.add(i)
        sum += i
print(res)
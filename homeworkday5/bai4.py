list = input().split()
t = tuple(list)
print(t)
cnt =0
for i in t:
    if i.isdigit():
        cnt+=1
print(cnt) 
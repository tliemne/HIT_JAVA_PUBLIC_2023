str1 = input()
cnt = {}
for i in str1:
  if i in cnt:
    cnt[i] += 1
  else:
    cnt[i] = 1
print(cnt)
     
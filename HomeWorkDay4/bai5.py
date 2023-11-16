list=[]
def flatten(a):
    if(type(a) == list):
        for i in a:
            flatten(i)
    else:
        list.append(a)

s = [0, 1, [2, 3, 4], 0, [6, 0, 8,90], 10, 111, 12]
flatten(s)

print(list)
    
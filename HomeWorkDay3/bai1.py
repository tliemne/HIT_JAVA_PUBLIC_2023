import math
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
x3=int(input())
y3=int(input())
AB = math.sqrt(math.pow(y2-y1,2)+math.pow(x2-x1,2)  )
AC= math.sqrt(math.pow(y3-y1,2)+math.pow(x3-x1,2)  ) 
BC = math.sqrt(math.pow(y3-y2,2)+math.pow(x3-x2,2) )
if AB+AC>BC and AB+ BC>AC and BC+AC>AB:
    print("Đây là tam giác")
else:
    print("Không là tam gi")    
      


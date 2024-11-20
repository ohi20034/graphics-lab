import matplotlib.pyplot as plt

x1,y1 = 9,17
x2,y2= 13,22

dx= x2-x1
dy= y2-y1

p= 2*dy - dx
print(p)

points=[]
points.append((x1,y1))

xi,yi = x1,y1

while xi!=x2 and yi!=y2:
    if p<0:
        xi=xi+1
        p= p + 2*dy
    else:
        xi= xi+1
        yi = yi+1
        p = p+ 2*(dy-dx)
        
        
    points.append((xi,yi))
    
points.append((x2,y2))


x= [point[0] for point in points]
y= [point[1] for point in points]

print(points)

plt.plot(x,y,color='r',marker='o')
plt.show()
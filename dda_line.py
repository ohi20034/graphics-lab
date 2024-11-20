#DDA LINE DRAWING
# pip install matplotlib for plt

import matplotlib.pyplot as plt

x1,y1 = 1,1
x2,y2 = 4,3

dx = x2-x1
dy = y2-y1

m = dy/dx

print('m ',m)

points = []

points.append((x1,y1))


xi,yi = x1,y1

while x1!=x2 and yi!=y2:
    if(abs(dx) >= abs(dy)):
        xi = xi+1
        yi = yi + m
    else:
        yi=yi+1
        xi= xi+ 1/m

    points.append((xi,yi))

points.append((x2,y2))
print(points)

x = [point[0] for point in points]
y = [point[1] for point in points]

plt.plot(x,y,color='b',marker='o')
plt.grid(True)
plt.show()
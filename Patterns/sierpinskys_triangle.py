import matplotlib.pylab as plt
from random import randint

def midpoint(p1, p2):
	return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

width, height = 1, 1
p, q, r = (width/2, height), (0, 0), (width, 0); #This three points form a triangle
triangle = [p,q,r]
mid_point = (width/2, height/2)

for _ in range(5000): #if you increase this number, then the fractal will be more defined!
	mid_point = midpoint(mid_point, triangle[randint(0,2)])
	plt.plot(mid_point[0], mid_point[1], 'm.', markersize=2)
plt.show()	
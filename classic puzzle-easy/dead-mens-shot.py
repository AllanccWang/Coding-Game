#https://www.codingame.com/training/easy/dead-mens-shot
import numpy as np
from scipy.spatial import ConvexHull
import math

def point_in_hull(point, hull, tolerance=1e-12):
    return all((np.dot(eq[:-1], point) + eq[-1] <= tolerance) for eq in hull.equations)

n=int(input())
points=[]
for i in range(n):
    x,y=[int(j) for j in input().split()]
    points+=[[x,y]]

hull=ConvexHull(points)
m=int(input())
for i in range(m):
    x,y=[int(j) for j in input().split()]
    if point_in_hull([x,y],hull)==True:
        print("hit")
    else:
        print("miss")

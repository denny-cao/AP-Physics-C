from vpython import *

radius = 0.5
sphere_color = color.green
arrow_color = color.red

# Sphere 1
sphere1_center = vector(-1,0,10)
sphere(pos=sphere1_center, radius=radius, color=sphere_color)
arrow(pos=sphere1_center, axis=vector(0,-1,0), color=arrow_color)

# Sphere 2
sphere2_center = vector(1,1,0)
sphere(pos=sphere2_center, radius=radius, color=sphere_color)
arrow(pos=sphere2_center, axis=vector(-1,0,0), color=arrow_color)

# Sphere 3
sphere3_center = vector(1,-1,0)
sphere(pos=sphere3_center, radius=radius, color=sphere_color)
arrow(pos=sphere3_center, axis=vector(1,1,0), color=arrow_color)

while True:
    pass

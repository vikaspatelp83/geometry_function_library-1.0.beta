"""
name   : geometry.py
writer : Vikas Patel
link   : github.com/vikaspatelp83
Area module to calculate areas of various shapes.
1. circle_area(radius)
2. circle_circumference(radius)
3. rectangle_area(length, width)
4. rectangle_perimeter(length, width)
5. parallelogram_area(base, height)
6. parallelogram_perimeter(base, height)
7. trapezoid_area(pside1, pside2, height)
8. trapezoid_perimeter(pside1, pside2, side1, side2)
9. triangle_area(height, base)
10. triangle_perimeter(side1, side2, side3)
11. cuboid_volume(length, width, height)
12. cuboid_surface(length, width, height)
13. prism_volume(base,height)
14. prism_surface(base, height)
15. cylinder_volume(radius, height)
16. cylinder_surface(radius, height)
17. pyramid_volume(base, height)
18. cone_volume(radius, height, tside)
19. cone_surface(radius, height, side=m.sqrt(radius**2+height**2))
20. sphere_volume(radius)
21. sphere_surface(radius)
"""
import math as m


def circle_area(radius):
    return m.pi * radius * radius
    """circle_area(radius)"""


def circle_circumference(radius):
    return 2 * m.pi * radius
    """circle_circumference(radius)"""


def rectangle_area(length, width):
    return length * width
    """rectangle_area(length,width)"""


def rectangle_perimeter(length, width):
    return 2 * length + 2 * width
    """rectangle_perimeter(length,width)"""


def parallelogram_area(base, height):
    return base * height
    """parallelogram_area(base,height)"""


def parallelogram_perimeter(base, height):
    return 2 * base + 2 * height
    """parallelogram_perimeter(base,height)"""


def trapezoid_area(pside1, pside2, height):
    return (pside1 + pside2) * height / 2
    """trapezoid_area(pside1, pside2, height)"""


def trapezoid_perimeter(pside1, pside2, side1, side2):
    return pside1 + pside2 + side1 + side2
    """trapezoid_perimeter(pside1, pside2, side1, side2)"""


def triangle_area(height, base):
    return (height * base) / 2
    """triangle_area(height,base)"""


def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3
    """triangle_perimeter(side1, side2, side3)"""


def cuboid_volume(l, w, h):
    return l * b * h
    """cuboid_volume(length, width, height)"""


def cuboid_surface(l, w, h):
    return (2 * l * w) + (2 * w * h) + (2 * h * l)
    """cuboid_surface(length, width, height)"""


def prism_volume(base, height):
    return base * height
    """prism_volume(base,height)"""


def prism_surface(base, height):
    return 2 * base + rectangle_perimeter(base, height) * height
    """prism_surface(base, height)"""


def cylinder_volume(radius, height):
    return m.pi * radius * radius * height
    """cylinder_volume(radius, height)"""


def cylinder_surface(radius, height):
    return 2 * m.pi * radius * height + 2 * m.pi * radius * radius
    """cylinder_surface(radius, height)"""


def pyramid_volume(base, height):
    return (rectangle_area(base, base) * height) / 3
    """pyramid_volume(base, height)"""


def cone_volume(radius, height, tside):
    return (m.pi * radius * radius * height) / 3
    """cone_volume(radius, height, tside)"""


def cone_surface(radius=0, height=0, side=0):
    side = m.sqrt(radius ** 2 + height ** 2)
    r = radius
    surf = circle_area(r) + (m.pi * radius * side)
    return surf
    """cone_surface(radius, height, side=m.sqrt(radius**2+height**2))"""


def sphere_volume(radius):
    return 4 * (m.pi * (radius ** 3)) / 3
    """sphere_volume(radius)"""


def sphere_surface(radius):
    return 4 * m.pi * (radius ** 2)
    """sphere_surface(radius)"""


####### end of the module    #######
def version():
    print("geometry - 1.0.beta")


def redme():
    print(
        """		
                	<< FREE OPEN SOURCE >>
	<< GEOMETRY FORMULAS FOR AREA, VOLUME, SURFACE, PERIMETER >>
	                   <<PYTHON 3.7.1>>

	>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	^  name    : geometry.py                ^
	^  writer  : Vikas Patel                ^	
	^  github  : github.com/vikaspatelp83  	^
	^  linkedIn: linkedin.com/vikaspatelp83 ^
	^  twitter : twitter.com/DevDp430       ^
	^  website : novice-vikas.blogspot.com	^
	>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


This module contains 21 formulas for geometry to make calculations easy.

Advantages :
	1> Well written functions with full name.
	2> In line support.
	3> All functions return calculated values.

--------The functions and thier parameters are given below.----------


 Area module to calculate areas of various shapes.
*************************************************************************
 1. circle_area(radius)
 2. circle_circumference(radius)
 3. rectangle_area(length, width)
 4. rectangle_perimeter(length, width)
 5. parallelogram_area(base, height)
 6. parallelogram_perimeter(base, height)
 7. trapezoid_area(pside1, pside2, height)
 8. trapezoid_perimeter(pside1, pside2, side1, side2)
 9. triangle_area(height, base)
 10. triangle_perimeter(side1, side2, side3)
 11. cuboid_volume(length, width, height)
 12. cuboid_surface(length, width, height)
 13. prism_volume(base,height)
 14. prism_surface(base, height)
 15. cylinder_volume(radius, height)
 16. cylinder_surface(radius, height)
 17. pyramid_volume(base, height)
 18. cone_volume(radius, height, tside)
 19. cone_surface(radius, height, side=m.sqrt(radius**2+height**2))
 20. sphere_volume(radius)
 21. sphere_surface(radius)

**************************************************************************

	<<<<<<<THANKYOU FOR GIVING A CHANCE TO MY LIBRARY>>>>>>>               
""")


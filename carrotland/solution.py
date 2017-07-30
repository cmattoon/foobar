"""
 * Carrotland
 * ==========
 *
 * The rabbits are free at last, free from that horrible zombie science experiment. They need a happy, safe home, where they can recover.
 *
 * You have a dream, a dream of carrots, lots of carrots, planted in neat rows and columns! But first, you need some land. And the only person who's selling land is Farmer Frida. Unfortunately, not only does she have only one plot of land, she also doesn't know how big it is - only that it is a triangle. However, she can tell you the location of the three vertices, which lie on the 2-D plane and have integer coordinates.
 *
 * Of course, you want to plant as many carrots as you can. But you also want to follow these guidelines: The carrots may only be planted at points with integer coordinates on the 2-D plane. They must lie within the plot of land and not on the boundaries. For example, if the vertices were (-1,-1), (1,0) and (0,1), then you can plant only one carrot at (0,0).
 *
 * Write a function answer(vertices), which, when given a list of three vertices, returns the maximum number of carrots you can plant.
 *
 * The vertices list will contain exactly three elements, and each element will be a list of two integers representing the x and y coordinates of a vertex. All coordinates will have absolute value no greater than 1000000000. The three vertices will not be collinear.
 *
 * Languages
 * =========
 *
 * To provide a Python solution, edit solution.py
 * To provide a Java solution, edit solution.java
 *
 * Test cases
 * ==========
 *
 * Inputs:
 * (int) vertices = [[2, 3], [6, 9], [10, 160]]
 * Output:
 * (int) 289
 *
 * Inputs:
 * (int) vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
 * Output:
 * (int) 1730960165
 *
 * Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
 """
from fractions import gcd


class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x,y

def answer(verts):
    pts = map(lambda v: Point(*v), verts)
    edges = zip(pts[:-1], pts[-1:]) + zip(pts, pts[1:])

    # Shoelace area calculation
    a,b,c = pts
    area = abs(
        ((a.x*b.y) + (b.x*c.y) + (c.x*a.y)) -
        ((a.y*b.x) + (b.y*c.x) + (c.y*a.x))
    ) / 2.0

    def _bpoints(v):
        # Number of lattice points on a line
        # v = (v1, v2) -> (x1,y1),(x2,y2)
        return gcd(abs(v[1].x-v[0].x),abs(v[1].y-v[0].y)) - 1

    # Find number of lattice points on each edge,
    # plus the three verticies themselves
    B = sum(map(_bpoints, edges)) + 3
    
    # Solve for 'i' in Pick's Theorem
    return int(1 + area - (B/2.0))
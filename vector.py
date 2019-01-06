import tools
import math
from decimal import Decimal

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        sum = []
        for i in range(len(v.coordinates)):
            sum.append(self.coordinates[i] + v.coordinates[i])
        return Vector(sum)

    def subtract(self, v):
        diff = []
        for i in range(len(v.coordinates)):
            diff.append(self.coordinates[i] - v.coordinates[i])
        return Vector(diff)

    def scalar_mult(self, s):
        product = []
        for i in range(len(self.coordinates)):
            product.append(self.coordinates[i] * s)
        return Vector(product)

    def magnitude(self):
        sum = 0;
        for i in range(len(self.coordinates)):
            sum += math.pow(self.coordinates[i], 2);
        return math.sqrt(sum)

    def unit_vector(self):
        mag = self.magnitude()
        return self.scalar_mult(1/mag)

    def dot(self, v):
#        dot_product = 0
#        for i in range(len(self.coordinates)):
#            dot_product += Decimal(Decimal(self.coordinates[i])*Decimal(v.coordinates[i]))
#        return dot_product
	return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    def theta(self, v):
        dot_product = self.dot(v)
        return math.acos(dot_product / (self.magnitude() * v.magnitude())) 

    def isParallel(self, v):
	angle = self.theta(v)
	return self.is_zero() or v.is_zero() or angle == 0 or angle == math.pi

    def is_zero(self, tolerance=1e-10):
	return self.magnitude() < tolerance

    def isOrthogonal(self, v):
	dot_product = self.dot(v)
	return dot_product == 0

    def projection(self, b):
	unit_of_b = b.unit_vector()
	return unit_of_b.scalar_mult(unit_of_b.dot(self))

    def orthogonal_component(self, b):
	return self.subtract(self.projection(b))

    def cross(self, w):
	try:
	    x1, y1, z1 = self.coordinates
	    x2, y2, z2 = w.coordinates
	    new = [y1*z2 - y2*z1, -(x1*z2 - x2*z1), x1*y2 - x2*y1]
	    print(new)
	    return Vector(new)
	except ValueError as e:
	    msg = str(e)
	    print(msg)

    def cross_parallelogram(self, w):
	return self.cross(w).magnitude()

    def cross_triangle(self, w):
	return self.cross_parallelogram(w)/2
v = Vector([1.5,9.547,3.691])
w = Vector([-6.007,0.124,5.772])

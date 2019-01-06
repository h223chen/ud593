import tools
import math

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
        dot_product = 0
        for i in range(len(self.coordinates)):
            dot_product += self.coordinates[i]*v.coordinates[i]
        return dot_product

    def theta(self, v):
        dot_product = self.dot(v)
        return math.acos(dot_product / (self.magnitude() * v.magnitude())) 

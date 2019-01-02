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

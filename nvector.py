import math

class Vector:

    # creates a vector with specified dimension, stored as an array
    # vector elements can only be integers
    def __init__(self, dim: int):
        self.dim = dim
        self.vector_array = [0] * dim  # zero vector by default

    def __repr__(self):  # print dimension of vector
        return str(self.dim) + "-dimensional vector"

    def __setitem__(self, key, value):  # set a particular vector element
        self.vector_array[key] = value

    def __getitem__(self, index):  # more intuitive access to vector elements
        return self.vector_array[index]

    def __add__(self, other):  # elementwise vector addition
        sum_vector = Vector(max(self.dim, other.dim))
        if self.dim > other.dim:
            t = other.vector_array + [0] * (self.dim - other.dim)
            for i in range(max(self.dim, other.dim)):
                sum_vector[i] = self[i] + t[i]
        elif self.dim < other.dim:
            t = self.vector_array + [0] * (other.dim - self.dim)
            for i in range(max(self.dim, other.dim)):
                sum_vector[i] = t[i] + other[i]
        return sum_vector

    def from_list(self, l: list):  # creates a new Vector from a given list
        i = 0
        for x in l:
            try:
                self.vector_array[i] = x
                i += 1
            except IndexError:
                print("Too many elements in list!")
                break
        return self

    def to_list(self):  # returns the vector as an array
        return self.vector_array

    def dot_product(self, other):
        if self.dim == other.dim:
            dp = 0
            for i in range(self.dim):
                p = self[i] * other[i]
                dp += p
            return dp
        return None

    def norm(self):
        return math.sqrt(self.dot_product(self))


vector = Vector(2).from_list([2, 2])
zero = Vector(3)
product = vector.dot_product(zero)
print(vector)
print(vector.vector_array)
print(zero)
print(zero.vector_array)
print(product)
print(vector.norm())

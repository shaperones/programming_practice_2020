import numpy as np
lenerr = 'векторы из пространств разной мерности, введите одинаковое число координат'
typeerr = 'прнимаются числа, списки, кортежи и векторы'
typeerr1 = 'прнимаются списки, кортежи и векторы'
numerr = 'принимаются числа'

class Vector(object):

    def __init__(self, *args):
        self.vector = np.array(args)

    def __repr__(self):
        return ', '.join([str(i) for i in self.vector])

    def __str__(self):
        return ', '.join([str(i) for i in self.vector])

    def __eq__(self, other):
        return self.vector == other.vector

    def __add__(self, other):  # сложение векторов или сложение каждого элемента со скаляром
        if isinstance(other, (int, float)):
            return self.vector + other
        elif isinstance(other, Vector):
            if len(self.vector) == len(other.vector):
                return self.vector + other.vector
            else:
                raise ValueError(lenerr)
        elif isinstance(other, (list, tuple)):
            if len(self.vector) == len(other):
                return self.vector + other
            else:
                raise ValueError(lenerr)
        else:
            raise ValueError(typeerr)

    def __mul__(self, other):  # поэлементое умножение на скаляр
        if isinstance(other, (int, float)):
            return self.vector * other
        else:
            raise ValueError(numerr)

    def __len__(self):  # размерность
        return len(self.vector)

    def neg(self):  # поворот на 180
        return -self.vector

    def length(self):  # длина вектора
        return np.linalg.norm(self.vector)

    def some_normal_vec(self):  # выдает один из векторов, нормальных данному (поворачивает данный вектор на 90)
        n = np.zeros((len(self.vector)))
        n[1] = -self.vector[0]
        n[0] = self.vector[1]
        return n

    def norm(self):  # нормализует вектор
        amax = np.max(self.vector)
        amin = np.min(self.vector)
        return self.vector / max(abs(amax), abs(amin))

    def scalar_mult(self, other):
        if isinstance(other, Vector):
            return np.dot(self.vector, other.vector)
        elif isinstance(other, (list, tuple)):
            if len(self.vector) == len(other):
                return np.dot(self.vector, other)
            else:
                raise ValueError(lenerr)
        else:
            raise ValueError(typeerr1)

    def vector_mult(self, other):

        if isinstance(other, Vector):
            if len(self.vector) == len(other.vector):
                return np.cross(self.vector, other.vector)
        elif isinstance(other, (list, tuple)):
            if len(self.vector) == len(other):
                return np.cross(self.vector, other)
            else:
                raise ValueError(lenerr)
        else:
            raise ValueError(typeerr1)

    def collcheck(self, other):  # проверка на коллинеарность 2 векторов
        if np.any(self.vector_mult(other)) == 0:
            return True
        else:
            return False





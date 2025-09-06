from math import sqrt

class Triangle:
    def __init__(self, a, b, c):
        if is_triangle(a, b, c):
            self.a = a
            self.b = b
            self.c = c
        else:
            raise Exception('это не треугольник')

    def perimeter(self):
        return round(self.a+self.b+self.c, 14)
    def area (self):
        pp = self.perimeter()/2
        return sqrt(pp*(pp-self.a)*(pp-self.b)*(pp-self.c))

def is_triangle(a, b, c):
    return a<b+c and b <a+c and c< a+b

#основной код:
s = input('введите 3 стороны треугольника')
try:
    a, b, c = map(float, s.strip().replace(',', '').split(' '))
    if a>0 and c>0 and b>0:
        trrr = Triangle(a, b, c)
        print(trrr.perimeter())
    else:
        print('отрицательная длина стороны')
except Exception as e:
    print(str(e))
except:
    print('неверные данные')

x = input()
from math import sqrt
print("a = ")
a = int(input())
print("b = ")
b = int(input())
print("c = ")
c = int(input())

d = b*b - 4*a*c
if d >= 0:
    x1 = (-b + sqrt(d)) / (2*a)
    x2 = (-b - sqrt(d)) / (2*a)
    answ = "x1 = %.3f x2 = %.3f" % (x1, x2)
else:
    answ = "Дискриминант = %s. Нет решения" % d
print(answ)
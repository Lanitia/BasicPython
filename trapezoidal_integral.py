from math import sin
from math import pi
from math import pi
from math import e
# --example--
# print(sin(0))
# >>> 0
# -----------
def trapezoidal_integral(f, a=0, b=1, n=100) :
    h = (b - a) / n
    s = sum([f(a + (i - 1) * h) + f(a + i * h) for i in range(1, n+1)])    
    return h / 2 * s

#(1)
print(trapezoidal_integral(lambda x : sin(x), b=pi/2, n=50))
#(2)
print(trapezoidal_integral(lambda x : 4/(1+x**2)))
#(3)
print(trapezoidal_integral(lambda x : pi**0.5 * e**(-x ** 2), -100, 100, 1000))

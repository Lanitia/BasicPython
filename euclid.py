a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
#問３
def euclid(a, b) :
    a, b = max(a, b), min(a, b)
    while b != 0 :
        a, b = b, a % b #値の更新
    return a

print(euclid(a, b))

#問４
def mutually_prime(a, b) :
    if euclid(a, b) == 1 :
        return True
    else :
        return False
print(mutually_prime(a, b))

#エクストラ
import random
count = 0

for _ in range(100000) :
    x, y = random.randint(2, 10000), random.randint(2, 10000)
    if mutually_prime(x, y) :
        count += 1

print(count / 100000)
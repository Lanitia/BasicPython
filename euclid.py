a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
a, b = int(a), int(b)
a, b = max(a, b), min(a, b)

while 1 :
    if a % b == 0 :
        break    
    a, b = b, a % b #値の更新

print(b)
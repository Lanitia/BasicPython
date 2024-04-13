a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO

test = int(b) #この値を変更してください

def isPrime(n) :
    if str(int(n)) != n or abs(int(n)) != int(n) :
        print("type error : unexpected type")
        print("正の整数を入力してください")
    else :
        n = int(n)
        for i in range(2, int(n ** 0.5)+1) :
            if i == int(n ** 0.5) :
                return True
                break
            elif n % i == 0 :
                return False
                break

print(isPrime(a))
print(isPrime(b))
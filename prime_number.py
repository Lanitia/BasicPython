a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO

def isPrime(n) :
    if str(int(n)) != n or abs(int(n)) != int(n) or int(n) == 1:
        print("type error : unexpected type")
        print("2以上の正の整数を入力してください")
    else :
        n = int(n)
        jud = None
        if n == 2 :
            return True
        else :
            for i in range(2, int(n ** 0.5)+1) :
                if n % i == 0 :
                    jud = True
                    break
            else :
                jud = False
            return jud

print(isPrime(a))
print(isPrime(b))
a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO

test = int(b) #この値を変更してください

if test <= 1 :
    print("例外です。2以上の整数を入力してください")
elif test == 2 :
    print("2は素数")
else :
    for i in range(2, int(test ** 0.5)+1) :
        if test % i == 0 :
            print(f"{test}は素数でない")
            break
    else :
        print(f"{test}は素数")

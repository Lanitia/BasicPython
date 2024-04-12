a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO

test = int(b) #この値を変更してください


for i in range(2, int(test ** 0.5)+1) :
    if i == int(test ** 0.5) :
        print(f"{test}は素数")
        break
    elif test // i * i == test :
        print(f"{test}は素数でない")
        print(f"{i}で割り切れる")
        break


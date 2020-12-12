import random

a = [1, 3]
b = [2, 5]

def isGoOn():
    s = input("输入玩家，例如 张三，李四")

    if s == "y":
        return True
    else:
        return False

def isBao():
     return	 sum(b)>=21 or sum(a)>=21

def startGame():
    while (not isBao()and isGoOn()):
        a.append(random.randint(1,10))
    if isBao():
        if sum(a)>=21:
            print("a bao, b win. sum(a) =", sum(a))
        else:
            print("b bao, a win. sum(b) =", sum(b))

    else:
        print("b要牌")
        while (not isBao()and isGoOn()):
            b.append(random.randint(1,10))
        if isBao():
            if sum(b)>=21:
                print("b bao, a win. sum(b) =", sum(a))
        else:
            if sum(a)>sum(b):
                print("a > b   a win", sum(a))
            else:
                print("a < b, b win", sum(b))
    print(sum(a),sum(b))
    print(a,b)




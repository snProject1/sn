import random

users=[]
zhuang={}
coins=[]
xianSumpais=[]
def isGoOn():
    s = input("是否抓牌，输入y/n")
    if s == "y":
        return True
    else:
        return False
def isBao(zhuang,xianSumpais):
    # print(zhuang["pais"],xianSumpais,"=========")
    for i in xianSumpais:
        if i>=21:
            return True
    if sum(zhuang["pais"])>= 21:
        return True
def startGame(zhuang,users,xianSumpais):
    print("====闲抓======")
    while (not isBao(zhuang,xianSumpais) and isGoOn()):
        for u in users:
            u["pais"].append(random.randint(1, 10))
            xianSumpais.append(sum(u["pais"]))
    if isBao(zhuang,xianSumpais):
        if sum(zhuang["pais"]) >= 21:
            if sum(xj>=21 for xj in xianSumpais)>0:
                print("庄闲都爆点,平局")
            else:
                print("庄%s bao, 闲 win. 庄点"%sum(zhuang["pais"]))
        else:
            print("闲 bao, 庄 win. 闲点", max(xianSumpais))
    else:
        print("====庄抓======")
        while (not isBao(zhuang,xianSumpais) and isGoOn()):
            zhuang["pais"].append(random.randint(1, 10))
        if isBao(zhuang,xianSumpais):
            print(xianSumpais)
            if sum(zhuang["pais"]) >= 21:
                if sum(xj >= 21 for xj in xianSumpais) > 0:
                    print("庄闲都爆点,平局")
                else:
                    print("庄%s bao, 闲 win. 庄点" % sum(zhuang["pais"]))
            else:
                print("闲 bao, 庄 win. 闲点", max(xianSumpais))
        else:
            if sum(zhuang["pais"]) > max(xianSumpais):
                print("庄 > 闲, 庄 win，庄%d " % (sum(zhuang["pais"])))
            else:
                for x in xianSumpais:
                    if sum(zhuang["pais"])<x:
                        print("庄 < 闲, 闲 win，庄%d "%(sum(zhuang["pais"])))
                        break
    print(users, zhuang)
    xianSumpais.clear()
def userInit():
    s = input("输入玩家，例如 张三，李四")
    names = s.split(",")
    for n in names:
        user={}
        user["name"]=n
        user["coin"]=random.randint(1000,2500)
        users.append(user)
        coins.append(user["coin"])
    zInsex=coins.index(max(coins))
    zhuang["name"]=users[zInsex]["name"]
    zhuang["coin"]=users[zInsex]["coin"]
    users.remove(users[zInsex])
def faPaiInit():
    # 闲发两张
    for i in users:
        ZP = []
        XP = []
        pai1=random.randint(1,10)
        pai2=random.randint(1,10)
        XP.append(pai1)
        XP.append(pai2)
        i["pais"]=XP
        xianSumpais.append(sum(i["pais"]))
    # 庄发两张
    zpai1 = random.randint(1, 10)
    zpai2 = random.randint(1, 10)
    ZP.append(zpai1)
    ZP.append(zpai2)
    zhuang["pais"] = ZP
    # print(zhuang,"%%%%%%zhaung%%%%%%%%%")
    return zhuang,users,xianSumpais
g=1
userInit()
while True:
    # 庄闲各发两张
    zhuang, users, xianSumpais = faPaiInit()
    print("====第%d局======"%g)
    if zhuang["coin"]<100:
        print("庄破产")
        break;
    else:
        for u in users:
            if u["coin"] < 100:
                print("闲家%s金币不够100，退出游戏" % u)
                users.remove(u)
                xianSumpais.remove(sum(u["pais"]))
                # sys.exit()
        if len(users)==0:
            print("全部闲家破产")
            break
        else:
            startGame(zhuang,users,xianSumpais)
            print("本局游戏结束，每人消耗800金币")
            # print(xianSumpais)
            for x in range(0,len(users)):
                # xianSumpais[x]-=500
                users[x]["coin"]-=800
            zhuang["coin"]-=800
    g+=1




import numpy as np
import random
def isGoOn():
    s = input("输入")
    print(s == "y", "===============================================")
    if s == "y":
        return True

def isBao(a, b):
    nums = np.sum(np.array(b) > 20)
    print("庄点和", a)
    print("闲爆数量", nums)
    return (a > 20 or nums > 0)



def NobaoPanDuan(zhuang, xians):
    if zhuang["coin"] > max(xians):
        print("庄>闲,zhuang win")
    else:
        for x in xians:
            if x > zhuang["coin"]:
                print("xian >zhuang ,xian win ")
                break


def baoPanDuan(zhuang, xians):
    # zhuang bao
    if sum(zhuang["pais"]) > 20:
        # xian 也 bao
        nums = np.sum(np.array(xians) > 20)
        if nums > 1:
            print("zhuang xian dou bao ，平局")
        else:
            print("zhuang bao ,xian win ")
    # zhuang wei bao ,xian bao
    else:
        print("xian bao,zhuang win")


def start(zhuang,xians):
    print("=======闲==========")
    while ((not isBao(sum(zhuang["pais"]), xians)) and isGoOn()):
        xians.clear()
        a = random.randint(1, 10)

        for x in xian:
            x["pais"].append(a)
            xians.append(sum(x["pais"]))
        print("-----")
        print("玩家", xian)
        print("玩家点数", xians)

    if isBao(sum(zhuang["pais"]), xians):
        print("=======闲爆了==========")
        baoPanDuan(zhuang,xians)
    else:
        # =====继续======
        print("=======庄==========")
        while ((not isBao(sum(zhuang["pais"]), xians)) and isGoOn()):
            zhuang["pais"].append(random.randint(1, 10))
        if isBao(sum(zhuang["pais"]), xians):
            baoPanDuan(zhuang, xians)
        else:
            NobaoPanDuan(zhuang, xians)
    print(zhuang, xian)


def unitUser():
    name=input("输入玩家，逗号隔开")
    names=name.split(",")
    zhuang={}
    xian=[]
    coins=[]
    pais=[]
    for n in names:
        user = {}
        num=random.randint(1000,5000)
        p1 = random.randint(1, 10)
        p2 = random.randint(1, 10)
        pais.append(p1)
        pais.append(p2)
        user["name"]=n
        user["coin"]=num
        user["pais"]=pais
        coins.append(num)
        xians.append(sum(user["pais"]))
        xian.append(user)

    zIndex=coins.index(max(coins))
    zhuang["name"] = xian[zIndex]["name"]
    zhuang["coin"] = xian[zIndex]["coin"]
    zhuang["pais"] = xian[zIndex]["pais"]
    xian.remove(xian[zIndex])
    xians.remove(xians[zIndex])



    return xian,zhuang,xians

zhuang = {"name": "zhangsan", "coin": "1500", "pais": [5, 9]}
xian = [{"name": "zhangsan", "coin": "500", "pais": [5, 6]}, {"name": "lisi", "coin": "666", "pais": [8, 6]}]
xians = []
zhuang,xian,xians=unitUser()
start(zhuang,xians)







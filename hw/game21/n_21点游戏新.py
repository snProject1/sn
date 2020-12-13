import json
import random

from hw.game21.pointUtils import PointUtils

j=1
# 创建文件
# dianshuGame2=open("../log/zBao2.json",mode="w",encoding="utf-8")
# dianshuGame2=open("../log/mBao2.json",mode="w",encoding="utf-8")
# dianshuGame2=open("../log/xBao2.json",mode="w",encoding="utf-8")
dianshuGame2=open("../log/xBao1.json",mode="w",encoding="utf-8")
name = input("输入玩家姓名，逗号隔开，例如，张三，李四，王五:")
pointUtils=PointUtils()
wanjias,zhuang=pointUtils.findZhuang(name)
while pointUtils.isNext():
    print("========新一轮开始==============")
    pointUtils.initPai()
    for wj in wanjias:
        print("------玩家-----------")
        while pointUtils.isNoBao(wj) and pointUtils.isNoInLosser(wj)  and pointUtils.isGo():
            p1=random.randint(1,10)
            wj["ds"]+=p1
    # 发完牌更新庄家
    zhuang=wanjias[-1]
    eNewSet=set()
    #出结果
    for wj in wanjias:
        dict1 = {}
        x,z,v={},{},[]
        if wj["name"] not in pointUtils.loser and wj["name"]!=zhuang["name"]:
            m = "原始状况庄={}\n原始状况闲={}".format(wanjias[-1],wj)
            dict1["juNum"]=j
            dict1["people"]=len(wanjias)
            dict1["oldZhuang"]=zhuang["coin"]
            dict1["oldXian"]=wj["coin"]
            dict1["zhuangName"]=zhuang["name"]

            dict1=pointUtils.resultGo(wj,dict1)
            eset=pointUtils.loser
            for e in eset:
                eNewSet.add(e)
            dict1["exit"] =list(eNewSet)
            z["name"]=wanjias[-1]["name"]
            z["coin"]=wanjias[-1]["coin"]
            z["sf"]=wanjias[-1]["sf"]
            z["ds"]=wanjias[-1]["ds"]
            x["name"]=  wj["name"]
            x["coin"] = wj["coin"]
            x["sf"] = wj["sf"]
            x["ds"] = wj["ds"]
            v.append(z)
            v.append(x)
            dict1["list"]=v
            pointUtils.jsonlist.append(dict1)

    j+=1
dianshuGame2.write(json.dumps(pointUtils.jsonlist,ensure_ascii=False))
dianshuGame2.write("\n")
dianshuGame2.close()
print("=====游戏结束====",pointUtils.loser)



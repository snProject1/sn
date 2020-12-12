import json
import random


# def isNext():
#     return  zhuang["name"] not in loser and len(wanjias)-len(loser)>1
# def isGo():
#     s=input("是否继续 Y/N")
#     return s=="y" or s=="Y"
# def isNoBao(wanjia):
#     return  wanjia["ds"]<22
# def initPai():
#     for w in wanjias:
#         if w["name"]!=zhuang["name"]:
#             w["sf"] = "闲"
#         pai1=random.randint(1,10)
#         pai2=random.randint(1,10)
#         w["pai1"]=pai1
#         w["pai2"]=pai2
#         w["ds"]=pai1+pai2
# def resultGo(wj,dict1):
#         # 闲爆
#         if wj["ds"]>21:
#             # 庄也爆
#             if zhuang["ds"]>21:
#                 # print("zhuang xian doubao   平局")
#                 dict1["resultSF"]="平局"
#             # 闲爆庄没爆,庄win
#             else:
#                 wj["coin"]-=100
#                 wanjias[-1]["coin"]+=100
#                 # print("xian bao ,zhuang win")
#                 dict1["resultSF"] = "庄"
#         # 庄爆,闲win,游戏结束
#         elif zhuang["ds"]>21:
#             wj["coin"] += 100
#             wanjias[-1]["coin"] -= 100
#             # print("zhuang bao, xian win ")
#             dict1["resultSF"] = "闲"
#         # 都没爆,比大小
#         else:
#             if wj["ds"]>zhuang["ds"]:
#                 wj["coin"] += 100
#                 wanjias[-1]["coin"] -= 100
#                 # print("xian >zhuang ,xian win")
#                 dict1["resultSF"] = "闲"
#             else:
#                 wj["coin"] -= 100
#                 wanjias[-1]["coin"] += 100
#                 # print("xian <zhuang ,zhuang win")
#                 dict1["resultSF"] = "庄"
#         # 比完大小,看是否退出游戏,庄退出,游戏结束,闲全部退出,游戏结束
#         if wj["coin"]<100:
#             loser.add(wj["name"])
#             loglosser.append(wj["name"])
#             print("闲{}退出游戏".format(wj["name"]))
#             dict1["exit"] = loglosser
#         elif wanjias[-1]["coin"]<100:
#             print("庄{}退出游戏".format(zhuang["name"]))
#             loser.add(wanjias[-1]["name"])
#             loglosser.append(wanjias[-1]["name"])
#             print("庄{}退出游戏".format(wj["name"]))
#             dict1["exit"] = loglosser
# def isNoInLosser(wj):
#     if wj["name"]  not in loser:
#         return True
# def paixu(item):
#     return item["coin"]
# def findZhuang():
#     names = name.split(",")
#     for n in names:
#         wj = {}
#         wj["name"] = n
#         coin = random.randint(200, 300)
#         wj["coin"] = coin
#         wj["name"] = n
#         wanjias.append(wj)
#     wanjias.sort(key=paixu)
#     zhuang=wanjias[-1]
#     zhuang["sf"]="庄"
#     return wanjias,zhuang

# wanjias, zhuang, loser = [], {}, set()
# jsonlist,loglosser=[],[]
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



import json

# 判断输赢,出测试结果
def panDuan(wj):
    wjlist=wj["list"]
    # 庄爆
    if wjlist[0]["ds"] > 21:
        if wjlist[1]["ds"] > 21:
            if wj["resultSF"] == "平局":
                print("第{}局,输赢测试通过,庄对{},庄点数{},闲点数{}".format(wj["juNum"], wj["xian"]["name"],wj["zhuang"]["ds"], wj["xian"]["ds"]))
            else:
                print("第{}局,输赢测试不通过,庄对{},庄点数{},闲点数{},{}win".format(wj["juNum"], wj["xian"]["name"], wj["zhuang"]["ds"], wj["xian"]["ds"],
                                                            wj["resultSF"]))
                # print("zhuang xian doubao   平局")
        else:
            zCoin = wj["oldZhuang"] - 100
            xCoin = wj["oldXian"] + 100
            # 先有金币与测试判断一致 且赢家与测试判断一致,认为测通过
            if wj["resultSF"] == "闲" and( wj["zhuang"]["coin"]==zCoin)and( wj["xian"]["coin"]==xCoin):
                print("第{}局,输赢测试通过,庄点数{},庄对{},闲点数{},{}win".format(wj["juNum"],wj["xian"]["name"],  wj["zhuang"]["ds"], wj["xian"]["ds"],
                                                           wj["resultSF"]))
            else:
                print("第{}局,输赢测试不通过,庄对{},庄点数{},闲点数{},{}win".format(wj["juNum"],wj["xian"]["name"],  wj["zhuang"]["ds"], wj["xian"]["ds"],
                                                            wj["resultSF"]))

    # 闲爆
    elif wjlist[1]["ds"] > 21:
        zCoin = wj["oldZhuang"] + 100
        xCoin = wj["oldXian"] - 100
        # print("===",zCoin,xCoin,wj["zhuang"]["coin"],wj["xian"]["coin"])
        # print(wj)
        if wj["resultSF"] == "庄" and( wjlist[0]["coin"]==zCoin)and( wjlist[1]["coin"]==xCoin):
            print(
                "第{}局,输赢测试通过,庄对{},庄点数{},闲点数{},{}win".format(wj["juNum"],wjlist[1]["name"],  wjlist[0]["ds"], wjlist[1]["ds"], wj["resultSF"]))
        else:
            print("第{}局,输赢测试不通过,庄对{},庄点数{},闲点数{},{}win".format(wj["juNum"],wjlist[1]["name"], wjlist[0]["ds"], wjlist[1]["ds"],
                                                        wj["resultSF"]))
            # print("xian bao, zhuang win ")
    # 都没爆
    else:
        if wjlist[0]["ds"] > wjlist[1]["ds"]:
            zCoin = wj["oldZhuang"] + 100
            xCoin = wj["oldXian"] - 100
            if wj["resultSF"] == "庄" and ( wjlist[0]["coin"]==zCoin)and( wjlist[1]["coin"]==xCoin):
                print("第{}局,输赢测试通过,庄对{},庄点数{},闲点数{},{}win".format(wj["juNum"],wjlist[1]["name"], wjlist[0]["ds"], wjlist[1]["ds"],
                                                           wj["resultSF"]))
            else:
                print("第{}局,输赢测试不通过,庄对{},庄点数{},闲点数{},{}win".format(wj["juNum"], wjlist[1]["name"], wjlist[0]["ds"],wjlist[1]["ds"],
                                                            wj["resultSF"]))
                # print("xian <zhuang ,zhuang win")
        else:
            zCoin = wj["oldZhuang"] - 100
            xCoin = wj["oldXian"] + 100
            if wj["resultSF"] == "闲" and ( wjlist[0]["coin"]==zCoin)and( wjlist[1]["coin"]==xCoin):
                print("第{}局,输赢测试通过,庄对{},庄点数{},闲点数{},{}win".format(wj["juNum"],wjlist[1]["name"],  wjlist[0]["ds"], wjlist[1]["ds"],
                                                           wj["resultSF"]))
            else:
                print("第{}局,输赢测试不通过,庄对{},庄点数{},闲点数{},{}win".format(wj["juNum"], wjlist[1]["name"], wjlist[0]["ds"], wjlist[1]["ds"],
                                                            wj["resultSF"]))
                # print("xian >zhuang ,xian win")
    if wjlist[1]["coin"] < 100:
        loser.add(wjlist[1]["name"])
        print("闲{}退出游戏".format(wjlist[1]["name"]))


def isPo(wj):
    # print(wj)
    wjlist = wj["list"]
    if wjlist[0]["coin"] < 100:
        if wjlist[0]["zhuangName"] in wj["exit"]:
            print("第{}局,破产测试通过,庄金币{},庄破产".format(wj["juNum"], wj["oldZhuang"]))
        else:
            print("第{}局,破产测试通过,庄金币{},庄破产".format(wj["juNum"], wj["oldZhuang"]))
            # print("庄破产,游戏结束")
        return False
    elif wj["people"]-len(loser)==1:
        b=list(loser)
        b.sort()
        a=wj["exit"]
        a.sort()
        if b==a:
            print("第{}局,破产测试通过,闲全部破产".format(wj["juNum"]))
        else:
            print("第{}局,破产测试不通过,闲全部破产".format(wj["juNum"]))
        return False
    else:
        return True


loser=set()
dianshuGame=open("../log/xBao1.json",mode="r",encoding="utf-8")
# dianshuGame=open("../log/zBao2.json",mode="r",encoding="utf-8")
# dianshuGame=open("../log/xBao2.json",mode="r",encoding="utf-8")
# 拿到日志,开始判断
contents=json.load(dianshuGame)

for wj in contents:
    # 庄没有破产且玩家人数大于1,出结果
    if isPo(wj):
        panDuan(wj)
        isPo(wj)








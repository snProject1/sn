import random


class PointUtils:
    wanjias, zhuang, loser = [], {}, set()
    jsonlist = []

    def isNext(self):
        return self.zhuang["name"] not in self.loser and len(self.wanjias)-len(self.loser)>1

    def isGo(self):
        s = input("是否继续 Y/N")
        return s == "y" or s == "Y"

    def isNoBao(self,wanjia):
        return wanjia["ds"] < 22

    def initPai(self):
        for w in self.wanjias:
            if w["name"] != self.zhuang["name"]:
                w["sf"] = "闲"
            pai1 = random.randint(1, 10)
            pai2 = random.randint(1, 10)
            w["pai1"] = pai1
            w["pai2"] = pai2
            w["ds"] = pai1 + pai2

    def resultGo(self,wj, dict1):
        # 闲爆
        if wj["ds"] > 21:
            # 庄也爆
            if self.zhuang["ds"] > 21:
                # print("zhuang xian doubao   平局")
                dict1["resultSF"] = "平局"
            # 闲爆庄没爆,庄win
            else:
                wj["coin"] -= 100
                self.wanjias[-1]["coin"] += 100
                # print("xian bao ,zhuang win")
                dict1["resultSF"] = "庄"
        # 庄爆,闲win,游戏结束
        elif self.zhuang["ds"] > 21:
            wj["coin"] += 100
            self.wanjias[-1]["coin"] -= 100
            # print("zhuang bao, xian win ")
            dict1["resultSF"] = "闲"
        # 都没爆,比大小
        else:
            if wj["ds"] > self.zhuang["ds"]:
                wj["coin"] += 100
                self.wanjias[-1]["coin"] -= 100
                # print("xian >zhuang ,xian win")
                dict1["resultSF"] = "闲"
            else:
                wj["coin"] -= 100
                self.wanjias[-1]["coin"] += 100
                # print("xian <zhuang ,zhuang win")
                dict1["resultSF"] = "庄"
        # 比完大小,看是否退出游戏,庄退出,游戏结束,闲全部退出,游戏结束
        if wj["coin"] < 100:
            self.loser.add(wj["name"])
            print("闲{}退出游戏".format(s))
        elif self.wanjias[-1]["coin"] < 100:
            self.loser.add(self.wanjias[-1]["name"])
            print("庄{}退出游戏".format(self.wanjias[-1]["name"]))

        return dict1

    def isNoInLosser(self,wj):
        if wj["name"] not in self.loser:
            return True

    def paixu(self,item):
        return item["coin"]

    def findZhuang(self,name):
        names = name.split(",")
        for n in names:
            wj = {}
            wj["name"] = n
            coin = random.randint(200, 300)
            wj["coin"] = coin
            wj["name"] = n
            self.wanjias.append(wj)
        self.wanjias.sort(key=self.paixu)
        self.zhuang = self.wanjias[-1]
        self.zhuang["sf"] = "庄"
        return self.wanjias, self.zhuang
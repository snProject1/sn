import random

msg=""
def caiPanInit():
    caiPanList=[]
    erwei = []
    # 生成中奖码和彩票盘  和用户金额
    zjMa = random.sample(range(1, 10), k=2)
    cpMa = random.sample(range(1, 28), k=25)

    k=0
    for i in range(5):
        hang=[]
        for j in range(1,6):
            caiPan = {}
            caiPan["x"] = i
            caiPan["y"] = j
            caiPan["ma"] = cpMa[i]
            caiPanList.append(caiPan)
            hang.append(cpMa[k])
            k+=1
        erwei.append(hang)
    return  caiPanList,zjMa,erwei
def isExit(coin):
    # 3破产停止
    if coin>=1:
        return True
    else:
        print("破产{}".format(coin))
        return False
# 不退出开始刮奖   金币够开始刮奖，，中途刮到最大奖项，所有奖项都刮开，手动输入结束  停止游戏
def mprint(s,zjMa,erwei):
    # print("%10s"%"右对齐，展位10")
    # print("%-10s"%"左对齐，展位10")
    # print("%.2s"% "截取两位字符串")
    # print("%10.2s"%"占位10，截取两位字符串")
    print("----{}----".format(s))
    print("      趣味彩票      ")
    print("中奖号码为:{}".format(zjMa))
    for i in range(len(erwei)):
        for j in range(len(erwei[i])):
            print("%-4s"%erwei[i][j],end="")
        print("")
def startGame(coin):
    global msg
    print("现有{}元".format(coin))
    erweiinit = []
    caiPanList, zjMa, erwei = caiPanInit()
    for e in range(6):
        if e == 0:
            er = [" "] + [1, 2, 3, 4, 5]
        else:
            er = [e] + ["+"] * 5
        erweiinit.append(er)
    # 打印初始盘
    mprint("刮奖前",zjMa, erweiinit)
    print("中奖码{}，金币{}".format(zjMa, coin))
    # 中奖的数量
    zjNum = 0
    fleg=True
    while isExit(coin) and fleg:
        sinput=input("请输入要刮的位置，以逗号隔开 例如x(1-5),y(1-5)")
        nums=sinput.split(",")
        x=int(nums[0])
        y=int(nums[1])
        if 1<=x<=5and 1<=y<=5:
            # 更新要刮的位置
            erweiinit[x][y] = erwei[x - 1][y - 1]
            isY=input("您是否退出(Y/N)")
            #4手动输入结束停止
            if isY=="Y" or isY=="y":
                msg="选择停止游戏"
                break
            else:
                # 出结果,结算金币
                # 判断是否中奖
                for z in range(len(zjMa)):
                    if zjMa[z] == erwei[x-1][y-1]:
                        zjNum += 1
                        # 1.大奖终止
                        if zjNum == 2:
                            coin += 50
                            msg="奖励50元"
                            fleg=False
                            break
                        else:
                            coin += 5
                            msg="恭喜中奖，奖励5元"
                    # 2中最大额度终止
                    elif erwei[x-1][y-1] == max(zjMa):
                        msg="中了最大额度{}".format(max(zjMa))
                        fleg = False
                        break
                    elif erwei[x-1][y-1] not in zjMa:
                        # 未中奖
                        if z==1:
                            msg = "谢谢参与" + str(z)
                    else:
                        pass
                if isExit(coin):
                    fleg=False

            #5.全部都刮过，停止
            isGua=True
            for e in erweiinit:
                if "+" in e:
                    isGua=False
                    break
            if isGua:
                break
        else:
            print("没有您输入的位置，请重新输入")

    # 打印最终键盘
    mprint("刮奖后",zjMa, erweiinit)
    return coin
def initUser():
    uname=input("输入用户名：")
    coin = random.randint(10, 20)
    return uname,coin
uname,coin=initUser()
print("原始{}元".format(coin))


def isBuy():
    s=input("是否购买彩票")
    return s=="Y" or s=="y"
while isBuy():
    coin -= 5
    coin=startGame(coin)
    print("------",coin)
    print("玩家{}中奖结果{},余额{}".format(uname,msg,coin))
# print("玩家停止购买彩票")







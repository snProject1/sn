"""
1. 现有一个补水站 水量无限  有一个7升的和一个4升的容器 请设计一个程序可以精确的计量出9升水
"""

wall1,wall2,target=4,7,9
i=0
print("现有{}升水".format(i))
while i<target:
    i+=wall2-wall1
    print("7升容器装满倒入4升容器中，保留剩余的{}升水，两个容器都倒掉".format(wall2-wall1))
print("现有{}升水".format(i))
import random

'''
2.3个开关在屋外 3盏灯在屋内 开关只能同时起一个并且只能进屋一次 请设计一个程序 判断开关和灯的对应关系
'''
# kaiguan,deng,dengDicts=[1,2,3],["d1","d2","d3"],[]
# # 初始化灯泡信息
# k=random.sample(range(0,len(kaiguan)),3)
# d=random.sample(range(0,len(deng)),3)
# for i in range(0,len(k)):
#     dengDict={}
#     dengDict["kg"]=kaiguan[k[i]]
#     dengDict["deng"]=deng[d[i]]
#     dengDict["isHot"]="n"
#     dengDict["isLiang"]="n"
#     dengDict["isKai"]="n"
#     dengDicts.append(dengDict)
# print(dengDicts)
# # 开始操作
# print("========开下一盏灯要关闭上一盏灯============")
# a=True
# while a:
#     kg=int(input("输入要操作的开关"))
#     if kg not in kaiguan:
#         print("没有这个开关,请重新输入")
#     else:
#         isOn=input("是否开灯Y/N")
#         for i in dengDicts:
#             if kg==i["kg"] and (isOn=="Y" or isOn=="y"):
#                 i["isHot"] = "y"
#                 i["isLiang"] = "y"
#                 i["isKai"] = "y"
#             if kg==i["kg"] and (isOn=="N" or isOn=="n"):
#                 i["isHot"] = "n"
#                 i["isLiang"] = "n"
#         b = False
#         for i in dengDicts:
#             if i["isKai"] == "N" or i["isKai"] == "n":
#                 b = True
#         a = b
#         if b:
#             isDoor=input("是否开门Y/N")
#             if isDoor == "Y" or isDoor == "y":
#                 break
#         else:
#             print("您已经全部都操作过开关了~")
#
# print(dengDicts)
# # 出结果
# for i in dengDicts:
#     if i["isKai"]=="Y" or i["isKai"]=="y":
#         print("您操作的开关是{}，对应的灯是{}".format(i["kg"],i["deng"]))
#     if i["isKai"]=="N" or i["isKai"]=="n":
#         print("您没有操作的开关是{}，对应的灯是{}".format(i["kg"],i["deng"]))

'''
3. 小明、小红、小刚是同班同学，且坐在同一排，分别坐在第一位、第二位、第三位。
由于他们的身高都差不多，所以，老师计划让他们三个轮流坐在第一位。
每次换座位的时候，第一位变第三位，后面两位都往前一位
'''
# students = ['小明','小红','小刚']
# print("原来的座位顺序是：",students)
# for i in range(3):
#     removeStu=students.pop(-1)
#     students.insert(0,removeStu)
#     print("更换座位后顺序是：", students)


'''
4.一天小明、小刚、小红在一起聊天 .小明说：“不存在大于 五分之一且小于三分之一的数.”
小刚说：“不对,只有一个得这样的分数,他就是4分之1、“小红接着说：你们说的都不对、这这样分数有无数个、：同学们、你知道他们三个人中谁的说法 是正确的?请输出所有满足要求的数
'''

# a,b=1/5,1/3
# # 分子 分母
# i,j,c=1,3,[]
# while i<500 and j<500:
#     value=i/j
#     s="{}/{}".format(i,j)
#     if a<value<b:
#         # print(value,i,j)
#         c.append(s)
#         i+=1
#         j+=1
#     elif value<=a:
#         i+=1
#     elif value >=b:
#         j+= 1
# if len(c)>0:
#     print("存在这样的数字，小明是错的")
# if len(c)>1 and "1/4" in c:
#     print("这样的分数不止1/4一个")
#     print("分子分母在500以内，满足条件的有{}个,小红说的是对的".format(len(c)))
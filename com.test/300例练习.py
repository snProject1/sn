# 1.反转三位数的整数
# 2.合并两个升序的数组，为一个新的升序数组
#3. 旋转字符串，按照给定的偏移量顺时针旋转
# 4.根据运动员得分得到相对排名，第一二三是金银铜，再往后是四五六。。。。
# 5.二分查找
# 6.A是B的子集，找出A的元素在B中下一个比当前元素大的下标
# 7.找出字符串中的单词数



# a=546
# bai=a//100
# shi=a//10%10
# ge=a%10
# newNum=ge*100+shi*10+bai
# print(bai,shi,ge,newNum)

# a=[1,2,4]
# b=[3,4,6,7]
# i,j=0,0
# n=[]
# while i<len(a) and j<len(b):
#     if a[i]<b[j]:
#         n.append(a[i])
#         i+=1
#     else:
#         n.append(b[j])
#         j+=1
# while i<len(a):
#     n.append(a[i])
#     i+=1
# while j<len(b):
#     n.append(b[j])
#     j+=1
# print(n)


# s="asdfgh"
# # s="asdfgh asdfgh"
# pianyi=4
# ns=(s+s)[len(s)-pianyi:len(s+s)-pianyi]
# print(ns)



# a=[23,43,2,45,0]
# b=[]
# c={}
# for i in range(len(a)):
#     c[a[i]]=i
# a.sort(reverse=True)
# for i in range(len(a)):
#     res=""
#     if i==0:
#         res="jin"
#     elif i==1:
#         res="yin"
#     elif i==2:
#         res="tong"
#     else:
#         res=i+1
#     c[a[i]]=res
# print("各运动员成绩对应的等级是{}".format(c))


# def findNums(a,start,end,target):
#     middle=(start+end)//2
#     for i in range(len(a)):
#         if start>end:
#             return -1
#         if a[middle]>target:
#             return  findNums(a,0,middle-1,target)
#         elif a[middle]==target:
#             return middle
#         elif a[middle]<target:
#             return findNums(a,middle+1,end,target)
#
# a = [2, 3, 5, 7, 23, 45]
# b=findNums(a,0,len(a)-1,4)
# c=findNums(a,0,len(a)-1,2)
# d=findNums(a,0,len(a)-1,45)
# e=findNums(a,0,len(a)-1,44)
# print(b,c,d,e)
# from math import sqrt
#
# lirun=float(input("请输入奖金"))
# jiangjin=0
# if lirun<0:
#     print("输入的利润不合理")
# else:
#     if 0<=lirun<100000:
#         jiangjin=lirun*0.1
#     elif 100000<lirun<=200000:
#         jiangjin=100000*0.1+(lirun-100000)*0.075
#     elif 200000<lirun<=400000:
#         jiangjin=100000*0.1+100000*0.075+(lirun-200000)*0.05
#     elif 400000<lirun<=600000:
#         jiangjin=100000*0.1+100000*0.075+200000*0.05+(lirun-400000)*0.03
#     elif 600000<lirun<=1000000:
#         jiangjin=100000*0.1+100000*0.075+200000*0.05+200000*0.03+(lirun-600000)*0.15
#     elif 1000000<lirun:
#         jiangjin = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.15+(lirun-1000000)*0.01
#
#     print("利润是{}奖金是{}".format(lirun,jiangjin))
import random
from math import sqrt
# 一个整数加上100是一个完全平方数，再加上168又是一个完全平方数，这个数是多少
# i=0
# while True:
#     a = sqrt(i+100)
#     print(a)
#     if a * a == i:
#         b = sqrt(i + 268)
#         if b * b== i:
#             print(i)
#             break
#     i+=1
# for i in range(1,1000):
#     for j in range(1,1000):
#         for k in range(1,1000):
#             if (i+100)==j*j and (i+268)==k*k:
#                 print (i)

# i=-100
# while i<1000:
#     a = int(sqrt(i+100))
#     b = int(sqrt(i + 268))
#     if a*a==(i+100) and b*b==(i+268):
#         # print(a, b)
#         print(i)
#         # break
#     i += 1

# 输入年月日，判断是今年的第几天
# s=input("请输入年月日，例1999.9.9")
# datas=s.split(".")
# year=int(datas[0])
# tian=0
# 判断是否是闰年
# for i in range(int(datas[1])):
#     if i in (1,3,5,7,8,10,12):
#         tian+=31
#     elif i in (4,6,9,11):
#         tian+=30
#     elif i ==2:
#         if (year % 4 == 0 and year % 100 == 0) or year % 400 == 0:
#             tian+=29
#         else:
#             tian+=28
#     print(tian)
# tian+=int(datas[2])
#
# print("{}是今年的第{}天".format(datas[0],tian))

# a=int(input("输入数字："))
# b=int(input("输入数字："))
# c=int(input("输入数字："))
# d=[a,b,c]
# d.sort()
# print(d)


#数列
# q,w=0,1
# a=[q,w]
# for i in range(10):
#     q,w =w,q+w
#     a.append(w)
# print(a)
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={}  ".format(i,j,i*j),end="")
#     print("")

# kaiguan=[1,2,3]
# dengpao=["d1","d2","d3"]
# dengpaos=[]
# kg=random.sample(range(0,len(kaiguan)),3)
# dp=random.sample(range(0,len(kaiguan)),3)
# # 初始化开关和灯泡
# for i in range(3):
#     every={}
#     every["kg"]=kaiguan[kg[i]]
#     every["dp"]=dengpao[dp[i]]
#     every["isHot"]="n"
#     every["isLiang"]="n"
#     every["isKai"]="n"
#     dengpaos.append(every)
# print("起始的开灯状态是：",dengpaos)
# print("========开启第二盏灯时，要把第一盏灯关闭==============")
# # 开始操作开关
# a=True
# while a:
#     switch = int(input("输入要操作的开关"))
#     isOnLight = input("是否开/关灯 Y/N")
#     for i in dengpaos:
#         if i["kg"] == switch:
#             if (isOnLight == "Y" or isOnLight == "y"):
#                 i["isKai"] = "y"
#                 i["isHot"] = "y"
#                 i["isLiang"] = "y"
#             elif isOnLight == "N" or isOnLight == "n":
#                 i["isHot"] = "n"
#                 i["isLiang"] = "n"
#     b=False
#     for i in range(len(dengpaos)):
#         if dengpaos[i]["isKai"]=="N" or dengpaos[i]["isKai"]=="n":
#             b=True
#     a=b
#     if b:
#         isOnDoor = input("是否开/开门 Y/N")
#         if isOnDoor == "Y" or isOnDoor == "y":
#             break
#
#
# for i in dengpaos:
#     if i["isKai"]=="N" or i["isKai"]=="n":
#         print("您没有开启的灯是{}，对应的开关是{}".format(i["dp"],i["kg"]))
#     else:
#         print("您开启的灯是{}，对应的开关是{}".format(i["dp"], i["kg"]))
# print("最终的开灯状态是：",dengpaos)



# 1.反转三位数的整数
# a=223
# bai=a//100
# shi=a//10%10
# ge=a%10
# print(ge*100+shi*10+bai)


# 2.合并两个升序的数组，为一个新的升序数组
# a,b,c=[2,3,4],[1,2,6,8],[]
# i,j=0,0
# while i<len(a) and j<len(b):
#     if a[i]<b[j]:
#         c.append(a[i])
#         i+=1
#     elif a[i]>b[j]:
#         c.append(b[j])
#         j+=1
#     elif a[i]==b[j]:
#         c.append(b[j])
#         c.append(a[i])
#         j += 1
#         i+=1
# while j<len(b):
#     c.append(b[j])
#     j += 1
# while i<len(a):
#     c.append(a[i])
#     i += 1
# print(c)

#3. 旋转字符串，按照给定的偏移量顺时针旋转 asdfghjkl asdfghjkl
# a,target="asdfghjkl",3
# s=a+a
# print(s[len(a)-target:len(s)-target])

# 4.根据运动员得分得到相对排名，第一二三是金银铜，再往后是四五六。。。。
# score,geren=[23,3,45,6,55,56],{}
#
# for s in range(len(score)):
#     geren[score[s]]=s
# score.sort(reverse=True)
# res = 0
# for s in range(len(score)):
#     if s==0:
#         res="jin"
#     elif s==1:
#         res="yin"
#     elif s==2:
#         res="tong"
#     else:
#         res=s+1
#     geren[score[s]]=res
# print(geren)

# 5.二分查找
# def findTarget(a, targt,start,end):
#     middle=(start+end)//2
#     if start>end:
#         return -1
#     if a[middle]>targt:
#         return  findTarget(a,targt,start,middle-1)
#     elif a[middle]<targt:
#         return  findTarget(a,targt,middle+1,end)
#     elif a[middle]==targt:
#         return middle
#
# a,targt=[2,4,5,6,7,8],8
# print(findTarget(a,targt,0,len(a)-1))

# 6.A是B的子集，找出A的元素在B中下一个比当前元素大的下标
# a,b,c=[2,4,1],[2,5,6,4,5,1],[]
# 只找比子集大的值下标
# for i in range(len(a)):
#     for j in range(b.index(a[i]),len(b)):
#         if a[i]<b[j]:
#             c.append(j)
#             break
#         elif j==len(b)-1:
#             c.append(-1)
#             break
# print(c)
# a,b,c,d=[2,4,1],[2,5,6,4,7,1],[],{}
# 找到大集合所有值对应的下一个更大的值
# for x in b:
#     while c and c[-1]<x:
#         print(c[-1])
#         d[c[-1]]=x
#         del c[-1]
#     c.append(x)
# for i in c:
#     print(i)
#     d[i]=-1
# print([d[i] for i in a])
# 7.找出字符串中的单词数
# s="my name is lxr, j"
# res=0
# for i in range(len(s)):
#     if s[i].isspace():
#         res+=1
#     elif (not s[i].isspace()) and i==len(s)-1:
#         res += 1
# print(res)

# 根据字符对应的十进制值，判断26个字符的包含情况
# a,b,c="qwe","qwert",True
# arr=[0]*26
# for i in b:
#     arr[ord(i)-ord("a")]+=1
# for i in a:
#     arr[ord(i)-ord("a")]-=1
#     if arr[ord(i)-ord("a")]<0:
#         c=False
# print(c)

#
# 返回不重复的两个数字
# a=[2,3,4,2,3,7]
# print ('50 & 10 ', 50&10)
# print ('50 | 10 ', 50|10)
# print ('50 ^ 10 ', 50^10)
# print ('10 >> 2', 10 >> 2)
# print ('10 << 2', 10 << 2)
# ans=[0,0]
# for i in a:
#     print(ans[0],i,ans[0]^i)
#     ans[0]=ans[0]^i
# c=1
# while c & ans[0]!=c:
#     c=c<<1
# for i in a:
#     if i&c==c:
#         ans[1]=ans[1]^i
# ans[0]=ans[0]^ans[1]
# print(ans)

# a=[2,3,4,2,3,7]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a.count(a[i])==1:
#             print(a[i])
#             break

# a,b=[2,2,2],[3,3,3]
# if len(a)==0 or len(b)==0 or len(a)!=len(b):
#     print("没有点积")
# else:
#     # 6+16+25
#     c=0
#     for i in range(len(a)):
#         c+=a[i]*b[i]
#     print(c)



#找出列表中和最接近，但不超过目标值的两个数字

# def mfind(nums,start,end,target):
#     c = 0x7fffffff
#     while start<end:
#         if nums[start]+nums[end]>target:
#             end-=1
#         else:
#             c=min(c,target-a[start]-a[end])
#             # print(c)
#             start+=1
#
#     return  target-c
#
# a=[2,4,1,5,12,9]
# a.sort()
# print(mfind(a,0,len(a)-1,20))






# def mfind(a, start, end, target):
#     c=0x7fffffff
#     while start<end:
#         print(a[start]+a[end])
#         if a[start]+a[end]<target:
#             start+=1
#             c=min(c,target-a[start]-a[end])
#         else:
#             end-=1
#
#     return target-c
#
# a=[2,4,1,5,12,9]
# a.sort()
# print(a)
# print(mfind(a,0,len(a)-1,5))


# s="qweoab"
# ss="ewqoba"
# oddS,eventS,oddT,evendT=[],[],[],[]
# # 奇数二进制尾是1 偶数是0
# for i in range(len(s)):
#     if i&1:
#         oddS.append(s[i])
#         oddT.append(ss[i])
#     else:
#         eventS.append(s[i])
#         evendT.append(ss[i])
# print(oddS,oddT,eventS,evendT)
# oddS.sort()
# oddT.sort()
# eventS.sort()
# evendT.sort()
# print(oddS,oddT,eventS,evendT)
# a=0
# for i in range(len(oddS)):
#     if oddS[i]!=oddT[i]:
#         a=-1
# for i in range(len(eventS)):
#     if eventS[i]!=evendT[i]:
#         a=-1
# print(a)

# !/usr/bin/python3

import sys
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()




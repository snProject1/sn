#15 成绩>90 ---A  60-89 B  <60 C
# while True:
#     s=int(input("请输入成绩"))
#     grade=""
#     if s>90:
#         grade="A"
#     elif 60<=s<89:
#         grade="B"
#     elif s<60:
#         grade="C"
#     print("该学生的成绩等级是%s"%grade)
#     print("停止输入回车。。。。。。。")
#     isst=input("是否停止y/s")
#     if isst=="y":
#         break

# 17 输入字符，统计英文字母 空格 数字 其他字符的个数
# 3kongge 3shuzi 4zimu 2teshu
# s="12 2 jkl;' p"
# zimu=0
# shuzi=0
# kongge=0
# qitazifu=0
# for i in s:
#     if i.isspace():
#         kongge+=1
#     elif i.isdigit():
#         shuzi+=1
#     elif not i.isalnum():
#         qitazifu+=1
#     elif i.isalpha():
#         zimu+=1
# print("英文字母%d 数字%d 其他字符%d 空格%d"%(zimu,shuzi,qitazifu,kongge))

#求 s=a+aa+a...
# 3+33+333
# a=int(input("输入要计算的值"))
# n=int(input("输入位数"))
# sn = 0
# num = 0
# if n==1:
#     sn=a
# else:
#     num=a
#     sn=num
#     print(num)
#     for i in range(1,n):
#         num=(num*10+a)
#         print(num)
#         sn+=num
#
# print("he",sn)

# 28. 第五个人多少岁 第一个人10岁 ，后面每个人比前面的人大两岁


# def poe(i):
#     if 1<i<=5:
#         i-=1
#         n=poe(i)+2
#     else:
#         n=10
#     return  n
# print(poe(5))

# 不超过5位的正整数，求是几位数，并且逆向打印
# num=int(input("输入正整数"))
# a=num//10000
# b=num//1000%10
# c=num//100%10
# d=num//10%10
# e=num%10
# def niXiang(n):
#     if a>0:
#         print("五位数")
#         print(e,d,c,b,a)
#     elif b>0:
#         print("四位数")
#         print(e, d, c, b)
#     elif c>0:
#         print("三位数")
#         print(e, d, c)
#     elif d>0:
#         print("2位数")
#         print(e, d)
#     elif e>0:
#         print("1位数")
#         print(e)
# niXiang(num)



# Monday  Tuesday  Wednesday  Thursday  Friday  Saturday  Sunday



# letter = input(":字母")
#
# while letter != 'Y':
#     if letter == 'S':
#         print( 'please input second letter')
#         letter = input(":字母")
#
#         if letter == 'a':
#             print( 'Saturday')
#         elif letter == 'u':
#             print( 'Sunday')
#         else:
#             print ('data error')
#         break
#     elif letter == 'P':
#         print ('Friday')
#         break
#     elif letter == 'M':
#         print ('Monday')
#     #break
#     elif letter =='T' :
#         print ('please input second letter')
#         letter =input(":字母")
#
#         if letter == 'u':
#             print ('Tuesday')
#         elif letter == 'h':
#             print( 'Thursday')
#         else:
#             print ('data error')
#             break
#     elif letter == 'W':
#         print( 'Wednesday')
#     else:
#         print ('data error')
#     letter = input(":字母")

# 100以内的素数
# sushu=[]
# for i in range(2, 100):
#     for j in range(2, i + 1):
#         # 模除等于0，且不是自己本身，是合数
#         if i % j == 0 and i != j:
#             break
#         # 模除等于0，且是自己本身，是素数
#         elif i % j == 0 and i == j:
#             sushu.append(i)
#             break
#
# print(sushu)

#排序
# a=[2,4,1,90,7,8,999,66,50,3]
#
# for i in range(0,len(a)):
#     for j in range(0,i+1):
#         if a[j]>a[j+i]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)

# a=0
# for i in range(0,100):
#     a+=1
# print(a)
import calendar
import unittest

# x,y=10,20
# maxnum=lambda x,y:True
# minnum=lambda x,y:False
# print(maxnum(x,y),minnum(x,y))

# a=[2,3,5,1]
# isA=lambda a: a.sort()
# isA(a)
# print(a)
import time
# 时间戳
# t=time.time()
# # print(t)
# # 当地时间
# n=time.localtime(t)
# # print(n)
# # 格式化时间
# # gt=time.asctime(n)
# gt=time.strftime("%Y-%m-%d %H:%M:%S",n)
# print(gt)
# t=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
# print(t)



# day=calendar.month(2020,2,w=2,l=1)
# print(day)
# c=calendar.calendar(2020,w=1,l=1,c=3)
# print(c)
# c=calendar.isleap(2004)
# print(c)
# d=calendar.leapdays(2000,2020)
# print(d)


#  0&1=0  1&1=1 1&0=0
# a=0
# b = a&3
# print(a,b)
# print ('a & b = %d' % b)
# b&=7
# print ('a & b = %d' % b)

# a = int(input('input a number:\n'))
# b = a>>4
# print(b)
# c = ~(~0 <<4)
# d = b & c
# print ('%o\t%o' %(a,d))
# a = int(input("请输入一个数字："))
# aa = a >> 4
# print(aa)
# b = ~(~0 << 4)   # b=00001111
# c = aa & b
# print("{0:b}".format(c))

# from Tkinter import *
# canvas = Canvas(width=800, height=600, bg='yellow')
# canvas.pack(expand=YES, fill=BOTH)
# k = l
# j = l
# for i in range(0,26):
# canvas.create_oval(310 - k,250 - k,310 + k,250 + k, width=l) k+= j
# j += 0.3
# mainloop()
# import math
# print(math.pi)
# print("PI=%9f" % math.pi)         # output: PI=003




# from tkinter import *
# #画圆
# # canvas=Canvas(width=900, height=600, bg='green')
# # canvas.pack(expand=YES, fill=BOTH)
# # k=1
# # j=1
# # for i in range(0,30):
# #     # 椭圆 x1 y1 x2 y2
# #     canvas.create_oval(410 - k,280 - k,410 + k,280 + k, width=2)
# #     k+= j
# #     j += 0.5
# # mainloop()
#
#
# # 画直线
# # canvas = Canvas(width=400, height=400, bg='green')
# # canvas.pack(expand=YES, fill=BOTH)
# # xO,yO= 263,263
# # y1,x1 = 275,275
# # for i in range(19):
# #     canvas.create_line(xO,yO,xO,y1, width=1, fill='red')
# #     xO = xO - 5
# #     yO = yO - 5
# #     xl = x1 + 5
# #     yl = y1 + 5
# # xO,y0= 263,263
# # y1= 275
# # for i in range(21):
# #     canvas.create_line(xO,yO,x1,yl,fill = 'red')
# #     xO += 5
# #     yO += 5
# #     yl +=5
# # mainloop()
#
#
# # nl = int(input('nl = :\n'))
# # n2 = int(input('n2 = :\n'))
# # n3 = int(input('n3 = :\n'))
# # def swap(pl,p2):
# #     return p2,pl
# # if nl > n2 :
# #     nl,n2 = swap(nl,n2)
# # if nl > n3 :
# #     nl,n3 = swap(nl,n3)
# # if n2 > n3 :
# #     n2,n3 = swap(n2,n3)
# # print (nl,n2,n3)
#
#
#
# # 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
#
#
#
# # 反转三位数
# # class Resver:
# #     def resever(self,num):
# #         bai=num//100
# #         shi=num//10%10
# #         ge=num%10
# #         return (ge*100+shi*10+bai)
# # if __name__ == '__main__':
# #     re=Resver()
# #     n1=int(input("请输入第一个数字："))
# #     n2=int(input("请输入第二个数字："))
# #     n3=int(input("请输入第三个数字："))
# #     num=n1 * 100 + n2 * 10 + n3
# #     print(num)
# #     newNum=re.resever(num)
# #     print(newNum)
#
#
# #将两个升序的数组合并为一个新的升序数组
# # a=[5,6,7,78,89]
# # b=[56,67,77,155,156]
# # c=[3,5,6,10,56,89]
# # def  paixu(n1,n2):
# #     i,j,c=0,0,[]
# #     while i<len(n1) and j<len(n2):
# #         if n1[i]<n2[j]:
# #             c.append(n1[i])
# #             i+=1
# #         elif n1[i]==n2[j]:
# #             c.append(n1[i])
# #             c.append(n2[j])
# #             i+=1
# #             j+=1
# #         else:
# #             c.append(n2[j])
# #             j+=1
# #     while i<len(n1):
# #         c.append(n1[i])
# #         i+=1
# #     while j <len(n2):
# #         c.append(n2[j])
# #         j+=1
# #     return   c
# #
# # def maopao(n):
# #     for i in n:
# #         for j in range(0,len(n)-1):
# #             if n[j]>n[j+1]:
# #                 n[j],n[j+1]=n[j+1],n[j]
# #     return n
# # print(maopao(a+b))
# # print(maopao(b+c))
# # print(paixu(a,b))
# # print(paixu(b,c))
#
# # 指定长度旋转字符串
# # def xuanzhaun(s, offset):
# #     if len(s)>0:
# #         s=(s+s)[(len(s)-offset):(len(s)*2-offset)]
# #     return s
# # s=input("请输入字符串：")
# # offset=int(input("请输入要旋转的长度："))
# # print(xuanzhaun(s,offset))
#
# #相对排名
# # def find(nums):
# #     score={}
# #     for i in range(0,len(nums)):
# #         score[nums[i]]=i
# #     soredScore=sorted(nums,reverse=True)
# #     answer=[0]*len(nums)
# #     # print("score:",score,"soredScore:",soredScore,"answer:",answer)
# #     for i in range(len(soredScore)):
# #         res=str(i+1)
# #         if i==0:
# #             res="Glod Medal"
# #         if i==1:
# #             res="Silver Medal"
# #         if i==2:
# #             res="Bronze Medal"
# #         # print(i,"soredScore[i]",soredScore[i],"score[soredScore[i]]",score[soredScore[i]],"answer[score[soredScore[i]]]",res)
# #         answer[score[soredScore[i]]]=res
# #     return answer
# # a=[5,4,3,7,8,9]
# # b=find(a)
# # print(b)
#
#
#
#
#
# # def findDengji(nums):
# #     scoreDict = {}
# #     for i in range(len(nums)):
# #         scoreDict[nums[i]] = i
# #     # 列表变成字典的key
# #     nums.sort(reverse=True)
# #     for i in range(len(nums)):
# #         res = ""
# #         if i == 0:
# #             res = "jin"
# #         elif i == 1:
# #             res = "yin"
# #         elif i == 2:
# #             res = "tong"
# #         else:
# #             res = i+1
# #         scoreDict[nums[i]] = res
# #     return scoreDict
# # # nums=[5,4,3,7,8,9]
# # nums=[7,6,8,3,10]
# # scoreDict=findDengji(nums)
# # print(scoreDict)
#
#
# # 二分查找
#
# #二分查找
# class Two:
#     # 查找数在列表中存在
#     # 1.如果中间数比查找数小，中间数+1代替0为起点继续查找，直到中间数为查找数
#     # 2.如果中间数比查找数大，中间数-1代替列表最后一位的下标继续查找，直到中间数为查找数
#     # 查找数在列表中不存在
#     # 起点大于终点，返回-1
#     def findnumn(self,nums,start,end,target):
#         if start>end:
#             return -1
#         middle=(start + end) // 2
#         print("===",middle,nums[middle])
#         if nums[middle]<target:
#             self.findnumn(nums,middle+1,end,target)
#         elif nums[middle]>target:
#             self.findnumn(nums,start,middle-1,target)
#         elif nums[middle]==target:
#             print("--------------",middle,nums[middle]==target)
#             return middle
# n=[3,5,6,9]
# t=Two()
# r1=t.findnumn(n,0,len(n)-1,3)
# print(r1)



# def myFindNext(a, b):
#     c={}
#     key=[]
#     # 字典中存放的的key是大列表中每个元素，值是下一个比自己大的值
#     # for循环key列表增加的是，在b集合里面有比子集大的数字，每次加完把值删掉
#     # key作为键，x作为值，添加到字典中
#     for x in b:
#         while key and key[-1]<x:
#             c[key[-1]]=x
#             del key[-1]
#         key.append(x)
#     for k in key:
#         c[k]=-1
#     return [c[i] for i in a]
#
#
# a=[2,4,1]
# b=[1, 2, 6, 4, 8]
# print(a,b)
# print(myFindNext(a,b))



# 输出单词数  my name is lxr 输出4
# s="jfhk kdjflk k djkh"
# s="hello, my name is jkl"
# res=0
# for i in range(0,len(s)):
#     if s[i].isspace() or (i==len(s)-1 and s[len(s)-1]!=""):
#         print(s[i],(i==len(s)-1 and s[len(s)-1]!=""))
#         res+=1
#
# # for i  in range(len(s)):
# #     if s[i]!=' 'and (i==0 or s[i-1]==" "):
# #         res+=1
# print(res)


a=set(["a","s","d"])
s=["asdfghjkl"]
# a.sort()
# a=set(a)
print(a.issubset(s))
# a = [1,2,3,4]
# b = set([2,1,6])
# print(b.issubset(a))



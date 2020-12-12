'''
输入某年某月某日，判断这一天是这一年的第几天？
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''
# while True:
#     date=input("请输入年月日，例如1999.3.3")
#     dates=date.split(".")
#     tian=0
#     # 计算本月份之前所有月份的天数和
#     for i in range(1,int(dates[1])):
#         if i in (1,3,5,7,8,10,12):
#             tian+=31
#         elif i in (4,6,9,11):
#             tian+=30
#         elif i == 2:
#         #    判断是平年还是闰年  可以被4整除，单数不可以被100整除  或者可以被400整除
#              if (i%4==0 and i%100!=0) or i%400==0:
#                  tian+=29
#              else:
#                  tian+=28
#         else:
#             print("输入的日期不合理,请重新输入")
#     print("这一天是{}的第{}天".format(dates[0],tian+int(dates[2])))
# import math
# num=0
# while True:
#      a=int(math.sqrt(num+100))
#      b=int(math.sqrt(num+168))
#      if(a*a==num+100) and (b*b==num+168):
#           print(num)
#           break
#      else:
#           num+=1

from os.path import join

import msvcrt

import sys

'''
问题:编写一个程序，它将找到所有这些数字，可被7整除，但不是5的倍数，2000年至3200年(包括在内)。得到的数字应按逗号分隔的顺序打印在一行上。
提示:考虑使用range(#begin， #end)方法
'''
# nums =[]
# for i in range(2000,3201):
#     if (i%7==0 )and(i%5!=0):
#         nums.append(str(i))
#
# print(",".join(str(i) for i in nums))

'''
问题:编写一个可以计算给定数的阶乘的程序。结果应该以逗号分隔的顺序打印在一行上。假设向程序提供以下输入:8
则输出为:40320
提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。
'''
# num=int(input("请输入要求阶乘的数字"))
# jiecheng=1
# for i in range(1,num+1):
#     jiecheng*=i
# print(jiecheng)
'''
问题:使用给定的整数n，编写一个程序生成一个包含(i, i*i)的字典，该字典包含1到n之间的整数(两者都包含)。然后程序应该打印字典。
假设向程序提供以下输入:8
则输出为:
{1:1，2:4，3:9，4:16，5:25，6:36，,7:49，8:64}
提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。考虑使用dict类型()
'''
# num=int(input("请输入数字"))
# b={}
# def dange(a):
#     b.update({a:a*a})
#     return b
# for i in range(1,num+1):
#     b=dange(i)
# print(b)
'''
问题:编写一个程序，该程序接受控制台以逗号分隔的数字序列，并生成包含每个数字的列表和元组。假设向程序提供以下输入:
34岁,67年,55岁,33岁,12日,98年
则输出为:['34'， '67'， '55'， '33'， '12'， '98']
               ('34'， '67'， '55'， '33'， '12'， '98')
提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。方法可以将列表转换为元组
'''
import re
# content=input("请输入内容，以,分割")
# contents=content.split(",")
# a=[]
# for i in range(0,len(contents)):
    # a.append(contents[i])
# print(a)
# print(tuple(a))
'''
问题:定义一个至少有两个方法的类:        getString:从控制台输入获取字符串        printString::打印大写母的字符串。
还请包含简单的测试函数来测试类方法。
提示:使用_init__方法构造一些参数
'''
# class A(object):
#     def __init__(self):
#         self.b=""
#     # 从控制台输入获取字符串
#     def getString(self,s):
#         for i in s:
#             if i.isalpha():
#                 self.b+=i
#         return self.b
#     # 打印大写字母的字符串
#     def printString(self,s):
#         self.b = ""
#         for i in s:
#             if i.isupper():
#                 self.b += i
#         return  self.b
# if __name__ == '__main__':
#     s=input("请输入")
#     a=A()
#     print(a.getString(s))
#     print(a.printString(s))
# s=[]
s=[{'name': 'zs', 'coin': 1715, 'pais': [10, 1, 3, 5, 9]}, {'name': 'wa', 'coin': 1458, 'pais': [2, 8, 1, 6, 5]}, {'name': 'zl', 'coin': 1799, 'pais': [8, 2, 5, 5, 2]}]
# b=sum(xj["pais"] >= 21 for xj in s)
# s=[1,2,3]
# b=sum(xj>2 for xj in s)
# print(b)
for i in s:
    for j in i["pais"]:
        b = sum(xj > 2 for xj in j)
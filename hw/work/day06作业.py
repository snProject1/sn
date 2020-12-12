'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
题目：输出 9*9 乘法口诀表。

'''

#方法一  列表内置排序方法

# try:
#     nums=[]
#     n1 = int(input("请输入整数1:"))
#     n2 = int(input("请输入整数2:"))
#     n3 = int(input("请输入整数3:"))
#     nums=[n1,n2,n3]
#     nums.sort()
#     print(nums)
# except Exception as e:
#     print(e)

# 方法二  冒泡排序
# while True:
#     try:
#         nums=[]
#         n1 = int(input("请输入整数1:"))
#         n2 = int(input("请输入整数2:"))
#         n3 = int(input("请输入整数3:"))
#         nums=[n1,n2,n3]
#         for i in range(len(nums)):
#             for j in range(0,len(nums)-1):
#                 if nums[j]>nums[j+1]:
#                     nums[j],nums[j+1]=nums[j+1],nums[j]
#         print(nums)
#     except Exception as e:
#         print(e)




# 斐波那契数列
# a,b=0,1
# try:
#     chang=int(input("请输入你要得到的数列长度:"))
#     nums = [a, b]
#     for i in range(chang-2):
#         a, b = b, a + b
#         nums.append(b)
#     print(nums)
# except Exception as e:
#     print(e)




# 九九乘法口诀
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={}".format(i,j,i*j),end=" ")
#     print(" ")


# i=1
# while i<10:
#     lie=1
#     while  lie<=i:
#         print(i,lie,end="")
#         lie+=1
#     print(" ")
#     i+=1







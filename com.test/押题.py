# 反转三位数
num1="235"
reversed(num1)
# print(num1)
# 合并排序数组
a=[2,3,5,7,8]
b=[3,4,5,6,7]
c=[]
i,j=0,0
while i<len(a)-1 and j<len(b)-1:
    if a[i]>b[j]:
        c.append(b[j])
        j+=1
    elif a[i]<b[j]:
        c.append(a[i])
        i+=1
    elif a[i]==b[j]:
        c.append(a[i])
        c.append(b[j])
        j+=1
        i += 1
while i<len(a):
    c.append(a[i])
    i+=1
while i<len(b):
    c.append(b[j])
    j+=1
# print(c)
# 旋转字符串
# 相对排名
# 二分查找
def findByEr(num1, mstart,mend,target):
    middle=(mstart+mend)//2
    if mstart>mend:
        return -1
    elif num1[middle]==target:
        return middle
    elif num1[middle]>target:
        return  findByEr(num1, mstart, middle - 1, target)
    elif num1[middle]<target:
        return  findByEr(num1,middle+1,mend,target)
num1=[34,55,67,89,90,98,99]
# print(findByEr(num1,0,len(num1)-1,98))
# 下一个更大的数
# 字符串中的单词数
# 勒索信
# 不重复的两个数
# 双胞胎字符串
# 最接近target的值
# 点积
x1=[1,3,5]
x2=[5,2,0]
ji=0
if len(x1)!=len(x2):
    print("没有点积")
else:
    for i in range(0,len(x1)):
        ji+=x1[i]*x2[i]
    # print(ji)
# 函数运行时间
# 查询区间
# 数组剔除元素后的乘积
def delNum(num1, param):
    # for i in
    pass
num1=[2,34,5,6,7]
delNum(num1,5)
# 键盘的一行
# 找不同
# 第k个组合
# 子域名访问计数
# 最长AB子串
# 删除字符
# 比较字符串
# 能否转换
# 二分查找
#排序数组中最接近元素
# 构造矩形
# 首字母大写
shou="my name is zhangsan"
nshou=""
for s in shou.split(" "):
    nshou+=s.capitalize()+" "
# print(nshou)

# 七进制
def shiZhuanQi(num):
    if num<=7:
        return num
    return  str(shiZhuanQi(num//7))+str(num%7)
# print(shiZhuanQi(21))
# 查找数组中没有出现的所有数字
# 合并排序数组
# 最小路径和
# 大小写转换
# 水仙花数
def shuixianhua(wei):
    mstart=10**(wei-1)
    mend=10**wei
    for i in range(mstart,mend):
        he=0
        for j in range(0,wei):
            n=str(i)
            he+=int(n[j])**wei
        if he==i:
            print(i)

# shuixianhua(3)
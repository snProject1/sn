

# 删除字符
def delS(s1,s2):
    t=False
    for j in range(0,len(s2)):
        for i in s1:
            if s2[j] in i and j==len(s2)-1:
                t=True
    return t
# print(delS("asdf","e"))

# 首字母大写
# a="sd dhfjks njk jdskl ds"
# n=a.split(" ")
# b=""
# for i in n:
#     c=i.capitalize()+" "
#     b+=c
# print(b)


# 二分查找
def findN(sta, end, s,target):
    midd=(sta+end)//2
    if sta>end:
        return -1
    if s[midd]==target:
        return s[midd]
    elif s[midd]>target:
        return  findN(sta,end-1,s,target)
    elif s[midd]<target:
        return  findN(sta+1,end,s,target)


s=[4,5,6,7,45,67]
num=findN(0,len(s)-1,s,67)
# print(num)


#能否转换
def isZhuan(a, b):
    j = 0
    for i in range(0, len(a)):
        if a[i] == b[j]:
            j += 1
            if j == len(b) - 1:
                return True

# a="hellloworld"
# b="llo"
# if isZhuan(a,b):
#     print("可以")
# else:
#     print("不可以")


# 字符串写入的行数
s=["asdfghjkl"]
wid=[20]*9
line=0
zi=0

for i in range(0,len(s)):
    line+=1
    zi+=wid[i]
    if zi==100:
        line+=1
        zi=0
    elif zi>100:
        line+=1
        zi=zi-100
    elif zi<100:
        zi+=wid[i]
# print(line,zi)

# 求指定位数内的水仙花数
def finwater(num):
    mstart=10**(num-1)
    mend=10**num
    for i in range(mstart,mend):
        mi=str(i)
        # print(mi)
        sum=0
        for j in range(0,num):
            sum+=int(mi[j])**num
        if sum==i:
            print(i)
# finwater(2)

# 将小写字符转换为大写字符   ASII大小写相差32
def lowwerToUpper(s):
    return chr(ord(s)-32)
# print(lowwerToUpper("c"))


# 找出1,n中未出现在此数组中的数字
def findNone(mlist):
    mset=set(mlist)
    for i in range(1,len(mlist)+1):
        if i not in mset:
            print(i)
mlist=[2,1,4,4,3,5,6,2,6]
# findNone(mlist)


def shiZQi(n):
    if n<0:
        return "-"+str(shiZQi(-n))
    if n<7:
        return str(n)
    return str(shiZQi(n//7))+str(n%7)
# print(shiZQi(777))

# 两个排好序的数组，找到第k个最小的数

def findMin(k):
    sum = []
    for i in a1:
        for j in b1:
            sum.append(i + j)
    sum.sort()
    return sum[k-1]

a1=[2,3,4]
b1=[4,8,9]
# print(findMin(4))

















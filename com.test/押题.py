# 1反转三位数
num1=str(235)
# print(num1[::-1])

# 2合并排序数组
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


# 3旋转字符串   输入"asdfghj"  offset=2 输出  hjasdfg
s="asdfghj"
offset=2
ss=s+s
newss=ss[len(s)-2:len(ss)-2]
# print(newss)


# 4相对排名 [4,5,3,6,7][4,tong,5,yin,jin]
a=[8,5,3,6,7]
score={}
paiming={}
# 初始化成绩
for i in a:
    score[i]=0
a.sort(reverse=True)
for i in range(0,len(a)):
    if i==0:
        paiming[a[i]]="jin"
    elif i==1:
        paiming[a[i]]="yin"
    elif i==2:
        paiming[a[i]]="tong"
    else:
        paiming[a[i]]=i+1
for i in paiming.items():
    score[i[0]]=i[1]
# print(score)


# 5二分查找
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


# 6下一个更大的数  第一个是第二个的子集，找到所有第一个集合元素在第二个里面的第一个最大的数，没有返回-1   [2,4,6]  [3,2,5,4,6,7]
# 找到大集合里米一个值得下一个最大值，根据字典取出
a,b,c=[2,4,6],[3,1,5,4,6,2],[]
bdict={}
for i in b:
    while c and c[-1]<i:
        bdict[c[-1]]=i
        del c[-1]
    c.append(i)
for j in c:
    bdict[j]=-1
# print(bdict)

# 7字符串中的单词数    一个单词为不含空格的连续字符串
danci="my name is liuxinru 12 %%%%"
n=0
for d in range(0,len(danci)):
    if danci[d].isspace() or d==len(danci)-1:
        n+=1
# print(n)


# 8勒索信   用ord函数返回对应的十进制
a1="qwe"
zazhi="qwerty"
isLe=True
zimu=[0]*26
for z in zazhi:
    zimu[ord(z)-ord("a")]+=1
for a in a1:
    zimu[ord(a)-ord("a")]-=1
    if zimu[ord(a)-ord("a")]<0:
        isLe=False
        break
# print(isLe)

# 9不重复的两个数
a=[2,3,4,1,2,3,4,6]
num=0
for i in a:
    if a.count(i)==1:
        num+=1
        # print(i)



# 10双胞胎字符串  任意转换奇数位或偶数位，最后可以相等
s1,s2="qwey","qwey"
s1ji,s1ou=[],[]
s2ji,s2ou=[],[]
for i in range(0,len(s1)):
    if i%2==0:
        s1ou.append(s1[i])
    else:
        s1ji.append(s1[i])
for i in range(0, len(s2)):
    if i % 2 == 0:
        s2ou.append(s2[i])
    else:
        s2ji.append(s2[i])
s1ji.sort()
s2ji.sort()
s1ou.sort()
s2ou.sort()
if s1ji==s2ji and s1ou==s2ou:
    # print(True)
    pass
else:
    # print(False)
    pass
# 11最接近target的值  [1,3,4,2,5] tar=12   找tar-(a+b) 接近0的两个值
a=[5,6,8,9]
mtarget=12
c=9999999999999
a.sort()
mstart,mend=0,len(a)-1
while mstart<mend:
    if a[mstart]+a[mend]<=mtarget:
        c=min(c,mtarget-(a[mstart]+a[mend]))
        mstart += 1
    elif a[mstart]+a[mend]>mtarget:
        mend-=1
# if c==9999999999999:
#     print(-1)
# else:
#     print(mtarget-c)

# 12点积
x1=[1,3,5]
x2=[5,2,0]
ji=0
if len(x1)!=len(x2):
    print("没有点积")
else:
    for i in range(0,len(x1)):
        ji+=x1[i]*x2[i]
    # print(ji)


# 13函数运行时间  ["f1 enter 10","f2 enter 11","f1 out 13","f2 enter 15"]
a=["f1 enter 10","f2 enter 11","f1 out 13","f2 enter 15"]
# a=["f1 enter 10","f1 out 11","f1 enter 13","f1 out 15"]
adict={}
for i in a:
    ii=i.split(" ")
    if ii[0] in adict.keys():
        adict[ii[0]]=int(ii[2])-int(adict[ii[0]])
    else:
        adict[ii[0]]=ii[2]
# for key,val in adict.items():
#     print(key+"|"+str(val))


# 14查询区间  判断目标值是否在列表中
a=[[200,300],[150,250],[600,700]]
target=250
b=False
for i in a:
    if i[0]<=target<=i[1]:
        b=True
        break
# print(b)

# 15数组剔除元素后的乘积
def delNum(num1, param):
    ji=1
    for i in range(0,len(num1)):
        if i!=param:
            ji*=num1[i]
    return ji
num1=[2,10,5,6,7,3]
# print(delNum(num1,3))
# 16键盘的一行  ["hello","dad","dec","ert"]  找出可以在一行键盘中输出的元素
bb=["hello","asd","dad"]
ss=["qwertyuiop","asdfghjkl","zxcvbnm"]
i=0
while i<len(bb):
    for  j in range(len(ss)):
        flag=True
        for zimu in bb[i]:
            if zimu not in ss[j]:
                flag=False
        # if flag:
        #     print(bb[i]+"在一行")
    i+=1


# 17找不同   s字符串无序，随机位置添加一个字符生成t，找出添加的字符
a="qwert"
b="qwerkt"
c=[0]*26
for i in a:
    c[ord(i)-ord("a")]+=1
for i in b:
    c[ord(i)-ord("a")]-=1
    if c[ord(i)-ord("a")]<0:
        # print(chr(ord(i)))
        break
# 18第k个组合  组合集合中的数字，按字典序排列   找出第k种排列
a=[1,2,3,4]
target=4


# 19子域名访问计数["9001 school.bupt.edu"]    ["9001 school.bupt.edu","9001 bupt.edu","9001 edu"]
a=["9001 school.bupt.edu"]
domianlst=[]
for aa in a:
    aaa=aa.split()
    num=aaa[0]
    di=aaa[1]
    domains=di.split(".")
    topdomain=domains[-1]
    secdomain=domains[-2]+"."+topdomain
    domianlst.append(num+" "+di)
    domianlst.append(num+" "+secdomain)
    domianlst.append(num+" "+topdomain)
# print(domianlst)


# 20最长AB子串  "ABAAABBBA" 输出8  [0,7][1,8]数目A与B相等 求最长的子串AB长度，且A与B次数相等
s="ABABAB"
anum,bnum=0,0
lens=[]
for item in s:
    if item=="A":
        anum+=1
    elif item=="B":
        bnum+=1
    if anum==bnum:
       lens.append(anum+bnum)
# print(lens[-1])

# 21删除字符   "asd"---"a" true  "asd" "j"---False
s="asdf"
d="nm"
a = False
for i in d:
    for j in s:
        if i in j:
            a=True
            break
    if not a:
        break
# print(a)

# 22比较字符串  A="ASDFG" B="SDF"  前提两个字符串都是大写字母，判断B是不是A的子集  同样用ord()返回十进制
A="ASDFG"
B="SDFM"
c=[0]*26
for i in A:
    c[ord(i)-ord("A")]+=1
for i in B:
    c[ord(i)-ord("A")]-=1
# for i in range(0,len(c)):
#     if c[i]<0:
#         print("False")
#         break
#     elif c[i]>=0 and i==len(c)-1:
#         print("True")

#23 能否转换   s,t   遍历解决
s="asdf"
t="v"
a=True
for i in t:
    if i not in s:
        a=False
        break
# print(a)

#24排序数组中最接近元素  排好序的数组中找出最接近目标值的角标 target-yuansu 最接近0的下标
a=[23,25,36,46,67]
target=36
b=99999999999
i=0
index=0
while i<len(a):
    if target==a[i]:
        index=i
        break
    if target-a[i]>0:
        b=min(b,target-a[i])
        if b==target-a[i]:
            index=i
    elif target-a[i]<0:
        b=min(b, abs(target - a[i]))
        if b==abs(target - a[i]):
            index=i
    i+=1
# print(index)

#25 构造矩形
area=82
wid=int(area**0.5)
while area%wid!=0:
    wid-=1
# print([area//wid,wid])

# 26首字母大写
shou="my name is zhangsan"
nshou=""
for s in shou.split(" "):
    nshou+=s.capitalize()+" "
# print(nshou)


#27 七进制
def shizq(param):
    if param<=7:
        return param
    else:
        return  str(shizq(param//7))+str(param%7)
# print(shizq(21))


# 28查找数组中没有出现的所有数字  输入[2,3,4,2,5,6,3] 输出[1，7]
a=[2,3,4,2,5,6,3]
for i in range(1,len(a)+1):
    pass
    # if i not in a:
    #     print(i)


# 29最小路径和
erwei=[[1,3,1],[1,5,1],[4,2,1]]
i=0
while i<len(erwei):
    for j in range(1,len(erwei[0])):
        if i==0 and j>0:
            erwei[i][j]+=erwei[i][j-1]
        elif i>0 and j==0:
            erwei[i][j]+=erwei[i-1][j]
        elif i>0 and j>0:
            erwei[i][j]+=min(erwei[i][j-1],erwei[i-1][j])
    i+=1
print(erwei[len(erwei)-1][len(erwei[0])-1])

# while i<len(erwei):
#     for j in range(1,len(erwei[0])):
#         if i==0 and j>0:
#             erwei[i][j]+=erwei[i][j-1]
#         elif i>0 and j==0:
#             erwei[i][j]+=erwei[i-1][j]
#         elif i>0 and j>0:
#             erwei[i][j]+=min(erwei[i][j-1],erwei[i-1][j])
#     i+=1
# print(erwei[len(erwei)-1][len(erwei[0])-1])


# 30大小写转换   输入a 输出A
s="asdf"
# print(s.upper())


# 31水仙花数

def shuijianhua(wei):
    qi=10**(wei-1)
    zhong=10**wei
    for i in range(qi,zhong):
        he=0
        for j in range(wei):
            he+=int(str(i)[j])**3
        if he==i:
            print(i)

# shuijianhua(3)


# 32平面列表  将二维列表拆为简单列表
erwei=[[2,6],9,[2,3]]
erwei_new=[]
for i in range(len(erwei)):
    if type(erwei[i])==int:
        erwei_new.append(erwei[i])
    else:
        erwei_new+=erwei[i]
# print(erwei_new)



# 33 第n个数位
n=18
# 初始化一位数从1开始
num=1
count=9
# 第n位所在的整数
mstart=1
while n>num*count:
    n-=num*count
    # print(n)
    num+=1
    count*=10
    mstart*=10

# 找到第n位数所在的整数
mstart+=(n-1)//num
# print(num,count,mstart)
# print(mstart)
# print(int(str(mstart)[(n-1)%length]))



# 34移动石子  生成连续奇偶列表的最小步数
alist=[1,6,7,8,9]
ji=0
ou=0

for i in range(0,len(alist)):
    ji+=abs(alist[i]-(2*i+1))
    ou+=abs(alist[i]-(2*i+2))
# print(min(ji,ou))

# 35抽搐词
s="whoooooeshpppeeeeehell"
qian=""
chou=set()
for i in s:
    if qian=="":
        qian=i
    else:
        if qian==i:
            num+=1
            # print(num)
            if num>=3:
                chou.add(i)
        else:
            num=1
            qian=i
# print(chou)



#36 玩具工厂    类的继承
class Base:
    def eat(self,s):
        print("吃的食物")
class Cat(Base):
    def eat(self,s):
        print("制作"+s)
class Dog(Base):
    def eat(self,s):
        print("制作"+s)
class AnimalFactory:
    def getjineng(self,ani):
        if ani=="cat":
            return Cat()
        if ani=="dog":
            return Dog()
mani=AnimalFactory()
# mani.getjineng("cat").eat("猫粮")
# mani.getjineng("dog").eat("狗粮")


# 37.形状工厂  考继承
class Base:
    def draw(self):
        raise NotImplementedError("必须实现")
class sanjiao(Base):
    def draw(self):
        print("  /\\")
        print(" /  \\")
        print("/____\\")
class chang(Base):
    def draw(self):
        print("----------")
        print("|         |")
        print("__________")
class zheng(Base):
    def draw(self):
        print("----------")
        print("|         |")
        print("|         |")
        print("__________")
class shapeFactory:
    def getDraw(self,s):
        if s=="长方形":
            chang().draw()
        elif s=="正方形":
            zheng().draw()
        elif s=="三角形":
            sanjiao().draw()
# shapeFactory().getDraw("正方形")

#38.字符串写入的行数   每行最大宽度是100
width=[10]*2
s="a"*2
space=0
hang=1
for i in range(0,len(s)):
    if space<100:
        space+=width[i]
    elif space==100:
        hang += 1
        space=width[i]
    elif space>100:
        space-=100
        hang+=1
# print(hang,space)



# 39 两个排序组合的第k个小元素  找求和后的数组第K个最小的值
a,b=[1,4,7],[23,34,56]
target=4
he=set()
for i in a:
    for j in b:
        he.add(i+j)
# print(list(he)[target-1])
























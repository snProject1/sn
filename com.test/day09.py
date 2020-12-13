#类变量可以不实例化对象直接调用   类变量改变，影响所有对象的变量  一个对象变量改变不会影响其余对象
# 实例对象  实例化后每个变量单独拥有的变量
# 类多态
# class A:
#     i=1
#     def getI(self):
#         return self.i
#     def getChangeI(self):
#         self.i +=1
#
#
# A.i=7
# print("类变量",A.i)
# a=A()
# a.getChangeI()
# print(a.i)
# b=A()
# print(b.i)


class Man:

    def eat(self):
        print('吃饭')


class Chinese(Man):

    def eat(self):
        print('筷子')


class Indian(Man):

    def eat(self):
        print('hands')


class English(Man):

    def eat(self):
        print('刀叉')


def Maneat(m):
    if isinstance(m,Man):
        m.eat()
    else:
        print('饿着')

Maneat(Chinese())
Maneat(Indian())
Maneat(English())






3+2







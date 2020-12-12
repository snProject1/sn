#函数调用  不定长
# 1个*代表参数是元组
# def test1(*b,parm="a"):
#     print(b,parm)
#
# test1(2,4,parm="d")
# 两个*代表参数是字典
# def test2(a,**b):
#     print(a,b)
# test2(2,name="zhangsan",age="12")
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)


#  文件读写
# a=open(file="a.txt",mode="w",encoding="utf-8")
# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         s="{}*{}={} ".format(j,i,i*j)
#         a.write(s)
#         j += 1
#     a.write("\n")
#     i+=1
# a.close()
a=open(file="a.txt",mode="r",encoding="utf-8")
b=a.readlines()
def yanzheng(iii):
    if int(iii[0])*int(iii[1])==int(iii[2]):
        print("{}*{}={}验证通过".format(iii[0],iii[1],iii[2]))
    else:
        print("{}*{}={}验证失败".format(iii[0], iii[1], iii[2]))
for i in b:
    gexiang=i.split(" ")
    # print(gexiang)
    for ii in gexiang:
        nii=ii.replace("*","=").split("=")
        print(nii)
        if len(nii)>1:
            yanzheng(nii)




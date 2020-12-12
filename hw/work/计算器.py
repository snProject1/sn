def add(x, y):
    """相加"""
    return x + y+1

def jian(x, y):
    """相减"""
    return x - y

def cheng(x, y):
    """相乘"""
    return x * y

def chu(x, y):
    """相除"""
    return x / y

def zhengchu(x, y):
    """整除"""
    return x // y
def yu(x, y):
    """取余"""
    return x % y
def zhishumi(x, y):
    """指数幂"""
    return x ** y
# 日志写入
jisuanqi=open("jisuanqi.txt",mode="w",encoding="utf-8")
s="选择运算：1、相加 2、相减 3、相乘 4、相除  5、整除 6、取余 7、指数幂"
jisuanqi.write("提示信息:"+s)
jisuanqi.write("\n")

for i in range(0,7):
    a=int(input("请输入第一个1-99999以内数字"))
    while True:
        if 1<a<99999:
            c=int(input("请输入第二个1-99999以内数字"))
            break
        else:
            jisuanqi.write("数字有误\n")
            print("输入的数字不在范围内，请重新输入")
            a = int(input("请输入第一个1-99999以内数字"))

    print(s)
    dict={}
    b=int(input("请输入运算符对应的标码"))
    dict["xuhao"] = b
    if b==1:
        jia=add(a, c)
        dict["jieguo"]=jia
        # print(jia)
    elif b==2:
        jian=jian(a, c)
        dict["jieguo"] = jian
        # print(jian)
    elif b==3:
        cheng=cheng(a, c)
        dict["jieguo"] = cheng
        # print(cheng)
    elif b==4:
        chu=chu(a, c)
        dict["jieguo"] = chu
        # print(chu)
    elif b==5:
        zhengchu=zhengchu(a, c)
        dict["jieguo"] = zhengchu
        # print(zhengchu)
    elif b==6:
        quyu=yu(a,c)
        dict["jieguo"] = quyu
        # print(quyu)
    elif b==7:
        zhishumi=zhishumi(a, c)
        dict["jieguo"] = zhishumi
        # print(zhishumi)

    dict["number1"] = a
    dict["number2"] = c
    jisuanqi.write(str(dict))
    jisuanqi.write("\n")
    end=input("结束请输入Y")
    if end=="Y" or end=="y":
        break
jisuanqi.close()




# 日志读取
jsq=open("jisuanqi.txt",mode="r+",encoding="utf-8")
mess=jsq.readlines()


def panduan(xuhao, result, num1, num2):
    if xuhao==1:
        if (num1+num2)==result:
            print("{}+{}={} 本条计算验证通过".format(num1,num2,result))
        else:
            print("{}+{}={} 本条计算验证失败".format(num1,num2,result))
    elif xuhao == 2:
        if (num1 - num2) == result:
            print("{}-{}={} 本条计算验证通过".format(num1, num2, result))
        else:
            print("{}-{}={} 本条计算验证失败".format(num1, num2, result))
    elif xuhao == 3:
        if (num1 * num2) == result:
            print("{}*{}={} 本条计算验证通过".format(num1, num2, result))
        else:
            print("{}*{}={} 本条计算验证失败".format(num1, num2, result))
    elif xuhao == 4:
        if (num1 / num2) == result:
            print("{}/{}={} 本条计算验证通过".format(num1, num2, result))
        else:
            print("{}/{}={} 本条计算验证失败".format(num1, num2, result))
    elif xuhao == 5:
        if (num1 // num2) == result:
            print("{}//{}={} 本条计算验证通过".format(num1, num2, result))
        else:
            print("{}//{}={} 本条计算验证失败".format(num1, num2, result))
    elif xuhao == 6:
        if (num1 % num2) == result:
            print("{}%{}={} 本条计算验证通过".format(num1, num2, result))
        else:
            print("{}%{}={} 本条计算验证失败".format(num1, num2, result))
    elif xuhao == 7:
        if (num1 ** num2) == result:
            print("{}**{}={} 本条计算验证通过".format(num1, num2, result))
        else:
            print("{}**{}={} 本条计算验证失败".format(num1, num2, result))
for i in range(1,len(mess)):
    if "数字有误" in mess[i]:
        pass
    else:
        m=mess[i].replace("\n","").replace(" ","")
        m=eval(m)
        xuhao=m["xuhao"]
        result=m["jieguo"]
        num1=m["number1"]
        num2=m["number2"]
        panduan(xuhao,result,num1,num2)












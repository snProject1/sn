import json
# a={'li', 'zss'}
# for i in a:
#     print(i)
jsq=open("jisuanqi.txt",mode="r+",encoding="utf-8")
mess=jsq.readlines()
for i in range(1,len(mess)):
    if "数字有误" in mess[i]:
        pass
    else:
        # print(mess[i])
        # m = mess[i].replace("\n", "").replace(" ","")
        # m = eval(mess[i])
        # xuhao = m["xuhao"]
        # print(xuhao)
        # m=mess[i].replace("\n","").replace(" ","")
        m=eval(mess[i])
        xuhao=m["xuhao"]
        result=m["jieguo"]
        num1=m["number1"]
        num2=m["number2"]
        print(xuhao,result,num1,num2)
        # panduan(xuhao,result,num1,num2)





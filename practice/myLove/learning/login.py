count = 3
while count<=3 and count>0:
    name = input("请输入用户名：")
    password = int(input("请输入密码："))
    if name == "login" and password==123456:
        print("输入正确，登录成功")
        break
    else:
        count-=1
        if count == 0:
            print("3次机会已用完，请稍后再试")
        else:
            print("输入错误，你还有%d次机会" % count)
        continue

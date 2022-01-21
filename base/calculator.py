def add(num1,num2):
    sumnum = num1 + num2
    print(num1,"+",num2,"=",sumnum)

def minus(num1,num2):
    minusnum = num1 - num2
    print(num1,"-",num2,"=",minusnum)

def multiply(num1,num2):
    multiplysnum = num1 * num2
    print(num1,"*",num2,"=",multiplysnum)

def divide(num1,num2):
    dividenum = num1 / num2
    print(num1,"/",num2,"=",dividenum)

def result(operator):
    if operator == "1":
        print("请输入两个数：")
        num1 = int(input())  # input默认接收的数据类型为字符串，需要手动转换类型，否则无法用于计算
        num2 = int(input())
        add(num1, num2)

    elif operator == "2":
        print("请输入两个数：")
        num1 = int(input())
        num2 = int(input())
        minus(num1, num2)

    elif operator == "3":
        print("请输入两个数：")
        num1 = int(input())
        num2 = int(input())
        multiply(num1, num2)

    elif operator == "4":
        print("请输入两个数：")
        num1 = int(input())
        num2 = int(input())
        divide(num1, num2)

    else:
        print("输入有误！")
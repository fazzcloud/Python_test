class MyCalculator():


    def add(self,num1, num2):
        sumnum = num1 + num2
        print(num1, "+", num2, "=", sumnum)

    def minus(self,num1, num2):
        sumnum = num1 - num2
        print(num1, "-", num2, "=", sumnum)

    def multiply(self,num1, num2):
        sumnum = num1 * num2
        print(num1, "*", num2, "=", sumnum)

    def divide(self,num1, num2):
        sumnum = num1 / num2
        print(num1, "/", num2, "=", sumnum)

    def result(self,operator):
        if operator == "1":
            print("请输入两个数：")
            num1 = int(input())
            num2 = int(input())
            MyCalculator.add(self,num1,num2)
        elif operator == "2":
            print("请输入两个数：")
            num1 = int(input())
            num2 = int(input())
            MyCalculator.minus(self,num1,num2)

        elif operator == "3":
            print("请输入两个数：")
            num1 = int(input())
            num2 = int(input())
            MyCalculator.multiply(self,num1,num2)

        elif operator == "4":
            print("请输入两个数：")
            num1 = int(input())
            num2 = int(input())
            MyCalculator.divide(self,num1,num2)

        else:
            print("输入有误！")
from MyCalculator import MyCalculator

print("选择运算符：")
print("1 is +")
print("2 is -")
print("3 is *")
print("4 is /")
print("请输入你的选择：")
operator = input() #接受选择的运算
result = MyCalculator()
result.result(operator)



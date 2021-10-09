from my_function import my_abs,quadratic
print(my_abs(1))
if 0 > 0:
    pass

#测试

if quadratic(2,3,1) != (-0.5,-1.0):
    print("测试失败")
elif quadratic(1,3,-4) != (1.0,-4.0):
    print("测试失败")
else:
    print("测试成功")
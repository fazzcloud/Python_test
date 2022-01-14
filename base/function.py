from my_function import my_abs,quadratic,power,enschool,add_end,calc,person,mul,trim,findMinAndMix
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

print(power(5))

enschool('lj','male')

print(add_end([1]))

print(calc(1,2,3))
extra = {'city':'nj','name':'lj','age':'26','happy':'awaa'}
person('jack',24,city = 'nj',job = 'pk')

print(mul(1,2,3,4,6))

trim('  hello')
# 测试:
findMinAndMix([7])
#求绝对值
def my_abs(x):
    if not isinstance(x,(int,float)):  #判断接收的值，数据类型是否正确
        raise TypeError('数据类型错误')  #抛出异常提示
    if x > 0:
        return x
    else:
        return -x
#空函数：
def nop():
    pass

#解一元二次方程，ax2+bx+c=0
import math
def quadratic(a, b, c):
    if not isinstance(a+b+c, (int, float)):#判断接收的值，数据类型是否正确
        raise TypeError('数据类型错误')#抛出异常提示
    elif (b**2 - 4*a*c) < 0: #判断是否符合求根的条件
        print("不符合数学公式")
    else:
        x = ( -b + math.sqrt( b**2 - 4*a*c )) / ( 2*a )
        x2 = (-b - math.sqrt( b**2 - 4*a*c )) / ( 2*a )
        return x,x2


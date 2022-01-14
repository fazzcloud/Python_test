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

#求平方
def power(x,y=2):
    return x ** y

def enschool(name,gender,age = 18,city = 'nj'):
    print("name:",name)
    print("gender:",gender)
    print("age:", age)
    print("city:", city)

#默认参数-list
def add_end(L = []):
    L.append('end')
    return  L

def calc(*numbers):
    sum = 0
    for n in  numbers:
        sum = sum + n*n
    return sum

def person(name,age,*args,city,job):
    print('name:',name,'age:',age,args,'city',city,'job',job)

#计算乘积
def mul(*args):
    s = 1
    if len(args) == 0:
        print("请输入值")
    for n in args:
        s = n*s
    return s

#去除首尾空格
def trim(s):
    print(s.strip(' '))  #strip方法去除首尾空格


#迭代出最小和最大值，并以tuple的方式返回
def findMinAndMix(L):

    print("最大值为：",max(L))
    print("最小值为：", min(L))


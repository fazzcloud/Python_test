#定义myclass类
class Myclass(object):

    def say_hello(self,name): #创建一个方法，也用def定义，和函数的区别是，方法的第一个参数必须声明，一般默认用self
        return "hello,"+ name

class A: #创建名为A的类
    def __init__(self,a,b): #创建__init__方法，用于初始化数据
        self.a = int(a)     #将参数类型转化为int整数型
        self.b = int(b)

    def add(self):          #创建add()方法，这里可以直接拿同一个类中的self.a和self.b来进行计算，因此不需要再额外传参
        return self.a + self.b

class B(A):  #创建名为B的类，继承A类
    def sub(self,a,b):
        return a - b



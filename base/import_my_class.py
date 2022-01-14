import my_class
import sys
from time import ctime as my_ctime
mc = my_class.Myclass() # 调用类给mc赋值
print(mc.say_hello("lj")) #调用say_hello这个方法给mc赋值

count = my_class.A('1', 2)
print(count.add())
count2 = my_class.B(2, 3) #调用B类给count2赋值，注意，由于B类继承了A类，所以会默认调用A类方法
print(count2.add()) #由于B类是子类，所以传参时，调用A类（父类）中的方法，不需要重新传参
print(count2.sub(1,2)) #调用子类内部的拓展类，需要重新传参

print(my_ctime()) #ctime()函数用于获得当前时间

print(sys.path)
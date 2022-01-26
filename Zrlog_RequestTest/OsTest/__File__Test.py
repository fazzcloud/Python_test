import os
#输出当前文件的全路径
print(__file__)
#输出当前文件的所在目录全路径
print(os.path.dirname(__file__))
#输出所在目录的上级目录
print(os.path.dirname(os.path.dirname(__file__)))
#返回当前目录绝对路径
print(os.path.abspath(__file__))
#组合使用
print(os.path.dirname(os.path.abspath(__file__)))
#拼接路径
path1 = os.path.dirname(__file__)
path2 = os.path.join(path1,'1.txt')
print("path2:",path2)
path3 = os.path.dirname(os.path.abspath(__file__))
path4 = os.path.join(path3,'2.txt')
print("path4:",path4)
import os
#获取当前文件的绝对路径
conf_file = os.path.abspath(__file__)
print(conf_file)
#返回所在目录
conf_path = os.path.dirname(conf_file)
print(conf_path)
#通过join方法拼接出新的路径
new_conf_file = os.path.join(conf_path,"score001.txt")
print(new_conf_file)
#返回上级目录
father_conf_path = os.path.dirname(conf_path)
print(father_conf_path)
#通过os.sep方式手动拼接出.py文件的绝对路径
new_conf_file2 = father_conf_path + os.sep + "OsTest" + os.sep + "score002.txt"
print(new_conf_file2)
#通过exists判断文件是否存在
res_file = os.path.exists(conf_file)
print(res_file)
#通过exists判断目录是否存在
res_path = os.path.exists(conf_path)
print(res_path)
#判断是否为文件
is_file = os.path.isfile(new_conf_file)
print(is_file)
#判断是否为目录
is_path = os.path.isdir(father_conf_path)
print(is_path)
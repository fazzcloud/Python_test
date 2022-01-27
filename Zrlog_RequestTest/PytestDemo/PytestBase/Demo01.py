import pytest
def test_login():
    print("我是会被执行的")

def testlogin():
    print("我也是会被执行的")
def login_test():
    print("我不会被执行")
def logintest():
    print("我不会被执行")

if __name__ == '__main__':
    '''
    运行方式：直接在文件内执行以下命令
    其中，-v参数显示命令执行过程，-s参数显示打印的信息
    不加-s参数，则print()函数打印的信息不会显示
    '''
    pytest.main(['-s','-v','Demo01.py'])
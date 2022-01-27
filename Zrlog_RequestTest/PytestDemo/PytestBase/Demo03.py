import pytest
'''
一个参数的参数化，username依次取出列表中的字符串对象
通过test_login()函数打印
'''
@pytest.mark.parametrize("username",["fazz","jack","cloud"])
def test_login(username):
    print("success,username is %s"%(username))
if __name__ == '__main__':
    pytest.main(['-s','-v','Demo03.py'])
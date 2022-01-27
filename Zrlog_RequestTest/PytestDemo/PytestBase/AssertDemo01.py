import pytest
x = 1
y = 0
z = 1
str1 = 'pythontest'
str2 = 'python'

def test_assert():#断言x为真
    assert x
    #True和False在python中都是关键字，并且总是等于1和0，所以x=1就相当于x=True

def test_assert02():#断言x不为真
    assert not y
    #assert not 表示不为真，因为y = 0相当于Y = False

def test_assert03():#断言x不为真
    assert  y
    #assert not 表示不为真，因为y = 0相当于Y = False
def test_assert04():#断言str1包含str2
    assert str2 in str1

#将异常写在函数里
def test_assert05():#断言x等于y
    try:
        assert x == z
        print("pass")
    except Exception as  e:
        print("error,not equals")

def test_assert06():#断言x不等于y
    try:
        assert x != y
        print("pass")
    except Exception as  e:
        print("error,not equals")

if __name__ == "__main__":
    pytest.main(['-s','-v','AssertDemo01.py'])
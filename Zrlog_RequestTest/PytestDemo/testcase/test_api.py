import pytest
def test_login():
    print('我是会被执行的')

def testlogin():
    print('我也是会被执行的')

if __name__ == 'main':
    pytest.main(['-s','-v','test_api.py'])
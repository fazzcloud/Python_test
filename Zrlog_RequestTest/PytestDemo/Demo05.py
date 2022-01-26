import pytest
@pytest.mark.parametrize("header",[("http"),("https")])
@pytest.mark.parametrize("host",[("192.168.3.201"),("106.14.135.177")])
def test_post(header,host):
    print(f" ip is {header}：//{host}".format(header=header,host=host))

if __name__ == '__main__':
    pytest.main(['-s','-v','Demo05.py'])
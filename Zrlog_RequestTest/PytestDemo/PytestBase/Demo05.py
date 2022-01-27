import pytest
@pytest.mark.parametrize("header,host",[("http","192.168.3.201"),('https',"106.14.135.177")])
#@pytest.mark.parametrize("host",[])
def test_post(header,host):
    print(f" ip is {header}：//{host}".format(header=header,host=host))

if __name__ == '__main__':
    pytest.main(['-s','-v','Demo05.py'])
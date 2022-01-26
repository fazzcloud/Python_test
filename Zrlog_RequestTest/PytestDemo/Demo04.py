import  pytest
@pytest.mark.parametrize('username',[('fazz1','fazz2'),(3,4)])
def test_login(username):
    print('username is :{username}'.format(username = username))

@pytest.mark.parametrize('userid', [{'fazz1': 1}, {'fazz2': 2}, {'fazz3': 3}, {'fazz4': 4}])
def test_login2(userid):
    print('user id is :{userid}'.format(userid = userid))

if __name__ == '__main__':
    pytest.main(['-s','-v','Demo04.py'])

#这里注意，每一个参数化，要写在对应的每一个函数或方法前面
import pytest

class TestOrdering():
    def test_login(self):
        print("loging")

    def test_add(self):
        print("adding")

    def deltest(self):
        print("deling")

class testing():
    def test_login2(self):
        print("loging")

    def test_add2(self):
        print("adding")

    def deltest2(self):
        print("deling")

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'Demo02.py'])
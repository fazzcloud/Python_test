import pytest

def setup_module():
    print("注意：这是模块前置，在整个py文件前出现")

def teardown_module():
    print("注意：这是模块后置，在整个py文件后出现")
def setup_function():
    print("注意：这是函数前置，在每个函数前出现")

def teardown_function():
    print("注意：这是函数后置，在每个函数后出现")

def test01():
    print("函数：用例1")

def test02():
    print("函数：用例2")

class Test: #注意这里一定要开头大写，否则不会自动执行

    def setup_class(self):
        print("注意：这是类前置，在类前出现")

    def teardown_class(self):
        print("注意：这是类后置，在类后出现")

    def setup_method(self):
            print("注意：这是方法前置，在方法前出现")

    def teardown_method(self):
            print("注意：这是方法后置，在方法后出现")

    def setup(self):
            print("注意：这是方法细化前置，在方法前，且setup_method后在出现")

    def teardown(self):
            print("注意：这是方法细化后置，在方法后，且在teardown_method前出现")

    def test03(self):
        print("方法：用例3")

    def test04(self):
        print("方法：用例4")

if __name__ == '__main__':
    pytest.main(['-s','-v','Demo06.py'])
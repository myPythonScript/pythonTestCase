
def setup_module():
    print("模块准备")

def teardown_module():
    print("模块清理")


def setup_function():
    print('准备')

def teardown_function():
    print('清理')


def test_1():
    print('test_1')
    

def test_2():
    print('test_2')


def test_3():
    print('test_3')


class TestA(object):
    def setup_class(self):
        print("类准备")

    def teardown_class(self):
        print("类清理")

    def setup_method(self):
        print("方法准备")

    def teardown_method(self):
        print("方法清理")

    def test_a(self):
        print('test_a')


    def test_b(self):
        print('test_b')

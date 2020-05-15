import pytest


@pytest.fixture()
def my():
    print('setup')
    yield 123
    print('teardown')

@pytest.fixture(scope='function', autouse=True)
def my2():
    print('my2 setup')


@pytest.mark.usefixtures('my')
def test_1():
    print('test_1')
    # print(my)


def test_2():
    print('test_2')


import pytest
from utils.data import Data
from utils.api import Api
#api接口地址
# 内网
# base_url = 'http://192.168.1.88'
# 外网
base_url = "http://114.67.225.196"

@pytest.fixture(scope = 'session')
def data():
    #数据文件名
    data = Data('data.yaml').from_yaml()
    return data

# @pytest.fixture(scope = 'session')
# def db():
#     try:
#         db = DB()
#     except Exception as ex:
#         pytest.skip(str(ex))
#     else:
#         yield db
#         db.close()

@pytest.fixture(scope = 'session')
def api():
    api = Api(base_url)
    return api

@pytest.fixture
def case_data(request,data):
    case_name = request.function.__name__
    case_data = data.get(case_name)
    print('用例名称为：%s' % case_name)
    print('用例参数为：%s' % case_data)
    return case_data


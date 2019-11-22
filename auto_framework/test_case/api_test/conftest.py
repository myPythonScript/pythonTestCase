import pytest
from utils.data import Data
from utils.db import DB
from utils.api import Api
#api接口地址
base_url = 'http://115.28.108.130:8080'

@pytest.fixture(scope = 'session')
def data():
    data = Data('data.json').from_json()
    return data

@pytest.fixture(scope = 'session')
def db():
    try:
        db = DB()
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        yield db
        db.close()

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


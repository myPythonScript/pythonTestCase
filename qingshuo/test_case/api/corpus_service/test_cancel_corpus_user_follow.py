import pytest_check as ck
import pytest
from jsonschema import validate


# 取消关注文集
@pytest.mark.api
@pytest.mark.run(order=3)
# @pytest.mark.dependency(depends=['corpus_service/test_query_is_follow_corpus.py::test_query_is_follow_corpus'],scope='session')
def test_cancel_corpus_user_follow(case_data, api):
    # 读取yaml文件中的数据并拆分
    url = case_data['url']
    headers = case_data['headers']
    para = case_data['params']

    # 执行接口测试
    res = api.get(url, headers, **para)
    result = res.json()
    schema = {
        "type": "object",
        "properties": {
            "resultCode": {
                "type": "integer"
            },
            "resultMessage": {
                "type": "string"
            }
        },
        "required": ["resultCode", "resultMessage"]
    }
    validate(result, schema)
    ck.equal(result["resultCode"], 1)
    ck.equal(result["resultMessage"], "success")

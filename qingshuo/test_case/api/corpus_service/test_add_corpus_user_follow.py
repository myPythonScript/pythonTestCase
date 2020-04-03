import pytest_check as ck
import pytest
from jsonschema import validate


# 关注文集
@pytest.mark.api
@pytest.mark.run(order=1)
# @pytest.mark.dependency()
def test_add_corpus_user_follow(case_data, api):
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
    test_sch = validate(result, schema)
    # return test_sch, result
    ck.equal(result["resultCode"], 1)
    ck.equal(result["resultMessage"], "success")







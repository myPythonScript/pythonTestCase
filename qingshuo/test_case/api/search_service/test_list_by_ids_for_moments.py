import pytest_check as ck
import pytest
from jsonschema import validate


# 搜索热标签列表
@pytest.mark.api
def test_list_by_ids_for_moments(case_data, api):
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
            },
            "data": {
                "type": "array",
                "items": {
                    "properties": {
                        "corpusId": {"type": "integer"},
                    },
                    "required": ["corpusId"]
                }
            }
        },
        "required": ["resultCode", "resultMessage", "data"]
    }
    validate(result, schema)

    ck.equal(res.status_code, 200)
    ck.equal(result["resultCode"], 1)

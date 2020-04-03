import pytest
import pytest_check as ck
from jsonschema import validate


@pytest.mark.api
def test_find_follow_corpus_by_user(case_data, api):
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
                        "corpusName": {
                            "type": "string",
                            "maxLength": 21,
                            "minLength": 1
                        },
                        "summary": {
                            "type": "string",
                            "maxLength": 150,
                            "minLength": 0
                        },
                        "sysUserAcc": {
                            "type": "object",
                            "properties": {
                                "accId": {"type": "integer"},
                                "userId": {"type": "integer"},
                                "name": {"type": "string"}
                            }
                        }
                    }
                }
            }
        },
        "required": ["resultCode", "resultMessage"]
    }
    validate(result, schema)

    ck.equal(result["resultCode"], 1)
    ck.equal(result["resultMessage"], "success")

import pytest_check as ck
import pytest
from jsonschema import validate


# 搜索热标签列表
@pytest.mark.api
@pytest.mark.skip
def test_list_trending_tag(case_data, api):
    url = case_data['url']
    headers = case_data['headers']
    res = api.get(url, headers)
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
                        "tagId": {"type": "integer"},
                        "tagName": {"type": "string"},
                        "countFollow": {
                            "type": "integer",
                            "minimum": 0
                        },
                        "countContent": {
                            "type": "integer",
                            "minimum": 0
                        }
                    },
                    "required": ["tagId", "tagName"]
                }
            }
        },
        "required": ["resultCode", "resultMessage", "data"]
    }
    validate(result, schema)

    ck.equal(result["resultCode"], 1)

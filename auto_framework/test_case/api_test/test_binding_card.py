import pytest_check as ck
import pytest

@pytest.mark.skip
@pytest.mark.api
def test_bingding_card(case_data,api):
    # 读取yaml文件中的数据并拆分
    url = case_data['url']
    para = case_data['data']
    cardnumber = para['CardInfo']['cardNumber']

    # 执行接口测试
    res = api.post(url, **para)
    # 验证返回数据
    ck.equal(res.json()['code'], 5010)
    ck.equal(res.json()['msg'], '绑定成功')
    ck.equal(res.json()['result["UserId"]'], 5616656)
    return cardnumber




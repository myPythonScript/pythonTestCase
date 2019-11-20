import pytest_check as ck
import pytest

@pytest.mark.skip
def test_qury_card(case_data,api):
    # 读取yaml文件中的数据并拆分
    url = case_data['url']
    para = case_data['data']
    # 执行接口测试
    add_res = api.post(url, **para)
    # 验证返回数据
    ck.equal(add_res.json()['code'], 200)
    ck.equal(add_res.json()['msg'], '成功返回')
    ck.equal(add_res.json()['success'], True)



import pytest_check as ck
from logging import log
import pytest

@pytest.mark.api
def test_add_card(case_data,db,api):
    # 读取yaml文件中的数据并拆分
    url = case_data['url']
    para = case_data['data']
    cardnumber = para['CardInfo']['cardNumber']
    # 在数据库中查询卡号是否已存在
    get_num = db.qury('cardinfo', 'cardNumber', cardnumber)
    if get_num == None:
        print('卡号不存在,可以添加')
    else:
        db.delete('cardinfo', 'cardNumber', cardnumber)
        print('已删除该卡号,可以添加')
    # 执行接口测试
    res = api.post(url, **para)
    # 验证返回数据
    ck.equal(res.json()['code'], 200)
    ck.equal(res.json()['msg'], '添加卡成功')
    ck.equal(res.json()['success'], False)
    return cardnumber
    # 清除数据
    db.delete('cardinfo', 'cardNumber', cardnumber)
    print('数据已清理')
    log.info("添加的数据已被清理")




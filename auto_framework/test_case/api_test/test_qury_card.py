# import pytest_check as ck
#
# def test_add_card(case_data,db,api):
#     try:
#         #第一步添加加油卡
#         #读取yaml文件中的数据并拆分
#         url = case_data['url']
#         para = case_data['data']
#         cardnumber = para['CardInfo']['cardNumber']
#         #在数据库中查询卡号是否已存在
#         get_num = db.qury('cardinfo','cardNumber',cardnumber)
#         if get_num == None:
#             print('卡号不存在,可以添加')
#         else:
#             db.delete('cardinfo','cardNumber',cardnumber)
#             print('已删除该卡号,可以添加')
#         #执行接口测试
#         add_res = api.post(url,**para)
#         #验证返回数据
#         ck.equal(add_res.json()['code'], 200)
#         ck.equal(add_res.json()['msg'], '添加卡成功')
#         ck.equal(add_res.json()['success'], False)
#         #第二步：查询刚添加的加油卡
#         qury_res = api.get(url,**para)
#         ck.equal(add_res.json()['code'], 200)
#         ck.equal(add_res.json()['msg'], '添加卡成功')
#         ck.equal(add_res.json()['success'], False)
#     except Exception as ex:
#         print('出现异常情况，信息为：%s'%ex)
#

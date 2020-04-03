import pytest_check as ck
import pytest


# 查询文集类型模板
@pytest.mark.api
def test_list_corpus_tmpl(case_data, api):
    # 读取yaml文件中的数据并拆分
    url = case_data['url']
    headers = case_data['headers']
    # 执行接口测试
    res = api.get(url, headers)
    result = res.json()
    # print(res.text)
    # 验证返回数据
    # 1.自媒体
    ck.equal(result['resultCode'], 1)
    ck.equal(result['resultMessage'], 'success')
    ck.equal(result['data'][0]['tmplId'], 1)
    ck.equal(result['data'][0]['tmplName'], '自媒体')
    ck.equal(result['data'][0]['tmplSign'], '您对外发布内容,展示生活窗口')
    ck.equal(result['data'][0]['tmplDesc'], '')
    ck.equal(result['data'][0]['permitList'][0]['desc'], '内容可见权限')
    ck.equal(result['data'][0]['permitList'][1]['desc'], '添加成员权限')
    ck.equal(result['data'][0]['permitList'][2]['desc'], '可投稿权限')
    # 2.资讯平台
    ck.equal(result['data'][1]['tmplId'], 2)
    ck.equal(result['data'][1]['tmplName'], '资讯平台')
    ck.equal(result['data'][1]['tmplSign'], '')
    ck.equal(result['data'][1]['tmplDesc'], '对于您希望涉及的领域进行专业的内容收集、展示的窗口\r\n您可以自己发布内容，也可以接受投稿')
    ck.equal(result['data'][1]['permitList'][0]['desc'], '内容可见权限')
    ck.equal(result['data'][1]['permitList'][1]['desc'], '添加成员权限')
    ck.equal(result['data'][1]['permitList'][2]['desc'], '可投稿权限')
    # 3.开放话题组
    ck.equal(result['data'][2]['tmplId'], 3)
    ck.equal(result['data'][2]['tmplName'], '开放话题组')
    ck.equal(result['data'][2]['tmplSign'], '')
    ck.equal(result['data'][2]['tmplDesc'], '对于您希望涉及的领域,与平台其他用户进行交流讨论')
    ck.equal(result['data'][2]['permitList'][0]['desc'], '内容可见权限')
    ck.equal(result['data'][2]['permitList'][1]['desc'], '添加成员权限')
    ck.equal(result['data'][2]['permitList'][2]['desc'], '可投稿权限')
    # 4.私密话题组
    ck.equal(result['data'][3]['tmplId'], 4)
    ck.equal(result['data'][3]['tmplName'], '私密话题组')
    ck.equal(result['data'][3]['tmplSign'], '')
    ck.equal(result['data'][3]['tmplDesc'], '对于您希望涉及的领域,与您所需要的特定用户进行交流讨论')
    ck.equal(result['data'][3]['permitList'][0]['desc'], '内容可见权限')
    ck.equal(result['data'][3]['permitList'][1]['desc'], '添加成员权限')
    ck.equal(result['data'][3]['permitList'][2]['desc'], '可投稿权限')
    # 5.日记本
    ck.equal(result['data'][4]['tmplId'], 5)
    ck.equal(result['data'][4]['tmplName'], '日记本')
    ck.equal(result['data'][4]['tmplSign'], '')
    ck.equal(result['data'][4]['tmplDesc'], '记录日记')
    ck.equal(result['data'][4]['permitList'][0]['desc'], '内容可见权限')
    ck.equal(result['data'][4]['permitList'][1]['desc'], '添加成员权限')
    ck.equal(result['data'][4]['permitList'][2]['desc'], '可投稿权限')
    # 6.自定义
    ck.equal(result['data'][5]['tmplId'], 6)
    ck.equal(result['data'][5]['tmplName'], '自定义')
    ck.equal(result['data'][5]['tmplSign'], '')
    ck.equal(result['data'][5]['tmplDesc'], '自定义您的小站配置')
    ck.equal(result['data'][5]['permitList'][0]['desc'], '内容可见权限')
    ck.equal(result['data'][5]['permitList'][1]['desc'], '添加成员权限')
    ck.equal(result['data'][5]['permitList'][2]['desc'], '可投稿权限')

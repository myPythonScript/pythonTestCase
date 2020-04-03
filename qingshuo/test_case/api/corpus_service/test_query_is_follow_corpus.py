import pytest
import pytest_check as ck


@pytest.mark.api
@pytest.mark.run(order=2)
# @pytest.mark.dependency()
# @pytest.mark.dependency(depends=['corpus_service/test_add_corpus_user_follow.py::test_add_corpus_user_follow'],scope='session')
def test_query_is_follow_corpus(case_data, api):
    # 读取yaml文件中的数据并拆分
    url = case_data['url']
    headers = case_data['headers']
    para = case_data['params']

    # 执行接口测试
    res = api.get(url, headers, **para)
    result = res.json()

    ck.equal(result, True)

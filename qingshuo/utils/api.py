''' 请求方法 '''
import requests


class Api(object):
    def __init__(self, base_url=None):
        self.session = requests.session()
        self.base_url = base_url

    def request(self, method, url, headers, **kwargs):
        url = self.base_url + url if self.base_url else url
        print('Api:%s' % url)
        response = requests.request(method, url, headers=headers, **kwargs)
        return response

    def get(self, url, headers, **kwargs):
        res = self.request('get', url, headers, params=kwargs)
        return res

    def post(self, url, **kwargs):
        res = self.request('post', url, json=kwargs)
        return res

    def put(self, url, **kwargs):
        res = self.request('put', url, json=kwargs)
        return res

    def patch(self, url, **kwargs):
        res = self.request('patch', url, parsms=kwargs)
        return res

    def delete(self, url, **kwargs):
        res = self.request('delete', url, json=kwargs)
        return res


# if __name__ == "__main__":
#     api_url = 'http://114.67.225.196/corpus-service/addCorpusUserFollow'
#     header = {"uId": "88731867704197357"}
#     para = {
#         "corpusId": 89821694436573357
#     }
#     res = Api()
#     result = res.get(api_url, header, **para)
#     print(result.json()["resultMessage"])

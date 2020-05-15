# -*- coding: UTF-8 -*-
import requests
import pytest
import yaml

def get_data():
	with open ('apis.yaml',encoding="utf-8") as f:
		data1 = yaml.safe_load(f)
	return data1

@pytest.mark.parametrize('para',get_data())
def test_login(para):
	lists = list(para.values())
	lists2 = list(para.keys())
	for i in lists2:
		if i == "headers":
			headers = para[i]
		elif i == "json":
			json = para[i]
		elif i == 'data':
			data = para[i]
		else:
			headers = ''
			json = ''
			data = ''
	method = lists[0]
	url = lists[1]
	res = requests.request(method = method,url = url,headers = headers,data= data ,json = json)
	assert res.status_code == 200

if __name__ == '__main__':
	pytest.main(['test_apis.py','-qs','--html=./report1.html'])

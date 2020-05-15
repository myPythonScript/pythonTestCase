import requests
from learning.dbSQL import DB

db1 = DB()

#添加卡
def test_add_card():
	db1.del_sql('delete from longtengserver.cardinfo where cardNumber = "12345678"')
	url = 'http://115.28.108.130:8080/gasStation/process'
	add_data = {
	"dataSourceId": "bHRz",
	"methodId": "00A",
	"CardInfo": {
		"cardNumber": "12345678"
	}
}
	response = requests.post(url,json = add_data)
	assert "添加卡成功" == response.json()['msg']
	cardNum = add_data['CardInfo']['cardNumber']

	# 绑定卡
	idNumber=db1.select_sql("SELECT idNumber FROM longtengserver.carduser "
							"left join longtengserver.cardinfo on "
							"longtengserver.carduser.userId = longtengserver.cardinfo.userId "
							"where cardNumber is null")["idNumber"]
	uName = db1.select_sql("SELECT userName FROM longtengserver.carduser "
							"left join longtengserver.cardinfo on "
							"longtengserver.carduser.userId = longtengserver.cardinfo.userId "
							"where cardNumber is null")["userName"]
	bind_data = {
		"dataSourceId": "bHRz",
		"methodId": "01A",
		"CardUser": {
			"userName": uName,
			"idType": "1",
			"idNumber": idNumber
		},
		"CardInfo": {
			"cardNumber": cardNum
		}
	}
	response = requests.post(url, json = bind_data)
	assert "绑定成功" == response.json()['msg']
	userid = response.json()['result']['UserId']

	# 卡充值
	paycheck_data = {
		"dataSourceId": "bHRz",
		"methodId": "03A",
		"CardInfo": {
			"cardNumber": cardNum,
			"cardBalance": "50"
		}
	}
	response = requests.post(url, json = paycheck_data)
	assert "充值成功" == response.json()['msg']

	# 卡消费
	data = {
	"dataSourceId": "bHRz",
	"methodId": "04A",
	"CardUser": {
		"userId":userid
	},
	"CardInfo": {
		"cardNumber": cardNum,
		"cardBalance": "50"
	}
}
	response = requests.post(url,json = data)
	assert "消费成功!" == response.json()['msg']

	#查询卡
	params = {
		"dataSourceId": "bHRz",
		"userId": userid,
		"cardNumber": cardNum,
		"methodId": "02A"
	}
	response = requests.get(url,params = params)
	assert "成功返回" == response.json()['msg']

#重复新加卡
def test_reAdd():
	cardNum = db1.select_sql('SELECT cardNumber FROM longtengserver.cardinfo')["cardNumber"]
	url = 'http://115.28.108.130:8080/gasStation/process'
	add_data = {
		"dataSourceId": "bHRz",
		"methodId": "00A",
		"CardInfo": {
			"cardNumber": cardNum
		}
	}
	response = requests.post(url, json=add_data)
	assert "该卡已添加" == response.json()['msg']

#重复绑定卡
def test_reBind():
	cardNumber = db1.select_sql('SELECT cardNumber FROM longtengserver.carduser '
				  'left join longtengserver.cardinfo '
				  'on longtengserver.carduser.userId = longtengserver.cardinfo.userId '
				  'where cardNumber is not null')["cardNumber"]
	idNumber = db1.select_sql("SELECT idNumber FROM longtengserver.carduser "
				   "left join longtengserver.cardinfo "
				   "on longtengserver.carduser.userId = longtengserver.cardinfo.userId "
				   "where cardNumber is not null")["idNumber"]
	userName = db1.select_sql("SELECT userName "
				  "FROM longtengserver.carduser "
				  "left join longtengserver.cardinfo  "
				  "on longtengserver.carduser.userId = longtengserver.cardinfo.userId "
				  "where cardNumber is not null")["userName"]
	url = 'http://115.28.108.130:8080/gasStation/process'
	bind_data = {
		"dataSourceId": "bHRz",
		"methodId": "01A",
		"CardUser": {
			"userName": userName,
			"idType": "1",
			"idNumber": idNumber
		},
		"CardInfo": {
			"cardNumber": cardNumber
		}
	}
	response = requests.post(url, json = bind_data)
	assert "卡已经被绑定,无法绑定" == response.json()['msg']
#
#充值后查询
def test_paycheck():
	cardnumber = db1.select_sql("SELECT cardNumber FROM longtengserver.cardinfo")["cardNumber"]
	url = 'http://115.28.108.130:8080/gasStation/process'
	paycheck_data = {
		"dataSourceId": "bHRz",
		"methodId": "03A",
		"CardInfo": {
			"cardNumber": cardnumber,
			"cardBalance": "50"
		}
	}
	response = requests.post(url, json = paycheck_data)
	assert "充值成功" == response.json()['msg']
	cardnumber = response.json()['result']['cardNumber']
	userid = response.json()['result']['userId']

	params = {
		"dataSourceId": "bHRz",
		"userId": userid,
		"cardNumber": cardnumber,
		"methodId": "02A"
	}
	res = requests.get(url,params = params)
	assert "成功返回" == res.json()['msg']
	assert cardnumber == res.json()['result']['cardNumber']

#充值卡号不存在
def test_paycheck():

	url = 'http://115.28.108.130:8080/gasStation/process'
	paycheck_data = {
		"dataSourceId": "bHRz",
		"methodId": "03A",
		"CardInfo": {
			"cardNumber": "0000999",
			"cardBalance": "50"
		}
	}
	response = requests.post(url, json = paycheck_data)
	assert "加油卡号不存在" == response.json()['msg']

#查询卡不存在
def test_search():
	url = 'http://115.28.108.130:8080/gasStation/process'
	params = {
		"dataSourceId": "bHRz",
		"userId": "10159",
		"cardNumber": "0000999",
		"methodId": "02A"
	}
	res = requests.get(url,params = params)
	assert "无查询信息" == res.json()['msg']

#充值金额不能为空
def test_paycheck_null():
	cardNumber = db1.select_sql("SELECT cardNumber FROM longtengserver.cardinfo  LIMIT 1")["cardNumber"]
	url = 'http://115.28.108.130:8080/gasStation/process'
	paycheck_data = {
		"dataSourceId": "bHRz",
		"methodId": "03A",
		"CardInfo": {
			"cardNumber": cardNumber,
			"cardBalance": ""
		}
	}
	response = requests.post(url, json = paycheck_data)
	assert "金额不能为空" == response.json()['msg']

#充值金额不能为小数
def test_paycheck_false():
	cardNumber = db1.select_sql("SELECT cardNumber FROM longtengserver.cardinfo  LIMIT 1")["cardNumber"]
	url = 'http://115.28.108.130:8080/gasStation/process'
	paycheck_data = {
		"dataSourceId": "bHRz",
		"methodId": "03A",
		"CardInfo": {
			"cardNumber": cardNumber,
			"cardBalance": "1.234"
		}
	}
	response = requests.post(url, json = paycheck_data)
	assert "金额需为整数" == response.json()['msg']

#每个用户只能绑定两张以下的卡
def test_reBind_max():
	uName = db1.select_sql("SELECT userName FROM longtengserver.carduser "
						   "right join longtengserver.cardinfo "
						   "on longtengserver.carduser.userId = longtengserver.cardinfo.userId "
						   "group by longtengserver.carduser.idNumber "
						   "having count(idNumber)>1")["userName"]
	iNumber = db1.select_sql("SELECT idNumber FROM longtengserver.carduser "
							 "right join longtengserver.cardinfo "
							 "on longtengserver.carduser.userId = longtengserver.cardinfo.userId "
							 "group by longtengserver.carduser.idNumber "
						     "having count(idNumber)>1")["idNumber"]
	cNumber = db1.select_sql("SELECT cardNumber FROM longtengserver.carduser "
							 "right join longtengserver.cardinfo "
							 "on longtengserver.carduser.userId = longtengserver.cardinfo.userId "
							 "where idNumber is null")["cardNumber"]
	url = 'http://115.28.108.130:8080/gasStation/process'
	bind_data = {
		"dataSourceId": "bHRz",
		"methodId": "01A",
		"CardUser": {
			"userName": uName,
			"idType": "1",
			"idNumber": iNumber
		},
		"CardInfo": {
			"cardNumber": cNumber
		}
	}
	response = requests.post(url, json = bind_data)
	assert "每个用户只能绑定两张卡" == response.json()['msg']

#绑定卡，卡号不能为空
def test_reBind_null():
	uName = db1.select_sql("SELECT userName FROM longtengserver.carduser "
						   "left join longtengserver.cardinfo "
						   "on longtengserver.carduser.userId = longtengserver.cardinfo.userId "
						   "where cardNumber is null")["userName"]
	iNumber = db1.select_sql("SELECT idNumber FROM longtengserver.carduser "
						   "left join longtengserver.cardinfo "
						   "on longtengserver.carduser.userId = longtengserver.cardinfo.userId "
						   "where cardNumber is null")["idNumber"]
	url = 'http://115.28.108.130:8080/gasStation/process'
	bind_data = {
		"dataSourceId": "bHRz",
		"methodId": "01A",
		"CardUser": {
			"userName": uName,
			"idType": "1",
			"idNumber": iNumber
		},
		"CardInfo": {
			"cardNumber": ""
		}
	}
	response = requests.post(url, json = bind_data)
	assert "卡号不能为空!" == response.json()['msg']
	print(response.json()['msg'])

#新增卡并绑定后，查询余额
def test_add_search():
	db1.del_sql('delete from longtengserver.cardinfo where cardNumber = "890890"')
	url = 'http://115.28.108.130:8080/gasStation/process'
	add_data = {
	"dataSourceId": "bHRz",
	"methodId": "00A",
	"CardInfo": {
		"cardNumber": "890890"
	}
}
	response = requests.post(url,json = add_data)
	assert "添加卡成功" == response.json()['msg']
	cardNum = add_data['CardInfo']['cardNumber']

	idNumber = db1.select_sql("SELECT idNumber FROM longtengserver.carduser "
							  "left join longtengserver.cardinfo on "
							  "longtengserver.carduser.userId = longtengserver.cardinfo.userId "
							  "where cardNumber is null")["idNumber"]
	uName = db1.select_sql("SELECT userName FROM longtengserver.carduser "
						   "left join longtengserver.cardinfo "
						   "on longtengserver.carduser.userId = longtengserver.cardinfo.userId "
						   "where cardNumber is null")["userName"]
	bind_data = {
	"dataSourceId": "bHRz",
	"methodId": "01A",
	"CardUser": {
		"userName": uName,
		"idType": "1",
		"idNumber": idNumber
		},
	"CardInfo": {
		"cardNumber": cardNum
		}
	}
	response = requests.post(url, json = bind_data)
	assert "绑定成功" == response.json()['msg']
	userid = response.json()['result']['UserId']

	url = f'http://115.28.108.130:8080/gasStation/process'
	params = {
		"dataSourceId": "bHRz",
		"userId": userid,
		"cardNumber": cardNum,
		"methodId": "02A"
	}
	res = requests.get(url,params = params)
	assert "成功返回" == res.json()['msg']

	params = {
		"dataSourceId": "bHRz",
		"userId": userid,
		"cardNumber": cardNum,
		"methodId": "02A"
	}
	res = requests.get(url,params = params)
	assert "0" == res.json()['result']['cardBalance']

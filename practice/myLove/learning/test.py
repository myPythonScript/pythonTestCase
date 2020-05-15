# import requests
# def test_chaxun_01():  # 查询已添加且绑定的加油卡
#     url = "http://115.28.108.130:8080/gasStation/process"
#     data1 = {
#         "dataSourceId": "bHRz",
#         "methodId": "01A",
#         "CardUser": {
#             "userName": "pili",
#             "idType": "1",
#             "idNumber": "668"
#         },
#         "CardInfo": {
#             "cardNumber": "274875"
#         }}
#     res1 = requests.post(url=url, json=data1)
#     print(res1.json())
#     userId = res1.json()['result']['UserId']
#     url = f"http://115.28.108.130:8080/gasStation/process?"
#     data = {"dataSourceId": "bHRz",
#             "cardNumber": "274875",
#             "userId": userId,
#             "methodId": "02A"
#             }
#     reponse = requests.get(url=url, params=data)
#
#     print(reponse.json())
#     assert "成功返回" == reponse.json()["msg"]
#     assert "已经被绑定,正常使用中" == reponse.json()["result"]["cardStatus"]



print({"name":"123"}["name"])
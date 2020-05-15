#coding:utf-8
def test1():
	print("----test1-----")
	print(num)
	print("----test2----")

def test2():
	print("---test2-1----")
	test1()
	print("---test2-2---")
def test3():
	try:
		print("----test3-1---")
		test1()
		print("----test3-2----")
	except Exception as result:
		print("捕获到了异常，信息是:%s"%result)
	print("---test3-3----")
test3()
print("-----分割线----")
test2()
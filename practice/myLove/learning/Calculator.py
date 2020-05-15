#coding:utf-8
#加法
def add(num1,num2):
	result = num1 + num2
	return result
#减法
def subtract(num1,num2):
	result = num1 - num2
	return result
#乘法
def multiply(num1,num2):
	result = num1 * num2
	return result
#除法
def divide(num1,num2):
	result = num1 / num2
	return result

try:
	symbol = input("请输入运算符号(+-*/):")
	while symbol == "+" or symbol == "-" or symbol == "*" or symbol == "/":
		n1 = int(input("请输入第一个数:"))
		n2 = int(input("请输入第二个数:"))
		if symbol == "+":
			res = add(n1,n2)
			print("%d+%d=%d"%(n1,n2,res))
		elif symbol == "-":
			res = subtract(n1, n2)
			print("%d-%d=%d" % (n1, n2, res))
		elif symbol == "*":
			res = multiply(n1, n2)
			print("%d*%d=%d" % (n1, n2, res))
		else:
			res = divide(n1, n2)
			print("%d/%d=%d" % (n1, n2, res))
		symbol = input("请输入运算符号(+-*/):")
	else:
		print("输入的不是算术运符，请重新开始")
except Exception as error:
	print("捕获到了异常，信息是:%s"%error)
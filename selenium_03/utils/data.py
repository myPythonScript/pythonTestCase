"""数据文件读取"""
import csv


def load_csv(file_path):
	"""读取csv文件，返回列表"""
	print("读取csv文件")
	with open(file_path, encoding='utf-8') as f:
		reader = csv.reader(f)
		data = list(reader)
	print("数据列表", data)
	return data

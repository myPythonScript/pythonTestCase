#coding:utf-8
import xlsxwriter
#创建一个文件
file_name = "第一个excle.xlsx"
workbook = xlsxwriter.Workbook(file_name)

#创建一个工作表
worksheet = workbook.add_worksheet("my_sheet")
#写单元格
worksheet.write(0,0,"hello")
worksheet.write('A2','有解')

#写入列
worksheet.write_row(2,0,[1,2,3,4,5,6])
#写入列
worksheet.write_column("A5",["nihao","我可以"])
#写入数据
#写入url
worksheet.write_url(0,1,"http://www.baidu.com")
#写入图片
#worksheet.insert_image("E5","img.jpg")
#写入公式
worksheet.write_formula("A6","=sum(1,23)")
#关闭
workbook.close()

'''
f = open("hello.txt","w",encoding="utf-8")
f.write("输入一行内容")
f.writelines(["可输入多行内容\n","这是一个txt文档\n","第二行数据在这\n","3是一个好数字"])
f.close()

f = open("hello.txt","r",encoding="utf-8")
info = f.read()
# info2 = f.readlines()#按照行的方式一次性读取，返回一个列表。read和readlines只能用一个不可重复使用，前一个输出内容，后一人为空
print(info)
# print(info2)
f.close()
'''
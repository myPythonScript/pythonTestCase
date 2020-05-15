#encoding = utf-8
import pymysql

class DB(object):
	def get_conn(self,sql):
		self.conn = pymysql.connect(
			host = '115.28.108.130',
			port = 3306,
			user = 'test',
			password = 'abc123456',
			db = 'api_test',
			charset = 'utf8',
			autocommit=True  # 使用autocommit
		)
		#建立游标
		self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
	def select_sql(self, sql):
		DB.get_conn(self,sql)
		self.cur.execute(sql)  # 执行sql
		result = self.cur.fetchone()  # 获取所有查询结果,字典形式显示
		return result
	def insert_sql(self,sql):
		DB.get_conn(self,sql)
		self.cur.execute(sql)
		self.conn.commit()  # 提交插入数据
	def del_sql(self,sql):
		DB.get_conn(self, sql)
		self.cur.execute(sql)
		self.conn.commit()  # 提交插入数据
	def execute(self,sql):
		try:
			self.cur.execute(sql)#执行sql
		except Exception as e:
			self.conn.rollback()#回滚

	def close(self):
		self.cur.close()  # 关闭游标
		self.conn.close()  # 关闭连接


# 		#执行sql语句,查找
# 		self.cur.execute('select * from user')#不返回查询结果
# 		print(cur.fetchone())#取完就删除
# 		print(cur.fetchmany(3))#取几个值
# 		print(cur.fetchall())#取所有值
#
#
# #插入
# cur.execute('insert into user(name,passwd) values ("七七","123456")')
# conn.commit()#提交插入数据


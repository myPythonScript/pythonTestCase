'''连接数据库'''
import pymysql
import os

DB_CONNF = {
    'host':os.getenv('MYSQL_HOST'),
    'port':int(os.getenv('MYSQL_PORT')),
    'user':os.getenv('MYSQL_USER'),
    'password':os.getenv('MYSQL_PWD'),
    'db':os.getenv('MYSQL_SERVER'),
    'charset':'utf8'
}

# DB_CONNF = {
#     "host":"115.28.108.130",
 #     "db": "longtengserver",
#     "user": "test",
#     "password": "abc123456",
#     "port": 3306,
#     "charset": "utf8"
# }
class DB(object):
    def __init__(self,conf = DB_CONNF):
        # 连接数据库
        self.conn = pymysql.connect(**conf, autocommit=True)
        # 创建游标，以字典"{}"型式返回结果
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
    #查找数据
    def qury(self,table_name,Column_name,value ):
        #执行sql语句
        self.cur.execute(f'select * from {table_name} where {Column_name} = {value}')
        #返回5条数据
        result = self.cur.fetchone()
        return result
    #更改数据
    def update(self,table_name,Column_name,new_value,value):
        self.cur.execute(f'update {table_name} set {Column_name} = {new_value} where {Column_name} = {value}')
    #删除数据
    def delete(self,table_name,Column_name,value):
        self.cur.execute(f'DELETE FROM {table_name} WHERE {Column_name} = {value}')
        print('db中执行了delete语句')
    #左外连接两表联合查询
    def left_join(self,left_tabel_name,right_tabel_name,Column_name,value):
        self.cur.execute(f'select * from {left_tabel_name} left join {right_tabel_name} on {left_tabel_name}.{Column_name} = {left_tabel_name}.{Column_name} wherer {left_tabel_name}.{Column_name} = {value} ')
    #关闭连接
    def close(self):
        self.cur.close()
        self.conn.close()

# if __name__ == '__main__':
#     db = DB()
#     res = db.qury('cardinfo','cardNumber','12301230')
#     print(res)
#     if res == None:
#         print('卡号不存在,可以添加')
#     else:
#         db.delete('cardinfo','cardNumber','12301230')
#         print('已删除该卡号,可以添加')











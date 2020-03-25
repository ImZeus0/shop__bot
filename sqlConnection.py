import pymysql.cursors
import config
	
def connect():
	connection = pymysql.connect(config.HOST,config.USER,config.PASS,config.DB,config.PORT)
	print('200')
	return connection

def insert(connection,name,type_file,coast):
		cur = connection.cursor()
		sql ='INSERT INTO files_info(name,type,coast) values(%s,%s,%s);'
		res_name = name[2:-2]
		cur.execute(sql,(res_name,type_file,coast))
		connection.commit()

def delete(connection,name,type_file):
		cur = connection.cursor()
		sql ='DELETE FROM files_info WHERE name = %s AND type = %s;'
		res_name = name[2:-2]
		cur.execute(sql,(res_name,type_file))
		connection.commit()

def rename(connection,old_name,new_name,type_file):
		cur = connection.cursor()
		sql ='UPDATE files_info set name = %s WHERE name = %s AND type = %s;'
		res_old_name = old_name[2:-2]
		res_new_name = new_name[2:-2]
		cur.execute(sql,(res_new_name,res_old_name,type_file))
		connection.commit()
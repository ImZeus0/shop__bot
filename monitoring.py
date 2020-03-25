import os
import sqlConnection
#[A-Z]+\-+[A-Z]+\-\d+.RU
key_dir = os.listdir('D:\\test monitoring dir\\keys')
sock_dir = os.listdir('D:\\test monitoring dir\\socks')
acc_dir = os.listdir('D:\\test monitoring dir\\accounts')


def find_new_file(ndir,buff_dir,type_file):
	coast = 0
	if type_file == 'key':
		coast = 5
	elif type_file == 'account':
		coast = 10
	elif type_file == 'socks':
		coast = 15
	con = sqlConnection.connect()
	set_ndir = set(ndir)
	set_buff_dir = set(buff_dir)
	res = set_buff_dir.difference(set_ndir)
	print(str(res))
	sqlConnection.insert(con,str(res),type_file,coast)
	con.close()
	print(str(res)+' <- added')

def find_delete_file(ndir,buff_dir,type_file):
	con = sqlConnection.connect()
	set_ndir = set(ndir)
	set_buff_dir = set(buff_dir)
	res = set_ndir.difference(set_buff_dir)
	sqlConnection.delete(con,str(res),type_file)
	con.close()
	print(str(res)+' <- delete')

def find_rename_file(ndir,buff_dir,type_file):
	con = sqlConnection.connect()
	set_ndir = set(ndir)
	set_buff_dir = set(buff_dir)
	old_name = set_ndir.difference(set_buff_dir)
	new_name = set_buff_dir.difference(set_ndir)
	sqlConnection.rename(con,str(old_name),str(new_name),type_file)
	con.close()
	print(str(old_name)+' -> rename -> '+str(new_name))

def chek(ndir,buff_dir,type_file):
	if (len(ndir)>len(buff_dir)):
		find_delete_file(ndir,buff_dir,type_file)
	if (len(ndir)<len(buff_dir)):
		find_new_file(ndir,buff_dir,type_file)
	if len(ndir)==len(buff_dir) and ndir!=buff_dir:
		find_rename_file(ndir,buff_dir,type_file)

while True :
	buff_k_dir = os.listdir('D:\\test monitoring dir\\keys')
	if key_dir != buff_k_dir:
		chek(key_dir,buff_k_dir,'key')
		print('keys')
		key_dir = buff_k_dir

	buff_s_dir = os.listdir('D:\\test monitoring dir\\socks')
	if sock_dir != buff_s_dir:
		chek(sock_dir,buff_s_dir,'socks')
		print('socks')
		sock_dir = buff_s_dir

	buff_a_dir = os.listdir('D:\\test monitoring dir\\accounts')
	if acc_dir != buff_a_dir:
		chek(acc_dir,buff_a_dir,'account')
		print('account')
		acc_dir = buff_a_dir


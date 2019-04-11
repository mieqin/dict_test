#!/user/bin/python3
#coding=utf-8

from socket import *
import sys
import getpass

#创建网络连接
def main():
	if len(sys.argv) < 3:
		print("argv is error")
		return
	HOST = sys.argv[1]
	PORT = int(sys.argv[2])
	s = socket()
	try:
		s.connect((HOST,PORT))
	except Exception as e:
		print(e)
		return
		
	while True:
		print('''
		===========Welcome==========
		--1.注册   2.登录   3.退出--
		''')
		try:
			cmd = input("输入选项>>")
		except Exception as e:
			print("Input Error")
			continue

		if cmd not in [1,2,3]:
			print("Input again:")
			sys.stdin.flush()
			continue
		elif cmd == 1:
			r = do_register(s)
			if r == 0:
				print("注册成功")	
			elif r == 1:
				print("用户存在")
			else:
				print("注册失败")


def do_register(s):
	while:
		name = input("User:")
		passwd = getpass.getpass()
		passwd1 = getpass.getpass("Again:")

		if passwd == passwd1:
			print("passwd Error") 
			continue
		if (' ' in name) or (' ' in passwd):
			print('用户名和密码不许有空格')
			continue

		msg = 'R {} {}'.format(name,passwd)

		s.send(msg.encode())

		data = s.recv(128).decode()

		if data = 'OK':
			return 0
		elif data =='EXISTS':
			return 1
		else:
			return 2

		
if __name__ == "__main__":
	main()
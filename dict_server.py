'''
name:TI-MI
date:2019-4-10
email:981203748@qq.com
modules:pymongo
This is a dict project fo AID
'''

from socket import *
import os
import time
import signal
import pymysql
import sys

#定义需要的全局变量
DICT_TEXT = './dict.txt'
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)

#流程控制
def main():
	#创建数据库连接
#	db = pymysql.connect('localhost','root','123456','dict')
	
	#创建套接字
	s = socket()
	s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	s.bind(ADDR)
	s.listen(5)
	
	#忽略子进程信号
	signal.signal(signal.SIGCHLD,signal.SIG_IGN)
	
	while True:
		try:
			c,addr = s.accept()
			print("Connect from",addr)
		except KeyboardInterrupt:
			s.close()
			sys.exit("服务器退出")
		except Exception as e:
			print(e)
			continue
			
		#创建子进程
		pid = os.fork()
		if pid ==0:
			s.close()
			print("子进程准备处理请求")
			do_child(c)
			sys.exit(0)
		else:
			c.close()
			continue

def do_child(c):
	try:
		get = c.recv(32).decode()
		if get == ('1' or '注册'):
			do_login(c)
		elif get == ('2' or '登录'):
			do_register()
		elif get == ('3' or '退出'):
			do_query()
		else:
			c.send("Input Error".encode())
	except Exception as e:
		print(e)


def do_login(c):
	c.send("Please login in my id".encode())

def do_register():
	pass

def do_query():
	pass

def do_hist():
	pass
	

if __name__ == '__main__':
	main()
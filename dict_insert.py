import pymysql
import re

db = pymysql.connect('localhost','root','123456','dict')

cursor = db.cursor()

f = open('dict.txt')

for line in f:
	if not line:
		continue
	else:
		l = re.split(r'\s+',line)
		word = l[0]
		interpret = ' '.join(l[1:])
		sql = "insert into words (word,interpret) values (%s,%s)"% (word,interpret)
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
f.close()
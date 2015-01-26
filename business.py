# -*- coding: utf-8 -*-

import mysql.connector

class dbMgr:
	def __init__(self):
		self.__conn = None
		self.__cursor = None
	
	def __enter__(self):
		self.__conn = mysql.connector.connect(user='root', password='',database='mysql',use_unicode=True)
		self.__cursor = self.__conn.cursor()
		return self.__cursor
	
	def __exit__(self, mytype, myvalue, tb):
		if self.__cursor:
			self.__cursor.close()
		if self.__conn:
			self.__conn.commit()
			self.__conn.close()


if __name__=='__main__':
	with dbMgr() as cursor:
		cursor.


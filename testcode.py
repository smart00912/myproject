# -*- coding: utf-8 -*-
import hashlib
import this
import web
import lxml
import time
import os
import urllib2, json
from lxml import etree
import xml


class WeixinInterface:
	def __init__(self):
		self.app_root = os.path.dirname(__file__)
		self.templates_root = os.path.join(self.app_root, 'templates')
		self.render = web.template.render(self.templates_root)
		
		
	def ato(self,s):
		print s
	'''
	def switch(self,ch):
		try:
			{'sean': lambda:self.ato("test!"),
			'status': lambda :self.ato("server fucked!"),
			'cpu': lambda :self.ato("everage 97% in last 5 mins"),
			'memory': lambda :self.ato("everage 30% in last 5 mins"),
			}[ch]()
		except KeyError:
			self.ato("Key not Found")
	
	'''
	def switch(self,str):
		res = ''
		if str == 'sean':
			res = 'goo guy'
		elif str == 'cpu':
			res = "everage 97% in last 5 mins"
		elif str == 'memory':
			res = "everage 30% in last 5 mins"
		elif str == 'status':
			res = "server fucked!"
		else :
			res = 'Unkow query string'
		return res
		

	def GET(self):
		# 获取输入参数
		data = web.input()
		signature = data.signature
		timestamp = data.timestamp
		nonce = data.nonce
		echostr = data.echostr
		#自己的token
		token = "seanyaotest"  #这里改写你在微信公众平台里输入的token
		#字典序排序
		list = [token, timestamp, nonce]
		list.sort()
		sha1 = hashlib.sha1()
		map(sha1.update, list)
		hashcode = sha1.hexdigest()
		#sha1加密算法

		#如果是来自微信的请求，则回复echostr
		if hashcode == signature:
			return echostr


	def POST(self):
		str_xml = web.data()
		xml = etree.fromstring(str_xml)
		content = xml.find("Content").text
		content = self.switch(content)
		if not len(content):
			content = "found nothing"
		#content = "found nothing"
		#content = "测试成功"
		msgType = xml.find("MsgType").text
		fromUser = xml.find("FromUserName").text
		toUser = xml.find("ToUserName").text
		createtime = int(time.time())
		return self.render.reply_text(fromUser, toUser, createtime, content)
	
	

    

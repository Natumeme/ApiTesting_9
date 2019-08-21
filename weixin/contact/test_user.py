#!usr/bin/env python
#-*- coding:utf-8 -*-
import json
import time

import requests
import logging
import pystache

from weixin.contact.token import Weixin


class TestUser:
	logging.basicConfig(level=logging.DEBUG)
	depart_id=1
	@classmethod
	def setup_class(cls):
		#todo: create
		pass

	def test_create(self):
		#创建成员
		uid="natume"+time.strftime("%H%M%S")
		data={
			"userid":uid,
			"name":uid,
			"department":[self.depart_id],
			"email":uid+"@testerhome.com"
		}

		r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
		              params={"access_token": Weixin.get_token()},
		              json=data).json()
		logging.debug(r)
		assert r["errcode"]==0

	def test_create_by_template(self):
		uid = "natume" + str(time.time())
		mobile=str(time.time()).replace(".","")[0:11]
		data=str(self.get_user({
			"name":"natume",
			"title":"校长",
			"email":"1@1.com",
			"mobile":mobile
		}))
		data=data.encode("UTF-8")
		r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
		                  params={"access_token": Weixin.get_token()},
		                  data=data,
		                  headers={"Content-Type":"application/json;charset=UTF-8"}).json()
		logging.debug(r)
		assert r["errcode"] == 0


	def test_list(self):
		#获取部门成员
		params={"access_token": Weixin.get_token(),
		        "department_id":1}
		r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
		             params=params).json()
		logging.debug(json.dumps(r,ensure_ascii=False,indent=2))
		assert r["errcode"] == 0

	def get_user(self,dict):
		template="".join(open("user_create.json",encoding='utf-8').readlines())
		#logging.debug(template)
		return pystache.render(template,dict)

	def test_get_user(self):
		logging.debug(self.get_user({"name":"natume","title":"校长","email":"1@1.com"}))

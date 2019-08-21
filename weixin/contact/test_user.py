#!usr/bin/env python
#-*- coding:utf-8 -*-
import json
from datetime import time

import requests
import logging

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


	def test_list(self):
		#获取部门成员
		params={"access_token": Weixin.get_token(),
		        "department_id":1}
		r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
		             params=params).json()
		logging.debug(json.dumps(r,ensure_ascii=False,indent=2))
		assert r["errcode"] == 0

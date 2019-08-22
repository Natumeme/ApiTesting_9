#!usr/bin/env python
#-*- coding:utf-8 -*-

import json
import time
import logging
import pystache
from weixin.contact.token import Weixin
from weixin.contact.user import User
from weixin.contact.utils import Utils


class TestUser:
	logging.basicConfig(level=logging.DEBUG)
	depart_id=278
	@classmethod
	def setup_class(cls):
		#todo: create
		cls.user=User()

	def test_create(self):
		#创建成员
		uid="natume"+Utils.udid()
		data={
			"userid":uid,
			"name":uid,
			"department":[self.depart_id],
			"email":uid+"@testerhome.com"
		}
		r=self.user.create(data)
		logging.debug(r)
		assert r["errcode"]==0

	def test_create_by_real(self):
		#使用mustache模板生成参数
		uid = "ruhi" + str(time.time())
		mobile=str(time.time()).replace(".","")[0:11]
		data=str(Utils.parse("user_create.json",{
			"name":uid,
			"title":"校长",
			"email":mobile+"@qq.com",
			"mobile":mobile
		}))
		data=data.encode("UTF-8")
		r = self.user.create(data)
		logging.debug(r)
		assert r["errcode"] == 0


	def test_list(self):
		#获取部门成员
		# r=self.user.list()
		# logging.debug(json.dumps(r,ensure_ascii=False,indent=2))
		#assert r["errcode"] == 0
		r=self.user.list(department_id=2)
		logging.debug(json.dumps(r, ensure_ascii=False, indent=2))

	def test_delete_user(self):
		#删除成员
		r=self.user.delete()



	def test_get_user(self):
		logging.debug(Utils.parse("user_create.json",{"name":"natume","title":"校长","email":"1@1.com"}))

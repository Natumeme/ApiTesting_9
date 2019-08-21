#!usr/bin/env python
#-*- coding:utf-8 -*-
import datetime
import json
import requests
from weixin.contact.token import Weixin
import logging
import pytest


class TestDepartment:
	logging.basicConfig(level=logging.DEBUG)

	@classmethod
	def setup_class(cls):
		print("setup class")
		Weixin.get_token()
		print(Weixin._token)

	def setup(self):
		print("setup")

	def test_create_depth(self):
		#创建部门
		parentid=1
		for i in range(5):
			data={
				"name": "第九期_natume_"+str(parentid)+str(datetime.datetime.now().timestamp()),
				"parentid": parentid
			}
			r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
			                  params={"access_token":Weixin.get_token()},
			                  json=data
			                  ).json()
			logging.debug(r)
			parentid=r["id"]
			assert r["errorcode"]==0

	@pytest.mark.parametrize("name",[
		"广州研发中心"
	])
	def test_create_order(self):
		data = {
			"name": name,
			"parentid": 1,
			"order": 1
		}
		r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
		                  params={"access_token": Weixin.get_token()},
		                  json=data
		                  ).json()

		#解密
		logging.debug(r)
		assert r["errorcode"]==0

	def test_get(self):
		#获取部门
		r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
		             params={"access_token":Weixin.get_token()}
		             ).json()
		logging.debug(json.dumps(r,indent=2,ensure_ascii=False))
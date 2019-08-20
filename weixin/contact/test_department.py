#!usr/bin/env python
#-*- coding:utf-8 -*-

import json
import requests
from weixin.contact.token import Weixin
import logging
import yaml


class TestDepartment:
	logging.basicConfig(level=logging.DEBUG)

	@classmethod
	def setup_class(cls):
		print("setup class")
		Weixin.get_token()
		print(Weixin._token)

	def setup(self):
		print("setup")

	def test_create_name(self):
		data={
			"name": "第十期_natume",
			"parentid": 1
		}
		r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
		                  params={"access_token":Weixin.get_token()},
		                  json=data
		                  ).json()
		logging.debug(r)

	def test_create(self):
		data = {
			"name": "广州研发中心",
			"parentid": 1,
			"order": 1
		}
		r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
		                  params={"access_token": Weixin.get_token()},
		                  json=data
		                  ).json()
		logging.debug(r)

	def test_get(self):
		r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
		             params={"access_token":Weixin.get_token()}
		             ).json()
		logging.debug(json.dumps(r,indent=2,ensure_ascii=False))
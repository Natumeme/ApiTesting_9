#!usr/bin/env python
#-*- coding:utf-8 -*-

import requests

from weixin.contact.token import Weixin
import logging


class TestDepartment(object):
	logging.basicConfig(level=logging.DEBUG)
	@classmethod
	def setup_class(cls):
		print("setup class")
		Weixin.get_token()
		print(Weixin._token)

	def setup(self):
		print("setup")

	def test_create(self):
		data={
			"name": "广州研发中心",
			"parentid": 1,
			"order": 1,
			"id": 2
		}
		r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
					params={"access_token":Weixin.get_token()},
					json=data
		            ).json()
		logging.debug(r)
#!usr/bin/env python
#-*- coding:utf-8 -*-

import requests

from weixin.contact.token import Weixin


class Department:
	def create(self,data):
		return requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
		                     params={"access_token": Weixin.get_token()},
		                     json=data
		                     ).json()

	def get_department(self):
		return requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
		                 params={"access_token": Weixin.get_token()}
		                 ).json()

	def update_department(self,data):
		return requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/update",
		                 params={"access_token": Weixin.get_token()},
		                 json=data
		                 ).json()

	def delete_department(self):
		return requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/delete",
		                 params={"access_token": Weixin.get_token(),"id":281}
		                 ).json()

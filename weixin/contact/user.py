#!usr/bin/env python
#-*- coding:utf-8 -*-

import requests
from weixin.contact.token import Weixin


class User:
	def create(self,dict=None,data=None):
		return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
		                  params={"access_token": Weixin.get_token()},
		                  json=dict,
		                  data=data
		                ).json()

	def list(self,department_id=1,fetch_child=0,**kwargs):
		params = {"access_token": Weixin.get_token(),
		          "department_id": department_id,
		          "fetch_child":fetch_child
		          }
		return requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
		                 params=params
		                ).json()
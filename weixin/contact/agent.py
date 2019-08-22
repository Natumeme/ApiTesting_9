#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests

from weixin.contact.token import Weixin


class Agent:
	def create_menu(self,data):
		return requests.post("https://qyapi.weixin.qq.com/cgi-bin/menu/create",
		                     params={
			                     "access_token": Weixin.get_token(),
			                     "agentid": 1000005
		                     },
		                     json=data
		                     )

	def get_menu(self):
		return requests.get("https://qyapi.weixin.qq.com/cgi-bin/menu/get",
		                    params={
			                    "access_token": Weixin.get_token(),
			                    "agentid":1000005
		                    }
		                    ).json()
#!usr/bin/env python
#-*- coding:utf-8 -*-
import datetime
import json
import requests
from weixin.contact.token import Weixin
import logging
import pytest

from weixin.contact.utils import Utils


class TestDepartment:
	logging.basicConfig(level=logging.DEBUG)
	def test_create_depth(self,token):
		#创建部门
		parentid=1
		for i in range(5):
			data={
				"name": "第九期_natume_"+str(parentid)+str(time.time()),
				"parentid": parentid
			}
			r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
			                  params={"access_token":token},
			                  json=data
			                  ).json()
			logging.debug(r)
			parentid=r["id"]
			assert r["errorcode"]==0

	@pytest.mark.parametrize("name",[
		"广州研发中心"
	])
	def test_create_order(self,name,token):
		data = {
			"name": name+Utils.udid(),
			"parentid": 1,
			"order": 1
		}
		r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
		                  params={"access_token": token},
		                  json=data
		                  ).json()

		#解密
		logging.debug(r)
		assert r["errorcode"]==0

	def test_get(self,token):
		#获取部门
		r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
		             params={"access_token":token}
		             ).json()
		logging.debug(json.dumps(r,indent=2,ensure_ascii=False))
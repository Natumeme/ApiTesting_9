#!usr/bin/env python
#-*- coding:utf-8 -*-

import json
import requests
import logging
import pytest
from weixin.contact.utils import Utils
from weixin.contact.department import Department


class TestDepartment:
	logging.basicConfig(level=logging.DEBUG)

	@classmethod
	def setup_class(cls):
		cls.department = Department()

	def test_create_depth(self,token):
		#创建部门
		parentid=278
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
		"妖精尾巴"
	])
	def test_create_order(self,name):
		data = {
			"name": name+Utils.udid(),
			"parentid": 1,
			"order": 1
		}
		r=self.department.create(data)

		#解密
		logging.debug(json.dumps(r,indent=2,ensure_ascii=False))
		assert r["errcode"]==0

	def test_get(self):
		#获取部门
		r=self.department.get_department()
		logging.debug(json.dumps(r,indent=2,ensure_ascii=False))
		assert r["errcode"] == 0

	def test_update(self):
		#更新部门
		data={
		   "id": 281,
		   "name": "妖精尾巴update",
		   "parentid": 1,
		   "order": 1
		}
		r=self.department.update_department(data)
		logging.debug(json.dumps(r,indent=2,ensure_ascii=False))
		assert r["errcode"] == 0

	def test_delete(self):
		#删除部门
		r=self.department.delete_department()
		logging.debug(json.dumps(r, indent=2, ensure_ascii=False))
		assert r["errcode"] == 0
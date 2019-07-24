#!usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import logging
import pytest
import json

class TestRequests(object):
	logging.basicConfig(level=logging.INFO)
	url="https://testerhome.com/api/v3/topics.json?limit=2"
	def test_get(self):
		r=requests.get(self.url)
		logging.info(r)
		logging.info(r.text)
		logging.info(json.dumps(r.json(),indent=2))

	def test_post(self):
		r=requests.post(self.url,
		                json={"a":1,"b":"string corntent"},
		                # headers={"a":"1","b":"b2"},
		                proxies={"https":"127.0.0.1:8888","http":"127.0.0.1:8888"},
		                verify=False
		                )
		logging.info(r.url)
		logging.info(r.text)
		logging.info(json.dumps(r.json(),indent=2))

	def test_cookies(self):
		r=requests.get("http://47.95.238.18:8090/cookies",cookies={"a":"1","b":"string"})
		logging.info(r.text)

	def test_xuqqiu_quote(self):
		pass




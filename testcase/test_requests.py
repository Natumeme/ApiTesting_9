#!usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import logging
import pytest
import json
import jsonpath

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
		                json={"a":"1","b":"string corntent"},
		                # headers={"a":"1","b":"b2"},
		                # proxies={},
		                verify=False
		                )
		# logging.info(r.url)
		logging.info(r.text)
		logging.info(json.dumps(r.json(),indent=2))

	def test_cookies(self):
		url = "https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?"
		r=requests.get(url,
		               params={"category":"2"},
		               cookies={"a":"1","b":"string"})
		logging.info(r.text)

	def test_xueqiu_quote(self):
		url = "https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?"
		r = requests.get(url,
		                 params={"category": "1"},
		                 headers={'User-Agent': 'Xueqiu Android 11.19'},
		                 cookies={"u": "6465710483", "xq_a_token": "f0c5a085040d507702cdeb99d51243451fc63d35"}
		                 )
		logging.info(json.dumps(r.json(),ensure_ascii=False,indent=2))
		assert r.json()["data"]["category"] == 1
		assert r.json()["data"]["stocks"][0]["name"] == "招商银行"
		assert jsonpath.jsonpath(r.json(),"$.data.stocks[?(@.symbol == 'SH600036')].name")[0] == "招商银行"
		# assert_that(jsonpath.jsonpath(r.json(), "$.data.stocks[?(@.symbol == 'F006947')].name")[0],equal_to("华宝中短债债券B"), "比较上市代码与名字")




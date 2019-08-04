#!usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import logging
import pytest
import json
import jsonpath
from hamcrest import *
from jsonschema import validate

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
		#logging.info(json.dumps(r.json(),ensure_ascii=False,indent=2))
		assert r.json()["data"]["category"] == 1
		assert r.json()["data"]["stocks"][0]["name"] == "招商银行"
		assert jsonpath.jsonpath(r.json(),"$.data.stocks[?(@.symbol == 'SH600036')].name")[0] == "招商银行"
		#assert_that(jsonpath.jsonpath(r.json(), "$.data.stocks[?(@.symbol == 'F006947')].name")[0],equal_to("招商银行"), "比较上市代码与名字")


	def test_xueqiu_list_schema(self):
		#使用schema校验基本字段
		#自动对比新老版本
		url = "https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?"
		r = requests.get(url,
		                 params={"category": "1"},
		                 headers={'User-Agent': 'Xueqiu Android 11.19'},
		                 cookies={"u": "6465710483", "xq_a_token": "f0c5a085040d507702cdeb99d51243451fc63d35"}
		                 )
		logging.info(json.dumps(r.json(),ensure_ascii=False,indent=2))
		schema=json.load(open("list_schema.json"))
		validate(instance=r.json(),schema=schema)


	def test_hamcrest(self):
		assert_that(0.1*0.1,close_to(0.01,0.0001))
		assert_that(["a","b","c"],has_item("a"))
		#只要有一个条件匹配即可
		assert_that(["a","b","c"],any_of(has_items("c","d"),has_items("c","a")))

	def test_homework(self):
		#课间作业
		url = "https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?"
		r = requests.get(url,
		                 params={"category": "1"},
		                 headers={'User-Agent': 'Xueqiu Android 11.19'},
		                 cookies={"u": "6465710483", "xq_a_token": "f0c5a085040d507702cdeb99d51243451fc63d35"}
		                 )
		assert_that(jsonpath.jsonpath(r.json(),"$.data.stocks[*].name"),any_of(has_item('招商银行'),has_item('阿里巴巴')))


	def test_schema(self):
		schema = {
        "type" : "object",
        "properties" : {
			 "price" : {"type" : "number"},
			"name" : {"type" : "string"},
            },
        }
		validate(instance={"name": "Eggs", "price": "34.99"}, schema=schema)





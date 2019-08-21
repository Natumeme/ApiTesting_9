#!usr/bin/env python
#-*- coding:utf-8 -*-
import requests
import yaml
import logging


class Weixin:
	logging.basicConfig(level=logging.DEBUG)
	_token= ""
	@classmethod
	def get_token(cls):
		if len(cls._token)==0:
			#完成初始化
			cls._token=cls.get_token_new()
		return cls._token

	@classmethod
	def get_token_new(cls):
		#完成初始化
		conf=yaml.safe_load(open("weixin.yaml"))
		logging.debug(conf["env"])
		r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
		             params={"corpid":conf["env"]["corpid"],
		                     "corpsecret":conf["env"]["secret"]}
		             ).json()
		return r["access_token"]

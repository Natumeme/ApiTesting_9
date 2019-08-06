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
		#完成初始化
		if len(cls._token)==0:
			conf=yaml.safe_load(open("weixin.yaml"))
			logging.debug(conf["env"])
			r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
			             params={"corpid":conf["env"]["corp_id"],
			                     "corpsecret":conf["env"]["secret"]}
			             ).json()
			cls._token=r["access_token"]
			return cls._token
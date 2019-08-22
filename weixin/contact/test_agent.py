#!/usr/bin/env python
#-*-coding:utf-8-*-
import json

from weixin.contact.agent import Agent
import logging


class TestAgent:
	logging.basicConfig(level=logging.DEBUG)
	@classmethod
	def setup_class(cls):
		cls.agent = Agent()

	# def test_create_menu(self):
	# 	#创建菜单
	# 	pass

	def test_get_menu(self):
		#获取菜单
		r=self.agent.get_menu()
		logging.debug(json.dumps(r,indent=2,ensure_ascii=False))

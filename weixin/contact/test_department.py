#!usr/bin/env python
#-*- coding:utf-8 -*-

class TestDepartment(object):
	@classmethod
	def setup_class(cls):
		print("setup class")
		Weixin.get_token()
		print(Weixin.token)

	def setup(self):
		print("setup")

	def test_create(self):
		pass
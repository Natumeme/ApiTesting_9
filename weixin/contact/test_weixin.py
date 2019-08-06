#!usr/bin/env python
#-*- coding:utf-8 -*-

from weixin.contact.token import Weixin
from unittest import TestCase

class TestWeixin(TestCase):
	def test_get_token(self):
		print(Weixin.get_token())
		assert Weixin.get_token() != ""
#!/usr/bin/env python
#-*-coding:utf-8-*-
import time

import pystache


class Utils:
	@classmethod
	def parse(cls, template_path,dict):
		template = "".join(open(template_path, encoding='utf-8').readlines())
		# logging.debug(template)
		return pystache.render(template, dict)

	@classmethod
	def udid(cls):
		return str(time.time()).replace(".","")[0:11]



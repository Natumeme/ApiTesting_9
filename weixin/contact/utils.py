#!/usr/bin/env python
#-*-coding:utf-8-*-
import pystache


class Utils:
	def parse(self, template_path,dict):
		template = "".join(open(template_path, encoding='utf-8').readlines())
		# logging.debug(template)
		return pystache.render(template, dict)
#!usr/bin/env python
#-*- coding:utf-8 -*-

import pytest

from weixin.contact.token import Weixin


@pytest.fixture(scope="session")
def token():
	return Weixin.get_token_new()
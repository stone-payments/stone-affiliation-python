# -*- coding: utf-8 -*-

"""
Módulo encapsula biblioteca de http request
"""
import requests


def post(url, data=None, json=None, **kwargs):
    kwargs["data"] = data
    kwargs["json"] = json
    return _request("post", url, **kwargs)


def _request(method, url, **kwargs):
    method = getattr(requests, method)
    return method(url, **kwargs)

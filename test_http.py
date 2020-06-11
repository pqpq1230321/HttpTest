#!/usr/bin/env python
#coding=utf-8

import requests


def test_http_get():
    r = requests.get("http://httpbin.ceshiren.com/get",params={"a":1,"b":2})
    print(r.status_code)
    print(r.json())
    print(r.text)

    assert r.status_code == 200
    assert r.json()["args"]["a"] == "1"

def test_http_post():
    r = requests.post("http://httpbin.ceshiren.com/post",data={"aas":"sdfsdf"})

    print(r.json())
    assert r.status_code == 200
    assert r.json()["form"]["aas"] == "sdfsdf"

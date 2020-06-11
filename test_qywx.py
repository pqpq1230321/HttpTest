#!/usr/bin/env python
# coding=utf-8
import json
import token
import requests


from qywx_fz import Qywx


class Test_Qywx:

    def setup_class(self):
        self.qywx = Qywx()
        self.token = self.qywx.token_get()

        for tag_name in ["0611","0612"]:
            tag_id = self.qywx.tag_find(tag_name)
            if tag_id is not None:
                r = self.qywx.tag_delete(tag_id)
                assert r.json()["errcode"] == 0

    def setup(self):
        pass

    def test_tags_get(self):
        r = self.qywx.get_tag_list()
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

    def test_tags_add(self):
        r = self.qywx.tag_add("0611","0611")
        assert r.json()["errcode"] == 0

    def test_tags_delete(self):

        self.qywx.tag_add("0611","0612")
        tag_id = self.qywx.tag_find("0612")
        r = self.qywx.tag_delete(tag_id)
        assert r.json()["errcode"] == 0

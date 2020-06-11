#!/usr/bin/env python
#coding=utf-8
import requests


class Qywx:

    def __init__(self):
        self.token = None

    def token_get(self):
        if self.token is None:
            r = requests.get(
                "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                params={"corpid": "ww0ff182a4785e9434", "corpsecret": "PxOXS48mqH4WUS3CNT8MJggb4UyXZ0qIdvoTBcjDixo"}
            )
            self.token = r.json()["access_token"]
        return self.token

    def get_tag_list(self):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={"access_token": self.token_get()},
            json={"tag_id": []}
        )
        return r

    def tag_add(self,group_name,tag_name):
        return requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            params={"access_token":self.token_get()},
            json={"group_name":group_name,
                  "tag":[{"name":tag_name}]
                  }
        )

    def tag_find(self,name):
        r = self.get_tag_list()
        print(r.text)

        tags = [tag for group in r.json()["tag_group"] for tag in group["tag"] if tag["name"] == name]
        if len(tags) == 0:
            return None
        else:
            return tags[0]["id"]

    def tag_delete(self,tag_id):
        return requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            params={"access_token":self.token_get()},
            json={"tag_id":[tag_id]}
        )

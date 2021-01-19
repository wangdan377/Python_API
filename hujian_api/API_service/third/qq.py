import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


#游客登录
def visitor_login():
    sessionX = requests.session()
    post_req = Post.Post()
    ass = Assert.Assertions()

    url = 'http://47.99.180.185:3000/v1/login/oauth'
    authData_pri = {
        "access_token": "6A6735C843D00D68189D847E02A55FC2",
        "openid": "F669262F01C93E55134167976DADA11E",
        "nickname": "张三",
        "sex": 1,
        "avatar": "https://avatars2.githubusercontent.com/u/11366654?s=60&v=4"
    }
    authData = json.dumps(authData_pri)
    print(type(authData))

    params = {'platform': 'qq', 'authData': authData}

    res = post_req.post_model_b(sessionX, url, params)
    print(res)

    resCode = res['code']
    resText = res['text']

    assert ass.assert_code(resCode, 200)
    assert ass.assert_in_text(resText, '成功')
    Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    a = visitor_login()
    print(a)


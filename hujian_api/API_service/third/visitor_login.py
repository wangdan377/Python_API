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

    url = 'http://47.99.180.185:2999/v1/login_by_visitor'
    params = {'sid':'hujianBBB@zhiyun-tech.com'}

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


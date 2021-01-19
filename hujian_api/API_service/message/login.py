import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


#邮箱注册
def off_reg():
    sessionX = requests.session()
    post_req = Post.Post()
    ass = Assert.Assertions()

    url = 'http://172.16.2.101:3000/v1/register'
    params = {'username':'hujiannnn@zhiyun-tech.com', 'password':'123456789'}

    res = post_req.post_model_b(sessionX, url, params)
    print(res)

    resCode = res['code']
    resText = res['text']

    assert ass.assert_code(resCode, 200)
    assert ass.assert_in_text(resText, '成功')
    Consts.RESULT_LIST.append('True')


#邮箱登录
def off_login():
    sessionX = requests.session()
    post_req = Post.Post()
    ass = Assert.Assertions()
    null = None

    url = 'http://172.16.2.101:3000/v1/login'
    params = {'username':'hujianQ1@zhiyun-tech.com', 'password':'123456789'}

    res = post_req.post_model_b(sessionX, url, params)
    print(res)

    resCode = res['code']
    resText = res['text']
    resToken = eval(resText)['token']

    assert ass.assert_code(resCode, 200)
    assert ass.assert_in_text(resText, '成功')
    Consts.RESULT_LIST.append('True')

    return resToken


if __name__ == "__main__":
    #a = off_reg()
    aaa = off_login()
    print(aaa)


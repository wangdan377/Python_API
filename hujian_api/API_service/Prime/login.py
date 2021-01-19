import pytest
import allure
import requests
import json
import time

from API_service.Common import Post
from API_service.Common import Get
from API_service.Common import Assert
from API_service.Common import Consts


def off_login():
    sessionX = requests.session()
    post_req = Post.Post()
    ass = Assert.Assertions()
    null = None

    url = 'https://api-test.zhiyun-tech.com/v1/login'
    #params = {'username':'huj@zhiyun-tech.com', 'password':'123456'}
    #params = {'username': '+8615220273140', 'password': '123456789'}
    params = {'username': 'hujiantest112@zs.com', 'password': '123456789'}
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
    test = off_login()
    print(test)


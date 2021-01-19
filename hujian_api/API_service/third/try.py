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

    url = 'http://api.share.mob.com/snsconf'

    params = {'appkey': '2976dcae83fdb', 'device': '375df518969e127f94d76a4a1ae5f06f2ac5782c'}

    res = post_req.post_model_b(sessionX, url, params)
    print(res)

    resCode = res['code']
    resText = res['text']

    assert ass.assert_code(resCode, 200)
    assert ass.assert_in_text(resText, '200')
    Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    visitor_login()


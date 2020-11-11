import requests
import json
from Common import Get
from Common import Post
from Common import Log
from Conf import Config

class testFile:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.Log()

    def addUser(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
        post_login_url = 'http://172.16.2.101:3000/v1/user/add'
        home_url = 'https://cms.zhiyun-tech.com/login'
        params = {'username': '13418483933@139.com', 'password': '12345678','vcode': '','role': 'super'}

        sessionX = requests.session()
        postA = Post.Post()
        getA = Get.Get()
        res = postA.post_model_b(post_login_url,sessionX,params)

        print(res.status_code)

if __name__ == '__main__':
    test = testFile()
    test.addUser()
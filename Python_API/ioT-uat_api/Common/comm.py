'''
@Author: xiaomin
@Date: 2020-04-26 15:42:52
@LastEditTime: 2020-04-30 15:25:12
@LastEditors: xiaomin
@Description: 
@FilePath: \ioT-uat\Common\comm.py
'''
import os
import sys
sys.path.append("..")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
import requests
import json

from Params.params import Login
from Common.Requestsfun import requestMethod

class loginToken(unittest.TestCase):
    # token=[]

    # def __init__(self):
    #     self.setUpClass()
    #     self.tearDownClass()
        

    @classmethod
    def setUpClass(cls):
        cls.data=Login()
        cls.request=requestMethod()
        
        urls=cls.data.url
        headers=cls.data.header
        paramss=cls.data.data
        
 
        response=cls.request.get_post(urls[0],headers[0],paramss[0])
        res=json.loads(response.text)
        loginToken.token=res['access_token']
        return loginToken.token

    @classmethod
    def tearDownClass(cls):
        pass



    
'''
@Author: xiaomin
@Date: 2020-05-07 09:46:06
@LastEditTime: 2020-05-07 18:21:01
@LastEditors: xiaomin
@Description: 封装调用测试数据的方法
@FilePath: \ioT-uat\Common\casefunction.py
'''
import os
import sys
sys.path.append("..")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import requests
import json


class CaseFunction():
    def get_request(self,request,url,headers,para,definedpara=None):
        if definedpara is None:
            response=request.get_get(url,headers,para)
            # res_info=json.loads(response.text)
            return response
        else:
            for k,v in definedpara.items():
                para[k]=v
            response=request.get_get(url,headers,para)
            # res_info=json.loads(response.text)
            return response

    def post_request(self,request,url,headers,para,definedpara=None):
        if definedpara is None:
            paras=json.dumps(para,separators=(',',':'))
            print(paras)
            response=request.get_post(url,headers,paras)        
            return response
        else:
            for k,v in definedpara.items():
                para[k]=v
            paras=json.dumps(para,separators=(',',':'))
            print(paras)
            response=request.get_post(url,headers,paras)        
            return response

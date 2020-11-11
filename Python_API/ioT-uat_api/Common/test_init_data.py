'''
@Author: xiaomin
@Date: 2020-05-06 15:26:01
@LastEditTime: 2020-05-11 15:21:40
@LastEditors: xiaomin
@Description: 测试数据初始化
@FilePath: \ioT-uat\Common\test_init_data.py
'''
import os
import sys
sys.path.append("..")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import unittest
import requests
import json
import time

from Params.params import init_Data
from Common.Requestsfun import requestMethod
from Common.comm import loginToken
from Common.config import Config

def get_request(request,url,headers,para,productname=None):
    if productname is None:
        response=request.get_get(url,headers,para)
        res_info=json.loads(response.text)
        return res_info
    else:
        para.update(productname)
        response=request.get_get(url,headers,para)
        res_info=json.loads(response.text)
        return res_info

def post_request(request,url,headers,para,productkey):
    para.update(productKey=productkey)
    paras=json.dumps(para,separators=(',',':'))
    response=request.get_post(url,headers,paras)

class initData(loginToken):
    def initdata(self,productname):

        #获取init.yaml数据
        data=init_Data()
        request=requestMethod()
        urls=data.url
        headers=data.header
        para=data.data

        '''给所有url补充域名'''
        url=[None]*len(urls)
        for n in range(0,len(urls)):
            url[n]=Config.host+urls[n]   

        '''给所有header添加token'''
        for n in range(0,len(headers)):
            headers[n].update(Authorization='bearer '+loginToken().token)
        
        getDevice=get_request(request,url[0],headers[0],para[0])#查询设备
        if len(getDevice['content']) != 0:#设备存在
            for i in range(0,len(getDevice['content'])):
                productkey=getDevice['content'][i]['productKey']
                post_request(request,url[1],headers[1],para[1],productkey)#解绑设备
                post_request(request,url[2],headers[2],para[2],productkey)#删除设备
                post_request(request,url[4],headers[4],para[4],productkey)#撤销产品
                time.sleep(2)
                post_request(request,url[5],headers[5],para[5],productkey)#删除产品
                print('数据初始化完成')               
        else:
            getproduct=get_request(request,url[3],headers[3],para[3],productname)#设备不存在，根据产品名称查询产品
            if len(getproduct['content'])!=0:
                productkey=getproduct['content'][0]['productKey']
                post_request(request,url[4],headers[4],para[4],productkey)#撤销产品
                time.sleep(2)
                post_request(request,url[5],headers[5],para[5],productkey)#删除产品
                print('数据初始化完成')
            else:
                print('不需初始化数据')

if __name__ == '__main__':
    unittest.main(verbosity=2)
    # init=initData()
    # init.test_initdata('apitest_auto16')
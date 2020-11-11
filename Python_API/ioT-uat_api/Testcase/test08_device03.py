'''
@Author: xiaomin
@Date: 2020-04-27 11:37:04
@LastEditTime: 2020-05-11 10:32:42
@LastEditors: xiaomin
@Description: 设备的新增标签流程
@FilePath: \ioT-uat\Testcase\test08_device03.py
'''

import os
import sys
sys.path.append("..")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import unittest
import requests
import json
import ddt

from Params.params import DeviceTest03
from Common.test_init_data import initData
from Common.casefunction import CaseFunction
from Common.Requestsfun import requestMethod
from Common.comm import loginToken
from Common.config import Config


@ddt.ddt
class DeviceTest_03(loginToken):
    '''
    创建产品-创建设备-增量更新设备标签-全量更新设备标签-查询标签
    '''
    @ddt.data({'title':'直连产品','dataFormat':'1','networkType':'WIFI','productName':'apitest_auto22','productNodeType':'0','sub':'false'},
              {'title':'网关子设备产品','dataFormat':'0','networkType':'WIFI','productName':'apitest_auto23','productNodeType':'0','sub':'true'},
              {'title':'边缘网关产品','dataFormat':'1','networkType':'WIFI','productName':'apitest_auto24','productNodeType':'2','sub':'false'})
    @ddt.unpack
    def test_device_03(self,dataFormat,networkType,productName,productNodeType,sub,title):

        # '''数据初始化'''
        a=initData()
        a.initdata({'productName':productName})

        # 变量用来控制调取接口索引
        i=0

        '''获取test_device3.yaml中的数据'''
        data=DeviceTest03()
        request=requestMethod()
        urls=data.url
        headers=data.header
        para=data.data
        expcode=data.code

        '''给所有url补充域名'''
        url=[None]*len(urls)
        for n in range(0,len(urls)):
            url[n]=Config.host+urls[n]

        '''给所有接口添加token'''
        for n in range(0,len(headers)):
            headers[n].update(Authorization='bearer '+loginToken().token)
            

        '''实例化调用测试数据的类'''
        case_function=CaseFunction()  

        '''创建产品'''
        print('\n'+url[i])
        print('------创建产品入参------')
        createproduct=case_function.post_request(request,url[i],headers[i],para[i],{'dataFormat':dataFormat,'networkType':networkType,'productNodeType':productNodeType,'productName':productName,'sub':sub})
        curcode=createproduct.status_code
        print('------创建产品返回------')
        print('status:%s'%str(curcode))
        print(createproduct.text)
        self.assertEqual(expcode[i],curcode)
        createproduct=json.loads(createproduct.text)
        productkeys=createproduct['productKey']
        print('获取产品Key：'+productkeys)
        i=i+1

        '''创建设备'''
        print('\n'+url[i])
        print('------创建设备入参------')
        createdevice=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=createdevice.status_code
        print('------创建设备返回------')
        print('status:%s'%str(curcode))
        print(createdevice.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''增量更新设备标签'''
        print('\n'+url[i])
        print('------增量更新设备标签入参------')
        devicetag=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=devicetag.status_code
        print('------增量更新设备标签返回------')
        print('status:%s'%str(curcode))
        print(devicetag.text)
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''全量更新设备标签'''
        print('\n'+url[i])
        print('------全量更新设备标签入参------')
        devicetags=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=devicetags.status_code
        print('------全量更新设备标签返回------')
        print('status:%s'%str(curcode))
        print(devicetags.text)
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''查询设备标签'''
        print('\n'+url[i])
        getdevicetag=case_function.get_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=getdevicetag.status_code
        print('------查询设备标签返回------')   
        print('status:%s'%str(curcode))
        print(getdevicetag.text)       
        self.assertIn(expcode[i][0],getdevicetag.text)
        self.assertIn(expcode[i][1],getdevicetag.text)
        i=i+1

        '''数据清理'''
        a.initdata({'productName':productName})       


if __name__ == '__main__':
    unittest.main(verbosity=2)




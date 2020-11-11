'''
@Author: xiaomin
@Date: 2020-04-27 11:37:04
@LastEditTime: 2020-05-11 15:20:02
@LastEditors: xiaomin
@Description: 设备的绑定用户流程
@FilePath: \ioT-uat\Testcase\test07_device02.py
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
import time

from Params.params import DeviceTest02
from Common.test_init_data import initData
from Common.casefunction import CaseFunction
from Common.Requestsfun import requestMethod
from Common.comm import loginToken
from Common.config import Config


@ddt.ddt
class DeviceTest_02(loginToken):
    '''
    创建产品-创建设备-登录用户-绑定用户-删除设备失败-解绑用户-删除设备成功-查询设备失败-删除产品
    '''
    @ddt.data({'title':'直连产品','dataFormat':'1','networkType':'WIFI','productName':'apitest_auto19','productNodeType':'0','sub':'false'},
              {'title':'网关子设备产品','dataFormat':'0','networkType':'WIFI','productName':'apitest_auto20','productNodeType':'0','sub':'true'},
              {'title':'边缘网关产品','dataFormat':'1','networkType':'WIFI','productName':'apitest_auto21','productNodeType':'2','sub':'false'})
    @ddt.unpack
    def test_device_02(self,dataFormat,networkType,productName,productNodeType,sub,title):

        # '''数据初始化'''
        a=initData()
        a.initdata({'productName':productName})

        # 变量用来控制调取接口索引
        i=0

        '''获取test_device2.yaml中的数据'''
        data=DeviceTest02()
        request=requestMethod()
        urls=data.url
        headers=data.header
        para=data.data
        expcode=data.code

        '''给所有url补充域名'''
        url=[None]*len(urls)
        for n in range(0,len(urls)):
            if 'oauth/login' not in urls[n]:
                url[n]=Config.host+urls[n]
            else:
                url[n]=urls[n]

        '''给没有token的所有接口添加token'''
        for n in range(0,len(headers)):
            if 'Authorization' not in headers[n]:
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
        deviceinfo=json.loads(createdevice.text)
        devicesecret=deviceinfo['deviceSecret']
        i=i+1  

        '''登录用户'''
        print('\n'+url[i])
        print('------登录用户入参------')
        print(para[i])
        response=request.get_post(url[i],headers[i],para[i])
        res_usrtoken=json.loads(response.text)
        curcode=response.status_code
        print('------登录用户返回------')
        print('status:%s'%str(curcode))
        print(str(response.text))
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''绑定用户'''
        headers[i]['Authorization']=res_usrtoken['token_type']+' '+res_usrtoken['access_token']
        print('\n'+url[i])
        print('------绑定用户入参------')
        binduser=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys,'deviceSecret':devicesecret})
        curcode=binduser.status_code
        print('------绑定用户返回------')
        print('status:%s'%str(curcode))
        print(str(binduser.text))
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''删除设备失败'''
        print('\n'+url[i])
        print('------删除设备入参------')
        deletedevice=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=deletedevice.status_code
        print('------删除设备返回------')
        print('status:%s'%str(curcode))
        print(deletedevice.text)
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''解绑设备'''
        print('\n'+url[i])
        print('------解绑设备入参------')
        unbinddevice=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=unbinddevice.status_code
        print('------解绑设备返回------')
        print('status:%s'%str(curcode))
        print(unbinddevice.text)
        self.assertEqual(expcode[i],curcode)
        i=i+1
        
        '''删除设备成功'''
        print('\n'+url[i])
        print('------删除设备入参------')
        deletedevice=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=deletedevice.status_code
        print('------删除设备返回------')
        print('status:%s'%str(curcode))
        print(deletedevice.text)
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''查询设备失败'''
        print('\n'+url[i])
        getdevice=case_function.get_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=getdevice.status_code
        print('------查询设备返回------')   
        print('status:%s'%str(curcode))
        print(getdevice.text)
        self.assertEqual(expcode[i],curcode)
        i=i+1

        time.sleep(2)
        
        '''删除产品'''
        print('\n'+url[i])
        print('------删除产品入参------')
        deleteproduct=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=deleteproduct.status_code
        print('------删除产品返回------')
        print('status:%s'%str(curcode))
        print(deleteproduct.text)
        self.assertEqual(expcode[i],curcode)


if __name__ == '__main__':
    unittest.main(verbosity=2)




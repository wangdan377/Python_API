'''
@Author: xiaomin
@Date: 2020-04-29 14:41:47
@LastEditTime: 2020-05-11 15:28:41
@LastEditors: xiaomin
@Description: 用户的绑定设备更新设备流程
@FilePath: \ioT-uat\Testcase\test13_userdevice01.py
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

from Params.params import userDeviceTest01
from Common.test_init_data import initData
from Common.casefunction import CaseFunction
from Common.Requestsfun import requestMethod
from Common.comm import loginToken
from Common.config import Config


@ddt.ddt
class userDeviceTest_01(loginToken):
    '''
    创建产品-创建设备-绑定设备-批量更新设备-批量更新设备备注名-查询设备-解绑设备-删除设备-删除产品
    '''
    @ddt.data({'title':'直连产品','dataFormat':'1','networkType':'WIFI','productName':'apitest_auto34','productNodeType':'0','sub':'false'},
              {'title':'网关子设备产品','dataFormat':'0','networkType':'WIFI','productName':'apitest_auto35','productNodeType':'0','sub':'true'},
              {'title':'边缘网关产品','dataFormat':'1','networkType':'WIFI','productName':'apitest_auto36','productNodeType':'2','sub':'false'})
    @ddt.unpack
    def test_userdevice_01(self,dataFormat,networkType,productName,productNodeType,sub,title):

        # '''数据初始化'''
        a=initData()
        a.initdata({'productName':productName})

        # 变量用来控制调取接口索引
        i=0

        '''获取test_userdevice1.yaml中的数据'''
        data=userDeviceTest01()
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
        

        '''给接口添加token'''
        for n in range(1,len(headers)):
            if 'deviceOwner' not in urls[n]:
                #开发者接口
                headers[n].update(Authorization='bearer '+loginToken().token)
            else:
                #用户接口
                headers[n].update(Authorization=res_usrtoken['token_type']+' '+res_usrtoken['access_token'])
            
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

        '''绑定用户'''
        print('\n'+url[i])
        print('------绑定用户入参------')
        binduser=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys,'deviceSecret':devicesecret})
        curcode=binduser.status_code
        print('------绑定用户返回------')
        print('status:%s'%str(curcode))
        print(str(binduser.text))
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''批量更新设备'''
        print('\n'+url[i])
        print('------更新设备入参------')
        para[i]['updateDeviceInfos'][0]['productKey']=productkeys
        updatedevice=case_function.post_request(request,url[i],headers[i],para[i])
        curcode=updatedevice.status_code
        print('------更新设备返回------')
        print('status:%s'%str(curcode))
        print(updatedevice.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1
        
        '''批量更新设备备注名称'''
        print('\n'+url[i])
        print('------批量更新设备备注名称入参------')
        para[i]['updateDeviceNicknameInfos'][0]['productKey']=productkeys
        updatenickname=case_function.post_request(request,url[i],headers[i],para[i])
        curcode=updatenickname.status_code
        print('------批量更新设备备注名称返回------')
        print('status:%s'%str(curcode))
        print(updatenickname.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1       

        '''查询设备'''
        print('\n'+url[i])
        getdevice=case_function.get_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=getdevice.status_code
        print('------查询设备返回------')   
        print('status:%s'%str(curcode))
        print(getdevice.text)      
        self.assertIn(expcode[i][0],getdevice.text)
        self.assertIn(expcode[i][1],getdevice.text)
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

        '''删除设备'''
        print('\n'+url[i])
        print('------删除设备入参------')
        deletedevice=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=deletedevice.status_code
        print('------删除设备返回------')
        print('status:%s'%str(curcode))
        print(deletedevice.text)
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

'''
@Author: xiaomin
@Date: 2020-04-27 11:37:04
@LastEditTime: 2020-05-11 14:46:22
@LastEditors: xiaomin
@Description: 设备的批量创建流程
@FilePath: \ioT-uat\Testcase\test11_device06.py
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
import time,datetime

from Params.params import DeviceTest06
from Common.test_init_data import initData
from Common.casefunction import CaseFunction
from Common.Requestsfun import requestMethod
from Common.comm import loginToken
from Common.config import Config


@ddt.ddt
class DeviceTest_06(loginToken):
    '''
    创建产品-批量创建设备-查询批次列表-查询批次详情-查询批次详情列表-查询设备-删除设备-删除产品-查询批次详情
    '''
    @ddt.data({'title':'直连产品','dataFormat':'1','networkType':'WIFI','productName':'apitest_auto31','productNodeType':'0','sub':'false'},
              {'title':'网关子设备产品','dataFormat':'0','networkType':'WIFI','productName':'apitest_auto32','productNodeType':'0','sub':'true'},
              {'title':'边缘网关产品','dataFormat':'1','networkType':'WIFI','productName':'apitest_auto33','productNodeType':'2','sub':'false'})
    @ddt.unpack
    def test_device_06(self,dataFormat,networkType,productName,productNodeType,sub,title):

        # '''数据初始化'''
        a=initData()
        a.initdata({'productName':productName})

        # 变量用来控制调取接口索引
        i=0

        '''获取test_device6.yaml中的数据'''
        data=DeviceTest06()
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

        '''批量创建设备'''
        print('\n'+url[i])
        print('------批量创建设备入参------')
        createdevice=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=createdevice.status_code
        print('------批量创建设备返回------')
        print('status:%s'%str(curcode))
        print(createdevice.text)        
        self.assertEqual(expcode[i],curcode)
        res_applyid=json.loads(createdevice.text)
        applyid=res_applyid['applyId']
        print('获取批次id：'+str(applyid))
        i=i+1
        
        time.sleep(5)

        '''查询批次列表'''
        print('\n'+url[i])
        getapplyid=case_function.get_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=getapplyid.status_code
        print('------查询批次列表返回------')   
        print('status:%s'%str(curcode))
        print(getapplyid.text) 
        self.assertIn(str(applyid),getapplyid.text)
        i=i+1

        time.sleep(5)

        '''查询批次详情'''
        print('\n'+url[i])
        getapplyinfo=case_function.get_request(request,url[i],headers[i],para[i],{'productKey':productkeys,'applyId':str(applyid)})
        curcode=getapplyinfo.status_code
        print('------查询批次详情返回------')   
        print('status:%s'%str(curcode))
        print(getapplyinfo.text) 
        res_info=json.loads(getapplyinfo.text)
        self.assertEqual(expcode[i],len(res_info['content']))
        i=i+1

        time.sleep(5)

        '''查询批次详情列表'''
        print('\n'+url[i])
        getapplylist=case_function.get_request(request,url[i],headers[i],para[i],{'applyId':str(applyid)})
        curcode=getapplylist.status_code
        print('------查询批次详情列表返回------')   
        print('status:%s'%str(curcode))
        print(getapplylist.text)       
        res_infolist=json.loads(getapplylist.text)        
        self.assertEqual(expcode[i],len(res_infolist['deviceInfos']))
        devicenames=[]
        for m in range(0,len(res_infolist['deviceInfos'])):                
            devicenames.append(res_infolist['deviceInfos'][m]['deviceName'])
        print('获取批量创建的设备deviceName：'+str(devicenames))
        i=i+1

        time.sleep(15)
        '''查询设备'''
        print('\n'+url[i])
        print('------查询设备------')
        for n in range(0,len(devicenames)):
            getdevice=case_function.get_request(request,url[i],headers[i],para[i],{'deviceName':devicenames[n],'productKey':productkeys})           
            curcode=getdevice.status_code
            print('查询设备：%s status:%s'%(devicenames[n],str(curcode)))
            print(getdevice.text)  
            self.assertIn(devicenames[n],getdevice.text)               
        i=i+1             

        '''删除设备'''
        print('\n'+url[i])
        print('------删除设备------')
        for n in range(0,len(devicenames)):          
            deletedevice=case_function.post_request(request,url[i],headers[i],para[i],{'deviceName':devicenames[n],'productKey':productkeys})
            curcode=deletedevice.status_code
            print('删除设备：%s status:%s'%(devicenames[n],str(curcode)))
            print(str(deletedevice.text))
            self.assertEqual(expcode[i],curcode)                
        i=i+1

        time.sleep(3)

        '''删除产品'''        
        print('\n'+url[i])
        print('------删除产品入参------')
        deleteproduct=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=deleteproduct.status_code
        print('------删除产品返回------')
        print('status:%s'%str(curcode))
        print(deleteproduct.text)
        self.assertEqual(expcode[i],curcode)
        i=i+1              

        '''查询批次详情'''
        print('\n'+url[i])
        getapplyinfo=case_function.get_request(request,url[i],headers[i],para[i],{'productKey':productkeys,'applyId':str(applyid)})
        curcode=getapplyinfo.status_code
        print('------查询批次详情返回------')   
        print('status:%s'%str(curcode))
        print(getapplyinfo.text) 
        res_info=json.loads(getapplyinfo.text)
        self.assertEqual(expcode[i],curcode)


if __name__ == '__main__':
    unittest.main(verbosity=2)

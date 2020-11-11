'''
@Author: xiaomin
@Date: 2020-05-09 17:53:06
@LastEditTime: 2020-05-11 11:15:54
@LastEditors: xiaomin
@Description: 入口app的边缘计算流程
@FilePath: \ioT-uat\Testcase\test19_edgeapp01.py
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

from Params.params import EdgeappTest01
from Common.test_init_data import initData
from Common.casefunction import CaseFunction
from Common.Requestsfun import requestMethod
from Common.comm import loginToken
from Common.config import Config


@ddt.ddt
class EdgeappTest_01(loginToken):
    '''
    开发者创建边缘网关产品-开发者创建边缘网关设备-开发者创建子设备产品和设备-网关设备绑定用户-入口app绑定驱动失败-入口app绑定子设备失败-开发者分配驱动给子设备产品-入口app绑定驱动成功-入口app绑定子设备成功-用户绑定子设备-用户查询子设备绑定的网关
    '''  
    def test_edgeapp_01(self):

        # '''数据初始化'''
        a=initData()
        a.initdata({'productName':'apitest_autoEdge'})
        a.initdata({'productName':'apitest_autoSub'})

        # 变量用来控制调取接口索引
        i=0

        '''获取test_edgeapp.yaml中的数据'''
        data=EdgeappTest01()
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
            if 'Owner' not in urls[n]:
                #开发者接口
                headers[n].update(Authorization='bearer '+loginToken().token)
            else:
                #用户接口
                headers[n].update(Authorization=res_usrtoken['token_type']+' '+res_usrtoken['access_token'])
            

        '''实例化调用测试数据的类'''
        case_function=CaseFunction()  

        '''开发者创建产品'''
        print('\n'+url[i])
        print('------开发者创建产品入参------')
        createproduct=case_function.post_request(request,url[i],headers[i],para[i])
        curcode=createproduct.status_code
        print('------开发者创建产品返回------')
        print('status:%s'%str(curcode))
        print(createproduct.text)
        self.assertEqual(expcode[i],curcode)
        createproduct=json.loads(createproduct.text)
        productkeys=createproduct['productKey']
        print('获取产品Key：'+productkeys)
        i=i+1

        '''开发者创建设备'''
        print('\n'+url[i])
        print('------开发者创建设备入参------')
        createdevice=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=createdevice.status_code
        print('------开发者创建设备返回------')
        print('status:%s'%str(curcode))
        print(createdevice.text)        
        self.assertEqual(expcode[i],curcode)
        deviceinfo=json.loads(createdevice.text)
        devicesecret=deviceinfo['deviceSecret']
        i=i+1

        '''开发者创建子设备产品'''
        print('\n'+url[i])
        print('------开发者创建子设备产品入参------')
        createsubproduct=case_function.post_request(request,url[i],headers[i],para[i])
        curcode=createsubproduct.status_code
        print('------开发者创建子设备产品返回------')
        print('status:%s'%str(curcode))
        print(createsubproduct.text)
        self.assertEqual(expcode[i],curcode)
        createsubproduct=json.loads(createsubproduct.text)
        subproductkeys=createsubproduct['productKey']
        print('获取子设备产品Key：'+subproductkeys)
        i=i+1

        '''开发者创建子设备'''
        print('\n'+url[i])
        print('------开发者创建设备入参------')
        createsubdevice=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':subproductkeys})
        curcode=createsubdevice.status_code
        print('------开发者创建设备返回------')
        print('status:%s'%str(curcode))
        print(createsubdevice.text)        
        self.assertEqual(expcode[i],curcode)
        subdeviceinfo=json.loads(createsubdevice.text)
        subdevicesecret=subdeviceinfo['deviceSecret']
        i=i+1

        '''网关绑定用户'''
        print('\n'+url[i])
        print('------网关绑定用户入参------')
        binduser=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys,'deviceSecret':devicesecret})
        curcode=binduser.status_code
        print('------网关绑定用户返回------')
        print('status:%s'%str(curcode))
        print(str(binduser.text))
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''入口app绑定驱动'''
        print('\n'+url[i])
        print('------入口app绑定驱动入参------')
        binddriver=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys,'boundProductKey':subproductkeys})
        curcode=binddriver.status_code
        print('------入口app绑定驱动返回------')
        print('status:%s'%str(curcode))
        print(binddriver.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''入口app绑定子设备'''
        print('\n'+url[i])
        print('------入口app绑定子设备入参------')
        bindsubdevice=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys,'boundProductKey':subproductkeys})
        curcode=bindsubdevice.status_code
        print('------入口app绑定子设备返回------')
        print('status:%s'%str(curcode))
        print(bindsubdevice.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''用户查询设备详情'''
        print('\n'+url[i])
        getdevice=case_function.get_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=getdevice.status_code
        print('------用户查询设备返回------')   
        print('status:%s'%str(curcode))
        print(getdevice.text)
        self.assertIn(expcode[i],getdevice.text)
        deviceinstance=json.loads(getdevice.text)
        instanceid=deviceinstance['instanceId']
        print('获取实例id：'+instanceid)
        i=i+1

        '''开发者绑定驱动给子设备'''
        print('\n'+url[i])
        print('------开发者绑定驱动给子设备入参------')
        binddriver=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':subproductkeys})
        curcode=binddriver.status_code
        print('------开发者绑定驱动给子设备返回------')
        print('status:%s'%str(curcode))
        print(binddriver.text)
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''入口app绑定驱动'''
        print('\n'+url[i])
        print('------入口app绑定驱动入参------')
        binddriver=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys,'boundProductKey':subproductkeys})
        curcode=binddriver.status_code
        print('------入口app绑定驱动返回------')
        print('status:%s'%str(curcode))
        print(binddriver.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''入口app绑定子设备'''
        print('\n'+url[i])
        print('------入口app绑定子设备入参------')
        bindsubdevice=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys,'boundProductKey':subproductkeys})
        curcode=bindsubdevice.status_code
        print('------入口app绑定子设备返回------')
        print('status:%s'%str(curcode))
        print(bindsubdevice.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''绑定用户到子设备'''
        print('\n'+url[i])
        print('------绑定用户到子设备入参------')
        binduser=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':subproductkeys,'deviceSecret':subdevicesecret})
        curcode=binduser.status_code
        print('------绑定用户到子设备返回------')
        print('status:%s'%str(curcode))
        print(str(binduser.text))
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''入口app查询子设备绑定的网关'''
        print('\n'+url[i])
        getdriver=case_function.get_request(request,url[i],headers[i],para[i],{'productKey':subproductkeys})
        curcode=getdriver.status_code
        print('------查询驱动返回------')   
        print('status:%s'%str(curcode))
        print(getdriver.text)
        self.assertIn(productkeys,getdriver.text)

        '''数据清理'''
        a.initdata({'productName':'apitest_autoEdge'})
        a.initdata({'productName':'apitest_autoSub'})


if __name__ == '__main__':
    unittest.main(verbosity=2)
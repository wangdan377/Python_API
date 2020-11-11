'''
@Author: xiaomin
@Date: 2020-04-26 15:42:52
@LastEditTime: 2020-04-28 16:58:30
@LastEditors: xiaomin
@Description: request(get/post)
@FilePath: \ioT-uat\Common\Requestsfun.py
'''
import requests

class requestMethod:
    def get_post(self,url,header,params,files=None):
        if files is not None:
            res=requests.post(url=url,headers=header,data=params,files=files,timeout=15)
        else:
            res=requests.post(url=url,headers=header,data=params,timeout=15)
        return res

    def get_get(self,url,header,params=None):
        if params is not None:
            res=requests.get(url=url,headers=header,params=params)
        else:
            res=requests.get(url=url,headers=header)
        return res
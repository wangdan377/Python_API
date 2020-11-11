import  sys
from otc_api import client
sys.path.append("..")
import time
import random
from util.util import  Util
from base_class import env_class
import uuid
import json
from common.read_yaml import ReadYaml
data = ReadYaml("data.yml").get_yaml_data()#读取数据

class Merchant(env_class.EnvClass,client.HttpClient):
    http_map = {
        "create_order":"web/api/pay",   #创建订单
        "confirm_order":"web/view/otc_ader/id/{}/_pay", #订单确认打款
        "get_ad_pay_info":"web/view/otc_ader_account/id/{}", #通过订单信息获取广告支付信息
        "get_finance_list":"api/v1/web/merchant_finance_history",  #获取订单历史记录
        "create_session_code":"api/v1/web/code_session", #生成图形验证码session
        "create_code":"api/v1/web/check_code", #生成验证码
        "merchant_login":"api/v1/web/merchant/_login",  #商户登录
        "refund":"web/api/refund",  #提现
        "add_pay_info":"api/v1/web/merchant_account",#添加支付方式
        "allow_order":"web/view/otc_ader/id/{}/_finish" #企业平台确认放币
    }
    def __init__(self):
        self.host = data['merchant_host']

        # self.sys_host = self.get_env()['merchant_sys_host'] #内部接口


    def create_order(self,access_key,secret,pay_type,match_type,coin_name,currency):
        #坑 amount 加密时需要给空值 调用接口时需要去掉否则接口不过
        body = {
            "return_url":"http://www.blockchaincoinpay.com/web/view/order/",
            "notify_url":"http://101.37.168.92:9900/point_card/api/done_point_card_order",
            "access_key":access_key,
            "pay_type":pay_type,
            "match_type":match_type,
            "coin_name":coin_name,
            "amount":"",
            "currency":currency,
            "merchant_order_id":"api_test_demo_"+ str(time.time()),
            "rand":str(random.randint(100000,999999)),
            "user_type":1,
            "uuid":str(uuid.uuid1())
        }
        sign = Util.sign_encrypt(body,secret)
        body.pop('amount')
        body['sign'] = sign
        url = self.get_full_url(self.http_map['create_order'])
        return self.send(url,body,method="post")

    def confirm_order(self,transac_id,pay_id,order_number):
        etc = {
            "order_number":order_number,
            "payid":pay_id
        }
        body = {
            "account_info": json.dumps({"pay_user_name":"abc"})
        }
        url = self.get_full_url(self.http_map['confirm_order'],replace={transac_id},etc=etc)
        return self.send(url,body,method="post")
    def get_ad_pay_info(self,transac_id):
        url = self.get_full_url(self.http_map['get_ad_pay_info'],replace={transac_id})
        return self.send(url)
    def get_finance_list(self,coin_id):
        etc = {
            "start":0,
            "limit":9999,
            "coin_id":coin_id
        }
        url = self.get_full_url(self.http_map['get_finance_list'],etc=etc)
        return self.send(url)

    def create_session_code(self):
        url = self.get_full_url(self.http_map['create_session_code'],h=self.sys_host)
        return self.send(url)

    def merchant_login(self,session,code,user_name,password):
        body = {
            "merchant_loginname":user_name,
            "passwd":password,
            "session":session,
            "code":code
        }
        url = self.get_full_url(self.http_map['merchant_login'],h=self.sys_host)
        return self.send(url,body,method="post")
    def create_code(self,session):
        etc = {
            "session":session
        }
        url = self.get_full_url(self.http_map['create_code'],h=self.sys_host,etc=etc)
        return self.send(url,need_rsp=False)
    def create_refund(self,coin_name,currency,pay_info,pay_type,access_key):
        body = {
            "coin_name":coin_name,
            "currency":currency,
            "access_key":access_key,
            "user_type":1,
            "pay_info":json.dumps(pay_info),
            "pay_type":pay_type,
            "match_type":1,
            "merchant_order_id":"api_test_refund_demo_"+str(time.time()),
        }
        url = self.get_full_url(self.http_map['refund'],h=self.sys_host)
        return self.send(url,body,method="post")

    def add_pay_info(self,pay_type,account_info,status,session):
        merchant_account_type_name = ""
        if pay_type == 3:
            merchant_account_type_name = "Bank"
        body = {
            "merchant_account_type":pay_type,
            "merchant_account_type_name":merchant_account_type_name,
            "merchant_account_info":account_info,
            "merchant_account_status":status
        }
        url = self.get_full_url(self.http_map['add_pay_info'])
        return self.send(url,body,method="post",sessions=session)

    def allow_order(self,transac_id,order_number):
        etc = {
            "order_number":order_number
        }
        url = self.get_full_url(self.http_map['allow_order'],etc=etc,replace={transac_id})
        return self.send(url,method="post")

import allure
from otc_api import merchant
import redis
from base_class import env_class
from common.read_yaml import ReadYaml
data = ReadYaml("data.yml").get_yaml_data()#读取数据
from db.db import *

class Merchant(env_class.EnvClass):
    is_valid_login = True
    def __init__(self,user_info,otc_db):

        self.username = user_info['user_name']
        self.password = user_info['password']
        self.db_conn = otc_db

        # row = self.db_conn.query("select * from t_merchant where merchant_loginname = '{}' ",self.user_name)
        row = sql(sql=("select * from t_merchant where merchant_loginname = '{}' ",self.user_name))
        assert row[0]
        self.merchant_id = row[0]['merchant_id']
        self.merchant_api_client = merchant.Merchant()

        rsp = self.create_session_code()

        if rsp['status_code']!= 200:
            self.is_valid_login = False
            return
        self.create_code(rsp['data']['session'])
        #获取到验证码值
        redis_config = self.get_env()['redis']
        r = redis.Redis(host=redis_config['host'], port=redis_config['port'], db=redis_config['db'])
        code = r.get(rsp['data']['session']).decode()
        login_rsp = self.merchant_login(rsp['data']['session'],code)
        if login_rsp['status_code'] != 200:
            self.is_valid_login = False
            return
        self.session = login_rsp['data']['session']

    @allure.step("获取验证code")
    def create_session_code(self):
        return self.merchant_api_client.create_session_code()
    @allure.step("生成验证码")
    def create_code(self,session):
        return self.merchant_api_client.create_code(session)

    @allure.step('企业平台-登录')
    def merchant_login(self,code_session,code):
        return self.merchant_api_client.merchant_login(code_session,code,self.user_name,self.password)
    def is_valid(self):
        return self.is_valid_login

    @allure.step('企业平台-创建订单')
    # pay_type|1-微信支付，2-支付宝支付，3-银行卡支付|
    # match_type|1-快速匹配模式，2-自由模式|
    def create_order(self,pay_type,match_type,coin_name,currency):
        merchant_access = self.get_access_key()
        access_key = merchant_access['access_key']
        access_secret = merchant_access['access_secret']
        return self.merchant_api_client.create_order(access_key,access_secret,pay_type,match_type,coin_name,currency)

    @allure.step('获取access_key')
    def get_access_key(self):
        row = self.db_conn.query("select * from t_merchant_access where merchant_id = {}", self.merchant_id)
        return row[0]

    @allure.step('企业平台-获取资产信息')
    def get_finance(self,coin_name):
        row = self.db_conn.query("select * from t_merchant_finance where merchant_id = {} and coin_name = '{}' ",self.merchant_id,coin_name)
        return row[0]
    @allure.step('企业平台-确认打款')
    def confirm_order(self,transac_id,pay_id,order_number):
        return self.merchant_api_client.confirm_order(transac_id,pay_id,order_number)
    @allure.step("企业平台-获取广告支付信息")
    def get_ad_pay_info(self,transac_id):
        return self.merchant_api_client.get_ad_pay_info(transac_id)
    @allure.step("企业平台-发起提现")
    def create_refund(self,coin_name,currency,pay_info,pay_type):
        merchant_access = self.get_access_key()
        access_key = merchant_access['access_key']
        return self.merchant_api_client.create_refund(coin_name,currency,pay_info,pay_type,access_key)
    @allure.step("企业平台-添加支付方式-并启用")
    def add_pay_info(self,pay_type,account_info,status):
        return self.merchant_api_client.add_pay_info(pay_type,account_info,status,self.session)
    @allure.step("企业平台-确认放币")
    def allow_order(self,transac_id,order_number):
        return self.merchant_api_client.allow_order(transac_id,order_number)

import allure
import sys
import  pytest
sys.path.append("..")
from db import  engine
from base_class import env_class,base_action
from otc_api import  otc_admin
from common.read_yaml import ReadYaml
data = ReadYaml("data.yml").get_yaml_data()#读取数据
from db.db import *

class OtcAdmin(env_class.EnvClass,base_action.BaseAction):
    def __init__(self,user_info,otc_admin_db):
        self.username = user_info['user_name']
        self.password = user_info['password']
        self.otc_admin_db = otc_admin_db
        self.otc_admin_api_client = otc_admin.OtcAdmin()
        result = self.admin_login()
        assert result['status_code'] == 200,"总后台管理员登录失败"
        self.session = result['data']['session']
    @allure.step("总后台账号登录")
    def admin_login(self):
        m = otc_admin.OtcAdmin()
        row = self.otc_admin_db.query("select * from t_admin where admin_name = '{}'",self.username)
        row =sql(sql=("select * from t_admin where admin_name = '{}'",self.username))
        code = self.google_code(row[0]['auth_key'])
        return m.admin_login(self.username,self.password, code)

    @allure.step("总后台获取指定账号的申请订单")
    def admin_get_draw_order(self,otc_ader_id,status):
        return self.otc_admin_api_client.admin_get_draw_order(otc_ader_id,status,self.session)

    @allure.step("修改提币申请状态")
    def admin_update_draw_status(self,otc_ader_id,order_id,status):
        return self.otc_admin_api_client.admin_update_draw_status(order_id,otc_ader_id,status,self.session)

    @allure.step("获取商户手续费信息")
    def admin_get_merchant_info(self,login_name):
        return self.otc_admin_api_client.admin_get_merchant_info(login_name,self.session)

    @allure.step("获取出售广告-交易对账")
    def admin_get_transac_list(self,order_number = ""):
        return self.otc_admin_api_client.admin_get_transac_list(self.session,order_number)

    @allure.step("获取购买广告-交易对账")
    def admin_get_withdraw_transac_list(self, order_number=""):
        return self.otc_admin_api_client.admin_get_withdraw_transac_list(self.session, order_number)

import sys

import allure
import pytest

sys.path.append("..")
from util.util import Util
from decimal import Decimal
from const import status_code, bs_code
from base_class import base_case
from action import otc
from otc_api.otc import *

class TestRecharge(base_case.BaseCase):
    # OtcClient=OtcClient()

    @allure.title("修改密码")
    @pytest.mark.parametrize("passwd_old,passwd_new,_except", [('a1234567', "a1234567", status_code.EXCEPT_SUCCESS)])
    def test_updata_passwd(self, passwd_old, passwd_new, _except, three_ad_action):
        ##修改密码
        code = three_ad_action.get_google_code()
        # print(self.OtcClient.get_full_url(self.http_map['passwd']))
        # code = three_ad_action.google_code(google_info['safe_secret'])
        new_update_passwd_info = three_ad_action.update_passwd(passwd_old, passwd_new, code)
        print(passwd_old, passwd_new, code)
        print(new_update_passwd_info)
        self.catch(new_update_passwd_info["status_code"] == 200, _except, status_code.OTC_UPDATA_PASSWD)

if __name__=="__main__":
    pytest.main(['-s',r'E:\何卜强-软件\接口自动化代码\gongsi-JKdaima\otc\case\recharge\test_hbqtest.py'])
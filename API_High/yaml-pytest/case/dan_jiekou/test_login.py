import allure
import requests
import pytest
from api.login_method import Login
from common.logger import Log
from common.read_yaml import ReadYaml
testdata = ReadYaml("login_data.yml").get_yaml_data()#读取数据

@allure.feature('登录测试用例接口')#测试报告显示测试功能
class Test_login():
    '''测试登录接口'''
    log = Log()
    @pytest.mark.parametrize("username,password,expect",testdata["test_login_data"],
                             ids = ["正常登录",
                                   "密码为空登录",
                                   "账号为空登录",
                                   "账号错误登录",
                                   "密码错误登录",
                                   "账号存在空格登录",
                                   "密码存在空格登录",
                                   "账号存在特殊符号登录",
                                   "密码存在特殊符号登录",
                                   "账号不完整登录",
                                   "密码不完整登录"])#参数化测试用例
    @allure.step('账号，密码登录')#测试报告显示步骤
    @allure.link('http://**********:6009/api/v1/dan_jiekou',name='测试接口')#测试报告显示链接
    def test_login(self,username,password,expect):
        s = requests.session()#定义session会话
        self.log.info('------用户登录接口-----')
        shili = Login(s)#实例化
        msg = shili.login(username,password)
        self.log.info('获取请求结果：%s'%msg.json())
        #print(msg.json())
        #断言
        assert msg.json()["msg"] == expect['msg']
        assert msg.json()["code"] == expect['code']



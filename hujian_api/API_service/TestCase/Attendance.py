import pytest
import allure
import requests
import json

from Params.params import Login
from Params.params import Login_info
from Params.params import Password_reset
from Params.params import Log_info
from Params.params import Log_latest
from Params.params import Log_list

from Params.params import Attendance_groups_sync
from Params.params import Attendance_schedules_sync
from Params.params import Attendance_records_sync
from Params.params import Flow_sync

from Params.params import Department_sync
from Params.params import Department_list
from Params.params import Department_employees_list
from Params.params import Department_employee_query


from Params.params import Attendance_class_list
from Params.params import Attendance_analyse
from Params.params import Attendance_analyse_result
from Params.params import Attendance_analyse_result_statistics

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


class TestAttendance:
    sessionA = requests.session()

    @allure.severity('normal')
    @allure.feature('Attendance')
    @allure.story('Attendance_login')
    def test_Attendance_login_01(self):
        ass = Assert.Assertions()
        reqF = Get.Get()
        reqS = Post.Post()
        reqN = Get.Get()

        urlF = 'http://172.16.2.101:4000/dist/login'
        urlS = 'http://172.16.2.101:4000/api/login'
        urlN = 'http://172.16.2.101:4000/api/login/info'
        dictP = {'username':'zy_admin','password':'zy123456789'}

        res = reqF.get_model_a(self.sessionA,urlF)
        resCode = res['code']
        assert ass.assert_code(resCode, 200)

        resp = reqS.post_model_b(self.sessionA,urlS,dictP)
        respCode = resp['code']
        respJson = resp['text']
        assert ass.assert_code(respCode, 200)
        assert ass.assert_in_text(respJson, 'ok')
        assert ass.assert_in_text(respJson, 'zy_admin')
        Consts.RESULT_LIST.append('True')

        response = reqN.get_model_a(self.sessionA, urlN)
        responseCode = response['code']
        responseJson = response['text']
        assert ass.assert_code(responseCode, 200)
        assert ass.assert_in_text(responseJson, 'zy_admin')
        Consts.RESULT_LIST.append('True')



    @allure.severity('normal')
    @allure.feature('Attendance')
    @allure.story('Attendance_log_info')
    #log信息
    def test_Attendance_log_info_01(self):
        req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4000/api/log/info?logId=123'

        response = req.get_model_a(self.sessionA, url)
        resCode = response['code']
        resJson = response['text']
        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resJson, 'ok')
        Consts.RESULT_LIST.append('True')


    @allure.severity('normal')
    @allure.feature('Attendance')
    @allure.story('Attendance_log_latest')
    #最近log信息
    def test_Attendance_log_latest_01(self):
        req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4000/api/log/last?type=SYNC_CLASS_GROUPS'

        response = req.get_model_a(self.sessionA, url)
        resCode = response['code']
        resJson = response['text']
        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resJson, 'ok')
        Consts.RESULT_LIST.append('True')


    @allure.severity('normal')
    @allure.feature('Attendance')
    @allure.story('Attendance_log_list')
    #log列表
    def test_Attendance_log_list_01(self):

        req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4000/api/log/list?type=SYNC_RECORD'
        response = req.get_model_a(self.sessionA,url)
        resCode = response['code']
        resJson = response['text']
        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resJson, 'ok')
        Consts.RESULT_LIST.append('True')



    @allure.severity('normal')
    @allure.feature('Attendance')
    @allure.story('Attendance_groups_sync')
    #同步班组信息
    def test_Attendance_groups_sync_01(self):
        req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4000/api/attendance/groups/sync'

        response = req.get_model_a(self.sessionA, url)
        resCode = response['code']
        resJson = response['text']
        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resJson, 'ok')
        Consts.RESULT_LIST.append('True')


    @allure.severity('normal')
    @allure.feature('Attendance')
    @allure.story('Attendance_schedule_sync')
    #同步排班记录
    def test_Attendance_schedule_sync_01(self):
        req = Get.Get()
        req_again = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4000/api/attendance/schedule/sync?date=2019-10'
        url_again = 'http://172.16.2.101:4000/api/attendance/schedule/sync?force=1&date=2019-10'

        response = req.get_model_a(self.sessionA, url)
        resCode = response['code']
        resJson = response['text']
        assert ass.assert_code(resCode, 200)
        x = ass.assert_code(resCode, 200)
        print(x)
        assert ass.assert_in_text(resJson, '指定时间段已经同步过')
        Consts.RESULT_LIST.append('True')

        response_again = req_again.get_model_a(self.sessionA, url_again)
        resCode_again = response_again['code']
        resJson_again = response_again['text']
        assert ass.assert_code(resCode_again, 200)
        assert ass.assert_in_text(resJson_again, 'ok')
        Consts.RESULT_LIST.append('True')


    @allure.severity('normal')
    @allure.feature('Attendance')
    @allure.story('Attendance_record_sync')
    #同步打卡记录
    def test_Attendance_record_sync_01(self):
        req = Get.Get()
        req_again = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4000/api/attendance/record/sync?date=2019-10'
        url_again = 'http://172.16.2.101:4000/api/attendance/record/sync?force=1&date=2019-10'

        response = req.get_model_a(self.sessionA, url)
        resCode = response['code']
        resJson = response['text']
        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resJson, '指定时间段已经同步过')

        Consts.RESULT_LIST.append('True')

        response_again = req_again.get_model_a(self.sessionA, url_again)
        resCode_again = response_again['code']
        resJson_again = response_again['text']
        assert ass.assert_code(resCode_again, 200)
        assert ass.assert_in_text(resJson_again, 'ok')
        Consts.RESULT_LIST.append('True')

    @allure.severity('normal')
    @allure.feature('Attendance')
    @allure.story('Attendance_flow_sync')
    #同步审批记录
    def test_Attendance_flow_sync_01(self):
        req = Get.Get()
        req_again = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4000/api/flow/sync?date=2019-10'

        url_again = 'http://172.16.2.101:4000/api/flow/sync?force=1&date=2019-10'

        response = req.get_model_a(self.sessionA, url)
        resCode = response['code']
        resJson = response['text']
        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resJson, '指定时间段已经同步过')
        Consts.RESULT_LIST.append('True')

        response_again = req_again.get_model_a(self.sessionA, url_again)
        resCode_again = response_again['code']
        resJson_again = response_again['text']
        assert ass.assert_code(resCode_again, 200)
        assert ass.assert_in_text(resJson_again, 'ok')
        Consts.RESULT_LIST.append('True')


    @allure.severity('normal')
    @allure.feature('Attendance')
    @allure.story('Attendance_department_sync')
    #同步部门
    def test_Attendance_department_sync_01(self):

        req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4000/api/dept/sync?force=1'

        response = req.get_model_a(self.sessionA, url)
        resCode = response['code']
        resJson = response['text']
        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resJson, 'ok')
        Consts.RESULT_LIST.append('True')


    @allure.severity('normal')
    @allure.feature('Attendance')
    @allure.story('Attendance_department_list')
    #查询部门列表
    def test_Attendance_department_list_01(self):
        req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4000/api/dept/list?parentId=1&deptId=1&isRoot=1'

        response = req.get_model_a(self.sessionA, url)
        resCode = response['code']
        resJson = response['text']
        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resJson, 'ok')
        Consts.RESULT_LIST.append('True')


    @allure.severity('normal')
    @allure.feature('Attendance')
    @allure.story('Attendance_employee_list')
    #查询部门员工列表
    def test_Attendance_employee_list_01(self):
        req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4000/api/dept/user/list?deptId=118994363'

        response = req.get_model_a(self.sessionA, url)
        resCode = response['code']
        resJson = response['text']
        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resJson, 'ok')
        Consts.RESULT_LIST.append('True')


    @allure.severity('normal')
    @allure.feature('Attendance')
    @allure.story('Attendance_employee_query')
    #模糊查询员工
    def test_Attendance_employee_query_01(self):
        req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4000/api/dept/user/query?query=王'

        response = req.get_model_a(self.sessionA, url)
        resCode = response['code']
        resJson = response['text']
        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resJson, 'ok')
        Consts.RESULT_LIST.append('True')

    @allure.severity('normal')
    @allure.feature('Attendance')
    @allure.story('Attendance_class_list')
    #班组列表
    def test_Attendance_class_list_01(self):
        req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4000/api/attendance/class/list'

        response = req.get_model_a(self.sessionA, url)
        resCode = response['code']
        resJson = response['text']
        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resJson, 'ok')
        Consts.RESULT_LIST.append('True')


    @allure.severity('normal')
    @allure.feature('Attendance')
    @allure.story('Attendance_analyse')
    #分析考勤

    def test_Attendance_analyse_01(self):
        req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4000/api/attendance/analyse?startDate=2019-12-01 00:00:00&endDate=2020-01-01 00:00:00&userIds=081912243819967935,013157464421091349'


        response = req.get_model_a(self.sessionA, url)
        resCode = response['code']
        resJson = response['text']
        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resJson, 'ok')
        Consts.RESULT_LIST.append('True')



    @allure.severity('normal')
    @allure.feature('Attendance')
    @allure.story('Attendance_analyse_result')
    #获取考勤分析结果
    def test_Attendance_analyse_result_01(self):
        req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4000/api/attendance/analyse/list?userId=013157464421091349&startDate=2019-12-01 00:00:00&endDate=2020-01-01 00:00:00&page=1&pageSize=31'

        response = req.get_model_a(self.sessionA, url)
        resCode = response['code']
        resJson = response['text']
        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resJson, 'ok')
        Consts.RESULT_LIST.append('True')


    @allure.severity('normal')
    @allure.feature('Attendance')
    @allure.story('Attendance_analyse_result_total')
    #分析考勤分析统计结果
    def test_Attendance_analyse_result_total_01(self):
        req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4000/api/attendance/analyse/statlist?startDate=2019-12-01&endDate=2019-12-01&userIds=076909244424161396,266734392436273342'

        response = req.get_model_a(self.sessionA, url)
        resCode = response['code']
        resJson = response['text']
        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resJson, 'ok')
        Consts.RESULT_LIST.append('True')

    @allure.severity('normal')
    @allure.feature('Attendance')
    @allure.story('Attendance_password_reset')
    def test_Attendance_password_reset_01(self):
        req = Post.Post()
        ass = Assert.Assertions()

        response = req.post_model_b(self.sessionA, url, dictP)
        resCode = response['code']
        resJson = response['text']
        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resJson, 'ok')
        Consts.RESULT_LIST.append('True')







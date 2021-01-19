import pytest
import allure
import requests
import json
import time

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


class Attendance_statistics:

    @allure.severity('normal')
    @allure.feature('Attendance_statistics')
    @allure.story('Attendance_statistics_single')
    def test_single_01(self):
        session_a = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url_2019_11 = 'http://172.16.2.101:4000/api/attendance/analyse?startDate=2019-11-01 00:00:00&endDate=2019-11-30 00:00:00&userIds=01694950111182631'
        # 分析 用户01694950111182631 2019年11月 考勤
        res_2019_11 = get_req.get_model_a(session_a, url_2019_11)

        time.sleep(10)

        resCode_2019_11 = res_2019_11['code']
        resText_2019_11 = res_2019_11['text']
        #print(resText_2019_11)
        assert ass.assert_code(resCode_2019_11, 200)
        assert ass.assert_in_text(resText_2019_11, 'ok')
        Consts.RESULT_LIST.append('True')

        url_statistics_2019_11 = 'http://172.16.2.101:4000/api/attendance/analyse/statlist?startDate=2019-11-01&endDate=2019-11-30&userIds=01694950111182631'
        #获取 用户01694950111182631 2019年11月 考勤统计结果
        res_statistics_2019_11 = get_req.get_model_a(session_a,url_statistics_2019_11)

        res_statCode_2019_11 = res_statistics_2019_11['code']
        res_statText_2019_11 = res_statistics_2019_11['text']
        assert ass.assert_code(res_statCode_2019_11, 200)
        assert ass.assert_in_text(res_statText_2019_11, 'ok')
        Consts.RESULT_LIST.append('True')

        res_statDict_2019_11 = json.loads(res_statText_2019_11)

        resInfo_name = res_statDict_2019_11['result']['list'][0]['user']['name']

        resInfo_days = res_statDict_2019_11['result']['list'][0]['days']
        resInfo_dutyDays = res_statDict_2019_11['result']['list'][0]['dutyDays']

        resInfo_abnormalDates = len(res_statDict_2019_11['result']['list'][0]['abnormalDates'])

        resInfo_overtime = res_statDict_2019_11['result']['list'][0]['dayoffDays']

        if res_statDict_2019_11['result']['list'][0]['leavesDays']:
            resInfo_business = res_statDict_2019_11['result']['list'][0]['leavesDays']['business']
        resInfo_business = 0

        if res_statDict_2019_11['result']['list'][0]['leavesDays']:
            resInfo_out = res_statDict_2019_11['result']['list'][0]['leavesDays']['out']
        resInfo_out = 0

        resInfo_abnormalMinute = res_statDict_2019_11['result']['list'][0]['abnormalMinute']

        resInfo_dinnerCount = res_statDict_2019_11['result']['list'][0]['dinnerCount']

        resInfo_nightSnackCount = res_statDict_2019_11['result']['list'][0]['nightSnackCount']

        #print(type(resInfo_nightSnackCount))

        assert ass.assert_text(resInfo_name, '郭维')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_text(resInfo_days, 30)
        Consts.RESULT_LIST.append('True')
        assert ass.assert_text(resInfo_dutyDays, 21)
        Consts.RESULT_LIST.append('True')
        assert ass.assert_text(resInfo_abnormalDates, 16)
        Consts.RESULT_LIST.append('True')
        assert ass.assert_text(resInfo_overtime, '0')
        Consts.RESULT_LIST.append('True')

        assert ass.assert_text(resInfo_business, 0)
        Consts.RESULT_LIST.append('True')
        assert ass.assert_text(resInfo_out, 0)
        Consts.RESULT_LIST.append('True')
        assert ass.assert_text(resInfo_abnormalMinute, '7140.00')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_text(resInfo_dinnerCount, 2)
        Consts.RESULT_LIST.append('True')
        assert ass.assert_text(resInfo_nightSnackCount, 2)
        Consts.RESULT_LIST.append('True')


if __name__ == '__main__':
    a = Attendance_statistics()
    a.test_single_01()

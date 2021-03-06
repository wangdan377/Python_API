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


class Attendance_analyse_patch:

    @allure.severity('normal')
    @allure.feature('Attendance_analyse')
    @allure.story('Attendance_analyse_patch')
    def test_patch_01(self):
        session_a = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url_2019_11 = 'http://172.16.2.101:4000/api/attendance/analyse?startDate=2019-11-01 00:00:00&endDate=2019-11-30 00:00:00&userIds=233469305921665897'
        # 分析 用户233469305921665897 2019年11月 考勤
        res_2019_11 = get_req.get_model_a(session_a, url_2019_11)

        time.sleep(10)

        resCode_2019_11 = res_2019_11['code']
        resText_2019_11 = res_2019_11['text']
        #print(resText_2019_11)
        assert ass.assert_code(resCode_2019_11, 200)
        assert ass.assert_in_text(resText_2019_11, 'ok')
        Consts.RESULT_LIST.append('True')

        url_result_2019_11 = 'http://172.16.2.101:4000/api/attendance/analyse/list?userId=233469305921665897&startDate=2019-11-01 00:00:00&endDate=2019-11-30 00:00:00&pageSize=31'
        # 获取 用户233469305921665897 2019年11月 考勤分析结果
        res_result_2019_11 = get_req.get_model_a(session_a, url_result_2019_11)

        res_resultCode_2019_11 = res_result_2019_11['code']
        res_resultText_2019_11 = res_result_2019_11['text']
        assert ass.assert_code(res_resultCode_2019_11, 200)
        assert ass.assert_in_text(res_resultText_2019_11, 'ok')
        Consts.RESULT_LIST.append('True')

        res_resultDict_2019_11 = json.loads(res_resultText_2019_11)
        resInfo_11_01 = res_resultDict_2019_11['result']['list'][0]
        resInfo_11_02 = res_resultDict_2019_11['result']['list'][1]
        resInfo_11_03 = res_resultDict_2019_11['result']['list'][2]
        resInfo_11_04 = res_resultDict_2019_11['result']['list'][3]
        resInfo_11_05 = res_resultDict_2019_11['result']['list'][4]
        resInfo_11_06 = res_resultDict_2019_11['result']['list'][5]
        resInfo_11_07 = res_resultDict_2019_11['result']['list'][6]
        resInfo_11_08 = res_resultDict_2019_11['result']['list'][7]
        resInfo_11_09 = res_resultDict_2019_11['result']['list'][8]
        resInfo_11_10 = res_resultDict_2019_11['result']['list'][9]
        resInfo_11_11 = res_resultDict_2019_11['result']['list'][10]
        resInfo_11_12 = res_resultDict_2019_11['result']['list'][11]
        resInfo_11_13 = res_resultDict_2019_11['result']['list'][12]
        resInfo_11_14 = res_resultDict_2019_11['result']['list'][13]
        resInfo_11_15 = res_resultDict_2019_11['result']['list'][14]
        resInfo_11_16 = res_resultDict_2019_11['result']['list'][15]
        resInfo_11_17 = res_resultDict_2019_11['result']['list'][16]
        resInfo_11_18 = res_resultDict_2019_11['result']['list'][17]
        resInfo_11_19 = res_resultDict_2019_11['result']['list'][18]
        resInfo_11_20 = res_resultDict_2019_11['result']['list'][19]
        resInfo_11_21 = res_resultDict_2019_11['result']['list'][20]
        resInfo_11_22 = res_resultDict_2019_11['result']['list'][21]
        resInfo_11_23 = res_resultDict_2019_11['result']['list'][22]
        resInfo_11_24 = res_resultDict_2019_11['result']['list'][23]
        resInfo_11_25 = res_resultDict_2019_11['result']['list'][24]
        resInfo_11_26 = res_resultDict_2019_11['result']['list'][25]
        resInfo_11_27 = res_resultDict_2019_11['result']['list'][26]
        resInfo_11_28 = res_resultDict_2019_11['result']['list'][27]
        resInfo_11_29 = res_resultDict_2019_11['result']['list'][28]
        resInfo_11_30 = res_resultDict_2019_11['result']['list'][29]

        assert ass.assert_in_text(resInfo_11_01, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_02, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_03, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_04, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_05, 'SUCCESS')
        Consts.RESULT_LIST.append('True')

        assert ass.assert_in_text(resInfo_11_06, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_07, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_08, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_09, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_10, 'SUCCESS')
        Consts.RESULT_LIST.append('True')

        assert ass.assert_in_text(resInfo_11_11, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_12, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_13, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_14, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_15, 'SUCCESS')
        Consts.RESULT_LIST.append('True')

        assert ass.assert_in_text(resInfo_11_16, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_17, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_18, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_19, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_20, 'SUCCESS')
        Consts.RESULT_LIST.append('True')

        assert ass.assert_in_text(resInfo_11_21, 'ABNORMAL480')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_22, 'ABNORMAL480')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_23, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_24, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_25, 'ABNORMAL480')
        Consts.RESULT_LIST.append('True')

        assert ass.assert_in_text(resInfo_11_26, 'ABNORMAL480')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_27, 'ABNORMAL480')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_28, 'ABNORMAL480')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_29, 'ABNORMAL480')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_11_30, 'SUCCESS')
        Consts.RESULT_LIST.append('True')

if __name__ == '__main__':
    a = Attendance_analyse_patch()
    a.test_patch_01()

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


class Attendance_analyse_combine_02:

    @allure.severity('normal')
    @allure.feature('Attendance_analyse')
    @allure.story('Attendance_analyse_combine')
    def test_combine_02(self):
        session_a = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url_2019_10 = 'http://172.16.2.101:4000/api/attendance/analyse?startDate=2019-10-01 00:00:00&endDate=2019-10-31 00:00:00&userIds=101237236736401301'
        #分析 用户101237236736401301 2019年10月 考勤
        res_2019_10 = get_req.get_model_a(session_a,url_2019_10)

        time.sleep(10)

        resCode_2019_10 = res_2019_10['code']
        resText_2019_10 = res_2019_10['text']
        #print(resText_2019_10)
        assert ass.assert_code(resCode_2019_10, 200)
        assert ass.assert_in_text(resText_2019_10, 'ok')
        Consts.RESULT_LIST.append('True')

        url_result_2019_10 = 'http://172.16.2.101:4000/api/attendance/analyse/list?userId=124734644336498201&startDate=2019-10-01 00:00:00&endDate=2019-10-31 00:00:00&pageSize=31'
        #获取 用户124734644336498201 2019年10月 考勤分析结果
        res_result_2019_10 = get_req.get_model_a(session_a,url_result_2019_10)

        res_resultCode_2019_10 = res_result_2019_10['code']
        res_resultText_2019_10 = res_result_2019_10['text']
        assert ass.assert_code(res_resultCode_2019_10, 200)
        assert ass.assert_in_text(res_resultText_2019_10, 'ok')
        Consts.RESULT_LIST.append('True')

        res_resultDict_2019_10 = json.loads(res_resultText_2019_10)
        resInfo_10_01 = res_resultDict_2019_10['result']['list'][0]
        resInfo_10_02 = res_resultDict_2019_10['result']['list'][1]
        resInfo_10_03 = res_resultDict_2019_10['result']['list'][2]
        resInfo_10_04 = res_resultDict_2019_10['result']['list'][3]
        resInfo_10_05 = res_resultDict_2019_10['result']['list'][4]
        resInfo_10_06 = res_resultDict_2019_10['result']['list'][5]
        resInfo_10_07 = res_resultDict_2019_10['result']['list'][6]
        resInfo_10_08 = res_resultDict_2019_10['result']['list'][7]
        resInfo_10_09 = res_resultDict_2019_10['result']['list'][8]
        resInfo_10_10 = res_resultDict_2019_10['result']['list'][9]
        resInfo_10_11 = res_resultDict_2019_10['result']['list'][10]
        resInfo_10_12 = res_resultDict_2019_10['result']['list'][11]
        resInfo_10_13 = res_resultDict_2019_10['result']['list'][12]
        resInfo_10_14 = res_resultDict_2019_10['result']['list'][13]
        resInfo_10_15 = res_resultDict_2019_10['result']['list'][14]
        resInfo_10_16 = res_resultDict_2019_10['result']['list'][15]
        resInfo_10_17 = res_resultDict_2019_10['result']['list'][16]
        resInfo_10_18 = res_resultDict_2019_10['result']['list'][17]
        resInfo_10_19 = res_resultDict_2019_10['result']['list'][18]
        resInfo_10_20 = res_resultDict_2019_10['result']['list'][19]
        resInfo_10_21 = res_resultDict_2019_10['result']['list'][20]
        resInfo_10_22 = res_resultDict_2019_10['result']['list'][21]
        resInfo_10_23 = res_resultDict_2019_10['result']['list'][22]
        resInfo_10_24 = res_resultDict_2019_10['result']['list'][23]
        resInfo_10_25 = res_resultDict_2019_10['result']['list'][24]
        resInfo_10_26 = res_resultDict_2019_10['result']['list'][25]
        resInfo_10_27 = res_resultDict_2019_10['result']['list'][26]
        resInfo_10_28 = res_resultDict_2019_10['result']['list'][27]
        resInfo_10_29 = res_resultDict_2019_10['result']['list'][28]
        resInfo_10_30 = res_resultDict_2019_10['result']['list'][29]
        resInfo_10_31 = res_resultDict_2019_10['result']['list'][30]

        assert ass.assert_in_text(resInfo_10_08, 'ABNORMAL')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_10_09, 'SUCCESS')
        Consts.RESULT_LIST.append('True')
        assert ass.assert_in_text(resInfo_10_10, 'ABNORMAL')
        Consts.RESULT_LIST.append('True')

if __name__ == '__main__':
    a = Attendance_analyse_combine_02()
    a.test_combine_02()

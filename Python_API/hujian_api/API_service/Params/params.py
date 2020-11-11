import os
from Params import tools
from Common import Log

log = Log.Log()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

def get_parameter(name):
    data = tools.GetPages().get_page_list()
    param = data[name]
    return param

class Attendance_groups_sync:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Attendance_groups_sync.yaml')
    params = get_parameter('Attendance_groups_sync')
    url = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])

class Attendance_class_list:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Attendance_class_list.yaml')
    params = get_parameter('Attendance_class_list')
    url = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])

class Attendance_schedules_sync:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Attendance_schedules_sync.yaml')
    params = get_parameter('Attendance_schedules_sync')
    url = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])

class Attendance_records_sync:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Attendance_records_sync.yaml')
    params = get_parameter('Attendance_records_sync')
    url = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])

class Flow_sync:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Flow_sync.yaml')
    params = get_parameter('Flow_sync')
    url = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])

class Attendance_analyse:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Attendance_analyse.yaml')
    params = get_parameter('Attendance_analyse')
    url = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])

class Attendance_analyse_result:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Attendance_analyse_result.yaml')
    params = get_parameter('Attendance_analyse_result')
    url = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])

class Attendance_analyse_result_statistics:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Attendance_analyse_result_statistics.yaml')
    params = get_parameter('Attendance_analyse_result_statistics')
    url = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])

class Department_sync:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Department_sync.yaml')
    params = get_parameter('Department_sync')
    url = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])

class Department_list:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Department_list.yaml')
    params = get_parameter('Department_list')
    url = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])

class Department_employees_list:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Department_employees_list.yaml')
    params = get_parameter('Department_employees_list')
    url = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])

class Department_employee_query:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Department_employee_query.yaml')
    params = get_parameter('Department_employee_query')
    url = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])

class Log_info:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Log_info.yaml')
    params = get_parameter('Log_info')
    url = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])

class Log_latest:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Log_latest.yaml')
    params = get_parameter('Log_latest')
    url = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])

class Log_list:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Log_list.yaml')
    params = get_parameter('Log_list')
    url = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])

class Login:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Login.yaml')
    params = get_parameter('Login')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])

class Login_info:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Login_info.yaml')
    params = get_parameter('Login_info')
    url = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])

class Password_reset:
    log.info('解析yaml,Path:' + path_dir + '/Params/Yaml/Password_reset.yaml')
    params = get_parameter('Password_reset')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])

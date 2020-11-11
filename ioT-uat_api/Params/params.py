'''
获取测试数据
'''
import os
from Params import tools
path_dir=str(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))


def get_parameter(name):
    data=tools.GetPages().get_page_list()
    param=data[name]
    return param

#取出Login中的测试数据
class Login:
    params=get_parameter('Login')
    url=[]
    header=[]
    data=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        
#取出init中的测试数据
class init_Data:
    params=get_parameter('init_Data')
    url=[]
    header=[]
    data=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        
# '''取出test_product1.yaml中的测试数据'''
class ProductTest01:
    params=get_parameter('ProductTest01')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_product2.yaml中的测试数据'''
class ProductTest02:
    params=get_parameter('ProductTest02')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_product3.yaml中的测试数据'''
class ProductTest03:
    params=get_parameter('ProductTest03')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_product4.yaml中的测试数据'''
class ProductTest04:
    params=get_parameter('ProductTest04')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_product5.yaml中的测试数据'''
class ProductTest05:
    params=get_parameter('ProductTest05')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_device1.yaml中的测试数据'''
class DeviceTest01:
    params=get_parameter('DeviceTest01')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_device2.yaml中的测试数据'''
class DeviceTest02:
    params=get_parameter('DeviceTest02')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_device3.yaml中的测试数据'''
class DeviceTest03:
    params=get_parameter('DeviceTest03')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_device4.yaml中的测试数据'''
class DeviceTest04:
    params=get_parameter('DeviceTest04')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_device5.yaml中的测试数据'''
class DeviceTest05:
    params=get_parameter('DeviceTest05')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_device6.yaml中的测试数据'''
class DeviceTest06:
    params=get_parameter('DeviceTest06')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_driver1.yaml中的测试数据'''
class DriverTest01:
    params=get_parameter('DriverTest01')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_userdevice1.yaml中的测试数据'''
class userDeviceTest01:
    params=get_parameter('userDeviceTest01')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_userdevice2.yaml中的测试数据'''
class userDeviceTest02:
    params=get_parameter('userDeviceTest02')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_userdevice3.yaml中的测试数据'''
class userDeviceTest03:
    params=get_parameter('userDeviceTest03')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_userdevice4.yaml中的测试数据'''
class userDeviceTest04:
    params=get_parameter('userDeviceTest04')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_edgedev.yaml中的测试数据'''
class EdgedevTest01:
    params=get_parameter('EdgedevTest01')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_edgeuser.yaml中的测试数据'''
class EdgeuserTest01:
    params=get_parameter('EdgeuserTest01')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])

# '''取出test_edgeapp.yaml中的测试数据'''
class EdgeappTest01:
    params=get_parameter('EdgeappTest01')
    url=[]
    header=[]
    data=[]
    code=[]
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])
        data.append(params[i]['data'])
        code.append(params[i]['code'])


import time
now = time.time()
print(now)



Content-Type: multipart/form-data; boundary=-----------13418483933

-----------13418483933
Content-Disposition: form-data; name="service_key"

-----------13418483933
Content-Disposition: form-data; name="device_sn"

-----------13418483933
Content-Disposition: form-data; name="service_code"

-----------13418483933


import sys

reload(sys)
sys.path.append('./python2.7/site-packages')
sys.path.append('./python2.7/site-packages/requests_toolbelt-0.8.0-py2.7.egg')
print
sys.path
import urllib2
import urllib
import cookielib
import json
import httplib
import re
import requests
import random
from requests_toolbelt import MultipartEncoder

if len(sys.argv) != 7:
    print
    sys.argv[
        0] + ' ' + 'deploy_name' + ' ' + 'apk_name' + ' ' + 'promptInfo' + ' ' + 'versionDesc' + ' ' + 'versionLargeNumber' + ' ' + 'applications.id'
    sys.exit()
deploy_name = sys.argv[1]
apk_name = sys.argv[2]
promptInfo = sys.argv[3]
versionDesc = sys.argv[4]
versionLargeNumber = sys.argv[5]
applications = sys.argv[6]
j = 10
id = []
id = ''.join(str(i) for i in random.sample(range(0, 11), j))  # sample(seq, n) 从序列seq中选择n个随机且独立的元素；
print
id

s = requests.session()
print
s.headers
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',

    'Host': '10.4.160.88:8080',
    'Referer': 'http://10.4.160.88:8080/nqsky-meap-manager/index',

}
login_url = 'http://10.4.160.88:8080/nqsky-meap-manager/login'
data = {'csrf': '', '_csrf_header': '', 'userName': 'admin', 'password': '1'}
# data = urllib.urlencode(data)
response = s.post(login_url, data=data, headers=headers)
# print  response
# print response.status_code
# print response.content
url = 'http://10.4.160.88:8080/nqsky-meap-manager/main/applications/applications/list'
r = s.get(url, headers=headers)
r = r.text
# print r

# headers = {
#
#    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'Refer':'http://10.4.160.88:8080/nqsky-meap-manager/main/applications/appInfo/list/0/8a8420d85f809d23015f93fa25590d8c',
#    'Content-Type': "multipart/form-data; 'boundary=---------------------------%s" %(id)
# }
print
headers
uploadurl = 'http://10.4.160.88:8080/nqsky-meap-manager/main/applications/appVersion/save'
# data={'versionName':'w213','deviceType':'1','status':'1','versionSystem':'1.0','platformType':'1','promptInfo':'publish','versionDesc':'','appUrl':'','versionLargeNumber':'1.1','versionLargeFile':'checkping.pl','largeFile':'','enforceStatus':'1','snapshotImg':'','snapshotFile':'','snapshotName':'','versionType':'','applications.id':'8a8420d85f809d23015f93fa25590d8c','id':'','auditStatus':'0','appOrder':'1','isPortal':'','deviceAuthority':'','technologyType':'3'}
arr1 = ['', '', '', '', '', '']
jsonstr = json.dumps(arr1)
m = MultipartEncoder(
    fields={
        "versionName": (None, deploy_name),
        "deviceType": (None, "1"),
        "status": (None, "1"),
        "versionSystem": (None, "1.5"),
        "platformType": (None, "1"),
        "promptInfo": (None, promptInfo),
        "versionDesc": (None, versionDesc),
        "versionLargeNumber": (None, versionLargeNumber),
        "versionLargeFile": "apk_name",
        "largeFile": (apk_name, open(apk_name, 'rb'), 'application/octet-stream'),
        "enforceStatus": (None, "1"),
        "applications.id": (None, applications),
        "auditStatus": (None, "0"),
        "appOrder": (None, "2"),
        "technologyType": (None, "3"),
        "snapshotImg": (None, jsonstr),
        "snapshotFile": (None, jsonstr),
        "snapshotName": (None, jsonstr)
    }

)
print
m
response = s.post(uploadurl, data=m, headers={'Content-Type': m.content_type})
print
'------------------------------------------------------'
print
response
print
response.url
print
response.status_code
# print response.content
if response.status_code == 200:
    print
    'deploy success'
else:
    print
    'deploy failed'












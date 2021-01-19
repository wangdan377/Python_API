import requests
import json


header={
    'Authorization':'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1ODgyOTY4OTcsInVzZXJfbmFtZSI6ImlvdF9kZXZlbG9wZXJfdGVzdCIsImF1dGhvcml0aWVzIjpbImRldmVsb3Blcl9Jb1RfZWRnZV9pbnN0YW5jZV9kZXYiLCJwbGF0Zm9ybV91dG1vZGVsX2ZpbmRfZXZlbnQiLCJpb3RhcHBfZGV2aWNlX2RldmVsb3Blcl9vcGVyYXRlIiwicGxhdGZvcm1fdXRtb2RlbF9xdWVyeV9zZXJ2aWNlIiwiZGV2ZWxvcGVyX0lvVF9kZXZpY2VfZGV2IiwicGxhdGZvcm1fdXRtb2RlbF9leHBvcnRfcHJvZmlsZSIsInBsYXRmb3JtX3V0bW9kZWxfbGlzdF9wcm9maWxlX2J5X2tleSIsInBsYXRmb3JtX3V0bW9kZWxfZGV2ZWxvcGVyIiwicGxhdGZvcm1fdXRtb2RlbF9maW5kX3Byb3BlcnR5IiwicGxhdGZvcm1fdXRtb2RlbF91cGRhdGVfc2VydmljZSIsInBsYXRmb3JtX3V0bW9kZWxfZGVsZXRlX3Byb2ZpbGUiLCJwbGF0Zm9ybV91dG1vZGVsX2NyZWF0ZV9wcm9maWxlIiwicGxhdGZvcm1fdXRtb2RlbF9maW5kX3Byb2ZpbGUiLCJpb3RhcHBfZHJpdmVyX2RldmVsb3BlciIsInBsYXRmb3JtX3V0bW9kZWxfZGVsZXRlX2V2ZW50IiwicGxhdGZvcm1fdXRtb2RlbF9maW5kX3NlcnZpY2UiLCJwbGF0Zm9ybV91dG1vZGVsX2xpc3RfcHJvZmlsZSIsInBsYXRmb3JtX3V0bW9kZWxfc2VydmljZW1hbmFnZXIiLCJwbGF0Zm9ybV91dG1vZGVsX2xpc3Rfc2VydmljZSIsImlvdGFwcF9wcm9kdWN0X2RldmVsb3Blcl9yb2xlIiwicGxhdGZvcm1fdXRtb2RlbF9jcmVhdGVfc2VydmljZSIsInBsYXRmb3JtX3V0bW9kZWxfcHJvcGVydHltYW5hZ2VyIiwiZGV2ZWxvcGVyX0lvdF9kcml2ZXJfZGV2IiwicGxhdGZvcm1fdXRtb2RlbF9saXN0X2V2ZW50IiwicGxhdGZvcm1fdXRtb2RlbF91cGRhdGVfcHJvZmlsZSIsInBsYXRmb3JtX3V0bW9kZWxfbGlzdF9wcm9wZXJ0eSIsImlvdGFwcF9kcml2ZXJfZGV2ZWxvcGVyX29wZXJhdGUiLCJwbGF0Zm9ybV91dG1vZGVsX2NyZWF0ZV9wcm9wZXJ0eSIsInBsYXRmb3JtX3V0bW9kZWxfZGVsZXRlX3Byb3BlcnR5IiwiaW90YXBwX2lvdGFwcF9zY3JpcHRfZGV2ZWxvcGVyIiwiZGV2ZWxvcGVyX0lvVF9wcm9kdWN0X2RldiIsImlvdGFwcF9wcm9kdWN0X2RldmVsb3BlciIsImlvdGFwcF9zY3JpcHRfZGV2ZWxvcGVyX29wZXJhdGUiLCJwbGF0Zm9ybV91dG1vZGVsX2NyZWF0ZV9ldmVudCIsImlvdGFwcF9kZXZpY2VfZGV2ZWxvcGVyIiwicGxhdGZvcm1fdXRtb2RlbF9kZWxldGVfc2VydmljZSIsInBsYXRmb3JtX3V0bW9kZWxfcXVlcnlfcHJvZmlsZSIsImlvdGFwcF9lZGdlX2RldmVsb3BlciIsInBsYXRmb3JtX3V0bW9kZWxfcXVlcnlfZXZlbnQiLCJwbGF0Zm9ybV91dG1vZGVsX3VwZGF0ZV9wcm9wZXJ0eSIsImlvdGFwcF9lZGdlX2RldmVsb3Blcl9vcGVyYXRlIiwicGxhdGZvcm1fdXRtb2RlbF91cGRhdGVfZXZlbnQiLCJwbGF0Zm9ybV91dG1vZGVsX3F1ZXJ5X3Byb3BlcnR5IiwicGxhdGZvcm1fdXRtb2RlbF9zZXRfcHJvZmlsZV90YWdzIiwicGxhdGZvcm1fdXRtb2RlbF9ldmVudG1hbmFnZXIiLCJwbGF0Zm9ybV91dG1vZGVsX2ltcG9ydF9wcm9maWxlIiwiZGV2ZWxvcGVyX2lvdF9kZXYiLCJwbGF0Zm9ybV91dG1vZGVsX3Byb2ZpbGVtYW5hZ2VyIl0sImp0aSI6IjA2MTc5Y2M3LWUzYjEtNDMyZS1iODllLWY4YzJiYTgxZDRlNCIsImNsaWVudF9pZCI6InNzby1nYXRld2F5Iiwic2NvcGUiOlsicmVhZCJdfQ.aZTWNmcZPdbQN_DXxzyBjhzic0vtYN187n1z07dBmS8',
    'Content-type':'application/json'
}

for i in range(0,101):
    param={
        "modelId":"5e82f6d9e033900001bf3553",
        "identifier":"apitest_"+str(i),
        "name":"apitest_"+str(i),
        "callType": "async",
        "inputData":[],
        "outputData":[]
    }
    response= requests.post(url='https://mobileuat.utcook.com/utmodel/modelServiceDeveloper/create',headers=header,data=json.dumps(param).encode("utf-8"))
    print(response.text)

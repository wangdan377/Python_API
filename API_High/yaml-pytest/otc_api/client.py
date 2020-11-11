import requests
import json
import allure
from urllib.parse import urlencode
import  time


class HttpClient :
      default_header = {
          "Content-Type":"application/json"
      }
      def send(self,url,body = {},method= 'get',headers = {},sessions = 0,x_token = 0,need_rsp = True):

          headers.update(self.default_header)
          if sessions :
              headers["Session"] = sessions
          if x_token :
              headers["X-Token"] = x_token

          self.create_request_log(url,method,body,headers)

          if method == "get":
              result =  requests.get(url,params = body,headers = headers)
          elif method == "post":
              result =  requests.post(url,data = json.dumps(body),headers=headers)
          elif method == "patch":
              result = requests.patch(url,data = json.dumps(body),headers=headers)

          if not need_rsp:
              return

          self.create_response_log(result.status_code,result.text)

          return {"status_code":result.status_code,"data":result.json()}

      def get_full_url(self,url,etc= {},replace = {},h=""):
          if h:
              host = h.rstrip('/')
          else:
              host = self.host.rstrip('/')

          url = url.lstrip('/')
          full_url = host + "/" + url
          full_url += "?platform=apitest&time=" + str(int(round(time.time() * 1000)))
          if len(etc):
              s = urlencode(etc)
              full_url += "&" +s
          if len(replace):
              full_url = str.format(full_url,*replace)
          return full_url

      @allure.step("请求日志")
      def create_request_log(self,url,method,body,header):
          pass
      @allure.step('响应日志')
      def create_response_log(self,status_code,body):
          pass

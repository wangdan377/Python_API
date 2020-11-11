import requests
import json
from API_service.Common import Log
from API_service.Conf import Config


class Get:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.Log()

    #only headers
    def get_model_a(self,session_a,url):
        #headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0", "X-ZY-Production": "zycami"}
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
                   "X-ZY-Platform": "android"}

        res = session_a.get(url, headers = headers)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict

    #headers +params
    def get_model_b(self,session_b,url,params):
        #headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
        #           "X-ZY-Production": "zycami", "X-ZY-Platform": "ios", "X-ZY-Version": "1.0.15",, "X-ZY-key": "mz8GveqAXo5jbPOfPfsIwQ=="}
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
        res = session_b.get(url, headers = headers, params = params)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict

    #add sessionId to cookies
    def get_model_c(self,session_c,url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}

        c = requests.cookies.RequestsCookieJar()
        #自定义设置键值对
        c.set('session_name','session_value')
        session_c.cookies.update(c)
        cookies = session_c.cookies

        res = session_c.get(url,headers = headers,cookies = cookies)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict

    #add token to cookies
    def get_model_d(self,session_d,url,token_name,token_value):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}

        c = requests.cookies.RequestsCookieJar()
        #自定义设置键值对
        c.set(token_name, token_value)
        session_d.cookies.update(c)
        cookies = session_d.cookies

        res = session_d.get(url,headers = headers,cookies = cookies)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict

    #add sessionId to cookie +params
    def get_model_e(self,session_e,url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
        #自定义设置键值对
        params = {'username': hu, 'password':123456}

        c = requests.cookies.RequestsCookieJar()
        #自定义设置键值对
        c.set('session_name', 'session_value')
        session_e.cookies.update(c)
        cookies = session_e.cookies

        res = session_e.get(url,headers = headers,cookies = cookies ,params = params)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict

    #add token to cookies +params
    def get_model_f(self,session_f,url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
        #自定义设置键值对
        params = {'username': 'hu', 'password': 123456}

        c = requests.cookies.RequestsCookieJar()
        #自定义设置键值对
        c.set('token_name', 'token_value')
        session_f.cookies.update(c)
        cookies = session_f.cookies

        res = session_f.get(url,headers = headers,cookies = cookies ,params = params)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict


if __name__ == '__main__':
    myGet = Get()
    session_a = requests.session()
    res = myGet.get_model_a(session_a, 'https://www.baidu.com')
    print(res)


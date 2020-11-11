import requests
import json
from API_service.Common import Log
from API_service.Conf import Config


class Post:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.Log()


    # only headers
    def post_model_a(self, session_a, url):
        #headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0", "X-ZY-Production": "zycami"}
        #headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
        #           "Content-Type": "application/json"}
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0", "X-ZY-Production": "zycami"}
        res = session_a.post(url, headers = headers)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict


    # headers + params
    def post_model_b(self, session_b, url, params):
        #headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0", "X-ZY-Production": "zycami"}
        #headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0", "X-ZY-Production": "zyplay",
        #           "X-ZY-Platform": "ios", "X-ZY-Version": "1.0.8"}

        #headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
        #           "X-ZY-Production": "zycami", "X-ZY-Platform": "ios", "X-ZY-Version": "1.0.15",'X-ZY-key':'mz8GveqAXo5jbPOfPfsIwQ=='}

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
                   "Content-Type": "application/x-www-form-urlencoded"}

        res = session_b.post(url, headers = headers, data = params)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict


    # add sessionID to cookie
    def post_model_c(self, session_c, url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}

        c = requests.cookies.RequestsCookieJar()
        c.set('session_name', 'session_value')
        session_c.cookies.update(c)
        cookies = session_c.cookies

        res = session_c.post(url, headers = headers, cookies = cookies)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict


    # add token to cookie
    def post_model_d(self, session_d, url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}

        c = requests.cookies.RequestsCookieJar()
        c.set('token_name', 'token_value')
        session_c.cookies.update(c)
        cookies = session_c.cookies

        res = session_d.post(url, headers = headers, cookies = cookies)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict


    # add sessionID to cookie +params
    def post_model_e(self, session_e, url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
        params = {'username': hu, 'password': 123456}

        c = requests.cookies.RequestsCookieJar()
        c.set('session_name', 'session_value')
        session_c.cookies.update(c)
        cookies = session_c.cookies

        res = session_e.post(url, headers = headers, cookies = cookies, data = params)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict


    # add token to cookie +params
    def post_model_f(self, session_f, url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
        params = {'username': hu, 'password': 123456}

        c = requests.cookies.RequestsCookieJar()
        c.set('token_name', 'token_value')
        session_c.cookies.update(c)
        cookies = session_c.cookies

        res = session_f.post(url, headers = headers, cookies = cookies, data = params)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict


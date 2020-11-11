import requests
import json
from Common import Log
from Conf import Config


class Put:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.Log()

    # only headers
    def put_model_a(self, session_a, url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}

        res = session_a.put(url, headers = headers)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict

    # headers +params
    def put_model_b(self, session_b, url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
        params = {'username': hu, 'password': 123456}
        res = session_b.put(url, headers = headers, data = params)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict

    # add sessionID to cookie
    def put_model_c(self, session_c, url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}

        c = requests.cookies.RequestsCookieJar()
        c.set('session_name', 'session_value')
        session_c.cookies.update(c)
        cookies = session_c.cookies

        res = session_c.put(url, headers = headers, cookies = cookies)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict

    # add token to cookie
    def put_model_d(self, session_d, url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}

        c = requests.cookies.RequestsCookieJar()
        c.set('token_name', 'token_value')
        session_c.cookies.update(c)
        cookies = session_c.cookies

        res = session_d.put(url, headers = headers, cookies = cookies)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict

    # add sessionID to cookie +params
    def put_model_e(self, session_e, url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
        params = {'username': hu, 'password': 123456}

        c = requests.cookies.RequestsCookieJar()
        c.set('session_name', 'session_value')
        session_c.cookies.update(c)
        cookies = session_c.cookies

        res = session_e.put(url, headers = headers, cookies = cookies, data = params)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict

    # add token to cookie +params
    def put_model_f(self, session_f, url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
        params = {'username': hu, 'password': 123456}

        c = requests.cookies.RequestsCookieJar()
        c.set('token_name', 'token_value')
        session_c.cookies.update(c)
        cookies = session_c.cookies

        res = session_f.put(url, headers = headers, cookies = cookies, data = params)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict


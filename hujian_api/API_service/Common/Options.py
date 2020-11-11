import requests
import json
from Common import Log
from Conf import Config


class Options:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.Log()


    #only headers
    def options_model_a(self,session_a,url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}

        res = session_a.options(url,headers = headers)
        res_dict = dict()
        res_dict['code'] = res.status_code
        res_dict['text'] = res.text

        return res_dict


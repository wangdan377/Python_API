from configparser import ConfigParser
from API_service.Common import Log
import os

class Config:
    TITLE_DEBUG = 'debug'
    TITLE_RELEASE = 'release'
    TITLE_EMAIL = 'email'

    VALUE_ENVIRONMENT = 'environment'
    VALUE_VERSION_CODE = 'versionCode'
    VALUE_CODER = 'coder'
    VALUE_HOST = 'host'
    VALUE_LOGIN_HOST = 'loginHost'
    VALUE_API_HOST = 'apiHost'
    VALUE_API_LOGIN_HOST = 'apiLoginHost'
    VALUE_LOGIN_INFO = 'loginInfo'

    VALUE_SMTP_SERVER = 'smtpserver'
    VALUE_SENDER = 'sender'
    VALUE_USERNAME = 'username'
    VALUE_PASSWORD = 'password'
    VALUE_RECEIVER = 'receiver'

    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        self.config = ConfigParser()
        self.log = Log.Log()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.xml_report_path = Config.path_dir+'/Report/xml'
        self.html_report_path = Config.path_dir+'/Report/html'

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError('请注意！NO config.ini文件.')

        self.config.read(self.conf_path, encoding='utf-8')


        self.environment_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_ENVIRONMENT)
        self.versionCode_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_VERSION_CODE)
        self.coder_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_CODER)
        self.host_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_HOST)
        self.loginHost_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_HOST)
        self.apiHost_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_API_HOST)
        self.apiLoginHost_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_API_LOGIN_HOST)
        self.loginInfo_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_INFO)


        self.environment_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_ENVIRONMENT)
        self.versionCode_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_VERSION_CODE)
        self.coder_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_CODER)
        self.host_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_HOST)
        self.loginHost_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_LOGIN_HOST)
        self.apiHost_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_API_HOST)
        self.apiLoginHost_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_API_LOGIN_HOST)
        self.loginInfo_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_LOGIN_INFO)



        self.smtpserver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SMTP_SERVER)
        self.sender = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SENDER)
        self.username = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_USERNAME)
        self.password = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_PASSWORD)
        self.receiver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_RECEIVER)

    def get_conf(self, title, value):
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)



    def add_conf(self, title):
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

if __name__ == "__main__":
    testConfig = Config()
    print(testConfig.path_dir)
    print(testConfig.conf_path)

    print(testConfig.environment_debug)
    print(testConfig.versionCode_debug)
    print(testConfig.coder_debug)
    print(testConfig.host_debug)
    print(testConfig.loginHost_debug)
    print(testConfig.apiHost_debug)
    print(testConfig.apiLoginHost_debug)
    print(testConfig.loginInfo_debug)

    print(testConfig.environment_release)
    print(testConfig.versionCode_release)
    print(testConfig.coder_release)
    print(testConfig.host_release)
    print(testConfig.loginHost_release)
    print(testConfig.apiHost_release)
    print(testConfig.apiLoginHost_release)
    print(testConfig.loginInfo_release)

    print(testConfig.smtpserver)
    print(testConfig.sender)
    print(testConfig.username)
    print(testConfig.password)
    print(testConfig.receiver)





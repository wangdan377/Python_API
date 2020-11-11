import requests
import json
from Common import Log
from Conf import Config

class SessionAndToken:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.Log()
        self.optionsSession = requests.session()
        self.postSession = requests.session()
        self.homeSession = requests.session()


    def getSessionAndToken(self):

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
        post_login_url = 'http://172.16.2.101:3000/v1/login'
        home_url = 'http://172.16.2.101:8000'
        params = {'username': '13418483933@139.com', 'password': '12345678'}

        listCookies = []
        listSessionAndToken = []

        #options cookie

        re = self.optionsSession.options(post_login_url)
        listCookies.append(re.cookies)

        #login cookie
        res = self.postSession.post(post_login_url, data=params, headers=headers)
        listCookies.append(res.cookies)
        listCookies.append(res.cookies)

        #options session
        reOptionsCookies = listCookies[0]
        reOptionsSession = reOptionsCookies['sid']
        listSessionAndToken.append(reOptionsSession)


        #login session
        resPostCookies = listCookies[1]
        rePostSession = resPostCookies['sid']
        listSessionAndToken.append(rePostSession)
        #listCookies = listCookies[2]


        #login token
        resJson = res.json()
        resToken = resJson['token']
        ###resID = resJson['id']
        ###print(resID)
        listSessionAndToken.append(resToken)


        #home session
        resHome = self.homeSession.get(home_url, headers=headers)
        resCookies = resHome.cookies
        resSession = resCookies['sid']
        listSessionAndToken.append(resSession)

        #option session,login session,login token,home session

        res.text = resPostCookies

        return listSessionAndToken
        #resCount = listSessionAndToken


if __name__ == '__main__':
    sessionToken = SessionAndToken()
    #print(sessionToken.optionsSession)
    print(sessionToken.getSessionAndToken())



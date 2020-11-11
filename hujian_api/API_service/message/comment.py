import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts

from message.login import off_login


class Comment:
#userId_S评论postId_M
    def Off_comment(self,postId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/share/comment/add'
        params = {'token':'12345678901234567890123456789012', 'postId':'1', 'content':'好看好看'}

        tokenData = off_login()

        params['token'] = tokenData
        params['postId'] = str(postId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#userId_S删除评论commentId_M
    def Off_delcomment(self,commentId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/share/comment/del'
        params = {'token':'12345678901234567890123456789012', 'id':'1'}

        tokenData = off_login()

        params['token'] = tokenData
        params['postId'] = str(commentId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

if __name__ =="__main__":
    test = Comment()
    test.Off_comment(304783)


import pymysql

class GetMysqlData:
    def getUserIdByMail(self,mail):
        # 打开数据库连接（ip/port/数据库用户名/登录密码/数据库名）
        db = pymysql.connect(host='172.16.2.101', port=3306, user='root', passwd='root', db='zy')
        # 使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 使用execute方法执行SQL语句
        cursor.execute('SELECT zy.user.id FROM zy.user WHERE zy.user.mail=%s',(mail))

        # 使用fetchone()方法获取一条数据
        userIdList = cursor.fetchone()
        userId = userIdList[0]
        db.close()
        return userId

    def getUserIdByMobile(self,mobile):
        # 打开数据库连接（ip/port/数据库用户名/登录密码/数据库名）
        db = pymysql.connect(host='172.16.2.101', port=3306, user='root', passwd='root', db='zy')
        # 使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 使用execute方法执行SQL语句
        cursor.execute('SELECT zy.user.id FROM zy.user WHERE zy.user.mobile=%s',(mobile))

        # 使用fetchone()方法获取一条数据
        userIdList = cursor.fetchone()
        userId = userIdList[0]

        db.close()
        return userId

    def getTokenByUserId(self,userId):
        #打开数据库连接（ip/port/数据库用户名/登录密码/数据库名）
        db = pymysql.connect(host = '172.16.2.101',port = 3306,user = 'root',passwd = 'root',db = 'zy')
        #使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        #使用execute方法执行SQL语句
        cursor.execute('SELECT zy.user_token.token FROM zy.user_token WHERE zy.user_token.userId=%s ORDER BY zy.user_token.createAt DESC',(userId))

        #使用fetchone()方法获取一条数据
        tokenList = cursor.fetchone()
        token = tokenList[0]

        db.close()
        return token


#已发布postId
    def getPostId(self,userId,title):
        #打开数据库连接（ip/port/数据库用户名/登录密码/数据库名）
        db = pymysql.connect(host = '172.16.2.101',port = 3306,user = 'root',passwd = 'root',db = 'zy')
        #使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        #使用execute方法执行SQL语句
        cursor.execute('SELECT zy.share_post.id FROM zy.share_post WHERE zy.share_post.userId=%s and zy.share_post.title=%s ORDER BY zy.share_post.createAt DESC',(userId,title))

        #使用fetchone()方法获取一条数据
        postIdList = cursor.fetchone()
        postId = postIdList[0]

        db.close()
        return postId

#最新已发布postId
    def getPostId_new(self,userId):
        #打开数据库连接（ip/port/数据库用户名/登录密码/数据库名）
        db = pymysql.connect(host = '172.16.2.101',port = 3306,user = 'root',passwd = 'root',db = 'zy')
        #使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        #使用execute方法执行SQL语句
        cursor.execute('SELECT zy.share_post.id FROM zy.share_post WHERE zy.share_post.userId=%s and zy.share_post.title IS NOT NULL ORDER BY zy.share_post.createAt DESC',(userId))

        #使用fetchone()方法获取一条数据
        postIdList = cursor.fetchone()
        postId = postIdList[0]

        db.close()
        return postId

#未发布postId
    def getPostId_none(self,userId):
        #打开数据库连接（ip/port/数据库用户名/登录密码/数据库名）
        db = pymysql.connect(host = '172.16.2.101',port = 3306,user = 'root',passwd = 'root',db = 'zy')
        #使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        #使用execute方法执行SQL语句
        cursor.execute('SELECT zy.share_post.id FROM zy.share_post WHERE zy.share_post.userId=%s and zy.share_post.title IS NULL ORDER BY zy.share_post.createAt DESC',(userId))

        #使用fetchone()方法获取一条数据
        postIdList = cursor.fetchone()
        postId = postIdList[0]

        db.close()
        return postId

    def getCommentId(self,userId_from,postId_to,content):
        #打开数据库连接（ip/port/数据库用户名/登录密码/数据库名）
        db = pymysql.connect(host = '172.16.2.101',port = 3306,user = 'root',passwd = 'root',db = 'zy')
        #使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        #使用execute方法执行SQL语句
        cursor.execute('SELECT zy.share_post_comment.id FROM zy.share_post_comment WHERE zy.share_post_comment.postId=%s and zy.share_post_comment.userId=%s and zy.share_post_comment.content=%s',(postId_to,userId_from,content))

        #使用fetchone()方法获取一条数据
        commentIdList = cursor.fetchone()
        commentId = commentIdList[0]

        db.close()
        return commentId

    def getReplyId(self,commentId,userId,content):
        #打开数据库连接（ip/port/数据库用户名/登录密码/数据库名）
        db = pymysql.connect(host = '172.16.2.101',port = 3306,user = 'root',passwd = 'root',db = 'zy')
        #使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        #使用execute方法执行SQL语句
        cursor.execute('SELECT zy.share_post_reply.id FROM zy.share_post_reply WHERE zy.share_post_reply.commentId=%s and zy.share_post_reply.userId=%s and zy.share_post_reply.content=%s',(commentId,userId,content))

        #使用fetchone()方法获取一条数据
        replyIdList = cursor.fetchone()
        replyId = replyIdList[0]

        db.close()
        return replyId

    def getCircleId(self,name):
        #打开数据库连接（ip/port/数据库用户名/登录密码/数据库名）
        db = pymysql.connect(host = '172.16.2.101',port = 3306,user = 'root',passwd = 'root',db = 'zy')
        #使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        #使用execute方法执行SQL语句
        cursor.execute('SELECT zy.circle.id FROM zy.circle WHERE zy.circle.name=%s',(name))

        #使用fetchone()方法获取一条数据
        circleIdList = cursor.fetchone()
        circleId = circleIdList[0]

        db.close()
        return circleId

    def getCircleArtId(self,circleId,title):
        #打开数据库连接（ip/port/数据库用户名/登录密码/数据库名）
        db = pymysql.connect(host = '172.16.2.101',port = 3306,user = 'root',passwd = 'root',db = 'zy')
        #使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        #使用execute方法执行SQL语句
        cursor.execute('SELECT zy.circle_article.id FROM zy.circle_article WHERE zy.circle_article.circleId=%s and zy.circle_article.title=%s',(circleId,title))

        #使用fetchone()方法获取一条数据
        circleArtIdList = cursor.fetchone()
        circleArtId = circleArtIdList[0]

        db.close()
        return circleArtId

    def getCircleCommentId(self,workId,content):
        #打开数据库连接（ip/port/数据库用户名/登录密码/数据库名）
        db = pymysql.connect(host = '172.16.2.101',port = 3306,user = 'root',passwd = 'root',db = 'zy')
        #使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        #使用execute方法执行SQL语句
        cursor.execute('SELECT zy.circle_comment.id FROM zy.circle_comment WHERE zy.circle_comment.workId=%s and zy.circle_comment.commentWords=%s',(workId,content))

        #使用fetchone()方法获取一条数据
        circleCommentIdList = cursor.fetchone()
        circleCommentId = circleCommentIdList[0]

        db.close()
        return circleCommentId









if __name__ == '__main__':
    a = GetMysqlData()
    print(a.getCircleCommentId(2,'我就是个评论2'))
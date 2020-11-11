import pymysql

class GetShareData:
    #播放排行--在所选时间段内，根据作品播放量的多少排行
    def getPVRanking(self):
        #打开数据库连接（ip/port/登陆用户名/登录密码/数据库名）
        db = pymysql.connect(host = '172.16.2.101', port = 3306, user = 'root', passwd = 'root', db = 'zy')
        #使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        #使用execute方法执行SQL语句
        cursor.execute("SELECT zy.`share_post`.`id`, zy.`share_post`.`pv` FROM zy.`share_post` WHERE zy.`share_post`.`status` = 1 ORDER BY zy.`share_post`.`pv` DESC LIMIT 50")

        #使用fetchone()方法获取一条数据
        dataList = cursor.fetchall()

        db.close()
        return dataList


    #点赞排行
    def getLikeRanking(self):
        #打开数据库连接（ip/port/登陆用户名/登录密码/数据库名）
        db = pymysql.connect(host = '172.16.2.101', port = 3306, user = 'root', passwd = 'root', db = 'zy')
        #使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        #使用execute方法执行SQL语句
        cursor.execute("SELECT zy.`share_post`.`id`, zy.`share_post`.`likeCnt` FROM zy.`share_post` WHERE zy.`share_post`.`status` = 1 ORDER BY zy.`share_post`.`likeCnt` DESC LIMIT 50")

        #使用fetchone()方法获取一条数据
        dataList = cursor.fetchall()

        db.close()
        return dataList


    #评论排行--在所选时间段内，根据作品评论量的多少排行
    def getCommentRanking(self):
        #打开数据库连接（ip/port/登陆用户名/登录密码/数据库名）
        db = pymysql.connect(host = '172.16.2.101', port = 3306, user = 'root', passwd = 'root', db = 'zy')
        #使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        #使用execute方法执行SQL语句
        cursor.execute("SELECT temp.postId, COUNT(temp.postId) AS number FROM (SELECT * FROM zy.share_post_comment WHERE (zy.share_post_comment.createAt = zy.share_post_comment.updateAt AND zy.share_post_comment.createAt >= '2019-04-01 19:00:00' AND zy.share_post_comment.createAt <= '2019-04-08 19:00:00' AND zy.share_post_comment.status = 1)\
                        UNION SELECT * FROM zy.share_post_comment WHERE (zy.share_post_comment.createAt >= '2019-04-01 19:00:00' AND zy.share_post_comment.updateAt >= '2019-04-08 19:00:00')) AS temp\
                        GROUP BY temp.postId ORDER BY number DESC")

        #使用fetchone()方法获取一条数据
        dataList = cursor.fetchall()

        db.close()
        return dataList


    #分享排行
    def getShareRanking(self):
        #打开数据库连接（ip/port/登陆用户名/登录密码/数据库名）
        db = pymysql.connect(host = '172.16.2.101', port = 3306, user = 'root', passwd = 'root', db = 'zy')
        #使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        #使用execute方法执行SQL语句
        cursor.execute("SELECT zy.`share_post`.`id`, zy.`share_post`.`shareCnt` FROM zy.`share_post` WHERE zy.`share_post`.`status` = 1 ORDER BY zy.`share_post`.`shareCnt` DESC LIMIT 50")

        #使用fetchone()方法获取一条数据
        dataList = cursor.fetchall()

        db.close()
        return dataList


    #综合分值排行
    def getScoreRanking(self):
        #打开数据库连接（ip/port/登陆用户名/登录密码/数据库名）
        db = pymysql.connect(host = '172.16.2.101', port = 3306, user = 'root', passwd = 'root', db = 'zy')
        #使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        #使用execute方法执行SQL语句
        cursor.execute("SELECT zy.`share_post`.id, (zy.`share_post`.`pv`*0.14+zy.`share_post`.`likeCnt`*0.48+zy.`share_post`.`commentCnt`*0.32+zy.share_post.`shareCnt`*0.06) AS score FROM zy.`share_post` WHERE zy.`share_post`.`status` = 1 ORDER BY score DESC LIMIT 50")

        #使用fetchone()方法获取一条数据
        dataList = cursor.fetchall()

        db.close()
        return dataList



if __name__ == '__main__':
    a = GetShareData()
    print(a.getCommentRanking())

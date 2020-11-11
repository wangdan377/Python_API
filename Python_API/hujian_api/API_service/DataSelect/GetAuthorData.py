import pymysql

class GetAuthorData:
    #人气排行--在所选时间段内，粉丝增长数量排行
    def getFansIncRanking(self,time_L,time_S):
        #打开数据库连接（ip/port/登陆用户名/登录密码/数据库名）
        db = pymysql.connect(host = '172.16.2.101', port = 3306, user = 'root', passwd = 'root', db = 'zy')
        #使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()


        #使用execute方法执行SQL语句
        cursor.execute("SELECT E.to_a AS uer, (ifnull(E.number_a,0)-ifnull(E.number_b,0)) AS inc FROM\
                        (SELECT A.to_a, A.number_a, B.number_b FROM\
                        (SELECT temp_a.to AS to_a, COUNT(temp_a.to) AS number_a FROM (SELECT * FROM zy.user_follow WHERE (zy.user_follow.createAt < %s AND zy.user_follow.updateAt > %s) UNION SELECT * FROM zy.user_follow WHERE (zy.user_follow.createAt < %s AND zy.user_follow.updateAt < %s AND zy.user_follow.status = 1)) AS temp_a GROUP BY to_a ORDER BY number_a DESC) AS A\
                        LEFT JOIN\
                        (SELECT temp_b.to AS to_b, COUNT(temp_b.to) AS number_b FROM (SELECT * FROM zy.user_follow WHERE (zy.user_follow.createAt < %s AND zy.user_follow.updateAt > %s) UNION SELECT * FROM zy.user_follow WHERE (zy.user_follow.createAt < %s AND zy.user_follow.updateAt < %s AND zy.user_follow.status = 1)) AS temp_b GROUP BY to_b ORDER BY number_b DESC) AS B\
                        ON A.to_a = B.to_b\
                        UNION\
                        SELECT C.to_a, C.number_a, D.number_b FROM\
                        (SELECT temp_a.to AS to_a, COUNT(temp_a.to) AS number_a FROM (SELECT * FROM zy.user_follow WHERE (zy.user_follow.createAt < %s AND zy.user_follow.updateAt > %s) UNION SELECT * FROM zy.user_follow WHERE (zy.user_follow.createAt < %s AND zy.user_follow.updateAt < %s AND zy.user_follow.status = 1)) AS temp_a GROUP BY to_a ORDER BY number_a DESC) AS C\
                        RIGHT JOIN\
                        (SELECT temp_b.to AS to_b, COUNT(temp_b.to) AS number_b FROM (SELECT * FROM zy.user_follow WHERE (zy.user_follow.createAt < %s AND zy.user_follow.updateAt > %s) UNION SELECT * FROM zy.user_follow WHERE (zy.user_follow.createAt < %s AND zy.user_follow.updateAt < %s AND zy.user_follow.status = 1)) AS temp_b GROUP BY to_b ORDER BY number_b DESC) AS D\
                        ON C.to_a = D.to_b) AS E\
                        ORDER BY inc DESC",(time_L,time_L,time_L,time_L,time_S,time_S,time_S,time_S,time_L,time_L,time_L,time_L,time_S,time_S,time_S,time_S))

        #使用fetchone()方法获取一条数据
        dataList = cursor.fetchall()


        db.close()
        return dataList


    #优质创作排行--在所选时间段内，根据用户作品的质量分排行
    def getCommentRanking(self):
        #打开数据库连接（ip/port/登陆用户名/登录密码/数据库名）
        db = pymysql.connect(host = '172.16.2.101', port = 3306, user = 'root', passwd = 'root', db = 'zy')
        #使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标

        cursor = db.cursor()
        #使用execute方法执行SQL语句


        cursor.execute("SELECT zy.`share_post`.`id`, zy.`share_post`.`commentCnt` FROM zy.`share_post` WHERE zy.`share_post`.`status` = 1 ORDER BY zy.`share_post`.`commentCnt` DESC LIMIT 50")
        #cursor.execute("select zy.'share_post','id', zy.share_post.commentcnt from zy.share_post where zy.share_post.status = 1 order by zy.share_post.commentcnt desc Limit 50))
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
        #方法执行SQL语句
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
    a = GetData()
    print(a.getFansIncRanking('2020-04-07 19:00:00','2019-04-07 19:00:00'))




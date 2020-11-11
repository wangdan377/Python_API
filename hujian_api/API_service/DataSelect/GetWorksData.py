import pymysql

class GetWorksData:
    #今日新增作品--全部平台、ZYPlay、莱塔社、Z-Film
    def get_works_inc_today(self,platform):
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


    #今日新增作品--周同比--全部平台、ZYPlay、莱塔社、Z-Film
    def get_works_inc_today_weekOnWeek(self,platform):
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


    #今日新增作品--日环比--全部平台、ZYPlay、莱塔社、Z-Film
    def get_works_inc_today_dayOnDay(self, platform):
        # 打开数据库连接（ip/port/登陆用户名/登录密码/数据库名）
        db = pymysql.connect(host='172.16.2.101', port=3306, user='root', passwd='root', db='zy')
        # 使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 使用execute方法执行SQL语句
        cursor.execute("SELECT zy.`share_post`.`id`, zy.`share_post`.`pv` FROM zy.`share_post` WHERE zy.`share_post`.`status` = 1 ORDER BY zy.`share_post`.`pv` DESC LIMIT 50")

        # 使用fetchone()方法获取一条数据
        dataList = cursor.fetchall()

        db.close()
        return dataList


    #本周累计新增作品（start周日）--全部平台、ZYPlay、莱塔社、Z-Film
    def get_works_inc_thisWeek(self,platform):
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


    #本周累计新增作品（start周日）--月同比--全部平台、ZYPlay、莱塔社、Z-Film
    def get_works_inc_thisWeek_monthOnMonth(self,platform):
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


    #本周累计新增作品（start周日）--周环比--全部平台、ZYPlay、莱塔社、Z-Film
    def get_works_inc_week_weekOnWeek(self, platform):
        # 打开数据库连接（ip/port/登陆用户名/登录密码/数据库名）
        db = pymysql.connect(host='172.16.2.101', port=3306, user='root', passwd='root', db='zy')
        # 使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 使用execute方法执行SQL语句
        cursor.execute(
            "SELECT zy.`share_post`.`id`, zy.`share_post`.`likeCnt` FROM zy.`share_post` WHERE zy.`share_post`.`status` = 1 ORDER BY zy.`share_post`.`likeCnt` DESC LIMIT 50")

        # 使用fetchone()方法获取一条数据
        dataList = cursor.fetchall()

        db.close()
        return dataList


    #本月累计新增作品（start 1号）--全部平台、ZYPlay、莱塔社、Z-Film
    def get_works_inc_month(self):
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


    #本月累计新增作品（start 1号）--年同比--全部平台、ZYPlay、莱塔社、Z-Film
    def get_works_inc_month_yearOnYear(self,platform):
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


    #本月累计新增作品（start 1号）--月环比--全部平台、ZYPlay、莱塔社、Z-Film
    def get_works_inc_month_monthOnMonth(self,platform):
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


    #本月累计新增作品（start 1号）--月环比--全部平台、ZYPlay、莱塔社、Z-Film
    def get_works_inc_month_monthOnMonth(self,platform):
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







if __name__ == '__main__':
    a = GetShareData()
    print(a.getCommentRanking())

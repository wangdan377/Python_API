import pymysql

class GetUserData:
    #今日新增用户-iOS，包括注册和访客--全部平台、ZYPlay、莱塔社、Z-Film, flag = 1
    def get_iOSUser_inc_today(self,platform,time_S,time_E):
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


    #今日新增注册用户-iOS--全部平台、ZYPlay、莱塔社、Z-Film, flag = 2
    def get_iOSReg_inc_today(self,platform,time_S,time_E):
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


    #今日新增访客-iOS--全部平台、ZYPlay、莱塔社、Z-Film, flag = 3
    def get_iOSGuest_inc_today(self,platform,time_S,time_E):
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


    #今日活跃-iOS,平台--全部平台、ZYPlay、莱塔社、Z-Film, flag = 4
    def get_iOSActUser_number_today(self,platform,time_S,time_E):
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


    #今日Android新增用户，包括注册和访客,全部平台、ZYPlay、莱塔社、Z-Film, flag = 5
    def get_AndroidUser_inc_today(self,platform,time_S,time_E):
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


    #今日Android新增注册用户,全部平台、ZYPlay、莱塔社、Z-Film, flag = 6
    def get_AndroidReg_inc_today(self,platform,time_S,time_E):
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


    #今日Android新增访客,全部平台、ZYPlay、莱塔社、Z-Film, flag = 7
    def get_AndroidGuest_inc_today(self,platform,time_S,time_E):
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


    #今日Android活跃用户,全部平台、ZYPlay、莱塔社、Z-Film,flag = 8
    def get_AndroidActUser_number_today(self,platform,time_S,time_E):
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


    #周同比--与上周的同一天相比的增长率
    def get_WeekOnWeek(self, flag, cur, last):
        if flag == 1:
            curNumber1 = self.get_iOSUser_inc_today('本周')
            lastNumber1 = self.get_iOSUser_inc_today('上周')
            percent1 = format((curNumber1 - lastNumber1) / lastNumber1, '.0%')
            return percent1

        if flag == 2:
            curNumber2 = self.get_iOSReg_inc_today('本周')
            lastNumber2 = self.get_iOSReg_inc_today('上周')
            percent2 = format((curNumber2 - lastNumber2) / lastNumber2, '.0%')
            return percent2

        if flag == 3:
            curNumber3 = self.get_iOSGuest_inc_today('本周')
            lastNumber3 = self.get_iOSGuest_inc_today('上周')
            percent3 = format((curNumber3 - lastNumber3) / lastNumber3, '.0%')
            return percent3

        if flag == 4:
            curNumber4 = self.get_iOSActUser_number_today('本周')
            lastNumber4 = self.get_iOSActUser_number_today('上周')
            percent4 = format((curNumber4 - lastNumber4) / lastNumber4, '.0%')
            return percent4

        if flag == 5:
            curNumber5 = self.get_AndroidUser_inc_today('本周')
            lastNumber5 = self.get_AndroidUser_inc_today('上周')
            percent5 = format((curNumber5 - lastNumber5) / lastNumber5, '.0%')
            return percent5

        if flag == 6:
            curNumber6 = self.get_AndroidReg_inc_today('本周')
            lastNumber6 = self.get_AndroidReg_inc_today('上周')
            percent6 = format((curNumber6 - lastNumber6) / lastNumber6, '.0%')
            return percent6

        if flag == 7:
            curNumber7 = self.get_AndroidGuest_inc_today('本周')
            lastNumber7 = self.get_AndroidGuest_inc_today('上周')
            percent7 = format((curNumber7 - lastNumber7) / lastNumber7, '.0%')
            return percent7

        if flag == 8:
            curNumber8 = self.get_AndroidActUser_number_today('本周')
            lastNumber8 = self.get_AndroidActUser_number_today('上周')
            percent8 = format((curNumber8 - lastNumber8) / lastNumber8, '.0%')
            return percent8


    #日环比,全部平台、ZYPlay、莱塔社、Z-Film
    def get_dayOnDay(self, flag, today, yesterday):
        if flag == 1:
            todayNumber1 = self.get_iOSUser_inc_today('今天')
            yesterdayNumber1 = self.get_iOSUser_inc_today('昨天')
            percent1 = format((todayNumber1 - yesterdayNumber1) / yesterdayNumber1, '.0%')
            return percent1

        if flag == 2:
            todayNumber2 = self.get_iOSReg_inc_today('今天')
            yesterdayNumber2 = self.get_iOSReg_inc_today('昨天')
            percent2 = format((todayNumber2 - yesterdayNumber2) / yesterdayNumber2, '.0%')
            return percent2

        if flag == 3:
            todayNumber3 = self.get_iOSGuest_inc_today('今天')
            yesterdayNumber3 = self.get_iOSGuest_inc_today('昨天')
            percent3 = format((todayNumber3 - yesterdayNumber3) / yesterdayNumber3, '.0%')
            return percent3

        if flag == 4:
            todayNumber4 = self.get_iOSActUser_number_today('今天')
            yesterdayNumber4 = self.get_iOSActUser_number_today('昨天')
            percent4 = format((todayNumber4 - yesterdayNumber4) / yesterdayNumber4, '.0%')
            return percent4

        if flag == 5:
            todayNumber5 = self.get_AndroidUser_inc_today('今天')
            yesterdayNumber5 = self.get_AndroidUser_inc_today('昨天')
            percent5 = format((todayNumber5 - yesterdayNumber5) / yesterdayNumber5, '.0%')
            return percent5

        if flag == 6:
            todayNumber6 = self.get_AndroidReg_inc_today('今天')
            yesterdayNumber6 = self.get_AndroidReg_inc_today('昨天')
            percent6 = format((todayNumber6 - yesterdayNumber6) / yesterdayNumber6, '.0%')
            return percent6

        if flag == 7:
            todayNumber7 = self.get_AndroidGuest_inc_today('今天')
            yesterdayNumber7 = self.get_AndroidGuest_inc_today('昨天')
            percent7 = format((todayNumber7 - yesterdayNumber7) / yesterdayNumber7, '.0%')
            return percent7

        if flag == 8:
            todayNumber8 = self.get_AndroidActUser_number_today('今天')
            yesterdayNumber8 = self.get_AndroidActUser_number_today('昨天')
            percent8 = format((todayNumber8 - yesterdayNumber8) / yesterdayNumber8, '.0%')
            return percent8


    #注册用户数
    def get_userReg_number(self):
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


    #iOS活跃用户占注册用户数百分比
    def get_iOSAct_percent(self):
        iOSAct = self.get_iOSActUser_number_today('当前')
        userReg = self.get_userReg_number()
        percent = format(iOSAct / userReg, '.0%')
        return percent


    #Android活跃用户占注册用户数百分比
    def get_AndroidAct_percent(self):
        AndroidAct = self.get_AndroidActUser_number_today('当前')
        userReg = self.get_userReg_number()
        percent = format(AndroidAct / userReg, '.0%')
        return percent


#新增用户
#新增用户
#新增用户--最近7天，最近30天，自定义时间段
    #自定义时间段--新增用户，包括注册和访客
    def get_user_inc_anytime(self,time_S,time_E):
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

    #自定义时间段--新增用户iOS，包括注册和访客
    def get_userIOS_inc_anytime(self, time_S, time_E):
        # 打开数据库连接（ip/port/登陆用户名/登录密码/数据库名）
        db = pymysql.connect(host='172.16.2.101', port=3306, user='root', passwd='root', db='zy')
        # 使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 使用execute方法执行SQL语句
        cursor.execute(
            "SELECT zy.`share_post`.`id`, zy.`share_post`.`pv` FROM zy.`share_post` WHERE zy.`share_post`.`status` = 1 ORDER BY zy.`share_post`.`pv` DESC LIMIT 50")

        # 使用fetchone()方法获取一条数据
        dataList = cursor.fetchall()

        db.close()
        return dataList

    #自定义时间段--新增用户Android，包括注册和访客
    def get_userAndroid_inc_anytime(self, time_S, time_E):
        # 打开数据库连接（ip/port/登陆用户名/登录密码/数据库名）
        db = pymysql.connect(host='172.16.2.101', port=3306, user='root', passwd='root', db='zy')
        # 使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 使用execute方法执行SQL语句
        cursor.execute(
            "SELECT zy.`share_post`.`id`, zy.`share_post`.`pv` FROM zy.`share_post` WHERE zy.`share_post`.`status` = 1 ORDER BY zy.`share_post`.`pv` DESC LIMIT 50")

        # 使用fetchone()方法获取一条数据
        dataList = cursor.fetchall()

        db.close()
        return dataList


    #最近7天新增用户，包括注册和访客
    def get_user_inc_7day(self,time_S,time_E):
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


    #最近7天新增用户iOS，包括注册和访客
    def get_userIOS_inc_7day(self,time_S,time_E):
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


    # 最近7天新增用户Android，包括注册和访客
    def get_userAndroid_inc_7day(self, time_S, time_E):
        # 打开数据库连接（ip/port/登陆用户名/登录密码/数据库名）
        db = pymysql.connect(host='172.16.2.101', port=3306, user='root', passwd='root', db='zy')
        # 使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 使用execute方法执行SQL语句
        cursor.execute(
            "SELECT zy.`share_post`.`id`, zy.`share_post`.`pv` FROM zy.`share_post` WHERE zy.`share_post`.`status` = 1 ORDER BY zy.`share_post`.`pv` DESC LIMIT 50")

        # 使用fetchone()方法获取一条数据
        dataList = cursor.fetchall()

        db.close()
        return dataList


    #最近30天新增用户，包括注册和访客
    def get_user_inc_30day(self,time_S,time_E):
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


    #最近30天新增用户IOS，包括注册和访客
    def get_userIOS_inc_30day(self,time_S,time_E):
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


    #最近30天新增用户Android，包括注册和访客
    def get_userAndroid_inc_30day(self,time_S,time_E):
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

    #任意一天新增用户
    def get_user_inc_anyDay(self,time_S,time_E):
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


    #任意一天新增用户iOS
    def get_userIOS_inc_anyDay(self,time_S,time_E):
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

    #任意一天新增用户Android
    def get_userAndroid_inc_anyDay(self,time_S,time_E):
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


#用户留存
#用户留存
#用户留存
#用户留存--时间段--日留存--次日、最近7日、最近14日、最近30日
    def get_day_remain_percent(self,time):
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


    #用户留存--时间段--周留存--次周、4周、12周
    def get_week_remain_percent(self,time):
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


    #用户留存--时间段--月留存--次月、6月、12月
    def get_month_remain_percent(self):
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



if __name__ == '__main__':
    a = GetUserData()

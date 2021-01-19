import pymysql

class GetMysqlDataSeller:
    def getUserIdByMail(self,mail):
        # 打开数据库连接（ip/port/数据库用户名/登录密码/数据库名）
        db = pymysql.connect(host='172.16.2.101', port=3306, user='root', passwd='root', db='zy_seller')
        # 使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 使用execute方法执行SQL语句
        cursor.execute('SELECT zy_seller.user.id FROM zy_seller.user WHERE zy_seller.user.mail=%s',(mail))

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
        db = pymysql.connect(host = '172.16.2.101',port = 3306,user = 'root',passwd = 'root',db = 'zy_seller')
        #使用cursor()方法创建一个游标对象cursor,使用cursor()方法获取操作游标
        cursor = db.cursor()

        #使用execute方法执行SQL语句
        cursor.execute('SELECT zy_seller.user_token.token FROM zy_seller.user_token WHERE zy_seller.user_token.userId=%s ORDER BY zy_seller.user_token.createAt DESC',(userId))

        #使用fetchone()方法获取一条数据
        tokenList = cursor.fetchone()
        token = tokenList[0]

        db.close()
        return token


if __name__ == '__main__':
    a = GetMysqlDataSeller()
    print(a.getUserIdByMail('huj@zhiyun-tech.com'))
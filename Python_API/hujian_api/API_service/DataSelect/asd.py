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
        return  percent2

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



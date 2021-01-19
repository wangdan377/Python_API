import random

class DataGeneral:
    def getData(self,choice):
        false = False
        true = True

        rNumber1 = 100
        rNumber2 = 10*random.randint(1,100)
        rNumber3 = random.choice(["9:16","16:9","4:3","1:1"])
        rNumber4 = random.choice([1,2,3,4,5,6,7])

        # duration: 0, // 时长
        # timebase: 100, // 1s等于多少时间片，默认显示100, 只可输入数字，且必须为10的倍
        # rotate: {enable: false, rotate: 0},
        # // 是否启用旋转
        # // 0不旋转
        # // 1左转
        # // 2右转
        # // 3垂直翻转
        # // 4水平翻转
        # // 5垂直翻转并右旋
        # // 6水平翻转并右旋
        # // 7 180度旋转
        # render: {renderSize: '9:16'} // 比例，选项包括9: 16、16: 9、4: 3、1: 1，默认选项为9: 16

#不旋转
        if choice == 0:
            general = {"duration": rNumber1, "timebase": rNumber2, "render": {"renderSize": rNumber3}, "rotate": {"enable": false, "rotate": 0}}
#旋转
        if choice == 1:
            general = {"duration": rNumber1, "timebase": rNumber2, "render": {"renderSize": rNumber3}, "rotate": {"enable": true, "rotate": rNumber4}}

        return general




if __name__ == '__main__':
    a = DataGeneral()
    print(a.getData(1))
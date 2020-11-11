import random

class DataMusic:
    def getData(self,choice):
        false = False
        true = True

    # attachTime: 0, // 此段音乐添加在总合成视频时间轴上的时间点(单位：timebase)
    # startTime: 0, // 开始时间(单位：timebase)
    # endTime: 23, // 结束时间(单位：timebase)
    # timebase: 30, // 1s由多少个时间单位组成
    # volume: 0, // 音量默认为0，输入范围为0~1，粒度为0.1
    # mute: false, // 原视频是否静音
    # name: 'name.aac', // 音乐
    # isLocalSource: false // 是否是app资源

        APP_resource = ["Sage", "Maid", "Mace"]
        rAPP = random.choice(APP_resource)

        Cloud_resource = ["音乐资源1", "音乐资源2", "音乐资源3"]
        rCloud = random.choice(Cloud_resource)

        preNumber = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        rNumber = random.choice(preNumber)

        rTime_s = random.randint(0,10)
        rTime_e = random.randint(10,20)
        rTime_att = random.randint(0,10)

        music = {
            "startTime": 0,
            "endTime": "",
            "timebase": 50,
            "volume": 0,
            "mute": false,
            "name": "",
            "isLocalSource": false
            }

        musics_none = [{
            "attachTime": "",
            "startTime": 0,
            "endTime": "",
            "timebase": 50,
            "volume": 0,
            "mute": false,
            "name": "",
            "isLocalSource": false
        }]

        if choice == 1:
            musics[1]["startTime"] = rTime_s
            musics[1]["endTime"] = rTime_e
            musics[1]["attachTime"] = rTime_att
            musics[1]["timebase"] = 100
            musics[1]["timebase"] = rNumber

        if choice == 2:
            music["enable"] = true
            music["name"] = rCloud
            music["strength"] = rNumber

        return music

if __name__ == '__main__':
    a = DataMusic()
    print(a.getData(2))
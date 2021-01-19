import random

class DataMusic:
    def getData(self,choice):
        false = False
        true = True

        rNumber1 = random.randint(0, 10)
        rNumber2 = random.randint(20, 50)
        rNumber3 = random.randint(0, 50)
        rNumber4 = 10*random.randint(1,100)
        rNumber5 = random.choice([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])

#前置条件：需要music数据
        if choice == 10:
            musics = [{"attachTime": rNumber3, "startTime": rNumber1, "endTime": rNumber2, "timebase": rNumber4, "volume": 0, "mute": true, "name": "in.mp3", "isLocalSource": true, "enabled": true},
                      {"attachTime": rNumber3, "startTime": rNumber1, "endTime": rNumber2, "timebase": rNumber4, "volume": rNumber5, "mute": false, "name": "out.mp3", "isLocalSource": false, "enabled": true}]
            return musics

    # attachTime: 0, // 此段音乐添加在总合成视频时间轴上的时间点(单位：timebase)
    # startTime: 0, // 开始时间(单位：timebase)
    # endTime: 23, // 结束时间(单位：timebase)
    # timebase: 30, // 1s由多少个时间单位组成
    # volume: 0, // 音量默认为0，输入范围为0~1，粒度为0.1
    # mute: false, // 原视频是否静音
    # name: 'name.aac', // 音乐
    # isLocalSource: false // 是否是app资源

#无BGM
        if choice == 0:
            music = {
                "startTime": 0,
                "timebase": 50,
                "volume": 0,
                "mute": false,
                "name": "",
                "isLocalSource": false}

#内置+静音
        if choice == 1:
            music = {
                "attachTime": rNumber3,
                "startTime": rNumber1,
                "endTime": rNumber2,
                "timebase": rNumber4,
                "volume": 0,
                "mute": true,
                "name": "in.mp3",
                "isLocalSource": true,
                "enabled": true}

#内置+不静音
        if choice == 2:
            music = {
                "attachTime": rNumber3,
                "startTime": rNumber1,
                "endTime": rNumber2,
                "timebase": rNumber4,
                "volume": rNumber5,
                "mute": false,
                "name": "in.mp3",
                "isLocalSource": true,
                "enabled": true}

#后台+静音
        if choice == 3:
            music = {
                "attachTime": rNumber3,
                "startTime": rNumber1,
                "endTime": rNumber2,
                "timebase": rNumber4,
                "volume": 0,
                "mute": true,
                "name": "out.mp3",
                "isLocalSource": false,
                "enabled": true}

#后台+不静音
        if choice == 4:
            music = {
                "attachTime": rNumber3,
                "startTime": rNumber1,
                "endTime": rNumber2,
                "timebase": rNumber4,
                "volume": rNumber5,
                "mute": false,
                "name": "out.mp3",
                "isLocalSource": false,
                "enabled": true}

        return music



if __name__ == '__main__':
    a = DataMusic()
    print(a.getData(10))



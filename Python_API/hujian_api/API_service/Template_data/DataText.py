import random

class DataText:
    def getData(self,choice):
        false = False
        true = True

        rNumber1 = random.randint(0, 10)
        rNumber2 = random.randint(20, 100)
        rNumber3 = 0.1*random.randint(0,3600)
        rNumber4 = random.choice([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
        rNumber5 = random.randint(1,7)



        # {
        # startTime: 0, // 贴纸在视频开始时间点(单位：timebase)
        # endTime: 23, // 贴纸在视频结束时间点(单位：timebase)
        # angle: 1, // 贴纸角度，单位：度, 默认值为0°，取值范围0~360°，粒度0.1
        # center: '0,0', // 贴纸在屏幕上的中心点(x, y) 范围：0~1, 粒度为0.1，]
        # type:
        # //贴纸类型：text, image, gif
        # scale: 0, // 缩放比例, 默认值为0，取值范围0~1，粒度为0.1
        # // type = text时存在
        # text: {
        #           isLocalSource: false,
        #           fontSize: 16, // 默认值为1，取值范围为1 - 7，整数
        #           fontName: 'MYingHeiPRC-W7.ttf',
        #           textColor: 'FFFFFFFF', // 字体颜色： ARGB
        #           text: '内容', // 最多可输入50个字符
        #           caption: { // 文字样式
        #           name: 'xxx.captionstyle', // 文字样式文件
        #           isLocalSource: false
        #       }
        # }


#无文字
        if choice == 0:
            text = {
                "startTime": 0,
                "angle": 0,
                "center": "0,0",
                "type": "text",
                "scale": 0,
                "text":
                    {
                    "isLocalSource": false,
                    "fontSize": 1,
                    "fontName": "",
                    "textColor": "",
                    "text": "",
                    "caption": {
                        "name": "",
                        "isLocalSource": false,
                        "type": "style"},
                    "type": "text"
                    }
                }

#文字+内置
        if  choice == 1:
            text = {
                "startTime": rNumber1,
                "angle": rNumber3,
                "center": "0.2,0.2",
                "type": "text",
                "scale": rNumber4,
                "text": {
                    "isLocalSource": true,
                    "fontSize": rNumber5,
                    "fontName": "in.ttf",
                    "textColor": "33747474",
                    "text": "嗯嗯嗯",
                    "caption": {
                        "name": "",
                        "isLocalSource": false,
                        "type": "style"},
                    "type": "text",
                    "enabled": true},
                "endTime": rNumber2}


#文字+后台
        if  choice == 2:
            text = {
                "startTime": rNumber1,
                "angle": rNumber3,
                "center": "0.2,0.2",
                "type": "text",
                "scale": rNumber4,
                "text": {
                    "isLocalSource": false,
                    "fontSize": rNumber5,
                    "fontName": "方正黑体简体.TTF",
                    "textColor": "3347474",
                    "text": "嗯嗯嗯",
                         "caption": {
                             "name": "方正黑体简体.TTF",
                             "isLocalSource": false,
                             "enabled": true,
                             "file": {
                                "id": 143,
                                "name": "方正黑体简体",
                                "hash": "803527c71e24d67cd9c7728ef838a4ce",
                                "url": "https://oss.zhiyun-tech.com/zyplaytest/templates/803527c71e24d67cd9c7728ef838a4ce.TTF",
                                "type": "font/ttf", "size": 2955220,
                                "ext": "{\"duration\":\"\",\"orgName\":\"方正黑体简体.TTF\",\"licenseUrl\":\"\"}",
                                "org_id": 26,
                                "org_label": "样式1"},
                             "type": "style"},
                         "type": "text",
                         "enabled": true,
                         "file": {
                             "id": 143,
                             "name": "方正黑体简体", "hash": "803527c71e24d67cd9c7728ef838a4ce",
                             "url": "https://oss.zhiyun-tech.com/zyplaytest/templates/803527c71e24d67cd9c7728ef838a4ce.TTF",
                             "type": "font/ttf", "size": 2955220,
                             "ext": "{\"duration\":\"\",\"orgName\":\"方正黑体简体.TTF\",\"licenseUrl\":\"\"}",
                             "org_id": 24,
                             "org_label": "胡健1"}
                         },
                "endTime": rNumber2 }

        return text


if __name__ == '__main__':
    a = DataText()
    print(a.getData(2))


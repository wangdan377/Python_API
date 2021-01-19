import random

class DataSticker:
    def getData(self,choice):
        false = False
        true = True

        rNumber2 = random.randint(0, 10)
        rNumber3 = random.randint(20, 100)
        rNumber1 = random.choice([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
        rNumber4 = random.choice([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
        rNumber3 = random.choice([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
        rNumber4 = random.choice([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
        rNumber5 = random.choice([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])

#无贴纸
        if choice == 0:
            sticker = {
                "angle": 0,
                "center": "0,0",
                "startTime": 0,
                "endTime": 0,
                "type": "image",
                "scale": 0,
                "image": {
                    "isLocalSource": false,
                    "name": ""}}

#贴纸为image+内置
        if choice == 1:
            sticker = {
                "angle": rNumber1,
                "center": "0.2,0.2",
                "startTime": rNumber2,
                "endTime": rNumber3,
                "type": "image",
                "scale": rNumber4,
                "image": {
                    "isLocalSource": true,
                    "name": "in.png"},
                "enable": true}

#贴纸为image+后台
        if choice == 2:
            sticker = {
                "angle": rNumber1,
                "center": "0.2,0.2",
                "startTime": rNumber2,
                "endTime": rNumber3,
                "type": "image",
                "scale": rNumber4,
                "image": {
                    "isLocalSource": false,
                    "name": "out.png",
                    "file": {
                        "id":114,
                        "name":"pic_zf_bjq_tz_dk",
                        "hash":"e99ceb880424e953d10490557b56aa03",
                        "url":"https://oss.zhiyun-tech.com/zyplaytest/templates/e99ceb880424e953d10490557b56aa03.png",
                        "type":"image/png",
                        "size":15838,
                        "ext":"{\"duration\":\"\",\"orgName\":\"pic_zf_bjq_tz_dk.png\",\"licenseUrl\":\"\"}",
                        "org_id":18,
                        "org_label":"打卡"}},
                "enable": true}

#贴纸为gif+内置
        if choice == 3:
            sticker = {
                "angle": rNumber1,
                "center": "0.2,0.2",
                "startTime": rNumber2,
                "endTime": rNumber3,
                "type": "gif",
                "scale": rNumber4,
                "gif": {
                    "isLocalSource": true,
                    "name": "in.gif"},
                "enable": true}

#贴纸为gif+后台
        if choice == 4:
            sticker = {
                "angle": rNumber1,
                "center": "0.2,0.2",
                "startTime": rNumber2,
                "endTime": rNumber3,
                "type": "gif",
                "scale": rNumber4,
                "gif": {
                    "isLocalSource": false,
                    "name": "out.gif",
                    "file": {
                        "id": 114,
                        "name": "pic_zf_bjq_tz_dk",
                        "hash": "e99ceb880424e953d10490557b56aa03",
                        "url": "https://oss.zhiyun-tech.com/zyplaytest/templates/e99ceb880424e953d10490557b56aa03.png",
                        "type": "image/png",
                        "size": 15838,
                        "ext": "{\"duration\":\"\",\"orgName\":\"pic_zf_bjq_tz_dk.png\",\"licenseUrl\":\"\"}",
                        "org_id": 18,
                        "org_label": "打卡"}},
                "enable": true}

        return sticker


if __name__ == '__main__':
    a = DataSticker()
    for i in range(0,5):
        print(a.getData(i))


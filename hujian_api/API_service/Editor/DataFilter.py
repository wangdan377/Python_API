import random

class DataFilter:
#是否启用_是否是app资源_滤镜名_取值:-1~1, 粒度：0.1
    def getData(self,choice):
        false = False
        true = True
      # // zy-cami 支持
      # // 内置
      # // "Sage"（明快）
      # // "Maid"（少女时代）
      # // "Mace"（锐利）
      # // "Lace"（蕾丝）
      # // "Mall"（时尚）
      # // "Sap"（元气）
      # // "Sara"（调皮）
      # // "Pinky"（草莓薄荷）
      # // "Sweet"（粉嫩）
      # // "Fresh"（清爽）
      # // 2.美摄文件滤镜.videofx文件
      # // 3.Lut文件：.mslut和.png文件
      # // zy-play 只支持.png

        APP_resource = ["Sage", "Maid", "Mace", "Lace", "Mall", "Sap", "Sara", "Pinky", "Sweet", "Fresh"]
        rAPP = random.choice(APP_resource)

        Cloud_resource = ["滤镜资源1", "滤镜资源2", "滤镜资源3"]
        rCloud = random.choice(Cloud_resource)

        preNumber = [-1, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        rNumber = random.choice(preNumber)

        filter = {"enable":false, "isLocalSource":false, "name":"", "strength":0}

        if choice == 1:
            filter["enable"] = true
            filter["isLocalSource"] = true
            filter["name"] = rAPP
            filter["strength"] = rNumber

        if choice == 2:
            filter["enable"] = true
            filter["name"] = rCloud
            filter["strength"] = rNumber

        return filter

if __name__ == '__main__':
    a = DataFilter()
    print(a.getData(2))
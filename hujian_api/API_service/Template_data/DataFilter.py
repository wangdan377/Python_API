import random

class DataFilter:
    def getData(self,choice):
        false = False
        true = True

        number_resource = [-1, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        rNumber1 = random.choice(number_resource)

        # filter: {enable: false, // 是否启用
        # isLocalSource: false, // 是否是app资源
        # name: 'lut.png', // 滤镜名
        # strength: 0.8 // 取值:-1~1, 粒度：0.1}
        # // zy - cami支持
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
        # // zy - play只支持.png

#无滤镜
        if choice == 0:
            filter = {
                "enable": false,
                "isLocalSource": false,
                "name": "",
                "strength": 0}

#滤镜+内置
        if choice == 1:
            filter = {
                "enable": true,
                "isLocalSource": true,
                "name": "in.png",
                "strength": rNumber1}

#滤镜+后台
        if choice == 2:
            filter = {
                "enable": true,
                "isLocalSource": false,
                "name": "out.png",
                "strength": rNumber1}

        return filter




if __name__ == '__main__':
    a = DataFilter()
    print(a.getData(2))
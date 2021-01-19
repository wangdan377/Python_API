import random

class DataEffect:
    def getData(self,choice):
        false = False
        true = True

        # APP_resource = ["Sage", "Maid", "Mace", "Lace", "Mall", "Sap", "Sara", "Pinky", "Sweet", "Fresh"]
        # rAPP = random.choice(APP_resource)
        #
        # cloud_resource = ["滤镜资源1", "滤镜资源2", "滤镜资源3"]
        # rCloud = random.choice(cloud_resource)

        number_resource = [-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1]
        rNumber1 = random.choice(number_resource)
        rNumber2 = random.choice(number_resource)
        rNumber3 = random.choice(number_resource)
        rNumber4 = random.choice(number_resource)
        rNumber5 = random.choice(number_resource)

        # enable: false, // 是否启用
        # saturation: 0, // 饱和度，取值: -1~1, 粒度：0.2
        # contrast: 0, // 对比度，取值: -1~1, 粒度：0.2
        # temperature: 0, // 色温，取值: -1~1, 粒度：0.2
        # hue: 0, // 色调，取值: -1~1, 粒度：0.2
        # exposure: 0, // 曝光，取值: -1~1, 粒度：0.2
        # vignette: 0, // 暗角，取值: -1~1, 粒度：0.2（zy - play不需要）
        # sharpen: 0 // 锐化，取值: -1~1, 粒度：0.2（zy - play不需要）

# 启用-无输入值
        if choice == 0:
            effect = {
                "enable": true,
                "vignette": "",
                "sharpen": ""}

#启用-有输入值
        if choice == 1:
            effect = {
                "enable": true,
                "contrast": rNumber1,
                "exposure": rNumber2,
                "saturation": rNumber3,
                "temperature": rNumber4,
                "hue": rNumber5,
                "vignette": "",
                "sharpen": ""}

        return effect




if __name__ == '__main__':
    a = DataEffect()
    print(a.getData(1))
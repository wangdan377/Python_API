import random

class DataEffect:
#是否启用_是否是app资源_滤镜名_取值:-1~1, 粒度：0.1
    def getData(self,choice):
        false = False
        true = True
        # saturation: 0, // 饱和度，取值: -1~1, 粒度：0.2
        # contrast: 0, // 对比度 取值: -1~1, 粒度：0.2
        # temperature: 0, // 色温取值: -1~1, 粒度：0.2
        # hue: 0, // 色调取值: -1~1, 粒度：0.2
        # exposure: 0, // 曝光取值: -1~1, 粒度：0.2
        # vignette: 0, // 暗角取值: -1~1, 粒度：0.2（zy - play不需要）
        # sharpen: 0 // 锐化取值: -1~1, 粒度：0.2（zy - play不需要）

        preNumber = [-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1]
        rNumber = random.choice(preNumber)

        effect = {"enable": false, "vignette":"", "sharpen":""}

        if choice == 1:
            effect["enable"] = true
            effect["contrast"] = rNumber
            effect["exposure"] = rNumber
            effect["saturation"] = rNumber
            effect["temperature"] = rNumber
            effect["hue"] = rNumber

        return effect

if __name__ == '__main__':
    a = DataEffect()
    print(a.getData(1))
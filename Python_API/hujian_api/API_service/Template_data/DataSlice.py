import random

class DataSlice:
    def getData(self,choice):
        false = False
        true = True

        slices=[{"tabconfig":{"canClose":true},
                 "timebase":60,"startTime":0,"endTime":50,"duration":6000,
                 "mute":false,"volume":0,"rate":1,
                 "rotate":{"enable":false,"rotate":0},
                 "transition":{"isLocalSource":true,"name":"641DC0DC-FDF9-4DF7-A268-C5F5B0E3293E.2",
                               "duration":6000,"timebase":60,"type":"transition","enable":true}
                 },
                {"tabconfig":{"canClose":true},
                 "timebase":60,"startTime":0,"endTime":0.5,"duration":0.5,
                 "mute":false,"volume":0,"rate":1,"rotate":{"enable":false,"rotate":0}
                 }]






if __name__ == '__main__':
    a = DataFilter()
    print(a.getData(2))
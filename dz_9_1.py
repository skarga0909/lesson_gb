import time


class TrafficLight:
    def __init__(self, __color_):
        self.__color_ = __color_

    def running(self):
        print(f'red')
        time.sleep(7)
        print(f'yellow')
        time.sleep(2)
        print(f'green')
        time.sleep(5)


traffic_light = TrafficLight('Traffic light')
traffic_light.running()

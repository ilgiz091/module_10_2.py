import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)

    def run(self):
        warriors = 100
        days = 0
        print(f'{self.name}, на нас напали!')
        for i in range(warriors):
            if warriors > 0:
                days += 1
                warriors -= self.power
                print(f'{self.name} сражается {days} день(дня)..., осталось {warriors} воинов.')
                time.sleep(1)
                if warriors <= 0:
                    print(f'{self.name} одержал победу спустя {days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print("Все битвы закончились!")


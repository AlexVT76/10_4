import threading
import time
import random
from queue import Queue
class Table:
    def __init__(self,number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self,name):
       super().__init__()
       self.name = name
    def run(self):
        time.sleep(random.randint(3,10))
class Cafe:
    def __init__(self,*tables):
        self.tables =list( tables )
        self.queue = Queue()
    def guest_arrival(self, *guests):
        for  guest in guests:
            for table in self.tables:
                flag = False
                if table.guest is None:
                    flag = True
                    break
            if flag:
               table.guest = guest
               guest.start()
               print(f'{guest.name} сел(-а) за стол номер {table.number}')

            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
    def discuss_guests(self):
        while not self.queue.empty() or any (table.guest is not None for table in tables):
            for table in self.tables:
               if table.guest and not table.guest.is_alive():
                   print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                   print(f'Стол номер {table.number} свободен')
                   table.guest = None
                   if not self.queue.empty():
                       guest = self.queue.get()
                       table.guest = guest
                       print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                       guest.start()



tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
cafe.discuss_guests()
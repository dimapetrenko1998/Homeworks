import threading
import time

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.queue = []
        self.tables = tables

    def customer_arrival(self):
        visitor_number = 1
        while True:
            time.sleep(1)  
            print(f"Посетитель номер {visitor_number} прибыл")
            visitor_number += 1
            self.serve_customer()

    def serve_customer(self, visitor_number=None):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {table.number} сел за стол {table.number}. (начало обслуживания)")
                time.sleep(5)  # Simulate eating time
                print(f"Посетитель номер {table.number} покушал и ушёл. (конец обслуживания)")
                table.is_busy = False
                return
        else:
            print(f"Посетитель номер {visitor_number - 1} ожидает свободный стол. (помещение в очередь)")



table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

customer_arrival_thread.join()

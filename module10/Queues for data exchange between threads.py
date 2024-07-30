import threading
import time

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = []
        self.customer_number = 0

    def customer_arrival(self):
        while True:
            time.sleep(1)  # Simulate customer arrival every second
            self.customer_number += 1
            customer = f"Посетитель номер {self.customer_number}"
            self.queue.append(customer)
            print(f"{customer} прибыл")
            self.serve_customer(customer)

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"{customer} сел за стол {table.number} (начало обслуживания)")
                time.sleep(5)  # Simulate meal duration
                print(f"{customer} покушал и ушёл (конец обслуживания)")
                table.is_busy = False
                break
        else:
            print(f"{customer} ожидает свободный стол (помещение в очередь)")

# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()

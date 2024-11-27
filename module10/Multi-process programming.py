import multiprocessing


class WarehouseManager:
    def __init__(self):
        self.data = multiprocessing.Manager().dict()

    def process_request(self, request):
        product, action, quantity = request
        if action == "receipt":
            if product in self.data:
                self.data[product] += quantity
            else:
                self.data[product] = quantity
            print(f"Получено: {quantity} единиц товара '{product}'. Текущий запас: {self.data[product]}.")
        elif action == "shipment":
            if product in self.data and self.data[product] >= quantity:
                self.data[product] -= quantity
                print(f"Отгружено: {quantity} единиц товара '{product}'. Текущий запас: {self.data[product]}.")
            else:
                print(f"Не удалось отгрузить {quantity} единиц товара '{product}'. Недостаточно на складе.")

    def run(self, requests):
        processes = []
        for request in requests:
            process = multiprocessing.Process(target=self.process_request, args=(request,))
            process.start()
            processes.append(process)

        for process in processes:
            process.join()


if __name__ == "__main__":
    manager = WarehouseManager()

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    manager.run(requests)

    print(dict(manager.data))

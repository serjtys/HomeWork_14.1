class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут цены
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict, products_list=None):
        """Класс-метод для создания нового продукта из словаря с проверкой дубликатов"""
        if products_list:
            for product in products_list:
                if product.name.lower() == product_data["name"].lower():
                    # Объединяем количество и выбираем максимальную цену
                    product.quantity += product_data["quantity"]
                    if product_data["price"] > product.price:
                        product.price = product_data["price"]
                    return product

        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self):
        """Геттер для цены"""
        return self._price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены с проверкой и подтверждением снижения"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self._price:
            answer = input(f"Вы действительно хотите снизить цену с {self._price} до {new_price}? (y/n): ")
            if answer.lower() == "y":
                self._price = new_price
        else:
            self._price = new_price


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут списка товаров

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Метод для добавления продукта в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для списка товаров"""
        return "\n".join([f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products])

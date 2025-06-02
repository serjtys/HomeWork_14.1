from src.products import Category, Product

if __name__ == "__main__":
    # Создаем продукты
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаем категорию и добавляем продукты
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Тестируем вывод списка товаров через property
    print("Список товаров в категории:")
    print(category1.products)

    # Тестируем добавление нового товара
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print("\nПосле добавления нового товара:")
    print(category1.products)
    print(f"Общее количество продуктов: {category1.product_count}")

    # Тестируем класс-метод создания продукта
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23",
            "description": "128GB, Черный цвет, 108MP камера",
            "price": 150000.0,
            "quantity": 3,
        }
    )
    print("\nНовый продукт через класс-метод:")
    print(f"{new_product.name}, {new_product.price} руб. Остаток: {new_product.quantity} шт.")

    # Тестируем сеттер цены
    print("\nТестирование изменения цены:")
    new_product.price = 160000.0  # Увеличение цены
    print(f"Новая цена после увеличения: {new_product.price}")

    new_product.price = -100  # Попытка установить отрицательную цену
    print(f"Цена после попытки установить отрицательное значение: {new_product.price}")

    # Тестируем подтверждение снижения цены (в интерактивном режиме запросит подтверждение)
    new_product.price = 140000.0  # Снижение цены
    print(f"Цена после снижения: {new_product.price}")

    # Тестируем обработку дубликатов
    print("\nТестирование обработки дубликатов:")
    existing_products = [product1, product2, product3, product4]
    duplicate_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет", "price": 190000.0, "quantity": 2},
        existing_products,
    )
    print(f"Количество после объединения: {product1.quantity}")  # Должно быть 7 (5 + 2)
    print(f"Цена после объединения: {product1.price}")  # Должно быть 190000.0 (максимальная цена)

# E-commerce Core (Домашнее задание 14)

Ядро интернет-магазина с названиями товаров и категорий.

## Функционал

- Реализованы основные классы для работы с товарами и категориями:
  - `Product` - товар с атрибутами:
    - Название
    - Описание
    - Цена
    - Количество на складе
  - `Category` - категория товаров с атрибутами:
    - Название
    - Описание
    - Список товаров
    - Автоматический подсчет категорий и товаров (атрибуты класса)

## Установка

1. Клонировать репозиторий:
   ```
   git clone HomeWork_14.1
   cd e-commerce-project
   ```

2. Установка зависимости:
   ```
   poetry install
   ```

## Запуск

Основной скрипт:
   ```
   python main.py
   ```

Запуск тестов:
   ```
   pytest tests/ --cov=src
   ```

## Дальнейшее развитие:

Проект будет расширяться в следующих домашних заданиях

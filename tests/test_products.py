from unittest.mock import patch

import pytest

from src.products import Category, Product


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 100.0, 10)


@pytest.fixture
def sample_category(sample_product):
    return Category("Test Category", "Test Category Description", [sample_product])


def test_product_initialization(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 10


def test_category_initialization(sample_category, sample_product):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Category Description"
    assert len(sample_category._Category__products) == 1
    assert sample_category._Category__products[0] == sample_product


def test_category_count():
    initial_count = Category.category_count
    _ = Category("Temp Category", "Temp Description", [])
    assert Category.category_count == initial_count + 1


def test_product_count():
    initial_count = Category.product_count
    product = Product("Temp Product", "Temp Desc", 50.0, 5)
    _ = Category("Temp Category", "Temp Description", [product])
    assert Category.product_count == initial_count + 1


def test_add_product(sample_category):
    initial_count = Category.product_count
    new_product = Product("New", "Desc", 20.0, 3)
    sample_category.add_product(new_product)
    assert len(sample_category._Category__products) == 2
    assert Category.product_count == initial_count + 1


def test_products_property(sample_category):
    products_str = sample_category.products
    assert "Test Product" in products_str
    assert "100" in products_str
    assert "10" in products_str


def test_new_product_classmethod():
    product_data = {"name": "New Product", "description": "New Desc", "price": 150.0, "quantity": 7}
    product = Product.new_product(product_data)
    assert product.name == "New Product"
    assert product.description == "New Desc"
    assert product.price == 150.0
    assert product.quantity == 7


def test_new_product_with_duplicate():
    product_data = {"name": "Duplicate Product", "description": "Desc", "price": 100.0, "quantity": 5}
    existing_product = Product("Duplicate Product", "Old Desc", 90.0, 10)
    product = Product.new_product(product_data, [existing_product])

    assert product == existing_product
    assert product.quantity == 15  # 10 + 5
    assert product.price == 100.0  # Более высокая цена


def test_price_setter(sample_product, capsys):
    sample_product.price = 120.0
    assert sample_product.price == 120.0

    sample_product.price = -10
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 120.0  # Цена не изменилась

    sample_product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 120.0  # Цена не изменилась


@patch("builtins.input", return_value="y")
def test_price_decrease_confirmation_yes(mock_input, sample_product):
    sample_product.price = 80.0
    assert sample_product.price == 80.0


@patch("builtins.input", return_value="n")
def test_price_decrease_confirmation_no(mock_input, sample_product):
    sample_product.price = 150.0  # Сначала увеличим
    sample_product.price = 80.0  # Пытаемся уменьшить
    assert sample_product.price == 150.0  # Цена не изменилась

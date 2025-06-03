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
    assert len(sample_category.products) == 1
    assert sample_category.products[0] == sample_product


def test_category_count():
    initial_count = Category.category_count
    _ = Category("Temp Category", "Temp Description", [])  # Используем _ для неиспользуемой переменной
    assert Category.category_count == initial_count + 1


def test_product_count():
    initial_count = Category.product_count
    product = Product("Temp Product", "Temp Desc", 50.0, 5)
    _ = Category("Temp Category", "Temp Description", [product])  # Используем _ для неиспользуемой переменной
    assert Category.product_count == initial_count + 1

import pytest


pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):

        mock_model = category_factory(name="test_category")
        assert mock_model.__str__() == "test_category"


class TestBrandModel:
    def test_str_method(self, brand_factory):

        mock_model = brand_factory(name="test_brand")
        assert mock_model.__str__() == "test_brand"


class TestProductModel:
    def test_str_method(self, product_factory):

        mock_model = product_factory(name="test_product")
        assert mock_model.__str__() == "test_product"

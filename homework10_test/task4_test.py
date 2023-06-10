# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


@pytest.mark.usefixtures("class_fixture")
class TestClass:

    def test_one_fixt_class(self):
        assert True

    def test_two_fixt_class(self):
        assert True

    def test_one_fixt_test(self, test_fixture):
        assert True

    def test_two_fixt_test(self, test_fixture):
        assert True

    @pytest.mark.usefixtures("test_fixture")
    def test_three_fixt_test(self):
        assert True

    @pytest.mark.usefixtures("test_fixture")
    def test_four_fixt_test(self):
        assert True

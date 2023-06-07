# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time


@pytest.fixture(scope="class")
def class_fixture(request):
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"\nClass {request.cls.__name__} finished in {end_time - start_time:.2f} seconds.")


@pytest.fixture()
def test_fixture():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"\nTest finished in {end_time - start_time:.2f} seconds.")


# tests.py
class TestClass:

    def test_one(self, test_fixture):
        assert True

    def test_two(self, test_fixture):
        assert True

    def test_three(self):
        assert True

    def test_four(self):
        assert True


class TestClassWithFixture:
    @pytest.mark.usefixtures("class_fixture")
    def test_one(self, test_fixture):
        assert True

    @pytest.mark.usefixtures("class_fixture")
    def test_two(self, test_fixture):
        assert True

    @pytest.mark.usefixtures("class_fixture")
    def test_three(self):
        assert True

    @pytest.mark.usefixtures("class_fixture")
    def test_four(self):
        assert True

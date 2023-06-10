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

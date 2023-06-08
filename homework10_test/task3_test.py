# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("a, b, expected_output", [
    (10, 2, 5),
    (0, 5, 0),
    pytest.param(25, 25, "skipped test case", marks=pytest.mark.skip(reason="skipping this test case")),
    pytest.param(100, 10, 10, marks=pytest.mark.smoke),
])
def test_division_two_numbers(a, b, expected_output):
    assert all_division(a, b) == expected_output
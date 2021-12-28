import allure


@allure.step("Verify equal")
def verify_equal(actual, expected):
    assert actual == expected

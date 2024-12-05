import pytest
import logging
#pytest --html=report.html --self-contained-html --log-cli-level=DEBUG

#Allure
# pip install allure-pytest
# pytest --alluredir=%allure_result_folder% ./tests
# allure serve %allure_result_folder%


@pytest.fixture(scope="module", params=[1, 5, 6])
def value(val):
    yield val.param

class TestMath:
    def test_is_positive(self, value):
        logging.info(f"run with {value}")
        assert value > 0

    def test_double(self, value):
        logging.info(f"run with {value}")
        assert value * 2 > 0
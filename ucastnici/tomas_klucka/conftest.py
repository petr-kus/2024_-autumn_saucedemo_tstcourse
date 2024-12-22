import logging

def pytest_configure():
 logging.basicConfig(
 filename='my_log_pytest.log',
  level=logging.DEBUG,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
 )
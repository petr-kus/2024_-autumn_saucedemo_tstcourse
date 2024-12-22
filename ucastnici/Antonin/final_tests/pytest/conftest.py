import logging

def pytest_configure():
 logging.basicConfig(
    filename="myLogFile.log",
    level=logging.INFO,
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s"
 )
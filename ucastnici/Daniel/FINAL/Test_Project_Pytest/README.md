# Test set - Online Store

- [Link to an excel sheet with test cases](https://docs.google.com/spreadsheets/d/14D5NowVyZjATBR5Rxf7qapqOt5uX0t25Fgv8FkvGvvg/edit?usp=sharing)

Automated test cases are applied on [Saucedemo.com](https://www.saucedemo.com/) testing webpage


## Testing tools:
Python based test tools: **Selenium, Pytest, Pytest dependency, Pytest-html , Allure**


- Versions of the libraries are accessible from file `requirements.txt`
- To setup virtual environment, you can use `install_prerequisities.ps1`
- Enter `pytest` to terminal command line in created virtual environment to launch the automated tests.

To show **Allure report** in html, write this into the command line after `pytest` is completed:

> `allure serve allure-results`

FYI:
You need to have JAVA installed on your device environment. To show results of allure report in web browser, its neccessary to set up the PATH to your JAVA_HOME.
You also need to have ALLURE installed on your device environment.

## Get more information here:
- Selenium DOC: https://selenium-python.readthedocs.io/
- Pytest DOC: https://docs.pytest.org/en/stable/contents.html
- Pytest dependency DOC: https://pytest-dependency.readthedocs.io/en/stable/
- Pytest html DOC: https://pytest-html.readthedocs.io/en/latest/
- Allure report DOC: https://allurereport.org/docs/pytest/
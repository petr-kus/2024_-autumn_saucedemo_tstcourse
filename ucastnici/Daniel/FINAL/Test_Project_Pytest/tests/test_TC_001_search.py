import pytest
import allure

@allure.title("Search for an existing product")
@allure.description("Verify behavior, when results match the search query.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("TC_001_search")
@pytest.mark.dependency(depends=["test_visibility_search_field"])
def test_search_functionality(logger, driver, search_page):

    # Step 1-3: Navigate to search page, click in the search field and enter product name into search_query. Click on the search icon.
    
    search_query = "Name of item to search"
    
    search_page.open()
    search_page.search_for(search_query)

    # Verify, if the search results are displayed, showing matching products. The url address corresponds to the search query.
    results = search_page.get_search_results()
    current_url = driver.current_url

    assert len(results) > 0, f"No results found for query '{search_query}'."
    logger.info(f"At least one result found for query '{search_query}'.")

    assert any(search_query in result for result in results), f"No results contain the search term '{search_query}'."
    logger.info(f"Results contain the search term '{search_query}'.")

    assert search_query.lower() in current_url.lower(), f"URL does not contain the search query '{search_query}'. Current URL: {current_url}"
    logger.info(f"URL contains the search query '{search_query}'. Current URL: {current_url}")

    logger.info(f"Searching for '{search_query}' was succesful.")

#HODNOCENI: (100 bodu je maximum - pokud někdo nebude fakt dobrej*á) 
# jde v podstate o totoznou ulohu s du 9 - muze byt. Vetsina komentaru k oprave je tam! 
# Pokud se nekdo chce poucit z tvých chyb (existuje k tomu i video z konzultace s tebou...).
# + 50 bodu za funkčnost (jde spustit, standard_user prochází a na uživateli error user  failuje). 
# + 5 bodu za readme markdown file!
# + 5 bodu odddeleni keywordu do souboru i dat - jen by to mohlo byt lepe provazane v idititelne
# + 5 je pouzite POM
# + 5 je pouzite OOP
# + 5 je pouzite Fixtures
# + 5 je pouzite pytest.ini a conftest.py
# + 5 je report do allure a html
# + 5 je relativně dobře logováno + screenshoty sem tam
# + 3 jsou pouzite specialni znaceni pro allure
# + 3 použití Domain Langauge

 
#=> 96 bodů TEST V Pytest splněn! 

# mohl jsi dostat další body kdyby třeba... (easy tip pro ostatní):
# - jsi lepe používal domain language (dlouhá názvy)
# - jsi lépe rozdělil page object (máš komponenty součástí base třídy...)
# - jsi nespouštěl pro každý test znovu browser
# - jsi realně použil dependency nebo rozdělení do fixtures pro zalogování například (jako prerequisitu)
# - jsi použil doplněk BDD pro pytest
# - jsi logoval relevantnější zprávy a dělal častěji screnshoty
# - ... 

#Ano, šlo by to pak jistě přes sto...
    
    
    

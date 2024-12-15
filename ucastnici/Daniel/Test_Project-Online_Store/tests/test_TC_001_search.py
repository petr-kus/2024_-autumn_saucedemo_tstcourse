import pytest
import allure

#TODO: Lektor - chvalim pouziti Allure popisku. TO je originalni funkcionalita. Chvalim dohledani si teto funckionality a vyuziti!

@allure.title("Search for an existing product")
@allure.description("Verify behavior, when results match the search query.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("TC_001_search")

#TODO: Lektor - toto dependency je super, funguje to krasne jako label v Allure, ale.. jinak je to na prd pokud nekde neni uvedeno
#@pytest.mark.dependency(name="test_visibility_search_field")
# coz nikde neni... . Takze je tam cisty skip. A proste tam sel napsat skip... . :-) Ale... jako ze pekne ty... .

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


    
    
#TODO: Lektor - co ty prazdne radky a znaky na konci?! TO je zbytecne odebirat prosim... . TIP: Da se pro to pouzivat auto formatovani... .

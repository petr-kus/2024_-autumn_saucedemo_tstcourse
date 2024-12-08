def test_search_functionality(search_page):

    # Step 1-3: Navigate to search page, click in the search field and enter product name into search_query. Click on the search icon.
    
    search_query = "Name of item to search"
    
    search_page.search_for(search_query)
    results = search_page.get_search_results()

    current_url = search_page.get_current_url()

    assert len(results) > 0, f"No results found for query '{search_query}'."
    assert any(search_query in result for result in results), f"No results contain the search term '{search_query}'."
    assert search_query.lower() in current_url.lower(), f"URL does not contain the search query '{search_query}'. Current URL: {current_url}"
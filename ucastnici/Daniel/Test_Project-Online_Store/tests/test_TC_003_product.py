import allure

@allure.title("Product detail - view the content")
@allure.description("Verify that clicking on a product in product category displays its detailed information and purchase button.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("TC_003_product")
def test_view_product_detail(logger, login_page, product_category_page, product_detail_page):
    #TODO Lektor: product_category_page - není to spíš products_page nebo inventory_page, nebo products_overview ... ? Název je děsně dlouhej a opakuje se tam page... .
    # Domain Langauge je důležitý!
    
    # Step 1: Log in
    login_page.login()

    # Step 2: View product detail by clicking on chosed product image
    #TODO Lektor: tady se ztraci testovana data. Neni yde vubec videt o jaký produkt jde. 
    #vyresil bych to napriklad tim ze tam je nake pole produktů, nebo objektovy strom, nebo dictionary ... dokonce to muze byt dynamicky načítané...
    #tim pádem by zde pak jsi mohl volat například (product_category_page.PRODUCT_IDS)['backpack'] nebo product_category_page.PRODUCTS['backpack']
    #ČITELNOST FIRST!
    product_id_image = (product_category_page.PRODUCT_ID_IMAGE)


    #TODO Lektor: všimni si že bych tu mohl napsat product = product_category_page.PRODUCT_IDS a pak volat product['backpack'] v dalším kroku!
    #TODO Lektor: možná spíš go_to_product - kratší a přesně vyjadřuje co se tam v pozadí děje z pohledu uživatele!
    product_category_page.show_product_detail(product_id_image)

    # Verify, if the product details page loads with corresponding URL, displaying name, product photo, price, description and purchase button.

    #TODO Lektor: tak to fakt ne! 4 tady nesmí být napsaná na "tvrdo"! To se mělo buď načíst z toho objektu a nebo to být zároveň tady definované. 
    # rozbíjíš princip že tyto dvě věci by měli být napsané někde blízko sebe! Snižuješ čitelnost testu a zvyšuješ maintanance!
    expected_product_id = 4
    actual_product_id = product_detail_page.get_product_id_from_url()

    #TODO Lektor: jo to je fajn ta ověření dole... klidně můžeš ověřit ještě, že to není prázdné nebo nula... a klidně by tam mohla být testovací položka u které přesně znáš tyto údaje. 
    #a porovnáváš že to tak je... to by jsi si pak musel to asi hodit někam jinam... do objektu nebo něco... a tam zjistit zda jde o ten testovací produkt či ne... .
    # aby jsi dodržel obecnost.

    # jinak to že je viditelný prvek s tím ID ještě neznamená, že tam je obrázek... aby bylo jasno... . Chce to přemýšlet na co se přesně v tom assertu ptáš... .

    assert expected_product_id == actual_product_id, f"Expected product ID '{expected_product_id}', but got product ID '{actual_product_id}' reflected in URL."
    assert product_detail_page.is_element_visible(product_detail_page.PRODUCT_NAME), f"Element 'Product name' is not visible on the page."
    assert product_detail_page.is_element_visible(product_detail_page.PRODUCT_PHOTO), f"Element 'Product photo' is not visible on the page."
    assert product_detail_page.is_element_visible(product_detail_page.PRODUCT_PRICE), f"Element 'Product price' is not visible on the page."
    assert product_detail_page.is_element_visible(product_detail_page.PRODUCT_DESCRIPTION), f"Element 'Product description' is not visible on the page."
    assert product_detail_page.is_element_visible(product_detail_page.PRODUCT_ADD_CART_BUTTON), f"Element 'Purchase button' is not visible on the page."

    logger.info("Product details page is displayed correctly.")
    #TODO Lektor: to je silné tvrzení a zavadějící... viz co jsem řekl výše... . Napsal bych ho něják líp. Měkčeji něco jako Page is probablz displazed correcty (ids exists and are displayed).
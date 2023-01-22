from selenium.webdriver.common.by import By


class FormPageLocators:
    HOURS = (By.CSS_SELECTOR, '#form-input-hour')
    MINUTES = (By.CSS_SELECTOR, '#form-input-minute')
    FROM = (By.CSS_SELECTOR, '#form-input-from')
    TO = (By.CSS_SELECTOR, '#form-input-to')
    MODE = (By.CSS_SELECTOR, '#form-mode-custom')
    TYPE = (By.CSS_SELECTOR, '#from-type-car')
    RESULT = (By.CSS_SELECTOR, '#result-time-price')


class DistanceLocators:
    SEARCH = (By.ID, 'text')
    SEARCH_RESULT = (By.PARTIAL_LINK_TEXT, 'avtodispetcher.ru')
    FROM = (By.NAME, 'from')
    TO = (By.NAME, 'to')
    FUEL_CONSUMPTION = (By.NAME, 'fc')
    FUEL_PRICE = (By.NAME, 'fp')
    BUTTON = (By.CSS_SELECTOR, '.submit_button > input[type="submit"]')
    TOTAL_DISTANCE = (By.ID, 'totalDistance')
    TOTAL_PRICE = (By.XPATH, "// *[contains(text(), '3726')]")
    # // *[ @ id = "summaryContainer"] / form / p / text()[4]
    CHANGE_ROUTE = (By.CLASS_NAME, 'anchor')
    ROUTE_BETWEEN = (By.NAME, 'v')




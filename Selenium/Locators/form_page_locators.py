from selenium.webdriver.common.by import By


class FormPageLocators:
    HOURS = (By.CSS_SELECTOR, '#form-input-hour')
    MINUTES = (By.CSS_SELECTOR, '#form-input-minute')
    FROM = (By.CSS_SELECTOR, '#form-input-from')
    TO = (By.CSS_SELECTOR, '#form-input-to')
    MODE = (By.CSS_SELECTOR, '#form-mode-custom')
    TYPE = (By.CSS_SELECTOR, '#from-type-car')
    RESULT = (By.CSS_SELECTOR, '#result-time-price')

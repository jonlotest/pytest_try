import re
from src.baseclasses.base_page import BasePage
from Selenium.Locators.form_page_locators import FormPageLocators as Locators, DistanceLocators as DL
from selenium.webdriver.common.keys import Keys
from config import PHRASE


class FormPage(BasePage):

    def fill_fields_routs(self, hours, minutes, _from, to):
        self.element_is_visible(Locators.HOURS).send_keys(hours)
        self.element_is_visible(Locators.MINUTES).send_keys(minutes)
        self.element_is_visible(Locators.FROM).send_keys(_from)
        self.element_is_visible(Locators.TO).send_keys(to)
        self.element_is_visible(Locators.MODE).click()
        self.element_is_visible(Locators.TYPE).click()
        print()
        print(f'Time: {hours}:{minutes}\nAddress: {_from} - {to}')

    @property
    def form_result(self):
        result_list = self.elements_are_visible(Locators.RESULT)
        result_text = [i.text for i in result_list]
        actual_result = re.findall('[0-9]+', str(result_text))
        return actual_result

    def fill_fields_distance(self):
        self.element_is_visible(DL.SEARCH).send_keys(PHRASE + Keys.RETURN)
        self.element_is_visible(DL.SEARCH_RESULT).click()
        self.element_is_visible(DL.FROM).send_keys('Тула')
        self.element_is_visible(DL.TO).send_keys('Санкт-Петербур')
        self.element_is_visible(DL.FUEL_CONSUMPTION).clear()
        self.element_is_visible(DL.FUEL_CONSUMPTION).send_keys('9')
        self.element_is_visible(DL.FUEL_PRICE).clear()
        self.element_is_visible(DL.FUEL_PRICE).send_keys('46')
        self.element_is_visible(DL.BUTTON).click()


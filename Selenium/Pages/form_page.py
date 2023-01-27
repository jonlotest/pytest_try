import re
from src.baseclasses.base_page import BasePage
from Selenium.Locators.form_page_locators import FormPageLocators as Locators


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

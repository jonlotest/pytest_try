from src.baseclasses.base_page import BasePage
from Selenium.Locators.form_page_locators import FormPageLocators as Locators
import re
from config import ADDRESSES
import random


class FormPage(BasePage):

    def fill_fields_morning(self):
        value_hours = '11'
        value_minutes = '12'
        value_from = 'Фрунзенская набережная, 46'
        value_to = 'Хамовнический Вал, 34'
        self.element_is_visible(Locators.HOURS).send_keys(value_hours)
        self.element_is_visible(Locators.MINUTES).send_keys(value_minutes)
        self.element_is_visible(Locators.FROM).send_keys(value_from)
        self.element_is_visible(Locators.TO).send_keys(value_to)
        self.element_is_visible(Locators.MODE).click()
        self.element_is_visible(Locators.TYPE).click()

    def fill_fields_day(self):
        value_hours = '12'
        value_minutes = '45'
        value_from = 'Фрунзенская набережная, 46'
        value_to = 'Хамовнический Вал, 34'
        self.element_is_visible(Locators.HOURS).send_keys(value_hours)
        self.element_is_visible(Locators.MINUTES).send_keys(value_minutes)
        self.element_is_visible(Locators.FROM).send_keys(value_from)
        self.element_is_visible(Locators.TO).send_keys(value_to)
        self.element_is_visible(Locators.MODE).click()
        self.element_is_visible(Locators.TYPE).click()

    def fill_fields_evening(self):
        value_hours = '21'
        value_minutes = '21'
        value_from = 'Фрунзенская набережная, 46'
        value_to = 'Хамовнический Вал, 34'
        self.element_is_visible(Locators.HOURS).send_keys(value_hours)
        self.element_is_visible(Locators.MINUTES).send_keys(value_minutes)
        self.element_is_visible(Locators.FROM).send_keys(value_from)
        self.element_is_visible(Locators.TO).send_keys(value_to)
        self.element_is_visible(Locators.MODE).click()
        self.element_is_visible(Locators.TYPE).click()

    def fill_fields_night(self):
        value_hours = '22'
        value_minutes = '59'
        value_from = 'Фрунзенская набережная, 46'
        value_to = 'Хамовнический Вал, 34'
        self.element_is_visible(Locators.HOURS).send_keys(value_hours)
        self.element_is_visible(Locators.MINUTES).send_keys(value_minutes)
        self.element_is_visible(Locators.FROM).send_keys(value_from)
        self.element_is_visible(Locators.TO).send_keys(value_to)
        self.element_is_visible(Locators.MODE).click()
        self.element_is_visible(Locators.TYPE).click()

    def fill_fields_after_midnight(self):
        value_hours = '06'
        value_minutes = '45'
        value_from = 'Фрунзенская набережная, 46'
        value_to = 'Хамовнический Вал, 34'
        self.element_is_visible(Locators.HOURS).send_keys(value_hours)
        self.element_is_visible(Locators.MINUTES).send_keys(value_minutes)
        self.element_is_visible(Locators.FROM).send_keys(value_from)
        self.element_is_visible(Locators.TO).send_keys(value_to)
        self.element_is_visible(Locators.MODE).click()
        self.element_is_visible(Locators.TYPE).click()

    def fill_fields_zero(self):
        value_hours = '12'
        value_minutes = '30'
        value_from = 'Комсомольский проспект, 18'
        value_to = 'Комсомольский проспект, 18'
        self.element_is_visible(Locators.HOURS).send_keys(value_hours)
        self.element_is_visible(Locators.MINUTES).send_keys(value_minutes)
        self.element_is_visible(Locators.FROM).send_keys(value_from)
        self.element_is_visible(Locators.TO).send_keys(value_to)
        self.element_is_visible(Locators.MODE).click()
        self.element_is_visible(Locators.TYPE).click()

    def fill_fields_random(self):

        value_hours = random.randrange(10, 23)    # начинается с 10 т.к.
        value_minutes = random.randrange(10, 59)  # однозначные не принимает
        value_from = random.choice(ADDRESSES)
        value_to = random.choice(ADDRESSES)
        self.element_is_visible(Locators.HOURS).send_keys(value_hours)
        self.element_is_visible(Locators.MINUTES).send_keys(value_minutes)
        self.element_is_visible(Locators.FROM).send_keys(value_from)
        self.element_is_visible(Locators.TO).send_keys(value_to)
        self.element_is_visible(Locators.MODE).click()
        self.element_is_visible(Locators.TYPE).click()
        print()
        print('Time: ', value_hours, ':', value_minutes, '\n',
              'Address: ', value_from, '-', value_to)

    @property
    def form_result(self):
        result_list = self.elements_are_visible(Locators.RESULT)
        result_text = [i.text for i in result_list]
        actual_result = re.findall('[0-9]+', str(result_text))
        return actual_result

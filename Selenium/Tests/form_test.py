from Selenium.Pages.form_page import FormPage
from config import YA_PRAKTIKUM
from src.enums.global_enums import GlobalErrorMessages


class TestFormPage:

    def test_form_morning(self, driver):
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_morning()
        actual_result = form_page.form_result
        expected_result = ['28', '2']
        assert expected_result == actual_result, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

    def test_form_day(self, driver):
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_day()
        actual_result = form_page.form_result
        expected_result = ['28', '2']
        assert expected_result == actual_result, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

    def test_form_evening(self, driver):
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_evening()
        actual_result = form_page.form_result
        expected_result = ['28', '3']
        assert expected_result == actual_result, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

    def test_form_night(self, driver):
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_night()
        actual_result = form_page.form_result
        expected_result = ['28', '2']
        assert expected_result == actual_result, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

    def test_form_after_midnight(self, driver):
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_after_midnight()
        actual_result = form_page.form_result
        expected_result = ['28', '2']
        assert expected_result == actual_result, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

    def test_form_zero(self, driver):
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_zero()
        actual_result = form_page.form_result
        expected_result = ['0']
        assert expected_result == actual_result, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

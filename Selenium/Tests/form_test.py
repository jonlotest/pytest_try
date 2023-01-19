from Selenium.Pages.form_page import FormPage
from config import YA_PRAKTIKUM


class TestFormPage:

    def test_form_morning(self, driver):
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_morning()
        result = form_page.form_result()
        assert 'Авто ~ 28 руб.\nВ пути 3 мин.' in result

    def test_form_day(self, driver):
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_day()
        result = form_page.form_result()
        assert 'Авто ~ 28 руб.\nВ пути 2 мин.' in result

    def test_form_evening(self, driver):
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_evening()
        result = form_page.form_result()
        assert 'Авто ~ 28 руб.\nВ пути 3 мин.' in result

    def test_form_night(self, driver):
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_night()
        result = form_page.form_result()
        assert 'Авто ~ 28 руб.\nВ пути 2 мин.' in result

    def test_form_after_midnight(self, driver):
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_after_midnight()
        result = form_page.form_result()
        assert 'Авто ~ 28 руб.\nВ пути 2 мин.' in result

    def test_form_zero(self, driver):
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_zero()
        result = form_page.form_result()
        print(result)
        assert 'Авто Бесплатно\nВ пути 0 мин.' in result

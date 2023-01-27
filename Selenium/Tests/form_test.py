import random
from Selenium.Pages.form_page import FormPage
from config import YA_PRAKTIKUM, ADDRESSES
from src.enums.global_enums import GlobalErrorMessages


class TestFormPage:

    def test_form_morning(self, driver):
        """
        Время и стоимость движения собственного автомобиля в Яндекс.Маршрутах
        при времени начала движения - 08:01-12:00
        """
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_routs(hours='11',
                                    minutes='12',
                                    _from=ADDRESSES[5],
                                    to=ADDRESSES[4])
        actual_result = form_page.form_result
        expected_result = ['28', '2']
        assert expected_result == actual_result, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

    def test_form_day(self, driver):
        """Время и стоимость движения собственного автомобиля в Яндекс.Маршрутах
        при времени начала движения - 12:01-18:00
        """
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_routs(hours='12',
                                    minutes='45',
                                    _from=ADDRESSES[5],
                                    to=ADDRESSES[4])
        actual_result = form_page.form_result
        expected_result = ['28', '2']
        assert expected_result == actual_result, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

    def test_form_evening(self, driver):
        """
        Время и стоимость движения собственного автомобиля в Яндекс.Маршрутах
        при времени начала движения - 18:01-22:00
        """
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_routs(hours='21',
                                    minutes='21',
                                    _from=ADDRESSES[5],
                                    to=ADDRESSES[4])
        actual_result = form_page.form_result
        expected_result = ['28', '3']
        assert expected_result == actual_result, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

    def test_form_night(self, driver):
        """
        Время и стоимость движения собственного автомобиля в Яндекс.Маршрутах
        при времени начала движения - 22:01-00:00
        """
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_routs(hours='22',
                                    minutes='59',
                                    _from=ADDRESSES[5],
                                    to=ADDRESSES[4])
        actual_result = form_page.form_result
        expected_result = ['28', '2']
        assert expected_result == actual_result, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

    def test_form_after_midnight(self, driver):
        """
        Время и стоимость движения собственного автомобиля в Яндекс.Маршрутах
        при времени начала движения - 00:01-08:00
        """
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_routs(hours='06',
                                    minutes='45',
                                    _from=ADDRESSES[5],
                                    to=ADDRESSES[4])
        actual_result = form_page.form_result
        expected_result = ['28', '2']
        assert expected_result == actual_result, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

    def test_form_zero(self, driver):
        """
        Время и стоимость движения собственного автомобиля в Яндекс.Маршрутах
        при расстоянии равном 0
        """
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_routs(hours='12',
                                    minutes='30',
                                    _from=ADDRESSES[1],
                                    to=ADDRESSES[1])
        actual_result = form_page.form_result
        expected_result = ['0']
        assert expected_result == actual_result, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

    def test_form_random(self, driver):
        """
        Расчет времени и стоимости движения собственного автомобиля
        в Яндекс.Маршрутах в рандомные время и адреса
        """
        form_page = FormPage(driver, YA_PRAKTIKUM)
        form_page.open()
        form_page.fill_fields_routs(hours=random.randrange(10, 23),
                                    minutes=random.randrange(10, 59),
                                    _from=random.choice(ADDRESSES),
                                    to=random.choice(ADDRESSES))

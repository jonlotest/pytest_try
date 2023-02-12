from Selenium.Pages.yandex_routs_page import YandexPage
from config import YANDEX_ROUTS


class TestSharingPage:

    def test_car_sharing(self, driver):
        """
        Проверка логики бронирования при заполнении полей "Откуда" и "Куда"
        """
        form_page = YandexPage(driver, YANDEX_ROUTS)
        form_page.open()
        form_page.fill_fields_sharing(driver)
        result_text = form_page.form_sharing_result()
        header = 'Машина забронирована'
        assert header in result_text

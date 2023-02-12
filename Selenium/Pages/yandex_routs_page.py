from src.baseclasses.base_page import BasePage
from Selenium.Locators.yandex_routs_locators import YandexRoutsLocators as YRL
from selenium.webdriver.common.action_chains import ActionChains


class YandexPage(BasePage):

    def fill_fields_sharing(self, driver):
        self.element_is_visible(YRL.FROM).send_keys('Усачева 3')
        self.element_is_visible(YRL.TO).send_keys('Хамовнический вал 18')
        self.element_is_visible(YRL.MODE_MY).click()
        self.element_is_visible(YRL.CARSHARING).click()
        self.element_is_visible(YRL.BUTTON_ROUND).click()
        self.element_is_visible(YRL.TARIFF_LUX).click()
        self.element_is_visible(YRL.BUTTON_DRIVER_LICENSE).click()
        self.element_is_visible(YRL.FIRST_NAME).send_keys('Антон')
        self.element_is_visible(YRL.LAST_NAME).send_keys('Еремин')
        self.element_is_visible(YRL.BIRTHDATE).send_keys('01011999')
        self.element_is_visible(YRL.DRIVER_LICENSE_NUMBER).send_keys('1212123456')
        ActionChains(driver).move_by_offset(250, 250).click().perform()
        self.element_is_visible(YRL.BUTTON_DRIVE_LICENSE_FORM_SUBMIT).click()
        self.element_is_visible(YRL.BUTTON_AGREE).click()
        self.element_is_visible(YRL.BUTTON_PAYMENT).click()
        self.element_is_visible(YRL.ADD_CARD).click()
        self.element_is_visible(YRL.CARD_NUMBER).send_keys('999999999999')
        self.element_is_visible(YRL.CODE_NUMBER).send_keys('99')
        ActionChains(driver).move_by_offset(250, 250).click().perform()
        self.element_is_visible(YRL.BUTTON_CARD_SUBMIT).click()
        self.element_is_visible(YRL.BUTTON_CLOSE_PAYMENT).click()
        self.element_is_visible(YRL.BUTTON_SMART).click()

    def form_sharing_result(self):
        result_list = self.elements_are_visible(YRL.RESULT)
        result_text = [i.text for i in result_list]
        order_result = result_text[0]
        return order_result

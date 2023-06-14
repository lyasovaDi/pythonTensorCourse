# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException


my_login = 'лояльность'
my_password = 'лояльность123'
base_url_sbis_fix = 'https://fix-online.sbis.ru/'
sends_message = "Это сообщение отправлено с помощью автотеста"

driver = webdriver.Chrome()
driver.implicitly_wait(10)


def check_element_present_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


try:
    driver.get(base_url_sbis_fix)
    sleep(3)
    login = driver.find_element(By.NAME, "Login")
    login.send_keys(my_login, Keys.ENTER)
    assert login.get_attribute('value') == my_login, 'Не введен логин'
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(my_password, Keys.ENTER)
    sleep(8)
    contacts = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"] .NavigationPanels-Accordion__title')
    assert contacts.is_displayed(), 'Блок контактов не отображается'
    contacts.click()
    contacts2 = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    assert contacts2.is_displayed(), 'Не раскрылся список действий'
    contacts2.click()
    sleep(3)
    plus = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    assert plus.is_displayed(), 'Не отображается кнопка +'
    plus.click()
    sleep(3)
    find_me = driver.find_element(By.CSS_SELECTOR, ' .controls-StackTemplate-content_wrapper .controls-Field')
    find_me.send_keys('Иванов Иван')
    sleep(2)
    ivanuska = driver.find_element(By.CSS_SELECTOR, ' .controls-ListView__item-leftPadding_l')
    assert ivanuska.is_displayed(), "Иванушка не отображается в результатах поиска"
    ivanuska.click()
    sleep(2)
    text = driver.find_element(By.CSS_SELECTOR, ' .textEditor_Viewer__Paragraph')
    text.send_keys(sends_message)
    sleep(2)
    send = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    assert send.is_displayed(), 'Нет кнопки "отправить"'
    send.click()
    sleep(2)
    message = driver.find_element(By.XPATH, ".//p[contains(text() , '" + sends_message + "')]")
    assert message.is_displayed(), 'Сообщение не отображается'
    action_chains = ActionChains(driver)
    action_chains.move_to_element(message)
    action_chains.perform()
    delete_button = driver.find_element(By.CSS_SELECTOR, ".controls-itemActionsV__action_style_delete")
    delete_button.click()
    assert not check_element_present_by_xpath(".//p[contains(text() , '" + sends_message + "')]"), \
        "Cообщение НЕ удалено"

finally:
    driver.quit()
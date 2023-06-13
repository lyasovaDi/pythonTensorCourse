# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

sbis_site = 'https://sbis.ru/'
tensor_site = 'https://tensor.ru/'
tensor_about = 'https://tensor.ru/about'

driver = webdriver.Chrome()
try:
    driver.get(sbis_site)
    assert driver.current_url == sbis_site, 'Не верно введен адрес сайта'
    sleep(2)
    contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    assert contacts.is_displayed(), 'Вкладка "Контакты" не отображается'
    contacts.click()
    sleep(2)
    banner = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor.mb-8:not(.sbisru-link)')
    assert banner.is_displayed(), 'Баннер не отображается'
    banner.click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == tensor_site, 'Баннер не ведет на сайт https://tensor.ru'
    block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    assert block.is_displayed(), 'Блок "Сила в людях" не отображается'
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".tensor_ru-Index__block4-content .tensor_ru-link"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button)
    button.click()
    assert driver.current_url == tensor_about, 'Не открылась страница "О компании"'
    sleep(3)

finally:
    driver.quit()

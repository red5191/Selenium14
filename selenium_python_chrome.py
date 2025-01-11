# Прописываем в терминале:
# python -m pip install --upgrade pip (Обновление менеджера пакетов pip)
# pip install selenium (Устанавливаем библиотеку selenium)
# pip install webdriver-manager (Устанавливаем webdriver-manager)

# импортируем необходимые библиотеки и элементы
import time
import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# создаем и настраиваем экземпляр driver класса webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# создаем переменную содержащую базовую ссылку и открываем её с помощью созданного ранее driver
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

# вводим логин
user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys('standard_u')

# выделяем введенные символы
user_name.send_keys(Keys.CONTROL + 'a')
time.sleep(2)

# очищаем поле ввода и вводим корректный логин
print('Введен логин')
user_name.send_keys(Keys.DELETE)
time.sleep(2)
user_name.send_keys('standard_user')

# вводим пароль
password = driver.find_element(By.NAME , "password")
password.send_keys('secret_s')
time.sleep(2)

# выделяем введенные символы
# password.send_keys(Keys.CONTROL + 'a')
# time.sleep(2)

# очищаем поле ввода и вводим корректный пароль
print("Введен пароль")
password.clear()
time.sleep(2)
password.send_keys('secret_sauce')
time.sleep(2)

# имитируем нажатие Enter
password.send_keys(Keys.ENTER)
print('Нажат Enter')

# открываем меню и жмем кнопку выхода
menu = driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']")
menu.click()
time.sleep(1)
logout_button = driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
logout_button.click()

# # набиваем корзину и переходим в неё
# button_add_backpack = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
# button_add_bike = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
# button_add_t_shirt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
# button_add_jacket = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
# button_add_onesie = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()
# button_add_t_shirt_red = driver.find_element(By.XPATH, "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
# button_cart_link = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
#
# # создаем на основе driver экземпляр класса ActionChains и используем его для скрола к выбранному элементу
# actions = ActionChains(driver)
# element = driver.find_element(By.ID, 'item_3_title_link')
# actions.move_to_element(element).perform()

# создаем скриншот результата выполнения кода
time.sleep(2)
now_date = datetime.datetime.now().strftime('%Y.%m.%d-%H.%M.%S')
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('C:\\Users\\the_r\\PycharmProjects\\Selenium14\\screenshots\\' + name_screenshot)

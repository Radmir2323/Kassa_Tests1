import random
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://localhost:65009/Reception/Client/Details/24503")

# login
textfield_name = driver.find_element(By.ID, "un")
# textfield_name.send_keys("ufa.u")
textfield_name.send_keys("ufa.u")
textfield_pass = driver.find_element(By.ID, "psw")
# textfield_pass.send_keys("123456")
textfield_pass.send_keys("123456")
enter_loginBtn = driver.find_element(By.ID, "loginBtn")
enter_loginBtn.click()

# открытие страницы поиска клиентов
# issuance_loans_element = driver.find_element(By.CLASS_NAME, "list-group-item-heading")
# issuance_loans_element.click()
#
# # ввод паспортных данных клиента и открытие страницы клиента
# receptionSearch_element = driver.find_element(By.ID, "receptionSearch")
# receptionSearch_element.send_keys("8021338099")
# receptionSearchSubmit_element = driver.find_element(By.ID, "receptionSearchSubmit")
# receptionSearchSubmit_element.click()
#
# choose_client = driver.find_element(By.CSS_SELECTOR, "a[href*='/Reception/Client/Details/17463']")
# choose_client.click()

# кнопка добавления банковских реквизитов
add_bank_details_btn = driver.find_element(By.XPATH, "//a[contains(text(), 'Добавить реквизиты')]")
add_bank_details_btn.click()
name_element = driver.find_element(By.ID, "Name")
time.sleep(0.5)
name_element.send_keys('ООО "ИГРА"')
inn_element = driver.find_element(By.ID, "INN")
time.sleep(0.5)
inn_element.send_keys("7743392713")
kpp_element = driver.find_element(By.ID, "KPP")
time.sleep(0.5)
kpp_element.send_keys("774301001")
checking_account = driver.find_element(By.ID, "RS")    # расчетный счет
checking_account.send_keys("12345678912345678912")
bik_element = driver.find_element(By.ID, "BIK")     # БИК банка
bik_element.send_keys("048073601")
bank_name = driver.find_element(By.ID, "BankName")
bank_name.send_keys("БАШКИРСКОЕ ОТДЕЛЕНИЕ N8598 ПАО СБЕРБАНК")
ks_element =driver.find_element(By.ID, "KS")       # кореспондентский счет
ks_element.send_keys("30101810300000000601")
submit_bank_details_btn = driver.find_element(By.ID, "clientBankAccountAddBtn")
submit_bank_details_btn.click()

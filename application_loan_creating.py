from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')

driver.implicitly_wait(5)
driver.maximize_window()

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://localhost:65009/Reception/Client/Details/24491")
textfield_name = driver.find_element(By.ID, "un")
textfield_name.send_keys("ufa.u")
# textfield_name.send_keys("shagiev.r")
textfield_pass = driver.find_element(By.ID, "psw")
textfield_pass.send_keys("123456")
# textfield_pass.send_keys("Ruka1234!")
enter_loginBtn = driver.find_element(By.ID, "loginBtn")
enter_loginBtn.click()

# открытие страницы поиска клиентов
# issuance_loans_element = driver.find_element(By.CLASS_NAME, "list-group-item-heading")
# issuance_loans_element.click()

# ввод паспортных данных клиента и открытие страницы клиента
# receptionSearch_element = driver.find_element(By.ID, "receptionSearch")
# receptionSearch_element.send_keys("8021"+"707981")
# receptionSearchSubmit_element = driver.find_element(By.ID, "receptionSearchSubmit")
# receptionSearchSubmit_element.click()

# choose_client = driver.find_element(By.CSS_SELECTOR, "a[href*='/Reception/Client/Details/17460']")
# choose_client.click()

appl_select_btn = driver.find_element(By.XPATH, '//button[contains(text(),"Заявка на заем")]')
appl_select_btn.click()
appl_btn = driver.find_element(By.XPATH, "//a[contains(text(),'Заявка на заем')][1]")
appl_btn.click()

borrowerType_element = driver.find_element(By.ID, 'BorrowerType')
borrowerType_element.click()
borrowerType_select = driver.find_element(By.XPATH, "//option[contains(text(),'Физическое лицо')]")
borrowerType_select.click()

# purpose_element = driver.find_element(By.ID, "PurposeId")
# purpose_element.click()
# choosing_purpose = driver.find_element(By.XPATH, "//option[contains(text(),'Прочие расходы')]")
# choosing_purpose.click()

# purposeAmount = driver.find_element(By.ID, "PurposeAmount")
# purposeAmount.send_keys("15000")

choose_tariff = driver.find_element(By.XPATH, "//button[@title='-- тариф не выбран --']")
choose_tariff.click()
select_simple_tariff = driver.find_element(By.XPATH, "(//span[contains(text(),'Простые')])[1]")
select_simple_tariff.click()
add_tariff = driver.find_element(By.XPATH, "//span[contains(text(),'Рондо 31/50 150 (30) (01.07.22)')]")
add_tariff.click()

term_loan = driver.find_element(By.ID, "Term")
term_loan.clear()
term_loan.send_keys("150")

amount_loan = driver.find_element(By.ID, "Amount")
amount_loan.clear()
amount_loan.send_keys("40000")

fact_amount = driver.find_element(By.ID, "RealAmount")
fact_amount.clear()
fact_amount.send_keys("40000")

nbki_check = driver.find_element(By.XPATH, "//input[@id='isConsentOfCreditHistoryDisclosureCheckbox']")
nbki_check.click()

submit_btn = driver.find_element(By.ID, "submitLoanBtn")
submit_btn.click()
alert_submit_btn = driver.find_element(By.CSS_SELECTOR, "button[data-bb-handler='confirm']")
alert_submit_btn.click()

time.sleep(2)
# driver.quit()
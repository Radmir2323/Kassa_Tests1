from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://localhost:65009/Reception/Client/Details/24500")

textfield_name = driver.find_element(By.ID, "un")
textfield_name.send_keys("ufa.u")
textfield_pass = driver.find_element(By.ID, "psw")
textfield_pass.send_keys("123456")
enter_loginBtn = driver.find_element(By.ID, "loginBtn")
enter_loginBtn.click()

# открытие страницы поиска клиентов
# issuance_loans_element = driver.find_element(By.CLASS_NAME, "list-group-item-heading")
# issuance_loans_element.click()
#
# # ввод паспортных данных клиента и открытие страницы клиента
# receptionSearch_element = driver.find_element(By.ID, "receptionSearch")
# receptionSearch_element.send_keys("8021"+"701456")
# receptionSearchSubmit_element = driver.find_element(By.ID, "receptionSearchSubmit")
# receptionSearchSubmit_element.click()
# time.sleep(25)
#
# choose_client = driver.find_element(By.CSS_SELECTOR, "a[href*='/Reception/Client/Details/17465']")
# choose_client.click()

# переход на страницу выдать заем
clientPhoto_upload = driver.find_element(By.ID, 'photoUpload')                  # загрузка(обновление) фото клиента перед выдачей займа
clientPhoto_upload.send_keys('C:/Users/Admin/PycharmProjects/beginSt/imagge/picture1.jpg')
give_loan_btn = driver.find_element(By.XPATH, '//button[contains(text(), "Выдать заём")]')
give_loan_btn.click()
give_loan_usual_btn = driver.find_element(By.CSS_SELECTOR, 'a[href="/Reception/Loan/Create/24500"]')
give_loan_usual_btn.click()

# страница выдачи заема

# выбор статуса лица(юр, физ и тд)
borrowerType_element = driver.find_element(By.ID, 'BorrowerType')
borrowerType_element.click()
borrowerType_select = driver.find_element(By.XPATH, "//option[contains(text(),'Физическое лицо')]")
borrowerType_select.click()

try:
    # "цель кредитования"
    purpose_element = driver.find_element(By.ID, "PurposeId")
    purpose_element.click()
    choosing_purpose = driver.find_element(By.XPATH, "//option[contains(text(),'Прочие расходы')]")
    choosing_purpose.click()
    # запрашиваемая сумма
    purposeAmount = driver.find_element(By.ID, "PurposeAmount")
    purposeAmount.send_keys("34000")
except:
    # выбор тарифа
    print("полей 'цель займа и запрашиваемая сумма нет'")
choose_tariff = driver.find_element(By.XPATH, "//button[@title='-- тариф не выбран --']")
choose_tariff.click()
select_simple_tariff = driver.find_element(By.XPATH, "//span[contains(text(),'Простые')]")
select_simple_tariff.click()
add_tariff = driver.find_element(By.XPATH, "//option[@value='1066']")
add_tariff.click()
# empty_zone = driver.find_element(By.XPATH, "//span[@id='select2-TariffId-container']")
# empty_zone.click()

# способ выдачи дс
give_cash = driver.find_element(By.XPATH, "//input[@value='Cash']")
give_cash.click()
# установка срока займа
term_loan = driver.find_element(By.ID, "Term")
term_loan.clear()
term_loan.send_keys("360")
# сколько денег дается
amount_loan = driver.find_element(By.ID, "Amount")
amount_loan.clear()
amount_loan.send_keys("20000")
# получение номера ордера
orderNumber_btn = driver.find_element(By.CSS_SELECTOR, "button[data-result-control='#Number']")
orderNumber_btn.click()
btn_confirm = driver.find_element(By.CSS_SELECTOR, "button[data-bb-handler='confirm']")
btn_confirm.click()
# сохранение заема
submit_btn = driver.find_element(By.ID, "submitLoanBtn")
submit_btn.click()
alert_submit_btn = driver.find_element(By.CSS_SELECTOR, "button[data-bb-handler='confirm']")
alert_submit_btn.click()
# выдача наличных
cash_btn = driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-warning'] a[class='btn btn-default']")
cash_btn.click()
btn_type_submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
btn_type_submit.click()
alert_ok_btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
alert_ok_btn.click()

# обновить страницу
driver.refresh()
driver.quit()
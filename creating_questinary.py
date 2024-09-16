import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# s = Service('Chromedriver PATH')
# driver = webdriver.Chrome(service=s)
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://localhost:65009/")

textfield_name = driver.find_element(By.ID, "un")
textfield_name.send_keys("ufa.u")
# textfield_name.send_keys("shagiev.r")
textfield_pass = driver.find_element(By.ID, "psw")
textfield_pass.send_keys("123456")
# textfield_pass.send_keys("Ruka1234!")
enter_loginBtn = driver.find_element(By.ID, "loginBtn")
enter_loginBtn.click()

issuance_loans_element = driver.find_element(By.CLASS_NAME, "list-group-item-heading")
issuance_loans_element.click()

# поиск клиента по паспорту для создания новой анкеты
receptionSearch_element = driver.find_element(By.ID, "receptionSearch")
receptionSearch_element.send_keys("0234567891")
receptionSearchSubmit_element = driver.find_element(By.ID, "receptionSearchSubmit")
receptionSearchSubmit_element.click()
# time.sleep(25)

new_client_btn = driver.find_element(By.CSS_SELECTOR, "a[class*=btn-lg]")
new_client_btn.click()

lastName_element = driver.find_element(By.ID, "LastName")
# рандом для фамилии
# letters_lastName = "абвгдежзиклмнопрстуфхчшщцэюя"
# lastName = letters_lastName
# letters_length = 3
# lastName_random = "".join(random.sample(lastName, letters_length))
# lastName_element.send_keys("бя" + lastName_random)
lastName_array = ["шадрин", "шаров", "чудов", "эдлин", "миров", "юсов", "царев", "цветков", "фурманов", "уфимцев", \
                  "турбин", "третьяк", "титов", "сурин", "славин", "розин", "романов", "потапов", "новак", "нильский"]
lastName_random_array = random.choice(lastName_array)
lastName_element.send_keys("НовЗалог-" + lastName_random_array)


firstName_element = driver.find_element(By.ID, "FirstName")
# рандом для имени
# letters_firstName = "абвгдежзиклмнопрстуфхчшщцэюя"
# letters_length_firstName = 4
# firstName_random = "".join(random.sample(letters_firstName, letters_length_firstName))
# firstName_element.send_keys(firstName_random)
firstName_array = ["витольд", "викентий", "герасим", "гавриил", "ефрем", "захар", "игнат", "капитон", "леонтий", "куприян", \
                  "мстислав", "нестор", "панкрат", "сайдулла", "рахмет", "севастьян", "тарас", "филипп", "яккуль", "хиромир", "брэдли", "стинг", "тюрон", "май"]
firstName_array_random = random.choice(firstName_array)
firstName_element.send_keys(firstName_array_random)

# # отчество клиента
middleName_element = driver.find_element(By.ID, "MiddleName")
# # middleName_element.send_keys("Андронович")
middleName_array = ["Борисович", "Дмитриевич", "Святославич", "Дорофеевич", "Никифорович", "Осипович", "Прохорович", "Ростиславович", "Иоаннович", "Леонович", \
                  "Федотович", "Тихонович", "Степанович", "Ваганович", "Ефимьевич", "Ааронович", "Арсенович", "Агович", "акулович", "паукович", "Кассович", "Денович", "Цаплевич"]
middleName_array_random = random.choice(middleName_array)
middleName_element.send_keys(middleName_array_random)

# дата рождения
dateOfBirth_element = driver.find_element(By.ID, "DateOfBirth")
dateOfBirth_element.click()
dateOfBirth_element.send_keys("16122000")

driver.execute_script("window.scrollBy(0, 100);")

passportSerial_element = driver.find_element(By.ID, "PassportSerial")
passportSerial_element.clear()
passportSerial_element.send_keys("8021")
passportNumber_element = driver.find_element(By.ID, "PassportNumber")
passportNumber_element.clear()

pass_number = random.randint(100000, 999999)   #рандом для номера паспорта
pass_number_str = str(pass_number)         #перевод int в string
passportNumber_element.send_keys(pass_number_str)

passportDepartamentCode_element = driver.find_element(By.ID, "PassportDepartamentCode")
passportDepartamentCode_element.send_keys("020-001")
passportDepartament_element = driver.find_element(By.ID, "PassportDepartament")
passportDepartament_element.send_keys("МВД ПО РЕСП. БАШКОРТОСТАН")

passportDate_element = driver.find_element(By.ID, "PassportDate")
passportDate_element.click()
passportDate_element.send_keys("16012021")

driver.execute_script("window.scrollBy(0, 300);")

# проверка старых паспортов
oldPassportUnchecked_element = driver.find_element(By.ID, "oldPassportUnchecked")
oldPassportUnchecked_element.click()
oldPassportsIsEmpty_element = driver.find_element(By.CSS_SELECTOR, "input[name*=OldPassportsIsEmpty]")
oldPassportsIsEmpty_element.click()

# место рождения
placeOfBirth_element = driver.find_element(By.ID, "PlaceOfBirth")
placeOfBirth_element.send_keys("-")

# адреса
passportAddress_Value_element = driver.find_element(By.ID, "PassportAddress_Value")
passportAddress_Value_element.send_keys("г Уфа, ул Ленина, д 16, кв 60")
# time.sleep(1)
copyAddress_element = driver.find_element(By.ID, "Address_Value")
copyAddress_element.send_keys("г Уфа, ул Ленина, д 16, кв 60")
#copyAddress_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Скопировать")
#copyAddress_element.click()
# time.sleep(1)

driver.execute_script("window.scrollBy(0, 500);")

mobileNumber_element = driver.find_element(By.ID, "MobileNumber")
mobileNumber_element.click()

# рандом для телефон. номера
phone_number = random.randint(100000000, 999999999)
phone_number_str = str(phone_number)
mobileNumber_element.send_keys("9" + phone_number_str)

driver.execute_script("window.scrollBy(0, 500);")

maritalStatus_element = driver.find_element(By.ID, "MaritalStatus")
select_maritalStatus = Select(maritalStatus_element)
select_maritalStatus.select_by_index(1)

# образование клиента
education_element = driver.find_element(By.ID, "Education")
select_education = Select(education_element)
select_education.select_by_index(4)

driver.execute_script("window.scrollBy(0, 500);")

# инн клиента ----- здесь не вводятся значения в поле ИНН
# inn_element = driver.find_element(By.ID, 'Inn')
# inn_element.send_keys('1234-123456-68')

# реклама, откуда клиент узнал о "Касса1"
# advld_element = driver.find_element(By.XPATH, "//div[text()='-- укажите рекламу --']")
advld_element = driver.find_element(By.ID, 'AdvId')
advld_element.click()
# choose_advld = driver.find_element(By.XPATH, "//div[contains(text(),'Газета')]")
choose_advld = driver.find_element(By.XPATH, "//option[contains(text(),'Газета')]")
choose_advld.click()

purposeId_element = driver.find_element(By.ID, "PurposeId")
select_purposeId = Select(purposeId_element)
select_purposeId.select_by_index(5)

driver.execute_script("window.scrollBy(0, 200);")

btn_submit_element = driver.find_element(By.CSS_SELECTOR, "button[type*=submit]")
btn_submit_element.click()

# driver.close()
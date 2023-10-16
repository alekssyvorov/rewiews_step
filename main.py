from random import randint
import requests
from bs4 import BeautifulSoup
import fake_useragent
from selenium.webdriver.support.wait import WebDriverWait
from json_data import *
from log_in import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support import expected_conditions as ec
from grades import result
from reviews_stud import write_reviews
url = "https://logbook.itstep.org/login/index#/"
group = input("Введите точное название группы ")
c_hw = int(input("Введите количество заданных(проверенных) ДЗ "))
c_cw = int(input('Введите количество проведенных уроков '))
count_items = int(input("Сколько предметов вы ведете? "))
# group = "КНК-11"
# c_hw = 1
# c_cw = 4
# count_items = 4
# login(url)
options = Options()
options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
options.add_experimental_option("excludeSwitches", ['enable-automation']);
# options.add_argument('--headless') # Скрыть браузер
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)
time.sleep(15)
ru = "/html/body/div/div/div/div/ul/li[1]/a"
log = '/html/body/div/div/form/div[1]/div/input'
pas = '/html/body/div/div/form/div[2]/div/input'

click_ru = driver.find_element(By.XPATH, ru)
click_ru.click()
time.sleep(25)
entry_login = driver.find_element(By.XPATH, log)
entry_login.send_keys(login_user)
entry_password = driver.find_element(By.XPATH, pas)
entry_password.send_keys(password_user)
button_enter = driver.find_element(By.XPATH, "/html/body/div/div/form/div[3]/button/span")
button_enter.click()

time.sleep(25) # Время на вход

# Переходим на страничку студенты
url_student = "https://logbook.itstep.org/#/students/list"
element = WebDriverWait(driver, 10).until(ec.url_changes(url_student))
driver.get(url_student)
time.sleep(25)

#Нажимаем на поле групп
field_group = '/html/body/main/div[2]/div/div[2]/div/div/div[1]/div/div[1]/md-select'
click_field_group = driver.find_element(By.XPATH, field_group).click()
time.sleep(30)
#Ищем поле поиска
search_group_X = "/html/body/div[4]/md-select-menu/md-content/md-select-header/input"
search_group = driver.find_element(By.XPATH, search_group_X)
search_group.send_keys(group)
time.sleep(3)
click_search_group_X = "/html/body/div[4]/md-select-menu/md-content/md-optgroup"
driver.find_element(By.XPATH, click_search_group_X).click()
time.sleep(20) # Время открытия группы

# Получаем список студентов
i = 1
stud_list = []
while True:
    name_X = f"/html/body/main/div[2]/div/div[2]/div/div/div[2]/div[{i}]/div/div[1]/div/div[2]/span"
    i += 1
    try:
        name = driver.find_element(By.XPATH, name_X).text
        stud_list.append(name)
    except:
        break
dict_stud = {}
j = 1
for i in stud_list:
    dict_stud[j] = i
    j += 1
print(dict_stud)


# Переходим в карточку студента
ball = 0
result_dict_home = {}
result_dict_class = {}

for i in range(1, len(stud_list)+1):
    student_X = f"/html/body/main/div[2]/div/div[2]/div/div/div[2]/div[{i}]/div/div[1]/div/div[2]/span"
    driver.find_element(By.XPATH, student_X).click()
    time.sleep(3)
    # Получаем средний бал
    ball_X = "/html/body/main/div[2]/div/div[3]/div/div/div[1]/div/div[4]/div[1]/div[2]"
    ball = driver.find_element(By.XPATH, ball_X).text
    ball = float(ball)
    # Получаем количество выполненных ДЗ
    count_bloc = 1
    count_hw = 0
    while True:
        try:
            bloc = f"/html/body/main/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[2]/table/tbody/tr[{count_bloc}]"
            driver.find_element(By.XPATH, bloc)
            count_bloc += 2
        except:
            print("Error")
            break
    count_bloc = int(count_bloc / 2)
    # Получаем список оценок за ДЗ
    count = -1
    lst = []
    while count <= (count_bloc * 2):
        count += 2
        try:
            field_hw_X = f"/html/body/main/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[2]/table/tbody/tr[{count}]/td[3]/div[1]/span"
            ocenka=driver.find_element(By.XPATH, field_hw_X).text
            lst.append(ocenka)
            print(f"Ocenka {ocenka}")
            count_hw += 1
        except:
            print("Нет оценки")

    count_class = -1
    lst_class = []
    count_class_work = 0
    while count_class <= (count_bloc * 2):
        count_class += 2
        try:
            work_class_X = f"/html/body/main/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[2]/table/tbody/tr[{count_class}]/td[3]/div[3]/span"
            class_ocenka = driver.find_element(By.XPATH, work_class_X).text
            lst_class.append(class_ocenka)
            print(f"Оценка в классе {class_ocenka}")
            count_class_work += 1
        except:
            print("Нет оценки")
    time.sleep(2)
    back_group_X = "/html/body/main/div[2]/div/div[1]/a/span"
    driver.find_element(By.XPATH, back_group_X).click()
    time.sleep(3)
    result_dict_home[stud_list[i-1]] = lst
    result_dict_class[stud_list[i-1]] = lst_class
# print(result_dict_home)
# print(result_dict_class)
# print(result(result_dict_home, result_dict_class, c_hw, c_cw))
result_date = result(result_dict_home, result_dict_class, c_hw, c_cw)
print(result_date)
#Вызываем функцию отзывов и передаем в нее данные
write_reviews(driver, stud_list, result_date, count_items)


driver.quit()
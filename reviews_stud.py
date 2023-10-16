from selenium.webdriver.common.by import By
import time
import pyautogui
from data import *


def writing_review(i, data):
    res = ""
    print(data)
    name, hw, cw = data[i][0], data[i][1], data[i][2]
    print("Распаковка", name, hw, cw)
    if hw > 10 and cw >= 4.5:  # Сильный студент
        res = f"{name}{strong_student()}"
    if 7 < hw <= 10:
        res = f"{name}{average_student_hw()}"
    if 0 < hw <= 7:
        res = f"{name}{weak_student_hw()}"
    if 4.5 < cw < 7:
        res += f"{strong_cw()}"
    if 3 < cw < 4.5:
        res += f"{average_student_cw()}"
    if 1 < cw <= 3:
        res += f"{weak_student_cw()}"
    if 0 <= cw <= 1:
        res += f"{cw_zero()}"
    return res


def write_reviews(driver, stud_list, result_date, count_items):
    for i in range(1, len(stud_list) + 1):
        time.sleep(3)
        student_X = f"/html/body/main/div[2]/div/div[2]/div/div/div[2]/div[{i}]/div/div[1]/div/div[2]/span"
        driver.find_element(By.XPATH, student_X).click()
        time.sleep(10)
        # Переходим в отзывы
        rev_X = "/html/body/main/div[2]/div/div[2]/ul/li[2]/a[1]"
        driver.find_element(By.XPATH, rev_X).click()
        time.sleep(5)
        # ПИШЕМ ОТЗЫВ
        # Поле предметы
        # subject_X = "/html/body/main/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/md-select"
        # driver.find_element(By.XPATH, subject_X).click()

        # Ищем пречень предметов

        if count_items == 1:
            subject_X = "/html/body/main/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/md-select"
            driver.find_element(By.XPATH, subject_X).click()
            time.sleep(2)
            subject_X = "/html/body/div[4]/md-select-menu/md-content/md-option/div[1]"
            driver.find_element(By.XPATH, subject_X).click()
            field_rev_X = "/html/body/main/div[2]/div/div[3]/div/div/div[2]/div[2]/div[2]/div[1]/md-input-container/div[1]/textarea"
            comment = driver.find_element(By.XPATH, field_rev_X)
            time.sleep(1)
            comment.send_keys(writing_review(i, result_date))
            time.sleep(1)
            # Кнопка Отправить

            time.sleep(5)
            btn_x = '//*[@id="reviews"]/div[2]/div[2]/button[2]'
            time.sleep(5)
            while True:
                try:
                    time.sleep(5)
                    btn_click = driver.find_element(By.XPATH, btn_x)
                    pyautogui.moveTo(500, 500, 2)
                    pyautogui.click()
                    print("Пытаемся кликнуть по ней")
                    time.sleep(5)
                    btn_click.click()
                    print("Клик прошел!!!!!!!!!!!!!!!!!")
                    time.sleep(5)
                    break
                except:
                    print("Не подходит ")
            time.sleep(3)
        else:
            print("Если предмет не 1")

            for j in range(2, count_items): # вернуть 1
                subject_X = "/html/body/main/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/md-select"
                driver.find_element(By.XPATH, subject_X).click()
                print(j)
                name_sub_X = f"/html/body/div[4]/md-select-menu/md-content/md-option[{j}]/div[1]"
                n = driver.find_element(By.XPATH, name_sub_X)
                time.sleep(3)
                n.click()
                time.sleep(2)
                field_rev_X = "/html/body/main/div[2]/div/div[3]/div/div/div[2]/div[2]/div[2]/div[1]/md-input-container/div[1]/textarea"

                # Вставить комментарий
                print("Вставить комментарий")
                comment = driver.find_element(By.XPATH, field_rev_X)
                time.sleep(1)
                comment.send_keys(writing_review(i, result_date))
                time.sleep(1)
                # Кнопка Отправить

                time.sleep(5)
                btn_x = '//*[@id="reviews"]/div[2]/div[2]/button[2]'
                time.sleep(5)
                while True:
                    try:
                        time.sleep(3)
                        btn_click = driver.find_element(By.XPATH, btn_x)
                        pyautogui.moveTo(500, 500, 2)
                        pyautogui.click()
                        print("Пытаемся кликнуть по ней")
                        time.sleep(3)
                        btn_click.click()
                        print("Клик прошел!!!!!!!!!!!!!!!!!")
                        time.sleep(5)
                        break
                    except:
                        print("Не подходит ")

        # Назад к группе
        print(" Мы уходим на страницу студентов ")
        time.sleep(5)
        back_group_X = "/html/body/main/div[2]/div/div[1]/a/span"
        driver.find_element(By.XPATH, back_group_X).click()

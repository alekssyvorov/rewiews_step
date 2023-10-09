from selenium.webdriver.common.by import By
import time
def write_reviews(driver, stud_list):
    for i in range(1, len(stud_list) + 1):
        time.sleep(3)
        print('TYT 1')
        student_X = f"/html/body/main/div[2]/div/div[2]/div/div/div[2]/div[{i}]/div/div[1]/div/div[2]/span"
        driver.find_element(By.XPATH, student_X).click()
        time.sleep(3)
        # Переходим в отзывы
        print('TYT 2')
        rev_X = "/html/body/main/div[2]/div/div[2]/ul/li[2]/a[1]"
        driver.find_element(By.XPATH, rev_X).click()
        time.sleep(5)
        print('TYT 3')
        # ПИШЕМ ОТЗЫВ
        # Поле предметы
        subject_X = "/html/body/main/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/md-select"
        driver.find_element(By.XPATH, subject_X).click()

        # Ищем пречень предметов
        # names_X = f"/html/body/div[4]/md-select-menu/md-content/md-option[{i}]/div[1]"
        count = 0
        while True:
            try:
                driver.find_element(By.XPATH, "/html/body/div[4]/md-select-menu/md-content/md-option").click()
                count = 1
            except:
                print("Всего 1 предмет ведете")
            try:
                count += 1
                names_X = f"/html/body/div[4]/md-select-menu/md-content/md-option[{count}]/div[1]"
                driver.find_element(By.XPATH, names_X)
            except:
                break
        print(count)
        subject_X = "/html/body/main/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/md-select"
        driver.find_element(By.XPATH, subject_X).click()
        time.sleep(1)
        for i in range(1, count):
            if count == 2:
                name_sub_X = "/html/body/div[4]/md-select-menu/md-content/md-option"
                n = driver.find_element(By.XPATH, name_sub_X)
                print(n)
                # time.sleep(1)
                # n.click()
                time.sleep(2)
            else:
                name_sub_X = f"/html/body/div[4]/md-select-menu/md-content/md-option[{i}]/div[1]"
                n = driver.find_element(By.XPATH, name_sub_X)
                time.sleep(1)
                n.click()
                time.sleep(2)


            field_rev_X = "/html/body/main/div[2]/div/div[3]/div/div/div[2]/div[2]/div[2]/div[1]/md-input-container/div[1]/textarea"

            #Вставить комментарий
            print("Вставить комментарий")
            comment = driver.find_element(By.XPATH, field_rev_X)
            time.sleep(1)
            comment.send_keys("Здесь будет отзыв")
            time.sleep(1)
            # Кнопка Отправить
            btn_x = "/html/body/main/div[2]/div/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/button[2]/span"
            btn_x = "/html/body/main/div[2]/div/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/button[2]"
            print("Здесь падаем?")
            driver.execute_script("window.scrollTo(0, 1080)")
            driver.find_element(By.XPATH, btn_x).click()

            print("Или вот здесь")
            # driver.find_element(By.LINK_TEXT, "Отправить")
            time.sleep(5)

        # Назад к группе
        back_group_X = "/html/body/main/div[2]/div/div[1]/a/span"
        driver.find_element(By.XPATH, back_group_X).click()
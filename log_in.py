from logopass import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


def login(url):
    options = Options()
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
    options.add_experimental_option("excludeSwitches", ['enable-automation']);
    # options.add_argument('--headless') # Скрыть браузер
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)
    time.sleep(2)
    log = '/html/body/div/div/form/div[1]/div/input'
    pas = '/html/body/div/div/form/div[2]/div/input'

    entry_login = driver.find_element(By.XPATH, log)
    entry_login.send_keys(login_user)
    entry_password = driver.find_element(By.XPATH, pas)
    entry_password.send_keys(password_user)
    button_enter = driver.find_element(By.XPATH, "/html/body/div/div/form/div[3]/button/span")
    button_enter.click()
    time.sleep(60)

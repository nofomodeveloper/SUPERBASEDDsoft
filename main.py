from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

chrome_service = Service('') #путь до хромдрайвера

def read_data_from_csv(file_path):
    data_list = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_list.append(row)
    return data_list

def register_account(data):
    driver = webdriver.Chrome(service=chrome_service)
    wait = WebDriverWait(driver, 30)  #можно увеличить время ожидания
    
    try:
        driver.get("https://6nok0qp4x1w.typeform.com/SUPERBASEDDWL")
        print("Opened the form")

        try:
            ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-qa="start-button" and contains(@class, "ButtonWrapper-sc-__sc-1qu8p4z-0") and contains(@class, "hRBHzH")]')))
            print("Start button found")
            ok_button.click()
        except Exception as e:
            print(f"Start button error: {e}")
            return
        
        # Заполнение Twitter
        try:
            twitter_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Type your answer here..."]')))
            print("Twitter field found")
            twitter_field.send_keys(data.get('twitter', ''))
            # Поиск и нажатие кнопки "OK" после ввода данных
            ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@data-qa, "ok-button-visible deep-purple-ok-button-visible") and contains(@class, "ButtonWrapper-sc-__sc-1qu8p4z-0") and contains(@class, "jMdgUv")]')))
            print("OK button found after Twitter field")
            ok_button.click()
        except Exception as e:
            print(f"Twitter field error: {e}")
        
        # Задержка
        print("Задержка перед заполнением следующего поля...")
        time.sleep(7)  # Можно настроить!!!!
        
        # Заполнение кошелька
        try:
            wallet_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Type your answer here..."]')))
            print("Wallet field found")
            wallet_field.send_keys(data.get('wallet', ''))
            # Поиск и нажатие кнопки "OK" после ввода данных
            ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@data-qa, "ok-button-visible deep-purple-ok-button-visible") and contains(@class, "ButtonWrapper-sc-__sc-1qu8p4z-0") and contains(@class, "jMdgUv")]')))
            print("OK button found after Wallet field")
            ok_button.click()
        except Exception as e:
            print(f"Wallet field error: {e}")
        
        # Задержка
        print("Задержка перед заполнением следующего поля...")
        time.sleep(7)  # Можно настроить!!!!
        
        # Заполнение почты
        try:
            email_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="name@example.com"]')))
            print("Email field found")
            email_field.send_keys(data.get('email', ''))
            # Поиск и нажатие кнопки "OK" после ввода данных
            ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@data-qa, "ok-button-visible deep-purple-ok-button-visible") and contains(@class, "ButtonWrapper-sc-__sc-1qu8p4z-0") and contains(@class, "jMdgUv")]')))
            print("OK button found after Email field")
            ok_button.click()
        except Exception as e:
            print(f"Email field error: {e}")
        
        # Задержка
        print("Задержка перед заполнением следующего поля...")
        time.sleep(7)  # Можно настроить!!!!
        
        # Заполнение Discord
        try:
            discord_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Type your answer here..."]')))
            print("Discord field found")
            discord_field.send_keys(data.get('discord', ''))
            ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-qa="submit-button deep-purple-submit-button"]')))
            print("Submit button found after Discord field")
            ok_button.click()
        except Exception as e:
            print(f"Discord field error: {e}")
        
        time.sleep(10) 

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()

data_list = read_data_from_csv('') #путь до CSV файла в котором хранятся данные аккаунтов
for data in data_list:
    register_account(data)
    time.sleep(20)

print("Регистрация завершена для всех записей.")


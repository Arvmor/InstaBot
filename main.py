from selenium import webdriver
from selenium.webdriver.common.by import By
from signal import signal, SIGINT
from time import sleep
from os import system
from credentials import account
# functions


def signal_handler(signal, frame):  # Handle Ctrl-C
    # system("sudo service apache2 stop")
    driver.close()
    exit(0)


def login(accountNumber):  # Login function
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(account[accountNumber][0])
    sleep(2)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(account[accountNumber][1])
    sleep(2)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button'
    ).click()


# Driver settings
chromedriver = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--log-level=OFF")
driver = webdriver.Chrome("chromedriver", options=chrome_options)
driver.get("https://www.instagram.com/accounts/login/")

driver.close()

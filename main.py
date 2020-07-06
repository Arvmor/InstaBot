from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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
    sleep(5)
    # Close the annoying alerts
    driver.refresh()
    if driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/section/div/div[2]').text == 'Save Your Login Info?':
        driver.find_element(
            By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button'
        ).click()
    if driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[2]/h2').text == 'Turn on Notifications':
        driver.find_element(
            By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]'
        ).click()


# Driver settings
chromedriver = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.page_load_strategy = 'eager'
chrome_options.add_argument("--log-level=OFF")
driver = webdriver.Chrome("chromedriver", options=chrome_options)
driver.get("https://www.instagram.com/accounts/onetap/")
# Main code
try:
    login(0)
    sleep(5)
    driver.close()
except:
    print("Crashed !")
    driver.close()

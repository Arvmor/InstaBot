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
    print("Closing the script")
    driver.close()
    exit(0)


def login(numberOfAccount):  # Login function
    sleep(2)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(account[numberOfAccount][0])
    sleep(2)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(account[numberOfAccount][1])
    sleep(2)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button'
    ).click()
    sleep(5)


def sendComment(commentText, postURL):  # Send Comments
    driver.get(postURL)
    sleep(3)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea').send_keys(commentText)
    sleep(10)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button').click()


def sendLike(postURL):  # Like the post
    driver.get(postURL)
    sleep(3)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button').click()


# Driver settings
chromedriver = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument(
    "user-data-dir=/home/r00t/.config/chromium/")
chrome_options.add_argument("--log-level=OFF")
driver = webdriver.Chrome("chromedriver", options=chrome_options)
driver.get("https://www.instagram.com")

# Main code
login(1)
sendComment(
    "Post Zibayi bood !", 'https://www.instagram.com/p/CBELcX9F361/')
sendLike('https://www.instagram.com/p/CBELcX9F361/')
driver.close()

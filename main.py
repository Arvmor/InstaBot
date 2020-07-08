#!/usr/bin/env python3
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
    driver.quit()
    exit(0)


def load(filename):
    f = open(f"./userInputs/{filename}.txt", "r")
    cPlace = ''
    for l in f:
        cPlace += l
    f.close()
    return cPlace


def login(numberOfAccount):  # Login function
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
    print(f"Loged in with {account[numberOfAccount][0]}")


def sendComment(commentText, postURL):  # Send Comments
    driver.get(postURL)
    sleep(3)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea').send_keys(commentText)
    sleep(3)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button').click()
    print(f"Commented {commentText} on this post {postURL}")
    sleep(5)


def sendLike(postURL=None, samePost=False):  # Like the post
    if samePost == False:
        driver.get(postURL)
    sleep(3)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button').click()
    print(f"liked this post {postURL}")
    sleep(3)


def sendReplay(postURL=None, samePost=False, commentNumber=1, commentText="GJ !"):
    if samePost == False:
        driver.get(postURL)
    sleep(3)
    driver.find_element(
        By.XPATH, f'//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/div[1]/ul/ul[{commentNumber}]/div/li/div/div[1]/div[2]/div/div/button').location_once_scrolled_into_view()
    driver.find_element(
        By.XPATH, f'//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/div[1]/ul/ul[{commentNumber}]/div/li/div/div[1]/div[2]/div/div/button').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea').send_keys(commentText)
    sleep(3)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button').click()
    print(f"Replayed to this post {postURL}")
    sleep(3)

    # Driver settings
chromedriver = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("user-data-dir=/home/r00t/.config/chromium/")
chrome_options.add_argument("--log-level=OFF")
driver = webdriver.Chrome("chromedriver", options=chrome_options)
driver.get("https://www.instagram.com/accounts/logout")
sleep(5)

# Main code
try:
    numberOfAccount = int(load("accountNumber"))
    login(numberOfAccount)
    commentText = load("commentText")
    postURL = load("postURLText")
    sendComment(commentText, postURL)
    sendLike(postURL=postURL, samePost=True)
    sendReplay(postURL=postURL, samePost=True,
               commentNumber=2, commentText="salam")
    driver.quit()
except:
    print("Crashed !")
    driver.quit()

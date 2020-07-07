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
    f = open(f"./webPanel/{filename}.txt", "r")
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
    sleep(10)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea').send_keys(commentText)
    sleep(3)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button').click()
    print(f"Commented {commentText} on this post {postURL}")
    sleep(10)


def sendLike(postURL):  # Like the post
    driver.get(postURL)
    sleep(10)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button').click()
    print(f"liked this post {postURL}")
    sleep(10)


# Driver settings
chromedriver = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("user-data-dir=~/.config/chromium/")
chrome_options.add_argument("--log-level=OFF")
driver = webdriver.Chrome("chromedriver", options=chrome_options)
driver.get("https://www.instagram.com/accounts/logout")
sleep(15)

# Main code
try:
    numberOfAccount = int(input("Which Account: "))
    login(numberOfAccount)
    commentText = load("commentText")
    postURL = input("Which Post: ")
    sendComment(commentText, postURL)
    sendLike(postURL)
    driver.quit()
except:
    print("Crashed !")
    driver.quit()

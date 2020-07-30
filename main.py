#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from PIL import Image, ImageDraw, ImageFont
from signal import signal, SIGINT
from arabic_reshaper import reshape
from bidi.algorithm import get_display
from time import sleep
from os import system
from credentials import account
from random import choice
from sys import argv
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
    driver.get('https://www.instagram.com/accounts/login/')
    sleep(10)
    driver.find_element(
        By.NAME, 'username').send_keys(account[numberOfAccount][0])
    sleep(2)
    driver.find_element(
        By.NAME, 'password').send_keys(account[numberOfAccount][1])
    sleep(2)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/main/article/div/div/div/form/div[5]/button'
    ).click()
    sleep(5)
    print(f"Logged in with {account[numberOfAccount][0]}")


def sendComment(commentText, postURL):  # Send Comments
    driver.get(postURL)
    sleep(10)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').send_keys(commentText)
    sleep(3)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button').click()
    print(f"Commented {commentText} on this post {postURL}")
    sleep(10)


def sendLike(postURL=None, samePost=False):  # Like the post
    if samePost == False:
        driver.get(postURL)
    sleep(10)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
    print(f"liked this post {postURL}")
    sleep(5)


def sendReplay(postURL=None, samePost=False, commentNumber=1, commentText="GJ !"):
    if samePost == False:
        driver.get(postURL)
    sleep(3)
    driver.find_element(
        By.XPATH, f'/html/body/div[1]/section/main/div/div[1]/article/div[3]/div[1]/ul/ul[{commentNumber}]/div/li/div/div[1]/div[2]/div/div/button').location_once_scrolled_into_view()
    driver.find_element(
        By.XPATH, f'/html/body/div[1]/section/main/div/div[1]/article/div[3]/div[1]/ul/ul[{commentNumber}]/div/li/div/div[1]/div[2]/div/div/button').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea').send_keys(commentText)
    sleep(3)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button').click()
    print(f"Replayed to this post {postURL}")
    sleep(5)


def forwardPost(postURL=None, samePost=False, username=None):
    if samePost == False:
        driver.get(postURL)
    sleep(3)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/button').click()
    sleep(3)
    driver.find_element(
        By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div[1]/div/div/div[2]').click()
    sleep(3)
    driver.find_element(
        By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(username)
    sleep(3)
    driver.find_element(
        By.XPATH, '/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()


def follow(username):
    driver.get(f"https://www.instagram.com/{username}/")
    sleep(5)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button').click()
    sleep(5)


def unfollow(username):
    driver.get(f"https://www.instagram.com/{username}/")
    sleep(5)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button').click()
    sleep(2)
    driver.find_element(
        By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[1]').click()
    sleep(5)


def CreateImage(text):
    if text == None:
        return "crash"
    image = Image.open(
        "/home/r00t/Desktop/Coding/GitHub/InstaBot/webPanel/bg.jpg")
    draw = ImageDraw.Draw(image)
    draw.text((640, 360), get_display(reshape(text)), (255, 255, 255),
              font=ImageFont.truetype("/home/r00t/Desktop/Coding/GitHub/InstaBot/webPanel/Yekan.ttf", 18))
    draw = ImageDraw.Draw(image)
    image.save(f"/tmp/{argv[1]}InstaImage.png")


def pickPost(channel, pattern=None):
    # it will pick a random post from telegram channel which in here is our Post source
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(f"https://t.me/{channel}")
    # Find last post id
    postHref = driver.find_element(
        By.XPATH, '/html/body/main/div/section/div[20]/div[1]/div[2]/div[3]/div/span[3]/a').get_attribute("href")
    postID = ''
    for l in range(len(postHref)):
        if postHref[-l] != '/':
            postID += postHref[-l]
        else:
            break
    # Find Text Caption or Image
    driver.get(f"https://t.me/{channel}/{postID}")
    sleep(10)
    try:
        driver.switch_to.frame(
            driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div[2]/div[1]/iframe",
            )
        )
    except:
        return
    postText = driver.find_element(
        By.XPATH, '/html/body/div/div[2]/div[2]').text.strip()
    try:
        if driver.find_element(
                By.XPATH, '/html/body/div/div[2]/a/div[1]/video'):
            return
    except:
        try:
            if driver.find_element(
                    By.XPATH, '/html/body/div/div[2]/a').get_attribute("style")[37:-3] != '':
                return
        except:
            return postText


def sendPost(caption=None):
    if checkForCrashed == "crash":
        return
    driver.find_element(By.XPATH, '/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]').send_keys(
        f'/tmp/{argv[1]}InstaImage.png')
    sleep(5)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/div[1]/header/div/div[2]/button').click()
    sleep(5)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea').send_keys(caption)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/div[1]/header/div/div[2]/button').click()
    sleep(60)


# Driver settings
chromedriver = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument(
    "--user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36")
chrome_options.add_argument("--log-level=OFF")
driver = webdriver.Chrome("chromedriver", options=chrome_options)
signal(SIGINT, signal_handler)  # Handle Ctrl-C

# Main code
try:
    # numberOfAccount = int(load("accountNumber"))
    # commentText = load("commentText")
    # postURL = load("postURLText")
    login(int(argv[1]))
    # checkForCrashed = CreateImage(pickPost('sigarism'))
    # sendPost()
    # sendComment(commentText, postURL)
    # sendLike(postURL=postURL, samePost=True)
    # sendReplay(postURL=postURL, samePost=True, commentNumber=2, commentText="salam")
    # forwardPost(postURL=postURL, samePost=True, username="9gag")
    # follow("9gag")
    # unfollow("instagram")
    driver.quit()
except Exception as excep:
    print(excep)
    driver.quit()

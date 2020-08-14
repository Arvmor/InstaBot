#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from signal import signal, SIGINT
from time import sleep
from os import system, getcwd
from importlib import reload
import credentials
from random import choice
from sys import argv
from re import sub
# functions


def writeFile(variableName, mode):  # save data into file
    if mode == "post":
        with open(f"./CreateImage.html", "+w") as fileHandle:
            for d in variableName:
                fileHandle.write("%s" % d)
            fileHandle.close()
    elif mode == "story":
        with open(f"./CreateStory.html", "+w") as fileHandle:
            for d in variableName:
                fileHandle.write("%s" % d)
            fileHandle.close()


def signal_handler(signal, frame):  # Handle Ctrl-C
    # system("sudo service apache2 stop")
    system(f'rm /tmp/{argv[1]}InstaImage.png')
    system(f'rm /tmp/{argv[1]}InstaStory.png')
    print("\nClosing the script")
    driver.quit()
    exit(0)


def login(numberOfAccount):  # Login function
    global sessionId
    driver.get('https://www.instagram.com/accounts/logout/')
    sleep(5)
    driver.get('https://www.instagram.com/accounts/login/')
    sleep(10)
    driver.find_element(
        By.NAME, 'username').send_keys(credentials.account[numberOfAccount][0])
    sleep(2)
    driver.find_element(
        By.NAME, 'password').send_keys(credentials.account[numberOfAccount][1], Keys.RETURN)
    sleep(10)
    print(f"Logged in with {credentials.account[numberOfAccount][0]}")
    sessionId = driver.get_cookies()[6]['value']


def follow(username):
    errors = 0
    driver.get(f"https://www.instagram.com/{username}/")
    print(f"Going for follow {username}")
    sleep(10)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/header/section/ul/li[2]').click()
    sleep(5)
    for i in range(1, 16):
        try:
            driver.find_element(
                By.XPATH, f'/html/body/div[4]/div/div/div[2]/ul/div/li[{i}]/div/div[3]/button').click()
            sleep(3)
        except:
            errors += 1
            if errors >= 8:
                break
            if driver.find_elements(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]'):
                driver.find_element(
                    By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]').click()
                sleep(4)


def CreateImage(mode, text, background, color=None):
    if text == "failed !" or text == None:
        raise Exception("failed to get post")
    # Create a HTML file
    html = """<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <style>
                        @font-face {
                                font-family: "myFont";
                                src: url("./webPanel/Tanha.ttf");
                        }

                        @font-face {
                                font-family: "myFont2";
                                src: url("./webPanel/MyFont.woff2");
                        }
                            body {"""+f"""
                                background-image: url({background});
                                background-repeat: no-repeat;
                                overflow-y: hidden;
                                overflow-x: hidden;
                                """+"""}
                        </style>
                </head>
                <body>
                <div dir="rtl" style="
                        font-family: myFont;
                        font-size:3vw;
                        margin: 0;
                        position: absolute;
                        top: 50%;
                        left: 50%;
                        -ms-transform: translate(-50%, -50%);
                        transform: translate(-50%, -50%);
                        text-align: center;"""
    if mode == "post":
        if color != None:
            html += f"""color: {credentials.account[int(argv[1])][4][color]};">"""
        else:
            html += f"""color: {credentials.account[int(argv[1])][4][0]};">"""
        html += f"""{text}</div>
            <div style="
            font-family: myFont2;
            position: absolute;
            {credentials.account[int(argv[1])][5][0]}
            ">
            <strong>@{credentials.account[int(argv[1])][0]}</strong>
            </div></body></html>"""
        # Create image
        writeFile(html, "post")
        driver.get(f'file:///{getcwd()}/CreateImage.html')
        driver.set_window_size(640, 640)
        sleep(5)
        driver.save_screenshot(f"/tmp/{argv[1]}InstaImage.png")
    elif mode == "story":
        html += f"""color: {credentials.account[int(argv[1])][4][1]};">{text}</div><div style="font-family: myFont2;position: absolute;{credentials.account[int(argv[1])][5][1]}"><strong>@{credentials.account[int(argv[1])][0]}</strong></div></body></html>"""
        # Create image
        writeFile(html, "story")
        driver.get(f'file:///{getcwd()}/CreateStory.html')
        driver.set_window_size(1242, 2208)
        sleep(5)
        driver.save_screenshot(f"/tmp/{argv[1]}InstaStory.png")
    sleep(5)
    driver.set_window_size(438, 894)


def pickPost(oldPost=0):
    # select random Channel
    chosen = choice(credentials.channels[credentials.account[int(argv[1])][2]])
    print(chosen)
    channel = chosen[0]
    pattern = chosen[1]
    # it will pick a random post from telegram channel which in here is our Post source
    driver.get(f"https://t.me/s/{channel}")
    # Find last post id
    postHref = driver.find_element(
        By.XPATH, '/html/body/main/div/section/div[20]/div[1]/div[2]/div[3]/div/span[3]/a').get_attribute("href")
    postID = 0
    for l in range(1, len(postHref)):
        if postHref[-l] != '/':
            postID -= 1
        else:
            postID = postHref[postID:]
            break
    # Find Text Caption
    driver.get(f"https://t.me/{channel}/{int(postID)-oldPost}")
    sleep(10)
    try:
        driver.switch_to.frame(
            driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div[2]/div[1]/iframe",
            )
        )
    except:
        return "failed !"
    postText = driver.find_element(
        By.XPATH, '/html/body/div/div[2]/div[2]').text.strip()
    try:
        if driver.find_element(
                By.XPATH, '/html/body/div/div[2]/a/div[1]/video'):
            return "failed !"
    except:
        try:
            if driver.find_element(
                    By.XPATH, '/html/body/div/div[2]/a').get_attribute("style")[37:-3] != '':
                return "failed !"
        except:
            newLineCounter = 0
            if pattern == 0:
                for l in range(1, len(postText)):
                    if postText[-l] == '\n':
                        l -= 1
                        newLineCounter += 1
                    if newLineCounter == 2:
                        break
                postText = postText[:-l]
            elif pattern == 1:
                ch = -24
                while abs(ch) != len(postText):
                    if postText[ch] == '》' or postText[ch] == '×' or postText[ch] == '•' or postText[ch] == '»' or postText[ch] == '*' or postText[ch] == '※' or postText[ch] == '☆':
                        postText = postText[:ch]
                    ch -= 1
                postText = postText.strip()
                ch = -1
                while abs(ch) != len(postText):
                    if postText[ch] == '×' or postText[ch] == '•' or postText[ch] == '*' or postText[ch] == '※' or postText[ch] == '☆':
                        postText = postText[:ch]
                    ch -= 1
                postText = postText.strip()
            # Filter Text for last time
            for s in range(1, len(postText)):
                if postText[-s] == '@':
                    return "failed !"
            # clean the text
            postText = sub('\n\n+', '<br><br>',
                           postText.strip()).replace('\n', '<br>')
            if len(postText) <= 10 or len(postText) >= 500:
                return "failed !"
            # check if text is already posted
            textFile = open(f"text{argv[1]}.txt", '+r')
            txtFile = textFile.read()
            textFile.close()
            if postText == txtFile:
                return "failed !"
            textFile = open(f"text{argv[1]}.txt", '+w')
            textFile.write(postText)
            textFile.close()
            return postText


def sendPost(caption=credentials.captions[int(argv[1])]):
    driver.get(
        f"https://www.instagram.com/{credentials.account[int(argv[1])][0]}")
    sleep(5)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/nav[2]/div/div/form/input').send_keys(f'/tmp/{argv[1]}InstaImage.png')
    sleep(15)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
    sleep(10)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea').send_keys(caption)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
    sleep(60)
    print("Uploaded Post")
    system(f'rm /tmp/{argv[1]}InstaImage.png')


def storyWebsite():
    # create email
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    emailAddress = ''
    for _ in range(16):
        emailAddress += choice(alphabet)
    driver.get("https://www.moakt.com/")
    print(f"Creating Email {emailAddress}@moakt.cc")
    sleep(5)
    driver.find_element(
        By.XPATH, '/html/body/div/div[1]/div[2]/div/div/form/span[3]/input').send_keys(emailAddress)
    driver.find_element(
        By.XPATH, '/html/body/div/div[1]/div[2]/div/div/form/input[2]').click()
    sleep(5)
    # Sign up
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://app.storrito.com/#/login")
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[2]/button').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div/input').send_keys(f"{emailAddress}@moakt.cc")
    sleep(5)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/button').click()
    sleep(30)
    # Get verify link
    driver.switch_to.window(driver.window_handles[0])
    sleep(2)
    driver.find_element(
        By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[1]/a[2]').click()
    sleep(2)
    driver.find_element(
        By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[1]/a').click()
    sleep(2)
    driver.switch_to.frame(
        driver.find_element(
            By.XPATH,
            "/html/body/div/div[1]/div[2]/div/div[3]/div[2]/iframe",
        )
    )
    driver.find_element(
        By.XPATH, '/html/body/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/table/tbody/tr/td/span/a').click()
    # add Instagram account
    driver.switch_to.window(driver.window_handles[2])
    sleep(20)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div[2]/div/aside/div/div[1]/a[5]/div').click()
    sleep(20)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[1]/button[2]').click()
    sleep(10)
    for char in sessionId:
        driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/div/form/div/input').send_keys(char)
        sleep(choice(range(1, 5)))
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div[1]/div/div/form/button[1]').click()
    sleep(10)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/button').click()
    # upload story image
    driver.get("https://app.storrito.com/#/gallery")
    sleep(20)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(f'/tmp/{argv[1]}InstaStory.png')
    sleep(60)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/img').click()
    sleep(20)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[1]/div[2]/div[1]/div/button').click()
    sleep(10)
    driver.find_element(
        By.XPATH, f'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div/div/select/option[text()="{credentials.account[int(argv[1])][0]}"]').click()
    sleep(10)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[3]/div/nav/div/div/div/button[1]').click()
    sleep(10)
    btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[3]/div/div/button')))
    btn.click()
    sleep(20)
    print("Uploaded Story")
    system(f'rm /tmp/{argv[1]}InstaStory.png')


signal(SIGINT, signal_handler)  # Handle Ctrl-C

# Variables
chromedriver = "chromedriver.exe"
TotalRunTime = 10
runtimehour = 0
sessionId = ''
posted = False
followed = False
storied = False
headlessChrome = webdriver.ChromeOptions()
headlessChrome.add_argument("--headless")
headlessChrome.add_argument("--no-sandbox")
headlessChrome.add_argument("--disable-dev-shm-usage")
headlessChrome.add_argument(
    "--user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36")
headlessChrome.add_argument("--log-level=3")
headlessChrome.add_argument("--log-level=OFF")
noneHeadlessChrome = webdriver.ChromeOptions()
noneHeadlessChrome.add_argument("--headless")
noneHeadlessChrome.add_argument("--no-sandbox")
noneHeadlessChrome.add_argument("--disable-dev-shm-usage")
noneHeadlessChrome.add_argument("--window-size=1920,1080")
noneHeadlessChrome.add_argument("--disable-extentions")
noneHeadlessChrome.add_argument("--start-maximized")
noneHeadlessChrome.add_argument("--ignore-certificate-errors")
noneHeadlessChrome.add_argument("--log-level=3")
noneHeadlessChrome.add_argument("--log-level=OFF")

# Main code
while True:
    if runtimehour == TotalRunTime:
        runtimehour = 0
        sleep(choice(range(50000, 50800)))
    while True:
        try:
            # Create Image for post
            if not posted:
                driver = webdriver.Chrome(
                    "chromedriver", options=headlessChrome)
                if credentials.account[int(argv[1])][3] == 1:
                    with open(f"./userInputs/bgUser{argv[1]}.txt", "r+") as f:
                        data = int(f.read())
                        f.seek(0)
                        CreateImage(
                            "post", pickPost(), f'./CreateImage/{argv[1]}-{data%2}.png', data % 2)
                        f.write(str(data + 1))
                        f.truncate()
                else:
                    CreateImage(
                        "post", pickPost(), f'./CreateImage/{argv[1]}.png')
                # Upload the created image
                login(int(argv[1]))
                sendPost()
                driver.quit()
            posted = True
            # Upload a new Story
            if not storied:
                driver = webdriver.Chrome(
                    "chromedriver", options=headlessChrome)
                CreateImage(
                    "story", pickPost(), f'./CreateImage/s{argv[1]}.png')
                driver.quit()
                driver = webdriver.Chrome(
                    "chromedriver", options=noneHeadlessChrome)
                storyWebsite()
                driver.quit()
            storied = True
            # Follow few pages
            if not followed:
                driver = webdriver.Chrome(
                    "chromedriver", options=headlessChrome)
                login(int(argv[1]))
                follow(
                    choice(credentials.followSource[credentials.account[int(argv[1])][2]]))
                driver.quit()
            followed = True
            # going for the next round
            runtimehour += 1
            if runtimehour == TotalRunTime:
                break
            print(f"All done ! {runtimehour}/{TotalRunTime}")
            # here you can set the delay time
            sleep(choice(range(3400, 3800)))
            posted = False
            followed = False
            storied = False
            reload(credentials)
        except Exception as excep:
            print(excep)
            driver.quit()
            break

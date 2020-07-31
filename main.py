#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from signal import signal, SIGINT
from time import sleep
from os import system, getcwd
from importlib import reload
import credentials
from random import choice
from sys import argv

# functions


def writeFile(variableName):  # save data into file
    with open(f"./CreateImage.html", "+w") as fileHandle:
        for d in variableName:
            fileHandle.write("%s" % d)
        fileHandle.close()


def signal_handler(signal, frame):  # Handle Ctrl-C
    # system("sudo service apache2 stop")
    system(f'rm /tmp/{argv[1]}InstaImage.png')
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
        By.NAME, 'username').send_keys(credentials.account[numberOfAccount][0])
    sleep(2)
    driver.find_element(
        By.NAME, 'password').send_keys(credentials.account[numberOfAccount][1])
    sleep(2)
    try:
        driver.find_element(
            By.XPATH, '//*[@id="react-root"]/section/main/article/div/div/div/form/div[5]/button'
        ).click()
    except:
        driver.find_element(
            By.XPATH, '/html/body/div[1]/section/main/article/div/div/div/form/div[7]/button'
        ).click()
    sleep(20)
    print(f"Logged in with {credentials.account[numberOfAccount][0]}")


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
    sleep(10)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/section/main/div/ul/li[2]/a').click()
    sleep(5)
    for i in range(2, 16):
        driver.find_element(
            By.XPATH, f'//*[@id="react-root"]/section/main/div/ul/div/li[{i}]/div/div[2]/button').click()
        sleep(2)


def unfollow(username):
    driver.get(f"https://www.instagram.com/{username}/")
    sleep(5)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button').click()
    sleep(2)
    driver.find_element(
        By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[1]').click()
    sleep(5)


def CreateImage(text, background, color=None):
    if text == None:
        return "crash"
    if credentials.account[int(argv[1])][3] == 1:
        html = """<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <style>
                                @font-face {
                                    font-family: "myFont";
                                    src: url("./webPanel/Tanha.ttf");
                                }
                                body {"""+f"""
                                    background-image: url({background});
                                    background-repeat: no-repeat;
                                    overflow-y: hidden;
                                    overflow-x: hidden;
                                    """+"""}
                            </style>
                    </head>
                    <body>"""+f"""
                    <div style="
                            font-family: myFont;
                            font-size:4vw;
                            margin: 0;
                            position: absolute;
                            top: 50%;
                            left: 50%;
                            -ms-transform: translate(-50%, -50%);
                            transform: translate(-50%, -50%);
                            text-align: center;
                            color: {credentials.account[int(argv[1])][4][color]};
                            ">
                            {text}
                            </div>
                    </body>
                    </html>"""
    else:
        html = """<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <style>
                        @font-face {
                            font-family: "myFont";
                            src: url("./webPanel/Tanha.ttf");
                        }
                        body {"""+f"""
                            background-image: url('{background}');
                            background-repeat: no-repeat;
                            overflow-y: hidden;
                            overflow-x: hidden;
                            """+"""}
                    </style>
            </head>
            <body>"""+f"""
            <div style="
                    font-family: myFont;
                    font-size:4vw;
                    margin: 0;
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    -ms-transform: translate(-50%, -50%);
                    transform: translate(-50%, -50%);
                    text-align: center;
                    color: {credentials.account[int(argv[1])][4][0]};
                    ">
                    {text}
                    </div>
            </body>
            </html>"""
    # Create image
    writeFile(html)
    driver.get(f'file:///{getcwd()}/CreateImage.html')
    driver.set_window_size(640, 640)
    sleep(5)
    driver.save_screenshot(f"/tmp/{argv[1]}InstaImage.png")
    sleep(5)
    driver.set_window_size(438, 894)


def pickPost():
    # select random Channel
    chosen = choice(credentials.channels[credentials.account[int(argv[1])][2]])
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
            newLineCounter = 0
            if pattern == 0:
                for l in range(1, len(postText)):
                    if postText[-l] == '\n':
                        l -= 1
                        newLineCounter += 1
                    if newLineCounter == 2:
                        break
            return postText[:-l]


def sendPost(caption=credentials.captions[int(argv[1])]):
    if checkForCrashed == "crash":
        return
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
    system(f'rm /tmp/{argv[1]}InstaImage.png')


def clear():  # will close useless tabs
    sleep(1)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


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
signal(SIGINT, signal_handler)  # Handle Ctrl-C

# Variables
driver = webdriver.Chrome("chromedriver", options=chrome_options)
TotalRunTime = 10
runtimehour = 0

# Main code
while True:
    if runtimehour == TotalRunTime:
        runtimehour = 0
        sleep(choice(range(50000, 50800)))
    while True:
        try:
            # Create Image (check if background changes)
            if credentials.account[int(argv[1])][3] == 1:
                with open(f"./userInputs/bgUser{argv[1]}.txt", "r+") as f:
                    data = int(f.read())
                    f.seek(0)
                    f.write(str(data + 1))
                    f.truncate()
                checkForCrashed = CreateImage(
                    pickPost(), f'./CreateImage/{argv[1]}-{data%2}.png', data % 2)
            else:
                checkForCrashed = CreateImage(
                    pickPost(), f'./CreateImage/{argv[1]}.png')
            # Login
            login(int(argv[1]))
            # Upload the created image
            sendPost()
            # Follow few pages
            follow(
                choice(credentials.followSource[credentials.account[int(argv[1])][2]]))
            # going for the next round
            runtimehour += 1
            print(f"All done ! {runtimehour}/{TotalRunTime}")
            if runtimehour == TotalRunTime:
                break
            driver.quit()
            # here you can set the delay time
            sleep(choice(range(3400, 3800)))
            reload(credentials)
            driver = webdriver.Chrome("chromedriver", options=chrome_options)
        except Exception as excep:
            print(excep)

# This script extracts the Name, Title, Email and Phone number from a Slack Account

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# *** below are the 6 variables that you need to define for this script to work *** :

slackEmail = ""
# your email used to login
slackPassword = ""
# your password used to login
baseUrl = ""
# this baseUrl included the team code - format is "https://<team>.slack.com/messages/<team code>/team/"
baseUrlWithoutTeamCode = ""
# this baseUrl format is "https://<team>.slack.com/"
driver = webdriver.Chrome(executable_path=r'C:\Program Files\chromedriver.exe') # this happened to be a windows device
# you need to install chrome driver to your computer and point to it's location here
harFileName = ""
# created per tbe below 6 steps

### ~~~ You can replace the 6 spaces inbetween each of the printed out contact details with a 'tab'   ###
### ~~~ and paste all the data into an excel document  (if you like...)   ###

#   To get the below list of Slack User ID's (create a .HAR file):
# 1. go to the slack website for a group, usually https://< id >.slack.com/messages, sign in
# 2. Click on a Channel's members link, a person icon and then see the "___ Members" on the right
# 3. With the chrome dev tools open and the network options selected, click on the 'See all __ Members' button
# 4. Scroll through this full list of Slack Group members, noting the api calls on the right
# 5. Export the data from Chrome developer tool as a .har file,
#    you just right-click any request from the network settings when you're done scrolling and select save as .HAR file.
# 6. Place this file in the same directory as this script the ParseChromeHarFile function will create
#    a list of url's to go to and extract the contact details from

urlList = []
def ParseChromeHarFile():
    # this function creates a list of url's with id's
    with open(harFileName, 'r') as file:
        line = file.readline()
        string = ",U"
        fullLine = ""
        idList = []
        global urlList
        for line in file:
            if string in line and 'text' not in line:
                line = line.replace("                ", "")
                line = line.replace("value", "")
                line = line.replace(":", "")
                line = line[3:]
                line = line.replace('"', "")
                line = line.replace('\n', ',')
                fullLine += line
    idList = fullLine.split(",")
    for id in idList:
        urlList.append(baseUrl + id)

def Login():
    # these 5 lines log into slack for you
    driver.get(baseUrlWithoutTeamCode) # for trident
    time.sleep(.5)
    username = driver.find_element_by_css_selector("#email")
    password = driver.find_element_by_css_selector("#password")
    username.send_keys(slackEmail)
    time.sleep(1)
    password.send_keys(slackPassword)
    time.sleep(1)
    driver.find_element_by_css_selector("#signin_btn").click()
    time.sleep(2)

def RunThrough():
    # this function goes through all of the links for a slack channel and records contact details, 15 at a time
    print("Below is the data for the %s channel" % baseUrlWithoutTeamCode)
    print("Name:","    ","Title:","    ","Email:","    ","Phone:")
    count = 0
    Login()
    for i in urlList:
        if count == 15:
            driver.find_element_by_id("team_menu").click()
            driver.find_element_by_css_selector("#logout>a>span>strong").click()
            time.sleep(2)
            count = 0
            Login()
        count += 1
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'T')
        time.sleep(.5)
        driver.get(i)
        time.sleep(5)
        try:
            driver.find_elements_by_xpath("//*[@id='generic_dialog']/div[4]/button[3]").click()
            time.sleep(120)
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'T')
            time.sleep(.5)
            driver.get(i)
            time.sleep(5)
        except:
            a = "a" # nonsense to take place of 'continue'
        name = driver.find_element_by_class_name("member_name").text
        time.sleep(.5)
        try:
            title = driver.find_element_by_class_name("member_title").text
            time.sleep(.5)
        except:
            title = "no_title"
        try:
            email = driver.find_element_by_xpath("//a[contains(text(), '@') and contains(text(), '.')]").text
        except:
            email = "no_email"
        try:
            tel = driver.find_element_by_xpath("//a[contains(@href, 'tel:')]").text
        except:
            tel = "no_number"
        print(name,"    ",title,"    ",email,"    ",tel)
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
        time.sleep(1)


ParseChromeHarFile()
RunThrough()
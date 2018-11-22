# get_contact_details_from_slack (using Python & Selenium WebDriver)
This script extracts all the Names, Titles, Emails and Phone numbers from a Slack Account

To use, you need to:

1. have python installed
2. install chromedriver and chrome
3. have a slack id and password
4. create a .HAR file 

steps in the script:

# This script extracts the Name, Title, Email and Phone number from a Slack Account

imports:

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
# created per the below 6 steps

#   To get the below list of Slack User ID's (create a .HAR file):
# 1. go to the slack website for a group, usually https://< id >.slack.com/messages, sign in
# 2. Click on a Channel's members link, a person icon and then see the "___ Members" on the right
# 3. With the chrome dev tools open and the network options selected, click on the 'See all __ Members' button
# 4. Scroll through this full list of Slack Group members, noting the api calls on the right
# 5. Export the data from Chrome developer tool as a .har file,
#    you just right-click any request from the network settings when you're done scrolling and select save as .HAR file.
# 6. Place this file in the same directory as this script the ParseChromeHarFile function will create
#    a list of url's to go to and extract the contact details from


 - if the script stops, you can make a note of the slack user id that it ended on and edit the list of urls to include only the url's after this point.... - you would need to print out the list of urls from ParseChromeHarFile() to edit this. 


### ~~~ You can replace the 6 spaces inbetween each of the printed out contact details with a 'tab'   ###
### ~~~ and paste all the data into an excel document  (if you like...)   ###
### ~~~ each bit of data will be in it's own column  ###






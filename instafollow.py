import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

#create driver object
driver=webdriver.Chrome(executable_path="C:\LOCAL DISC D\slovo\PROJECTS\instagram bot\chromedriver.exe")
#use the driver.get command to open url
driver.get("https://www.instagram.com/accounts/login/?hl=en")
time.sleep(4)#will wait 10 secs before proceeding

#Instructing the program to find an element whose name is username
#send_keys will input the specified items in the usename field
driver.find_element_by_name("username").send_keys("")#your username
driver.find_element_by_name("password").send_keys("")#your password
time.sleep(2)
#we click the login button using its xpath
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]").click()
time.sleep(3)
#clicks the turn on notifications pop up
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
time.sleep(1)
#Working on the search bar
searchbox = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Search']")
    )
)
# send search into input
searchbox.send_keys('')#instagram user whose followers you want to follow
time.sleep(4)
searchbox.send_keys(Keys.ENTER)
time.sleep(1)
searchbox.send_keys(Keys.ENTER)
time.sleep(4)

#click the followers button to dispaly the users followers
driver.find_element_by_partial_link_text("following").click()
time.sleep(3)

#scroll through the followers lst
scroll_box=driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
last_ht, ht=0, 1
while last_ht !=ht:
    last_ht=ht
    time.sleep(2)
    ht=driver.execute_script("""
    arguments[0].scrollTo(0,arguments[0].scrollHeight);
    return arguments[0].scrollHeight
    """, scroll_box)
    time.sleep(1)

#Click follow buttons in intervals of 2 seconds then pause for one hour after 120 clicks
clicked=0
buttons = driver.find_elements_by_xpath("//button[contains(.,'Follow')]")
for btn in buttons:
    # Use the Java script to click on follow
    driver.execute_script("arguments[0].click();", btn)
    clicked +=1
    if clicked == 120:
        clicked = 0
        time.sleep(3600)
    else:
        time.sleep(2)

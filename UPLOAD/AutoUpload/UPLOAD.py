from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import json
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
wait = WebDriverWait(driver, 10)


driver.get("https://2020.igem.org/Team:Korea-SIS")

# 클릭
element = wait.until(
    EC.element_to_be_clickable((By.ID, "user_item"))
)
element.click()

driver.switch_to.frame("nlogin_iframe")
driver.find_element_by_name('username').send_keys("")
driver.find_element_by_name('password').send_keys("")
driver.find_element_by_name('Login').click()
driver.switch_to.default_content()

# json 파일 열어서 내용 import
with open("URLlist.json", "r") as f:
    file_list = json.load(f)

# file_name 을 
for file_name in file_list.keys():
    try:
        soup = BeautifulSoup(open(f"../{file_name}.html", encoding='UTF8'), 'html.parser')
        ## 파일 수정 로직 ##
        temp = soup.prettify()
        temp = temp.replace(
            'cssForUpload.css',
            'https://2020.igem.org/wiki/index.php?title=Template:Korea-SIS/CSS&action=raw&ctype=text/css'
        )        
        
        #####

        URL = file_list[file_name]
        print(URL)
        # https://2020.igem.org/Team:Korea-SIS
        # https://2020.igem.org/wiki/index.php?title=Team:Korea-SIS&action=edit
        driver.get(
            URL.split('Team:Korea-SIS')[0] +
            "wiki/index.php?title=Team:Korea-SIS" +
            URL.split('Team:Korea-SIS')[1] +
            "&action=edit"
        )
        
        driver.find_element_by_id("wpTextbox1").clear()
        driver.find_element_by_id("wpTextbox1").send_keys(temp)
        driver.find_element_by_id("wpSave").click()
        
        # break # 일단 하나만 테스트 하려고 추가, 추후에 삭제

    except FileNotFoundError as e:
        print(e)

print('Test Completed')
driver.quit()



# '<link rel="stylesheet" type="text/css" href="https://2020.igem.org/wiki/index.php?title=Template:Korea-SIS/CSS&action=raw&ctype=text/css" />'
# https://2020.igem.org/wiki/index.php?title=Team:Korea-SIS&action=edit


# mid_result = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "gNO89b")))
# driver.find_element_by_name("q").send_keys("selenium" + Keys.RETURN)

# first_result = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "rc")))
# print(first_result.get_attribute("textContent"))

# driver.maximize_window()
# driver.refresh()

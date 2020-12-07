from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

try: 
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # 창 켜기
    driver = webdriver.Chrome('./chromedriver', options=options)
    wait = WebDriverWait(driver, 10)
    driver.get("https://2020.igem.org/Team:Korea-SIS")

    print("Start")

    # 로그인
    element = wait.until(
        EC.element_to_be_clickable((By.ID, "user_item"))
    )
    element.click()

    driver.switch_to.frame("nlogin_iframe")
    driver.find_element_by_name('username').send_keys("")
    driver.find_element_by_name('password').send_keys("")
    driver.find_element_by_name('Login').click()
    driver.switch_to.default_content()

    print("Login Complete")

    # 일정 시간마다 새로고침하며 css 업로드
    while True:
        start = time.strftime('%c', time.localtime(time.time()))
        print("Upload Start")

        driver.get("https://2020.igem.org/wiki/index.php?title=Template:Korea-SIS/CSS&action=edit")

        with open('../cssForUpload.css', 'r', encoding='UTF8') as f:
            temp = f.read()

        driver.find_element_by_id("wpTextbox1").clear()
        driver.find_element_by_id("wpTextbox1").send_keys(temp)
        driver.find_element_by_id("wpSave").click()
        
        print("Upload Complete, time:", start)

except KeyboardInterrupt:
    print("End")
    driver.quit()


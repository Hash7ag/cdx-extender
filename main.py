from sys import exit
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.common import exceptions as selenium_exceptions

import checker
from argument import args
from environment import current_path, get_user, del_user_file


def main():
    checker.check()
    user = get_user()

    try:
        opts = webdriver.ChromeOptions()
        opts.headless = args.headless
        browser = webdriver.Chrome(executable_path=f"{current_path}/chromedriver" ,options=opts)
        browser.set_window_size(1280, 900)

        browser.get("https://cdx.nchc.org.tw")
        browser.find_element_by_id("btn_login").click()
        WebDriverWait(browser, 3).\
            until(expected_conditions.\
                visibility_of_element_located((By.ID, "login")))
    except Exception as error:
        exit(error)
    
    try:
        browser.execute_script("document.getElementsByName('login_user_email')[0].type='text';")
        browser.find_element_by_name("login_user_email").send_keys(user[0])
        browser.find_element_by_name("login_user_password").send_keys(user[1])
        browser.find_elements_by_class_name("btn-success")[0].click()
        WebDriverWait(browser, 3).\
            until(expected_conditions.\
                alert_is_present())
        alert = browser.switch_to.alert
        if "非法字元" in alert.text:
            exit("Incorrect username.")
        elif "沒有權限" in alert.text:
            exit("Incorrect username or password.")
        else:
            exit(alert.text)
    except selenium_exceptions.TimeoutException:
        pass
    except Exception as error:
        exit(error)

    try:
        browser.get("https://cdx.nchc.org.tw/setting_vmmgt_common.php")

        for i in range(max(1, len(browser.find_elements_by_class_name("page-link")))):
            if i != 0:
                browser.find_elements_by_class_name("page-link")[i].click()
            for j in range(len(browser.find_elements_by_class_name("vm-detail"))):
                VMs = browser.find_elements_by_class_name("vm-detail")
                VMs[j].find_element_by_css_selector("button[data-target*=extend]").click()
                WebDriverWait(browser, 3).\
                    until(expected_conditions.\
                        visibility_of_element_located((By.ID, f"extend-{j}")))
                Select(VMs[j].find_element_by_name("extend_machine_day")).select_by_index(2)
                VMs[j].find_elements_by_class_name("btn-success")[0].click()
        
        browser.quit()

        print("Extend Completed!")
    except Exception as error:
        exit(error)

if __name__ == '__main__':
    main()
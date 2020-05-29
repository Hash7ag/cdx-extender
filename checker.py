from sys import exit, platform

from socket import create_connection
from socket import error as socket_exceptions
from requests import get
from requests import ConnectionError as requests_exceptions

from selenium import webdriver
from selenium.common.exceptions import WebDriverException as selenium_exceptions

from argument import args
from environment import \
    current_path, set_user_file, del_user_file, \
    download_chrome_driver, del_chrome_driver


def check():
    print("Check the current environment...", flush=True)

    if not platform.startswith("linux"):
        exit('This platform is not supported.')
    
    try:
        create_connection(("1.1.1.1", 80), timeout=3).close()
    except socket_exceptions:
        exit("Please check your internet connection.")
    except Exception as error:
        exit(error)
        
    try:
        download_chrome_driver(overwrite=False)
        opts = webdriver.ChromeOptions()
        opts.headless = True
        webdriver.Chrome(executable_path=f"{current_path}/chromedriver", options=opts).close()
    except selenium_exceptions as error:
        del_chrome_driver()
        exit("Chrome Driver is not available. Please update the Chrome Driver.")
    except Exception as error:
        exit(error)
    
    try:
        get("https://cdx.nchc.org.tw", timeout=3).close()
    except requests_exceptions:
        exit("CDX cannot be reached. Please try again later.")
    except Exception as error:
        exit(error)
    
    print("Now, it's ready to go.", flush=True)
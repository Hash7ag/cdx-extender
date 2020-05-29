from os import remove
from sys import exit
from subprocess import check_output
from io import StringIO, BytesIO
from pathlib import Path
current_path = Path(__file__).parent.absolute()

from json import load, dump
from getpass import getpass
from base64 import b64encode, b64decode

from requests import get
from xml.etree import ElementTree as ET
from packaging.version import parse
from zipfile import ZipFile


def set_user_file():
    print("Pleast enter the information of your CDX account.")
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    if password != getpass("Retype your password: "):
        exit("Sorry, the passwords do not match.")

    with open(f"{current_path}/.user", mode="w+") as f:
        dump([username, b64encode(password.encode()).decode()], f)
    return [username, password]

def get_user():
    try:
        with open(f"{current_path}/.user", mode="r") as f:
            user = load(f)
        if len(user) > 2:
            user = set_user_file()
        else:
            user[1] = b64decode(user[1].encode()).decode()
    except:
        user = set_user_file()
    return user

def del_user_file():
    if Path(f"{current_path}/.user").exists():
        remove(f"{current_path}/.user")

def download_chrome_driver(overwrite):
    try:
        if not Path(f"{current_path}/chromedriver").exists() or overwrite:
            print("Download Chrome Driver...", end="", flush=True)
            del_chrome_driver()

            browser_version = check_output(["google-chrome", "--version"]).decode().split()[-1]

            with get("https://chromedriver.storage.googleapis.com/") as xml_req:
                it = ET.iterparse(BytesIO(xml_req.content))
            for _, el in it:
                _, _, el.tag = el.tag.rpartition('}')
            root = it.root

            driver_list = []
            for content in root.findall("Contents"):
                content_key = content.find("Key").text
                if "linux" in content_key and ".zip" in content_key:
                    if parse(content_key.split("/")[0]) < parse(browser_version):
                        driver_list.append(content_key)
            with get(f"https://chromedriver.storage.googleapis.com/{driver_list[-1]}") as zip_req:
                with ZipFile(BytesIO(zip_req.content)) as zip_file:
                    zip_file.extractall(current_path)
            driver = Path(f"{current_path}/chromedriver")
            driver.chmod(driver.stat().st_mode | 0o111)

            print("Done", flush=True)
    except FileNotFoundError:
        exit("You have to install Google Chrome before running!")
    except Exception as error:
        print(error)
        exit("You might need to re-download the driver via https://sites.google.com/a/chromium.org/chromedriver.")

def del_chrome_driver():
    if Path(f"{current_path}/chromedriver").exists():
        remove(f"{current_path}/chromedriver")
from sys import exit

from json import dump
from getpass import getpass
from base64 import b64encode

from argparse import Action, ArgumentParser, RawDescriptionHelpFormatter

from environment import download_chrome_driver, set_user_file, del_user_file


class DownloadChromeDriver(Action):
    def __call__(self, parser, namespace, values, option_string):
        download_chrome_driver(overwrite=True)
        exit("The Chrome Driver has downloaded.")

class ResetUserFile(Action):
    def __call__(self, parser, namespace, values, option_string):
        set_user_file()
        exit("The user file has been reset.")

class ClearUserFile(Action):
    def __call__(self, parser, namespace, values, option_string):
        del_user_file()
        exit("The user file has been deleted.")


parser = ArgumentParser(
    prog="cdx-extender",
    formatter_class=RawDescriptionHelpFormatter,
    description="The Solution to Extend the Deadline for the Virtual Machines on CDX", 
    epilog="It's better to work with cron(crontab) on Linux.")

parser.add_argument(
    "-H", "--headless", dest="headless",
    action="store_true", help="set headless browser")


group = parser.add_mutually_exclusive_group()
group.add_argument(
    "-D", "--download-chromedriver", dest="download_chrome_driver", nargs=0,
    action=DownloadChromeDriver, help=" download and overwrite(if any) the Chrome Driver and exit")
group.add_argument(
    "--reset", dest="reset", nargs=0,
    action=ResetUserFile, help="reset the user data and exit")
group.add_argument(
    "--clear", dest="clear", nargs=0,
    action=ClearUserFile, help="clear the user data and exit")

args = parser.parse_args()
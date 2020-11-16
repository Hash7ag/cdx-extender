# CDX Extender
[![MyGet](https://img.shields.io/github/license/Hash7ag/cdx-extender)](https://github.com/Hash7ag/cdx-extender/blob/master/LICENSE)

The solution to extend the deadline for the virtual machines on [CDX](https://cdx.nchc.org.tw/).

Ohter Languages: English, [繁體中文](README.zh-tw.md)

## Notice
- **Since [CDX](https://cdx.nchc.org.tw/) integrates Google reCAPTCHA, this project is no longer available.**

## Installing
### Dependencies
- [Google Chrome](https://chrome.google.com/)
- [Python3](https://python.org/downloads/) and [Git](https://git-scm.com/downloads)
    ```sh
    sudo apt update
    sudo apt install python3 python3-pip git
    ```

### Setup
```sh
git clone https://github.com/Hash7ag/cdx-extender.git ~/cdx-extender
cd ~/cdx-extender
python3 -m pip install -r requirements.txt
./main.py --reset
```
Then, enter the username and the password of your [CDX](https://cdx.nchc.org.tw/) account.

## Documentation
```
optional arguments:
  -h, --help            show the help message and exit
  -H, --headless        set headless browser
  -D, --download-chromedriver
                        download and overwrite(if any) the ChromeDriver and exit
  --reset               reset the user data and exit
  --clear               clear the user data and exit
```

## Usage
```sh
~/cdx-extender/main.py
```
It's better to work with [cron(crontab)](https://en.wikipedia.org/wiki/Cron) on Linux.

## License
Copyright © 2020 Hash7ag All Rights Reserved

This project is licensed under the [MIT License](LICENSE).

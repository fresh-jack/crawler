import time

import requests
import json
from bs4 import BeautifulSoup


def bs_get():
    html = '''
    <ul>
        <li><a href="zhangwuji.com">张无忌</a></li>
        <li id="abc"><a href="zhouxingchi.com">周星驰</a></li>
        <li><a href="zhubajie.com">猪八戒</a></li>
        <li><a href="wuzetian.com">武则天</a></li>
        <a href="jinmaoshiwang.com">金毛狮王</a>
    </ul>
    '''
    page = BeautifulSoup(html, "html.parser")
    # page.find("标签名", attrs={"属性": "值"}) 查找某个元素 标签名 只会找到一个结果
    li = page.find("li", attrs={"id": "abc"})
    # print(li)
    a = li.find("a")
    print(a.text)  # 拿文本
    print(a.get("href"))  # 拿属性 .get("属性名")
    # page.find_all("标签名", attrs={"属性": "值"}) 查找某个元素 标签名 找到所有结果

    ##############################
    li_list = page.find_all("li")
    # print(li_list)
    for li in li_list:
        a = li.find("a")
        text = a.text
        href = a.get("href")
        print(text, href)


def get_image():
    url = "https://www.umei.cc/bizhitupian/xiaoqingxinbizhi/"
    resp = requests.get(url)
    resp.encoding = "utf-8"
    main_image = BeautifulSoup(resp.text, "html.parser")
    image_list = main_image.find_all("div", attrs={"class": "img"})
    n = 0
    for image in image_list:
        image_resp = requests.get(image.find("img").get("data-original"))
        with open(f"{n}.jpg", mode="wb") as f:
            f.write(image_resp.content)
        n += 1
        print("{n} complete!!!")
    print("task done")

if __name__ == '__main__':
    get_image()

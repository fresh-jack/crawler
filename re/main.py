# 思路
# 拿到页面源代码
# 编写正则 提取页面数据
# 保存数据
import time

import requests
import re


def get_douban():
    f = open("top250.csv", mode="w", encoding="utf-8")
    for i in range(1, 2, 1):
        start = (i - 1) * 25
        url = f"https://movie.douban.com/top250?start={start}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }
        resp = requests.get(url, headers=headers)
        resp.encoding = "utf-8"
        pageSource = resp.text
        # print(pageSource)
        # re.S 让正则中的.匹配换行符
        obj = re.compile(r'<div class="item">.*?<a href="(?P<link>.*?)">.*?<span class="title">(?P<name>.*?)</sp'
                         r'an>.*?<p class="">.*?导演: (?P<director>.*?)&nbsp;.*?主演:(?P<actor>.*?)<br>'
                         r'(?P<year>.*?)&nbsp;/&nbsp;(?P<country>.*?)&nbsp;/&nbsp;(?P<story>.*?)</p>', re.S)
        result = obj.finditer(pageSource)
        for item in result:
            link = item.group("link")
            name = item.group("name")
            director = item.group("director")
            actor = item.group("actor")
            year = item.group("year").strip()
            country = item.group("country")
            story = item.group("story")
            movie_detail(link)
            #
            break
            f.write(f"{name},{director},{actor},{year},{country},{story},{link}\n")
        time.sleep(1)
        break
    f.close()
    resp.close()
    print("豆瓣top250提取完毕!")


def movie_detail(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    detail = requests.get(url, headers=headers)

    infoObj = re.compile(r'<div id="info">(?P<info>.*?)</div>', re.S)
    resp = infoObj.search(detail.text)
    print(resp.group("info"))


def director(obj, info):
    return obj.finditer(info)

def script_writer(obj, info):
    return obj.finditer()


if __name__ == '__main__':
    get_douban()

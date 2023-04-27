import os

import requests
from lxml import etree
import requests
import re
import time


def xpath_get():
    print('xpath_get')
    # et = etree.XML()
    # et.xpath("/book") # 表示根节点
    # et.xpath("/book/name) # xpath中间的/表示子节点
    # et.xpath("/book/name/text())[0] # text() 表示拿文本 返回的是个list
    # et.xpath("/book//nick) # 表示book后面的所有子节点
    # et.xpath("/book/*/nick/text()) # *表示通配符
    # et.xpath("/book/author/nick[@class='jay']/text()) # []表示属性筛选。@属性名=值
    # et.xpath("/book/partner/nick/@id) # 最后一个/表示拿到nick里面的id的内容 @属性 可以拿到属性


def zhubajie():
    url = "https://beijing.zbj.com/search/f/?type=new&kw=saas&r=2"
    resp = requests.get(url)
    resp.encoding = "utf-8"
    et = etree.HTML(resp.text)
    shop_list = et.xpath("//div[@class='service-card-wrap']")
    print(len(shop_list))
    for shop in shop_list:
        name = shop.xpath("./div/a/div[2]/div/div/text()")
        print(name)


def doutu_get():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Referer": "https://www.doutub.com/"
    }
    num = int(input("你想爬取前几页: "))

    if not os.path.exists("images"):
        os.mkdir("images")

    for n in range(num):
        url = f'https://www.doutub.com/img_lists/new/{n + 1}'
        resp = requests.get(url, headers=headers)
        html = etree.HTML(resp.text)
        divs = html.xpath("//div[@class='cell']")[0:50]
        # 返回的 divs 是一个列表，切片去除无用信息，第51个div我们不需要,详细看图三

        for div in divs:
            imgSrc = div.xpath("./a/img/@data-src")[0]
            word = div.xpath("./a/span/text()")[0].strip()
            name = re.sub(r'[\:*?"<>/|]', '', word)  # 使用正则表达式sub函数去除 \:*?"<>/|这些字符。原因看图四
            img_type = imgSrc.split(".")[-1]  # 因为图片文件的格式有些是jpg，有些是gif，这里取出图片格式
            # 下载图片
            img_resp = requests.get(imgSrc, headers=headers)
            with open("images/" + name + "." + img_type, mode="wb") as f:
                f.write(img_resp.content)
            print(name + "." + img_type, "下载完成")
            time.sleep(0.3)  # 防止频繁访问被封ip，这里休息0.3秒
        print(f"\n第{n + 1}页下载完成！\n")
        time.sleep(5)


if __name__ == '__main__':
    zhubajie()

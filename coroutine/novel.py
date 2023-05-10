import asyncio
import time

import aiofiles
import aiohttp
import requests
from lxml import etree


def get_every_chapter_url(url):
    while 1:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            }
            resp = requests.get(url, headers)
            resp.encoding = "gbk"
            tree = etree.HTML(resp.text)
            href_list = tree.xpath("//ul[@id='section-list']/li/a/@href")
            # print(href_list)
            return href_list
        except:
            print("again...")
            time.sleep(3)


async def download_chapter(url):
    print("download start ", url)
    for i in range(10):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    page_source = await resp.text()
                    tree = etree.HTML(page_source)
                    title = tree.xpath("//div[@class='reader-main']/h1/text()")[0].strip()
                    content = "\n".join(tree.xpath("//div[@id='content']/text()")).replace("\u3000", "")
                    async with aiofiles.open(f"./明朝那些事儿/{title}.txt", mode="w", encoding="utf-8") as f:
                        await f.write(content)
                    break
        except:
            print("download_chapter failed ", url)
            await asyncio.sleep((i + 1) * 5)
    print("download end ", url)


async def download(href_list):
    tasks = []
    for href in href_list:
        t = asyncio.create_task(download_chapter(href))
        tasks.append(t)
    await asyncio.wait(tasks)


def main():
    url = "https://www.zanghaihua.org/mingchaonaxieshier/"
    href_list = get_every_chapter_url(url)
    asyncio.run(download(href_list))


if __name__ == '__main__':
    main()

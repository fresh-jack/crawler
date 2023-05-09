# aiohttp aiofiles

'''
https://pic.3gbizhi.com/uploadmark/20230507/1949d62332530a6572adac5103bb0312.jpg
https://pic.3gbizhi.com/uploadmark/20230507/71e19ec4067632bacc039801295ac438.jpg
https://pic.3gbizhi.com/uploadmark/20230507/a3985f7b37a2f7954b33841387766645.jpg
'''
import asyncio

import aiofiles
import aiohttp


async def download(url):
    print("开始下载.", url)
    file_name = url.split("/")[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # await resp.text() => resp.text
            content = await resp.content.read()  # => resp.content
            # 写入文件
            async with aiofiles.open(file_name, mode="wb") as f:
                await f.write(content)
    print("下载完成.", url)


async def main():
    url_list = [
        "https://pic.3gbizhi.com/uploadmark/20230507/1949d62332530a6572adac5103bb0312.jpg",
        "https://pic.3gbizhi.com/uploadmark/20230507/71e19ec4067632bacc039801295ac438.jpg",
        "https://pic.3gbizhi.com/uploadmark/20230507/a3985f7b37a2f7954b33841387766645.jpg"
    ]

    tasks = []
    for url in url_list:
        t = asyncio.create_task(download(url))
        tasks.append(t)
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())

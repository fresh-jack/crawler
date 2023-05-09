import asyncio


async def func1():
    print("func1----")
    await asyncio.sleep(1)
    print("func1 end")
    return "return func1"


async def func2():
    print("func2----")
    await asyncio.sleep(2)
    print("func2 end")
    return "return func2"


async def func3():
    print("func3----")
    await asyncio.sleep(3)
    print("func3 end")
    return "return func3"


async def download(url, t):
    print("begin----")
    await asyncio.sleep(t)
    print("end------")


async def main():
    urls = [
        "www.baidu.com",
        "www.google.com",
        "www.tencent.com"
    ]

    tasks = []

    for url in urls:
        task = asyncio.create_task(download(url, 3))
        tasks.append(task)
    await asyncio.wait(tasks)


async def test_gather():
    f1 = func1()
    f2 = func2()
    f3 = func3()
    tasks = [
        f1,
        f2,
        f3
    ]

    result = await asyncio.gather(*tasks)
    print(result)


if __name__ == '__main__':
    # f1 = func1()
    # f2 = func2()
    # f3 = func3()
    # tasks = [
    #     f1,
    #     f2,
    #     f3
    # ]
    #
    # result = await asyncio.gather(*tasks)
    asyncio.run(test_gather())

    # done, pending = asyncio.run(asyncio.wait(tasks))
    # for t in done:
    #     print(t.result())

    # asyncio.run(main())

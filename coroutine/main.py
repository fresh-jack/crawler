import asyncio

async def func1():
    print("func1----")
    await asyncio.sleep(1)
    print("func1 end")

async def func2():
    print("func2----")
    await asyncio.sleep(2)
    print("func2 end")

async def func3():
    print("func3----")
    await asyncio.sleep(3)
    print("func3 end")

if __name__ == '__main__':
    f1 = func1()
    f2 = func2()
    f3 = func3()
    tasks = [
        f1,
        f2,
        f3
    ]
    asyncio.run(asyncio.wait(tasks))
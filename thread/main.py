# 继承式调用
import threading
import time
from concurrent.futures import ThreadPoolExecutor


class MyThreading(threading.Thread):
    def __init__(self, name):
        super(MyThreading, self).__init__()
        self.name = name

    # 线程要运行的代码
    def run(self):
        print("我是线程%s" % self.name)
        time.sleep(2)
        print("线程%s运行结束" % self.name)


def fun(name):
    print("我是线程%s " % name)
    time.sleep(2)
    print("线程%s运行结束" % name)


if __name__ == '__main__':
    t1 = MyThreading(1)
    t2 = MyThreading(2)
    start_time = time.time()
    t1.start()
    t2.start()
    end_time = time.time()
    print("两个线程一共的运行时间为：", end_time - start_time)
    print("主线程结束")

    print("-------------")
    t3 = threading.Thread(target=fun, args=("jay",))
    t4 = threading.Thread(target=fun, args=("Bob",))
    t3.start()
    t4.start()

    print("-------thread-pool-----")
    st = time.time()
    name_list = ['xiaozi', 'aa', 'bb', 'cc']
    with ThreadPoolExecutor(10) as t:
        for i in range(len(name_list)):
            t.submit(fun, name_list[i])
    et = time.time()
    print("cost time: ", et - st)
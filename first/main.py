# This is a sample Python script.
import requests
import re


def get(data):
    url = f"https://www.sogou.com/web?query={data}"
    headers = {
        "User-Agent":
            "Mozilla / 5.0(Macintosh;\
       Intel\
       Mac\
       OS\
       X\
       10_15_7) AppleWebKit / 537.36(KHTML, like\
       Gecko) Chrome / 112.0\
       .0\
       .0\
      Safari / 537.36"
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"
    with open("sougou.html", mode="w", encoding="utf-8") as f:
        f.write(resp.text)


def post(data):
    url = "https://fanyi.baidu.com/sug"
    resp = requests.post(url, data={"kw": data})
    # print(resp.text)  # text
    print(resp.json()['data'])  # josn


def movie():
    url = "https://movie.douban.com/j/chart/top_list"
    data = {
        "type": "13",
        "interval_id": "100:90",
        "action": "",
        "start": 0,
        "limit": 20
    }
    headers = {
        "User-Agent":
            "Mozilla / 5.0(Macintosh;\
       Intel\
       Mac\
       OS\
       X\
       10_15_7) AppleWebKit / 537.36(KHTML, like\
       Gecko) Chrome / 112.0\
       .0\
       .0\
      Safari / 537.36"
    }
    resp = requests.get(url, params=data, headers=headers)
    print(resp.json())


def test_re():
    # r 防止转义字符
    result1 = re.findall(r".*?x", "aaaxbbbx")
    print("findall", result1)

    # 迭代器
    result2 = re.finditer(r".*?x", "aaaxbbbx")
    for item in result2:
        print(item.group())

    # 只会匹配到第一次匹配的内容
    result3 = re.search(r".*?x", "aaaxbbbx")
    print("search", result3.group())

    # match 匹配的时候从字符串的开头开始匹配 类似在正则前面加上^
    result3 = re.match(r".*?x", "aaaxbbbx")
    print("match", result3.group())
    # 预加载 提前把正则对象加载完毕
    obj = re.compile(r".*?x")
    # 直接把编译好的正则进行使用
    result4 = obj.findall("aaaxbbbx")
    print("compile", result4)


if __name__ == '__main__':
    # content = input("请输入一个单词: ")
    # post(content)
    # movie()
    test_re()

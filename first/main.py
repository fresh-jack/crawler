# This is a sample Python script.
import requests


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
      "action":"",
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


if __name__ == '__main__':
    # content = input("请输入一个单词: ")
     # post(content)
     movie()
import requests
from pyquery import PyQuery


def pyquery_get():
    html = '''
    <ul>
    <li class="aaa"><a href="www.google.com">谷歌</a></li>
    <li class="aaa"><a href="www.baidu.com">百度</a></li>
    <li class="bbb" id="qq"><a href="www.qq.com">腾讯</a></li>
    <li class="bbb"><a href="www.yuanlai.com">原来</a></li>
    </ul>
    '''
    p = PyQuery(html)
    # a = p("li")("a")         # print(a, type(a))  => p("li a")
    # a = p(".aaa a")          # class="aaa"
    # a = p("#qq a")           # id="qq"
    # a = p("#qq a").attr("href") # 获取属性
    a = p("#qq a").text()  # 文本
    print(a)

    # 如果多个标签同时拿属性 只能默认拿到第一个 借助items函数返回迭代器
    it = p("li a").items()
    for i in it:
        print(i.text())
        print(i.attr("href"))

    # heml() text()
    div = '''
    <div><span>i love u</span></div>
    '''
    pq = PyQuery(div)
    html = pq("div").html()  # 全部内容
    text = pq("div").text()  # 只要文本
    print(html, text)


# 1. pyquery(选择器)
# 2. items() 当选择器选择的内容很多的时候 需要一个一个处理的时候
# 3. attr(属性名) 获取属性
# 4. text() 获取文本

# pyquery 修改
def pyquery_update():
    html = '''
    <HTML>
        <div class="aaa">哒哒哒</div>
        <div class="bbb">嘟嘟嘟</div>
    </HTML>
    '''

    p = PyQuery(html)
    # 在xxx标签后面添加xxx新标签
    p("div.aaa").after('''<div class="ccc">吼吼吼</div>''')
    p("div.aaa").append('''<span>i love u</span>''')
    p("div.bbb").attr("class", "aaa")  # 新增属性
    p("div.ccc").attr("id", "12306")  # 修改属性
    p("div.ccc").remove_attr("id")  # 删除属性
    p("div.ccc").remove()  # 删除标签
    print(p)


def get_page_source(url):
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return resp.text


def parse_page_source(html):
    doc = PyQuery(html)
    print(doc)
    pass

def f17k():
    url = "https://passport.17k.com/ck/user/login"
    data = {
        "loginName": "user",
        "password": "passwd"
    }
    session = requests.session()
    session.post(url, data=data)
    # print(resp.json())
    resp = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
    print(resp.json())

# https://video.pearvideo.com/mp4/short/20170306/cont-1043251-10252590-hd.mp4 真实地址
# https://pearvideo.com/videoStatus.jsp?contId=1043251&mrd=0.6596387695500097
def pear_get():
    url = "https://pearvideo.com/video_1043251"
    contId = url.split("_")[1]
    videoStatusUrl = f"https://pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.6596387695500097"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        # 防盗链 溯源 当前请求的上一级是谁
        "Referer": "https://pearvideo.com/video_1043251"
    }

    dic = requests.get(videoStatusUrl, headers=headers).json()
    srcUrl = dic['videoInfo']['videos']['srcUrl']
    systemTime = dic['systemTime']
    srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
    with open(f"{contId}.mp4", mode="wb") as f:
        f.write(requests.get(srcUrl).content)





def main():
    # url = "https://k.autohome.com.cn/146/"
    # html = get_page_source(url)
    # parse_page_source(html)
    pear_get()


if __name__ == '__main__':
    main()

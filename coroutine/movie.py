import requests
from lxml import etree


def get_page_source(url):
    resp = requests.get(url)
    return resp.text


def get_iframe_src(url):
    page_source = get_page_source(url)
    print(page_source)


def main():
    url = "http://www.yunbtv.net/vodplay/qianmiantewu-1-1.html"
    get_iframe_src(url)


if __name__ == '__main__':
    main()

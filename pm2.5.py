import requests
import traceback
from xpinyin import Pinyin
from bs4 import BeautifulSoup

def getHtml(url):
    try:
        r = requests.get(url)
        r.encoding = 'utf-8'
        r.raise_for_status
        return r.text
    except:
        traceback.print_exc()
        return ''

def cityDetail(url):
    HTML = getHtml(url)
    soup = BeautifulSoup(HTML,'html.parser')
    digit = soup.select('.aqivalue')
    return digit[0].text

def main():
    cityZH = input('要查询的城sssss市名称：')
    p = Pinyin()
    cityPY = p.get_pinyin(cityZH,'')
    url = f'http://www.pm25x.com/city/{cityPY}.htm'
    print(cityZH,'PM2.5:',cityDetail(url))
main()
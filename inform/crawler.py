import urllib
from bs4 import BeautifulSoup

def find_naver_toon():
    html = urllib.request.urlopen('http://comic.naver.com/webtoon/weekday.nhn')
    soup = BeautifulSoup(html,"html.parser")
    titles = soup.find_all('a','title')
    return titles

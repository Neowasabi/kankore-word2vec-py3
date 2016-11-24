import re
import urllib.request
from bs4 import BeautifulSoup
#正規表現置き場
del_tag = re.compile('<.*?>')
del_ref = re.compile('&gt;&gt;\d+')
del_url = re.compile('h*t+ps*?://[\w/:%#\$&\?\(\)~\.=\+\-]+')
del_dayofweek = re.compile('\(.*\)')
del_millisecond = re.compile('\..*')
del_arrow = re.compile("(>>)\d*")
del_reply = re.compile("\d*件")

def get_thread(url):
    print (url)
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,"html.parser")
    tmp =  soup.findAll('a',href=True)
    tmp_list = []
    for i in tmp :
        if re.search("艦隊これくしょん",i.get_text()):
            tmp_list.append(i["href"])
    return tmp_list


def get_text(url_list):
    for a in url_list:
        url_tmp = "http://uni.open2ch.net"+a
        print (url_tmp[0:-3])
        html = urllib.request.urlopen(url_tmp[0:-3])
        soup = BeautifulSoup(html,"html.parser")
        tmp = soup.findAll("dd")
        through_cnt = 0
        for one in tmp:
            if through_cnt < 15:#15レスまで無視
                through_cnt += 1
                continue
            tmp_text = one.get_text().replace("\n","")#消し
            print (del_url.sub('',del_ref.sub('',del_tag.sub("",del_arrow.sub("",del_reply.sub('',tmp_text))))))


if __name__ == "__main__":
    argvs = ["fetch_text","http://uni.open2ch.net/gameswf/subback.html","gameswf/subback.html"," 艦これ"]
    url = argvs[1]
    board = argvs[2]
    keyword = argvs[3]

    url_list = get_thread(url)
    get_text(url_list)


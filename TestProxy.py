# -*- coding:utf-8 -*-

import urllib2, random

url = "http://www.baidu.com/"

proxy_list = [
    {"http": "124.88.67.81:80"},
    {"http": "58.252.6.165:9000"},
    {"http": "115.223.243.166:115"},
    {"http": "115.218.217.92:115"},
    {"http": "115.223.219.86:115"},
    {"http": "27.205.45.15:27"},
    {"http": "121.225.25.29:121"},
    {"http": "115.223.231.251:115"},
    {"http": "121.237.141.236:121"},
    {"http": "115.218.223.194:115"},
    {"http": "115.218.223.202:115"},
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36", 
}

# proxy = random.choice(proxy_list)

for proxy in proxy_list:

    httpproxy_handler = urllib2.ProxyHandler(proxy)

    opener = urllib2.build_opener(httpproxy_handler)

    request = urllib2.Request(url, headers = headers)

    try:
        response = opener.open(request, timeout=3).read()
        print proxy
    except Exception as e:
        pass




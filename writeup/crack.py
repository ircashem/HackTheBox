#!/usr/bin/env python3
import hashlib

salt = "5a599ef579066807"
password = "62def4866937f08cc13bab43bb14e6f7"
wordlist = "/opt/rockyou.txt"

for word in open(wordlist, encoding="latin-1"):

    word = word.replace("\n","")
    # hashlib.md5((str(salt) + line).encode('utf-8')).hexdigest() == password
    HASH = (salt + word).encode('latin-1')
    # print(HASH)
    print("[*] Trying password: ", word,end='\r')
    if (hashlib.md5(HASH).hexdigest()) == password:
        print("[+] Found password: ", word)
        exit(1)
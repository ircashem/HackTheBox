#!/usr/bin/env python3
from hashlib import md5
import sys

def usage():
    print("Usage: python crack-pass.py <hash> <wordlist>")
    print("Example: python crack-pass.py 0f2029b932cf39410b8e988538dd5bbe:rp /opt/rockyou.txt")

if len(sys.argv) != 3:
    usage()
    print(len(sys.argv))
    exit(1)

HASH = sys.argv[1]
WORDLIST = sys.argv[2]
# ENCRYPTED_HASH = '0f2029b932cf39410b8e988538dd5bbe'
# SALT = 'rp' 8512c803ecf70d315b7a43a1c8918522:lBHk0AOG0ux8Ac4tcM1sSb1iD5BNnRJp
try:
    ENCRYPTED_HASH = HASH.split(":")[0]
    SALT = HASH.split(":")[1]
except IndexError:
    print("[-] Please provide HASH in correct format.")
    exit(1)

PASSWORD = ''
try:
    file = open(WORDLIST, encoding='utf-8')
except FileNotFoundError:
    print("[-] Wordlist Not Found. Make Sure it is there.")
    exit(1)

for word in open(WORDLIST, encoding='latin-1'):
    PASSWORD = word.replace("\n","")
    HASH = md5((SALT + PASSWORD).encode('latin-1')).hexdigest()
    if HASH == ENCRYPTED_HASH:
        # print()
        print("[+] Password Found: ", PASSWORD)
        exit(1)
    else:
        # print("[*] Trying password: ", PASSWORD, end='\r')
        continue

#print(md5((SALT + PASSWORD).encode('utf-8')).hexdigest())


# for word in open(wordlist, encoding="latin-1"):

#     word = word.replace("\n","")
#     # hashlib.md5((str(salt) + line).encode('utf-8')).hexdigest() == password
#     HASH = (salt + word).encode('latin-1')
#     # print(HASH)
#     print("[*] Trying password: ", word,end='\r')
#     if (hashlib.md5(HASH).hexdigest()) == password:
#         print("[+] Found password: ", word)

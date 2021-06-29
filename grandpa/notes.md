Name & IP Address of Machine:
> grandpa : `10.10.10.14`
<!-- TOC -->

- [Synopsis](#synopsis)

<!-- /TOC -->



## Synopsis
Nmap reveals a iis server running on port 80. Checking the version of iis server , it was vulnerable to 
`Microsoft IIS 6.0 - WebDAV 'ScStoragePathFromUrl' Remote Buffer Overflow  | windows/remote/41738.py`
However the shell we get from msfconsole was really unstable and die frequently within a minute.
However, we are able to run our post-exploit script within the msfconsole and comes across five to six vulnerable exploits.
Trying one by one, the right exploit was
`exploit/windows/local/ms14_070_tcpip_ioctl`
and we gain a nt authority system on the system.


<!-- ## Tools Used.
- [ ] . -->
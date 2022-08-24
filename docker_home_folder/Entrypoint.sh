#!/bin/sh

Xvfb :99 -ac &
#top
ifconfig  eth0 mtu 1500
ethtool -K eth0 tx off rx off tso off gso off gro off lro off
source /root/pyvenv/bin/activate
python3 /home/action.py $1

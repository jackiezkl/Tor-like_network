#!/bin/sh

Xvfb :99 -ac &
ifconfig  eth0 mtu 1500
ethtool -K eth0 tx off rx off tso off gso off gro off lro off
source /root/pyvenv/bin/activate
if [[ $2 == "regular" ]]
then
    python3 /home/action.py $1
elif [[ $2 == "tor" ]]
then
    python3 /home/tor_action.py $1
elif [[ $2 == "tor-like" ]]
then
    python3 /home/tor_like_action.py $1
fi

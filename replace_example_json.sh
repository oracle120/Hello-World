#!/bin/bash

result=$(python get_shadowsocks_account_1.py | tr -s '\n')

ip=$(echo $result | awk '{print $1}')
port=$(echo $result | awk '{print $2}')
pwd=$(echo $result | awk '{print $3}')

sed -i 's/"server".*$/"server":"'"$ip"'",/g' /etc/shadowsocks/example.json
sed -i 's/"server_port".*$/"server_port":'"$port"',/g' /etc/shadowsocks/example.json
sed -i 's/"password".*$/"password":"'"$pwd"'",/g' /etc/shadowsocks/example.json

systemctl restart shadowsocks@example

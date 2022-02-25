#!/bin/bash
# IPsweep program for IPv4.

if [ "$1" == "" ]
then
echo "You forgot an argument"
echo "syntax ./ipsweep.sh 192.168"

else
for ip in `seq 48 57`; do
for ip1 in `seq 1 254`;do
ping -c 1 $1.$ip.$ip1 | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
done
fi
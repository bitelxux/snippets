#!/bin/sh

# Extremely rudimentary but working iptables script

# set a few variables
echo ""
echo "setting global variables"
echo ""
export PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin
iptables="/sbin/iptables"

export NIC="eth0"

# flush any existing chains and set default policies

$iptables -F INPUT
$iptables -F OUTPUT
$iptables -F FORWARD
$iptables -P INPUT DROP
$iptables -P OUTPUT ACCEPT
$iptables -P FORWARD ACCEPT

# enable TUN for VPN
$iptables -A INPUT -i tun+ -j ACCEPT
$iptables -A FORWARD -i tun+ -j ACCEPT
$iptables -A INPUT -i tap+ -j ACCEPT
$iptables -A FORWARD -i tap+ -j ACCEPT

# allow all packets on the loopback interface
$iptables -A INPUT -i lo -s 127.0.0.1 -j ACCEPT
$iptables -A OUTPUT -o lo -s 127.0.0.1 -j ACCEPT

## allow established and related packets back in
$iptables -A INPUT -i $NIC -m state --state ESTABLISHED,RELATED -j ACCEPT

# icmp
echo "applying icmp rules"
echo ""
$iptables -A OUTPUT -p icmp -m state --state NEW -j ACCEPT
$iptables -A INPUT -p icmp -j ACCEPT

# open ports to the firewall
echo "  applying the open port(s) to the firewall rules"
echo ""

# FTP
$iptables -A INPUT -p tcp --dport 21 -j ACCEPT
$iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# HTTP, HTTPS
$iptables -A INPUT -p tcp --dport 80 -j ACCEPT
$iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# SALTSTACK
$iptables -A INPUT -p tcp --dport 4505 -j ACCEPT
$iptables -A INPUT -p tcp --dport 4506 -j ACCEPT

# DOCKER
iptables -I INPUT -i docker0 -j ACCEPT

# Port for reverse SSH tunnel
iptables -I INPUT -p tcp --dport 5000 -j ACCEPT

# netdata
iptables -I INPUT -p tcp --dport 19999 -j ACCEPT

# drop all other packets
echo "applying default drop policies"
echo ""
$iptables -A INPUT -i $NIC -p tcp --dport 0:65535 -j DROP
$iptables -A INPUT -i $NIC -p udp --dport 0:65535 -j DROP

echo "### quicktables is loaded ###"
echo ""

**Check Logged On Users**
```
w
who
```
**Firewall Block ICMP**
```
iptables -A INPUT -p icmp --icmp-type echo-request -j REJECT
```

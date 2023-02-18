**Check Logged On Users**
```
w
who
```
**Firewall Block ICMP**
```
iptables -A INPUT -p icmp --icmp-type echo-request -j REJECT
```
**Firewall C2**
```
iptables -F
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
iptables -A INPUT -p tcp -j DROP
```

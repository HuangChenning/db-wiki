---
title: "1、HGDB单机修改IP地址或主机名(Linux)"
book: "配置类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/HGDB_ip.html"
tags:
  - highgo
  - highgo-v45
  - way-configuration
---

## HGDB单机修改IP地址或主机名（Linux）

## 1、修改IP地址

使用”ifconfig”或”ip a”查看当前IP，记录网卡名和IP地址

```
[root@host ~]# ifconfig 

ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500

    inet 192.168.191.72 netmask 255.255.255.0 broadcast 192.168.191.255
```

进入/etc/sysconfig/network-scripts目录修改”ifcfg-网卡名”文件下的IPADDR

```
[root@host network-scripts]# pwd

/etc/sysconfig/network-scripts

[root@host network-scripts]# vi ifcfg-ens33

[root@host network-scripts]# cat ifcfg-ens33 | grep IPADDR

IPADDR=192.168.191.123
```

重启”network.service”服务，查看IP

```
[root@host network-scripts]# systemctl restart network.service

[root@host ~]# ifconfig 

ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500

    inet 192.168.191.123 netmask 255.255.255.0 broadcast 192.168.191.255
```

## 2、修改主机名

使用hostnamectl set-hostname \[name\]命令修改主机名,不需要重启服务器，重启会话生效

```
[root@host ~]# hostnamectl set-hostname hgdb

[root@host ~]# hostname

hgdb
```

## 3、修改hosts文件

/etc/hosts记录本机ip地址和主机名，修改IP地址或主机名后应修改hosts文件

```
[root@hgdb ~]# cat /etc/hosts

127.0.0.1  localhost localhost.localdomain localhost4 localhost4.localdomain4

::1     localhost localhost.localdomain localhost6 localhost6.localdomain6

192.168.191.72 host

[root@hgdb ~]# vi /etc/hosts

[root@hgdb ~]# cat /etc/hosts

127.0.0.1  localhost localhost.localdomain localhost4 localhost4.localdomain4

::1     localhost localhost.localdomain localhost6 localhost6.localdomain6

192.168.191.123 hgdb
```
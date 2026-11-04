---
title: "26、HAC集群更改IP（单节点更改、全部节点更改）"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/HAC_ip.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## HAC集群更改IP（单节点更改、全部节点更改）

## 一、停掉hghac服务

### 1、按照先停备库，最后停主库原则停服务

### 2、各个节点查询进程，有sender节点的是主库，有receiver节点的是备库

```
ps -ef | grep sender
root     26418  3233  0 6月11 ?    00:00:22 postgres: c: walsender sysdba 192.168.80.228(45186) streaming 0/16000000
ps -ef | grep receiver
root      3372  3348  0 6月11 ?     00:13:54 postgres: c: walreceiver   streaming 0/16000000
```

### 3、停服务命令

```
systemctl stop hghac-vip.service
```

## 二、各个节点停掉etcd服务

```
systemctl stop etcd.service
```

## 三、修改服务器ip

### 1、根据实际情况修改各个服务器ip

### 2、查找虚拟ip配置文件

```
find / -iname vip.env -print
```

### 3、修改虚拟ip和网卡等信息

```
vim /opt/HighGo4.5.7-see/tools/hghac/vip.env
VIP=192.168.1.67
GATEWAY=192.168.234.2
DEV=ens33
```

## 四、修改etcd

### 1、find命令找到etcd.yaml文件

```
find / -iname etcd.yaml -print
```

### 2、修改etcd.yaml配置文件（各个服务器都需要进行修改）

```
vim /opt/HighGo4.5.7-see/tools/hghac/etcd/etcd.yaml

debug: false
name: hghac54
data-dir: /opt/HighGo/tools/hghac/etcd/hghac54.etcd
initial-advertise-peer-urls: http://192.168.1.54:2380    #修改为本机ip
listen-peer-urls: http://192.168.1.54:2380           #修改为本机ip
advertise-client-urls: http://192.168.1.54:2379        #修改为本机ip
listen-client-urls: http://192.168.1.54:2379          #修改为本机ip
initial-cluster-token: etcd-cluster
initial-cluster: hghac54=http://192.168.1.54:2380,hghac55=http://192.168.1.55:2380,hghac61=http://192.168.1.61:2380 
#不同节点修改ip，此处各个节点也需要修改对应的ip。
initial-cluster-state: new
enable-v2: true
```

## 五、修改hghac

### 1、find命令找到hghac.yaml文件

```
find / -iname hghac.yaml -print
```

### 2、修改hghac.yaml文件（各个服务器都需要进行修改）

```
vim /opt/HighGo4.5.7-see/tools/hghac/hghac.yaml
restapi:
  connect_address: 192.168.1.55:8008  #修改本机ip
  listen: 192.168.1.55:8008        #修改本机ip
etcd/zookeeper:     #etcd和zookeeper只会用一个，根据实际情况，修改hosts各个节点实际ip                       
  hosts: 192.168.1.54:2379,192.168.1.55:2379,192.168.1.61:2379 
connect_address:  192.168.1.55:5866   #修改本机ip
```

## 六、启动etcd集群

### 1、各个节点同时启动etcd

```
systemctl start etcd.service
```

### 2、查看单个节点状态

```
systemctl status etcd.service
```

### 3、查看etcd集群状态

配置环境变量如下命令：

```
etcdctl endpoint status --write-out=table
```

未配置环境变量如下命令：

```
/opt/HighGo4.5.7-see/tools/hghac/etcd/etcdctl  --endpoints=http://192.168.1.55:2379,http://192.168.1.56:2379,http://192.168.1.61:2379 endpoint status --write-out=table
```

## 七、启动hghac

### 1、和之前停服务顺序相反，先启动主库服务，再启动备库服务

```
systemctl start hghac-vip.service
```

### 2、单个节点状态查看

```
systemctl status hghac-vip.service
```

### 3、集群状态查看

配置环境变量如下命令：

```
hghactl list
```

未配置环境变量如下命令：

```
/opt/HighGo4.5.7-see/tools/hghac/hghactl -c /opt/HighGo4.5.7-see/tools/hghac/hghac.yaml list
```

## 八、其他

### 1、监控集群使用etcd或者zookeeper，如果使用zookeeper作为监控集群，使用如下方法。

### 2、find命令查找zoo.cfg文件

```
find / -iname zoo.cfg -print
```

### 3、修改zoo.cfg文件（各个服务器节点都需要修改）

```
vi  /opt/Highgo/tools/zookeeper/conf/zoo.cfg
server.1=192.168.1.55:2888:3888
server.2=192.168.1.56:2888:3888
server.3=192.168.1.61:2888:3888
```

### 4、启停zookeeper服务

```
systemctl  start  zookeeper.service
systemctl  stop   zookeeper.service
```

### 5、查看zookeeper状态

```
systemctl  status zookeeper.service
```
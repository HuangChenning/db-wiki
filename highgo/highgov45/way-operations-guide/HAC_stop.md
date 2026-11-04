---
title: "27、HAC集群启停步骤"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/HAC_stop.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## HAC集群启停步骤

## 一、停止集群

### 1、停hghac集群

①按照先停备库，最后停主库原则停服务

②使用A,B两种方法判断集群主备库

#### A、集群命令查看，role显示Leader表示主库，显示Replica表示备库

```
[root@localhost ~]# hghactl list

+ Cluster: ha (7072256965608815760) -------+---------+----+-----------+

| Member   | Host                | Role    | State   | TL | Lag in MB |

+----------+---------------------+---------+---------+----+-----------+

| hghac228 | 192.168.80.228:5866 | Leader  | running |  6 |           |

| hghac230 | 192.168.80.230:5866 | Replica | running |  6 |         0 |

+----------+---------------------+---------+---------+----+-----------+
```

#### B、各个节点查询进程，有sender节点的是主库，有receiver节点的是备库

```
ps -ef | grep sender

root     26418  3233  0 6月11 ?    00:00:22 postgres: c: walsender sysdba 192.168.80.228(45186) streaming 0/16000000

ps -ef | grep receiver

root      3372  3348  0 6月11 ?     00:13:54 postgres: c: walreceiver   streaming 0/16000000
```

③使用如下命令判断数据库是用哪一个服务启动，状态显示 Active: active (running)，代表数据库使用该服务启动。

```
systemctl status hghac.service

systemctl status hghac-vip.service
```

④按照先停备库再停主库原则停掉服务，例如hghac.service服务活动，停掉即可：

```
systemctl stop hghac.service
```

### 2、停etcd集群

①各个节点执行如下命令停掉etcd服务

```
systemctl stop etcd.service
```

②检查etcd服务

```
systemctl status etcd.service
```

## 二、启动集群

### 1、启动etcd集群

①各个节点同时启动etcd服务

```
systemctl start etcd.service
```

②查看单个节点状态

```
systemctl status etcd.service
```

③查看etcd集群状态

配置环境变量如下命令：

```
etcdctl endpoint status --write-out=table
```

未配置环境变量如下命令：

```
/opt/HighGo4.5.7-see/tools/hghac/etcd/etcdctl  --endpoints=http://192.168.1.55:2379,http://192.168.1.56:2379,http://192.168.1.61:2379 endpoint status --write-out=table
```

注意：根据实际情况修改etcdctl命令的实际路径和各个节点的ip地址端口号。

可以使用find命令查找etcdctl路径

```
find / -iname etcdctl -print
```

## 2、启动hghac集群

①和之前停服务顺序相反，先启动主库服务，再启动备库服务，启动的是之前停掉的服务

```
systemctl start hghac.service
```

②单个节点状态查看

```
systemctl status hghac.service
```

③集群状态查看

配置环境变量如下命令：

```
hghactl list
```

未配置环境变量如下命令：

```
/opt/HighGo4.5.7-see/tools/hghac/hghactl -c /opt/HighGo4.5.7-see/tools/hghac/hghac.yaml list
```

注意：根据实际情况修改hghactl命令的实际路径。

可以使用find命令查找hghactl路径

```
find / -iname hghactl -print
```

## 三、其他问题

1、先停etcd集群，会导致数据库各个节点变为只读模式（尽管主备节点存在send和receive进程）。

2、hghac集群先停主库会导致集群主备发生切换。
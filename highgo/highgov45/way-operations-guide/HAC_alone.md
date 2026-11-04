---
title: "25、HAC集群修改为单机"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/HAC_alone.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## HAC集群修改为单机

## 1、检查集群状态，使用A、B两种方法进行判断

### 方法A：使用集群命令，确保TL时间线一致，Lag in MB数据同步延迟不能过高，最好延迟为0。

```
[root@localhost ~]# hghactl list
+ Cluster: ha (7072256965608815760) -------+---------+----+-----------+
| Member   | Host                | Role    | State   | TL | Lag in MB |
+----------+---------------------+---------+---------+----+-----------+
| hghac228 | 192.168.80.228:5866 | Leader  | running |  6 |           |
| hghac230 | 192.168.80.230:5866 | Replica | running |  6 |         0 |
+----------+---------------------+---------+---------+----+-----------+
```

### 方法B：各个节点查询进程，有sender节点的是主库，有receiver节点的是备库

```
ps -ef | grep sender
root     26418  3233  0 6月11 ?    00:00:22 postgres: c: walsender sysdba 192.168.80.228(45186) streaming 0/16000000
ps -ef | grep receiver
root      3372  3348  0 6月11 ?     00:13:54 postgres: c: walreceiver   streaming 0/16000000
```

## 2、不作为单机节点的集群其他各个节点停止、禁用hghac服务

```
[root@hgdw231 hgupload]# systemctl stop hghac.service
[root@hgdw231 hgupload]# systemctl disable hghac.service
Removed symlink /etc/systemd/system/multi-user.target.wants/hghac.service.
```

注意：

也有可能不是hghac.service,可能是hghac-vip.service 请使用systemctl status hghac.service/hghac-vip.service确定运行的服务

## 3、修改为单机节点的数据库停止、禁用hghac服务，并设置数据库服务开机自启动

```
[root@hgdw231 hgupload]# systemctl stop hghac.service
[root@hgdw231 hgupload]# systemctl disable hghac.service
Removed symlink /etc/systemd/system/multi-user.target.wants/hghac.service.
[root@hgdw231 etc]# systemctl enable hgdb-see-4.5.7.service
```

## 4、修改为单机节点的数据库检查数据库服务是否开机自启动，并启动数据库

```
[root@hgdw231 etc]# systemctl status hgdb-see-4.5.7.service
● hgdb-see-4.5.7.service - highgodb-4.5.7
   Loaded: loaded (/usr/lib/systemd/system/hgdb-see-4.5.7.service; enabled; vendor preset: disabled)
   Active: inactive (dead)

[root@hgdw231 etc]# pg_ctl start
等待服务器进程启动 ....2022-04-19 14:33:53 CST [21906]: [1-1] 625e57d1.5592 0     日志:  data encryption performed by sm4
2022-04-19 14:33:53 CST [21906]: [2-1] 625e57d1.5592 0     日志:  Password detection module is disabled
2022-04-19 14:33:53 CST [21906]: [3-1] 625e57d1.5592 0     日志:  正在启动 HighGo Security Enterprise Edition Database System 4.5.7 on CentOS7 x86_64,build on 20220302
2022-04-19 14:33:53 CST [21906]: [4-1] 625e57d1.5592 0     日志:  正在监听IPv4地址"0.0.0.0"，端口 5866
2022-04-19 14:33:53 CST [21906]: [5-1] 625e57d1.5592 0     日志:  正在监听IPv6地址"::"，端口 5866
2022-04-19 14:33:53 CST [21906]: [6-1] 625e57d1.5592 0     日志:  在Unix套接字 "/tmp/.s.PGSQL.5866"上侦听
2022-04-19 14:33:53 CST [21906]: [7-1] 625e57d1.5592 0     日志:  日志输出重定向到日志收集进程
2022-04-19 14:33:53 CST [21906]: [8-1] 625e57d1.5592 0     提示:  后续的日志输出将出现在目录 "hgdb_log"中.
 完成
服务器进程已经启动
```

## 5、所有节点停掉并禁用etcd服务

```
systemctl stop etcd.service
systemctl disable etcd.service
```

## 6、其他

执行hghactl等集群命令提示“未找到命令”，请配置环境变量，参考如下：

```
vim ~/.bash_profile

export PGPORT=5866
export PGUSER=sysdba
export PGDATABASE=highgo
export PGHOME=/opt/HighGo4.5.7-see
export PGDATA=/opt/HighGo4.5.7-see/data
export PATH=$PGHOME/bin:$PATH:$HOME/bin:/opt/HighGo/tools/hghac:/opt/HighGo/tools/hghac/etcd
export LD_LIBRARY_PATH=$PGHOME/lib:/usr/lib64:$LD_LIBRARY_PATH
export ETCDCTL_ENDPOINTS=http://10.1.194.182:2379,http://10.1.194.191:2379,http://10.1.194.192:2379
export PATRONICTL_CONFIG_FILE=/opt/HighGo/tools/hghac/hghac-see.yaml

source ~/.bash_profile
```

注意：

1、需要根据实际情况修改环境变量实际路径，可以使用find命令查找文件路径

例：查找hghac find / -iname hghac -print

2、ETCDCTL\_ENDPOINTS三个ip需要修改为配置etcd三节点的ip，可以参考/opt/HighGo/tools/hghac/hghac-see.yaml文件中的etcd:hosts
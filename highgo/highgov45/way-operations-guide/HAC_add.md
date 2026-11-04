---
title: "28、HAC集群添加新节点"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/HAC_add.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## HAC集群添加新节点

## 1、查看集群状态，使用A、B两种方法进行判断

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

## 2、新增节点安装数据库，hghac软件

```
rpm -ivh hgdb4.5.7-see-centos7-x86-64-20220307.rpm
rpm -ivh hghac4.0.1-centos7-x86-64-20210604.rpm
```

## 3、将主节点环境变量复制到新增节点，并使环境变量生效

```
vim ~/.bash_profile
source ~/.bash_profile
```

## 4、新增节点执行如下命令将主库hghac-see.yaml复制到本机

```
scp /opt/HighGo/tools/hghac root@192.168.80.228:/opt/HighGo/tools/hghac/hghac-see.yaml
```

## 5、新增节点修改hghac-see.yaml文件

```
vim /opt/HighGo/tools/hghac/hghac-see.yaml
connect_address: 192.168.80.228:8008   #将ip修改为本机ip,例：192.168.80.230:8008          
name: hghac228                  #修改为hghac+本机ip最后一位，例：hghac230
connect_address: 192.168.80.228:5866   #将ip修改为本机ip,例：192.168.80.230:5866  
data_dir: /hgdata/highgo/data        #查看/hgdata/highgo目录是否存在，
                           #不存在mkdir -p /hgdata/highgo创建，/hgdata目录应该是挂载的磁盘目录
dir: /hgdata/hghalog              #查看该目录是否存在，不存在mkdir -p /hgdata/hghalog 创建
```

## 6、新增节点设置集群服务开机自启动，并启动集群服务器和禁用数据库服务

```
[root@hgdw231 hgupload]# systemctl enable hghac.service
Created symlink from /etc/systemd/system/multi-user.target.wants/hghac.service to /etc/systemd/system/hghac.service.
[root@hgdw231 hgupload]# systemctl start hghac.service
[root@hgdw231 hgupload]#  systemctl disable hgdb-see-4.5.7.service
Removed symlink /etc/systemd/system/multi-user.target.wants/hgdb-see-4.5.7.service.
Removed symlink /etc/systemd/system/graphical.target.wants/hgdb-see-4.5.7.service.
```

注意：

也有可能不是hghac.service,可能是hghac-vip.service 请使用systemctl status hghac.service/hghac-vip.service确定运行的服务

## 7、检查集群状态

```
[root@localhost ~]# hghactl list
```

## 8、其他

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
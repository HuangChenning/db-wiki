---
title: "12、HAC集群修改管理员用户密码"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/HAC_username.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## HAC集群修改管理员用户密码

## 1、检查集群状态，使用A、B两种方法进行判断

### 方法A：使用集群命令，确保TL时间线一致，Lag in MB数据同步延迟不能过高，最好延迟为0。

```
[root@localhost ~]# hghactl list
Cluster: ha (7072256965608815760) -------+---------+----+-----------+
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

## 2、暂停集群

（任意节点执行即可，暂停集群只是停止集群主备切换，不影响数据库使用）

```
hghactl  pause
```

## 3、修改密码（只能在主库执行）

```
highgo=# alter user sysdba with password 'bx@H45cw!';
```

## 4、主备库修改密码文件

```
vim ~/.pgpass
#hostname:port:database:username:password
localhost:5866:highgo:sysdba:Highgo@12345
localhost:5866:highgo:syssso:Highgo@12345
```

冒号为分隔符，倒数第二位用户名，最后一位数据库密码，将密码修改为修改之后的密码即可，保存退出。

## 5、主备库修改集群配置文件

```
vim /opt/HighGo/tools/hghac/hghac.yaml
authentication:
    replication:   
      password: Hello@123   
      username: sysdba    
    rewind:    
      password: Hello@123    
      username: sysdba    
    sysdba:
      password: Hello@123  
    syssso:  
      password: Hello@123    
    syssao:   
      password: Hello@123
```

根据对应的用户名修改密码即可,保存退出。

## 6、备库修改data目录下的postgresql.auto.conf文件

```
vim $PGDATA/postgresql.auto.conf

primary_conninfo = 'user=sysdba password=''Highgo@123456'' host=192.168.80.228 port=5866 sslmode=prefer sslcompression=0 gssencmode=disable krbsrvname=postgres target_session_attrs=any'
```

注意：password前边的user为sysdba，即修改用户sysdba的密码

## 7、恢复集群（任意节点执行即可）

```
hghactl  resume
```

## 8、重启集群生效（任意节点执行即可）

```
hghactl restart c
注意：
最后一个参数c是集群的名字，查看方法
ps -ef | grep -v grep |grep post |awk '{print $9}'|tail -1|awk '{sub(/.$/,"")}1'
```

## 9、查看集群状态

```
hghactl  list
```

## 10、重新初始化所有节点的hgproxy

（如果没有使用hgproxy请跳过该步骤）

```
systemctl stop hgproxy-4.0.2.service   --停掉hgproxy服务，hgproxy后边具体内容请使用tab健补齐(proxy版本迭代service不一样)
proxy_ctl  init -h 192.168.1.54  -U sysdba -d highgo -p 5866  --初始化
systemctl start hgproxy-4.0.2.service  --启动hgproxy服务
```

## 11、其他

执行hghactl等集群命令提示“未找到命令”，请配置环境变量，参考如下：

```
vim ~/.bash_profile

export PGPORT=5866
export PGUSER=sysdba
export PGDATABASE=highgo
export PGHOME=/opt/HighGo4.5.7-see
export PGDATA=/opt/HighGo4.5.7-see/data
export PATH=$PGHOME/bin:$PATH:$HOME/bin:/opt/HighGo/tools/hgproxy/bin:/opt/HighGo/tools/hghac:/opt/HighGo/tools/hghac/etcd
export LD_LIBRARY_PATH=$PGHOME/lib:/usr/lib64:$LD_LIBRARY_PATH
export ETCDCTL_ENDPOINTS=http://10.1.194.182:2379,http://10.1.194.191:2379,http://10.1.194.192:2379
export PATRONICTL_CONFIG_FILE=/opt/HighGo/tools/hghac/hghac-see.yaml

source ~/.bash_profile
```

注意：

1、需要根据实际情况修改环境变量实际路径，可以使用find命令查找文件路径

```
例：查找hghac  
find / -iname hghac -print
```

2、ETCDCTL\_ENDPOINTS三个ip需要修改为配置etcd三节点的ip，可以参考/opt/HighGo/tools/hghac/hghac-see.yaml文件中的etcd:hosts
---
title: "8、启动hghac服务报错:OSError [Errno 98] Address already in use"
book: "数据库使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/hghac_starterror.html"
tags:
  - highgo
  - highgo-v45
  - faq-database-usage
---

## 启动hghac服务报错：OSError \[Errno 98\] Address already in use

启动hghac服务无法正常启动，检查服务状态报错：OSError: \[Errno 98\] Address already in use。  
查看patroni日志提示：

```
ERROR: Couldn't start a service on '0.0.0.0:8008', please check your \`restapi.listen\` configuration
```

## 1、问题原因

端口被占用

## 2、解决方案

### （1）使用netstat -tunlp 查看端口占用情况

```
[root@hgdw2 ~]# netstat -tunlp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:8008            0.0.0.0:*               LISTEN      1044/patroni
tcp        0      0 0.0.0.0:5866            0.0.0.0:*               LISTEN      1343/postgres
tcp        0      0 192.168.197.12:2379     0.0.0.0:*               LISTEN      21973/etcd
tcp        0      0 192.168.197.12:2380     0.0.0.0:*               LISTEN      21973/etcd
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      977/sshd
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      1149/master
tcp6       0      0 :::22                   :::*                    LISTEN      977/sshd
tcp6       0      0 ::1:25                  :::*                    LISTEN      1149/master
udp        0      0 127.0.0.1:323           0.0.0.0:*                           719/chronyd
udp6       0      0 ::1:323                 :::*                                719/chronyd
```

### （2）判断占用端口进程能否杀掉，如能杀掉执行kill命令

\_\_注意\_\_：kill前确认杀死进程是否影响业务

```
kill -9 1044
```
---
title: "5、psql远程连接-psql could not connect to server Connection refused"
book: "连接使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/remote_connection.html"
tags:
  - highgo
  - highgo-v45
  - faq-connections
---

## 使用psql远程连接数据库报错：Connection refused和No route to host

## 1、问题现象

使用psql远程连接数据库报错：Connection refused和No route to host。

```
psql: could not connect to server: Connection refused
```

![clip_image002](img/clip_image002.jpg)

```
psql: could not connect to server:No route to host
```
```
[highgo@hgdb ~]$ psql -h 192.168.10.123 -p 5866

psql: could not connect to server: No route to host

Is the server running on host "192.168.10.123" and accepting TCP/IP connections on p ort 5866?
```

## 2、解决方案

### （1）首先确认数据库服务是否已经启动。

![clip_image004](img/clip_image004.jpg)

### （2）检查监听并查看IP地址是否正确。

```
# su - highgo  $ cat  $PGDATA/postgresql.conf|grep listen  $ cat  $PGDATA/postgresql.auto.conf |grep listen  $ cat  $PGDATA/postgresql.conf|grep port  $ cat $PGDATA/postgresql.auto.conf  |grep port
```

例如：

```
listen_addresses = '*'

port = 5866
```

![clip_image006](img/clip_image006.jpg)

### （3）查看pg\_hba.conf文件确定是否具有正确的配置。

```
su – highgo

cat $PGDATA/pg_hba.conf
```

例如：允许远程主机192.168.10.123无密码访问数据库的配置如下

![clip_image008](img/clip_image008.jpg)

![clip_image010](img/clip_image010.jpg)
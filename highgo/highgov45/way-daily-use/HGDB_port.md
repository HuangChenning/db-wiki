---
title: "14、HGDB修改端口号指导手册"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/HGDB_port.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## HGDB修改端口号指导手册

## 1、文档用途

本文档为HGDB端口号修改指导手册。

## 2、详细信息

HGDB修改访问端口号：

### （1） 查看当前使用的端口号

查询HGDB的pid

```
[highgo@pgstandby ~]$ ps -ef|grep pos
root      17398   7579  0 14:10 pts/0    00:00:00 su - postgres
postgres  17399  17398  0 14:10 pts/0    00:00:00 -bash
highgo    37483      1 43 16:45 pts/0    00:00:01 /opt/HighGo4.3.4.8-see/bin/postgres
highgo    37485  37483  0 16:45 ?        00:00:00 postgres: logger process   
highgo    37489  37483  0 16:45 ?        00:00:00 postgres: checkpointer process   
highgo    37490  37483  0 16:45 ?        00:00:00 postgres: writer process   
highgo    37491  37483  0 16:45 ?        00:00:00 postgres: wal writer process   
highgo    37492  37483  1 16:45 ?        00:00:00 postgres: autovacuum launcher process  
highgo    37493  37483  0 16:45 ?        00:00:00 postgres: archiver process   
highgo    37494  37483  0 16:45 ?        00:00:00 postgres: stats collector process  
highgo    37495  37483  0 16:45 ?        00:00:00 postgres: bgworker: logical replication launcher 
highgo    37499  37439  0 16:45 pts/0    00:00:00 grep --color=auto pos
```

通过pid查询端口号

```
[highgo@pgstandby ~]$ netstat -antup |grep 37483
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
tcp        0      0 0.0.0.0:5866      0.0.0.0:*     LISTEN      37483/postgres     
tcp6       0      0 :::5866        :::*         LISTEN      37483/postgres
```

### （2）端口修改

检查端口是否被占用

```
[root@pgstandby1 bin]# lsof -i:5866
COMMAND    PID   USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
postgres 10668 highgo    3u  IPv4 1345178      0t0  TCP *:5866 (LISTEN)
postgres 10668 highgo    4u  IPv6 1345179      0t0  TCP *:5866 (LISTEN)
```

寻找到一个未被占用的端口，然后进行修改，保存退出

```
vi $PGDATA/postgresql.auto.conf

port=5700
```

重启数据库

```
pg_ctl restart
```

### (3)检查端口号是否修改成功

使用上述方式查看或登录数据库进行查询

```
show port;
```
  
根据实际情况判断是否将端口号添加到防火墙中，如防火墙已关闭，则无需添加  
中标麒麟等centos系列：
```
firewall-cmd --permanent --add-port=5899/tcp

firewall-cmd  --add-port=5899/tcp
```

银河麒麟v4等ubuntu系列：

```
iptables -A INPUT -p tcp --dport 5899 -j ACCEPT

iptables -A OUTPUT -p tcp --sport 5899 -j ACCEPT
```

详询操作系统厂商。

验证命令：

```
firewall-cmd --list-ports
```

注意：

除此之外，在HGDB的一些数据库脚本，配置文件中也包含有端口信息，如下：

例如：runpsql文件，依据操作系统类型的不同而不同，

对于Windows操作系统来说，以瀚高数据库企业版V5.6.5来举例，该文件是指D:\\highgo\\database\\5.6.5\\bin\\runpsql.bat

```
REM Run psql
:psqlcmd
psql.exe -h localhost -U "highgo" -d highgo -p 5866
```

对于Linux操作系统来说，以瀚高数据库安全版V4.3.4.8来举例，该文件是指/opt/HighGo4.3.4.8-see/bin/runpsql.sh

```
[highgo@pgstandby bin]$ grep 5866 ./*
Binary file ./pgauditreader matches
Binary file ./pg_config matches
Binary file ./postgres matches
Binary file ./postmaster matches
Binary file ./psql matches
./runipsql.sh:echo -n "Port [5866]: "
./runipsql.sh:    HGDBPORT="5866"
./runpsql.sh:LD_LIBRARY_PATH=/opt/HighGo4.3.4.8-see/lib:$LD_LIBRARY_PATH /opt/HighGo4.3.4.8-see/bin/psql -h localhost -p 5866 -U sysdba highgo
```

在其它脚本，例如runipsql.sh，配置文件，例如hg\_repmgr.conf等地方也有可能包含实际端口号

请修改端口时，考虑到修改需使用的脚本和配置文件的端口
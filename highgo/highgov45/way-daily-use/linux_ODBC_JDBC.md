---
title: "4、Linux 通过ODBC连接HGDB"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/linux_ODBC_JDBC.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## Linux 通过ODBC连接HGDB

## 一、ODBC安装

### 1、UnixODBC安装

```
# yum安装
  [root@localhost ~]yum install -y unixODBC.x86_64

# 验证安装
  [root@localhost ~]# rpm -qa | grep unixODBC
  unixODBC-2.3.1-14.el7.x86_64
```

### 2、PostgresqlODBC安装

```
# yum安装
  [root@localhost ~]yum install -y postgresql-odbc.x86_64

# 验证安装
  [root@localhost ~]rpm -qa | grep postgresql-odbc
  postgresql-odbc-09.03.0100-2.el7.x86_64
```

## 二、ODBC配置

### 1、查看odbcinst

```
# cat /etc/odbcinst.ini
[PostgreSQL]
Description = ODBC for PostgreSQL
Driver   = /usr/lib/psqlodbcw.so
Setup    = /usr/lib/libodbcpsqlS.so
Driver64  = /usr/lib64/psqlodbcw.so
Setup64   = /usr/lib64/libodbcpsqlS.so
FileUsage  = 1
```

### 2、配置odbc

```
# vim /etc/odbc.ini
[HGDB]
Description = Test to HGDB
Driver = PostgreSQL
Database = highgo
Servername = 192.168.80.126
UserName = highgo
Password = password
Port = 5866
ReadOnly = 0
ConnSettings = set client_encoding to UTF8
```

### 3、验证odbc

```
# isql访问
[root@localhost ~]isql HGDB highgo password

+---------------------------------------+
| Connected!              |
|                    |
| sql-statement             |
| help [tablename]           |
| quit                 |
|                    |
+---------------------------------------+
SQL>
```
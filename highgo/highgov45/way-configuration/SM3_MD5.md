---
title: "2、安全版V4.5密码加密算法由SM3改为MD5"
book: "配置类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/SM3_MD5.html"
tags:
  - highgo
  - highgo-v45
  - way-configuration
---

## 安全版V4.5密码加密算法由SM3改为MD5

## 1、用默认三权用户和普通用户登录数据库，修改密码加密算法并更改密码

```
[root@host ~]# psql -U sysdba -d highgo

highgo=# alter system set password_encryption ='md5';

highgo=# set password_encryption ='md5';

highgo=# alter user sysdba with password 'Hello@123';

highgo=# \q

[root@host ~]# psql -U syssso -d highgo

highgo=# set password_encryption ='md5';

highgo=# alter user syssso with password 'Hello@123';

highgo=# \q

[root@host ~]# psql -U syssao -d highgo

highgo=# set password_encryption ='md5';

highgo=# alter user syssao with password 'Hello@123';

highgo=# \q

[root@host ~]# psql -U test -d highgo

highgo=# set password_encryption ='md5';

highgo=# alter user test with password 'Hello@123';

highgo=# \q
```

## 2、更改.pgpass中的密码，如未配置.pgpass请忽略此步

```
[root@host ~]# vi ~/.pgpass

#hostname:port:database:username:password

localhost:5866:highgo:sysdba:Hello@123
```

## 3、修改数据目录中的pg\_hba.conf文件，将sm3改为md5

```
# TYPE DATABASE    USER      ADDRESS         METHOD

 

# "local" is for Unix domain socket connections only

local  all       all                md5

# IPv4 local connections

host  all       all       127.0.0.1/32     md5

host  all       all       0.0.0.0/0      md5

# IPv6 local connections:

host  all       all       ::1/128       md5

# Allow replication connections from localhost, by a user with the

# replication privilege.

local  replication   all                 md5

host  replication   all       127.0.0.1/32       md5

host  replication   all       ::1/128        md5
```

## 4、重启数据库

```
[root@host data]# pg_ctl restart
```

## 5、验证

```
[root@host ~]# psql -U sysdba -d highgo
#输入密码登入成功即可
```
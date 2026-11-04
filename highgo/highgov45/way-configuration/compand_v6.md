---
title: "5、企业版V6口令复杂度配置"
book: "配置类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/compand_v6.html"
tags:
  - highgo
  - highgo-v45
  - way-configuration
---

## 企业版V6口令复杂度配置

瀚高数据库企业版V6在创建新用户设置口令或修改已有用户口令时，默认要符合以下规则：

（1）最短长度8位，最长长度1024位。开关参数passwordlength，默认on。

（2）须同时含有数字 、大小写字母和特殊字符，特殊字符包括 “!@#$%^&\*()”。不能使用包含瀚高数据库关键字和当前用户名的密码，以及其他被数据库系统认定为过于简单的密码。开关参数passwordstrength，默认on。

（3）不能使用前五次使用过的密码。开关参数passwordhistory，默认on。

（4）创建用户所使用的密码不能含有瀚高保留字、关键字。

关闭以上口令复杂度功能需要使用管理员执行“alter system set passwordxxxx = off”后，重启数据库生效。

例：

## 1、关闭口令强度要求，设置简单密码

```
[highgo@host ~]$ psql highgo highgo

highgo=# create user test with password 'cQdGp#n3';

CREATE ROLE

highgo=# alter user test with password 'cqdcqdcqd';

ERROR: Password must contain upper and lower case letters, numbers, and special characters:cqdcqdcqd.

highgo=# alter system set passwordstrength = off;

ALTER SYSTEM

highgo=# \q

[highgo@host ~]$ pg_ctl restart

[highgo@host ~]$ psql highgo highgo

highgo=# alter user test with password 'cqdcqdcqd';

ALTER ROLE
```

## 2、关闭口令长度要求

```
[highgo@host ~]$ psql highgo highgo

highgo=# alter user test with password 'cqd';

ERROR: The password is too short

highgo=# alter system set passwordlength = off;

ALTER SYSTEM

highgo=# \q

[highgo@host ~]$ pg_ctl restart

[highgo@host ~]$ psql highgo highgo

highgo=# alter user test with password 'cqd';

ALTER ROLE
```

## 3、能重复设置之前的口令

```
[highgo@host ~]$ psql highgo highgo

highgo=# alter user test with password 'cqdcqdcqd';

ERROR: The password cannot be the same as the old password.

highgo=# alter system set passwordhistory = off;

ALTER SYSTEM

highgo=# \q

[highgo@host ~]$ pg_ctl restart

[highgo@host ~]$ psql highgo highgo

highgo=# alter user test with password 'cqdcqdcqd';

ALTER ROLE
```
---
title: "7、瀚高数据库修改用户密码及有效期"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/validity.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## 瀚高数据库修改用户密码及有效期

## 1、安全版

### 1.1 修改用户密码

#### 1）三权开启时

修改非管理员用户密码

• 安全保密管理员 syssso 用户修改普通用户（非管理员用户）密码。

• 用户连入修改自身密码。

```
--syssso 用户修改普通用户密码。（不可修改为5次以内的历史密码） 

[root@dj ~]# psql -U syssso

psql (4.5.7)

Type "help" for help.

highgo=> alter user u1 password 'Hello@1231';

ALTER ROLE

 

--用户连入修改自身密码。（不可修改为5次以内的历史密码）

highgo=> \c - u1

Password for user u1:

You are now connected to database "highgo" as user "u1".

highgo=> alter user u1 password 'Hello@1232';

ALTER ROLE
```

修改管理员用户密码

• 用户连入修改自身密码。

```
--用户连入修改自身密码。（不可修改为5次以内的历史密码）

[root@dj ~]# psql -U sysdba

psql (4.5.7)

Type "help" for help.

highgo=# alter user sysdba password 'Hello@1231';

ALTER ROLE

highgo=# \c - syssso

You are now connected to database "highgo" as user "syssso".

highgo=> alter user syssso password 'Hello@1231';

ALTER ROLE

highgo=> \c - syssao

You are now connected to database "highgo" as user "syssao".

highgo=> alter user syssao password 'Hello@1231';

ALTER ROLE
```

#### 2）三权关闭时

• 系统管理员 sysdba 用户可修改所有用户密码。

• 用户连入修改自身密码。

```
--sysdba 用户修改所有用户密码

[root@dj ~]# psql -U sysdba

psql (4.5.7)

Type "help" for help.

highgo=# alter user sysdba password 'Hello@123';

ALTER ROLE

highgo=# alter user syssso password 'Hello@123';

ALTER ROLE

highgo=# alter user syssao password 'Hello@123';

ALTER ROLE

highgo=# alter user u1 password 'Hello@123';

ALTER ROLE

 

--用户连入修改自身密码。

[root@dj ~]# psql -U sysdba

psql (4.5.7)

Type "help" for help.

highgo=# alter user sysdba password 'Hello@123';

ALTER ROLE

highgo=# \c - syssso

You are now connected to database "highgo" as user "syssso".

highgo=> alter user syssso password 'Hello@123';

ALTER ROLE

highgo=> \c - syssao

You are now connected to database "highgo" as user "syssao".

highgo=> alter user syssao password 'Hello@123';

ALTER ROLE

highgo=> \c - u1

Password for user u1:

You are now connected to database "highgo" as user "u1".

highgo=> alter user u1 password 'Hello@123';

ALTER ROLE
```

#### 3）管理员密码遗忘时（非常规手段）

• 单用户模式连入修改管理员密码（需停库）。

```
--单用户模式修改密码。（不论三权是否开启，均不可修改为5次以内的历史密码，回车后无回显信息，ctrl+d 直接退出即可） 

[root@dj ~]# pg_ctl stop

waiting for server to shut down....... done

server stopped

[root@dj ~]# postgres --single

2023-05-09 17:53:10.256 CST [8400] LOG: data encryption performed by sm4

2023-05-09 17:53:10.510 CST [8400] LOG: Switchover the SSHA Role. Current is NONE

2023-05-09 17:53:10.512 CST [8400] FATAL: database "root" does not exist

[root@dj ~]# postgres --single highgo

2023-05-09 17:54:26.414 CST [8412] LOG: data encryption performed by sm4

2023-05-09 17:54:26.624 CST [8412] LOG: Switchover the SSHA Role. Current is NONE

PostgreSQL stand-alone backend 12.7

backend> alter user sysdba password 'Hello@123456';

backend> alter user syssso password 'Hello@123456';
```

### 1.2 修改用户有效期

#### 1）三权开启时

修改非管理员用户有效期

• 普通用户（非管理员用户）可使用安全保密管理员 syssso 用户延期。

```
--使用 syssso 用户将普通用户延期至指定时间

highgo=> alter user u1 valid until '2099-09-09';

ALTER ROLE

highgo=> \du

                                List of roles

 Role name |                     Attributes                      | Member of

-----------+-----------------------------------------------------+-----------

 sysdba    | No inheritance, Create role, Create DB, Replication+| {}

           | Password valid until 2023-05-16 17:14:03+08         |

 syssao    | No inheritance                                     +| {}

           | Password valid until 2023-05-16 17:14:26+08         |

 syssso    | No inheritance                                     +| {}

           | Password valid until 2023-05-16 17:14:15+08         |

 u1        | Password valid until 2099-09-09 00:00:00+08         | {}

 

--使用 syssso 用户将普通用户延期至永久

highgo=> alter user u1 valid until 'infinity';

ALTER ROLE

highgo=> \du

                                List of roles

 Role name |                     Attributes                      | Member of

-----------+-----------------------------------------------------+-----------

 sysdba    | No inheritance, Create role, Create DB, Replication+| {}

           | Password valid until 2023-05-16 17:14:03+08         |

 syssao    | No inheritance                                     +| {}

           | Password valid until 2023-05-16 17:14:26+08         |

 syssso    | No inheritance                                     +| {}

           | Password valid until 2023-05-16 17:14:15+08         |

 u1        | Password valid until infinity                       | {}
```

修改管理员用户有效期

• 通过安全保密管理员 syssso 用户调整密码策略，修改密码生效策略。

```
--密码有效期策略调至指定时间 180 天，该策略调整后仅对后续新建用户有效，已存在用户若要应用该策略，需重置密码。

[root@dj ~]# psql -U syssso

psql (4.5.7)

Type "help" for help.

highgo=> select show_secure_param();

            show_secure_param

-----------------------------------------

   hg_sepofpowers = on,                 +

   hg_macontrol = min,                  +

   hg_rowsecure = off,                  +

   hg_showlogininfo = off,              +

   hg_clientnoinput = 30 min(s),        +

   hg_idcheck.enable = on,              +

   hg_idcheck.pwdlock = 5 time(s),      +

   hg_idcheck.pwdlocktime = 24 hour(s), +

   hg_idcheck.pwdvaliduntil = 7 day(s), +

   hg_idcheck.pwdpolicy = highest,      +

   hg_sepv4 = v4,                       +

(1 row)

 

highgo=> select set_secure_param('hg_idcheck.pwdvaliduntil','180');

        set_secure_param

---------------------------------

 set configuration successfully.

(1 row)

 

highgo=> select show_secure_param();

             show_secure_param

-------------------------------------------

   hg_sepofpowers = on,                   +

   hg_macontrol = min,                    +

   hg_rowsecure = off,                    +

   hg_showlogininfo = off,                +

   hg_clientnoinput = 30 min(s),          +

   hg_idcheck.enable = on,                +

   hg_idcheck.pwdlock = 5 time(s),        +

   hg_idcheck.pwdlocktime = 24 hour(s),   +

   hg_idcheck.pwdvaliduntil = 180 day(s), +

   hg_idcheck.pwdpolicy = highest,        +

   hg_sepv4 = v4,                         +

(1 row)

 

--管理员用户连入修改自身密码。（因三权开启，不可修改为5次以内历史密码，若要将密码改为跟原来一样，需先改五次其他密码）

highgo=> \du

                                List of roles

 Role name |                     Attributes                      | Member of

-----------+-----------------------------------------------------+-----------

 sysdba    | No inheritance, Create role, Create DB, Replication+| {}

           | Password valid until 2023-05-17 09:16:09+08         |

 syssao    | No inheritance                                     +| {}

           | Password valid until 2023-05-16 17:33:36+08         |

 syssso    | No inheritance                                     +| {}

           | Password valid until 2023-05-16 17:33:23+08         |

 u1        | Password valid until infinity                       | {}

 

highgo=> alter user syssso password 'Hello@12311';

ALTER ROLE

highgo=> alter user syssso password 'Hello@12312';

ALTER ROLE

highgo=> alter user syssso password 'Hello@12313';

ALTER ROLE

highgo=> alter user syssso password 'Hello@12314';

ALTER ROLE

highgo=> alter user syssso password 'Hello@12315';

ALTER ROLE

highgo=> alter user syssso password 'Hello@123';

ALTER ROLE

highgo=> \c - sysdba

You are now connected to database "highgo" as user "sysdba".

highgo=# alter user sysdba password 'Hello@12311';

ALTER ROLE

highgo=# alter user sysdba password 'Hello@12312';

ALTER ROLE

highgo=# alter user sysdba password 'Hello@12313';

ALTER ROLE

highgo=# alter user sysdba password 'Hello@12314';

ALTER ROLE

highgo=# alter user sysdba password 'Hello@12315';

ALTER ROLE

highgo=# alter user sysdba password 'Hello@123';

ALTER ROLE

highgo=# \c - syssao

You are now connected to database "highgo" as user "syssao".

highgo=> alter user syssao password 'Hello@12311';

ALTER ROLE

highgo=> alter user syssao password 'Hello@12312';

ALTER ROLE

highgo=> alter user syssao password 'Hello@12313';

ALTER ROLE

highgo=> alter user syssao password 'Hello@12314';

ALTER ROLE

highgo=> alter user syssao password 'Hello@12315';

ALTER ROLE

highgo=> alter user syssao password 'Hello@123';

ALTER ROLE

highgo=> \du

                                List of roles

 Role name |                     Attributes                      | Member of

-----------+-----------------------------------------------------+-----------

 sysdba    | No inheritance, Create role, Create DB, Replication+| {}

           | Password valid until 2023-11-06 09:18:51+08         |

 syssao    | No inheritance                                     +| {}

           | Password valid until 2023-11-06 09:19:02+08         |

 syssso    | No inheritance                                     +| {}

           | Password valid until 2023-11-06 09:18:31+08         |

 u1        | Password valid until infinity                       | {}

 

--密码有效期策略调至无限期，该策略调整后仅对后续新建用户有效，已存在用户若要应用该策略，需重置密码。

[root@dj ~]# psql -U syssso

psql (4.5.7)

Type "help" for help.

highgo=> select show_secure_param();

             show_secure_param

-------------------------------------------

   hg_sepofpowers = on,                   +

   hg_macontrol = min,                    +

   hg_rowsecure = off,                    +

   hg_showlogininfo = off,                +

   hg_clientnoinput = 30 min(s),          +

   hg_idcheck.enable = on,                +

   hg_idcheck.pwdlock = 5 time(s),        +

   hg_idcheck.pwdlocktime = 24 hour(s),   +

   hg_idcheck.pwdvaliduntil = 180 day(s), +

   hg_idcheck.pwdpolicy = highest,        +

   hg_sepv4 = v4,                         +

(1 row)

 

highgo=> select set_secure_param('hg_idcheck.pwdvaliduntil','0');

        set_secure_param

---------------------------------

 set configuration successfully.

(1 row)

 

highgo=> select show_secure_param();

            show_secure_param

-----------------------------------------

   hg_sepofpowers = on,                 +

   hg_macontrol = min,                  +

   hg_rowsecure = off,                  +

   hg_showlogininfo = off,              +

   hg_clientnoinput = 30 min(s),        +

   hg_idcheck.enable = on,              +

   hg_idcheck.pwdlock = 5 time(s),      +

   hg_idcheck.pwdlocktime = 24 hour(s), +

   hg_idcheck.pwdvaliduntil = 0 day(s), +

   hg_idcheck.pwdpolicy = highest,      +

   hg_sepv4 = v4,                       +

(1 row)

 

highgo=> alter user syssso password 'Hello@12311';

ALTER ROLE

highgo=> alter user syssso password 'Hello@12312';

ALTER ROLE

highgo=> alter user syssso password 'Hello@12313';

ALTER ROLE

highgo=> alter user syssso password 'Hello@12314';

ALTER ROLE

highgo=> alter user syssso password 'Hello@12315';

ALTER ROLE

highgo=> alter user syssso password 'Hello@123';

ALTER ROLE

highgo=> \c - sysdba

You are now connected to database "highgo" as user "sysdba".

highgo=# alter user sysdba password 'Hello@12311';

ALTER ROLE

highgo=# alter user sysdba password 'Hello@12312';

ALTER ROLE

highgo=# alter user sysdba password 'Hello@12313';

ALTER ROLE

highgo=# alter user sysdba password 'Hello@12314';

ALTER ROLE

highgo=# alter user sysdba password 'Hello@12315';

ALTER ROLE

highgo=# alter user sysdba password 'Hello@123';

ALTER ROLE

highgo=# \c - syssao

You are now connected to database "highgo" as user "syssao".

highgo=> alter user syssao password 'Hello@12311';

ALTER ROLE

highgo=> alter user syssao password 'Hello@12312';

ALTER ROLE

highgo=> alter user syssao password 'Hello@12313';

ALTER ROLE

highgo=> alter user syssao password 'Hello@12314';

ALTER ROLE

highgo=> alter user syssao password 'Hello@12315';

ALTER ROLE

highgo=> alter user syssao password 'Hello@123';

ALTER ROLE

highgo=> \du

                                List of roles

 Role name |                     Attributes                      | Member of

-----------+-----------------------------------------------------+-----------

 sysdba    | No inheritance, Create role, Create DB, Replication+| {}

           | Password valid until infinity                       |

 syssao    | No inheritance                                     +| {}

           | Password valid until infinity                       |

 syssso    | No inheritance                                     +| {}

           | Password valid until infinity                       |

 u1        | Password valid until infinity                       | {}

2）三权关闭时

• 用户不受有效期限制，即便查询结果中显示到期时间，也无影响。

 

[root@dj ~]# psql -U syssso

psql (4.5.7)

Type "help" for help.

highgo=> select show_secure_param();

            show_secure_param

-----------------------------------------

   hg_sepofpowers = off,                +

   hg_macontrol = min,                  +

   hg_rowsecure = off,                  +

   hg_showlogininfo = off,              +

   hg_clientnoinput = 30 min(s),        +

   hg_idcheck.enable = off,             +

   hg_idcheck.pwdlock = 5 time(s),      +

   hg_idcheck.pwdlocktime = 24 hour(s), +

   hg_idcheck.pwdvaliduntil = 7 day(s), +

   hg_idcheck.pwdpolicy = highest,      +

   hg_sepv4 = off,                      +

(1 row)

 

highgo=> \du

                                List of roles

 Role name |                     Attributes                      | Member of

-----------+-----------------------------------------------------+-----------

 sysdba    | No inheritance, Create role, Create DB, Replication+| {}

           | Password valid until infinity                       |

 syssao    | No inheritance                                     +| {}

           | Password valid until infinity                       |

 syssso    | No inheritance                                     +| {}

           | Password valid until infinity                       |

 u1        | Password valid until 2022-09-09 00:00:00+08         | {}

highgo=> \! date

Wed May 10 09:40:03 CST 2023

highgo=> \c - u1

Password for user u1:

You are now connected to database "highgo" as user "u1".

highgo=> create table t1(id int);

CREATE TABLE

highgo=> \dt

       List of relations

 Schema | Name | Type  | Owner

--------+------+-------+-------

 public | t1   | table | u1

(1 row)

highgo=> drop table t1;

DROP TABLE

 

二、企业版

2.1 修改用户密码

1）正常情况下修改密码

• highgo 管理员用户修改所有密码。

• 用户连入修改自身密码。

 

--highgo 管理员用户修改所有用户密码。（不可修改为5次以内的历史密码）

[highgo@dj ~]$ psql -U highgo

psql (HighGo Database 6 Release 6.0.4-64-bit Production)

 

PSQL: Release HighGo Database 6 Release 6.0.4-64-bit Production

Type "help" for help.

highgo=# alter user highgo password 'Hello@1231';

ALTER ROLE

highgo=# alter user test password 'Hello@1231';

ALTER ROLE

 

--用户连入修改自身密码。（不可修改为5次以内的历史密码）

highgo=# \c - test

Password for user test:

PSQL: Release HighGo Database 6 Release 6.0.4-64-bit Production

You are now connected to database "highgo" as user "test".

highgo=> alter user test password 'Hello@1232';

ALTER ROLE

2）管理员密码遗忘时（非常规手段）

• 修改认证方式，免密连入数据库修改密码。

 

--修改配置文件，本地登录认证方式改为 trust 

[highgo@dj ~]$ vi $PGDATA/pg_hba.conf

[highgo@dj ~]$ cat $PGDATA/pg_hba.conf|sed -n 80,100p

 

# TYPE DATABASE USER ADDRESS METHOD

 

# "local" is for Unix domain socket connections only

local all all trust

# IPv4 local connections:

host all all 127.0.0.1/32 md5

# IPv6 local connections:

host all all ::1/128 md5

# Allow replication connections from localhost, by a user with the

# replication privilege.

local replication all md5

host replication all 127.0.0.1/32 md5

host replication all ::1/128 md5

host all all 0.0.0.0/0 md5

 

--生效修改

[highgo@dj ~]$ pg_ctl reload

server signaled

 

--免密连入数据库修改密码

[highgo@dj ~]$ psql -U highgo

psql (HighGo Database 6 Release 6.0.4-64-bit Production)

 

PSQL: Release HighGo Database 6 Release 6.0.4-64-bit Production

Type "help" for help.

 

highgo=# alter user highgo password 'Hello@123456';

ALTER ROLE

highgo=# exit

 

--调回之前 md5认证策略

[highgo@dj ~]$ vi $PGDATA/pg_hba.conf

[highgo@dj ~]$ cat $PGDATA/pg_hba.conf|sed -n 80,100p

 

# TYPE DATABASE USER ADDRESS METHOD

 

# "local" is for Unix domain socket connections only

local all all md5

# IPv4 local connections:

host all all 127.0.0.1/32 md5

# IPv6 local connections:

host all all ::1/128 md5

# Allow replication connections from localhost, by a user with the

# replication privilege.

local replication all md5

host replication all 127.0.0.1/32 md5

host replication all ::1/128 md5

host all all 0.0.0.0/0 md5

[highgo@dj ~]$ pg_ctl reload

server signaled

 

2.2 修改用户有效期

• highgo 管理员用户有效期默认为无限期（不可修改）。

• 普通用户（非管理员用户）有效期，可使用 highgo 管理员用户修改。

 

[highgo@dj ~]$ psql -U highgo

psql (HighGo Database 6 Release 6.0.4-64-bit Production)

PSQL: Release HighGo Database 6 Release 6.0.4-64-bit Production

Type "help" for help.

 

highgo=# \du

                                   List of roles

 Role name |                         Attributes                         | Member of

-----------+------------------------------------------------------------+-------

 highgo    | Superuser, Create role, Create DB, Replication, Bypass RLS        | {}

 test       | Password valid until 2023-05-17 09:58:41.10164+08             | {}

 

highgo=# alter user test valid until '2023-09-09';

ALTER ROLE

highgo=# \du

                                   List of roles

 Role name |                         Attributes                         | Member of

-----------+------------------------------------------------------------+-------

 highgo    | Superuser, Create role, Create DB, Replication, Bypass RLS       | {}

 test       | Password valid until 2023-09-09 00:00:00+08                  | {}

 

highgo=# alter user test valid until 'infinity';

ALTER ROLE

highgo=# \du

                                   List of roles

 Role name |                         Attributes                         | Member of

-----------+------------------------------------------------------------+-------

 highgo    | Superuser, Create role, Create DB, Replication, Bypass RLS       | {}

 test       | Password valid until infinity                                  | {}

 

2.3 用户有效期策略调整

• highgo 管理员用户连入调整有效期策略，调整后仅对后续新建用户有效，已存在用户若要应用该策略，需重置密码。（highgo 管理员用户不受有效期策略限制）

 

--用户有限期策略调整为 180 天

[highgo@dj ~]$ psql

psql (HighGo Database 6 Release 6.0.4-64-bit Production)

PSQL: Release HighGo Database 6 Release 6.0.4-64-bit Production

Type "help" for help.

 

highgo=# select show_secure_param();

           show_secure_param

---------------------------------------

 hg_idcheck.pwdlock = 5 time(s),      +

 hg_idcheck.pwdlocktime = 24 hour(s), +

 hg_idcheck.pwdvaliduntil = 7 day(s), +

(1 row)

 

highgo=# select set_secure_param('hg_idcheck.pwdvaliduntil','180');

        set_secure_param

---------------------------------

 set configuration successfully.

(1 row)

 

highgo=# select show_secure_param();

            show_secure_param

-----------------------------------------

 hg_idcheck.pwdlock = 5 time(s),        +

 hg_idcheck.pwdlocktime = 24 hour(s),   +

 hg_idcheck.pwdvaliduntil = 180 day(s), +

(1 row)

 

highgo=# \du

                                   List of roles

 Role name |                         Attributes                         | Member of

-----------+------------------------------------------------------------+-------

 highgo    | Superuser, Create role, Create DB, Replication, Bypass RLS        | {}

 test       | Password valid until infinity                                   | {}

 

highgo=# create user u1 password 'Hello@123';

CREATE ROLE

highgo=# alter user test password 'Hello@1234123';

ALTER ROLE

highgo=# \du

                                   List of roles

 Role name |                         Attributes                         | Member of

-----------+------------------------------------------------------------+-------

 highgo    | Superuser, Create role, Create DB, Replication, Bypass RLS        | {}

 test       | Password valid until 2023-11-06 10:26:56.715074+08            | {}

 u1        | Password valid until 2023-11-06 10:26:38.088548+08            | {}

 

--用户有限期策略调整为无限期

highgo=# select set_secure_param('hg_idcheck.pwdvaliduntil','0');

        set_secure_param

---------------------------------

 set configuration successfully.

(1 row)

 

highgo=# select show_secure_param();

           show_secure_param

---------------------------------------

 hg_idcheck.pwdlock = 5 time(s),      +

 hg_idcheck.pwdlocktime = 24 hour(s), +

 hg_idcheck.pwdvaliduntil = 0 day(s), +

(1 row)

 

highgo=# \du

                                   List of roles

 Role name |                         Attributes                         | Member of

-----------+------------------------------------------------------------+-------

 highgo    | Superuser, Create role, Create DB, Replication, Bypass RLS        | {}

 test       | Password valid until 2023-11-06 10:26:56.715074+08            | {}

 u1        | Password valid until 2023-11-06 10:26:38.088548+08            | {}

 

highgo=# create user u2 password 'Hello@123';

CREATE ROLE

highgo=# alter user test password 'Hello@111';

ALTER ROLE

highgo=# alter user u1 password 'Hello@111';

ALTER ROLE

highgo=# \du

                                   List of roles

 Role name |                         Attributes                         | Member of

-----------+------------------------------------------------------------+-------

 highgo    | Superuser, Create role, Create DB, Replication, Bypass RLS        | {}

 test       | Password valid until infinity                                   | {}

 u1        | Password valid until infinity                                   | {}

 u2        | Password valid until infinity                                   | {}
```
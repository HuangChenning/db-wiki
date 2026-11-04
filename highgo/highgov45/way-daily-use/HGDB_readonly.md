---
title: "13、HGDB 创建只读用户"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/HGDB_readonly.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## HGDB 创建只读用户

## 1、以超级用户highgo登录数据库，创建用户：

```
highgo=# create user read_only with password 'read';
CREATE ROLE
```

## 2、设置为只读的transaction：

```
highgo=# alter user read_only set default_transaction_read_only = on;
ALTER ROLE
```

## 3、访问非 public 模式中的表:

默认在highgo数据库的public模式下的对象是可以访问的,如果要访问别的schema的表，则需要两步：

### (1)首先要有使用schema的权限：

```
highgo=# grant usage on schema test_schema to read_only ;
GRANT
```

### (2)然后加所有表的只读权限：

```
highgo=# grant select on all tables in schema test_schema to read_only; 
GRANT
如果不想给所有表的查询权限，则单独给某个表的查询权限：
highgo=# grant select on TABLE test_schema.abc to read_only; 
GRANT
```

## 4、可以进行一下权限测试:

```
[highgo@localhost ~]$ psql -U read_only highgo 
highgo=> select * from test_schema.abc limit 1;
 a |        b         
---+----------------------------------
 1 | db18340e7e9a86ea85a64addd9ea309f
(1 row)

highgo=> insert into test_schema.abc values(10,'10');
ERROR: 25006: cannot execute INSERT in a read-only transaction
highgo=> delete from test_schema.abc where a=1;
ERROR: 25006: cannot execute DELETE in a read-only transaction
highgo=> update test_schema.abc set b = 'xx' where a = 1;
ERROR: 25006: cannot execute UPDATE in a read-only transaction
```

## 5、如果要在别的数据库访问:

### (1) 先要用highgo（超级用户登录），然后\\c到对应的数据库:

```
highgo=# \c test
PSQL: Release 5.6.4
Connected to:
HighGo Database V5.6 Enterprise Edition Release 5.6.4 - 64-bit Production
You are now connected to database "test" as user "highgo".
```

### (2) 执行下面的命令，将对应的schema的表查询权限给这个用户：

```
# test数据库的public模式的usage权限是默认就有的，只需要添加表的只读权限即可：
test=# grant select on all tables in schema public to read_only;
GRANT
```

## 6、授予对只读用户的默认访问权限，对于对应模式 schema 下后期新创建的表也生效。

默认在对应模式下新创建的数据表,只读用户是没有访问权限的,需要手工赋权;可以修改默认权限让只读用户直接拥有新表的访问权限

这样即使是该模式中新加的表，read\_only用户都有只读权限

```
test=# alter default privileges in schema public grant select on tables to read_only;
ALTER DEFAULT PRIVILEGES
```
---
title: "6、HGDB Extension"
book: "配置类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/HGDB_Extension.html"
tags:
  - highgo
  - highgo-v45
  - way-configuration
---

## HGDB Extension

## 1、介绍

HGDB被设计为易于扩展。因此，加载到数据库中的扩展功能就可以像内置的特性一样运行。与源代码一起发布的contrib/ 目录包含一些核心代码中的扩展。也有一些扩展是独立开发的，比如PostGIS，需要单独下载安装。

例如，pg\_pool是一个受欢迎的主/备用复制解决方案，它是独立于核心项目开发的。

HGDB引入了一种方式来安装contrib模块，称为扩展（extensions）。

此方法适用于所有使用扩展规范构建的contrib模块，包括如下：

扩展SQL文件（ extension\_name.sql ）

扩展控制文件 （ extension\_name.control ）

扩展库文件（extension\_name.so）

hgdb的扩展插件通常位于目录$PGHOME/share/extension中。

编译安装过程中，通常安装HGDB源码文件中的contrib文件夹中安装程序脚本。如果尚未安装，则目录中不会有这些插件。

## 2、查看

通过以下两个视图查看数据库可安装的扩展插件和已安装的扩展插件

pgaudit扩展插件可安装

```
postgres=# select * from pg_available_extensions where name like '%audit%';
  name   | default_version | installed_version |             comment            
---------+-----------------+-------------------+---------------------------------
 pgaudit | 1.2.1           | 1.2.1             | provides auditing functionality
(1 row)
```

已安装的扩展如下

```
postgres=# select * from pg_extension;
      extname       | extowner | extnamespace | extrelocatable | extversion |   extconfig   | extcondition
--------------------+----------+--------------+----------------+------------+---------------+--------------
 plpgsql            |       10 |           11 | f              | 1.0        |               |
 pg_buffercache     |       10 |         2200 | t              | 1.3        |               |
 pg_pathman         |       10 |         2200 | f              | 1.5        | {98416,98427} | {"",""}
 pg_stat_statements |       10 |         2200 | t              | 1.5        |               |
 pgcrypto           |       10 |         2200 | t              | 1.3        |               |
(5 rows)
postgres=#
```

## 3、扩展插件的维护

修改扩展插件所属模式

这里新添加的扩展属于public模式，另外pg\_catalog这个schema是HGDB默认的元数据schema，所有的元数据都在这里。创建在pg\_catalog里面的扩展优先级最高，所有用户可见。

可以运行如下指令指定或修改扩展的所属模式：

```
create extension extension_name with schema pg_catalog;
alter extension extension_name set schema pg_catalog;
```
```
Example：
postgres=# alter extension pgaudit set schema pg_catalog;
ALTER EXTENSION
postgres=# \dx
                                     List of installed extensions
        Name        | Version |   Schema   |                        Description                       
--------------------+---------+------------+-----------------------------------------------------------
 pg_buffercache     | 1.3     | zscs       | examine the shared buffer cache
 pg_stat_statements | 1.6     | public     | track execution statistics of all SQL statements executed
 pgaudit            | 1.2.1   | pg_catalog | provides auditing functionality
 plpgsql            | 1.0     | pg_catalog | PL/pgSQL procedural language
(4 rows)
postgres=#
```

删除扩展插件

```
postgres=# drop extension pgaudit;
DROP EXTENSION
postgres=# \dx
                                 List of installed extensions
    Name        | Version |   Schema   |                        Description                       
--------------------+---------+------------+-----------------------------------------------------------
 pg_buffercache     | 1.3     | zscs       | examine the shared buffer cache
 pg_stat_statements | 1.6     | public     | track execution statistics of all SQL statements executed
 plpgsql            | 1.0     | pg_catalog | PL/pgSQL procedural language
(3 rows)
```
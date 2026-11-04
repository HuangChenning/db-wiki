---
title: "21、逻辑导入导出(pg_dumppg_restore)-导入到不同的schema或tablespace"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/pg_dumppg_restore.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## 逻辑导入导出(pg\_dump/pg\_restore)-导入到不同的schema或tablespace

逻辑导入导出，导入到不同的schema或tablespace

如果需要将数据导入到不同的schema，tablespace。如何做？

实现方式：将schema数据导出为Fp平面文件，及sql脚本的形式，然后替换sql脚本中的schema和tablespace，再将其导入到数据库中。

步骤如下：

1 、使用pg\_dump工具实现平面文件格式备份文件，将数据字典和表数据分开导出

如：导出schema pub数据

```
导出字典信息
pg_dump -Fp -s -v -n pub test -f /backup/pub_dic.dmp
导出表数据
pg_dump -Fp -a -v -n pub test -f /backup/pub_data.dmp
```

2 、创建新的用户和schema

如：创建新用户和schema test\_1209

```
psql -d tpsgdb -U postgres

create role prod_1209 with login password 'test_1209';

create schema if not exists test_1209;

grant all on schema prod_1209 to test_1209;
```

3 、替换备份文件中schema的名字

如 将schema pub替换为schema test\_1209

```
替换字典备份文件

sed -i "s/pub/test_1209/g" /backup/pub_dic.dmp

替换数据备份文件

sed -i "s/COPY pub/COPY test_1209/g" /backup/pub_data.dmp
```

4 、替换替换字典备份文件中的tablespace参数设置

```
sed -i "s/default_tablespace='postgres'/default_tablespace='test'/g" /backup/pub_dic.dmp
```

5 、导入数据到新schema和tablespace

如：

```
连接新用户

psql -d testt -U test_1209

or

tpsgdb=# \c testt test_1209
```

导入数据

```
tpsgdb=> \i /backup/pub_dic.dmp

tpsgdb=> \i /backup/pub_data.dmp
```
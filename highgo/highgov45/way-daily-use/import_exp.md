---
title: "1、数据库数据导入导出使用方法"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/import_exp.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## 数据库数据导入导出使用方法

## 1、导出某个业务库(highgo)的数据

```
[root@localhost ~]# pg_dump -O -Fp  -U sysdba -d  highgo -f  /opt/highgo.sql
```

## 2、导出某个模式(public)下所有表的数据

```
[root@localhost ~]# pg_dump -O -Fp  -U sysdba -d  highgo  -n  public -f  /opt/public.sql
```

## 3、导出某个业务表(test)的数据

```
[root@localhost ~]# pg_dump -O -Fp  -U sysdba -d  highgo  -t  test -f  /opt/test.sql
```

## 4、只导出某个表的表结构

```
[root@localhost ~]# pg_dump -O -Fp -s -U sysdba -d  highgo -t test  -f  /opt/test-ddl.sql
```

## 5、数据导入

```
[root@localhost ~]# psql  -U test -d  test   -f  导出文件的绝对地址
```
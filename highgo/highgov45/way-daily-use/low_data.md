---
title: "3、数据量很小但是data目录很大的排查思路"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/low_data.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## 数据量很小但是data目录很大的排查思路

在数据库服务正常运行阶段，可能会出现数据量很小但是data目录很大的情况。下面将对此类情况的排查思路进行介绍。

## 1、排查data目录下的pg\_wal目录占用大小。

```
在data目录下执行命令：

$ du -sh {pg_wal,pg_xlog}

33G   pg_wal
```

该目录下存放数据库的在线重做日志，可以通过max\_wal\_size和wal\_keep\_segments参数对wal日志保留上限进行限制。在配有复制槽的流复制环境下，主备延迟变大时也会造成此目录占用空间过大。

## 2、排查data目录下的审计日志目录占用大小。

```
$ du -sh *audit*

248M  hgaudit
```

此类目录下存放数据库的审计日志，可以通过审计参数进行限制。

## 3、排查data目录下的运行日志目录占用大小。

```
$ du -sh {hgdb_log,log}   

68K   hgdb_log
```

此类目录下存放数据库的运行日志，可以通过配置数据库log参数进行限制。

## 4、排查data目录下的core文件占用大小。

```
$ ls -lh core*

-rw------- 1 highgo dba 2.8G  Nov 9 2018 core.5643
```

当data目录下存在core文件，说明数据库进程存在过崩溃，可通过core文件进行分析。不需要的情况可以删除。

## 5、考察表膨胀情况。

在经过一段时间的增删改后，在有效数据量并未发生大的变化的情况下，表占用空间不断增大的情况我们称之为表膨胀或索引膨胀。此时需要通过一些手段将其查询出来进行空间回收，降低空间使用率。
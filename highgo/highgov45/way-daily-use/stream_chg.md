---
title: "15、HighGo Database 流复制切换"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/stream_chg.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## HighGo Database 流复制切换

pg\_rewind是流复制维护时一个非常好的数据同步工具，用于在未关闭原主库便将备库提升为主库的情况下，将原主库恢复为备库。pg\_rewind并非全量从主库同步数据，只是复制变化的数据。

## 1、使用pg\_rewind的前提条件为以下之一：

• wal\_log\_hints参数设置为on  
• 数据库initdb时使用了 –data-checksums选项，打开这个选项开启后会在数据块上进行检测以发现I/O错误，开启后性能有损失。  
• full\_page\_writes也必须被设置为on，这是默认的。

## 2、pg\_rewind原理

基本思想是将所有内容从新集群复制到旧集群，除了我们知道是一样的块。  
1）扫描旧集群的WAL日志，从新集群的时间轴历史记录从旧集群分出的点之前的最后一个检查点开始。对于每个WAL记录，记下被触摸的数据块。这将产生一个列表，在新集群分支关闭后，旧集群中已更改的所有数据块的列表。  
2）将所有这些更改的块从新集群复制到旧集群。  
3）将所有其他文件（如clog，conf文件等）从新集群复制到旧集群。除关系文件外的所有内容。  
4）从在故障切换中创建的检查点开始，从新集群应用WAL。 （严格来说，pg\_rewind并不应用 WAL，它只是创建一个备份标签文件，指示当PostgreSQL启动时，它将从该检查点开始重播并应用所有所需的WAL）。

## 3、具体步骤：

1.激活备库（db2）: pg\_ctl promote  
2.将主库(db1)关闭，使用pg\_rewind工具增量同步原备库(db2)上的数据到原主库(db1):  
3.pg\_rewind –target-pgdata $PGDATA –source-server=’host=db2 port=5866 user=highgo dbname=highgo’ -P  
4.在db1上将recovery.done重命名为recovery.conf  
5.启动db1数据库pg\_ctl start

如果数据库版本为V6 及以上，recovery.conf被移除，这可以通过在目标数据目录中创建一个recovery.signal文件并且在postgresql.conf中配置适合的restore\_command来实现。

## 4、实验

①主端db1关闭数据库

```
pg_ctl stop -m f
```

②备端db2升为主库：

```
pg_ctl promote -D $PGDATA
```

③查看db2是否升为主端：

```
pg_controldata | grep cluster
Database cluster state:               in production
```

④在db2插入测试数据：

```
[highgo@hgdb1 ~]$ psql
highgo=#  create table test_2(id int4);
CREATE TABLE
highgo=# insert into test_2(id) select n from generate_series(1,10000) n;
INSERT 0 10000
```

⑤在db1上运行pg\_rewind

```
[highgo@hgdb1 ~]$ pg_rewind --target-pgdata $PGDATA --source-server='host=db2IP  port=5866 user=highgo dbname=highgo' -P

connected to server
servers diverged at WAL position 0/1060EC38 on timeline 3
rewinding from last common checkpoint at 0/1060EB90 on timeline 3
reading source file list
reading target file list
reading WAL in target
need to copy 228 MB (total source directory size is 246 MB)
233767/233767 kB (100%) copied
creating backup label and updating control file
syncing target data directory
Done
```

pg\_rewind 成功。

```
cd $PGDATA
mv recovery.done recovery.conf

[highgo@hgdb1 ~]$ cat recovery.conf
standby_mode = 'on'
primary_conninfo = 'user=highgo password=hg@123456 host=DB2IP  port=5866 sslmode=prefer sslcompression=1'
primary_slot_name = 'node_a_slot'
recovery_target_timeline = 'latest'

pg_ctl start
```

psql进入数据库：

```
highgo=# select count(*) from test_2;

 count

 10000
(1 row)
```

切换成功。
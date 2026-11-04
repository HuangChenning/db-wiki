---
title: "10、数据库data目录下存在大量core文件导致磁盘爆满"
book: "数据库使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/core.html"
tags:
  - highgo
  - highgo-v45
  - faq-database-usage
---

## 数据库data目录下存在大量core文件导致磁盘爆满

## 1、问题描述

hghac集群中某个数据库节点宕机，初步排查后发现磁盘爆满。继续排查发现数据库data目录下存在大量core文件，导致磁盘空间不足。

## 2、问题原因

```
[root@test-1 /]# /opt/HighGo/tools/hghac/hghactl  list
+ Cluster: test (6982441441117241376) -+--------------+----+-----------+
| Member |   Host         | Role    | State        | TL | Lag in MB |
+--------+-------------------+---------+--------------+----+-----------+
| test-0 | 192.168.10.1:5866 | Leader  | running      | 22 |           |
| test-1 | 192.168.10.2:5866 | Replica | start failed |    |   unknown |
| test-2 | 192.168.10.3:5866 | Replica | running      | 22 |       0.0 |
| test-3 | 192.168.10.4:5866 | Replica | start failed |    |   unknown |
+--------+-------------------+---------+--------------+----+-----------+
[root@test-1 /]# ps -ef |grep postgres |grep -v grep
[root@test-1 /]# cd  $PGDATA
[root@test-1 data]# ll
total 2085495568
-rw-------. 1 root root       3100 Jul  8 14:39 audit_param.conf
-rw-------. 1 root root        224 Jul  8 14:39 backup_label.old
drwx------. 6 root root       4096 Jul 14 17:40 base
-rw-------. 1 root root 8891727872 Jul 15 10:19 core.28081
-rw-------. 1 root root 8891727872 Jul 15 10:04 core.28122
-rw-------. 1 root root 8891858944 Jul 15 10:09 core.28124
…………
-rw-------. 1 root root 7112949760 Jul 15 11:10 core.30885
-rw-------. 1 root root 7116390400 Jul 15 11:10 core.30905
-rw-------. 1 root root 8891727872 Jul  8 17:46 core.32
-rw-------. 1 root root 8891727872 Jul  8 17:47 core.39
-rw-------. 1 root root         32 Jul 15 10:19 current_logfiles
drwx------. 2 root root       4096 Jul 15 09:03 global
drwx------. 4 root root       4096 Jul 12 09:02 hgaudit
drwx------. 2 root root       4096 Jul 15 00:00 hgdb_log
-rw-------. 1 root root       1094 Jul  8 14:39 patroni.dynamic.json
drwx------. 2 root root       4096 Jul  8 14:39 pg_commit_ts
drwx------. 2 root root       4096 Jul  8 14:39 pg_dynshmem
-rw-------. 1 root root        751 Jul 15 17:47 pg_hba.conf
-rw-------. 1 root root        751 Jul 15 11:10 pg_hba.conf.backup
-rw-------. 1 root root       1636 Jul  8 14:39 pg_ident.conf
-rw-------. 1 root root       1636 Jul 15 11:10 pg_ident.conf.backup
drwx------. 4 root root       4096 Jul 15 09:03 pg_logical
drwx------. 4 root root       4096 Jul  8 14:39 pg_multixact
drwx------. 2 root root       4096 Jul 15 10:19 pg_notify
drwx------. 2 root root       4096 Jul 12 09:02 pg_replslot
drwx------. 2 root root       4096 Jul  8 14:39 pg_serial
drwx------. 2 root root       4096 Jul  8 14:39 pg_snapshots
drwx------. 2 root root       4096 Jul 15 11:10 pg_stat
drwx------. 2 root root       4096 Jul 12 09:02 pg_stat_tmp
drwx------. 2 root root       4096 Jul  8 14:59 pg_subtrans
drwx------. 2 root root       4096 Jul  8 14:39 pg_tblspc
drwx------. 2 root root       4096 Jul  8 14:39 pg_twophase
-rw-------. 1 root root          3 Jul  8 14:39 PG_VERSION
drwx------. 3 root root      45056 Jul 15 09:03 pg_wal
drwx------. 2 root root       4096 Jul  8 14:39 pg_xact
-rw-------. 1 root root        113 Jul 14 17:54 postgresql.auto.conf
-rw-------. 1 root root      28596 Jul  8 14:39 postgresql.base.conf
-rw-------. 1 root root      28596 Jul 15 11:10 postgresql.base.conf.backup
-rw-r--r--. 1 root root       1967 Jul 15 17:47 postgresql.conf
-rw-r--r--. 1 root root       1967 Jul 15 11:10 postgresql.conf.backup
-rw-------. 1 root root        464 Jul 15 10:19 postmaster.opts
-rw-------. 1 root root         32 Jul  8 14:39 secure_param.conf
-rw-r--r--. 1 root root          0 Jul 15 17:47 standby.signal
[root@test-1 data]# df -h
Filesystem          Size  Used Avail Use% Mounted on
overlay             901G   20G  836G   3% /
tmpfs                64M     0   64M   0% /dev
tmpfs                32G     0   32G   0% /dev/shm
/dev/sda2           901G   20G  836G   3% /etc/hosts
/dev/mapper/mpathj  2.0T  2.0T     0 100% /opt/hgdb_data
/dev/sdb1          1008M  100M  858M  11% /boot
```

对core文件进行简单排查

```
[root@test-1 data]# file core.28122
core.28122: from 'cp pg_xlog/000000160000000500000049 /archive/000000160000000500000049'
```

由此推测，core文件由cp命令产生，该cp命令为归档参数 archieve\_command 配置。

仔细查看系统日志记录（/var/log/messages），发现系统出现过OOM（Out of Memory)事件。也就是说数据库使用了过量内存导致系统发出了kill命令，于是归档进程崩溃，导致产生了core文件。

## 3、解决方案

如果我们想阻止core文件的产生，可以设置core file的size limit为0。

```
# vi /etc/profile 
然后，在profile中添加：
ulimit -c 0  (KB)
# source /etc/profile
```

使用source命令使之马上生效。  
建议优先解决进程崩溃问题，再设置/etc/profile。
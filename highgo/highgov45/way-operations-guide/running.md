---
title: "5、查看正在在运行的瀚高数据库服务的启动方式：是由systemd(systemctl)启动的，还是由pg_ctl启动的"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/running.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## 查看正在在运行的瀚高数据库服务的启动方式：是由systemd(systemctl)启动的，还是由pg\_ctl启动的

## 1、问题描述

瀚高数据库在RHEL 7系列操作系统中的开机自动启动是用systemd来实现的，另外，瀚高数据库也有pg\_ctl 命令去启动、关闭、重启瀚高数据库服务。

那么，若是systemd拉起的瀚高数据库服务，由pg\_ctl去关闭、重启，这样的话，会导致systemd无法检测到瀚高数据库的状态，反之亦然。因此不推荐这两种方法交叉使用。

本文提供了一种方法，来查看正在运行的瀚高数据库服务的启动方式：是由systemd(systemctl)启动的，还是由pg\_ctl启动的。

注意，此问题不仅仅是瀚高数据库存在，Oracle数据库也存在本问题，请参见Oracle文章：  
Auto Startup/Shutdown Issue In RHEL 7.X Using Systemctl After Manually Shutdown/Start Database (Doc ID 2401600.1)

## 2、问题原因

本问题的原因是systemd固有的设计方式与实现机制。

## 3、解决方案

### （1）systemd(systemctl)启动瀚高数据库服务的证据

```
[root@dbserver 2017]# ps -ef |grep postg
root       2016      1  0 05:42 ?        00:00:00 /opt/HighGo4.3.4.7-see/bin/postgres -D /opt/HighGo4.3.4.7-see/data
root       2017   2016  0 05:42 ?        00:00:00 postgres: logger process  
root       2019   2016  0 05:42 ?        00:00:00 postgres: checkpointer process  
root       2020   2016  0 05:42 ?        00:00:00 postgres: writer process  
root       2021   2016  0 05:42 ?        00:00:00 postgres: wal writer process  
root       2022   2016  0 05:42 ?        00:00:00 postgres: autovacuum launcher process  
root       2023   2016  0 05:42 ?        00:00:00 postgres: archiver process  
root       2024   2016  0 05:42 ?        00:00:00 postgres: stats collector process  
root       2025   2016  0 05:42 ?        00:00:00 postgres: bgworker: logical replication launcher  
root       6039   2132  0 06:29 pts/0    00:00:00 grep --color=auto postg
[root@dbserver 2017]#
[root@dbserver 2017]#
[root@dbserver 2017]# systemctl status hgdb-see-4.3.4.7
● hgdb-see-4.3.4.7.service - hgdb-see-4.3.4.7
   Loaded: loaded (/usr/lib/systemd/system/hgdb-see-4.3.4.7.service; enabled; vendor preset: disabled)
   Active: active (running) since Sat 2020-02-29 05:42:02 EST; 50min ago
  Process: 2011 ExecStart=/opt/HighGo4.3.4.7-see/etc/hgdb-see-4.3.4.7 start (code=exited, status=0/SUCCESS)
  Process: 1171 ExecStartPre=/usr/bin/sleep 30 (code=exited, status=0/SUCCESS)
 Main PID: 2016 (postgres)
    Tasks: 9
   CGroup: /system.slice/hgdb-see-4.3.4.7.service             ----------------------->>>>本段输出中，CGroup及下面的输出是systemd启动瀚高数据库的证据
           ├─2016 /opt/HighGo4.3.4.7-see/bin/postgres -D /opt/HighGo4.3.4.7-see/data
           ├─2017 postgres: logger process  
           ├─2019 postgres: checkpointer process  
           ├─2020 postgres: writer process  
           ├─2021 postgres: wal writer process  
           ├─2022 postgres: autovacuum launcher process  
           ├─2023 postgres: archiver process  
           ├─2024 postgres: stats collector process  
           └─2025 postgres: bgworker: logical replication launcher  
Feb 29 05:41:31 dbserver systemd[1]: Starting hgdb-see-4.3.4.7...
Feb 29 05:42:01 dbserver hgdb-see-4.3.4.7[2011]: Starting HighGo Database Server:
Feb 29 05:42:02 dbserver hgdb-see-4.3.4.7[2011]: waiting for server to start.... done
Feb 29 05:42:02 dbserver hgdb-see-4.3.4.7[2011]: server started
Feb 29 05:42:02 dbserver hgdb-see-4.3.4.7[2011]: HighGo Database Server started successfully
Feb 29 05:42:02 dbserver systemd[1]: Started hgdb-see-4.3.4.7.
[root@dbserver 2017]#
[root@dbserver system.slice]# cd hgdb-see-4.3.4.7.service/
[root@dbserver hgdb-see-4.3.4.7.service]# ll
total 0
-rw-r--r-- 1 root root 0 Feb 29 05:41 cgroup.clone_children
--w--w--w- 1 root root 0 Feb 29 05:41 cgroup.event_control
-rw-r--r-- 1 root root 0 Feb 29 05:41 cgroup.procs
-rw-r--r-- 1 root root 0 Feb 29 05:41 notify_on_release
-rw-r--r-- 1 root root 0 Feb 29 05:41 tasks
[root@dbserver hgdb-see-4.3.4.7.service]# pwd
/sys/fs/cgroup/systemd/system.slice/hgdb-see-4.3.4.7.service
[root@dbserver hgdb-see-4.3.4.7.service]# cat cgroup.clone_children
0
[root@dbserver hgdb-see-4.3.4.7.service]# cat cgroup.event_control
cat: cgroup.event_control: Invalid argument
[root@dbserver hgdb-see-4.3.4.7.service]# cat cgroup.procs
2016
2017
2019
2020
2021
2022
2023
2024
2025
[root@dbserver hgdb-see-4.3.4.7.service]# cat notify_on_release
1
[root@dbserver hgdb-see-4.3.4.7.service]# cat tasks   -------->>>>这是systemd启动瀚高数据库的证据
2016
2017
2019
2020
2021
2022
2023
2024
2025
[root@dbserver hgdb-see-4.3.4.7.service]# pwd
/sys/fs/cgroup/systemd/system.slice/hgdb-see-4.3.4.7.service
[root@dbserver hgdb-see-4.3.4.7.service]#
[root@dbserver hgdb-see-4.3.4.7.service]# cd ..
[root@dbserver system.slice]# cd ..
[root@dbserver systemd]# ll
total 0
-rw-r--r--   1 root root 0 Feb 29 05:41 cgroup.clone_children
--w--w--w-   1 root root 0 Feb 29 05:41 cgroup.event_control
-rw-r--r--   1 root root 0 Feb 29 05:41 cgroup.procs
-r--r--r--   1 root root 0 Feb 29 05:41 cgroup.sane_behavior
-rw-r--r--   1 root root 0 Feb 29 05:41 notify_on_release
-rw-r--r--   1 root root 0 Feb 29 05:41 release_agent
drwxr-xr-x 101 root root 0 Feb 29 05:56 system.slice
-rw-r--r--   1 root root 0 Feb 29 05:41 tasks
drwxr-xr-x   4 root root 0 Feb 29 05:41 user.slice
[root@dbserver systemd]# cd user.slice/
[root@dbserver user.slice]# ll
total 0
-rw-r--r-- 1 root root 0 Feb 29 05:41 cgroup.clone_children
--w--w--w- 1 root root 0 Feb 29 05:41 cgroup.event_control
-rw-r--r-- 1 root root 0 Feb 29 05:41 cgroup.procs
-rw-r--r-- 1 root root 0 Feb 29 05:41 notify_on_release
-rw-r--r-- 1 root root 0 Feb 29 05:41 tasks
drwxr-xr-x 3 root root 0 Feb 29 06:40 user-0.slice
drwxr-xr-x 3 root root 0 Feb 29 05:41 user-42.slice
[root@dbserver user.slice]# cat cgroup.procs
[root@dbserver user.slice]# pwd
/sys/fs/cgroup/systemd/user.slice
[root@dbserver user.slice]#
[root@dbserver user.slice]# cat tasks
[root@dbserver user.slice]#
```

### （2）pg\_ctl启动瀚高数据库服务的证据

```
[root@dbserver session-1.scope]# ll
total 0
-rw-r--r-- 1 root root 0 Feb 29 07:25 cgroup.clone_children
--w--w--w- 1 root root 0 Feb 29 07:25 cgroup.event_control
-rw-r--r-- 1 root root 0 Feb 29 07:25 cgroup.procs
-rw-r--r-- 1 root root 0 Feb 29 07:25 notify_on_release
-rw-r--r-- 1 root root 0 Feb 29 07:25 tasks
[root@dbserver session-1.scope]# cat tasks ---->>>注意，本查询的输出是pg_ctl启动瀚高数据库的证据。
2087
2105
2232
2233
2235
2236
2237
2238
2239
2240
2241
2545
[root@dbserver session-1.scope]# pwd
/sys/fs/cgroup/systemd/user.slice/user-0.slice/session-1.scope
[root@dbserver session-1.scope]# ps -ef |grep postg
root       2232      1  0 07:26 pts/0    00:00:00 /opt/HighGo4.3.4.7-see/bin/postgres
root       2233   2232  0 07:26 ?        00:00:00 postgres: logger process  
root       2235   2232  0 07:26 ?        00:00:00 postgres: checkpointer process  
root       2236   2232  0 07:26 ?        00:00:00 postgres: writer process  
root       2237   2232  0 07:26 ?        00:00:00 postgres: wal writer process  
root       2238   2232  0 07:26 ?        00:00:00 postgres: autovacuum launcher process
root       2239   2232  0 07:26 ?        00:00:00 postgres: archiver process  
root       2240   2232  0 07:26 ?        00:00:00 postgres: stats collector process
root       2241   2232  0 07:26 ?        00:00:00 postgres: bgworker: logical replication launcher
root       4278   2105  0 07:50 pts/0    00:00:00 grep --color=auto postg
```
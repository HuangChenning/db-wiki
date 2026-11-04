---
title: "18、pg_resetwal 使用简介"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/pg_resetwal.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## pg\_resetwal 使用简介

pg\_resetwal会清除预写式日志（WAL）并且有选择地重置存储在pg\_control文件中的一些控制信息。如果控制文件已经被损坏，某些时候就需要 pg\_resetwal 挽救数据。

## 一、注意事项：

1.当服务器由于这样的损坏而无法启动并且无其他有效备份及归档可用时，才应该考虑使用 pg\_resetwal ，换句话说 pg\_resetwal只应该被用作最后的手段。

2.运行这个命令之后，就可能可以启动服务器，但是数据库可能包含由于部分提交事务产生的不一致数据。此时应当立刻转储所有的数据、执行initdb并且将数据重新导入到新初始化的数据库中。重新导入后，检查不一致并且根据需要修复数据。

3.只能被安装数据库的用户运行，因为它要求对数据目录的读写访问。出于安全考虑，必须在命令行中指定数据目录。pg\_resetwal不使用环境变量PGDATA。

4.这个命令不能在数据库服务正在运行时被使用。如果在数据目录中发现一个锁文件，pg\_resetwal将拒绝启动。如果数据库服务崩溃那么一个锁文件可能会被留下，在那种情况下你能移除该锁文件来让pg\_resetwal运行。但是在你那样做之前，应该再次确认没有数据库进程仍然存活。

5.pg\_resetwal 仅能在具有相同主版本的数据库上使用。

如果pg\_resetwal 提示它无法为 pg\_control 决定合法数据，你可以通过指定-f（强制）选项强制它继续。在这种情况下，丢失的数据将被替换为看似合理的值，可以期望大部分域是匹配的，但是下一个 OID、下一个事务 ID 、下一个多事务 ID 和偏移以及 WAL 开始位置域可能还是需要人工协助。这些域可以使用下面讨论的选项设置。

如果你不能为所有这些域决定正确的值，-f还是可以被使用，但是恢复的数据库中的数据不能保证是一致的，应该立即进行转储并导入到新初始化的数据库中。  
转储之前不要在该数据库中执行任何数据修改操作，因为任何这样的操作都可能使破坏更严重。

## 二、参数

pg\_resetwal \[ –force | -f \] \[ –dry-run | -n \] \[option…\] \[ –pgdata | -D \] datadir

\-f/–force

即使不能确定pg\_control的有效数据，也要强制pg\_resetwal进行。

\-n/–dry-run

pg\_resetwal打印从pg\_control中重建的值和即将改变的值，然后不做任何修改就退出。这主要是一个调试工具，允许 pg\_resetwal 真正执行之前做一个明智的检查。

\-V/–version

显示版本信息然后退出。

\-?/–help

显示帮助，然后退出。

只有当 pg\_resetwal 无法通过读取 pg\_control 确定合适的值时，才需要下列选项。安全值可以按下文所述来确定。对于接收数字参数的值，可以使用前缀0x指定 16 进制值。

\-c xid,xid/–commit-timestamp-ids=xid,xid。

手动设置可以获取提交时间的最老和最新的事务ID，可以通过查找数据目录下pg\_commit\_ts中数值最小的文件名来确定。  
最早可以检索到提交时间的事务ID的安全值（第一部分），可以通过在数据目录下的pg\_commit\_ts目录中查找数值最小的文件名来确定。反之，最新的事务ID的安全值（第二部分）可以通过在同一目录下查找数值最大的文件名来确定。文件名是十六进制的。

\-e xid\_epoch/–epoch=xid\_epoch

手动设置下一个事务ID的epoch。

除了在pg\_resetwal设置的字段中，事务ID的epoch实际上并不存储在数据库中的任何地方，所以就数据库本身而言，任何值都是有效的。你可能需要调整这个值，以确保诸如Slony-I和Skytools这样的下游复制系统能够正常工作–如果是这样的话，应该可以从下游复制的数据库的状态中获得一个合适的值。

\-l walfile/–next-wal-file=walfile。

通过指定下一个WAL段文件的名称，手动设置WAL的起始位置。

下一个WAL段文件的名称应该大于当前存在于数据目录下pg\_wal目录中的任何WAL段文件名称。这些名称也是十六进制的，有三部分组成。第一部分是 “时间轴ID”，通常应保持不变。例如，如果000001000000320000004A是pg\_wal中最大的条目，则使用-l 00000001000000320000004B或更高。

请注意，当使用非默认的WAL段大小时，WAL文件名中的数字与系统函数和系统视图报告的LSNs不同。此选项采用WAL文件名，而不是LSN。

note：该选项采用WAL文件名，而不是LSN。  
pg\_resetwal本身会查看pg\_wal中的文件，并在最后一个文件名之外选择一个默认的-l设置。因此，只有当你知道 WAL 段文件当前不在pg\_wal中时（例如只能通过离线归档中的日志来判断参数值），或者当pg\_wal的内容完全丢失时，才需要对-l进行手动调整。

\-m mxid,mxid/–multixact-ids=mxid,mxid。

手动设置下一个和最老的多事务ID。

下一个多事务 ID的安全值（第一部分）可以通过在数据目录下的 pg\_multixact/offsets 目录中查找数值最大的文件名，加1，然后乘以65536 (0x10000)来确定。相应的，可以通过在同一目录下寻找数值最小的文件名，然后乘以65536来确定最老的多事务ID（-m的第二部分）的安全值。文件名是以十六进制为单位的，所以最简单的方法是用十六进制指定选项值，并附加四个零。

\-o oid/–next-oid=oid

手动设置下一个OID。

没有比较简单的方法来确定超越数据库中最大的下一个OID，但幸运的是，是否正确的设置下一个OID并不关键。

\-O mxoff/–multixact-offset=mxoff

手动设置下一个多事务偏移量。

可以通过在数据目录下的 pg\_multixact/members 目录中查找数值最大的文件名，加一，然后乘以52352 (0xCC80)来确定安全值。文件名是十六进制的。没有简单的办法，如其他选项的追加零的方式。

–wal-segsize=wal\_segment\_size。

设置新的WAL段的大小，以兆字节为单位。该值必须设置为2的1次幂和1024次幂（兆字节）之间。

note：在这个选项中，我们必须设置新的WAL段大小，单位是兆字节。  
虽然pg\_resetwal将把WAL起始地址设置成超过最新的现有WAL段文件，但一些段尺寸的改变可能导致之前的WAL文件名被重用。如果WAL文件名重叠会导致归档策略出现问题，推荐把-l和这个选项一起使用来手动设置WAL起始地址。

\-x xid/–next-transaction-id=xid

手工设置下一个事务 ID。

确定安全值的方法：在数据目录下的 pg\_xact 目录中查找最大的数字文件名，然后在它的基础上加一并且乘以 1048576 (0x100000)。注意文件名是十六进制的数字。通常以十六进制的形式指定该选项值也是最容易的。例如，如果0011是pg\_xact中的最大项，-x 0x1200000就可以（五个尾部的零就表示了前面说的乘数）。

## 三、示例

下面展示一个重新控制文件的示例来帮你理解整个恢复过程。

### 1、插入测试数据

```
[highgo@localhost global]$ psql
psql (5.6.4)

PSQL: Release 5.6.4
Connected to:
HighGo Database V5.6 Enterprise Edition Release 5.6.4 - 64-bit Production

Type "help" for help.

highgo=# create table oid_test(id int primary key) with oids;
CREATE TABLE
highgo=# insert into oid_test select generate_series(1,100000);
INSERT 0 100000
highgo=# select min(oid),max(oid) from oid_test ;
  min  |  max  
-------+--------
 24659 | 124658
(1 row)

highgo=# select min(oid),max(oid) from oid_test ;
  min  |  max  
-------+--------
 24659 | 124658
(1 row)

highgo=# \q
[highgo@localhost global]$ pg_ctl stop -m fast
waiting for server to shut down.... done
server stopped
```

### 2、查看控制文件信息

```
[highgo@localhost global]$ pg_controldata
pg_control version number:            1002
Catalog version number:               201707211
Database system identifier:           6837282431617040045
Database cluster state:               shut down
pg_control last modified:             Thu Aug 13 09:40:40 2020
Latest checkpoint location:           0/CF125A0
Prior checkpoint location:            0/C1BB3B8
Latest checkpoint's REDO location:    0/CF125A0
Latest checkpoint's REDO WAL file:    00000004000000000000000C
Latest checkpoint's TimeLineID:       4
Latest checkpoint's PrevTimeLineID:   4
Latest checkpoint's full_page_writes: on
Latest checkpoint's NextXID:          0:1031
Latest checkpoint's NextOID:          124659
Latest checkpoint's NextMultiXactId:  1
Latest checkpoint's NextMultiOffset:  0
Latest checkpoint's oldestXID:        553
Latest checkpoint's oldestXID's DB:   1
Latest checkpoint's oldestActiveXID:  0
Latest checkpoint's oldestMultiXid:   1
Latest checkpoint's oldestMulti's DB: 1
Latest checkpoint's oldestCommitTsXid:0
Latest checkpoint's newestCommitTsXid:0
Time of latest checkpoint:            Thu Aug 13 09:40:40 2020
Fake LSN counter for unlogged rels:   0/1
Minimum recovery ending location:     0/0
Min recovery ending loc's timeline:   0
Backup start location:                0/0
Backup end location:                  0/0
End-of-backup record required:        no
wal_level setting:                    replica
wal_log_hints setting:                off
max_connections setting:              2000
max_worker_processes setting:         10
max_prepared_xacts setting:           0
max_locks_per_xact setting:           64
track_commit_timestamp setting:       off
Maximum data alignment:               8
Database block size:                  8192
Blocks per segment of large relation: 131072
WAL block size:                       8192
Bytes per WAL segment:                16777216
Maximum length of identifiers:        64
Maximum columns in an index:          32
Maximum size of a TOAST chunk:        1996
Size of a large-object chunk:         2048
Date/time type storage:               64-bit integers
Float4 argument passing:              by value
Float8 argument passing:              by value
Data page checksum version:           0
Data encryption:                      off
Mock authentication nonce:            b59d43a6c226cf8a82f7bb6865bb7cc95d6d078cb4177fd60e9a38d1707d30ec
```

### 3、模拟控制文件丢失：

```
[highgo@localhost global]$ rm $PGDATA/global/pg_control

[highgo@localhost global]$ cd $PGDATA/pg_wal
[highgo@localhost pg_wal]$ ll
total 180244
-rw------- 1 highgo highgo      309 Jun 19 09:45 000000010000000000000003.00000060.backup
-rw------- 1 highgo highgo       41 Jun 19 09:45 00000002.history
-rw------- 1 highgo highgo       41 Jun 19 09:45 00000003.history
-rw------- 1 highgo highgo       83 Jun 19 09:45 00000004.history
-rw------- 1 highgo highgo 16777216 Aug 13 09:40 00000004000000000000000C
-rw------- 1 highgo highgo 16777216 Jun 19 09:45 00000004000000000000000D
-rw------- 1 highgo highgo 16777216 Jun 19 09:45 00000004000000000000000E
-rw------- 1 highgo highgo 16777216 Jun 19 09:45 00000004000000000000000F
-rw------- 1 highgo highgo 16777216 Jun 19 09:45 000000040000000000000010
-rw------- 1 highgo highgo 16777216 Jun 19 09:45 000000040000000000000011
-rw------- 1 highgo highgo 16777216 Jun 19 09:45 000000040000000000000012
-rw------- 1 highgo highgo 16777216 Jun 19 09:45 000000040000000000000013
-rw------- 1 highgo highgo 16777216 Jun 19 09:45 000000040000000000000014
-rw------- 1 highgo highgo 16777216 Jun 19 09:45 000000040000000000000015
-rw------- 1 highgo highgo 16777216 Jun 19 09:45 000000040000000000000016
-rw------- 1 highgo highgo       41 Jun 19 09:45 RECOVERYHISTORY
drwx------ 2 highgo highgo      146 Aug 12 16:06 archive_status
```

–查看-l选项的参数值，pg\_wal目录下存在的最新的wal文件名为 000000040000000000000016 ，使用000000040000000000000017 即可。

```
[highgo@localhost pg_wal]$ ll $PGDATA/pg_xact/
-rw------- 1 highgo highgo 8192 Aug 13 09:40 0000
```

–查看-x选项的参数值,pg\_xact 目录下的文件名为0000，使用 0x100000 即可

```
[highgo@localhost pg_wal]$ cd $PGDATA/pg_multixact/offsets
[highgo@localhost offsets]$ ll
total 8
-rw------- 1 highgo highgo 8192 Aug 13 09:40 0000
```

–查看-m选项的参数值，pg\_multixact/offsets 目录下的文件名为0000，使用 0x10000 即可

```
[highgo@zx members]$ ll $PGDATA/pg_multixact/members
total 8
-rw------- 1 highgo highgo 8192 Jun 19 09:45 0000
```

–查看-O选项的参数值，pg\_multixact/members 目录下的文件名为0000,文件名换算后可得参数值为 0xCC80

### 4、做一次检查测试：

```
[highgo@zx global]$ pg_resetwal -l 000000040000000000000017 -x 0x100000  -m 0x10000,0x10000 -O 0xCC80  -n -f $PGDATA
```

### 5、正式重建控制文件：

```
[highgo@localhost data]$ pg_resetwal -l 000000040000000000000017 -x 0x100000  -m 0x10000,0x10000 -O 0xCC80 -f $PGDATA
pg_resetwal: pg_control exists but is broken or wrong version; ignoring it
Write-ahead log reset
[highgo@localhost data]$ ll global/pg_control
-rw------- 1 highgo highgo 8192 Aug 13 10:06 global/pg_control
[highgo@localhost data]$ pg_controldata
pg_control version number:            1002
Catalog version number:               201707211
Database system identifier:           6860284186546668097
Database cluster state:               shut down
pg_control last modified:             Thu Aug 13 10:06:22 2020
Latest checkpoint location:           0/17000028
Prior checkpoint location:            0/0
Latest checkpoint's REDO location:    0/17000028
Latest checkpoint's REDO WAL file:    000000040000000000000017
Latest checkpoint's TimeLineID:       4
Latest checkpoint's PrevTimeLineID:   4
Latest checkpoint's full_page_writes: off
Latest checkpoint's NextXID:          0:1048576
Latest checkpoint's NextOID:          10000
Latest checkpoint's NextMultiXactId:  65536
Latest checkpoint's NextMultiOffset:  52352
Latest checkpoint's oldestXID:        2296015872
Latest checkpoint's oldestXID's DB:   0
Latest checkpoint's oldestActiveXID:  0
Latest checkpoint's oldestMultiXid:   65536
Latest checkpoint's oldestMulti's DB: 0
Latest checkpoint's oldestCommitTsXid:0
Latest checkpoint's newestCommitTsXid:0
Time of latest checkpoint:            Thu Aug 13 10:06:22 2020
Fake LSN counter for unlogged rels:   0/1
Minimum recovery ending location:     0/0
Min recovery ending loc's timeline:   0
Backup start location:                0/0
Backup end location:                  0/0
End-of-backup record required:        no
wal_level setting:                    minimal
wal_log_hints setting:                off
max_connections setting:              100
max_worker_processes setting:         8
max_prepared_xacts setting:           0
max_locks_per_xact setting:           64
track_commit_timestamp setting:       off
Maximum data alignment:               8
Database block size:                  8192
Blocks per segment of large relation: 131072
WAL block size:                       8192
Bytes per WAL segment:                16777216
Maximum length of identifiers:        64
Maximum columns in an index:          32
Maximum size of a TOAST chunk:        1996
Size of a large-object chunk:         2048
Date/time type storage:               64-bit integers
Float4 argument passing:              by value
Float8 argument passing:              by value
Data page checksum version:           0
Data encryption:                      off
Mock authentication nonce:            0000000000000000000000000000000000000000000000000000000000000000
```

### 6、启动数据库检查数据：

```
[highgo@localhost data]$ pg_ctl start
waiting for server to start....2020-08-13 10:09:40.177 CSTWARNING:  01000: gdb version should large than 7.10
2020-08-13 10:09:40.177 CSTWARNING:  01000: coredump function is off
2020-08-13 10:09:40.193 CSTLOG:  00000: listening on IPv4 address "0.0.0.0", port 5868
2020-08-13 10:09:40.193 CSTLOG:  00000: listening on IPv6 address "::", port 5868
2020-08-13 10:09:40.207 CSTLOG:  00000: listening on Unix socket "/tmp/.s.PGSQL.5868"
2020-08-13 10:09:40.347 CSTLOG:  00000: redirecting log output to logging collector process
2020-08-13 10:09:40.347 CSTHINT:  Future log output will appear in directory "hgdb_log".
 done
server started
[highgo@localhost data]$
[highgo@localhost data]$
[highgo@localhost data]$ psql
psql (5.6.4)

PSQL: Release 5.6.4
Connected to:
HighGo Database V5.6 Enterprise Edition Release 5.6.4 - 64-bit Production

Type "help" for help.

highgo=# \d
                 List of relations
 Schema |           Name           | Type  | Owner 
--------+--------------------------+-------+--------
 public | oid_test                 | table | highgo
 public | pg_stat_statements       | view  | highgo
 public | pg_wait_sampling_current | view  | highgo
 public | pg_wait_sampling_history | view  | highgo
 public | pg_wait_sampling_profile | view  | highgo
 public | t1                       | table | highgo
(6 rows)

highgo=# select min(oid),max(oid) from oid_test ;
  min  |  max  
-------+--------
 24659 | 124658
(1 row)

highgo=# \q
[highgo@localhost data]$ pg_ctl stop -m f
waiting for server to shut down.... done
server stopped
[highgo@localhost data]$ pg_controldata      
pg_control version number:            1002
Catalog version number:               201707211
Database system identifier:           6860284186546668097
Database cluster state:               shut down
pg_control last modified:             Thu Aug 13 10:11:48 2020
Latest checkpoint location:           0/17D48240
Prior checkpoint location:            0/17000028
Latest checkpoint's REDO location:    0/17D48240
Latest checkpoint's REDO WAL file:    000000040000000000000017
Latest checkpoint's TimeLineID:       4
Latest checkpoint's PrevTimeLineID:   4
Latest checkpoint's full_page_writes: on
Latest checkpoint's NextXID:          0:1048579
Latest checkpoint's NextOID:          116384
Latest checkpoint's NextMultiXactId:  65536
Latest checkpoint's NextMultiOffset:  52352
Latest checkpoint's oldestXID:        553
Latest checkpoint's oldestXID's DB:   13864
Latest checkpoint's oldestActiveXID:  0
Latest checkpoint's oldestMultiXid:   1
Latest checkpoint's oldestMulti's DB: 13864
Latest checkpoint's oldestCommitTsXid:0
Latest checkpoint's newestCommitTsXid:0
Time of latest checkpoint:            Thu Aug 13 10:11:47 2020
Fake LSN counter for unlogged rels:   0/1
Minimum recovery ending location:     0/0
Min recovery ending loc's timeline:   0
Backup start location:                0/0
Backup end location:                  0/0
End-of-backup record required:        no
wal_level setting:                    replica
wal_log_hints setting:                off
max_connections setting:              2000
max_worker_processes setting:         10
max_prepared_xacts setting:           0
max_locks_per_xact setting:           64
track_commit_timestamp setting:       off
Maximum data alignment:               8
Database block size:                  8192
Blocks per segment of large relation: 131072
WAL block size:                       8192
Bytes per WAL segment:                16777216
Maximum length of identifiers:        64
Maximum columns in an index:          32
Maximum size of a TOAST chunk:        1996
Size of a large-object chunk:         2048
Date/time type storage:               64-bit integers
Float4 argument passing:              by value
Float8 argument passing:              by value
Data page checksum version:           0
Data encryption:                      off
Mock authentication nonce:            0000000000000000000000000000000000000000000000000000000000000000
[highgo@localhost data]$
```

–到此为止，应当立刻转储所有的数据，执行initdb并且将数据重新导入到新初始化的数据库中。重新导入后，检查数据不一致并且根据需要修复数据。

注意：数据库启动时，无法正常执行 pg\_resetwal 命令。

```
[highgo@localhost offsets]$  pg_resetwal -l 000000040000000000000017 -x 0x100000  -m 0x10000,0x10000 -O 0xCC80 -f $PGDATA
pg_resetwal: lock file "postmaster.pid" exists
Is a server running?  If not, delete the lock file and try again.
[highgo@localhost ~]$ cd $PGDATA
[highgo@localhost data]$ ll *.pid
-rw------- 1 highgo highgo      74 Aug 13 09:41 postmaster.pid
```

### 7、执行以下操作前请确认已经不存在数据库进程。

```
[highgo@localhost data]$ mv  postmaster.pid postmaster.pid.bak
```
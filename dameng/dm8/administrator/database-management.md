---
title: "数据库布局和存储管理"
book: "DM8 系统管理员手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/database-management.html
tags:
  - dameng
  - dm8
  - administrator
---

规划数据库结构时需要考虑如何管理数据库中的相关文件，每个表空间存储什么数据，在表空间中创建几个多大的数据文件，以及数据文件存储的位置等。本章介绍了表空间的管理、数据文件的管理、重做日志文件的管理、回滚空间的管理和控制文件的管理。

## 14.1 管理表空间

表空间的管理操作需要 DM 服务器处于打开状态下。

### 14.1.1 创建表空间

创建表空间时需要指定表空间名和其拥有的数据文件列表。比如创建名为 bookshop 的表空间，并指定该空间上拥有 2 个数据文件，每个数据文件的大小为 128MB。

```
CREATE TABLESPACE bookshop DATAFILE 'd:\bookshop1.dbf' SIZE 128, 'd:\bookshop2.dbf' SIZE 128;
```

理论上最多允许有 65535 个表空间，但用户允许创建的表空间 ID 取值范围为 0~32767，超过 32767 的只允许系统使用，ID 由系统自动分配，ID 不能重复使用，即使删除掉已有表空间，也无法重复使用已用 ID 号，也就是说只要创建 32768 次表空间后，用户将无法再创建表空间。

### 14.1.2 扩展表空间

表空间通过数据文件来扩展，表空间的大小等于构成该表空间的所有数据文件的大小之和。所以要扩展表空间可以通过添加新的数据文件或者扩展表空间中已有的数据文件完成。数据文件的添加和扩展可见下一节。

### 14.1.3 删除表空间

只可以删除用户创建的表空间并且只能删除未使用过的表空间。删除表空间时会删除其拥有的所有数据文件。例如删除 bookshop 表空间。

```
DROP TABLESPACE bookshop;
```

### 14.1.4 修改表空间名

可修改已存在的由用户创建的表空间的名称。比如可修改 bookshop 表空间名为 books。

```
ALTER TABLESPACE bookshop RENAME TO books;
```

### 14.1.5 修改表空间状态

用户表空间有联机和脱机两种状态。系统（SYSTEM）表空间、回滚（ROLL）表空间、日志表空间（RLOG）和临时（TEMP）表空间不允许脱机。设置表空间状态为脱机状态时，如果该表空间有未提交的事务，则脱机失败报错。脱机后可对表空间的数据进行备份。

例 1 修改 bookshop 表空间状态为脱机

```
ALTER TABLESPACE bookshop OFFLINE;
```

例 2 修改 bookshop 表空间状态为联机

```
ALTER TABLESPACE bookshop ONLINE;
```

注意：DM MPP 环境下，可能发现节点间的表空间不一致情况，例如：EP01 为 ONLINE 状态，EP02 为 OFFLINE 状态，这个时候，无论执行 ONLINE 还是 OFFLINE 都是报错。需要用户介入，才可以解决问题。用户 LOCAL 方式登录实例，并执行 SP\_SET\_SESSION\_LOCAL\_TYPE(1)，使得该会话可以执行 DDL 操作，再执行 ONLINE 或者 OFFLINE 即可。

### 14.1.6 查询表空间与数据文件对应关系

可以通过查询动态视图 V$TABLESPACE 得到系统中除 RLOG 表空间外其他所有表空间的信息，通过查询动态视图 V$DATAFILE 得到系统中除 RLOG 表空间外所有数据文件的信息。将两个动态视图以表空间 ID 为连接条件，通过以下查询可以得到表空间上对应的数据文件。

```
SELECT ts.NAME, df.PATH FROM V$TABLESPACE ts, V$DATAFILE AS df WHERE ts.ID = df.GROUP_ID;
```

### 14.1.7 表空间文件失效检查

LINUX 操作系统中，被进程打开的文件仍可以在 OS 系统中被删除，因此存在 DM 数据文件可能被误删的风险。如果数据文件被删除，DM 系统能够及时检测出来，并立刻停止对其继续使用并通知用户。

在 dm.ini 中参数 FIL\_CHECK\_INTERVAL 的值指定 DM 系统检查数据文件是否仍存在的时间间隔。将其设为 0 表示不进行检查。

也可以通过系统过程 SP\_FILE\_SYS\_CHECK()来手动的进行检查。

系统一旦检测出某个表空间内的数据文件被删除，则与该表空间所有的操作都将会失败，并报错该表空间内有数据文件被删除。

### 14.1.8 表空间失效文件恢复

LINUX 系统中被删除的文件，只要其句柄没有被关闭，可以在/proc/\<pid>/fd 中找到其对应的文件副本。其中\<pid>指打开该文件的进程 id。

利用该方法，结合 OS 命令，DM 提供失效文件的恢复方案如下：

1. 调用系统过程 SP\_TABLESPACE\_PREPARE\_RECOVER(表空间名称)准备进行恢复；
2. 如果使用过程中 DM 报错表空间数据文件被删除，通过操作系统的 ps 命令找到当前 DMServer 的 PID：ps -ef|grep dmserver；
3. 使用操作系统 ll 命令查看被删除文件对应的副本：ll /proc/ *< *PID* >* /fd，会发现被删除的文件后有(deleted)字样；
4. 使用操作系统的 cp 命令将文件复制到原位置：cp 源路径 目的路径；
5. 复制成功后，调用系统过程 SP\_TABLESPACE\_RECOVER(表空间名称)完成表空间失效文件的恢复。

注意，要保证数据文件正确修复，需要保证在 SP\_TABLESPACE\_PREPARE\_RECOVER 后进行数据文件的复制。

## 14.2 管理数据文件

管理数据文件的操作需要 DM 服务器处于打开状态下。其中，移动数据文件的操作在 DM 服务器处于打开或配置状态下都可以进行。

### 14.2.1 添加数据文件

可以在用户表空间中添加数据文件。添加的数据文件大小最小为 4096\*页大小，如页大小为 8KB，则可添加的文件最小值为 4096\*8kB=32MB。比如在 bookshop 表空间中添加大小为 64M 的数据文件。

```
ALTER TABLESPACE bookshop ADD DATAFILE 'd:\book.dbf' SIZE 64;
```

一个表空间中，数据文件和镜像文件的个数一起不能超过 INI 参数 TS\_FIL\_MAX\_ID 设置的值。例如，如果创建表空间的时候已经指定了 1 个数据文件，那么添加数据文件的时候，最多只能添加 TS\_FIL\_MAX\_ID-1 个文件了。

### 14.2.2 删除数据文件

可以删除用户表空间中的数据文件。比如删除 bookshop 表空间中的一个名为 book.dbf 的数据文件。

```
ALTER TABLESPACE bookshop DROP DATAFILE 'd:\book.dbf';
```

删除表空间中数据文件时必须遵守文件 ID 从大到小的原则。先从具有最大文件 ID 的数据文件开始，且表空间中文件 ID 为零的数据文件不能被删除。

### 14.2.3 扩展数据文件的大小

可以扩展用户表空间中已存在的数据文件的大小。比如扩展 bookshop 表空间中数据文件 book.dbf 大小至 128MB。

```
ALTER TABLESPACE bookshop RESIZE DATAFILE 'd:\book.dbf' TO 128;
```

### 14.2.4 缩减数据文件的大小

可以缩减用户表空间中已存在的数据文件的大小。比如将 bookshop 表空间中数据文件 book.dbf 大小缩减至 32M。

```
ALTER TABLESPACE bookshop RESIZE DATAFILE 'd:\book.dbf' TO 32;
```

### 14.2.5 指定数据文件的扩展属性

可以指定数据文件是否可以扩展，每次扩展的空间大小以及数据文件可扩展到的最大空间大小，子句的语法为：

```
AUTOEXTEND OFF|ON [NEXT <文件扩展大小>] [MAXSIZE <文件限制大小>]
```

OFF 表示文件不可扩展，ON 表示文件可扩展。文件扩展大小表示当需要扩展文件时，文件一次增大的空间大小，取值范围是 1~2048，单位是 MB。实际的文件扩展大小由指定的值与 INI 参数 TS\_AUTO\_EXTEND\_SIZE 共同决定，为大于等于 TS\_AUTO\_EXTEND\_SIZE 且是指定的文件扩展大小的整数倍的值。若未指定文件扩展大小，则扩展大小默认为 INI 参数 TS\_AUTO\_EXTEND\_SIZE 所指定的大小，后续不随该 INI 参数的变化而动态调整。另外，TEMP 表空间文件在 V$DATAFILE 中显示的扩展大小始终为 0，但其实际扩展大小由 INI 参数 TS\_AUTO\_EXTEND\_SIZE 控制，会随着该参数值的变化而自动调整；使用 V8.1.5.13 之前的版本创建的扩展大小为 0 的表空间文件在 V$DATAFILE 中显示的扩展大小为 0 时，其实际扩展大小由 INI 参数 TS\_AUTO\_EXTEND\_SIZE 控制，会随着该参数值的变化而自动调整。

文件限制大小表示文件可扩展的最大空间大小，为 0 或者 UNLIMITED 表示无限制，单位是 MB，缺省为无限制。

创建表空间时可指定文件的扩展属性。如创建表空间时指定数据文件的扩展属性为可自动扩展，每次扩展大小为 10MB，最大可扩展到 100MB：

```
CREATE TABLESPACE bookshop DATAFILE 'd:\book.dbf' SIZE 32 AUTOEXTEND ON NEXT 10 MAXSIZE 100;
```

在表空间中添加文件时可指定文件的扩展属性。如添加数据文件时指定扩展属性为不可自动扩展：

```
ALTER TABLESPACE bookshop ADD DATAFILE 'd:\book.dbf' SIZE 1024 AUTOEXTEND OFF;
```

可修改表空间中已存在的数据文件的扩展属性。如修改数据文件的扩展属性为可自动扩展：

```
ALTER TABLESPACE bookshop DATAFILE 'd:\book.dbf' ;
```

### 14.2.6 修改数据文件的路径

可以修改用户表空间中已存在数据文件的路径，待修改的数据文件所在表空间必须处于脱机状态并且只可修改用户创建的表空间中文件的路径。如修改 bookshop 表空间中文件 book.dbf 的路径为 e:\\ book.dbf。

```
ALTER TABLESPACE bookshop RENAME DATAFILE 'd:\book.dbf' TO 'e:\book.dbf';
```

### 14.2.7 添加 HUGE 数据文件路径

可以为普通表空间添加 HUGE 数据文件路径将其升级为混合表空间，也可以为混合表空间添加 HUGE 数据文件路径，一个混合表空间最多可以添加 127 个 HUGE 数据文件路径。如为普通表空间 bookshop 添加 HUGE 数据文件路径 e:\\HUGE，将 bookshop 升级为混合表空间。

```
ALTER TABLESPACE bookshop ADD HUGE PATH 'e:\HUGE';
```

## 14.3 管理重做日志文件

### 14.3.1 添加重做日志文件

在服务器打开状态下，可以添加新的重做日志文件。在 32 位版本下，文件大小的范围是 256 和 2048 之间的整数，单位 MB；在 64 位版本下，文件大小的范围是 256 和 8192 之间的整数，单位 MB。如添加重做大小为 256MB 的重做日志文件 DAMENG03.log。

```
ALTER DATABASE ADD LOGFILE 'd:\DAMENG03.log' size 256;
```

### 14.3.2 扩展重做日志文件

在服务器打开状态下，可以扩展已有的重做日志文件的大小。如扩展重做日志文件 DAMENG03.log 到 300M。

```
ALTER DATABASE RESIZE LOGFILE 'd:\DAMENG03.log' to 300;
```

### 14.3.3 删除重做日志文件

在服务器打开状态下，可以删除已有的重做日志文件。如删除重做日志文件 DAMENG03.log。

```
ALTER DATABASE DROP LOGFILE 'd:\DAMENG03.log';
```

在删除重做日志文件时，指定的文件需要满足以下的一些条件才能够成功删除：

1. 指定文件必须是当前节点自身的重做日志文件。
2. 指定文件不是当前正在写的重做日志文件，并且该文件上不存在有效的重做日志。
3. 指定文件必须是 RLOG 表空间中 FILE\_ID 最大的那个文件。
4. 指定文件不能是 0 号或 1 号重做日志文件。
5. 指定文件删除前后的日志空间都应该是安全的。即当前已使用的日志空间不应该超过 RLOG\_RESERVE\_THRESHOLD，并且删除该文件不会导致剩余日志空间过小。

## 14.4 管理回滚表空间

回滚表空间的管理和用户表空间的管理基本是一样的，区别是回滚表空间的空间名固定为 ROLL，不可修改。可增加、扩展和缩减回滚空间中的回滚文件，设置回滚空间的扩展属性，相关操作可参考\[14.2 管理数据文件\](#14.2 管理数据文件)中的说明。需要注意的是，回滚表空间文件的缩减操作比较特殊。由于执行缩减语句的事务本身需要分配新的回滚页，而每个用户会话的事务所新分配出的回滚页，其页号分布是不相同的。因此，当指定的目标缩减偏移量较小时，即使不存在其他已使用且未释放的回滚页，也无法保证能够一次性缩减成功，这种情况下可以通过开启多个会话反复尝试。

回滚文件的路径记录在控制文件里面，可以使用 dmctlcvt 工具在 DM 服务器关闭的状态下对控制文件进行修改。使用 dmctlcvt 工具将控制文件转换为文本文件，编辑文本文件中要修改的文件的路径后再使用 dmctlcvt 工具将文本文件转换为控制文件即可。

首先转换控制文件到文本文件：

```
dmctlcvt type=1 src=D:\dm.ctl  dest=D:\ctl.txt
```

编辑 ctl.txt 文本文件中 fil\_path=d:\\roll.dbf 为 fil\_path=e:\\roll.dbf，保存文本文件。复制 d:\\roll.dbf 文件为 e:\\roll.dbf。

最后转换文本文件到控制文件：

```
dmctlcvt type=2 src= D:\ctl.txt  dest= D:\dm.ctl
```

这种修改文件路径的方法也可用于重做日志文件，SYSTEM 表空间文件等路径的修改。

## 14.5 管理控制文件

可以在 dm.ini 中通过设置 CTL\_PATH 配置参数的值来指定控制文件的路径，缺省控制文件在数据目录下。例如可以把控制文件复制到 D 盘的 control\_path 目录下，同时修改 dm.ini 中 CTL\_PATH = D:\\control\_path\\dm.ctl。
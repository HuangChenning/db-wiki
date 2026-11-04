---
title: "DMDPC使用须知"
book: "DM8 分布计算集群"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dpc-terms-use.html
tags:
  - dameng
  - dm8
  - dpc
---

## 4.1 软硬件环境

部署 DMDPC 集群所用到的硬件和软件环境。

- **硬件环境**
	- 主机一台或多台。用于部署 MP、SP 和 BP。内存大小要求：至少 2GB。测试环境中可以将上述服务部署到同一主机，生产环境下推荐每个主机只部署一种类型服务器。
- **软件环境**
	- 操作系统。Linux、Unix、Windows 等。
		- 达梦数据库软件。安装好 DM 数据库软件之后，将拥有配置和管理 DMDPC 所需的所有软件：dmserver、dminit、DIsql 等。这些软件位于安装目录的 bin、tool 等子目录中。

## 4.2 系统规范

在 DMDPC 系统中，有如下规范及约束：

1. 集群中 SP、BP、MP 都有自己的实例名，这些实例名要求全局唯一；
2. 一个 DMDPC 集群可以有多个 SP 和多个 BP，但只能有一个 MP；
3. DMDPC 中数据的分布以分区为单位，同一分区必须位于同一 BP，同一表的不同分区可以位于不同 BP，一张分区表的所有分区可以只落在部分 BP；非分区表只包含一个分区，因此非分区表只落在一个 BP 上。分区表包含一个或多个分区，因此分区表可以落在一个或多个 BP 上；DMDPC 下，分区列同时也是分布列；
4. 在 DMDPC 中分区和分布统一为一个概念；在 DM MPP 中，分区和分布是两个不同的概念；
5. 实例在初始化时需指定 DPC\_MODE 以决定其角色（SP、BP 或 MP），随后启动时需要附带上 DPC\_MODE 参数。实例角色在初始化后不能更改。

## 4.3 功能限制

和达梦单机实例、DM MPP 等架构相比，DMDPC 在部分数据库功能上存在使用限制，本章节将对这些功能限制进行详细说明。

### 4.3.1 表限制

DMDPC 对于表存在以下使用限制：

1. 不支持外部表。并且由于 DMDPC 不支持外部表，所以下面三个专门修改外部表的操作均不支持：
```
<修改表定义子句> ::=
MODIFY PATH <外部表文件路径> |
DEFAULT DIRECTORY <目录名>|
LOCATION ('<文件名>')
```
2. 不支持涉及临时表、V$ARCHIVED\_LOG、V$LOGMNR\_LOGS、V$LOGMNR\_CONTENTS、V$LOGMNR\_PARAMETERS、V$LOGMNR\_DICTIONARY 的查询建表；
3. 非本地登录时，不支持临时表的 DML 操作回滚；
4. 不支持堆表的全局索引；
5. 不支持建表语句中使用的 < 空间限制子句 >。若建表时指定了 < 空间限制子句 >，则既不报错，也不生效；
6. 不支持有 DPC 全局索引的分区表 truncate 子表；
7. 不支持高级日志表 advanced log；
8. 不支持修改 HUGE 表的操作：WITH DELTA 和 HUGE 表跨节点交换分区 EXCHANGE PARTITION；
9. HUGE 表加列时不支持以序列作为默认值；
10. DMDPC 仅支持多级分区中的二级分区。二级分区中的分区组合方式和单机一样，主表和子表的总个数也不能超过 65535；
11. 不支持包含大字段或使用 USING LONG ROW 存储选项的表使用半透明加密；
12. 不支持临时表上创建物化视图；
13. 不支持修改水平分区表的操作：
```
<修改表定义子句> ::=
EXCHANGE < SUBPARTITION > <分区名> WITH TABLE [<模式名.>]<表名>|
MOVE SUBPARTITION <子分区名> TABLESPACE <表空间名>
```

### 4.3.2 约束限制

DMDPC 对于约束存在以下使用限制：

1. 不支持虚拟列上的非空约束；
2. 不支持 DOMAIN 的 CHECK 约束；
3. 引用约束必须包含分布列，即引用表中的引用列和被引用表中的被引用列都必需包含分布列，且分布情况完全相同；
4. 仅 BS 模式支持自引用约束，其他模式均不支持。

### 4.3.3 索引限制

DMDPC 对于索引存在以下使用限制：

1. 不支持空间索引、位图索引、位图连接索引、全局函数索引；
2. 不支持外键引用全局索引列；
3. 不支持将包方法、类方法作为函数索引的列；
4. 不支持设置二级索引的默认表空间，如果已经设置则直接忽略，系统自动将表聚集索引所在的表空间作为表二级索引的表空间，二级索引的表空间必须和表聚集索引表空间相同。
5. 创建全局分区索引时，\<PARTITION 子句 > 不支持和 ONLINE 关键字一起使用。\<PARTITION 子句 > 仅支持一级分区，且分区列必须是索引列的子集和前导列。\<PARTITION 子句 > 中的 RANGE 分区必须包含 MAXVALUE 分区，LIST 分区必须包含 DEFAULT 分区。\<PARTITION 子句 > 中指定的子索引表空间、\<STORAGE 子句 > 中主索引的表空间，均需和主表的表空间保持一致。

### 4.3.4 系统包限制

DMDPC 对于系统包存在以下使用限制：

1. 不支持 DBMS\_AUDIT 包、DBMS\_SPACE 包、DBMS\_REDEFINITION 包；
2. DBMS\_FLASHBACK 包不支持查询指定 LSN 时刻的数据库版本，可以查询指定时间的数据库版本；
3. 对于 DBMS\_REDEFINITION 包，不支持包中的 COPY\_TABLE\_DEPENDENTS 方法；
4. DMDPC 环境下执行 DBMS\_MVIEW.REFRESH 方法时，只能单条执行。如果在语句块中执行该方法，则只能通过 EXECUTE IMMEDIATE 动态执行。

### 4.3.5 备份还原限制

DMDPC 对于备份还原存在以下使用限制：

1. 不支持表级备份；
2. 不支持 DDL\_CLONE 备份还原；
3. 不支持联机还原；
4. 不支持 BP 节点还原恢复到指定 LSN；
5. 不支持表空间级备份还原。不支持执行 LINUX 操作系统下，恢复被删除文件的过程 SP\_TABLESPACE\_PREPARE\_RECOVER 和 SP\_TABLESPACE\_RECOVER；
6. 不支持备份还原相关的系统函数 SF\_BAKSET\_CHECK、SF\_BAKSET\_REMOVE、SP\_DUMP\_BCT，位于《DM8\_SQL 语言使用手册》附录 3 系统存储过程和函数中 3.备份恢复管理；仅支持删除归档的系统函数 SF\_ARCHIVELOG\_DELETE\_BEFORE\_TIME()和 SF\_ARCHIVELOG\_DELETE\_BEFORE\_LSN()，位于《DM8\_SQL 语言使用手册》附录 3 系统存储过程和函数中 9.日志与检查点管理。

### 4.3.6 其他限制

除上述功能限制外，DMDPC 还存在以下使用限制：

1. 不支持在 SP 节点上使用 ALTER DATABASE 语句修改数据库状态和模式，例如 ALTER DATABASE MOUNT、ALTER DATABASE OPEN、ALTER DATABASE NORMAL 等。
2. 不支持游标类型的参数。
3. 不支持 new 数组对象。
4. 关闭两阶段提交后不支持 XA 接口功能。
5. 对于闪回表、闪回查询和 DBMS\_FLASHBACK 包，仅支持基于时间执行闪回相关操作，不支持基于 LSN 执行闪回相关操作。
6. 不支持结果集缓存，即无法配置结果集缓存相关的参数。
7. 不支持 JOIN APPLY 的连接查询。
8. 不支持同层引用列。
9. 执行 DDL 时，强制自动提交，不支持 DDL\_AUTO\_COMMIT=0。
10. 目前 DM 没有错误码合并机制，当连接 SP 执行相同语句，多个节点反馈出错的情况下，可能出现报错不同的情况，符合预期。
11. DMDPC 下连接 SP/BS\[GLOBAL 方式\]执行 ALTER DATABASE ADD/RESIZE LOGFILE 时，会广播给所有 BP 主节点执行，BP 备节点不会执行, 主节点不会生成日志。通过增加 ALTER TABLESPACE RLOG ADD DATAFILE 的方式增加联机日志时,主节点会生成日志，但 BP 备库会跳过执行。
12. DMDPC 下直连 MP/BP/BS\[LOCAL 方式\]，DISQL 连接的节点会自己单独执行。
13. DMDPC 下暂时不支持 ALTER DATABASE RENAME LOGFILE 语句。
14. DMDPC 下连接 SP/BS\[GLOBAL 方式\]执行 ALTER SYSTEM SWITCH LOGFILE 或 ALTER SYSTEM ARCHIVE LOG CURRENT 时，会广播给 MP 主节点执行。
15. DMDPC 下连接 MP/BP/BS\[LOCAL\]方式执行 ALTER SYSTEM SWITCH LOGFILE 或 ALTER SYSTEM ARCHIVE LOG CURRENT 时，会自己执行。
16. 不支持收集多列统计信息。
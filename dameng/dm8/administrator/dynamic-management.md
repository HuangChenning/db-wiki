---
title: "动态管理和性能视图"
book: "DM8 系统管理员手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dynamic-management.html
tags:
  - dameng
  - dm8
  - administrator
---

## 21.1 理解动态管理视图

达梦数据库中的动态性能视图能自动收集数据库中的一些活动信息，系统管理员根据这些信息可以了解数据库运行的基本情况，为数据库的维护和优化提供依据。动态性能视图信息也是数据库中数据字典的一部分，与我们平常所说的数据字典不同的是，平常意义上的数据字典是指静态数据字典信息，也即用户访问数据字典信息时，内容不会发生改变，而动态视图信息是随着数据库的运行随时更改，具有一定的即时性。

系统管理员为了更好地了解数据库的一些运行时信息，可以查询动态视图表。首先系统管理员需要知道达梦数据库中提供了多少动态视图，有哪些类型动态视图，以及这些动态视图的用途是什么。关于这些内容可以参考附录 2，也可以通过查询 V$DYNAMIC\_TABLES 获得所有的动态性能视图名称。

动态视图表与静态字典信息表命名方式不同，静态字典表一般以 SYS 为前缀，如系统表 SYSINDEXES，而动态视图则以 V$为前缀，如 V$DM\_INI。

## 21.2 使用动态管理视图

在 DM8 中，动态视图提供的系统信息主要分为以下几个方面：

1. **系统信息**

包括数据库版本、实例统计信息、资源限制信息、进程信息、全局索引 IID 信息、事件信息；涉及的动态视图有 V$SESSIONS、V$INSTANCE、V$RESOURCE\_LIMIT、V$PROCESS、V$IID、V$SYSSTAT 等。

例 查看数据库中实例信息

```
SELECT * FROM V$INSTANCE;
```

查询结果如下：

```
行号       NAME     INSTANCE_NAME INSTANCE_NUMBER HOST_NAME SVR_VERSION                DB_VERSION          START_TIME          STATUS$ MODE$  OGUID       DSC_SEQNO   DSC_ROLE BUILD_VERSION                     BUILD_TIME
---------- -------- ------------- --------------- --------- -------------------------- ------------------- ------------------- ------- ------ ----------- ----------- -------- --------------------------------- --------------------
1          DMSERVER DMSERVER      1               test121   DM Database Server x64 V8  DB Version: 0x7000d 2024-11-26 17:10:40 OPEN    NORMAL 0           0           NULL     03134284347-20241121-250764-10000 Nov 26 2024 15:41:48
```
2. **存储信息**

包括数据库信息、表空间信息、数据文件信息、日志相关信息；涉及的动态视图有 V$DATAFILE、V$DATABASE、V$TABLESPACE、V$HUGE\_TABLESPACE、V$RLOGFILE 等。

例 查询表空间信息

```
SELECT * FROM V$TABLESPACE;
```

查询结果如下：

```
ID NAME CACHE TYPE$ STATUS$ MAX_SIZE TOTAL_SIZE FILE_NUM ENCRYPT_NAME ENCRYPTED_KEY COPY_NUM SIZE_MODE

……

7 TABLESPACE_03 NORMAL 1 0 0 32768 1 null null null null

9 TS_001 NORMAL 1 0 0 16384 1 null null null null
```
3. **内存管理信息**

包括内存池使用情况、缓冲区信息、虚拟机信息、虚拟机栈帧信息；涉及的动态视图有 V$MEM\_POOL、V$VMS、V$STKFRM、V$BUFFERPOOL、V$BUFFER\_LRU\_FIRST、V$BUFFER\_UPD\_FIRST、V$BUFFER\_LRU\_LAST、V$BUFFER\_UPD\_LAST 等。

例 查询内存池 BUFFERPOOL 的页数、读取页数和命中率信息

```
SELECT NAME,N_PAGES,N_LOGIC_READS,RAT_HIT FROM V$BUFFERPOOL;
```

查询结果如下：

```
行号    NAME       N_PAGES         N_LOGIC_READS           RAT_HIT
------ ---- -------------------- ----------- -----------------
1       NORMAL    1024            0                   1.0000000000E+000
2       RECYCLE   8192            52                  9.8113207547E-001
3       NORMAL    1280            1772                9.2726321298E-001
4       NORMAL    8960            7                    7.0000000000E-001
```
4. **事务信息**

包括所有事务信息、当前事务可见的事务信息、事务锁信息（TID 锁、对象锁）、回滚段信息、事务等待信息；涉及的动态视图有 V$TRX、V$TRXWAIT、V$LOCK、V$PURGE 等。

例 查询系统中上锁的事务、锁类型，以及表 ID 信息

```
SELECT TRX_ID,LTYPE,LMODE,TABLE_ID FROM V$LOCK;
```

查询结果如下：

```
行号 TRX_ID LTYPE LMODE TABLE_ID

---------- -------------------- ------ ----- -----------

1 1436 OBJECT IX 1311

2 1433 OBJECT IX 1310

3 1436 TID X -1

4 1433 TID X -1
```
5. **线程信息**

包括所有活动线程信息、线程作业信息、线程锁信息、线程的资源等待信息；涉及的动态视图有 V$THREADS 等。

例 查看系统中所有活动的线程信息

```
SELECT TOP 2* FROM V$THREADS;
```

查询结果如下：

```
行号       ID                   NAME       START_TIME                 THREAD_DESC         SESS_ID              PROCESSOR_ID WAIT_SEQ    WAIT_STATUS     WAIT_TIME  
---------- -------------------- ---------- -------------------------- ------------------- -------------------- ------------ ----------- --------------- -----------
1          84540                dm_sql_thd 2025-12-03 09:47:44.000000 User session thread 140199769256688      65535        0           NOTHING TO WAIT -1
2          84541                dm_sql_thd 2025-12-03 09:47:44.000000 User session thread 140198870257504      65535        27          NOTHING TO WAIT -1
```
6. **历史模块**

包括 SQL 历史信息、SQL 执行节点历史信息、检查点历史信息、命令行历史信息、线程等待历史信息、死锁历史信息、回滚段历史信息、运行时错误历史信息、DMSQL 程序中执行 DDL 语句的历史信息、返回大数据量结果集的历史信息、所有活动过线程的历史信息；涉及的动态视图有 V$CKPT\_HISTORY、V$CMD\_HISTORY、V$DEADLOCK\_HISTORY、V$PLSQL\_DDL\_HISTORY、V$PRE\_RETURN\_HISTORY、V$RUNTIME\_ERR\_HISTORY、V$SQL\_HISTORY、V$SQL\_NODE\_HISTORY、V$SQL\_NODE\_NAME 等。

例 查询系统执行的 SQL 历史信息

```
SELECT SESS_ID,TOP_SQL_TEXT,TIME_USED FROM V$SQL_HISTORY;
```

查询结果如下：

```
行号 SESS_ID TOP_SQL_TEXT TIME_USED
-------- ----------------- ---------------------
1  187744368 INSERT INTO T1 VALUES(5,0); 21707
```
7. **缓存信息**

包括 SQL 语句缓存、执行计划缓存、结果集缓存、字典缓存信息、字典缓存中的对象信息、代价信息；涉及的动态视图有 V$CACHEITEM、V$SQL\_PLAN、V$CACHERS、V$CACHESQL、V$DICT\_CACHE\_ITEM、V$DICT\_CACHE 等。

例 查看字典缓存的信息

```
SELECT * FROM V$DICT_CACHE;
```

查询结果如下：

```
行号 ADDR POOL_ID TOTAL_SIZE USED_SIZE DICT_NUM
-------- ----------------- ---------------------
1  0x0B56F070 1 5242880 113530 36
```
8. **会话信息**

包括连接信息、会话信息；涉及的动态视图有 V$CONNECT、V$STMTS、V$SESSIONS 等。

例 查看会话信息

```
SELECT SESS_ID,SQL_TEXT,STATE,CREATE_TIME,CLNT_HOST FROM V$SESSIONS;
```

查询结果如下：

```
行号 SESS_ID SQL_TEXT STATE CREATE_TIME CLNT_HOST
-------- ----------------- ---------------------
1 187744368 SELECT SESS_ID,SQL_TEXT,STATE,CREATE_TIME,CLNT_HOST FROM V\$SESSIONS; ACTIVE 2011-09-19 19:20:38.000000 FREESKYC-FB8846
```

查看动态视图可以不单单只查询一个动态视图表，还可利用动态视图表之间的联系得到更多想要的信息。

例如，系统管理员如果要对一条 SQL 语句进行调优，需要知道每个执行节点花费了多少时间，查询 V$SQL\_NODE\_NAME 可以知道执行节点的名字，查询 V$SQL\_NODE\_HISTORY 可以查询到每个执行节点的时间，通过两个动态视图表的执行节点类型 TYPE$字段做等值连接。

如执行一条 SQL 语句，然后查询其执行节点所花费时间，假设其执行 ID（EXEC\_ID）为 4。

```
SELECT * FROM t1 WHERE c1 = (SELECT d1 FROM t2 WHERE c2 = d2);
```

关联查询动态视图 V$SQL\_NODE\_NAME 和 V$SQL\_NODE\_HISTORY 获取节点执行时间：

```
SELECT N.NAME, TIME_USED, N_ENTER FROM V$SQL_NODE_NAME N, V$SQL_NODE_HISTORY H WHERE N.TYPE$ = H.TYPE$ AND EXEC_ID = 4;
```

查询结果如下：

```
行号    NAME  TIME_USED  N_ENTER
1       CSCN2   381     6
2       CSCN2   250     3
3       NLI2    52      14
4       SLCT2   102     8
5       HAGR2   11831   6
6       PRJT2   32      6
7       CSCN2   272     3
8       HI3     19309   9
9       PRJT2   29      6
10      NSET2   120     4
11      DLCK    23      2
```

根据结果可以看到执行计划中各执行节点花费的时间，进而对 SQL 语句进行分析和改写。
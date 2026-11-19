---
title: "查看内存的使用信息"
book: "系统管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150270.html"
tags:
  - oceanbase
  - standalone
  - ref-system-management
---

# 查看内存的使用信息

本文介绍了使用虚拟表和日志内容查看内存使用信息的方式。

## 视图查询

### 查询 OBServer 节点总内存

在 `sys` 租户下，通过查询 `oceanbase.gv$sysstat` 视图可以查看指定机器的内存占用，示例如下：

``` sql
obclient> SELECT * FROM oceanbase.gv$sysstat WHERE svr_ip = '172.xx.xxx.xxx' AND svr_port=2882 AND con_id=1 AND name like '%observer memory%';
+--------+----------------+----------+------------+---------------------------------+-------+-------------+------------+---------+
| CON_ID | SVR_IP         | SVR_PORT | STATISTIC# | NAME                            | CLASS | VALUE       | VALUE_TYPE | STAT_ID |
+--------+----------------+----------+------------+---------------------------------+-------+-------------+------------+---------+
|      1 | 172.xx.xxx.xxx |     2882 |        657 | observer memory used size       |    64 |  5941141504 | SET_VALUE  |  140008 |
|      1 | 172.xx.xxx.xxx |     2882 |        658 | observer memory free size       |    64 |   297742336 | SET_VALUE  |  140009 |
|      1 | 172.xx.xxx.xxx |     2882 |        660 | observer memory hold size       |    64 |  6238883840 | SET_VALUE  |  140011 |
|      1 | 172.xx.xxx.xxx |     2882 |        663 | effective observer memory limit |    64 | 21474836480 | SET_VALUE  |  140014 |
+--------+----------------+----------+------------+---------------------------------+-------+-------------+------------+---------+
4 rows in set
```

### 查看各个租户内存使用总量

在 `sys` 租户下，通过查询 `oceanbase.GV$OB_TENANT_MEMORY` 视图可以查看所有租户的内存使用总量。

``` sql
obclient> SELECT tenant_id, hold FROM oceanbase.GV$OB_TENANT_MEMORY WHERE svr_ip = '172.xx.xxx.xxx' AND svr_port=2882  GROUP BY tenant_id;
+-----------+------------+
| tenant_id | hold       |
+-----------+------------+
|         1 | 1629179904 |
|       500 | 1164455936 |
|       508 |   36343808 |
|      1001 |  874590208 |
|      1002 | 1184763904 |
|      1003 |  500969472 |
|      1004 |  536158208 |
+-----------+------------+
7 rows in set
```

### 查看指定租户的内存使用详情

在 `sys` 租户下，通过查询 `oceanbase.GV$OB_MEMORY` 视图，可以查看指定租户的内存使用详情。

``` sql
obclient> SELECT tenant_id, CTX_NAME, hold FROM oceanbase.GV$OB_MEMORY WHERE svr_ip = '172.xx.xxx.xxx' AND svr_port=2882 AND tenant_id = 1002 GROUP BY CTX_NAME;
+-----------+-------------------------------+-----------+
| tenant_id | CTX_NAME                      | hold      |
+-----------+-------------------------------+-----------+
|      1002 | DEFAULT_CTX_ID                |  83927040 |
|      1002 | DO_NOT_USE_ME                 |         0 |
|      1002 | MEMSTORE_CTX_ID               |  56180736 |
|      1002 | EXECUTE_CTX_ID                |         0 |
|      1002 | TRANS_CTX_MGR_ID              |    933888 |
|      1002 | PLAN_CACHE_CTX_ID             | 135717248 |
|      1002 | WORK_AREA                     |         0 |
|      1002 | GLIBC                         |  33681520 |
|      1002 | CO_STACK                      | 116637696 |
|      1002 | LIBEASY                       |         0 |
|      1002 | LOGGER_CTX_ID                 |         0 |
|      1002 | KVSTORE_CACHE_ID              | 251658240 |
|      1002 | META_OBJ_CTX_ID               |   9216000 |
|      1002 | TX_CALLBACK_CTX_ID            |   1259840 |
|      1002 | LOB_CTX_ID                    |      8128 |
|      1002 | PS_CACHE_CTX_ID               |         0 |
|      1002 | RPC_CTX_ID                    |         0 |
|      1002 | PKT_NIO                       |         0 |
|      1002 | TX_DATA_TABLE                 |  11595648 |
|      1002 | STORAGE_LONG_TERM_META_CTX_ID |         0 |
|      1002 | MDS_DATA_ID                   |   1332992 |
|      1002 | MDS_CTX_ID                    |         0 |
|      1002 | SCHEMA_SERVICE                |         0 |
|      1002 | UNEXPECTED_IN_500             |         0 |
+-----------+-------------------------------+-----------+
24 rows in set
```

### 查看某个内存模块中内存的使用详情

在 `sys` 租户下，通过查询 `oceanbase.GV$OB_MEMORY`，可以查看某个内存模块中内存的使用详情。也可以指定机器、租户等信息来查询。

``` sql
obclient> SELECT * FROM oceanbase.GV$OB_MEMORY WHERE svr_ip = ' 172.xx.xxx.xxx' AND svr_port= 2882 AND tenant_id = 1002 ORDER BY hold desc limit 10;
+-----------+----------------+----------+-------------------+-----------------+-------+-----------+-----------+
| TENANT_ID | SVR_IP         | SVR_PORT | CTX_NAME          | MOD_NAME        | COUNT | HOLD      | USED      |
+-----------+----------------+----------+-------------------+-----------------+-------+-----------+-----------+
|      1002 |  172.xx.xxx.xxx |     2882 | KVSTORE_CACHE_ID  | KvstorCacheMb   |   120 | 251658240 |         0 |
|      1002 |  172.xx.xxx.xxx |     2882 | PLAN_CACHE_CTX_ID | SqlPhyPlan      |  9037 | 135717248 | 122930613 |
|      1002 |  172.xx.xxx.xxx |     2882 | CO_STACK          | CoStack         |   226 | 116637696 | 116420736 |
|      1002 |  172.xx.xxx.xxx |     2882 | DEFAULT_CTX_ID    | LogGroupBuffer  |     2 |  83927040 |  83886080 |
|      1002 |  172.xx.xxx.xxx |     2882 | MEMSTORE_CTX_ID   | Memstore        |    27 |  56180736 |  56155032 |
|      1002 |  172.xx.xxx.xxx |     2882 | DEFAULT_CTX_ID    | MysqlRequesReco |    40 |  55697408 |  55533120 |
|      1002 |  172.xx.xxx.xxx |     2882 | GLIBC             | PlJit           | 50696 |  33681520 |  29551316 |
|      1002 |  172.xx.xxx.xxx |     2882 | DEFAULT_CTX_ID    | ServerObjecPool |     3 |  23187456 |  23126016 |
|      1002 |  172.xx.xxx.xxx |     2882 | DEFAULT_CTX_ID    | CACHE_MAP_NODE  |    10 |  20807680 |  20797440 |
|      1002 |  172.xx.xxx.xxx |     2882 | DEFAULT_CTX_ID    | DiagnosticInfos |    16 |  16908288 |  16777728 |
+-----------+----------------+----------+-------------------+-----------------+-------+-----------+-----------+
10 rows in set
```

## 日志查询

### 查询 OBServer 节点总内存

1.  登录 OBServer 节点所在的机器。

2.  执行以下命令，进入日志文件所在的目录。

    ```
    cd ~/oceanbase/log
    ```

3.  执行以下命令，查询 OBServer 节点总内存使用情况。

    ```
    grep CHUNK_MGR observer.log
    ```

    查询结果如下：

    ```
    [2022-07-14 09:29:26.243252] INFO  [STORAGE] print_tenant_usage (ob_tenant_memory_printer.cpp:121) [104667][ServerGTimer][T0][Y0-0000000000000000-0-0] [lt=6] [CHUNK_MGR] free=42 pushes=2504440 pops=2504398 limit= 85,899,345,920 hold= 10,254,864,384 total_hold= 10,655,629,312 used= 10,166,784,000 freelist_hold=     88,080,384 maps=        159,816 unmaps=        156,719 large_maps=        156,935 large_unmaps=        156,719 memalign=0 virtual_memory_used= 11,851,849,728
    [2022-07-14 09:29:36.309803] INFO  [STORAGE] print_tenant_usage (ob_tenant_memory_printer.cpp:121) [104667][ServerGTimer][T0][Y0-0000000000000000-0-0] [lt=11] [CHUNK_MGR] free=39 pushes=2504609 pops=2504570 limit= 85,899,345,920 hold= 10,254,864,384 total_hold= 10,655,629,312 used= 10,173,075,456 freelist_hold=     81,788,928 maps=        159,826 unmaps=        156,729 large_maps=        156,945 large_unmaps=        156,729 memalign=0 virtual_memory_used= 11,851,849,728
    [2022-07-14 09:29:46.376095] INFO  [STORAGE] print_tenant_usage (ob_tenant_memory_printer.cpp:121) [104667][ServerGTimer][T0][Y0-0000000000000000-0-0] [lt=6] [CHUNK_MGR] free=36 pushes=2504774 pops=2504738 limit= 85,899,345,920 hold= 10,254,864,384 total_hold= 10,655,629,312 used= 10,179,366,912 freelist_hold=     75,497,472 maps=        159,836 unmaps=        156,739 large_maps=        156,955 large_unmaps=        156,739 memalign=0 virtual_memory_used= 11,851,849,728
    [2022-07-14 09:29:56.455361] INFO  [STORAGE] print_tenant_usage (ob_tenant_memory_printer.cpp:121) [104667][ServerGTimer][T0][Y0-0000000000000000-0-0] [lt=9] [CHUNK_MGR] free=33 pushes=2504938 pops=2504905 limit= 85,899,345,920 hold= 10,254,864,384 total_hold= 10,655,629,312 used= 10,185,658,368 freelist_hold=     69,206,016 maps=        159,846 unmaps=        156,749 large_maps=        156,965 large_unmaps=        156,749 memalign=0 virtual_memory_used= 11,851,849,728
    [2022-07-14 09:30:06.520032] INFO  [STORAGE] print_tenant_usage (ob_tenant_memory_printer.cpp:121) [104667][ServerGTimer][T0][Y0-0000000000000000-0-0] [lt=7] [CHUNK_MGR] free=32 pushes=2505099 pops=2505067 limit= 85,899,345,920 hold= 10,254,864,384 total_hold= 10,655,629,312 used= 10,187,755,520 freelist_hold=     67,108,864 maps=        159,856 unmaps=        156,759 large_maps=        156,975 large_unmaps=        156,759 memalign=0 virtual_memory_used= 11,851,849,728
    [2022-07-14 09:30:16.586924] INFO  [STORAGE] print_tenant_usage (ob_tenant_memory_printer.cpp:121) [104667][ServerGTimer][T0][Y0-0000000000000000-0-0] [lt=8] [CHUNK_MGR] free=32 pushes=2505261 pops=2505229 limit= 85,899,345,920 hold= 10,254,864,384 total_hold= 10,655,629,312 used= 10,187,755,520 freelist_hold=     67,108,864 maps=        159,866 unmaps=        156,769 large_maps=        156,985 large_unmaps=        156,769 memalign=0 virtual_memory_used= 11,851,849,728
    ```

    日志信息中的部分参数说明如下表所示。

    | 参数          | 说明                                        |
    |---------------|---------------------------------------------|
    | limit         | OBServer 节点总内存限制                     |
    | hold          | OBServer 节点从操作系统获取到的所有的内存   |
    | used          | OBServer 节点实际使用到的内存（包括 Cache） |
    | freelist_hold | OBServer 节点未使用的内存                   |

### 查看各个租户的内存使用总量

1.  登录 OBServer 节点所在的机器。

2.  执行以下命令，进入日志文件所在的目录。

    ```
    cd ~/oceanbase/log
    ```

3.  执行以下命令，查看各租户的内存使用总量。

    ```
    grep ob_malloc_allocator.cpp observer.log
    ```

    查询的部分结果如下：

    ```
    [2022-07-14 09:29:26.241149] INFO  [LIB] operator() (ob_malloc_allocator.cpp:387) [104667][ServerGTimer][T0][Y0-0000000000000000-0-0] [lt=8] [MEMORY] tenant: 500, limit: 9,223,372,036,854,775,807 hold: 6,765,867,008 rpc_hold: 0 cache_hold: 0 cache_used: 0 cache_item_count: 0
    [2022-07-14 09:29:26.241729] INFO  [LIB] operator() (ob_malloc_allocator.cpp:387) [104667][ServerGTimer][T1][Y0-0000000000000000-0-0] [lt=10] [MEMORY] tenant: 1, limit: 17,179,869,184 hold: 1,170,079,744 rpc_hold: 0 cache_hold: 144,703,488 cache_used: 144,703,488 cache_item_count: 69
    [2022-07-14 09:29:26.242025] INFO  [LIB] operator() (ob_malloc_allocator.cpp:387) [104667][ServerGTimer][T1001][Y0-0000000000000000-0-0] [lt=5] [MEMORY] tenant: 1001, limit: 1,073,741,824 hold: 511,574,016 rpc_hold: 0 cache_hold: 218,103,808 cache_used: 218,103,808 cache_item_count: 104
    [2022-07-14 09:29:26.242321] INFO  [LIB] operator() (ob_malloc_allocator.cpp:387) [104667][ServerGTimer][T1002][Y0-0000000000000000-0-0] [lt=8] [MEMORY] tenant: 1002, limit: 6,442,450,944 hold: 534,687,744 rpc_hold: 0 cache_hold: 44,040,192 cache_used: 44,040,192 cache_item_count: 21
    [2022-07-14 09:29:26.242625] INFO  [LIB] operator() (ob_malloc_allocator.cpp:387) [104667][ServerGTimer][T1003][Y0-0000000000000000-0-0] [lt=4] [MEMORY] tenant: 1003, limit: 1,073,741,824 hold: 511,574,016 rpc_hold: 0 cache_hold: 224,395,264 cache_used: 224,395,264 cache_item_count: 107
    [2022-07-14 09:29:26.242901] INFO  [LIB] operator() (ob_malloc_allocator.cpp:387) [104667][ServerGTimer][T1004][Y0-0000000000000000-0-0] [lt=8] [MEMORY] tenant: 1004, limit: 6,442,450,944 hold: 633,266,176 rpc_hold: 0 cache_hold: 65,011,712 cache_used: 65,011,712 cache_item_count: 31
    [2022-07-14 09:29:36.307729] INFO  [LIB] operator() (ob_malloc_allocator.cpp:387) [104667][ServerGTimer][T0][Y0-0000000000000000-0-0] [lt=10] [MEMORY] tenant: 500, limit: 9,223,372,036,854,775,807 hold: 6,765,867,008 rpc_hold: 0 cache_hold: 0 cache_used: 0 cache_item_count: 0
    ```

### 查看某个租户内存使用详情

1.  登录 OBServer 节点所在的机器。

2.  执行以下命令，进入日志文件所在的目录。

    ```
    cd ~/oceanbase/log
    ```

3.  进行以下操作，查看 `tenant_id` 为 `1002` 的租户的内存使用总量。

    1.  使用 Vim 打开 `observer.log`。

    2.  搜索 `ob_malloc_allocator.cpp.*1002`。

        ``` javascript
        [MEMORY] ctx_id=           DEFAULT_CTX_ID hold_bytes=    258,838,528 limit= 9,223,372,036,854,775,807
        [MEMORY] ctx_id=          MEMSTORE_CTX_ID hold_bytes=     67,108,864 limit= 9,223,372,036,854,775,807
        [MEMORY] ctx_id=         TRANS_CTX_MGR_ID hold_bytes=      2,097,152 limit= 9,223,372,036,854,775,807
        [MEMORY] ctx_id=        PLAN_CACHE_CTX_ID hold_bytes=    132,120,576 limit= 9,223,372,036,854,775,807
        [MEMORY] ctx_id=                WORK_AREA hold_bytes=      4,194,304 limit=               322,122,545
        [MEMORY] ctx_id=          META_OBJ_CTX_ID hold_bytes=     22,093,824 limit=               644,245,090
        [MEMORY] ctx_id=       TX_CALLBACK_CTX_ID hold_bytes=      2,097,152 limit= 9,223,372,036,854,775,807
        [MEMORY] ctx_id=               LOB_CTX_ID hold_bytes=      2,097,152 limit= 9,223,372,036,854,775,807
        ```

### 查看某个内存模块的内存使用详情

1.  登录 OBServer 节点所在的机器。

2.  执行以下命令，进入日志文件所在的目录。

    ```
    cd ~/oceanbase/log
    ```

3.  进行以下操作，查看 `tenant_id` 为 `1002` 的租户的 `DEFAULT_CTX_ID` 模块的内存使用详情。

    1.  使用 Vim 打开 `observer.log`。

    2.  搜索 `MEMORY.*1002.*DEFAULT_CTX_ID`。

        ``` javascript
        [MEMORY] tenant_id= 1002 ctx_id=           DEFAULT_CTX_ID hold=    258,838,528 used=    216,411,808 limit= 9,223,372,036,854,775,807
        [MEMORY] idle_size=         0 free_size=         0
        [MEMORY] wash_related_chunks=         0 washed_blocks=         0 washed_size=         0
        [MEMORY] hold=     86,261,760 used=     86,239,232 count=       4 avg_used=     21,559,808 mod=MysqlRequesReco
        [MEMORY] hold=     83,927,040 used=     83,886,080 count=       2 avg_used=     41,943,040 mod=LogGroupBuffer
        [MEMORY] hold=     16,646,144 used=     16,637,952 count=       8 avg_used=      2,079,744 mod=CACHE_MAP_NODE
        [MEMORY] hold=     10,674,448 used=     10,631,028 count=      42 avg_used=        253,119 mod=OmtTenant
        [MEMORY] hold=      5,021,696 used=      4,977,920 count=       3 avg_used=      1,659,306 mod=SqlPlanMon
        [MEMORY] hold=      4,249,664 used=      4,229,120 count=       2 avg_used=      2,114,560 mod=LSMap
        [MEMORY] hold=      1,589,248 used=      1,573,024 count=       2 avg_used=        786,512 mod=HashBuckLCSta
        [MEMORY] hold=      1,571,264 used=      1,558,656 count=     197 avg_used=          7,911 mod=TX_DATA_TABLE
        [MEMORY] hold=      1,548,288 used=      1,383,795 count=      21 avg_used=         65,895 mod=SqlDtl
        [MEMORY] hold=      1,187,840 used=      1,179,768 count=       1 avg_used=      1,179,768 mod=HashBuckPsInfo
        [MEMORY] hold=      1,187,840 used=      1,179,768 count=       1 avg_used=      1,179,768 mod=HashBuckPsCache
        [MEMORY] hold=        794,624 used=        786,512 count=       1 avg_used=        786,512 mod=HashBuckPlanCac
        ```

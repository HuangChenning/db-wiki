---
title: "附录 2"
book: "DM8 系统管理员手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dm8-admin-manual-appendix2.html
tags:
  - dameng
  - dm8
  - administrator
---

## 附录 2 动态性能视图

动态视图存储着数据库的配置及数据库中变化的活动状态信息，可以通过查询 V$DYNAMIC\_TABLES 获得所有的动态性能视图名称，V$DYNAMIC\_TABLES 各列介绍如下：

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 动态视图名 |
| 2 | ID | INTEGER | 动态视图 ID |
| 3 | SCHNAME | VARCHAR(128) | 动态视图所属模式 |
| 4 | SYNONYMS | VARCHAR(512) | 动态视图的同义词 |

动态视图的模式名为 SYS，例如：SYS. V$DICT\_CACHE\_ITEM。不过 DM 为每个动态视图建立了同名的全局同义词，因此用户也可以省略模式名对动态视图进行访问。动态视图的模式名为 SYS，例如：SYS. V$DICT\_CACHE\_ITEM。不过 DM 为每个动态视图建立了同名的全局同义词，因此用户也可以省略模式名对动态视图进行访问。

关于动态视图的几点说明如下：

一. 普通用户查询某动态视图需要获得系统管理员的授权才能进行；

二. 在 MPP 环境下，查询结果会显示所有节点的动态视图信息；

三. 与备份还原相关的动态视图此处不作介绍，请参考《DM8 备份与还原》；

四．与 DM MPP 相关的动态视图此处不作介绍，请参考《DM8 大规模并行处理 MPP》；

五．与 DMDSC 相关的动态视图此处不作介绍，请参考《DM8 数据共享集群》；

六．与数据守护相关的动态视图此处不作介绍，请参考《DM8 数据守护与读写分离集群 V4.0》。

#### 1\. 资源管理

1） **V$DICT\_CACHE\_ITEM**

显示字典缓存中的字典对象信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TYPE | VARCHAR(128) | 字典对象的类型。类型如下：DB、TABLE、VIEW、INDEX、USER、ROLE、PROCEDURE、TRIGGER、CONSTRAINT、SCHEMA、SEQUENCE、DBLINK、PACKAGE、OBJECT、SYNOM、CRYPT、CIPHER、IDENTITY、SYS PRIVILEGE、OBJ PRIVILEGE、POLICY、RULE、COLUMN、DOMAIN、COLLATION、CONTEXT INDEX、REGEXP REWRITE、NORMAL REWRITE、CONTEXT、DIRECTORY、PROFILE、OPERATOR |
| 2 | ID | INTEGER | 字典对象 ID |
| 3 | NAME | VARCHAR(128) | 字典对象的名称 |
| 4 | SCHID | INTEGER | 字典对象所属模式 |
| 5 | PID | INTEGER | 父 ID |
| 6 | HASH\_VALUE | BIGINT | 缓存的 HASH 值 |
| 7 | SIZE | INTEGER | 字典对象内存大小，单位:BYTE |

2） **V$DICT\_CACHE**

显示字典缓存信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ADDR | VARCHAR(20) | 地址 |
| 2 | POOL\_ID | INTEGER | 缓冲区 ID |
| 3 | TOTAL\_SIZE | BIGINT | 总大小，单位 BYTE |
| 4 | USED\_SIZE | BIGINT | 实际使用大小，单位 BYTE |
| 5 | DICT\_NUM | INTEGER | 字典对象总数 |

3） **V$BUFFERPOOL**

数据缓冲区动态性能表，用来记录数据缓冲区结构的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 缓冲区 ID |
| 2 | NAME | VARCHAR(20) | 缓冲区名称 NORMAL/RECYCLE/FAST |
| 3 | PAGE\_SIZE | INTEGER | 基缓冲区页大小，不包括扩展池页，单位 BYTE |
| 4 | N\_PAGES | INTEGER | 页数 |
| 5 | N\_FIXED | INTEGER | 数据页被引用的次数 |
| 6 | FREE | INTEGER | 空闲页数目 |
| 7 | N\_DIRTY | INTEGER | 非空闲页中的脏页数目 |
| 8 | N\_CLEAR | INTEGER | 非空闲页中的干净页数目 |
| 9 | N\_TOTAL\_PAGES | INTEGER | 页总数，包括扩展池页 |
| 10 | N\_MAX\_PAGES | INTEGER | 最多的页数 |
| 11 | N\_LOGIC\_READS | BIGINT | READ 命中的次数 |
| 12 | N\_DISCARD | BIGINT | 淘汰的页数 |
| 13 | N\_PHY\_READS | BIGINT | READ 未命中的次数 |
| 14 | N\_PHY\_M\_READS | BIGINT | READ 未命中，批量读的次数 |
| 15 | RAT\_HIT | DOUBLE | 命中率 |
| 16 | N\_EXP\_BUFFERPOOL | INTEGER | 扩展缓冲区个数 |
| 17 | N\_UPD\_REMOVE | BIGINT | 从 update 链表删除页总数 |
| 18 | N\_PHY\_WRITE | BIGINT | 物理写入磁盘总次数 |
| 19 | N\_UPD\_PUT | BIGINT | DSC 远程读取数据后，加入 update 链表总数 |
| 20 | N\_UPD\_SEARCH | BIGINT | DSC 远程读取数据后，查找 update 链表插入位置扫描总数 |
| 21 | N\_DISCARD64 | BIGINT | 淘汰的页数，同 N\_DISCARD |
| 22 | N\_PHY\_READS64 | BIGINT | READ 未命中的次数，同 N\_PHY\_READS |
| 23 | N\_PHY\_M\_READS64 | BIGINT | READ 未命中，批量读的次数，同 N\_PHY\_M\_READS |
| 24 | N\_UPD\_REMOVE64 | BIGINT | 从 update 链表删除页总数，同 N\_UPD\_REMOVE |
| 25 | N\_PHY\_WRITE64 | BIGINT | 物理写入磁盘总数，同 N\_PHY\_WRITE |
| 26 | N\_UPD\_PUT64 | BIGINT | DSC 远程读取数据后，加入 update 链表总数，同 N\_UPD\_PUT |
| 27 | N\_UPD\_SEARCH64 | BIGINT | DSC 远程读取数据后，查找 update 链表插入位置扫描总数，同 N\_UPD\_SEARCH |
| 28 | N\_BUFMEM\_ALLOCED | INTEGER | 已分配出去的缓冲区页数 |
| 29 | N\_PTX\_BI\_ALLOCED | INTEGER | 分配给 PTX 前镜像页的缓冲区页数 |

4） **V$BUFFER\_LRU\_FIRST**

显示所有缓冲区 LRU 链首页信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | 缓冲区 ID |
| 2 | SPACE\_ID | INTEGER | 表空间 ID |
| 3 | FILE\_ID | INTEGER | 文件 ID |
| 4 | PAGE\_NO | INTEGER | 数据在文件中的页号 |
| 5 | RWLOCK | BIGINT | 线程锁地址 |
| 6 | PAGE | BIGINT | 数据页对应的内存块地址 |
| 7 | HASH | BIGINT | HASH 地址 |
| 8 | LSN | BIGINT | 页的当前 LSN |
| 9 | LRU\_NEXT | BIGINT | 下一个非空闲页地址 |
| 10 | LRU\_PREV | BIGINT | 上一个非空闲页地址 |
| 11 | UPD\_NEXT | BIGINT | 下一个脏页地址 |
| 12 | UPD\_PREV | BIGINT | 上一个脏页地址 |
| 13 | N\_FIXED | INTEGER | 数据页被引用的次数 |
| 14 | STATUS | INTEGER | 页状态。1：空闲；2：使用；4:正在读；5：正在写 |
| 15 | ACCESS\_CNT | INTEGER | 正在访问的页号 |
| 16 | FIRST\_LSN | BIGINT | 第一次被修改时对应的日志文件号 |
| 17 | FIRST\_FIL | INTEGER | 第一次被修改时对应的已经刷盘的最新文件号 |
| 18 | FIRST\_OFF | BIGINT | 第一次被修改时对应的已经刷盘的最新文件偏移 |

5） **V$BUFFER\_UPD\_FIRST**

显示所有缓冲区 UPDATE 链首页信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | 缓冲区 ID |
| 2 | SPACE\_ID | INTEGER | 表空间 ID |
| 3 | FILE\_ID | INTEGER | 文件 ID |
| 4 | PAGE\_NO | INTEGER | 数据在文件中的页号 |
| 5 | RWLOCK | BIGINT | 线程锁地址 |
| 6 | PAGE | BIGINT | 数据页对应的内存块地址 |
| 7 | HASH | BIGINT | HASH 地址 |
| 8 | LSN | BIGINT | 页的当前 LSN |
| 9 | LRU\_NEXT | BIGINT | 下一个非空闲页地址 |
| 10 | LRU\_PREV | BIGINT | 上一个非空闲页地址 |
| 11 | UPD\_NEXT | BIGINT | 下一个脏页地址 |
| 12 | UPD\_PREV | BIGINT | 上一个脏页地址 |
| 13 | N\_FIXED | INTEGER | 数据页被引用的次数 |
| 14 | STATUS | INTEGER | 页状态。1：空闲；2：使用；4:正在读；5：正在写 |
| 15 | ACCESS\_CNT | INTEGER | 正在访问的页号 |
| 16 | FIRST\_LSN | BIGINT | 第一次被修改时对应的日志文件号 |
| 17 | FIRST\_FIL | INTEGER | 第一次被修改时对应的已经刷盘的最新文件号 |
| 18 | FIRST\_OFF | BIGINT | 第一次被修改时对应的已经刷盘的最新文件偏移 |

6） **V$BUFFER\_LRU\_LAST**

显示所有缓冲区 LRU 链末页信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | 缓冲区 ID |
| 2 | SPACE\_ID | INTEGER | 表空间 ID |
| 3 | FILE\_ID | INTEGER | 文件 ID |
| 4 | PAGE\_NO | INTEGER | 数据在文件中的页号 |
| 5 | RWLOCK | BIGINT | 线程锁地址 |
| 6 | PAGE | BIGINT | 数据页对应的内存块地址 |
| 7 | HASH | BIGINT | HASH 地址 |
| 8 | LSN | BIGINT | 页的当前 LSN |
| 9 | LRU\_NEXT | BIGINT | 下一个非空闲页地址 |
| 10 | LRU\_PREV | BIGINT | 上一个非空闲页地址 |
| 11 | UPD\_NEXT | BIGINT | 下一个脏页地址 |
| 12 | UPD\_PREV | BIGINT | 上一个脏页地址 |
| 13 | N\_FIXED | INTEGER | 数据页被引用的次数 |
| 14 | STATUS | INTEGER | 页状态。1：空闲；2：使用；4:正在读；5：正在写 |
| 15 | ACCESS\_CNT | INTEGER | 正在访问的页号 |
| 16 | FIRST\_LSN | BIGINT | 第一次被修改时对应的日志文件号 |
| 17 | FIRST\_FIL | INTEGER | 第一次被修改时对应的已经刷盘的最新文件号 |
| 18 | FIRST\_OFF | BIGINT | 第一次被修改时对应的已经刷盘的最新文件偏移 |

7） **V$BUFFER\_UPD\_LAST**

显示所有缓冲区 UPDATE 链末页信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | 缓冲区 ID |
| 2 | SPACE\_ID | INTEGER | 表空间 ID |
| 3 | FILE\_ID | INTEGER | 文件 ID |
| 4 | PAGE\_NO | INTEGER | 数据在文件中的页号 |
| 5 | RWLOCK | BIGINT | 线程锁地址 |
| 6 | PAGE | BIGINT | 数据页对应的内存块地址 |
| 7 | HASH | BIGINT | hash 地址 |
| 8 | LSN | BIGINT | 页的当前 LSN |
| 9 | LRU\_NEXT | BIGINT | 下一个非空闲页地址 |
| 10 | LRU\_PREV | BIGINT | 上一个非空闲页地址 |
| 11 | UPD\_NEXT | BIGINT | 下一个脏页地址 |
| 12 | UPD\_PREV | BIGINT | 上一个脏页地址 |
| 13 | N\_FIXED | INTEGER | 数据页被引用的次数 |
| 14 | STATUS | INTEGER | 页状态。1：空闲；2：使用；4:正在读；5：正在写 |
| 15 | ACCESS\_CNT | INTEGER | 正在访问的页号 |
| 16 | FIRST\_LSN | BIGINT | 第一次被修改时对应的日志文件号 |
| 17 | FIRST\_FIL | INTEGER | 第一次被修改时对应的已经刷盘的最新文件号 |
| 18 | FIRST\_OFF | BIGINT | 第一次被修改时对应的已经刷盘的最新文件偏移 |

8） **V$CACHEITEM**

显示 SQL 缓冲区中缓存项的相关信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ADDRESS | BIGINT | CACHE 项的地址 |
| 2 | TYPE$ | VARCHAR（8188) | CACHE 项的类型：SQL，计划（PLN），结果集（RS），包信息（PKG\_INFO） |
| 3 | OVERFLOW | CHAR(1) | 是否溢出 |
| 4 | IN\_POOL | CHAR(1) | 是否在内存池中 |
| 5 | DISABLED | CHAR(1) | 是否可用 |
| 6 | N\_FIXED | INTEGER | 此缓冲项被引用的次数 |
| 7 | TS\_VALUE | INTEGER | 时间戳 |
| 8 | ITEM\_SIZE | BIGINT | 缓存节点大小（字节数） |
| 9 | N\_HIT | INTEGER | 节点命中次数 |
| 10 | N\_DIS\_FIXED | INTEGER | 内部保留字段 |

9） **V$CACHERS**

显示 SQL 缓冲区中结果集缓存的相关信息。在 INI 参数 USE\_PLN\_POOL!=0 时才统计。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | CACHE\_ITEM | BIGINT | 结果集在缓冲区中的地址，对应 V$CACHEITEM 中的 ADDRESS |
| 2 | PLN | BIGINT | 结果集对应查询计划，对应 V$SQL\_PLAN 的 PLN\_ADDR |
| 3 | N\_TABLES | INTEGER | 结果集涉及的表的数目 |
| 4 | TABLEID | VARCHAR(256) | 结果集涉及的表的 ID，用空格隔开 |
| 5 | MEM\_SIZE | BIGINT | 缓存节点大小（字节数） |
| 6 | EXEC\_TIME | INTEGER | 结果集生成所消耗的时间，单位毫秒 |

10） **V$CACHESQL**

显示 SQL 缓冲区中 SQL 语句缓存的相关信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | CACHE\_ITEM | BIGINT | 在内存中的位置，对应 V$CACHEITEM 中的 ADDRESS |
| 2 | SQL | VARCHAR(4096) | SQL 文本 |
| 3 | LEN | INTEGER | SQL 文本长度 |
| 4 | HASH\_VALUE | INTEGER | HASH 值 |

11） **V$CACHEPLN**

显示 SQL 缓冲区中的计划缓存的相关信息。在 INI 参数 USE\_PLN\_POOL!=0 时才统计。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | CACHE\_ITEM | BIGINT | CACHE 项的地址 |
| 2 | TYPE$ | VARCHAR(8188) | CACHE 项的类型：   SQL，   过程（SP），   触发器（TRIGGER），   动态执行（DYNAMIC SQL），   动态游标（DYNAMIC CURSOR）,   其它类型（UNKNOWN） |
| 3 | HASH\_VALUE | INTEGER | CACHE 项的 HASH 值 |
| 4 | SCHID | INTEGER | 模式 ID |
| 5 | USER\_ID | INTEGER | 用户 ID |
| 6 | OBJ\_ID | INTEGER | 对象 ID |
| 7 | RS\_CAN\_CACHED | CHAR(1) | 结果集是否缓存 |
| 8 | N\_RS\_CACHED | INTEGER | 无意义，均显示 0 |
| 9 | N\_TABLE | INTEGER | 涉及的表个数 |
| 10 | TABLEID | VARCHAR(256) | 计划涉及的表的 ID，用空格隔开 |
| 11 | SQLSTR | VARCHAR(4096) | 语句内容 |
| 12 | SQLCACHE | BIGINT | 对应 V$CACHESQL 中的 CACHE\_ITEM 地址 |
| 13 | DDLSCRIPT | VARCHAR(4096) | 无意义，均显示 NULL |
| 14 | RET\_CMD | INTEGER | 返回响应命令字 |
| 15 | STMT\_TYPE | INTEGER | SQL 语句类型 |
| 16 | N\_LIT\_PARA | INTEGER | 常量参数个数 |
| 17 | N\_CLNT\_PARA | INTEGER | 客户端绑定参数个数 |
| 18 | N\_COLS | INTEGER | 涉及到的列个数 |
| 19 | SEL\_UPDATABLE | CHAR(1) | 是否为查询更新 |
| 20 | MEM\_SIZE | BIGINT | 缓存节点大小，单位为字节数 |
| 21 | RS\_CAN\_CACHED\_IN\_RULE | CHAR(1) | 依据基本规则是否可以缓存结果集（'Y'或'N'），实际是否缓存还受结果集缓存相关参数影响，或者被手工强制设置不缓存 |
| 22 | BINDED | CHAR(1) | 用于表示执行计划的绑定情况，'N'：未绑定；'M'：内存中绑定；'P'：持久化绑定；'B'：内存中绑定与持久化绑定同时生效 |
| 23 | INDEPENDENT | CHAR(1) | 用于表示执行计划是否为独立计划。'Y'：独立计划；'N'：非独立计划 |
| 24 | BPARAM\_FOR\_OPT | CHAR(1) | 用于表示执行计划是否是批量参数优化的计划。'Y'：是；'N'：否 |
| 25 | HAS\_VPD\_POLICY | CHAR(1) | 用于表示执行计划是否含有 VPD 策略，'Y'：有；'N'：没有 |

12） **V$SQLTEXT**

显示 SQL 缓冲区中的 SQL 语句的相关信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SQL\_ADDR | VARBINARY(8) | 语句在缓存中的地址 |
| 2 | SQL\_ID | INTEGER | SQL 语句 ID（唯一标识） |
| 3 | N\_EXEC | INTEGER | 语句执行次数 |
| 4 | HASH\_VALUE | INTEGER | 语句 HASH 值 |
| 5 | CMD\_TYPE | VARCHAR(32) | 语句类型（来自语句类型，例如：DRO\_STMT\_CTAB） |
| 6 | SQL\_TEXT | VARCHAR(7168) | SQL 语句内容（如果超过 7168 字符，则分段存储） |
| 7 | SQL\_NTH | INTEGER | SQL 语句段号（从 0 开始） |
| 8 | HASH | VARBINARY(8) | SQL 语句的哈希节点地址 |
| 9 | LINK\_ADDR | VARBINARY(8) | 下一个 SQL 语句地址 |
| 10 | SQL\_TEXT\_ID | VARCHAR(13) | SQL 语句对应的固定散列字符，用于标记 |
| 11 | USER\_ID | INTEGER | 用户 ID |
| 12 | SCH\_ID | INTEGER | 模式 ID |

13） **GV$SQLTEXT**

显示全局 SQL 缓冲区中的 SQL 语句的相关信息。

| **序 号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INSTANCE\_NAME | VARCHAR(128) | 实例名 |
| 2 | SQL\_ADDR | VARBINARY(8) | 语句在缓存中的地址 |
| 3 | SQL\_ID | INTEGER | SQL 语句 ID（唯一标识） |
| 4 | N\_EXEC | INTEGER | 语句执行次数 |
| 5 | HASH\_VALUE | INTEGER | 语句 HASH 值 |
| 6 | CMD\_TYPE | VARCHAR(32) | 语句类型（来自语句类型，例如：DRO\_STMT\_CTAB） |
| 7 | SQL\_TEXT | VARCHAR(7168) | SQL 语句内容（如果超过 7168 字符，则分段存储） |
| 8 | SQL\_NTH | INTEGER | SQL 语句段号（从 0 开始） |
| 9 | HASH | VARBINARY(8) | SQL 语句的哈希节点地址 |
| 10 | LINK\_ADDR | VARBINARY(8) | 下一个 SQL 语句地址 |
| 11 | SQL\_TEXT\_ID | VARCHAR(13) | SQL 语句对应的固定散列字符，用于标记 |
| 12 | USER\_ID | INTEGER | 用户 ID |
| 13 | SCH\_ID | INTEGER | 模式 ID |

14） **V$SQL\_PLAN**

显示 SQL 缓冲区中的执行计划的相关信息。在 INI 参数 USE\_PLN\_POOL!=0 时才统计。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PLN\_ADDR | VARBINARY(8) | 计划在缓存中的地址 |
| 2 | HASH\_VALUE | INTEGER | 计划 HASH 值 |
| 3 | SQL\_ID | INTEGER | SQL 语句 ID（唯一标识） |
| 4 | PLN\_TYPE | VARCHAR(16) | 计划类型 |
| 5 | SQLSTR | VARCHAR(1000) | 语句内容 |
| 6 | RT\_METHOD | VARBINARY(8) | 计划的运行时方法 |
| 7 | SVPNT | VARCHAR(128) | 计划的保存点名称 |
| 8 | N\_LIT\_PARAS | INTEGER | 常量参数个数 |
| 9 | N\_CLNT\_PARAS | INTEGER | 客户端绑定参数个数 |
| 10 | N\_COLS | INTEGER | 涉及到的列个数 |
| 11 | SEL\_UPDATABLE | CHAR(1) | 是否为查询更新 |
| 12 | N\_NDCTS | INTEGER | 涉及到的字典对象个数 |
| 13 | N\_SUBPLNS | INTEGER | 子计划个数 |
| 14 | N\_SUBPGS | INTEGER | 子过程个数 |
| 15 | PRE\_COMMIT | CHAR(1) | 执行 DDL 之前先提交事务 |
| 16 | IS\_RECURSIVE | CHAR(1) | 是否为递归调用 |
| 17 | BPARAM\_CAN\_OPT | CHAR(1) | 参数是否可以优化 |
| 18 | NDCT\_VERSION | INTEGER | 字典对象版本号 |
| 19 | CAN\_REUSE | CHAR(1) | 计划是否可重用 |
| 20 | HAS\_SQL | CHAR(1) | 是否有对应的 SQL 语句 |
| 21 | HASH | VARBINARY(8) | 计划哈希节点地址 |
| 22 | SCHID | INTEGER | 模式 ID |
| 23 | USER\_ID | INTEGER | 用户 ID |
| 24 | OBJ\_ID | INTEGER | 对象 ID |
| 25 | RS\_CAN\_CACHE | CHAR(1) | 结果集是否缓存 |
| 26 | RS\_CAN\_CLT\_CACHE | CHAR(1) | 客户端是否缓存结果集 |
| 27 | RS\_MUTEX | VARBINARY(8) | 互斥量地址 |
| 28 | N\_TABLES | INTEGER | 涉及的表个数 |
| 29 | LINK\_ADDR | VARBINARY(8) | 下一个计划地址 |
| 30 | PHD\_TIME | DATETIME(6) | 生成计划时间 |
| 31 | OPTIMIZER | VARCHAR(128) | 优化方式 |
| 32 | TABLEID | VARCHAR(256) | 计划涉及的表的 ID，用空格隔开 |
| 33 | SQLCACHE | BIGINT | 对应 V$CACHESQL 中的 CACHE\_ITEM |
| 34 | RET\_CMD | SMALLINT | 返回响应命令字 |
| 35 | STMT\_TYPE | INTEGER | SQL 语句类型号，具体对应类型名称可查看 V$SQLCOMMAND |
| 36 | MEM\_SIZE | BIGINT | 缓存节点大小，单位为字节数 |
| 37 | RS\_CAN\_CACHED\_IN\_RULE | CHAR(1) | 依据基本规则是否可以缓存结果集（'Y'或'N'），实际是否缓存还受结果集缓存相关参数影响，或者被手工强制设置不缓存 |
| 38 | NLS\_SORT\_TYPE | INTEGER | 执行计划的自然语言的排序方式。0：按默认字符集二进制编码排序；1：按中文拼音排序；2：按中文笔画排序；3：按中文部首排序；4：按泰文排序；5：按韩文排序 |
| 39 | BINDED | CHAR(1) | 用于表示执行计划的绑定情况，'N'：未绑定；'M'：内存中绑定；'P'：持久化绑定；'B'：内存中绑定与持久化绑定同时生效 |
| 40 | SQL\_TEXT\_ID | VARCHAR(13) | 语句固定的散列字符；相同的 SQL 散列字符相同 |

15） **V$MEM\_POOL**

显示所有的内存池信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ADDR | BIGINT | 内存结构地址 |
| 2 | NAME | VARCHAR(128) | 内存池名称 |
| 3 | IS\_SHARED | CHAR(1) | 是否是共享的 |
| 4 | CHK\_MAGIC | CHAR(1) | 是否打开了内存校验 |
| 5 | CHK\_LEAK | CHAR(1) | 是否打开了泄漏检查 |
| 6 | IS\_OVERFLOW | CHAR(1) | 是否已经触发 BAK\_POOL 的分配 |
| 7 | IS\_DSA\_ITEM | CHAR(1) | 是否是 DSA(Dameng Share Area)项目， 目前一律为 N |
| 8 | ORG\_SIZE | BIGINT | 初始大小，单位为字节数 |
| 9 | TOTAL\_SIZE | BIGINT | 当前总大小，单位为字节数 |
| 10 | RESERVED\_SIZE | BIGINT | 当前分配出去的大小，单位为字节数 |
| 11 | DATA\_SIZE | BIGINT | 当前分配出去的数据占用大小，单位为字节数 |
| 12 | EXTEND\_SIZE | BIGINT | 每次扩展的块大小，单位为字节数 |
| 13 | TARGET\_SIZE | BIGINT | 可以扩展到的大小，单位为字节数。当 TARGET\_SIZE 为 0 时，不限制此内存池的扩展；对于共享内存池，即使 TARGET\_SIZE 不为 0，也不限制其扩展，TARGET\_SIZE 用于提示系统尽快把内存占用释放到 TARGET\_SIZE 以下 |
| 14 | EXTEND\_LEN | INTEGER | 扩展链长度（扩展块数量） |
| 15 | N\_ALLOC | BIGINT | 累计分配了几次 |
| 16 | N\_EXTEND\_NORMAL | BIGINT | TARGET 范围内累计扩展次数 |
| 17 | N\_EXTEND\_EXCLUSIVE | BIGINT | 超过 TARGET 累计扩展次数 |
| 18 | N\_FREE | BIGINT | 累计释放次数 |
| 19 | MAX\_EXTEND\_SIZE | BIGINT | 保留字段，始终返回 NULL |
| 20 | MIN\_EXTEND\_SIZE | BIGINT | 保留字段，始终返回 NULL |
| 21 | FILE\_NAME | VARCHAR(256) | 本池创建点所在的源文件名 |
| 22 | FILE\_LINE | INTEGER | 创建点所在的代码行 |
| 23 | CREATOR | INTEGER | 创建者线程号 |
| 24 | EXTEND\_MODE | CHAR(1) | 内存池的扩展模式，O：扩展时从操作系统（OS）申请扩展块；S：扩展时从共享池（Share Pool）申请扩展块 |
| 25 | PEAK\_SIZE | BIGINT | 该内存池使用内存的峰值，单位为字节数 |
| 26 | PARENT | BIGINT | 该父池的内存结构地址 |

16） **V$MEM\_REGINFO**

显示系统当前已分配并未释放的内存信息，当 MEMORY\_LEAK\_CHECK 为 1 时才会在此动态视图注册信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL | VARCHAR(128) | 注册项来源内存池名称 |
| 2 | FNO | INTEGER | 文件编号 |
| 3 | LINENO | INTEGER | 文件中的代码行编号 |
| 4 | REFNUM | INTEGER | 引用次数 |
| 5 | RESERVED\_SIZE | BIGINT | 调用点累计分配未释放的内存量，单位为字节数 |
| 6 | DATA\_SIZE | BIGINT | 调用点累计分配未释放的净数据量，单位为字节数 |
| 7 | FNAME | VARCHAR(256) | 源文件名 |
| 8 | ADDR | BIGINT | POOL 的内存地址 |
| 9 | N\_ENTER | INTEGER | 用于监测该文件/行位置内存申请调用/释放的次数 |

17） **V$GSA**

显示全局 SORT 内存缓冲区的使用情况。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ADDR | BIGINT | 缓冲块的内存地址 |
| 2 | SIZE | BIGINT | 缓冲块大小，单位为字节数 |

18） **V$MEM\_HEAP**

显示系统当前内存堆的信息，仅当系统启动时 MEMORY\_LEAK\_CHECK 为 1 时有效。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ADDR | BIGINT | 内存堆对象的地址 |
| 2 | FILE\_NAME | VARCHAR(256) | 本内存堆创建点所在的源文件名 |
| 3 | FILE\_LINE | INTEGER | 创建点所在的代码行 |
| 4 | DATA\_LEN | BIGINT | 内存堆占用空间大小，单位为字节 |
| 5 | BLK\_LEN | INTEGER | 内存堆包含的 block 个数 |

19） **V$LARGE\_MEM\_SQLS**

最近 1000 条使用大内存的 sql 语句。一条 sql 语句使用的内存值超过 ini 参数 LARGE\_MEM\_THRESHOLD，就认为使用了大内存。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SESS\_ID | BIGINT | 会话 ID，系统内部标识 |
| 2 | SQL\_ID | INTEGER | SQL 语句 ID |
| 3 | SQL\_TEXT | VARCHAR(1024) | SQL 文本。最多选取 1024 个字符。如果 SQL 语句大于 1024 个字符，则从 SQL 语句的首尾各取一半，中间部分省略 |
| 4 | MEM\_USED\_BY\_K | BIGINT | 使用的内存数，单位 KB |
| 5 | FINISH\_TIME | DATETIME(0) | 执行结束时间 |
| 6 | N\_RUNS | INTEGER | 执行次数 |
| 7 | SEQNO | INTEGER | 编号 |
| 8 | TRX\_ID | BIGINT | 事务号 |
| 9 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |

20） **V$SYSTEM\_LARGE\_MEM\_SQLS**

系统中使用大内存最多的 20 条 sql 语句。字段定义与 v$large\_mem\_sqls 相同。

21） **V$SCP\_CACHE**

显示缓存池信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SCP\_ADDR | VARBINARY(8) | 缓存池地址 |
| 2 | PLN\_CNT | BIGINT | 计划缓存总数 |
| 3 | RS\_CNT | BIGINT | 结果集缓存总数 |
| 4 | SQL\_CNT | BIGINT | SQL 缓存总数 |
| 5 | PKGINFO\_CNT | BIGINT | 包信息缓存总数 |
| 6 | LRU\_SIZE | INTEGER | LRU 链表的节点数 |
| 7 | DISABLE\_SIZE | INTEGER | 失效缓存节点数 |
| 8 | DISCARD | BIGINT | 缓存对象淘汰次数 |
| 9 | DISCARD\_MEM | BIGINT | 缓存对象淘汰的大小，单位 BYTE |
| 10 | N\_ADD\_FAIL | BIGINT | 添加缓存失败次数 |

22） **V$DB\_SYSPRIV\_CACHE**

系统权限缓存信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 字典对象的 ID |
| 2 | UID | INTEGER | 用户 ID |
| 3 | DDL\_PRIV | VARBINARY(512) | DDL 权限 |
| 4 | DML\_PRIV | VARBINARY(16) | DML 权限，由 4 个 INT 值组成。 0~3 字节：is\_any&is\_tab 4~7 字节：!is\_any&is\_tab 8~11 字节：is\_any&!is\_tab 12~15 字节：!is\_any&!is\_tab |

23） **V$DB\_OBJPRIV\_CACHE**

对象权限缓存信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 字典对象的 ID |
| 2 | UID | INTEGER | 用户 ID |
| 3 | COLID | INTEGER | 列 ID |
| 4 | OBJ\_PRIV | VARBINARY(8) | 对象权限 |
| 5 | COL\_PRIV | VARBINARY(8) | 列权限 |

24） **V$SQL\_STAT**

语句级资源监控内容。记录当前正在执行的 SQL 语句的资源开销。需要 ENABLE\_MONITOR=1 才开始监控。针对 63~68 列中的监控项，还需开启参数 MONITOR\_SQL\_EXEC=1、ENABLE\_MONITOR\_DMSQL=1 才开始监控。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SESSID | BIGINT | 会话 ID，系统内部标识 |
| 2 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |
| 3 | SQL\_TXT | VARCHAR(1024) | 语句 |
| 4 | SQL\_ID | INTEGER | SQL 语句 ID |
| 5 | EXEC\_TIME | BIGINT | 以系统时间统计的执行时间，单位毫秒 |
| 6 | PARSE\_CNT | BIGINT | 解析次数 |
| 7 | PARSE\_TIME | BIGINT | 以系统时间统计的解析时间，单位毫秒 |
| 8 | HARD\_PARSE\_CNT | BIGINT | 硬解析次数 |
| 9 | HARD\_PARSE\_TIME | BIGINT | 硬解析时间，单位毫秒 |
| 10 | SEL\_SQL\_CNT | BIGINT | 执行的查询语句总数 |
| 11 | INS\_SQL\_CNT | BIGINT | 执行的插入语句总数 |
| 12 | DEL\_SQL\_CNT | BIGINT | 执行的删除语句总数 |
| 13 | UPD\_SQL\_CNT | BIGINT | 执行的更新语句总数 |
| 14 | DDL\_SQL\_CNT | BIGINT | 执行的 DDL 语句总数 |
| 15 | SEL\_IN\_PL\_CNT | BIGINT | 执行的语句块中的查询语句总数 |
| 16 | INS\_IN\_PL\_CNT | BIGINT | 执行的语句块中的插入语句总数 |
| 17 | DEL\_IN\_PL\_CNT | BIGINT | 执行的语句块中的删除语句总数 |
| 18 | UPD\_IN\_PL\_CNT | BIGINT | 执行的语句块中的更新语句总数 |
| 19 | DYN\_EXEC\_CNT | BIGINT | 执行的语句块中的动态执行语句总数 |
| 20 | DDL\_EVT\_TRG\_CNT | BIGINT | DDL 事件触发器触发次数 |
| 21 | STMT\_BF\_TRG\_CNT | BIGINT | 语句级 BEFORE 触发器触发次数 |
| 22 | STMT\_AF\_TRG\_CNT | BIGINT | 语句级 AFTER 触发器触发次数 |
| 23 | ROW\_BF\_TRG\_CNT | BIGINT | 元组级 BEFORE 触发器触发次数 |
| 24 | ROW\_AF\_TRG\_CNT | BIGINT | 元组级 AFTER 触发器触发次数 |
| 25 | INSTEAD\_OF\_TRG\_CNT | BIGINT | INSTEAD OF 触发器触发次数 |
| 26 | OPTIMIZED\_SORT\_CNT | BIGINT | 最优排序次数 |
| 27 | ONE\_WAY\_SORT\_CNT | BIGINT | 单路排序次数 |
| 28 | MULTI\_WAY\_SORT\_CNT | BIGINT | 多路排序次数 |
| 29 | RUNTIME\_OBJ\_ALLOC\_CNT | BIGINT | 运行时对象创建次数 |
| 30 | RUNTIME\_OBJ\_SIZE\_CNT | BIGINT | 运行时对象占用空间大小，单位 BYTE |
| 31 | RUNTIME\_OBJ\_RECLAIM\_CNT | BIGINT | 运行时对象回收次数 |
| 32 | LONG\_ROW\_CVT\_CNT | BIGINT | 超长记录字段压缩次数 |
| 33 | LOGIC\_READ\_CNT | BIGINT | 逻辑读页次数 |
| 34 | PHY\_READ\_CNT | BIGINT | 物理读页次数 |
| 35 | PHY\_MULTI\_READ\_CNT | BIGINT | 物理读多页次数 |
| 36 | RECYCLE\_LOGIC\_READ\_CNT | BIGINT | 临时表空间逻辑读次数 |
| 37 | RECYCLE\_PHY\_READ\_CNT | BIGINT | 临时表空间物理读次数 |
| 38 | HBUF\_LOGIC\_READ\_CNT | BIGINT | HBUF 逻辑读次数 |
| 39 | HBUF\_PHY\_READ\_CNT | BIGINT | HBUF 物理读次数 |
| 40 | HBUF\_PHY\_WRITE\_CNT | BIGINT | HBUF 物理写次数 |
| 41 | HBUF\_PHY\_READ\_SIZE | BIGINT | HBUF 物理读总大小，单位 BYTE |
| 42 | HBUF\_PHY\_WRITE\_SIZE | BIGINT | HBUF 物理写总大小，单位 BYTE |
| 43 | UNDO\_PAGE\_CHANGES\_CNT | BIGINT | undo 页变化次数 |
| 44 | RECYCLE\_PAGE\_CHANGES\_CNT | BIGINT | 临时页变化次数 |
| 45 | DATA\_PAGE\_CHANGES\_CNT | BIGINT | 数据页变化次数 |
| 46 | IO\_WAIT\_TIME | BIGINT | I/O 等待时间，单位毫秒 |
| 47 | TAB\_SCAN\_CNT | BIGINT | 统计全表扫描次数 |
| 48 | HASH\_JOIN\_CNT | BIGINT | 统计哈希连接的次数 |
| 49 | BTR\_SPLIT\_CNT | BIGINT | B 树分裂次数 |
| 50 | BTR\_PAGE\_DISCARD\_CNT | BIGINT | 数据页丢弃次数 |
| 51 | BTR\_LEVEL\_DISCARD\_CNT | BIGINT | B 树层丢弃次数 |
| 52 | BTR\_LEFT\_TRY\_CNT | BIGINT | B 树左移次数 |
| 53 | BTR\_DIRECT\_UPDATE\_CNT | BIGINT | B 树直接更新次数 |
| 54 | BTR\_INSDEL\_UPDATE\_CNT | BIGINT | B 树插入删除更新次数 |
| 55 | BTR\_UPDATE\_2ND\_CONFLICT\_CNT | BIGINT | 二级索引更新冲突次数 |
| 56 | UPDATE\_MVCC\_RETRY\_CNT | BIGINT | 多版本更新重试次数 |
| 57 | DELETE\_MVCC\_RETRY\_CNT | BIGINT | 多版本删除重试次数 |
| 58 | MAX\_MEM\_USED | BIGINT | 内存使用峰值，单位 KB |
| 59 | VIS\_RECS\_CNT | BIGINT | 可见数据获取次数 |
| 60 | VIS\_RECS\_TIME | BIGINT | 可见数据获取时间，单位毫秒 |
| 61 | INVIS\_RECS\_CNT | BIGINT | 不可见数据获取次数 |
| 62 | INVIS\_RECS\_TIME | BIGINT | 不可见数据获取时间，单位毫秒 |
| 63 | NET\_BYTES\_RECV | BIGINT | 从客户端接收的数据字节数 |
| 64 | NET\_BYTES\_SEND | BIGINT | 向客户端发送的数据字节数 |
| 65 | NET\_ROUNDTRIPS | BIGINT | 和客户端之间的数据往返传送次数 |
| 66 | REDO\_SIZE | BIGINT | REDO 日志大小，单位字节 |
| 67 | PARSE\_ELAPSD | BIGINT | 以 CPU 时钟统计的解析时间，单位毫秒 |
| 68 | EXEC\_CPU | BIGINT | 以 CPU 时钟统计的执行时间，单位毫秒 |
| 69 | PLN\_ADDR | BIGINT | 执行计划地址，与 V$CACHEPLN 的 CACHE\_ITEM 列对应 |
| 70 | START\_TIME | DATETIME(6) | SQL 执行的开始时间 |
| 71 | END\_TIME | DATETIME(6) | SQL 执行的结束时间 |
| 72 | BTR\_SPLIT\_OPT\_CNT | BIGINT | BTR\_SPLIT\_MODE 开启插入封锁优化时，B 树分裂优化成功的次数 |
| 73 | BTR\_SPLIT\_OPT\_FAIL\_CNT | BIGINT | BTR\_SPLIT\_MODE 开启插入封锁优化时，B 树分裂优化失败的次数 |
| 74 | EXEC\_ID | BIGINT | SQL 执行 ID，取值为-1 表示没有到计划执行阶段 |
| 75 | SQL\_TEXT\_ID | VARCHAR(13) | 语句固定的散列字符；相同的 SQL 散列字符相同 |
| 76 | BLTR\_WAIT\_SPLIT\_CNT | BIGINT | 保留列，暂未公开 |
| 77 | DIRECT\_PHY\_READ\_CNT | BIGINT | 保留列，暂未公开 |
| 78 | PROC\_EXEC\_TIME | BIGINT | 过程执行时间，单位毫秒 |
| 79 | LOCK\_WAIT\_TIME | BIGINT | 封锁等待时间，单位毫秒 |
| 80 | RS\_COUNT | BIGINT | 结果集返回的行数 |
| 81 | DB\_TIME | BIGINT | 语句的 DB TIME，单位毫秒 |

25） **V$SQL\_STAT\_HISTORY**

语句级资源监控内容。记录历史 SQL 语句（不含存储过程中的 SQL）执行的资源开销。需要 ENABLE\_MONITOR=1 才开始监控。单机最大行数为 10000。

其中 5~62、64 和 66 列中的监控项，可以通过 SP\_SET\_SQL\_STAT\_THRESHOLD()设置监控阈值，当资源超过设置的阈值才开始统计并记录该项，具体使用参考《DM8\_SQL 语言使用手册》。当前已设置的监控阈值内容，可以通过查询视图 V$SQL\_STAT\_THRESHOLD 进行查看。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1~81 | 1~81 行和 V$SQL\_STAT 结构相同。请参考 V$SQL\_STAT | …… | …… |

26） **V$HLDR\_TABLE**

记录当前系统中所有 HLDR 使用 HLDR\_BUF 的情况。

| 序号 | 列 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| 1 | TABLE\_ID | INTEGER | 装载表 ID |
| 2 | N\_ALLOC | INTEGER | 申请 HLDR\_BUF 的次数 |
| 3 | N\_FAILl | INTEGER | 申请 HLDR\_BUF 失败的次数 |
| 4 | N\_WAIT | INTEGER | 申请 HLDR\_BUF 时等待的次数 |
| 5 | WAIT\_TIME | BIGINT | 申请 HLDR\_BUF 等待的总时长 |
| 6 | N\_BUF | INTEGER | 申请的 HLDR\_BUF 的个数 |

27） **V$HBUF\_STAT**

显示当前系统中 HUGE BUFFER 的使用信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SIZE\_LEVEL | INTEGER | 空间大小的层级，按照页数是 2 的幂数划分层级 |
| 2 | MIN\_PAGE\_NUM | INTEGER | 当前层级理论上的最小页数 |
| 3 | MAX\_PAGE\_NUM | INTEGER | 当前层级理论上的最大页数 |
| 4 | N\_FREE\_FRAGMENTS | INTEGER | 当前层级 HUGE BUFFER 中空闲碎片的个数 |
| 5 | N\_FREE\_PAGES | INTEGER | 当前层级所有空闲碎片的页数之和 |
| 6 | N\_MEM\_USE\_PAGES | INTEGER | 内存一次使用的空间大小属于当前层级的页数总和 |
| 7 | N\_MEM\_ALLOC | BIGINT | 内存一次申请的空间大小属于当前层级的次数 |
| 8 | N\_MEM\_RELEASE | BIGINT | 内存一次释放的空间大小属于当前层级的次数 |
| 9 | N\_CTL\_USE\_PAGES | INTEGER | HUGE BUFFER 一次使用的空间大小属于当前层级的页数总和 |
| 10 | N\_CTL\_ALLOC | BIGINT | HUGE BUFFER 一次申请的空间大小属于当前层级的次数 |
| 11 | N\_CTL\_RELEASE | BIGINT | HUGE BUFFER 一次释放的空间大小属于当前层级的次数 |
| 12 | N\_CTL\_RESERVE | BIGINT | HUGE BUFFER 一次 RESERVE 的空间大小属于当前层级的次数 |

28） **V$CACHE\_ID**

显示缓存中可分配 ID 的相关信息，仅当 INI 参数 ID\_RECYCLE\_FLAG 为 1 时有效。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(100) | 对象类型名 |
| 2 | MIN\_ID | INTEGER | 最小可用 ID 值 |
| 3 | MAX\_ID | INTEGER | 最大可用 ID 值 |
| 4 | COUNT | INTEGER | 可用 ID 数量 |

29） **V$IDBITMAP**

显示系统中已分配字典 ID 的位图项信息，仅当 INI 参数 ID\_RECYCLE\_FLAG 为 1 时有效。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NTH | INTEGER | 序号 |
| 2 | DICT\_TYPE | VARCHAR(32) | 对应字典类型 |
| 3 | MIN\_ID | INTEGER | 起始 ID |
| 4 | MAX\_ID | INTEGER | 最大 ID |
| 5 | REAL\_MAX\_ID | INTEGER | 已分配的最大 ID |
| 6 | N\_ALLOC | INTEGER | 已分配 ID 数 |
| 7 | SCAN\_START | INTEGER | 下次分配时起始扫描 ID |

30） **V$IDPURGE**

显示系统中已登记待延迟处理的事务 ID 信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TRID | BIGINT | 事务号 |
| 2 | ID\_NUM | INTEGER | 登记的字典 ID 数目 |
| 3 | ARR\_CNT | INTEGER | 登记数组项数 |

31） **V$HOTPAGE**

显示缓存中的热点页信息。输出系统缓存中访问最频繁的前 1000 页信息，按 ACCESS\_CNT 排序。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TS\_ID | INTEGER | 所属的表空间 ID |
| 2 | FILE\_ID | INTEGER | 数据库文件 ID |
| 3 | PAGE\_NO | INTEGER | 页号 |
| 4 | ACCESS\_CNT | BIGINT | 自启动以后页的访问计数 |
| 5 | INDEXID | INTEGER | 索引 ID, 仅对索引/数据页有意义 |
| 6 | PAGETYPE | VARCHAR(16) | 页类型，取值如下：   PSEG\_MGR：回滚记录管理页   BLOB\_REC\_CTL：大字段记录管理页   BLOB\_REC：大字段页   MTAB\_PAGE：临时数据页   BLOB\_PAGE：大字段页   PSEG\_SLOT\_CTL：回滚段管理页   PSEG\_UREC：回滚记录页   INDEX\_INNER：索引内节点页   INDEX\_LEAF：索引叶节点页   DATA\_INNER：数据内节点页   DATA\_LEAF：数据页节点页   TS\_HDR：表空间/文件头页   INODE：段描述页   BTR\_CONTROL：B 树控制页   EXTENT\_DESC：簇描述页   OTHER：其他页 |
| 7 | FIRST\_LSN | BIGINT | 缓存中首次修改时的 LSN，0 表示没有修改过 |
| 8 | LSN | BIGINT | 当前的 LSN，0 表示没有被修改过 |
| 9 | POOL\_ID | INTEGER | 页所在的缓存池编号 |

32） **V$OS\_MEM\_INFO**

显示操作系统内存的分配释放信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | N\_2\_LOG | INTEGER | 2 的 n 次方的 n |
| 2 | N\_ALLOC | BIGINT | 分配的次数 |
| 3 | N\_FREE | BIGINT | 释放的次数 |

33） **V$XBOX**

获取并显示系统中所有 XBOX 的槽信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | XBOX ID |
| 2 | SLOT\_NO | INTEGER | XBOX 内的槽号 |
| 3 | LETTER\_NUM | INTEGER | 槽内收到的邮件数 |
| 4 | FILE\_NAME | VARCHAR(256) | 创建 XBOX 的文件名 |
| 5 | FILE\_LINE | INTEGER | 创建 XBOX 的文件行号 |
| 6 | EID | BIGINT | 使用 XBOX 的 ESESS\_ID |
| 7 | SIO | INTEGER | 使用 XBOX 的 ERECV 操作符在计划中的行序号 |
| 8 | STASK\_NO | INTEGER | 使用 XBOX 的 ERECV 操作符在计划中的子任务号 |
| 9 | NO\_IN\_STASK | INTEGER | 使用 XBOX 的 ERECV 操作符在子任务中的序号 |
| 10 | DUMP\_LEN\_BYTES | BIGINT | XBOX 上使用临时文件保存的邮件总量，单位 BYTE |
| 11 | LONG\_BYTES | BIGINT | 槽内缓存的大于 32KB 的消息空间大小 |
| 12 | SHORT\_NUM | INTEGER | 槽内缓存的 1KB 大小的消息数 |
| 13 | MIDDLE\_NUM | INTEGER | 槽内缓存的 32KB 大小的消息数 |
| 14 | LONG\_NUM | INTEGER | 槽内缓存的大于 32KB 大小的消息数 |
| 15 | DUMP\_NUM | INTEGER | 槽内缓存的需转储的消息数 |

34） **V$PREBUILD\_PLNS**

此视图获取并显示计划缓存池中所有预生成计划信息，在 ini 参数 USE\_PLN\_POOL!=0 且 ENABLE\_PLN\_PRESEARCH=1 时，才有预生成计划。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SCHID | INTEGER | 预生成计划模式 ID |
| 2 | UID | INTEGER | 预生成计划用户 ID |
| 3 | SQLSTR | VARCHAR(4096) | 预生成计划 SQL 语句内容 |
| 4 | OBJID | INTEGER | 若预生成计划是过程子计划，其对象 ID |
| 5 | N\_WAIT | INTEGER | 相同 SQL 正在等待的线程数 |
| 6 | THRD\_ID | INTEGER | 创建预生成计划的线程 ID |
| 7 | MPP\_LOGIN\_TYPE | INTEGER | 会话 MPP 登录类型，0：全局登录；1：本地登录，限制模式；2：本地登录，非限制模式，可以进行 DDL 操作 |
| 8 | MPP\_DDL\_FLAG | CHAR(1) | 会话 MPP 下 DDL 标识 |
| 9 | NLS\_SORT\_TYPE | INTEGER | 会话执行计划的自然语言的排序方式 |
| 10 | CASE\_SENSITIVE | INTEGER | 会话标识符大小写是否敏感 |
| 11 | PARSE\_TYPE | INTEGER | 会话解析器类型 |
| 12 | PARALLEL\_POLICY | INTEGER | 会话默认并行任务个数 |
| 13 | LANGUAGE | INTEGER | 会话语言 |

35） **V$NOT\_FREED\_CACHEITEMS**

此视图显示不在缓冲池中且未释放的缓存项信息，便于定位内存泄漏。在 INI 参数 CACHEITEM\_ALLOC\_MONITOR 非 0 时才统计对应的未释放缓存项。

其中 HEAP\_ADDR 列即为视图 V$MEM\_HEAP 的 ADDR 列，结合本视图可以查看计划堆的相关信息，如堆的创建文件名、创建文件行等，方便定位未释放计划的来源。计划、结果集的 SQLSTR 列均为其对应的 SQL 语句，包信息的 SQLSTR 列为其包名。

存在使用注意事项如下：

1. 此动态性能视图的主要目的为便于定位内存泄漏位置来确定泄漏原因，INI 参数 CACHEITEM\_ALLOC\_MONITOR 默认为 0，不开启统计功能。当 SQL 缓冲区有内存膨胀等异常现象时，若用户怀疑产生了内存泄漏，可以动态打开 CACHEITEM\_ALLOC\_MONITOR 参数来监控后续加入的缓存项，打开参数前已生成的缓存项无法记录。当查看完相关信息后，需要及时关闭 CACHEITEM\_ALLOC\_MONITOR 参数，避免影响性能；关闭参数后，将不再记录后续缓存项，当前的记录会随缓存项释放自然淘汰。
2. 由于一般情况下，内存泄漏最有可能由计划缓存引起，建议将 INI 参数 CACHEITEM\_ALLOC\_MONITOR 设置为 1 或 3，用于收集监控不在缓冲池中未释放的计划缓存、包信息。因为 SQL 语句缓存一定加入缓冲池，所以不必记录。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ADDRESS | BIGINT | 未释放的缓存项的地址 |
| 2 | TYPE$ | VARCHAR(10) | 未释放的缓存项的类型：计划（PLN），结果集（RS），包信息（PKG\_INFO） |
| 3 | IN\_POOL | CHAR(1) | 未释放缓存项是否在 SQL 缓冲区中 |
| 4 | DISABLED | CHAR(1) | 未释放缓存项是否失效 |
| 5 | HEAP\_ADDR | BIGINT | 未释放缓存项堆地址，即 V$MEM\_HEAP 的 ADDR |
| 6 | SQLSTR | VARCHAR(4096) | 未释放缓存项的 SQL 语句/包名 |
| 7 | MEM\_SIZE | BIGINT | 未释放缓存项的缓存节点大小，单位为字节数 |

**36）** **V$MEM\_POOL\_EXTEND\_INFO**

此视图显示内存池的扩展信息。视图中的每一行数据表示内存池中的一个扩展大块的信息。扩展大块可以进一步划分为扩展小块，扩展小块的信息请通过视图 V$MEM\_POOL\_EXTEND\_BLOCK\_INFO 获取。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_NAME | VARCHAR(33) | 内存池名 |
| 2 | POOL\_ADDR | BIGINT | 内存池地址 |
| 3 | NTH | INTEGER | 扩展大块的序号 |
| 4 | SIZE | BIGINT | 扩展大块的总大小，单位字节 |
| 5 | USED\_SIZE | BIGINT | 扩展大块的已使用的大小，单位字节 |
| 6 | ADDR | VARBINARY(8) | 扩展大块的地址 |
| 7 | BLOCK\_COUNT | INTEGER | 扩展大块包含的扩展小块的数量 |
| 8 | USED\_BLOCK | INTEGER | 扩展大块包含的已使用扩展小块的数量 |

**37）** **V$MEM\_POOL\_EXTEND\_BLOCK\_INFO**

此视图显示内存池的各个扩展块的具体信息。视图中的每一行数据表示内存池的一个扩展大块的其中一个扩展小块的信息。

支持此动态视图的主要目的是便于用户定位内存中未释放的扩展内存位置，来确定扩展内存未释放原因。

查询该视图时，一定要使用带 WHERE 条件的 SQL 语句，并且同时指定 POOL\_ADDR 和 NTH，且 WHERE 条件必须是等值条件。例如：SELECT \* FROM V$MEM\_POOL\_EXTEND\_BLOCK\_INFO WHERE POOL\_ADDR=197578644 AND NTH=1;

其中 POOL\_ADDR 可通过视图 V$MEM\_POOL\_EXTEND\_INFO 获取。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_NAME | VARCHAR(33) | 内存池名 |
| 2 | POOL\_ADDR | BIGINT | 内存池地址 |
| 3 | NTH | INTEGER | 扩展大块的序号 |
| 4 | EXTEND\_SIZE | BIGINT | 扩展大块的总大小，单位字节 |
| 5 | BLOCK\_SIZE | BIGINT | 扩展小块的大小，单位字节 |
| 6 | BLOCK\_ADDR | VARBINARY(8) | 扩展小块的地址 |
| 7 | IS\_USED | CHAR | 扩展小块的是否正在被使用 |
| 8 | FILE\_NAME | VARCHAR(256) | 使用该扩展小块的文件名 |
| 9 | FILE\_LINE | INTEGER | 使用该扩展小块的文件行号 |

**38）V$MEM\_FREE\_LIST**

此视图显示系统当前空闲链表和空闲对象的信息。

可以通过系统过程 SP\_CLEAR\_MEM\_FREE\_LIST 清理指定模块的可清理的空闲对象，或清理所有模块的可清理的空闲对象。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | MODULE\_NAME | VARCHAR(128) | 空闲链表所属模块名 |
| 2 | FREE\_OBJ\_COUNT | INT | 空闲对象数目 |

**39) V$PAGE\_SPACE\_INFO**

此视图用于记录系统函数 SF\_GET\_TABLE\_FRAG\_RATE 中查询的页的空间信息，系统函数 SF\_GET\_TABLE\_FRAG\_RATE 的具体介绍可以查看《DM8\_SQL 语言使用手册》。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TS\_ID | INTEGER | 所属的表空间 ID |
| 2 | FILE\_ID | INTEGER | 数据库文件 ID |
| 3 | PAGE\_NO | INTEGER | 页号 |
| 4 | REC\_NUM | INTEGER | 物理记录数 |
| 5 | DELETED\_REC\_NUM | INTEGER | 删除的物理记录数 |
| 6 | USED\_SPACE | INTEGER | 已使用空间，单位 BYTE |
| 7 | FREE\_SPACE | INTEGER | 空闲空间，单位 BYTE |
| 8 | FRAG\_RATE | INTEGER | 空间占有率，单位百分比 |

#### 2\. 段簇页

1） **V$SEGMENT\_INFOS**

显示所有的段信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TS\_ID | INTEGER | 表空间 ID |
| 2 | SEG\_ID | INTEGER | 段 ID |
| 3 | TYPE | VARCHAR(256) | 段的类型（INNER 表示内节点段，LEAF 表示叶子节点段，LIST 表示堆表段，BLOB 表示 BLOB 段，SEQ 表示序列段，REP 表示复制段） |
| 4 | OBJ\_ID | INTEGER | 若段为内节点段或叶子节点段，则为索引 ID；若为 BLOB 段，则为 BLOB 所在的表 ID |
| 5 | INODE\_FILE\_ID | INTEGER | 段的 inode 所在的页的文件号 |
| 6 | INODE\_PAGE\_NO | INTEGER | 段的 inode 所在的页的页号 |
| 7 | INODE\_OFFSET | INTEGER | 段的 inode 所在的页的页内的偏移 |
| 8 | N\_FULL\_EXTENT | INTEGER | 段中的满簇数 |
| 9 | N\_FREE\_EXTENT | INTEGER | 段中的空闲簇数 |
| 10 | N\_FRAG\_EXTENT | INTEGER | 段中的半满簇数 |
| 11 | N\_FRAG\_PAGE | INTEGER | 段中的半满簇中总页数，为估算值 |

**2）** **V$EXTENTS**

显示所有的簇信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TS\_ID | INTEGER | 表空间 ID |
| 2 | FILE\_ID | INTEGER | 文件 ID |
| 3 | SEG\_ID | INTEGER | 段 ID |
| 4 | EXTENT\_ID | INTEGER | 簇 ID |
| 5 | STATE | VARCHAR(8) | 簇状态，其中 FULL 代表全满簇，FRAG 代表半满簇，FREE 代表空闲簇，NOUSE 代表未使用簇 |
| 6 | USED | INTEGER | 簇中已分配数据页个数 |

3） **V$SEGMENTINFO**

索引叶子段信息视图。查询该视图时，一定要带 WHERE 条件，并且必须是等值条件。同时，查询条件必须且只能指定 1 个，且只能是该视图的首列，即 INDEX\_ID。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INDEX\_ID | INTEGER | 索引 ID |
| 2 | SEG\_ID | INTEGER | 段 ID |
| 3 | LOGIC\_PAGE\_NO | INTEGER | 逻辑页号 |
| 4 | PHY\_PAGE\_NO | INTEGER | 物理页号 |
| 5 | PHY\_FIRST\_PAGE\_IN\_EXTENT | INTEGER | 物理页所属的 extent 的第一个物理页 |
| 6 | FIL\_ID | INTEGER | 文件 ID |
| 7 | USE\_BYTES | BIGINT | 已使用的字节数 |
| 8 | FREE\_BYTES | BIGINT | 空闲的字节数 |

4） **V$BTREE\_INNER\_PAGES/V$BTREE\_LEAF\_PAGES**

索引的叶子段/内节点段的页信息视图。查询该视图时，一定要带 WHERE 条件，并且必须是等值条件。同时，查询条件必须且只能指定 1 个，且只能是该视图的首列，即 INDEX\_ID。如：select \* from v$btree\_leaf\_pages where index\_id =\*id\*;（此处\*id\*表示需要根据实际情况替换为指定的索引 ID 值）

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INDEX\_ID | INTEGER | 索引 ID |
| 2 | LEVEL | INTEGER | 页所在的层数 |
| 3 | GROUP\_ID | INTEGER | 页的表空间号 |
| 4 | FILE\_ID | INTEGER | 页的文件号 |
| 5 | PAGE\_NO | INTEGER | 页的页号 |
| 6 | PAGE\_LSN | BIGINT | 页的版本号 |
| 7 | N\_REC | INTEGER | 页的记录数 |

注意：在 V$BTREE\_INNER\_PAGES 视图中，索引 BTREE 的控制页的 level 指定为-1。

5） **V$LOB\_SEG**

用于查看各表大字段的段首页中记录的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SEG\_ID | INTEGER | 段 ID |
| 2 | TAB\_ID | INTEGER | 表 ID |
| 3 | USER\_ID | INTEGER | 用户 ID |
| 4 | N\_EXTENT | BIGINT | 占用簇的个数 |
| 5 | N\_PAGE | BIGINT | 空闲页的个数 |

6） **V$RESOURCE\_LIMIT**

显示表的空间限制信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 表名称 |
| 2 | ID | INTEGER | 表 ID |
| 3 | TYPE | VARCHAR(6) | 表类型 |
| 4 | SPACE\_LIMIT | INTEGER | 空间限制大小，以页为单位 |
| 5 | SPACE\_USED | BIGINT | 空间实际使用大小，以页为单位 |

7） **V$SEGMENT\_PAGES**

段中数据页的信息视图。查询该视图时，一定要带 WHERE 条件并且同时指定 GROUP\_ID 和 SEG\_ID，并且必须是等值条件。例如：select \* from v$segment\_pages where group\_id=1 and seg\_id = 200;

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | GROUP\_ID | INTEGER | 表空间 ID |
| 2 | SEG\_ID | INTEGER | 段编号 |
| 3 | FILE\_ID | INTEGER | 页的文件号 |
| 4 | PAGE\_NO | INTEGER | 页的页号 |

8） **V$PSEG\_SYS**

显示当前回滚段信息。

| 序号 | 列 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| 1 | N\_ITEM | INTEGER | 系统中存在回滚项目的个数 |
| 2 | EXTENT\_SIZE | INTEGER | 每次新申请的回滚页数目 |
| 3 | ALLOC\_PAGES | BIGINT | 回滚页分配的空间大小，单位页数 |
| 4 | EXTEND\_NUM | BIGINT | 回滚页分配的簇大小，单位页数 |
| 5 | RECLAIM\_PAGES | BIGINT | 回滚段重新回收的页数 |
| 6 | TAB\_ITEMS | BIGINT | 回滚段缓存表的个数（有 storage 选项不计） |
| 7 | TAB\_HASH\_SIZE | BIGINT | 回滚段缓存的 HASH 表中节点的个数 |
| 8 | OBJ\_COUNT | BIGINT | purge 涉及对象的个数 |
| 9 | OBJ\_HASH\_SIZE | BIGINT | purge 涉及对象的 HASH SIZE（哈希表中元素个数） |

9） **V$PSEG\_ITEMS**

显示回滚系统中当前回滚项信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NTH | INTEGER | ITEM 序号 |
| 2 | N\_PAGES | INTEGER | 回滚页数 |
| 3 | N\_EXTEND | INTEGER | 扩展回滚段次数 |
| 4 | N\_PURGED\_PAGES | INTEGER | 已 PURGE 的页数 |
| 5 | N\_USED\_PAGES | INTEGER | 正在使用的页数 |
| 6 | N\_UREC\_BYTES | BIGINT | 生成回滚记录的总字节数 |
| 7 | N\_COMMIT\_TRX | INTEGER | 已经提交未 PURGE 的事务数 |
| 8 | RESERVE\_TIME | INTEGER | 事务提交后，最长的保留时间，单位秒 |
| 9 | STACK\_SIZE | INTEGER | 空闲回滚页堆栈空间大小，单位页数 |
| 10 | STACK\_SP | INTEGER | 空闲回滚页堆栈中空闲页数 |
| 11 | MAX\_COMMIT\_TRX | INTEGER | 已提交未 PURGE 的最大事务数 |
| 12 | N\_FREE\_NODE | INTEGER | 提交队列的空闲个数 |
| 13 | N\_QUEUE\_ITEM | INTEGER | 队列项的个数，每个项管理一组提交队列 |
| 14 | FIRST\_COMMIT\_TIME | INTEGER | 第一个提交事务的时间到当前时间的间隔，单位：秒 |
| 15 | N\_PURGING\_TRX | INTEGER | 正在 PURGE 的事务数 |
| 16 | N\_TRX | BIGINT | 申请 ITEM 对应的事务数 |
| 17 | TUNED\_UNDO\_RETENTION | DOUBLE | 调整后的回滚页保留时长，单位秒 |
| 18 | N\_PURGE\_DEL\_PAGE\_DIRECT | BIGINT | PURGE 时根据记录地址直接数据页内定位的次数 |
| 19 | N\_PURGE\_DEL\_PAGE\_SEARCH | BIGINT | PURGE 时根据记录地址在数据页内查找的次数 |
| 20 | N\_PURGE\_DEL\_BTR\_SEARCH | BIGINT | PURGE 时通过 B 树进行查找的次数 |

10） **V$PSEG\_COMMIT\_TRX**

显示回滚项中已提交但未 PURGE 的事务信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ITEM\_NTH | INTEGER | 隶属回滚项的序号 |
| 2 | TRX\_ID | BIGINT | 事务 ID |
| 3 | CMT\_TIME | TIMESTAMP(6) | 事务提交时间 |
| 4 | FPA\_FILE\_ID | INTEGER | 起始页地址文件号。-1 表示该事务没有涉及回滚记录的删除与更新，在事务提交时会直接释放掉涉及的所有回滚页，并清理事务对应的回滚页统计信息，所以回滚文件号为空 |
| 5 | FPA\_PAGE\_NO | INTEGER | 起始页地址页 ID。-1 表示该事务没有涉及回滚记录的删除与更新，在事务提交时会直接释放掉涉及的所有回滚页，并清理事务对应的回滚页统计信息，所以回滚页为空 |
| 6 | N\_PAGES | INTEGER | 事务实际使用的回滚页数量 |
| 7 | FPA\_OFFSET | INTEGER | 回滚记录在起始页内的起始偏移位置。-1 表示该事务没有修改数据，所以没有回滚记录 |
| 8 | NEED\_PURGE | INTEGER | 是否需要 purge：1 表示需要，0 表示不需要 |
| 9 | CRASH\_FLAG | INTEGER | 是否为故障前提交的事务：1 表示是，0 表示不是 |

11） **V$PURGE**

显示当前 PURGE 回滚段信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | OBJ\_NUM | INTEGER | 待 PURGE 事务个数 |
| 2 | IS\_RUNNING | CHAR(1) | 是否有 PURGE 线程正在执行清理回滚段任务(Y/N) |
| 3 | PURG\_FOR\_TS | CHAR(1) | 是否正在 PURGE 表空间（Y/N） |

12） **V$PURGE\_PSEG\_OBJ**

显示 PURGE 系统中，待 PURGE 的所有 PSEG 对象信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TRX\_ID | BIGINT | 事务 ID |
| 2 | NEED\_PURGE | CHAR(1) | 是否需要 PURGE（Y/N） |
| 3 | TAB\_NUM | INTEGER | 涉及表数 |

13） **V$PURGE\_PSEG\_TAB**

显示待 PURGE 表信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TRX\_ID | BIGINT | 事务 ID |
| 2 | TAB\_ID | INTEGER | 表 ID |
| 3 | GROUP\_ID | INTEGER | 控制页所在表空间 ID |
| 4 | FILE\_ID | INTEGER | 控制页文件 ID |
| 5 | PAGE\_NO | INTEGER | 控制页编号 |
| 6 | TAB\_TYPE | INTEGER | 表类型：0 普通表、1 全局临时表、6 范围分区表主表、7 范围分区表子表、8HASH 分区表主表、9HASH 分区表子表、10 位图连接索引表、11LIST 分区表主表、12LIST 分区表子表、13 外部表、15 DBLINK 远程表、24HUGE 表范围分区表主表、25HUGE 表范围分区表子表、26HUGE 表 HASH 分区表主表、27HUGE 表 HASH 分区表子表、28HUGE 表 LIST 分区表主表、29HUGE 表 LIST 分区表子表、32 位图索引表、33HUGE 表 |
| 7 | ROW\_COUNT | BIGINT | insert/delete 操作影响表行数。每插入一行加 1，每删除一行减 1 |

14） **V$TMP\_FREE\_EXTENTS**

显示开启临时表簇管理优化策略后，存储在全局 FREE\_EXTENTS 堆栈中的空闲簇信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NTH | INTEGER | 堆栈序号 |
| 2 | FREE\_EXTENTS\_NUM | INTEGER | 当前堆栈中保存的空闲簇数目 |
| 3 | GLOBAL\_EXTENT\_SIZE | INTEGER | 一个空闲簇所占用的内存大小，单位 KB |
| 4 | FREE\_EXTENTS\_SIZE | BIGINT | 当前堆栈中保存的空闲簇所占用的内存空间，单位 KB |

**15）V$PURGING\_TRX**

显示当前正在 PURGE 的事务信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ITEM\_NTH | INTEGER | 隶属回滚项的序号 |
| 2 | TRX\_ID | BIGINT | 事务 ID |
| 3 | CMT\_TIME | TIMESTAMP(6) | 事务提交时间 |
| 4 | FPA\_FILE\_ID | INTEGER | 起始页地址文件号。-1 表示该事务没有涉及回滚记录的删除与更新，在事务提交时会直接释放掉涉及的所有回滚页，并清理事务对应的回滚页统计信息，所以回滚文件号为空 |
| 5 | FPA\_PAGE\_NO | INTEGER | 起始页地址页 ID。-1 表示该事务没有涉及回滚记录的删除与更新，在事务提交时会直接释放掉涉及的所有回滚页，并清理事务对应的回滚页统计信息，所以回滚页为空 |
| 6 | N\_PAGES | INTEGER | 事务实际使用的回滚页数量 |
| 7 | CRASH\_FLAG | INTEGER | 是否为故障前提交的事务：1 表示是，0 表示不是 |
| 8 | PURGE\_STIME | TIMESTAMP(6) | 事务开始 purge 的时间 |
| 9 | N\_PAGE\_PURGED | INTEGER | 事务已经 purge 掉的回滚页数量 |

#### 3\. 数据库信息

1） **V$LICENSE**

显示 LICENSE 信息，用来查询当前系统的 LICENSE 信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | LIC\_VERSION | VARCHAR(256) | 许可证版本号 |
| 2 | SERIES\_NO | VARCHAR(256) | LICENSE 文件序列号 |
| 3 | SERVER\_SERIES | VARCHAR(256) | 服务器版本类型。P：单机版、S：标准版、E：企业版、A：安全版、T:可信版、X：定制版 |
| 4 | SERVER\_TYPE | VARCHAR(256) | 服务器发布类型。1：正式版、2：测试版、3：试用版、4：其他 |
| 5 | SERVER\_VER | VARCHAR(256) | 服务器版本号 |
| 6 | EXPIRED\_DATE | DATE | 有效日期 |
| 7 | AUTHORIZED\_CUSTOMER | VARCHAR(256) | 用户名称 |
| 8 | AUTHORIZED\_USER\_NUMBER | BIGINT | 授权用户数 |
| 9 | CONCURRENCY\_USER\_NUMBER | BIGINT | 并发连接数 |
| 10 | MAX\_CPU\_NUM | INTEGER | 最大 CPU 数目 |
| 11 | NOACTIVE\_DEADLINE | DATE | 未激活状态截止日期 |
| 12 | HARDWARE\_ID | VARCHAR(256) | 绑定的硬件编码，根据 HARDWARE\_TYPE 不同，此项内容对应的获取和检测方式不同 |
| 13 | CHECK\_CODE | VARCHAR(16) | 校验码 |
| 14 | PRODUCT\_TYPE | VARCHAR(8) | 产品类型：内容为：DM8/DM7/DM6/DMETLV4/DMETLV3/DMHSV3 |
| 15 | PROJECT\_NAME | VARCHAR(128) | 项目名称 |
| 16 | CPU\_TYPE | VARCHAR(24) | 授权运行的 CPU 类型 |
| 17 | OS\_TYPE | VARCHAR(24) | 授权运行的操作系统 |
| 18 | MAX\_CORE\_NUM | INTEGER | 授权最大 CPU 核个数，0 表示无限制 |
| 19 | HARDWARE\_TYPE | VARCHAR(24) | 硬件绑定类型。1：MAC 地址、 2：cpu id、 3：harddriver id |
| 20 | CLUSTER\_TYPE | VARCHAR(24) | 授权使用的集群类型，格式为字符串“XXXX”，每一位上 0 表示禁止，1 表示授权使用。第 1 个字符：表示数据守护；第 2 个字符：表示 MPP；第 3 个字符：表示读写分离；第 4 个字符：表示 DSC。例如，“0010”表示授权该可作为读写分离集群的节点使用 |
| 21 | DATE\_GEN | DATE | KEY 的生成日期 |
| 22 | SERVER\_SERIES\_NAME | VARCHAR(128) | 定制版版本名称 |
| 23 | TABLE\_RECORD\_NUMBER\_LIMIT | INTEGER | 单表最大数据行数限制，以万为单位，0 表示无限制 |
| 24 | TOTAL\_SPACE\_LIMIT | INTEGER | 数据总空间大小限制，以 GB 为单位，0 表示无限制 |

2） **V$VERSION**

显示版本信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | BANNER | VARCHAR(80) | 版本标识。   DM Database Server 64/空：服务器版本号。其中，64/空表示 64/32 操作系统。   DB Version：数据库版本号。   DMDSC Version：DMDSC 版本号。   Msg Version：服务器通信版本号。   Gsu level(5) cnt：服务器 5 级不兼容修改版本计数 |

3） **GV$VERSION**

显示版本信息，包括其他 raft 节点、实时归档目标、即时归档目标、dsc 其他节点。

| 序号 | 列 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| 1 | INSTANCE\_NAME | VARCHAR(128) | 数据库实例名 |
| 2 | BANNER | VARCHAR(128) | 版本标识。   DM Database Server \[64\]：服务器版本号。   DB Version：库版本号。   DSC Version：DMDSC 版本号。   Msg Version：服务器通信版本号。   Gsu level(5) cnt：服务器 5 级不兼容修改版本计数 |

4） **V$DATAFILE**

显示数据文件信息，不包括 RLOG 表空间信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | GROUP\_ID | INTEGER | 所属的表空间 ID |
| 2 | ID | INTEGER | 数据库文件 ID |
| 3 | PATH | VARCHAR(256) | 数据库文件路径 |
| 4 | CLIENT\_PATH | VARCHAR(256) | 数据库文件路径，专门提供给客户端 |
| 5 | CREATE\_TIME | TIMESTAMP(0) | 数据库文件创建时间 |
| 6 | STATUS$ | TINYINT | 状态，标识数据文件当前的状态，取值 0/1, 取值为 0 表示数据文件状态异常（被删除或者处于恢复中），取值为 1 表示数据文件状态正常   对于 windows 平台，正在使用的文件不支持直接在操作系统中删除，因此 windows 平台下，status 取值恒为 1   对于其他平台，当数据库检查到数据文件被删除或者数据文件正在执行恢复，则 status 取值为 0，否则取值为 1 |
| 7 | RW\_STATUS | TINYINT | 读写状态：1 读，2 写 |
| 8 | LAST\_CKPT\_TIME | DATETIME(0) | 最后一次检查点时间。只对 online 的 DB 做统计，否则就是空 |
| 9 | MODIFY\_TIME | DATETIME(0) | 文件修改时间 |
| 10 | MODIFY\_TRX | BIGINT | 修改事务 |
| 11 | TOTAL\_SIZE | BIGINT | 总大小。单位：页数 |
| 12 | FREE\_SIZE | BIGINT | 未分配的空闲大小，单位：页数 |
| 13 | FREE\_PAGE\_NO | BIGINT | 数据文件中尚未格式化的最小页号。文件系统以簇为单位格式化数据页，数据文件创建时首先格式化第一个簇的数据页，后续分配使用数据页时再继续格式化数据页，数据页一旦被格式化便无法再恢复到未被格式化时的状态 |
| 14 | PAGES\_READ | BIGINT | 累计读页数量 |
| 15 | PAGES\_WRITE | BIGINT | 累计写页数量 |
| 16 | PAGE\_SIZE | INTEGER | 页大小，单位 BYTE |
| 17 | READ\_REQUEST | INTEGER | 累计读请求次数 |
| 18 | WRITE\_REQUEST | INTEGER | 累计写请求次数 |
| 19 | AUTO\_EXTEND | INTEGER | 是否支持自动扩展：1 支持，0 不支持 |
| 20 | MAX\_SIZE | INTEGER | 文件最大大小，单位 MB |
| 21 | NEXT\_SIZE | INTEGER | 文件每次扩展大小，单位 MB，若创建文件时没有指定，则由 INI 参数 TS\_AUTO\_EXTEND\_SIZE 决定 |
| 22 | MIRROR\_PATH | VARCHAR(256) | 镜像文件路径 |
| 23 | REAL\_FREE\_SIZE | BIGINT | 未分配的空闲大小，单位：页数 |

5） **V$DATABASE**

显示数据库信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 数据库名称 |
| 2 | CREATE\_TIME | DATETIME(0) | 数据库创建时间 |
| 3 | ARCH\_MODE | CHAR(1) | 归档模式：归档或不归档。默认为不归档 |
| 4 | LAST\_CKPT\_TIME | DATETIIME(0) | 最后一次检查点时间。只对 ONLINE 的 DB 做统计，否则就是空 |
| 5 | STATUS$ | TINYINT | 状态。1：启动；2：启动，redo 完成；3：MOUNT；4：打开；5：挂起；6：关闭 |
| 6 | ROLE$ | TINYINT | 角色。0：普通；1：主库；2：备库 |
| 7 | MAX\_SIZE | BIGINT | 最大大小，单位：页数。0 代表只受操作系统限制 |
| 8 | TOTAL\_SIZE | BIGINT | 除回滚表空间外所有表空间的文件大小之和，单位：页数 |
| 9 | DSC\_NODES | INTEGER | DSC 集群系统中的实例总数 |
| 10 | OPEN\_COUNT | INTEGER | 数据库 open 次数 |
| 11 | STARTUP\_COUNT | BIGINT | 数据库启动次数 |
| 12 | LAST\_STARTUP\_TIME | DATETIME(0) | 数据库最近一次启动时间 |

6） **V$IID**

显示下一个创建的数据库对象的 ID。该视图提供用户可以查询下一个创建对象的 ID 的值，可以方便用户查询预知自己所要建立对象的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(100) | 对象名称 |
| 2 | VALUE | BIGINT | 对象值 |

7） **V$INSTANCE**

显示实例信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 实例名称 |
| 2 | INSTANCE\_NAME | VARCHAR (128) | 实例名称 |
| 3 | INSTANCE\_NUMBER | INTEGER | 实例 ID，单节点默认 1，MPP 或 DSC 环境下为实例序号加 1 |
| 4 | HOST\_NAME | VARCHAR(128) | 主机名称 |
| 5 | SVR\_VERSION | VARCHAR(128) | 服务器版本号。详见 V$VERSION 介绍 |
| 6 | DB\_VERSION | VARCHAR(40) | 数据库版本号 |
| 7 | START\_TIME | DATETIME(0) | 服务器启动时间 |
| 8 | STATUS$ | VARCHAR(128) | 系统状态 |
| 9 | MODE$ | VARCHAR(128) | 模式 |
| 10 | OGUID | INTEGER | 控制文件的 OGUID |
| 11 | DSC\_SEQNO | INTEGER | DSC 序号 |
| 12 | DSC\_ROLE | VARCHAR(32) | 非 DSC 环境显示 NULL；DSC 环境下表示 DSC 系统角色：Control node（控制节点）/Normal node（普通节点） |
| 13 | BUILD\_VERSION | VARCHAR(128) | 编译版本号 |
| 14 | BUILD\_TIME | VARCHAR(32) | 编译时间 |

8） **GV$INSTANCE**

显示全局实例信息。在 DPC 环境的备机上查询该视图，将只返回 RAFT 内的主备信息。

GV$INSTANCE 结构和 V$INSTANCE 结构一样。

9） **V$RESERVED\_WORDS**

显示关键字和保留字的分类信息。

对于 RESERVED=Y 且 RES\_FIXED=N 的保留字，可通过 ini 参数 EXCLUDE\_RESERVED\_WORDS 去除保留字身份。去除后的保留字将变为普通字符串，本视图不再记录。例如：若想去除保留字 AUTO\_INCREMENT，可设置 EXCLUDE\_RESERVED\_WORDS=AUTO\_INCREMENT，重启服务器后，查询此视图时，则不会出现保留字 AUTO\_INCREMENT 的相关信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | KEYWORD | VARCHAR(30) | 关键字名字 |
| 2 | LENGTH | INTEGER | 关键字长度 |
| 3 | RESERVED | VARCHAR(1) | 是否是保留字。Y 是； N 否 |
| 4 | RES\_SQL | VARCHAR(1) | 是否是 SQL 保留字。Y 是； N 否。是则不能作 SQL 中的标识符 |
| 5 | RES\_PL | VARCHAR(1) | 是否是 DMSQL 程序保留字。Y 是； N 否。是则不能作 DMSQL 程序语句块中的标识符 |
| 6 | RES\_SCHEMA | VARCHAR(1) | 是否是模式保留字。Y 是； N 否。是则不能作模式标识符 |
| 7 | RES\_VARIABLE | VARCHAR(1) | 是否是变量保留字。Y 是； N 否。是则不能作变量标识符 |
| 8 | RES\_ALIAS | VARCHAR(1) | 是否是别名保留字。Y 是； N 否。是则不能作别名标识符 |
| 9 | RES\_FIXED | VARCHAR(1) | 表示当前保留字是否被系统预定。Y 是，N 否。只有 RES\_FIXED 为 N 时，才可以通过 ini 参数 EXCLUDE\_RESERVED\_WORDS 去除保留字身份 |

10） **V$ERR\_INFO**

显示系统中的错误码信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | CODE | INTEGER | 错误码 |
| 2 | errinfo | VARCHAR(512) | 错误码描述 |

11） **V$HINT\_INI\_INFO**

显示支持的 HINT 参数信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PARA\_NAME | VARCHAR(128) | 参数名称 |
| 2 | HINT\_TYPE | VARCHAR(16) | HINT 类型，OPT：优化分析阶段使用；EXEC：执行阶段使用 |

12） **V$DYNAMIC\_TABLES**

显示当前数据库中的动态视图。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 动态视图名称 |
| 2 | ID | INTEGER | 动态视图 ID |
| 3 | SCHNAME | VARCHAR(128) | 动态视图所属模式名 |
| 4 | SYNONYMS | VARCHAR(512) | 动态视图的其他同义词，若有多个用逗号分隔，没有为 NULL |

13） **V$DYNAMIC\_TABLE\_COLUMNS**

显示当前数据库中所有动态视图的列信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TABNAME | VARCHAR(128) | 列所属动态视图名称 |
| 2 | COLNAME | VARCHAR(128) | 列名 |
| 3 | COLID | SMALLINT | 列 ID |
| 4 | TYPE$ | VARCHAR(128) | 列数据类型 |
| 5 | LENGTH$ | INTEGER | 列定义长度 |
| 6 | SCALE | SMALLINT | 列定义精度 |
| 7 | NULLABLE$ | CHAR(1) | 是否可以为空，Y:是，N：否 |
| 8 | DEFVAL | VARCHAR(2048) | 默认值 |

14） **V$AUTHORITIES**

显示当前数据库中的所有权限信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 权限 ID |
| 2 | NAME | VARCHAR(256) | 权限名称 |
| 3 | TYPE | INTEGER | 权限类型。1 表示数据库权限；2 表示对象权限；3 表示黑名单权限。黑名单权限表示关闭指定的对象权限 |

#### 4\. 数据库对象相关

数据库对象包括：表空间、序列、包、索引和函数等。

1） **V$TABLESPACE**

显示表空间信息，不包括 RLOG 表空间信息。

在集群环境中，V$TABLESPACE 会汇总所有站点的表空间信息。在集群环境中，为了区分不同站点的表空间信息，建议使用 select SF\_GET\_PARA\_STRING\_VALUE(1, 'INSTANCE\_NAME'),\* from V$TABLESPACE;加入实例名称一起查看。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 表空间 ID |
| 2 | NAME | VARCHAR(128) | 表空间名称 |
| 3 | CACHE | VARCHAR(20) | CACHE 名，早期用于区分表空间使用的缓冲区。后因系统调整，实际已无意义，目前为空或 NORMAL |
| 4 | TYPE$ | TINYINT | 表空间类型：1 DB 类型，2 临时表空间 |
| 5 | STATUS$ | TINYINT | 状态。0 ONLINE，1 OFFLINE，2 RES\_OFFLINE 3 CORRUPT |
| 6 | MAX\_SIZE | BIGINT | 最大大小，以页为单位。0 代表只受操作系统限制（暂无实际意义） |
| 7 | TOTAL\_SIZE | BIGINT | 总大小，以页为单位 |
| 8 | FILE\_NUM | INTEGER | 包含的文件数 |
| 9 | ENCRYPT\_NAME | VARCHAR(128) | 加密算法名 |
| 10 | ENCRYPTED\_KEY | VARCHAR(500) | 暂无意义，均显示 NULL |
| 11 | COPY\_NUM | INTEGER | 保留字段 |
| 12 | SIZE\_MODE | VARCHAR(128) | 保留字段 |
| 13 | OPT\_NODE | INTEGER | 指定的 DSC 集群表空间负载均衡优化节点号 |
| 14 | USED\_SIZE | BIGINT | 表示已使用的簇所占的大小，以页为单位 |
| 15 | SPACE\_LIMIT\_CNT | BIGINT | 表示达到表空间限制的次数 |
| 16 | EXTEND\_FAILED\_CNT | BIGINT | 扩展失败的次数 |
| 17 | N\_RESERVE\_EXTENTS | INTEGER | 期望保留的簇个数 |
| 18 | FREE\_EXTENTS | INTEGER | 当前表空间剩余空间簇的个数 |
| 19 | MDF\_FREE\_COUNT | INTEGER | 执行 MODIFY FREE EXTENTS 的次数，每 100 次重新计算一次，保证 FREE\_EXTENTS 准确 |
| 20 | FILE\_LIMIT | INTEGER | 文件个数限制 |

2） **V$HUGE\_TABLESPACE**

显示混合表空间的 HUGE 数据文件副本策略和路径统计信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 混合表空间 ID |
| 2 | NAME | VARCHAR(128) | 混合表空间名称 |
| 3 | PATHNAME | VARCHAR(256) | 混合表空间的 HUGE 数据文件路径 |
| 4 | DIR\_NUM | INTEGER | 混合表空间的 HUGE 数据文件路径数 |
| 5 | COPY\_NUM | INTEGER | 保留字段 |
| 6 | SIZE\_MODE | VARCHAR(128) | 保留字段 |

3） **V$HUGE\_TABLESPACE\_PATH**

显示混合表空间的 HUGE 数据文件路径信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 混合表空间 ID |
| 2 | PATHNAME | VARCHAR(256) | 混合表空间的 HUGE 数据文件路径 |

4） **V$SEQCACHE**

显示当前系统中缓存的序列的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 序列 ID |
| 2 | NAME | VARCHAR(128) | 序列名 |
| 3 | NEXTVAL | DEC(38) | 序列的值 |
| 4 | CACHE\_NUM | INTEGER | 创建序列时指定的缓存值的个数 |
| 5 | N\_USED | INTEGER | 已经使用的缓存值的个数 |
| 6 | OVERFLOW | INTEGER | 当前序列是否已溢出的标识 |

5） **V$PKGPROCS**

显示当前用户拥有执行权限的包中的方法。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PKGID | INTEGER | 包 ID |
| 2 | PKGNAME | VARCHAR(128) | 包名 |
| 3 | MTDID | INTEGER | 方法 ID，每个包中方法从 0 开始编号 |
| 4 | MTDNAME | VARCHAR(128) | 方法名 |
| 5 | IS\_PROC | CHAR(1) | 是否是过程，’Y’表示是过程，’N’表示是函数 |

6） **V$PKGPROCINFOS**

显示当前用户拥有执行权限的包中方法的相关信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | OWNER | VARCHAR(128) | 包所属用户名 |
| 2 | OBJECT\_NAME | VARCHAR(128) | 包名 |
| 3 | PROCEDURE\_NAME | VARCHAR(128) | 方法名 |
| 4 | OBJECT\_ID | INTEGER | 包 ID |
| 5 | SUBPROGRAM\_ID | INTEGER | 方法 ID，每个包中方法从 1 开始编号 |
| 6 | OVERLOAD | INTEGER | 方法在包中第几个重载 |
| 7 | OBJECT\_TYPE | VARCHAR(7) | 对象类型，始终为 PACKAGE |
| 8 | AGGREGATE | VARCHAR(10) | 是否是聚合函数，兼容保留字段 |
| 9 | PIPELINED | VARCHAR(10) | 是否是管道化表函数，‘YES’：是；‘NO’：否 |
| 10 | IMPLTYPEOWNER | VARCHAR(128) | 实现类所属的模式名，兼容保留字段 |
| 11 | IMPLTYPENAME | VARCHAR(128) | 实现类名，兼容保留字段 |
| 12 | PARALLEL | VARCHAR(10) | 是否可以并行，‘YES’：是；‘NO’：否 |
| 13 | INTERFACE | VARCHAR(10) | 是否是使用 DCI 接口实现的表函数，兼容保留字段 |
| 14 | DETERMINISTIC | VARCHAR(10) | 是否是确定性函数，‘YES’：是；‘NO’：否 |
| 15 | AUTHID | VARCHAR(12) | 标识定义者权限和调用者权限，DEFINER：定义者权限；CURRENT\_USER：调用者权限 |
| 16 | IS\_PRIV | INTEGER | 当前用户是否具有执行权限，1：是；0：否 |

7） **V$PKGPROCPARAMS**

显示当前用户拥有执行权限的包中方法的参数信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 参数名 |
| 2 | PKGID | INTEGER | 包 ID |
| 3 | MTDID | INTEGER | 方法 ID |
| 4 | PARAMID | SMALLINT | 参数 ID，每个方法的参数从 1 开始编号，0 表示返回值 |
| 5 | TYPE$ | VARCHAR(128) | 参数类型 |
| 6 | LENGTH$ | INTEGER | 参数长度 |
| 7 | SCALE | SMALLINT | 参数精度 |
| 8 | NULLABLE | CHAR(1) | 参数是否可为空 |
| 9 | IOFLAG | CHAR(2) | 参数输入输出标记，’I’表示输入，’O’表示输出，’IO’表示输入输出，’R’表示返回值 |
| 10 | DEFVAL | VARCHAR(2000) | 参数缺省值 |

8） **V$DB\_CACHE**

数据字典缓存表，用于记录数据字典的实时信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | DB\_ADDR | VARBINARY(8) | 数据字典地址 |
| 2 | POOL\_ID | INTEGER | 缓存池 ID |
| 3 | TOTAL\_SIZE | BIGINT | 缓存池总空间，单位字节 |
| 4 | USED\_SIZE | BIGINT | 实际使用的空间，单位字节 |
| 5 | DICT\_NUM | INTEGER | 缓存池中字典对象的总数 |
| 6 | SIZE\_LRU\_DISCARD | BIGINT | 由于缓存池已满导致字典对象被淘汰的空间的总和，单位字节 |
| 7 | LRU\_DISCARD | INTEGER | 由于缓存池已满导致字典对象被淘汰的次数 |
| 8 | DDL\_DISCARD | INTEGER | DDL 操作导致字典对象被淘汰的次数 |
| 9 | DISABLED\_SIZE | BIGINT | 被淘汰字典对象的空间，单位字节 |
| 10 | DISABLED\_DICT\_NUM | INTEGER | 缓存池中被淘汰字典对象的总数 |

9） **V$DB\_OBJECT\_CACHE**

数据字典对象缓存表，用于记录数据字典中每个对象的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TYPE | VARCHAR(32) | 字典对象类型 |
| 2 | ID | INTEGER | 字典对象的 ID |
| 3 | NAME | VARCHAR(128) | 字典对象的名称 |
| 4 | SCHID | INTEGER | 所在模式的 ID |
| 5 | PID | INTEGER | 所属对象的 ID |
| 6 | STATUS | VARCHAR(16) | 状态 |
| 7 | T\_SIZE | INTEGER | 对象结构所占空间，单位字节 |
| 8 | R\_SIZE | INTEGER | 对象在缓存中实际的空间，单位字节 |
| 9 | VERSION | INTEGER | 对象的版本号 |
| 10 | ID\_HASH | VARBINARY(8) | 对象 ID 的 HASH 值 |
| 11 | NAME\_HASH | VARBINARY(8) | 对象 NAME 的 HASH 值 |
| 12 | LOAD\_TIME | DATETIME(6) | 对象被加载的时间 |
| 13 | N\_DECODE | INTEGER | 对象 DECODE 的次数 |
| 14 | N\_SEARCH | INTEGER | 对象 SEARCH 的次数 |

10） **V$OBJECT\_USAGE**

记录索引监控信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INDEX\_NAME | VARCHAR(128) | 索引名 |
| 2 | SCH\_NAME | VARCHAR(128) | 模式名 |
| 3 | TABLE\_NAME | VARCHAR(128) | 表名 |
| 4 | MONITORING | VARCHAR(3) | 是否被监控(YES\\NO)，仅在 MONITOR\_INDEX\_FLAG=0 时有效 |
| 5 | USED | VARCHAR(3) | 是否被使用(YES\\NO) |
| 6 | START\_MONITORING | VARCHAR(19) | 开始监控时间，仅在 MONITOR\_INDEX\_FLAG=0 时有效 |
| 7 | END\_MONITORING | VARCHAR(19) | 停止监控时间，仅在 MONITOR\_INDEX\_FLAG=0 时有效 |
| 8 | USED\_NUM | BIGINT | 索引被使用次数 |
| 9 | SQL\_TEXT\_ID | VARCHAR(13) | 最近一次使用此索引的语句的 SQL\_TEXT\_ID |

11） **V$IFUN**

显示数据库提供的所有函数。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 函数名 |
| 2 | ID | INTEGER | 函数 ID |
| 3 | ARG\_NUM | INTEGER | 参数个数 |
| 4 | HAS\_RT\_FACT | CHAR(1) | 是否存在运行时因素，‘Y’：是；‘N’：否 |
| 5 | IS\_READONLY | CHAR(1) | 是否只读 |
| 6 | IS\_MPP\_BRO | CHAR(1) | MPP 下是否需要广播 |
| 7 | IS\_MPP\_FORBIDEN | CHAR(1) | MPP 下是否禁用该函数 |
| 8 | IS\_MOUNT\_ONLY | CHAR(1) | 系统 MOUNT 状态下是否可以使用该函数 |
| 9 | IS\_INCLUDE\_SQL | CHAR(1) | 函数中是否会执行 SQL 语句 |
| 10 | EXTRA\_ATTR | VARCHAR(1024) | 预留字段，无实际意义，全为 NULL |
| 11 | CLASS$ | VARCHAR(128) | 函数所属的类别 |
| 12 | COMMENT$ | VARCHAR(1024) | 预留字段，无实际意义，全为 NULL |
| 13 | IS\_LPQ\_FORBIDDEN | CHAR(1) | 此函数是否禁止并行执行 |

12） **V$IFUN\_ARG**

显示数据库提供的所有函数的参数。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 函数 ID |
| 2 | NAME | VARCHAR(128) | 函数参数名 |
| 3 | SEQ | INTEGER | 参数序号，从 0 开始依次递增，-1 表示返回值 |
| 4 | DATA\_TYPE | VARCHAR(64) | 参数数据类型 |
| 5 | LEN | INTEGER | 参数数据长度 |
| 6 | PREC | INTEGER | 参数数据精度 |
| 7 | IO\_TYPE | VARCHAR(8) | 参数输入输出类型 |
| 8 | COMMENT$ | VARCHAR(1024) | 参数说明。预留字段，无实际意义，全为 NULL。 |

13） **V$SYSSTAT**

显示系统中统计对象的信息，支持通过系统过程 SP\_DYNAMIC\_VIEW\_DATA\_CLEAR 来清空此视图的历史信息。

| 1 | ID | INTEGER | 统计对象 ID |
| --- | --- | --- | --- |
| **序号** | **列** | **数据类型** | **说明** |
| 2 | CLASSID | INTEGER | 统计对象所属类别 ID。1：字典信息；2：SQL；3：事务； 4：检查点；5：RLOG；6：UNDO；7：IO；8：B 树；9：网络；10：文件；11：内存；12：CPU；13：OS；14：缓冲区；15：限流控制；16：DMDPC；20：其它 |
| 3 | NAME | VARCHAR(128) | 统计对象名 |
| 4 | STAT\_VAL | BIGINT | 统计值 |

14） **V$JOBS\_RUNNING**

显示系统中正在执行的作业信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SID | BIGINT | 作业执行的 SESSION 的 ID |
| 2 | JOBID | INTEGER | 作业号 |
| 3 | FAILURES | INTEGER | 作业自上一次成功以来的失败次数，暂不支持 |
| 4 | LAST\_DATE | DATETIME(6) | 最后一次成功运行工作的时间 |
| 5 | THIS\_DATE | DATETIME(6) | 本次运行的开始时间 |
| 6 | INSTANCE | INTEGER | 本次运行所在实例的序号 |

15） **V$AUTO\_STAT\_TABLE\_IDU**

记录用户表中增删改数据的实时变化信息。在 INI 参数 AUTO\_STAT\_OBJ =1 或 2 时才统计。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 表 ID |
| 2 | TOTAL\_ROWS | BIGINT | 表中数据的总行数。TOTAL\_ROWS 为系统启动时的总行数，不是实时数据。只有发生统计的时候，TOTAL\_ROWS 才会更新 |
| 3 | INSERT\_ROWS | BIGINT | 插入数据的行数，为实时数据 |
| 4 | DELETE\_ROWS | BIGINT | 删除数据的行数，为实时数据 |
| 5 | UPDATE\_ROWS | BIGINT | 更新数据的行数，为实时数据显示当前系统打开的 HUGE 表列中存储的文件信息。 |

16） **V$HFILE**

显示当前系统打开的 HUGE 表列中存储的文件信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TSID | INTEGER | HUGE 表所属表空间 ID |
| 2 | SCHID | INTEGER | HUGE 表所属模式 ID |
| 3 | TABLEID | INTEGER | HUGE 表 ID |
| 4 | COLID | SMALLINT | 列 ID |
| 5 | FILEID | INTEGER | 列中存储的文件 ID |
| 6 | HANDLE | BIGINT | 文件句柄 |
| 7 | N\_FIX | INTEGER | 引用计数，表示有 N\_FIX 处正在使用该文件 |

17） **V$POLICY\_CACHE**

记录缓存中的对象策略信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 对象 ID |
| 2 | SCHID | INTEGER | 对象所在模式 ID |
| 3 | CONTEXT\_NUM | INTEGER | 对象关联的上下文数目 |
| 4 | GROUP\_NUM | INTEGER | 对象关联的策略组数目 |

18） **V$POLICY\_CACHE\_ITEM**

记录指定对象的具体策略信息。查询该视图时，一定要带 WHERE 条件。同时，查询条件必须且只能指定 1 个，且只能是该视图的首列，即 ID。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 对象 ID |
| 2 | SCHID | INTEGER | 对象所在模式 ID |
| 3 | CONTEXT | VARCHAR(128) | 上下文名 |
| 4 | ATTRIBUTE | VARCHAR(128) | 上下文属性值 |
| 5 | GROUP | VARCHAR(128) | 策略组名 |
| 6 | POLICY | VARCHAR(128) | 策略组内的策略名 |

19） **V$SYSINFO**

显示系统中全局量的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 全局量 ID |
| 2 | NAME | VARCHAR(128) | 全局量名 |
| 3 | INFO | VARCHAR(2048) | 全局量值 |

21）V$IO\_TIMEOUT

监控耗时较长的 IO 操作。仅保留最新的 10000 条记录。

TYPE 为 RLOG 时，GROUP\_ID、FILE\_ID、PAGE\_NO 为 NULL，记录 IO 延迟超过 1 秒的记录。DSC 环境下，TYPE 为 RLOG 时，记录 IO 延迟超过 IO\_TIMEOUT/2 的记录，并且会根据 DSC\_SLOT\_WAIT\_TIMEOUT 调整，但保证最小为 15 秒。

TYPE 为 PAGE 时，记录 IO 延迟超过 3 秒的记录。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TYPE | VARCHAR(8) | PAGE/RLOG |
| 2 | CHECK\_TIME | TIMESTAMP(0) | 检查时间 |
| 3 | WAIT\_TIME | INT | IO 延迟时间，单位：秒 |
| 4 | TIMEOUT | INT | 超时时间，单位：秒 |
| 5 | GROUP\_ID | INT | 页的表空间号 |
| 6 | FILE\_ID | INT | 页的文件号 |
| 7 | PAGE\_NO | INT | 页号 |

#### 5\. 数据库配置参数

1） **V$PARAMETER**

显示 ini 参数和 dminit 建库参数的类型及参数值信息（当前会话值、系统值及 dm.ini 文件中的值）。

| **序号** | **字段** | **类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | ID 号 |
| 2 | NAME | VARCHAR(80) | 参数名字 |
| 3 | TYPE | VARCHAR(200) | 参数类型。 READ ONLY：手动参数，表示服务器运行过程中不可修改； IN FILE：静态参数，只可修改 ini 文件； SYS 和 SESSION：动态参数，ini 文件和内存同时可修改，其中，SYS 为系统级参数；SESSION 为会话级参数 |
| 4 | VALUE | VARCHAR(4000) | 参数的值（当前会话） |
| 5 | SYS\_VALUE | VARCHAR(4000) | 参数的值（系统） |
| 6 | FILE\_VALUE | VARCHAR(4000) | 参数的值（ini 文件） |
| 7 | DESCRIPTION | VARCHAR2(255) | 参数描述 |
| 8 | DEFAULT\_VALUE | VARCHAR(256) | 参数默认值 |
| 9 | ISDEFAULT | INTEGER | dm.ini 中参数的值和默认值是否相同，1 表示相同，0 表示不同。系统默认初始化后，某些静态建库参数在系统启动过程中会根据环境自动调整数值，导致与默认值不同 |

2） **V$DM\_INI**

显示 ini 参数和 dminit 建库参数信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PARA\_NAME | VARCHAR (128) | 参数名称 |
| 2 | PARA\_VALUE | VARCHAR (256) | 系统参数值 |
| 3 | MIN\_VALUE | VARCHAR (256) | 最小值 |
| 4 | MAX\_VALUE | VARCHAR (256) | 最大值 |
| 5 | DEFAULT\_VALUE | VARCHAR (256) | 默认值 |
| 6 | MPP\_CHK | CHAR(1) | 是否检查 MPP 节点间参数一致性。Y 是，N 否 |
| 7 | SESS\_VALUE | VARCHAR(256) | 会话参数值 |
| 8 | FILE\_VALUE | VARCHAR(256) | INI 文件中参数值 |
| 9 | DESCRIPTION | VARCHAR(256) | 参数描述 |
| 10 | PARA\_TYPE | VARCHAR(200) | 参数类型 |
| 11 | SYNC\_FLAG | VARCHAR(16) | 已废弃，取值 UNKNOWN。 |
| 12 | SYNC\_LEVEL | VARCHAR(16) | 已废弃，取值 UNKNOWN。 |
| 13 | PARA\_MODULE | VARCHAR(32) | 标识参数所属模块，有如下可能取值：   files location：控制文件相关   instance name：实例名   memory pool and buffer：内存池和缓冲区相关   thread：线程相关   query：查询相关   select rate：查询效率相关   checkpoint：检查点相关   IO：IO 相关   database：数据库相关   pre-load table：预先装载表相关   redo log：REDO 日志生成相关   redo：REDO 重做/重演相关   transaction：事务相关   security：安全相关，储存在 dm.ini 中   security2：安全相关，储存在系统数据文件中，仅能通过系统过程调整，未列在 dm.ini 中   compatibility：兼容性相关   drop table：删除表相关   fast insert：快速插入   request trace：用户请求跟踪相关   system trace：系统跟踪相关   monitor：MONITOR 监控相关   data watch：数据守护相关   for test only：测试专用   for context index：全文索引相关   rdma：RDMA 通讯相关   configuration file：配置文件相关   DSC：DMDSC 相关   mem only：内存相关   backup and restore：备份还原相关 |
| 14 | PRIMARY\_SYNC | CHAR(1) | 参数是否会进行主备同步，取值：Y/N。Y：会进行主备同步，N：不会主备同步。 |
| 15 | DSC\_SYNC | CHAR(1) | 参数是否进行 DSC 节点间同步，取值：Y/N。Y：会进行 DSC 节点间同步，N：不会进行 DSC 节点间同步。 |

3） **GV$DM\_INI**

DPC 环境下查询所有正常打开实例的 INI 参数。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INSTANCE\_NAME | VARCHAR (128) | 实例名 |
| 2 | PARA\_NAME | VARCHAR (128) | 参数名称 |
| 3 | PARA\_VALUE | VARCHAR(256) | 系统参数值 |
| 4 | MIN\_VALUE | VARCHAR(256) | 最小值 |
| 5 | MAX\_VALUE | VARCHAR(256) | 最大值 |
| 6 | DEFAULT\_VALUE | VARCHAR(256) | 默认值 |
| 7 | MPP\_CHK | CHAR(1) | 是否检查 MPP 节点间参数一致性。Y 是，N 否 |
| 8 | SESS\_VALUE | VARCHAR(256) | 会话参数值 |
| 9 | FILE\_VALUE | VARCHAR(256) | INI 文件中参数值 |
| 10 | DESCRIPTION | VARCHAR(256) | 参数描述 |
| 11 | PARA\_TYPE | VARCHAR(200) | 参数类型 |
| 12 | SYNC\_FLAG | VARCHAR(16) | 已废弃，取值 UNKNOWN。 |
| 13 | SYNC\_LEVEL | VARCHAR(16) | 已废弃，取值 UNKNOWN。 |
| 14 | PARA\_MODULE | VARCHAR(32) | 标识参数所属模块，有如下可能取值： files location、instance name、memory pool and buffer、thread、query、select rate、cpu、checkpoint、IO、database、pre-load table、redo log、redo、transaction、security、security2、compatibility、drop table、fast insert、request trace、system trace、ecs、monitor、data watch、for test only、for context index、rdma、configuration file、DSC、mem only、backup and restore |
| 15 | PRIMARY\_SYNC | CHAR(1) | 参数是否会进行主备同步，取值：Y/N。Y：会进行主备同步，N：不会主备同步。 |
| 16 | DSC\_SYNC | CHAR(1) | 参数是否进行 DSC 节点间同步，取值:Y/N。Y：会进行 DSC 节点间同步，N：不会进行 DSC 节点间同步。 |

4） **V$DM\_INI\_DESC**

所有查询相关 INI 参数的具体描述信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PARA\_NAME | VARCHAR(128) | 参数名称 |
| 2 | DESCRIPTION | VARCHAR(4096) | 参数具体描述 |

5） **V$DM\_ARCH\_INI**

归档参数信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ARCH\_NAME | VARCHAR (128) | 归档名称 |
| 2 | ARCH\_TYPE | VARCHAR (128) | 归档类型 |
| 3 | ARCH\_DEST | VARCHAR (512) | 对于本地归档，表示归档路径；对于远程归档，表示远程节点实例名；对于其余类型的归档，表示归档目标实例名 |
| 4 | ARCH\_FILE\_SIZE | INTEGER | 归档文件大小，单位 MB |
| 5 | ARCH\_SPACE\_LIMIT | INTEGER | 归档文件的磁盘空间限制，单位 MB |
| 6 | ARCH\_HANG\_FLAG | INTEGER | 如果写入本地归档时磁盘空间不够，是否让服务器挂起。仅对本地归档有效，其他归档类型显示为 NULL |
| 7 | ARCH\_TIMER\_NAME | VARCHAR (128) | 对于异步归档，表示定时器名称；其余类型归档显示 NULL |
| 8 | ARCH\_IS\_VALID | CHAR(1) | 归档状态，是否有效 |
| 9 | ARCH\_WAIT\_APPLY | INTEGER | 在主备系统中，主库发送归档日志给备库之前，是否需要等待备库将上一批日志重演完成。 取值 0：高性能模式，不用等待重演完成；1：事务一致模式，需等待重演完成。除即时归档和实时归档外，其他归档取值均为 NULL |
| 10 | ARCH\_INCOMING\_PATH | VARCHAR(256) | 对于远程归档，表示远程节点的本地归档日志文件存放路径；其余类型归档显示 NULL |
| 11 | ARCH\_CURR\_DEST | VARCHAR(256) | 当前归档目标实例名，如果备库是 DMDSC 集群，则归档目标是备库控制节点，该字段表示当前被选定为归档目标的节点实例名。备库是单机的情况下，就是指的备库实例名。 |
| 12 | ARCH\_FLUSH\_BUF\_SIZE | INTEGER | 归档刷盘缓存大小，单位 MB，取值范围 0~128。0 表示不使用归档刷盘缓存机制。缺省为 2 |
| 13 | ARCH\_RESERVE\_TIME | INTEGER | 归档日志保留时间，单位分钟。只对本地归档有效。服务器每隔 5 分钟检查是否存在超过保留时间的归档并删除。缺省为 0，表示不删除归档。 |
| 14 | ARCH\_LOCAL\_SHARE | INTEGER | 预留字段 |
| 15 | ARCH\_LOCAL\_SHARE\_CHECK | INTEGER | 预留字段 |
| 16 | ARCH\_SEND\_DELAY | INTEGER | 源库到异步备库的归档延时发送时间。单位分钟。0 表示未启用归档延时发送功能 |
| 17 | ARCH\_DEST\_IP | VARCHAR(64) | RAFT 归档目标 IP |
| 18 | ARCH\_DEST\_PORT | INTEGER | RAFT 归档目标端口 |
| 19 | ARCH\_DEST\_ID | INTEGER | 归档目标多副本节点编号，用于标识多副本 RAFT 组中不同的节点 |
| 20 | ARCH\_ASM\_MIRROR | SMALLINT | 归档文件配置在 DMASM 上的镜像类型，DMASM 镜像专用，取值：1：单副本，表示外部冗余，不提供任何镜像，假设磁盘高度可靠；2：双副本，表示正常冗余，提供双向镜像，可较好的保证数据完整性；3：三副本，表示高度冗余，提供三向镜像，能够更好的保证数据的完整性。未配置显示 NULL。 仅在 DMASM 镜像环境下有效 |
| 21 | ARCH\_ASM\_STRIPING | SMALLINT | 归档文件配置在 DMASM 上的条带化粒度，DMASM 镜像专用，取值 0 表示粗粒度，32/64/128/256 表示细粒度条带化大小，单位 KB。未配置显示 NULL。仅在 DMASM 镜像环境下有效 |
| 22 | ARCH\_RECOVER\_TIME | INTEGER | 主库向归档状态为 Invalid 的同步备库发起异步恢复的时间间隔，单位为秒 |

6） **V$DM\_MAL\_INI**

MAL 参数信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | MAL\_NAME | VARCHAR (128) | MAL 名称 |
| 2 | MAL\_INST\_NAME | VARCHAR (256) | 实例名称 |
| 3 | MAL\_HOST | VARCHAR (256) | IP 地址 |
| 4 | MAL\_PORT | INTEGER | 端口号 |
| 5 | MAL\_INST\_HOST | VARCHAR (256) | 对应实例 IP 地址 |
| 6 | MAL\_INST\_PORT | INTEGER | 对应实例的端口号 |
| 7 | MAL\_DW\_PORT | INTEGER | MAL\_INST\_NAME 实例的守护进程监听远程守护进程或监视器连接请求的端口 |
| 8 | MAL\_LINK\_MAGIC | INTEGER | MAL 链路网段标识 |
| 9 | MAL\_INST\_DW\_PORT | INTEGER | MAL\_INST\_NAME 实例监听守护进程连接请求的端口 |
| 10 | MAL\_RDMA\_MAGIC | INTEGER | MAL 链路通信方式标识，取值范围 0~65534，缺省为 0，属于为每个实例配置的局部变量，为了支持 RDMA/TCP 混合通信。在 MAL\_USE\_RDMA 开启的情况下，配置相同 MAL\_RDMA\_MAGIC 的节点间使用 RDMA 通信，不同则使用 TCP 通信。若不配置 MAL\_RDMA\_MAGIC，缺省为 0，可以和 MAL\_RDMA\_MAGIC 为 0 的节点进行 RDMA 通信 |

7） **V$DM\_TIMER\_INI**

定时器参数信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TIMER\_NAME | VARCHAR(128) | 定时器名称 |
| 2 | TYPE | TINYINT | 类型。1：执行一次；2：按日执行；3：按周执行；4：按月执行的第几天；5：按月执行的第一周；6：按月执行的第二周；7：按月执行的第三周；8：按月执行的第四周； 9：按月执行的最后一周；10：日历表达式 |
| 3 | FREQ\_MONTH\_WEEK\_INTERVAL | INTEGER | 间隔的月/周/天（调度类型决定）数 |
| 4 | FREQ\_SUB\_INTERVAL | INTEGER | 第几天/星期几/一个星期中的某些天 |
| 5 | FREQ\_MINUTE\_INTERVAL | INTEGER | 分钟间隔 |
| 6 | START\_TIME | TIME(0) | 开始时间 |
| 7 | END\_TIME | TIME(0) | 结束时间 |
| 8 | DURING\_START\_DATE(6) | DATETIME(6) | 有效时间段的开始日期时间 |
| 9 | DURING\_END\_DATE(6) | DATETIME(6) | 有效时间段的结束日期时间 |
| 10 | NO\_END\_DATE\_FLAG | CHAR(1) | 无结束日期标识 |
| 11 | DESCRIBE | VARCHAR(256) | 描述 |
| 12 | IS\_VALID | CHAR(1) | 是否有效，取值 Y/N。对应 dmtimer.ini 中的 IS\_VALID 配置项，但在 dmtimer.ini 中 IS\_VALID 配置项取值为 1/0 |
| 13 | REPEAT\_INTERVAL | VARCHAR(4000) | 日历表达式 |

8） **V$OBSOLETE\_PARAMETER**

已作废的 INI 信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PARA\_NAME | VARCHAR (128) | 参数名称 |

9） **V$OPTION**

安装数据库时的参数设置。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PARA\_NAME | VARCHAR (128) | 参数名称 |
| 2 | PARA\_VALUE | VARCHAR (256) | 系统参数值 |

10） **V$DM\_SQLLOG\_INI**

显示 sqllog.ini 中的配置参数信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | MODE\_NAME | VARCHAR(128) | SQL 日志模式名。值为\<PUBLIC> 时，表示当前参数为全局配置参数 |
| 2 | PARA\_NAME | VARCAHR(128) | SQL 日志中的参数名 |
| 3 | PARA\_VALUE | VARCAHR(32767) | SQL 日志中的参数值 |
| 4 | IS\_DEFAULT | CHAR(1) | PARA\_VALUE 是否与\<DEFAULT> 模式中对应参数值相等 |

11） **V$DM\_SQLLOG\_CONFIG**

显示内存中的 SQL 日志配置参数信息，即当前生效的配置参数信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | MODE\_NAME | VARCHAR(128) | SQL 日志模式名。值为\<PUBLIC> 时，表示当前参数为全局配置参数；值为\<DEFAULT> 时，表示当前使用系统默认配置 |
| 2 | PARA\_NAME | VARCAHR(128) | SQL 日志中的参数名 |
| 3 | PARA\_VALUE | VARCAHR(32767) | SQL 日志中的参数值 |

#### 6\. 日志管理

1） **V$RLOG**

显示日志的总体信息。通过该视图可以了解系统当前日志事务号 LSN 的情况、检查点的执行情况等。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | CKPT\_LSN | BIGINT | 最近一次检查点 LSN |
| 2 | FILE\_LSN | BIGINT | 已经到盘上的 LSN |
| 3 | FLUSH\_LSN | BIGINT | 当前准备刷盘的 LSN |
| 4 | CUR\_LSN | BIGINT | 当前的 LSN |
| 5 | NEXT\_SEQ | BIGINT | 下一个日志包序号 |
| 6 | N\_MAGIC | INTEGER | 本次运行，日志的 MAGIC |
| 7 | DB\_MAGIC | BIGINT | 数据库的 MAGIC |
| 8 | FLUSH\_PAGES | INTEGER | Flush 链表中的总页数 |
| 9 | FLUSHING\_PAGES | INTEGER | 正在刷盘的总页数 |
| 10 | CUR\_FILE | INTEGER | 记录刷文件前当前文件的 ID |
| 11 | CUR\_OFFSET | BIGINT | 记录刷文件前 cur\_file 的 free |
| 12 | CKPT\_FILE | INTEGER | 最近一次检查点对应的当时的文件号 |
| 13 | CKPT\_OFFSET | BIGINT | 最近一次检查点对应的当时的文件偏移 |
| 14 | FREE\_SPACE | BIGINT | 目前可用的日志空间，单位为字节 |
| 15 | TOTAL\_SPACE | BIGINT | 日志总空间，单位为字节 |
| 16 | SUSPEND\_TIME | DATETIME(6) | 挂起时间戳 |
| 17 | UPD\_CTL\_LSN | BIGINT | 系统修改控制文件的 ptx->lsn |
| 18 | N\_RESERVE\_WAIT | INTEGER | 日志空间预申请等待的个数 |
| 19 | TOTAL\_FLUSH\_PAGES | BIGINT | 系统启动后累计刷盘的总页数 |
| 20 | TOTAL\_FLUSH\_TIMES | BIGINT | 系统启动后累计刷盘的总次数 |
| 21 | TOTAL\_ECPR\_FLUSH\_PAGES | BIGINT | 系统启动后累计刷盘的日志总页数，非加密压缩情况下等于 TOTAL\_FLUSH\_PAGES |
| 22 | GLOBAL\_NEXT\_SEQ | BIGINT | 下一个全局日志包序号 |
| 23 | N\_PRIMARY\_EP | INTEGER | 主库节点数 |
| 24 | PRIMARY\_DB\_MAGIC | BIGINT | 主库 DB\_MAGIC 值 |
| 25 | CKPT\_N\_PRIMARY\_EP | INTEGER | 主库节点数,刷盘时调整 |
| 26 | CKPT\_PRIMARY\_DB\_MAGIC | BIGINT | 主库 DB\_MAGIC，刷盘时调整 |
| 27 | MIN\_EXEC\_VER | VARCHAR(64) | 日志文件允许访问的最小执行码版本号 |
| 28 | MIN\_DCT\_VER | INTEGER | 日志文件允许访问的最小字典版本号 |
| 29 | CLSN\_OPEN\_ID | INTEGER | 当前实例检查点偏移对应的 DB\_OPEN\_ID |
| 30 | DB\_OPEN\_ID | INTEGER | 当前实例 OPEN 次数。DMDSC 集群推进检查点时，从 DB\_OPEN\_ID 值最小的节点开始依次推进检查点，以保证故障处理时严格按照日志包产生顺序重做 REDO 日志 |
| 31 | ALMOST\_FULL\_STATUS | VARCHAR(16) | 日志空间使用情况，SAFE：剩余空间足够，UNSAFE：剩余空间不足 |
| 32 | PTX\_RESERVED | BIGINT | 当前所有物理事务 ptx 预留的日志总量，单位：字节 |
| 33 | RESERVE\_THRESHOLD | INTEGER | 启动日志空间预留机制的日志量门槛，单位：MB |
| 34 | RESERVE\_SIZE | INTEGER | 启动日志空间预留机制后，每个物理事务 ptx 操作预留的日志空间大小，单位为日志页个数，参考 2.1.1.1.10 中 RLOG\_RESERVE\_SIZE |

2） **V$RLOG\_PKG**

显示日志包信息。通过该视图可以查询日志系统中当前日志包的使用情况，如包的长度、最大 LSN、最小 LSN 等。通过该视图还可以查询当前实例日志系统中等待刷盘的链表上的日志包信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PKG\_LEN | BIGINT | 日志包的长度，单位 BYTE |
| 2 | DATA\_OFF | BIGINT | 日志包中有效数据长度，单位 BYTE |
| 3 | ENC\_LEN | BIGINT | 日志包加密后数据长度，单位 BYTE |
| 4 | CMPR\_LEN | BIGINT | 日志包压缩后数据长度，单位 BYTE |
| 5 | HDR\_SIZE | INTEGER | 日志包包头长度，单位 BYTE |
| 6 | N\_MAGIC | BIGINT | 日志包固定魔数 |
| 7 | DB\_MAGIC | BIGINT | 数据库魔数 |
| 8 | N\_DSC | INTEGER | DSC 集群节点数 |
| 9 | DSC\_SEQNO | INTEGER | DSC 集群节点号 |
| 10 | FROM\_PRIMARY | INTEGER | 是否为主库生成的日志包，1：是主库生成的包；0：不是主库生成的包 |
| 11 | PKG\_TYPE | INTEGER | 日志包包类型，不同取值对应类型如下：0：RLOG；1：PLOG；2：CKPT；3：UPD\_KEY，联机日志密码更新 |
| 12 | ENC\_CMPR | INTEGER | 加密压缩标记，0：CMPR\_NONE；1：ENC\_ONLY；2：CMPR\_ONLY；3：ENC\_CMPR。 |
| 13 | L\_SEQNO | BIGINT | 本地包序号 |
| 14 | G\_SEQNO | BIGINT | 全局包序号 |
| 15 | MIN\_LSN | BIGINT | 包内日志最小 LSN |
| 16 | MAX\_LSN | BIGINT | 包内日志最大 LSN |
| 17 | PREV\_LSN | BIGINT | 前一个包的日志最大 LSN |
| 18 | N\_FIXED | INTEGER | 包的日志填充次数 |
| 19 | N\_FILLED | INTEGER | 包的填充完成的次数 |
| 20 | PKG\_STAT | INTEGER | 日志包状态，0 表示正在填充的串行包，1 表示正在填充的并行包，2 表示已填充完成待刷盘的日志包 |

3） **V$RLOG\_PKG\_STAT**

显示当前实例日志系统中日志包使用的统计信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | N\_FLUSH\_TO | BIGINT | 请求刷盘的次数 |
| 2 | N\_FLUSH\_WAIT | BIGINT | 刷盘等待的次数 |
| 3 | N\_PUSHED | BIGINT | 拷贝到 flush\_lst 次数 |
| 4 | N\_COPY\_WAIT | BIGINT | 拷贝到 flush\_lst 过程中产生等待的次数 |
| 5 | N\_FOR\_CKPT | BIGINT | 检查点类型的日志包个数 |
| 6 | N\_DISCARDED | BIGINT | 日志刷盘线程中丢弃的日志包个数 |
| 7 | N\_FLUSHED | BIGINT | 刷盘日志包个数 |
| 8 | BYTES\_FLUSHED | BIGINT | 刷盘日志包长度总和，单位 BYTE |
| 9 | PKG\_AVG\_BYTES | INTEGER | 刷盘日志包平均长度，单位 BYTE |
| 10 | NEXT\_SEQNO | BIGINT | 下一个日志包序号 |
| 11 | N\_ALLOC\_WAIT | BIGINT | 分配日志包过程中产生等待的次数 |
| 12 | GLOBAL\_NEXT\_SEQNO | BIGINT | 下一个全局日志包序号 |
| 13 | PKG\_AVG\_PLL | INTEGER | 日志包的平均并行度 |
| 14 | N\_FLUSH\_LST | INTEGER | 待刷盘的日志包个数 |

4） **V$RLOGFILE**

显示日志文件的具体信息。包括文件号、完整路径、文件的状态、文件大小等等。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | GROUP\_ID | INTEGER | 表空间 ID |
| 2 | FILE\_ID | INTEGER | 文件 ID |
| 3 | PATH | VARCHAR(256) | 文件路径 |
| 4 | CLIENT\_PATH | VARCHAR(256) | 文件路径，专门提供给客户端 |
| 5 | CREATE\_TIME | DATETIME(5) | 创建时间 |
| 6 | RLOG\_SIZE | BIGINT | 文件大小，单位 BYTE |
| 7 | MIN\_EXEC\_VER | VARCHAR(64) | 此文件允许访问的最小执行码版本号 |
| 8 | MIN\_DCT\_VER | INTEGER | 此文件允许访问的最小字典版本号 |

5） **V$ARCHIVED\_LOG**

显示当前实例的所有归档日志文件信息。此动态视图中有一些保留列，查询时均显示 NULL。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | RECID | INTEGER | 保留列 |
| 2 | STAMP | INTEGER | 保留列 |
| 3 | NAME | VARCHAR(513) | 归档日志文件名 |
| 4 | DEST\_ID | INTEGER | 保留列 |
| 5 | THREAD# | BIGINT | 保留列。均为 0 |
| 6 | SEQUENCE# | INTEGER | 日志文件的序号；若序号 SEQUENCE#连续，则表示不存在归档缺失；若相邻两行的序号 SEQUENCE#之间跳过一个数，则表示这两个序号代表的归档文件中间有归档缺失 |
| 7 | RESETLOGS\_CHANGE# | INTEGER | 保留列 |
| 8 | RESETLOGS\_TIME | DATETIME(6) | 保留列 |
| 9 | RESETLOGS\_ID | INTEGER | 保留列 |
| 10 | FIRST\_CHANGE# | BIGINT | 日志文件所记录日志的最小 LSN 值 |
| 11 | FIRST\_TIME | DATETIME(6) | 日志文件所记录的日志的起始时间 |
| 12 | NEXT\_CHANGE# | BIGINT | 日志文件所记录日志的最大 LSN 值 |
| 13 | NEXT\_TIME | DATETIME(6) | 日志文件所记录的日志的截止时间 |
| 14 | BLOCKS | INTEGER | 保留列 |
| 15 | BLOCK\_SIZE | INTEGER | 保留列 |
| 16 | CREATOR | VARCHAR(7) | 保留列 |
| 17 | REGISTRAR | VARCHAR(7) | 保留列 |
| 18 | STANDBY\_DEST | VARCHAR(3) | 保留列 |
| 19 | ARCHIVED | VARCHAR(3) | 保留列。均为 YES |
| 20 | APPLIED | VARCHAR(9) | 归档文件日志包是否全部重演完成。NO：归档文件中日志包还没有重演完成；YES：归档文件中日志包全部重演完成   对于 DMDSC 备库非控制节点，不会重演，此字段结果为 NULL；对于 RAFT 下的影子备库，不会重演，此字段结果为 NO |
| 21 | DELETED | VARCHAR(3) | 保留列。均为 NO |
| 22 | STATUS | VARCHAR(1) | 保留列。均为 A |
| 23 | COMPLETION\_TIME | DATETIME(6) | 保留列 |
| 24 | DICTIONARY\_BEGIN | VARCHAR(3) | 保留列 |
| 25 | DICTIONARY\_END | VARCHAR(3) | 保留列 |
| 26 | END\_OF\_REDO | VARCHAR(3) | 保留列 |
| 27 | BACKUP\_COUNT | INTEGER | 保留列 |
| 28 | ARCHIVAL\_THREAD# | INTEGER | 保留列 |
| 29 | ACTIVATION# | INTEGER | 保留列 |
| 30 | IS\_RECOVERY\_DEST\_FILE | VARCHAR(3) | 保留列。均为 NO |
| 31 | COMPRESSED | VARCHAR(3) | 保留列 |
| 32 | FAL | VARCHAR(3) | 保留列 |
| 33 | END\_OF\_REDO\_TYPE | VARCHAR(10) | 保留列 |
| 34 | BACKED\_BY\_VSS | VARCHAR(3) | 保留列 |
| 35 | ARCH\_TYPE | VARCHAR(128) | 归档类型 |
| 36 | EP\_SEQNO | INTEGER | DSC 节点号 |
| 37 | ARCH\_SEQ | BIGINT | 起始包序号 |
| 38 | NEXT\_SEQ | BIGINT | 最大包序号 |
| 39 | VERSION | BIGINT | 库版本 |

6） **V$LOGMNR\_LOGS**

显示当前会话添加的需要分析的归档日志文件。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | LOG\_ID | INTEGER | 日志文件 ID 号 |
| 2 | FILENAME | VARCHAR(512) | 日志文件 ID 名 |
| 3 | LOW\_TIME | DATETIME(6) | 日志文件创建时间 |
| 4 | HIGH\_TIME | DATETIME(6) | 日志文件最后修改时间 |
| 5 | DB\_ID | INTEGER | 日志文件的实例 ID 号 |
| 6 | DB\_NAME | VARCHAR(128) | 日志文件的数据库名称 |
| 7 | RESET\_SCN | BIGINT | 保留列。暂无意义 |
| 8 | RESET\_SCN\_TIME | DATETIME(6) | 保留列。暂无意义 |
| 9 | COMPATIBLE | VARCHAR(17) | 保留列。暂无意义 |
| 10 | THREAD\_ID | BIGINT | 保留列。均为 0 |
| 11 | THREAD\_SQN | INTEGER | 日志文件的序号 |
| 12 | LOW\_SCN | BIGINT | 日志文件最小 LSN |
| 13 | NEXT\_SCN | BIGINT | 日志文件最大 LSN |
| 14 | DICTIONARY\_BEGIN | VARCHAR(3) | 保留列。均为 NO |
| 15 | DICTIONARY\_END | VARCHAR(3) | 保留列。均为 NO |
| 16 | TYPE | VARCHAR(8) | 保留列。均为 ARCHIVED |
| 17 | BLOCKSIZE | INTEGER | 保留列。均为 512 |
| 18 | FILESIZE | BIGINT | 日志文件的大小，单位 BYTE |
| 19 | INFO | VARCHAR(32) | 保留列。暂无意义 |
| 20 | STATUS | INTEGER | 保留列。均为 0 |

7） **V$LOGMNR\_PARAMETERS**

显示当前会话 START\_LOGMNR 启动日志文件分析的参数。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | START\_DATE | DATETIME(6) | 过滤分析归档日志的起始时间 |
| 2 | REQUIRED\_START\_DATE | DATETIME(6) | 保留列，返回 NULL |
| 3 | END\_DATE | DATETIME(6) | 过滤分析归档日志的截止时间 |
| 4 | START\_SCN | BIGINT | 过滤分析归档日志的起始 LSN |
| 5 | REQUIRED\_START\_SCN | BIGINT | 保留列，返回 0 |
| 6 | END\_SCN | BIGINT | 过滤分析归档日志的截止 LSN |
| 7 | OPTIONS | INTEGER | 分析归档日志的选项 |
| 8 | INFO | VARCHAR(32) | 保留列，返回 NULL |
| 9 | STATUS | INTEGER | 保留列，返回 0 |

8） **V$LOGMNR\_CONTENTS**

显示当前会话日志分析的内容。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SCN | BIGINT | 当前记录的 LSN |
| 2 | START\_SCN | BIGINT | 当前事务的起始 LSN |
| 3 | COMMIT\_SCN | BIGINT | 当前事务的截止 LSN |
| 4 | TIMESTAMP | DATETIME(6) | 当前记录的创建时间 |
| 5 | START\_TIMESTAMP | DATETIME(6) | 当前事务的起始时间 |
| 6 | COMMIT\_TIMESTAMP | DATETIME(6) | 当前事务的截止时间 |
| 7 | XIDUSN | BIGINT | 保留列，暂无意义，显示为 NULL |
| 8 | XIDSLT | BIGINT | 保留列，暂无意义，显示为 NULL |
| 9 | XIDSQN | BIGINT | 保留列，暂无意义，显示为 NULL |
| 10 | XID | BINARY(8) | 当前记录的事务 ID 号，为 BIGINT 类型的事务 ID 直接转换为 16 进制，并在前面补 0 |
| 11 | PXIDUSN | BIGINT | 保留列，暂无意义，显示为 NULL |
| 12 | PXIDSLT | BIGINT | 保留列，暂无意义，显示为 NULL |
| 13 | PXIDSQN | BIGINT | 保留列，暂无意义，显示为 NULL |
| 14 | PXID | BINARY(8) | 保留列，暂无意义，显示为 NULL |
| 15 | TX\_NAME | VARCHAR(256) | 保留列，暂无意义，显示为 NULL |
| 16 | OPERATION | VARCHAR(32) | 操作类型：INSERT、DELETE、UPDATE、BATCH\_UPDATE、DDL、START、COMMIT、LOB\_NEW、LOB\_DATA、PRE\_COMMIT、ROLLBACK、SEQ MODIFY、XA\_COMMIT、UNSUPPORTED |
| 17 | OPERATION\_CODE | INTEGER | 操作类型编号：   1 - INSERT   2 - DELETE   3 - UPDATE   4 - BATCH\_UPDATE   5 - DDL   6 - START   7 - COMMIT   13 - LOB\_NEW   14 - LOB\_DATA   15 - PRE\_COMMIT   36 - ROLLBACK   37 - SEQ MODIFY   38 - XA\_COMMIT   255 - UNSUPPORTED |
| 18 | ROLL\_BACK | INTEGER | 当前记录是否被回滚，1：是，0：否 |
| 19 | SEG\_OWNER | VARCHAR(128) | 操作的模式名 |
| 20 | SEG\_NAME | VARCHAR(256) | 保留列，暂无意义，显示为 NULL |
| 21 | TABLE\_NAME | VARCHAR(128) | 操作的表名 |
| 22 | SEG\_TYPE | INTEGER | 保留列，暂无意义，显示为 NULL |
| 23 | SEG\_TYPE\_NAME | VARCHAR(32) | 保留列，暂无意义，显示为 NULL |
| 24 | TABLE\_SPACE | VARCHAR(32) | 保留列，暂无意义，显示为 NULL |
| 25 | ROW\_ID | VARCHAR(20) | 对应记录的行号 |
| 26 | USERNAME | VARCHAR(128) | 执行这条语句的用户名 |
| 27 | OS\_USERNAME | VARCHAR(4000) | 保留列，暂无意义，显示为 NULL |
| 28 | MACHINE\_NAME | VARCHAR(4000) | 保留列，暂无意义，显示为 NULL |
| 29 | AUDIT\_SESSIONID | BIGINT | 保留列，暂无意义，显示为 NULL |
| 30 | SESSION# | BIGINT | 当前记录的会话 ID 信息 |
| 31 | SERIAL# | BIGINT | 保留列，暂无意义，显示为 NULL |
| 32 | SESSION\_INFO | VARCHAR(4000) | 语句来源机器的 IP 地址 |
| 33 | THREAD# | BIGINT | 保留列，暂无意义，显示为 NULL |
| 34 | SEQUENCE# | INTEGER | 保留列，暂无意义，显示为 NULL |
| 35 | RBASQN | INTEGER | 对应的归档日志文件号 |
| 36 | RBABLK | INTEGER | RBASQN 所指日志文件的块号，从 0 开始 |
| 37 | RBABYTE | INTEGER | RBABLK 所指块号的块内偏移 |
| 38 | UBAFIL | BIGINT | 保留列，暂无意义，显示为 NULL |
| 39 | UBABLK | BIGINT | 保留列，暂无意义，显示为 NULL |
| 40 | UBAREC | BIGINT | 保留列，暂无意义，显示为 NULL |
| 41 | UBASQN | BIGINT | 保留列，暂无意义，显示为 NULL |
| 42 | ABS\_FILE# | INTEGER | 保留列，暂无意义，显示为 NULL |
| 43 | REL\_FILE# | INTEGER | 保留列，暂无意义，显示为 NULL |
| 44 | DATA\_BLK# | INTEGER | 保留列，暂无意义，显示为 NULL |
| 45 | DATA\_OBJ# | INTEGER | 对象 ID 号 |
| 46 | DATA\_OBJV# | INTEGER | 对象版本号 |
| 47 | DATA\_OBJD# | INTEGER | 保留列，暂无意义，显示为 NULL |
| 48 | SQL\_REDO | VARCHAR(4000) | 客户端发送给数据库的 SQL 语句 |
| 49 | SQL\_UNDO | VARCHAR(4000) | 回滚 SQL 语句。该列结果受 INI 参数 RLOG\_APPEND\_LOGIC 影响。 当 RLOG\_APPEND\_LOGIC 为 1 时，支持挖掘 INSERT 类型的 UNDO 语句，如果表含有主键列，则不能挖掘 DELETE、UPDATE 类型的语句，否则可挖掘； 当 RLOG\_APPEND\_LOGIC 为 2 时，支持挖掘 INSERT、DELETE、UPDATE 类型的 UNDO 语句； 当 RLOG\_APPEND\_LOGIC 为 3 时，仅支持挖掘 INSERT 类型的 UNDO 语句； 当 RLOG\_APPEND\_LOGIC 为 4 时，不支持挖掘 INSERT、DELETE、UPDATE 类型的 UNDO 语句 |
| 50 | RS\_ID | VARCHAR(32) | 记录集 ID |
| 51 | SSN | INTEGER | 连续 SQL 标志。如果 SQL 长度超过单个 sql\_redo 字段能存储的长度，则 SQL 会被截断成多个 SQL 片段在结果集中“连续”返回 |
| 52 | CSF | INTEGER | 与 SSN 配合，最后一个片段的 csf 值为 0，其余片段的值均为 1。没因超长发生截断的 SQL 该字段值均为 0。 |
| 53 | INFO | VARCHAR(32) | 保留列，暂无意义，显示为 NULL |
| 54 | STATUS | INTEGER | 保留列，暂无意义，显示为 NULL |
| 55 | REDO\_VALUE | BIGINT | 用于数据挖掘新值 |
| 56 | UNDO\_VALUE | BIGINT | 用于数据挖掘旧值 |
| 57 | SAFE\_RESUME\_SCN | BIGINT | 保留列，暂无意义，显示为 NULL |
| 58 | CSCN | BIGINT | 与 COMMITSCN 一样，已过时 |
| 59 | OBJECT\_ID | BINARY(16) | 保留列，暂无意义，显示为 NULL |
| 60 | EDITION\_NAME | VARCHAR(30) | 保留列，暂无意义，显示为 NULL |
| 61 | CLIENT\_ID | VARCHAR(64) | 保留列，暂无意义，显示为 NULL |
| 62 | SUBTAB\_ID | INTEGER | 子表 ID |
| 63 | SRC\_RAFT\_ID | INTEGER | 用于作为事务来源节点号 |

9） **V$ARCH\_QUEUE**

显示当前归档任务队列信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ARCH\_TYPE | VARCHAR(32) | 归档类型:LOCAL; REALTIME; TIMELY ASYN; REMOTE; |
| 2 | WAITING | INTEGER | 等待处理任务数 |
| 3 | READY | BIGINT | 已处理任务数 |
| 4 | CUR\_WAIT\_TIME | INTEGER | 当前任务等待时间，单位毫秒 |
| 5 | MAX\_WAIT\_TIME | INTEGER | 最大任务等待时间，单位毫秒 |
| 6 | TOTAL\_WAIT\_TIME | BIGINT | 已处理任务的总等待时间，单位：毫秒 |
| 7 | AVERAGE\_WAIT\_TIME | INTEGER | 已处理任务的平均等待时间，单位：毫秒 |

10） **V$RLOG\_HISTORY**

显示日志的历史总体信息。通过该视图可以了解最近一周内系统每过一分钟日志事务号 LSN 的情况、归档日志情况以及检查点的执行情况等。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | RECORD\_TIME | DATETIME(6) | 记录产生的时间 |
| 2 | G\_NEXT\_SEQ | BIGINT | 全局日志包序号 |
| 3 | CUR\_LSN | BIGINT | 记录产生时，当前的 LSN |
| 4 | FLUSH\_LSN | BIGINT | 记录产生时，当前准备刷盘的 LSN |
| 5 | FILE\_LSN | BIGINT | 记录产生时，已经到盘上的 LSN |
| 6 | CKPT\_LSN | BIGINT | 记录产生时，最近一次检查点 LSN |
| 7 | FLUSH\_PAGES | BIGINT | 记录产生时，Flush 链表中的总页数 |
| 8 | FLUSHING\_PAGES | BIGINT | 记录产生时，正在刷盘的总页数 |
| 9 | TOTAL\_SPACE | BIGINT | 记录产生时，日志总空间，单位字节 |
| 10 | FREE\_SPACE | BIGINT | 记录产生时，目前可用的日志空间，单位字节 |
| 11 | CKPT\_FILE | INTEGER | 记录产生时，最近一次检查点对应的当时的文件号 |
| 12 | CKPT\_OFF | BIGINT | 记录产生时，最近一次检查点对应的当时的文件偏移 |
| 13 | CUR\_FILE | INTEGER | 记录产生时，记录刷文件前当前文件的 ID |
| 14 | CUR\_OFF | BIGINT | 记录产生时，记录刷文件前 cur\_file 的 free |
| 15 | RPKG\_MEM\_SIZE | BIGINT | 记录产生时，RLOG 上当前 PKG 分配的空间 |
| 16 | RPKG\_USED\_SIZE | BIGINT | 记录产生时，RLOG 上当前 PKG 使用的空间 |
| 17 | TOTAL\_FLUSH\_PAGES | BIGINT | 记录产生时，系统启动后累计刷盘的总页数 |
| 18 | TOTAL\_FLUSH\_TIMES | BIGINT | 记录产生时，系统启动后累计刷盘的总次数 |

11） **V$ELOG\_FILE**

显示 ELOG 日志的记录时间范围、大小、SITE\_ID 等信息。通过该视图可以了解当前实例的所有 ELOG 日志文件的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | FILE\_NAME | VARCHAR(128) | 日志文件名，包含文件类型 |
| 2 | SITE\_ID | INTEGER | 文件所属的站点的站点号，在 DPC 环境中为 RAFT\_ID，在 MPP 环境中为执行站点号 EPSEQ，在 DSC 环境中为节点号 |
| 3 | FILE\_SIZE | INTEGER | 日志文件大小，单位 MB，总大小不足 1MB 的按照 1MB 算 |
| 4 | FIRST\_REC\_TIME | DATETIME(6) | 日志文件内第一条记录的时间 |
| 5 | LAST\_REC\_TIME | DATETIME(6) | 日志文件内最后一条记录的时间 |

12） **V$RLOG\_FREE\_LIST**

显示日志空闲链表中的空闲日志包信息。

对于主库或 NORMAL 模式的库，如果开启了 RLOG\_PARALLEL\_ENABLE，则会显示每路并行日志的空闲链表信息，显示行数为 WORKER\_THREADS + 1，否则只显示 1 行。

其中 RLOG\_BUF\_SIZE 和 RLOG\_POOL\_SIZE 会结合日志并行信息、工作线程个数等因素再进行调整，不一定是 dm.ini 中的配置大小。

日志包内存分配关系说明如下：

（1）默认日志包大小 = RLOG\_BUF\_SIZE \* 512 字节。

（2）FREE\_RPKG\_LEN = FREE\_RPKG\_CNT \* 默认日志包大小，代表已分配但未使用的空闲空间。

（3）FREE\_RPKG\_LEN 一定不会超过 RLOG\_POOL\_SIZE 大小。

（4）已分配出的默认大小的日志包内存空间 = N\_ALLOC\_PAGE \* 512 字节，此空间大小大于等于 FREE\_RPKG\_LEN，但不会超过 RLOG\_POOL\_SIZE 大小。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | RLOG\_BUF\_SIZE | INTEGER | 单个日志缓冲区大小，以日志页个数为单位 |
| 2 | RLOG\_POOL\_SIZE | BIGINT | 最大日志缓冲区大小，单位字节 |
| 3 | N\_ALLOC\_PAGE | INTEGER | 空闲链表中已分配出的日志页个数 |
| 4 | FREE\_RPKG\_CNT | INTEGER | 空闲链表中存放的日志包个数 |
| 5 | FREE\_RPKG\_LEN | BIGINT | 空闲链表中存放的日志包总大小，单位字节 |

13） **V$LOG\_HISTORY**

服务器启动后，记录当前节点联机日志切换的历史信息。只记录最近 128 次切换记录。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | RECID | BIGINT | 记录 ID，表示联机日志发生的第 N 次切换 |
| 2 | RECTIME | DATETIME(0) | 联机日志切换时间 |
| 3 | FIL\_ID | INTEGER | 切换后的联机日志文件号 |
| 4 | CKPT\_LSN | BIGINT | 切换时的 CKPT\_LSN |
| 5 | FILE\_LSN | BIGINT | 切换时的 FILE\_LSN |
| 6 | CUR\_LSN | BIGINT | 切换时的 CUR\_LSN |

14） **V$ARCH\_BACKUP\_HISTORY**

服务器启动后，记录当前节点归档日志备份的历史信息。只记录最近 100 次备份记录。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | BEGIN\_ARCH\_PATH | VARCHAR(256) | 本次归档备份开始时的归档文件路径 |
| 2 | BEGIN\_LSN | BIGINT | 本次归档备份开始时的归档文件的 BEGIN\_LSN |
| 3 | BEGIN\_SEQ | BIGINT | 本次归档备份开始时的归档文件的 BEGIN\_SEQ |
| 4 | END\_ARCH\_PATH | VARCHAR(256) | 本次归档备份结束时的归档文件路径 |
| 5 | END\_LSN | BIGINT | 本次归档备份结束时的归档文件的 END\_LSN |
| 6 | END\_SEQ | BIGINT | 本次归档备份结束时的归档文件的 END\_SEQ |

15） **V$ARCH\_APPLY\_INFO**

主库或级联异步备库上记录的备库重演信息。重演信息来源于备库，且与备库上真实的重演信息存在 60s 延迟。如果本视图查不到信息，那么可能因为备库上无重演信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | DEST\_NAME | VARCHAR(512) | 归档目标名，如果备库是 DSC 集群，则打印控制节点实例名，若控制节点不存在，则打印归档对象字符串中首个归档对象实例名。 |
| 2 | ARCH\_STANDBY\_APPLY | INTEGER | DMARCH.INI 中归档目标的 ARCH\_STANDBY\_APPLY 配置 |
| 3 | DSC\_SEQNO | INTEGER | 重演信息对应的主库 DSC 节点号 |
| 4 | APPLY\_SEQNO | BIGINT | 备库刷盘到的日志包序号 |
| 5 | APPLY\_LSN | BIGINT | 备库刷盘到的最大 LSN |
| 6 | KEEP\_SEQNO | BIGINT | 备库保持不重演的最大日志包序号 |
| 7 | KEEP\_LSN | BIGINT | 备库保持不重演的最大 LSN |
| 8 | STANDBY\_SEQNO | BIGINT | 备库已接收到的最大日志包序号 |
| 9 | STANDBY\_LSN | BIGINT | 备库已接收到的最大 LSN |
| 10 | RPKG\_SEQNO | BIGINT | 备库已重演到的日志包序号 |
| 11 | RPKG\_LSN | BIGINT | 备库已重演到的 LSN |
| 12 | C\_SEQNO | BIGINT | 备库已提交到的日志包序号，仅在 DMDPC 的多副本系统中有效 |
| 13 | C\_LSN | BIGINT | 备库已提交到的 LSN，仅在 DMDPC 的多副本系统中有效 |

16. **V$ARCH\_FILE**

查询本地已经归档的日志信息。对 DMDSC 集群，除了显示本地归档外，也显示远程归档信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | DB\_MAGIC | BIGINT | 写入日志的数据库的 MAGIC 值 |
| 2 | STATUS | VARCHAR(64) | 归档日志状态 |
| 3 | LEN | BIGINT | 日志长度，单位为字节 |
| 4 | FREE | BIGINT | 写日志偏移位置 |
| 5 | ARCH\_LSN | BIGINT | 归档文件起始 LSN，仅对归档文件有意义 |
| 6 | CLSN | BIGINT | 已归档的最大 LSN |
| 7 | ARCH\_SEQ | BIGINT | 归档文件起始包序号，仅对归档文件有意义 |
| 8 | NEXT\_SEQ | BIGINT | 已归档的最大包序号。 |
| 9 | CREATE\_TIME | DATETIME(6) | 归档文件创建时间 |
| 10 | CLOSE\_TIME | DATETIME(6) | 归档文件关闭时间 |
| 11 | PATH | VARCHAR(256) | 归档文件所在路径，包括归档文件名 |
| 12 | PMNT\_MAGIC | BIGINT | 数据库的永久 MAGIC |
| 13 | DSC\_SEQNO | INTEGER | DSC 节点序号，单节点为 0 |
| 14 | CRC\_CHECK | INTEGER | 是否进行 CRC 校验 |
| 15 | LAST\_PKG\_OFF | BIGINT | 最后一个有效的日志包在文件中的偏移位置 |
| 16 | PREV\_LSN | BIGINT | 前一个归档文件已归档的最大 LSN |
| 17 | GLOBAL\_NEXT\_SEQ | BIGINT | 已归档的最大包序号 |
| 18 | SRC\_DB\_MAGIC | BIGINT | 产生日志的源数据库的 MAGIC 值 |
| 19 | LLOG\_FIRST\_TIME | DATETIME(6) | 归档文件中包含的第一条逻辑日志的生成时间，仅在开启逻辑日志时有效 |
| 20 | LLOG\_LAST\_TIME | DATETIME(6) | 归档文件中包含的最后一条逻辑日志的生成时间，仅在开启逻辑日志时有效 |

17） **V$ARCH\_FILE\_HISTORY**

当 INI 参数 ENABLE\_MONITOR=1 时，该视图显示因归档空间不足而被服务器主动删除的所有归档文件信息。

1. 此视图只能查询到已被服务器主动删除的归档文件信息，对于尚未被删除或者用户手动删除的归档文件则无法查询到；
2. 此视图最多能够查询到最近 10000 个被服务器主动删除的归档文件信息；
3. 若存在多路本地归档，则该视图的查询结果中将包含每一路本地归档下被删除的归档文件信息；
4. 此视图记录的归档文件历史信息是内存值，不会持久化到磁盘，因此服务器重启后将无法再查询到此前被删除的归档文件信息；
5. 可以通过系统过程 SP\_DYNAMIC\_VIEW\_DATA\_CLEAR 来清空此视图的历史信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | DSC\_SEQNO | INTEGER | DSC 节点序号，单节点为 0 |
| 2 | SRC\_DB\_MAGIC | BIGINT | 产生日志的源数据库的 MAGIC 值 |
| 3 | PMNT\_MAGIC | BIGINT | 数据库的永久 MAGIC |
| 4 | DB\_MAGIC | BIGINT | 写入日志的数据库的 MAGIC 值 |
| 5 | CREATE\_TIME | DATETIME(6) | 归档文件创建时间 |
| 6 | CLOSE\_TIME | DATETIME(6) | 归档文件关闭时间 |
| 7 | DELETE\_TIME | DATETIME(6) | 归档文件删除时间 |
| 8 | LEN | BIGINT | 日志长度，单位为字节 |
| 9 | FREE | BIGINT | 写日志偏移位置 |
| 10 | ARCH\_LSN | BIGINT | 归档文件起始 LSN |
| 11 | LSN | BIGINT | 已归档的最大 LSN |
| 12 | ARCH\_SEQ | BIGINT | 归档文件起始包序号 |
| 13 | NEXT\_SEQ | BIGINT | 已归档的最大包序号 |
| 14 | PATH | VARCHAR(256) | 归档文件所在路径，包括归档文件名 |

**18）** **V$ARCH\_FILE2**

查询本地已经归档的日志信息。对 DMDSC 集群，除了显示本地归档外，也显示远程归档信息，若存在故障节点，查询 V$ARCH\_FILE 视图，可以显示故障节点的归档信息，而 V$ARCH\_FILE2 中无法显示故障节点的归档信息。

V$ARCH\_FILE2 展示的字段与 V$ARCH\_FILE 相同。V$ARCH\_FILE2 中的信息从缓存中获取，查询速度更快，但是可能存在一定的延时问题，可能会导致处于 ACTIVIE 状态下的某些字段与查询 V$ARCH\_FILE 视图展示的结果不一致。若想获得即时的归档日志信息，请查询 V$ARCH\_FILE。如果手动删除归档日志文件，目前缓存中还会保留已删除的文件信息，即查询 V$ARCH\_FILE2 视图也会展示已经删除的归档日志文件信息，会导致查询 V$ARCH\_FILE2 与 V$ARCH\_FILE2 结果不一致。

#### 7\. 会话

1） **V$CONNECT**

显示活动连接的所有信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 连接名称 |
| 2 | SADDR | BIGINT | 会话地址 |
| 3 | CREATE\_TIME | DATETIME(0) | 会话创建时间 |
| 4 | STATUS$ | VARCHAR(128) | 连接状态 |
| 5 | TYPE$ | VARCHAR(128) | 连接类型，可能有如下取值：ODBC、SQL3、JDBC、.NET PROVIDER、PYTHON、GO、NODEJS、DCI、DCCI、PHP、UNKNOWN |
| 6 | PROTOCOL\_TYPE | TINYINT | 协议类型，取值 1 表示 TCP |
| 7 | IP\_ADDR | VARCHAR(192) | IP 地址 |

2） **V$SESSIONS**

显示当前数据库中所有会话的信息，如执行的 sql 语句、主机名、当前会话状态、用户名等等。本视图中时间相关的字段均按服务器端进行记录。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SESS\_ID | BIGINT | 会话 ID，系统内部标识 |
| 2 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |
| 3 | SQL\_TEXT | VARCHAR(1000) | 对于会话当前正在执行的或最近一次执行的 SQL 语句，记录该 SQL 的前 1000 个字符 |
| 4 | STATE | VARCHAR(8) | 会话状态。   CREATE：创建，表示会话对象已创建，但还不能使用；   STARTUP：启动，表示会话正在启动中；   IDLE：空闲，表示会话当前没有执行操作；   ACTIVE：活动，表示会话当前正在执行操作；   PENDING：限流等待，当 INI 参数 MAX\_CONCURRENT\_TRX>0 时，会话可能会因为并行事务限流而处于此状态；   UNKNOWN：正在释放，表示会话正在被释放； |
| 5 | N\_STMT | INTEGER | 语句 STMT 的容量 |
| 6 | N\_USED\_STMT | INTEGER | 已使用的语句 STMT 数量 |
| 7 | SEQ\_NO | INTEGER | 会话上语句的序列号 |
| 8 | CURR\_SCH | VARCHAR(128) | 当前模式 |
| 9 | USER\_NAME | VARCHAR(128) | 当前用户 |
| 10 | TRX\_ID | BIGINT | 事务 id，0 表示事务未开始或事务已结束 |
| 11 | CREATE\_TIME | DATETIME(6) | 会话创建时间 |
| 12 | CLNT\_TYPE | VARCHAR(128) | 客户端类型，可能有如下取值：ODBC、SQL3、JDBC、.NET PROVIDER、PYTHON、GO、NODEJS、DCI、DCCI、PHP、UNKNOWN |
| 13 | TIME\_ZONE | VARCHAR(6) | 会话使用的时区 |
| 14 | CHK\_CONS | CHAR(1) | 会话是否忽略约束检查。'Y'：忽略约束检查，'N'：不忽略 |
| 15 | CHK\_IDENT | CHAR(1) | 会话是否忽略自增列指定列表检查。'Y'：是，'N'：否 |
| 16 | RDONLY | CHAR(1) | 是否为只读会话。'Y'：是，'N'：否 |
| 17 | INS\_NULL | CHAR(1) | 当列不存在 default 选项时，是否插入空值。'Y'：是，'N'：否 |
| 18 | COMPILE\_FLAG | CHAR(1) | 是否忽略编译选项，用于 VIEW、PROCEDURE、TRIGGER 等对象的编译。'Y'：是，'N'：否 |
| 19 | AUTO\_CMT | CHAR(1) | 会话是否为自动提交。'Y'：是，'N'：否 |
| 20 | DDL\_AUTOCMT | CHAR(1) | DDL 语句是否自动提交。'Y'：是，'N'：否 |
| 21 | RS\_FOR\_QRY | CHAR(1) | 是否为非查询语句生成结果集。'Y'：是，'N'：否 |
| 22 | CHK\_NET | CHAR(1) | 会话是否检查网络。'Y'：是，'N'：否 |
| 23 | ISO\_LEVEL | INTEGER | 隔离级别。0：读未提交；1：读提交；2：可重复读；3：串行化 |
| 24 | CLNT\_HOST | VARCHAR(128) | 客户端主机名 |
| 25 | APPNAME | VARCHAR(128) | 应用程序名 |
| 26 | CLNT\_IP | VARCHAR(128) | 客户端 IP |
| 27 | OSNAME | VARCHAR(128) | 客户端操作系统名 |
| 28 | CONN\_TYPE | VARCHAR(20) | 连接类型 |
| 29 | VPOOLADDR | BIGINT | 内存池的首地址 |
| 30 | RUN\_STATUS | VARCHAR(20) | 记录运行状态，可能值为"IDLE"或"RUNNING" |
| 31 | MSG\_STATUS | VARCHAR(20) | 记录消息处理状态，可能值为"RECEIVE"（已接受）或"SEND"（已发送） |
| 32 | LAST\_RECV\_TIME | DATETIME(6) | 会话最近一次接收消息的时间 |
| 33 | LAST\_SEND\_TIME | DATETIME(6) | 会话最近一次发送消息的时间 |
| 34 | DCP\_FLAG | CHAR(1) | 1) 是否是通过 DCP\_PORT 登录 DCP 服务器的会话，'Y'表示是，'N'表示否；   2) 是否是通过 DCP 代理连接到 MPP 的会话，'Y'表示是，'N'表示否 |
| 35 | THRD\_ID | INTEGER | 线程 ID |
| 36 | CONNECTED | INTEGER | 会话连接是否正常：1 表示连接正常；0 表示连接已经关闭 |
| 37 | PORT\_TYPE | INTEGER | 连接端口类型：   0 表示 TCP 连接；   1 表示 TCP 和 SSL 连接；   2 表示 NetIPC 连接；   3 表示连接已经关闭；   4 表示 UDP 连接；   5 表示 RDMA 连接；   6 表示 UNIXSOCKET 连接；   7 表示国密 GmSSL 连接 |
| 38 | SRC\_SITE | INTEGER | 源节点，65535 表示是本地 SESSION，其他值代表 MPP 集群用户直接登录的节点号 |
| 39 | MAL\_ID | BIGINT | 邮箱 ID |
| 40 | CONCURRENT\_FLAG | INTEGER | 是否占用了限流资源 ，1：是；0：否 |
| 41 | CUR\_LINENO | INTEGER | 记录存储过程执行时，当前执行的行号 |
| 42 | CUR\_MTDNAME | VARCHAR(128) | 记录存储过程执行时，当前执行的方法名 |
| 43 | CUR\_SQLSTR | VARCHAR(128) | 记录存储过程执行时，当前执行的 SQL 的前 100 个字符 |
| 44 | CLNT\_VER | VARCHAR(128) | 记录登录会话接口的程序的版本号 |
| 45 | SQL\_ID | INTEGER | SQL\_TEXT 对应的语句 ID，为-1 表示会话当前没有执行 SQL，SQL\_TEXT 中显示的 SQL 为上次执行的 SQL 信息 |
| 46 | EID | BIGINT | 在 DPC 环境下会话的全局 ID |
| 47 | CLIENT\_INFO | VARCHAR(64) | 记录通过系统包方法 dbms\_application\_info.set\_client\_info('当前会话的客户端信息')设置的当前会话的客户端信息 |
| 48 | CLIENT\_IDENTIFIER | VARCHAR(64) | 记录通过系统包方法 dbms\_session.set\_identifier('当前会话 ID')设置的当前会话 ID |
| 49 | MODULE | VARCHAR(64) | 记录通过系统包方法 dbms\_application\_info.set\_module()设置的当前会话运行的模块名称 |
| 50 | ACTION | VARCHAR(64) | 记录通过系统包方法 dbms\_application\_info.set\_action('当前模块正在执行的事务名称')设置的当前模块正在执行的事务名称 |
| 51 | HEART\_BEAT\_INTERVAL | INTEGER | 会话的连接心跳间隔，单位：秒 |
| 52 | HEART\_BEAT\_TIMEOUT | INTEGER | 会话的连接心跳超时时间，单位：秒 |
| 53 | TMP\_USED\_TYPE | VARCHAR(128) | 记录会话中使用的临时表空间的类型（如 BTR、BLOB、MTAB、BACKUP 等），存在多个类型时，不同类型用“/”隔开（如 BTR/BLOB） |
| 54 | TMP\_USED\_EXTENT\_NUM | INTEGER | 记录会话中使用的临时表空间所占用的总簇数 |
| 55 | SQL\_TEXT\_ID | VARCHAR(13) | 会话当前正在执行的或最近一次执行的 SQL 语句固定的散列字符 |
| 56 | LOGIN\_PWD\_FLAG | VARCHAR(8) | 会话登录方式。   NORMAL：主密码登录；   OLDPWD：辅助密码登录；   OTHERS：其他方式登录 |
| 57 | VM\_COUNT | INTEGER | 会话的虚拟机个数 |
| 58 | PREV\_SQL\_ID | INTEGER | 会话上次执行的 SQL 语句对应 ID |
| 59 | PREV\_SQL\_TEXT\_ID | VARCHAR(13) | 会话上次执行的 SQL 语句对应 SQL\_TEXT\_ID |

3） **GV$SESSIONS**

显示全局会话的具体信息，如执行的 sql 语句、主机名、当前会话状态、用户名等等。本视图中时间相关的字段均按服务器端进行记录。

支持的集群有 DPC、DSC、实时主备、读写分离集群、AFC。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INSTANCE\_NAME | VARCHAR(128) | 实例名 |
| 2 | SESS\_ID | BIGINT | 会话 ID，系统内部标识 |
| 3 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |
| 4 | SQL\_TEXT | VARCHAR(1000) | 对于会话当前正在执行的或最近一次执行的 SQL 语句，记录该 SQL 的头 1000 个字符 |
| 5 | STATE | VARCHAR(8) | 会话状态。共 6 种状态：CREATE 创建、STARTUP 启动、IDLE 空闲、ACTIVE 活动、PENDING 限流等待、UNKNOWN 正在释放 |
| 6 | N\_STMT | INTEGER | 语句 STMT 的容量 |
| 7 | N\_USED\_STMT | INTEGER | 已使用的语句 STMT 数量 |
| 8 | SEQ\_NO | INTEGER | 会话上语句的序列号 |
| 9 | CURR\_SCH | VARCHAR(128) | 当前模式 |
| 10 | USER\_NAME | VARCHAR(128) | 当前用户 |
| 11 | TRX\_ID | BIGINT | 事务 id |
| 12 | CREATE\_TIME | DATETIME(6) | 会话创建时间 |
| 13 | CLNT\_TYPE | VARCHAR(128) | 客户端类型，可能有如下取值：ODBC、SQL3、JDBC、.NET PROVIDER、PYTHON、GO、NODEJS、DCI、DCCI、PHP、UNKNOWN |
| 14 | TIME\_ZONE | VARCHAR(6) | 会话使用的时区 |
| 15 | CHK\_CONS | CHAR(1) | 会话是否忽略约束检查。'Y'：忽略约束检查，'N'：不忽略 |
| 16 | CHK\_IDENT | CHAR(1) | 会话是否忽略自增列指定列表检查。'Y'：忽略约束检查，'N'：不忽略 |
| 17 | RDONLY | CHAR(1) | 是否为只读会话。'Y'：是，'N'：否 |
| 18 | INS\_NULL | CHAR(1) | 当列不存在 default 选项，是否插入空值。'Y'：是，'N'：否 |
| 19 | COMPILE\_FLAG | CHAR(1) | 是否忽略编译选项，用于 VIEW、PROCEDURE、TRIGGER 等对象的编译。'Y'：是，'N'：否 |
| 20 | AUTO\_CMT | CHAR(1) | 会话是否为自动提交。'Y'：是，'N'：否 |
| 21 | DDL\_AUTOCMT | CHAR(1) | DDL 语句是否自动提交。'Y'：是，'N'：否 |
| 22 | RS\_FOR\_QRY | CHAR(1) | 是否为非查询语句生成结果集。'Y'：是，'N'：否 |
| 23 | CHK\_NET | CHAR(1) | 会话是否检查网络。'Y'：是，'N'：否 |
| 24 | ISO\_LEVEL | INTEGER | 隔离级别。0：读未提交；1：读提交；2：可重复读；3：串行化 |
| 25 | CLNT\_HOST | VARCHAR(128) | 客户端主机名 |
| 26 | APPNAME | VARCHAR(128) | 应用程序名 |
| 27 | CLNT\_IP | VARCHAR(128) | 客户端 IP |
| 28 | OSNAME | VARCHAR(128) | 客户端操作系统名 |
| 29 | CONN\_TYPE | VARCHAR(20) | 连接类型 |
| 30 | VPOOLADDR | BIGINT | 内存池的首地址 |
| 31 | RUN\_STATUS | VARCHAR(20) | 记录运行状态，可能值为"IDLE"或"RUNNING" |
| 32 | MSG\_STATUS | VARCHAR(20) | 记录消息处理状态，可能值为"RECEIVE"（已接受）或"SEND"（已发送） |
| 33 | LAST\_RECV\_TIME | DATETIME(6) | 会话最近一次接收消息的时间 |
| 34 | LAST\_SEND\_TIME | DATETIME(6) | 会话最近一次发送消息的时间 |
| 35 | DCP\_FLAG | CHAR(1) | 1) 是否是通过 DCP\_PORT 登录 DCP 服务器的会话，'Y'表示是，'N'表示否；   2) 是否是通过 DCP 代理连接到 MPP 的会话，'Y'表示是，'N'表示否 |
| 36 | THRD\_ID | INTEGER | 线程 ID |
| 37 | CONNECTED | INTEGER | 会话连接是否正常：1 表示连接正常，0 表示连接已经关闭 |
| 38 | PORT\_TYPE | INTEGER | 连接端口类型：2 表示 TCP 连接，12 表示端口已经关闭，13 表示 UDP 连接 |
| 39 | SRC\_SITE | INTEGER | 源节点，65535 表示是本地 SESSION，其他值代表 MPP 集群用户直接登录的节点号 |
| 40 | MAL\_ID | BIGINT | 邮箱 ID |
| 41 | CONCURRENT\_FLAG | INTEGER | 是否占用了限流资源 ，1：是；0：否 |
| 42 | CUR\_LINENO | INTEGER | 记录存储过程执行时，当前执行的行号 |
| 43 | CUR\_MTDNAME | VARCHAR(128) | 记录存储过程执行时，当前执行的方法名 |
| 44 | CUR\_SQLSTR | VARCHAR(128) | 记录存储过程执行时，当前执行的方法名 |
| 45 | CLNT\_VER | VARCHAR(128) | 记录登录会话接口的程序的版本号 |
| 46 | SYSDATE | DATETIME(0) | 数据库服务器所在操作系统的当前日期时间 |

4） **V$SESSION\_SYS**

显示系统当前会话的一些状态统计信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | N\_SESS | INTEGER | 会话个数 |
| 2 | N\_FREEING | INTEGER | 正在释放的会话个数 |
| 3 | ALLOW\_NEW\_LOGIN | INTEGER | 是否允许登录 |
| 4 | MAX\_CONCURRENT\_TRX | INTEGER | 限流的最大并行数 |
| 5 | CONCURRENT\_TRX\_MODE | INTEGER | 预留参数，暂无意义 |
| 6 | CURR\_CONCURRENT\_TRX | INTEGER | 可用资源 |
| 7 | N\_WAIT | INTEGER | 等待执行的任务数 |

5） **GV$SESSION\_SYS**

显示系统全局会话的一些状态统计信息。

支持的集群有 DPC、DSC、实时主备、读写分离集群、AFC。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INSTANCE\_NAME | VARCHAR(128) | 实例名 |
| 2 | N\_SESS | INTEGER | 会话个数 |
| 3 | N\_FREEING | INTEGER | 正在释放的会话个数 |
| 4 | ALLOW\_NEW\_LOGIN | INTEGER | 是否允许登录 |
| 5 | MAX\_CONCURRENT\_TRX | INTEGER | 限流的最大并行数 |
| 6 | CONCURRENT\_TRX\_MODE | INTEGER | 预留参数，暂无意义 |
| 7 | CURR\_CONCURRENT\_TRX | INTEGER | 可用资源 |
| 8 | N\_WAIT | INTEGER | 等待执行的任务数 |

6） **V$OPEN\_STMT**

连接语句句柄表，用于记录 SESSION 上语句句柄的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SESS\_ADDR | VARBINARY(8) | SESSION 地址 |
| 2 | SESSION# | INTEGER | SESSION 的 ID |
| 3 | STMT\_ID | INTEGER | STMT 的 ID |
| 4 | STMT\_SEQNO | INTEGER | STMT 的执行序号 |
| 5 | TYPE | VARCHAR(32) | 语句类型 |
| 6 | REP\_TYPE | VARCHAR(32) | 复制语句类型 |
| 7 | EXEC\_DIRECT | CHAR(1) | 是否直接执行 |
| 8 | PLN\_ADDR | VARBINARY(8) | 执行计划的地址 |
| 9 | ROWCOUNT | BIGINT | 影响记录的行数 |
| 10 | ROWCOUNT\_FOR\_DML | BIGINT | DML 影响的行数 |
| 11 | ROWCOUNT\_REQUEST | BIGINT | 请求的行数 |
| 12 | BATCH\_FLAG | CHAR(1) | 批量处理标识 |
| 13 | N\_PARA\_ROWS | INTEGER | 多行参数时的行数 |
| 14 | NTH\_PARA\_ROW | INTEGER | 多行参数时的当前行序号 |
| 15 | CUR\_PARA\_OFF | INTEGER | 参数的当前偏移 |
| 16 | PARA\_BUF | VARBINARY(8) | 参数的内存地址 |
| 17 | SQL\_STR | VARCHAR(1000) | 执行语句的前 1000 个字符 |
| 18 | BPARAM\_CAN\_OPT | CHAR(1) | 绑定批量参数时是否可优化 |
| 19 | CURSOR\_FORWARD\_ONLY | CHAR(1) | 对应游标是否 FORWARD\_ONLY |
| 20 | CURSOR\_NAME | VARCHAR(128) | 对应游标名 |
| 21 | CURSOR\_KEEP\_NAME | CHAR(1) | 对应游标是否保存名字 |
| 22 | CURSOR\_REF\_ID | INTEGER | 引用游标语句句柄 ID |
| 23 | CURSOR\_REF\_SEQNO | INTEGER | 引用语句的执行序号 |
| 24 | MPP\_EXEC\_ID | BIGINT | MPP 下的执行 ID |
| 25 | VM\_ADDR | VARBINARY(8) | VM 地址 |
| 26 | DBG\_FLAG | CHAR(1) | 是否 DEBUG |
| 27 | STMT\_DBG | VARBINARY(8) | DEBUG 的语句句柄地址 |
| 28 | MPP\_DDL\_FLAG | CHAR(1) | MPP 下 DDL 标识 |
| 29 | REMOTE\_OPERATION | CHAR(1) | 是否是 DBLINK 的远程操作 |
| 30 | RS\_BDTA\_FLAG | CHAR(1) | 返回的结果集是否直接将 BDTA 打包 |
| 31 | RS\_BDTA\_SIZE | INTEGER | 返回的打包结果集时最大的行数 |
| 32 | STMT\_LINK | VARBINARY(8) | 用于串连语句的链表地址 |
| 33 | LPQ | VARBINARY(8) | 并行查询地址 |
| 34 | RS\_INFO | VARBINARY(8) | 结果集地址 |
| 35 | MPLN\_ADDR | VARBINARY(8) | 从 EP 上保留 MPLN |
| 36 | BIND\_PARAM | VARBINARY(8) | 绑定参数地址 |
| 37 | BAK\_SYS | VARBINARY(8) | 备份链表信息 |
| 38 | RT\_STACK | VARBINARY(8) | MPP 从 EP 的运行时信息堆栈 |

7） **V$SESSION\_HISTORY**

显示当前会话历史的记录信息，如主机名、用户名等，与 V$SESSIONS 的区别在于会话历史记录只记录了会话一部分信息，对于一些动态改变的信息没有记录，如执行的 SQL 语句等。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SESS\_ID | BIGINT | 会话 ID，系统内部标识 |
| 2 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |
| 3 | CURR\_SCH | VARCHAR(128) | 当前模式 |
| 4 | USER\_NAME | VARCHAR(128) | 当前用户 |
| 5 | CREATE\_TIME | DATETIME(6) | 会话创建时间 |
| 6 | CLNT\_TYPE | VARCHAR(128) | 客户类型，可能有如下取值：ODBC、SQL3、JDBC、.NET PROVIDER、PYTHON、GO、NODEJS、DCI、DCCI、PHP、UNKNOWN |
| 7 | TIME\_ZONE | VARCHAR(6) | 时区 |
| 8 | RDONLY | CHAR(1) | 是否是只读会话 |
| 9 | DDL\_AUTOCMT | CHAR(1) | DDL 语句是否自动提交 |
| 10 | RS\_FOR\_QRY | CHAR(1) | 非查询语句生成结果集标记 |
| 11 | CHK\_NET | CHAR(1) | 是否检查网络 |
| 12 | CLNT\_HOST | VARCHAR(128) | 客户主库名 |
| 13 | APPNAME | VARCHAR(128) | 应用程序名 |
| 14 | CLNT\_IP | VARCHAR(128) | 客户端 IP |
| 15 | OSNAME | VARCHAR(128) | 客户端操作系统名 |
| 16 | CONN\_TYPE | VARCHAR(20) | 连接类型 |

8） **GV$SESSION\_HISTORY**

显示全局会话历史的记录信息，如主机名、用户名等，与 V$SESSIONS 的区别在于会话历史记录只记录了会话一部分信息，对于一些动态改变的信息没有记录，如执行的 SQL 语句等。

支持的集群有 DPC、DSC、实时主备、读写分离集群、AFC。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INSTANCE\_NAME | VARCHAR(128) | 实例名 |
| 2 | SESS\_ID | BIGINT | 会话 ID，系统内部标识 |
| 3 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |
| 4 | CURR\_SCH | VARCHAR(128) | 当前模式 |
| 5 | USER\_NAME | VARCHAR(128) | 当前用户 |
| 6 | CREATE\_TIME | DATETIME(6) | 会话创建时间 |
| 7 | CLNT\_TYPE | VARCHAR(128) | 客户类型，可能有如下取值：ODBC、SQL3、JDBC、.NET PROVIDER、PYTHON、GO、NODEJS、DCI、DCCI、PHP、UNKNOWN |
| 8 | TIME\_ZONE | VARCHAR(6) | 时区 |
| 9 | RDONLY | CHAR(1) | 是否是只读会话 |
| 10 | DDL\_AUTOCMT | CHAR(1) | DDL 语句是否自动提交 |
| 11 | RS\_FOR\_QRY | CHAR(1) | 非查询语句生成结果集标记 |
| 12 | CHK\_NET | CHAR(1) | 是否检查网络 |
| 13 | CLNT\_HOST | VARCHAR(128) | 客户主库名 |
| 14 | APPNAME | VARCHAR(128) | 应用程序名 |
| 15 | CLNT\_IP | VARCHAR(128) | 客户端 IP |
| 16 | OSNAME | VARCHAR(128) | 客户端操作系统名 |
| 17 | CONN\_TYPE | VARCHAR(20) | 连接类型 |

9） **V$CONTEXT**

显示当前会话所有上下文的名字空间、属性和值。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAMESPACE | VARCHAR(30) | 上下文名字空间 |
| 2 | ATTRIBUTE | VARCHAR(30) | 名字空间属性 |
| 3 | VALUE | VARCHAR(4000) | 属性值 |

10） **V$NLS\_PARAMETERS**

显示当前会话的日期时间格式、日期时间语言以及自然语言的排序方式。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PARAMETER | VARCHAR(128) | 当前会话的属性：目前只支持日期串语言、日期串格式以及自然语言的排序方式 |
| 2 | VALUE | VARCHAR(128) | 当前会话的属性值 |

在没有设置 NLS\_\*\_FORMAT 情况下，显示为 NULL，则说明使用默认格式（无会话格式、会话格式没有默认格式）。DM 默认格式为：DATE 格式是"YYYY-MM-DD"；TIME 格式是"HH24:MI:SS.FF"；TIMESTAMP 格式是"YYYY-MM-DD HH24:MI:SS.FF"；TIMESTAMP WITH TIME ZONE 格式是"YYYY-MM-DD HH24:MI:SS.FF TZH:TZM"；TIME WITH TIME ZONE 格式是"HH24:MI:SS.FF TZH:TZM"。

默认格式的解析逻辑为：上述格式中的分、秒、毫秒、时区分量都会依次尝试解析，都允许从后往前完整省略后续分量，直到最后一个分量“时区”或整个源串解析完成。分钟及其之后的分量可以一起省略。若源串解析完对应分量后，仍存在未解析的冗余字符，则根据 COMPATIBLE\_MODE 的值判断是否进行报错：当 COMPATIBLE\_MODE=0（达梦默认）或者 2（兼容 ORACLE）时直接报错；当 COMPATIBLE\_MODE=4（兼容 MYSQL）或者 7（兼容 PG）时成功。

11） **V$ACTIVE\_SESSION\_HISTORY**

当 INI 参数 ENABLE\_MONITOR=1 时，显示当前活动会话的等待信息，保留 1 万条数据。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SAMPLE\_ID | BIGINT | 采样 ID |
| 2 | SAMPLE\_TIME | DATETIME(3) | 采样时戳 |
| 3 | IS\_AWR\_SAMPLE | VARCHAR(1) | 是否已经刷盘或者即将刷盘(Y/N) |
| 4 | SESSION\_ID | BIGINT | 会话 ID |
| 5 | SESSION\_SERIAL# | INTEGER | 会话序列号，用来唯一标识会话 |
| 6 | SESSION\_TYPE | VARCHAR(10) | FOREGROUND/BACKGROUND   FOREGROUND 表示用户创建的会话；   BACKGROUND 表示系统内部创建的会话 |
| 7 | USER\_ID | INTEGER | 当前用户 ID |
| 8 | SQL\_ID | INTEGER | 采样时正在执行的 SQL 语句 ID |
| 9 | IS\_SQLID\_CURRENT | VARCHAR(1) | SQL\_ID 列所标识的语句是否正在执行(Y/N) |
| 10 | SQL\_OPCODE | INTEGER | SQL 语句类型 |
| 11 | SQL\_OPNAME | VARCHAR(64) | SQL 语句类型名 |
| 12 | TOP\_LEVEL\_SQL\_ID | INTEGER | 顶层 SQL 语句 ID |
| 13 | TOP\_LEVEL\_SQL\_OPCODE | INTEGER | 顶层 SQL 语句类型 |
| 14 | SQL\_EXEC\_ID | BIGINT | SQL 执行 ID |
| 15 | EVENT | VARCHAR(64) | 如果 SESSION\_STATE=WAITING,则表示会话在采样时的等待事件，否则为 NULL |
| 16 | EVENT\_ID | SMALLINT | 采样时等待事件的 ID |
| 17 | EVENT# | SMALLINT | 会话正在等待或者会话上次等待的资源或事件编号 |
| 18 | P1TEXT | VARCHAR(64) | 等待事件对应的参数 1 说明 |
| 19 | P1 | VARCHAR(256) | 等待事件对应的参数 1 值 |
| 20 | P2TEXT | VARCHAR(64) | 等待事件对应的参数 2 说明 |
| 21 | P2 | BIGINT | 等待事件对应的参数 2 值 |
| 22 | P3TEXT | VARCHAR(64) | 等待事件对应的参数 3 说明 |
| 23 | P3 | BIGINT | 等待事件对应的参数 3 值 |
| 24 | P4TEXT | VARCHAR(64) | 等待事件对应的参数 4 说明 |
| 25 | P4 | BIGINT | 等待事件对应的参数 4 值 |
| 26 | WAIT\_CLASS | VARCHAR(64) | 等待会话在采样时等待的事件的类名 |
| 27 | WAIT\_CLASS\_ID | INTEGER | 等待会话在采样时等待的事件的类 ID |
| 28 | WAIT\_TIME | BIGINT | 如果是在 SESSION\_STATE=ON CPU 采样，则表示会话上次等待的事件的总等待时间，单位微秒，否则为 0 |
| 29 | SESSION\_STATE | VARCHAR(7) | WAITING/ON CPU |
| 30 | TIME\_WAITED | BIGINT | 如果 SESSION\_STATE=WAITING，则表示会话实际花费在等待该事件的时间，单位微秒 |
| 31 | TRX\_ID | BIGINT | 采样时的事务 ID |
| 32 | PROGRAM | VARCHAR(128) | 程序名 |
| 33 | MODULE | VARCHAR(64) | 采样时执行模块的名称(DBMS\_APPLICATION\_INFO.SET\_MODULE) |
| 34 | ACTION | VARCHAR(64) | 采样时执行模块的动作(DBMS\_APPLICATION\_INFO.SET\_ACTION) |
| 35 | CLIENT\_ID | VARCHAR(64) | 客户端标识 |
| 36 | MACHINE | VARCHAR(128) | 客户端的机器名 |
| 37 | PORT | INTEGER | 客户端的端口号 |

12） **GV$ACTIVE\_SESSION\_HISTORY**

当 INI 参数 ENABLE\_MONITOR=1 时，显示全局活动会话的等待信息。

目前仅支持 DSC 集群。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INSTANCE\_NAME | VARCHAR(128) | 实例名 |
| 2 | SAMPLE\_ID | BIGINT | 采样 ID |
| 3 | SAMPLE\_TIME | DATETIME(3) | 采样时戳 |
| 4 | IS\_AWR\_SAMPLE | VARCHAR(1) | 是否已经刷盘或者即将刷盘(Y/N) |
| 5 | SESSION\_ID | BIGINT | 会话 ID |
| 6 | SESSION\_SERIAL# | INTEGER | 会话序列号，用来唯一标识会话 |
| 7 | SESSION\_TYPE | VARCHAR(10) | FOREGROUND/BACKGROUND FOREGROUND 表示用户创建的会话；BACKGROUND 表示系统内部创建的会话 |
| 8 | USER\_ID | INTEGER | 当前用户 ID |
| 9 | SQL\_ID | INTEGER | 采样时正在执行的 SQL 语句 ID |
| 10 | IS\_SQLID\_CURRENT | VARCHAR(1) | SQL\_ID 列所标识的语句是否正在执行(Y/N) |
| 11 | SQL\_OPCODE | INTEGER | SQL 语句类型 |
| 12 | SQL\_OPNAME | VARCHAR(64) | SQL 语句类型名 |
| 13 | TOP\_LEVEL\_SQL\_ID | INTEGER | 顶层 SQL 语句 ID |
| 14 | TOP\_LEVEL\_SQL\_OPCODE | INTEGER | 顶层 SQL 语句类型 |
| 15 | SQL\_EXEC\_ID | BIGINT | SQL 执行 ID |
| 16 | EVENT | VARCHAR(64) | 如果 SESSION\_STATE=WAITING,则表示会话在采样时的等待事件。否则为 NULL |
| 17 | EVENT\_ID | SMALLINT | 采样时等待事件的 ID |
| 18 | EVENT# | SMALLINT | 会话正在等待或者会话上次等待的资源或事件编号 |
| 19 | P1TEXT | VARCHAR(64) | 等待事件对应的参数 1 说明 |
| 20 | P1 | VARCHAR(256) | 等待事件对应的参数 1 值 |
| 21 | P2TEXT | VARCHAR(64) | 等待事件对应的参数 2 说明 |
| 22 | P2 | BIGINT | 等待事件对应的参数 2 值 |
| 23 | P3TEXT | VARCHAR(64) | 等待事件对应的参数 3 说明 |
| 24 | P3 | BIGINT | 等待事件对应的参数 3 值 |
| 25 | P4TEXT | VARCHAR(64) | 等待事件对应的参数 4 说明 |
| 26 | P4 | BIGINT | 等待事件对应的参数 4 值 |
| 27 | WAIT\_CLASS | VARCHAR(64) | 等待会话在采样时等待的事件的类名 |
| 28 | WAIT\_CLASS\_ID | INTEGER | 等待会话在采样时等待的事件的类 ID |
| 29 | WAIT\_TIME | BIGINT | 如果是在 SESSION\_STATE=ON CPU 采样，则表示会话上次等待的事件的总等待时间，单位微秒，否则为 0 |
| 30 | SESSION\_STATE | VARCHAR(7) | WAITING/ON CPU |
| 31 | TIME\_WAITED | BIGINT | 如果 SESSION\_STATE=WAITING，则表示会话实际花费在等待该事件的时间，单位微秒 |
| 32 | TRX\_ID | BIGINT | 采样时的事务 ID |
| 33 | PROGRAM | VARCHAR(128) | 程序名 |
| 34 | MODULE | VARCHAR(64) | 采样时执行模块的名称(DBMS\_APPLICATION\_INFO.SET\_MODULE) |
| 35 | ACTION | VARCHAR(64) | 采样时执行模块的动作(DBMS\_APPLICATION\_INFO.SET\_ACTION) |
| 36 | CLIENT\_ID | VARCHAR(64) | 客户端标识 |
| 37 | MACHINE | VARCHAR(128) | 客户端的机器名 |
| 38 | PORT | INTEGER | 客户端的端口号 |

#### 8\. SQL 执行相关

1） **V$SQL\_HISTORY**

当 INI 参数 ENABLE\_MONITOR=1 时，显示执行 sql 的历史记录信息；可以方便用户经常使用的记录进行保存。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SEQ\_NO | INTEGER | 序列号 |
| 2 | SQL\_ID | INTEGER | SQL 语句 ID |
| 3 | SESS\_ID | BIGINT | 会话 ID，系统内部标识 |
| 4 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |
| 5 | TRX\_ID | BIGINT | 事务 ID |
| 6 | THREAD\_ID | BIGINT | 线程 ID |
| 7 | TOP\_SQL\_TEXT | VARCHAR(1000) | 栈帧中第一个 SQL |
| 8 | SEC\_SQL\_TEXT | VARCHAR(1000) | 栈帧中第二个 SQL |
| 9 | THRD\_SQL\_TEXT | VARCHAR(1000) | 栈帧中第三个 SQL |
| 10 | START\_TIME | DATETIME(6) | SQL 执行的起始时间 |
| 11 | TIME\_USED | BIGINT | SQL 执行所使用时间（usec），单位为微秒（us） |
| 12 | IS\_OVER | CHAR(1) | 是否结束 |
| 13 | EXEC\_ID | BIGINT | SQL 执行 ID |
| 14 | VM | BIGINT | 执行 SQL 的虚拟机地址 |
| 15 | STKFRM | BIGINT | 当前的栈帧 |
| 16 | STK\_LEVEL | INTEGER | 当前栈帧的级别 |
| 17 | BYTES\_DYNAMIC\_ALLOCED | BIGINT | 动态分配字节数 |
| 18 | BYTES\_DYNAMIC\_FREED | BIGINT | 动态释放字节数 |
| 19 | CUR\_SQL\_NODE | BIGINT | 当前的 SQL 节点地址 |
| 20 | MAL\_ID | BIGINT | 邮件标识号 |
| 21 | N\_LOGIC\_READ | INTEGER | 语句逻辑读的次数 |
| 22 | N\_PHY\_READ | INTEGER | 语句物理读的次数 |
| 23 | AFFECTED\_ROWS | INTEGER | 语句影响的行数 |
| 24 | HARD\_PARSE\_FLAG | INTEGER | 语句硬解析标记，0：软解析；1：语义解析；2：硬解析 |
| 25 | MPP\_EXEC\_ID | BIGINT | MPP 会话句柄上的执行序号，同一个会话上的每个节点上值相同 |
| 26 | COMMAND\_TYPE | INTEGER | SQL 语句的类型 |
| 27 | IS\_SQC | INTEGER | 是否为 DPC 子任务，0：否；1：是 |

2） **V$SQL\_NODE\_HISTORY**

通过该视图既可以查询 sql 执行节点信息，包括 sql 节点的类型、进入次数和使用时间等等；又可以查询所有执行的 sql 节点执行情况，如哪些使用最频繁、耗时多少等。

当 INI 参数 ENABLE\_MONITOR 和 MONITOR\_SQL\_EXEC 都开启时，才会记录 SQL 执行节点信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SEQ\_NO | INTEGER | 操作符在计划中的序号，即 explain 显示执行计划时的行号 |
| 2 | EXEC\_ID | BIGINT | 执行 ID |
| 3 | NODE | BIGINT | 节点 ID |
| 4 | TYPE$ | INTEGER | 节点类型 |
| 5 | BYTES\_DYNAMIC\_ALLOCED | BIGINT | 动态分配字节数 |
| 6 | BYTES\_DYNAMIC\_FREED | BIGINT | 动态释放字节数 |
| 7 | N\_ENTER | INTEGER | 节点进入次数 |
| 8 | TIME\_USED | BIGINT | 节点执行所耗时，单位为微秒 |
| 9 | PLN\_OP\_ID | INTEGER | MPP 模式下，节点所属通讯操作符中的序号 |
| 10 | BYTES\_SEND | BIGINT | 发送的字节数，仅在 MPP 环境下有效 |
| 11 | BYTES\_RECV | BIGINT | 接收的字节数，仅在 MPP 环境下有效 |
| 12 | ROWS\_SEND | BIGINT | 发送的行数，仅在 MPP 环境下有效 |
| 13 | ROWS\_RECV | BIGINT | 接收的行数，仅在 MPP 环境下有效 |
| 14 | BDTA\_SEND | BIGINT | 发送 BDTA 的次数，仅在 MPP 环境下有效 |
| 15 | BDTA\_RECV | BIGINT | 接收 BDTA 的次数，仅在 MPP 环境下有效 |
| 16 | MAL\_ID | BIGINT | 邮件标识号 |
| 17 | MPP\_EXEC\_ID | BIGINT | MPP 会话句柄上的执行序号，同一个会话上的每个节点上值相同 |
| 18 | HASH\_USED\_CELLS | BIGINT | 哈希表上使用的槽数 |
| 19 | HASH\_CONFLICT | BIGINT | 哈希表上每个槽的冲突的个数 |
| 20 | STASK\_NO | INTEGER | 节点所在的子任务号 |
| 21 | THRD\_NO | INTEGER | 节点所在的线程号 |
| 22 | MEM\_USED | BIGINT | 操作符使用的内存空间，单位 KB |
| 23 | DISK\_USED | BIGINT | 操作符预期使用的磁盘空间，单位 KB |
| 24 | DHASH3\_USED\_CELLS | VARCHAR(500) | 动态哈希表中使用的槽数 |
| 25 | DHASH3\_CONFLICT | VARCHAR(300) | 动态哈希表中的冲突情况 |
| 26 | HASH\_SAME\_VALUE | BIGINT | 开启哈希相同值挂链优化时，记录哈希表中相同值的总数，唯一值不纳入计数。例如：哈希表中存在一个 0 和两个相同值链 1—1—1、3—3，此时 HASH\_SAME\_VALUE=5 |
| 27 | SORT\_BUF\_ROWS | BIGINT | 排序操作符的排序缓冲区存放的总行数（关闭大内存排序时）或每路排序的行数（开启大内存排序时） |
| 28 | SORT\_BUF\_AVG\_ROWSIZE | BIGINT | 排序操作符的排序缓冲区存放数据的预估平均行长，单位 Byte |

3） **V$SQL\_PARSE\_HISTORY**

通过该视图可以查看 SQL 查询分析过程中的优化信息。

当 INI 参数 ENABLE\_MONITOR 和 MONITOR\_SQL\_PARSE 都开启时，才会记录查询分析过程中的优化信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SEQ\_NO | INTEGER | 序列号 |
| 2 | SQL\_ID | INTEGER | 监控语句的 SQL 语句 ID |
| 3 | SESS\_ID | BIGINT | 会话 ID |
| 4 | SESS\_SEQ | INTEGER | 会话序列号，用来唯一标识会话 |
| 5 | TRX\_ID | BIGINT | 事务 ID |
| 6 | THREAD\_ID | BIGINT | 线程 ID |
| 7 | SQL\_TEXT | VARCHAR(256) | 原始 SQL 内容 |
| 8 | PHASE\_FLAG | VARCHAR(10) | 优化发生阶段（pha 或 phb 或 pha/phb） |
| 9 | OPTIMIZE\_CLASS | VARCHAR(64) | 优化类别 |
| 10 | OPTIMIZE\_TYPE | INTEGER | 优化类型 |
| 11 | OPT\_DESCRIPTION\_EN | VARCHAR(256) | 优化类型的英文描述 |
| 12 | OPT\_DESCRIPTION\_CN | VARCHAR(256) | 优化类型的中文描述。繁体中文版本下该列展示为 NULL |
| 13 | INI\_PARA | VARCHAR(256) | 相关 INI 参数及决定优化的相关取值 |
| 14 | OPT\_MONITOR\_TEXT | VARCHAR(256) | 监控优化内容或释义 |

4） **V$SQL\_NODE\_NAME**

显示所有的 sql 节点描述信息，包括 sql 节点类型、名字和详细描述。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TYPE$ | INTEGER | 节点类型 |
| 2 | NAME | VARCHAR(24) | 节点的名字 |
| 3 | DESC\_CONTENT | VARCHAR(128) | 节点的详细描述 |
| 4 | VERSION | SMALLINT | 节点的版本号 |

5） **V$COSTPARA**

显示代价估算各项指标的基准值。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | RAN\_IO\_R\_COST | DEC(5,3) | 随机读代价基准值 |
| 2 | RAN\_IO\_W\_COST | DEC(5,3) | 随机写代价基准值 |
| 3 | SEQ\_IO\_R\_COST | DEC(5,3) | 顺序读代价基准值 |
| 4 | SEQ\_IO\_W\_COST | DEC(5,3) | 顺序写代价基准值 |
| 5 | SEL\_RATE\_EQU | DEC(5,3) | 等于谓词的选择率基准值 |
| 6 | SEL\_RATE\_SINGLE | DEC(5,3) | 非等于谓词的选择率基准值 |
| 7 | INDEX\_JOIN\_HIT\_RATIO | DEC(5,3) | 索引连接命中率基准值 |

6） **V$LONG\_EXEC\_SQLS**

当 INI 参数 ENABLE\_MONITOR=1 时，显示系统最近 n 条执行时间超过预定值的 SQL 语句，不包括 DDL 这类敏感语句。n 由 INI 参数 LONG\_EXEC\_SQLS\_CNT 指定。默认预定值为 1000 毫秒，可通过 SP\_SET\_LONG\_TIME 系统函数修改，通过 SF\_GET\_LONG\_TIME 系统函数查看当前值。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SESS\_ID | BIGINT | 会话 ID，系统内部标识 |
| 2 | SQL\_ID | INTEGER | SQL 语句 ID |
| 3 | SQL\_TEXT | VARCHAR(1024) | SQL 文本 |
| 4 | EXEC\_TIME | BIGINT | 执行时间，单位毫秒 |
| 5 | FINISH\_TIME | DATETIME(0) | 执行结束时间 |
| 6 | N\_RUNS | INTEGER | 执行次数 |
| 7 | SEQNO | INTEGER | 编号 |
| 8 | TRX\_ID | BIGINT | 事务号 |
| 9 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |
| 10 | EXEC\_ID | INTEGER | SQL 执行 ID，对应 V$SQL\_HISTORY 的 EXEC\_ID |
| 11 | USER\_ID | INTEGER | 用户 ID |
| 12 | SCH\_ID | INTEGER | 模式 ID |

7） **GV$LONG\_EXEC\_SQLS**

当 INI 参数 ENABLE\_MONITOR=1 时，显示集群各节点最近 n 条执行时间超过预定值的 SQL 语句。n 由 INI 参数 LONG\_EXEC\_SQLS\_CNT 指定。默认预定值为 1000 毫秒，可通过 SP\_SET\_LONG\_TIME 系统函数修改，通过 SF\_GET\_LONG\_TIME 系统函数查看当前值。

目前仅支持 DSC 集群。

| 序号 | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INSTANCE\_NAME | VARCHAR(128) | 实例名 |
| 2 | SESS\_ID | BIGINT | 会话 ID，系统内部标识 |
| 3 | SQL\_ID | INTEGER | SQL 语句 ID |
| 4 | SQL\_TEXT | VARCHAR(1024) | SQL 文本 |
| 5 | EXEC\_TIME | BIGINT | 执行时间，单位毫秒 |
| 6 | FINISH\_TIME | DATETIME(0) | 执行结束时间 |
| 7 | N\_RUNS | INTEGER | 执行次数 |
| 8 | SEQNO | INTEGER | 编号 |
| 9 | TRX\_ID | BIGINT | 事务号 |
| 10 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |
| 11 | EXEC\_ID | INTEGER | SQL 执行 ID，对应 V$SQL\_HISTORY 的 EXEC\_ID |
| 12 | USER\_ID | INTEGER | 用户 ID |
| 13 | SCH\_ID | INTEGER | 模式 ID |

8） **V$SYSTEM\_LONG\_EXEC\_SQLS**

当 INI 参数 ENABLE\_MONITOR=1 时，显示系统自启动以来执行时间最长的 n 条 SQL 语句，不包括执行时间低于预定值的语句和 DDL 这类敏感语句。n 由 INI 参数 SYSTEM\_LONG\_EXEC\_SQLS\_CNT 指定。默认预定值为 1000 毫秒，可通过 SP\_SET\_LONG\_TIME 系统函数修改，通过 SF\_GET\_LONG\_TIME 系统函数查看当前值。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SESS\_ID | BIGINT | 会话 ID，系统内部标识 |
| 2 | SQL\_ID | INTEGER | SQL 语句 ID |
| 3 | SQL\_TEXT | VARCHAR(1024) | SQL 文本 |
| 4 | EXEC\_TIME | BIGINT | 执行时间，单位毫秒 |
| 5 | FINISH\_TIME | DATETIME(0) | 执行结束时间 |
| 6 | N\_RUNS | INTEGER | 执行次数 |
| 7 | SEQNO | INTEGER | 编号 |
| 8 | TRX\_ID | BIGINT | 事务号 |
| 9 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |
| 10 | MIN\_EXEC\_TIME | BIGINT | 该 SQL 最小执行时间，单位毫秒 |
| 11 | MAX\_EXEC\_TIME | BIGINT | 该 SQL 最大执行时间，单位毫秒 |
| 12 | TOTAL\_EXEC\_TIME | BIGINT | 该 SQL 累计执行时间，单位毫秒 |
| 13 | EXEC\_ID | INTEGER | SQL 执行 ID，对应 V$SQL\_HISTORY 的 EXEC\_ID |
| 14 | USER\_ID | INTEGER | 用户 ID |
| 15 | SCH\_ID | INTEGER | 模式 ID |

9） **GV$SYSTEM\_LONG\_EXEC\_SQLS**

当 INI 参数 ENABLE\_MONITOR=1 时，显示集群各节点自启动以来执行时间最长的 n 条 SQL 语句，不包括执行时间低于预定值的语句。n 由 INI 参数 SYSTEM\_LONG\_EXEC\_SQLS\_CNT 指定。默认预定值为 1000 毫秒，可通过 SP\_SET\_LONG\_TIME 系统函数修改，通过 SF\_GET\_LONG\_TIME 系统函数查看当前值。

目前仅支持 DSC 集群。

| 序号 | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INSTANCE\_NAME | VARCHAR(128) | 实例名 |
| 2 | SESS\_ID | BIGINT | 会话 ID，系统内部标识 |
| 3 | SQL\_ID | INTEGER | SQL 语句 ID |
| 4 | SQL\_TEXT | VARCHAR(1024) | SQL 文本 |
| 5 | EXEC\_TIME | BIGINT | 执行时间，单位毫秒 |
| 6 | FINISH\_TIME | DATETIME(0) | 执行结束时间 |
| 7 | N\_RUNS | INTEGER | 执行次数 |
| 8 | SEQNO | INTEGER | 编号 |
| 9 | TRX\_ID | BIGINT | 事务号 |
| 10 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |
| 11 | MIN\_EXEC\_TIME | BIGINT | 该 SQL 最小执行时间，单位毫秒 |
| 12 | MAX\_EXEC\_TIME | BIGINT | 该 SQL 最大执行时间，单位毫秒 |
| 13 | TOTAL\_EXEC\_TIME | BIGINT | 该 SQL 累计执行时间，单位毫秒 |
| 14 | EXEC\_ID | INTEGER | SQL 执行 ID，对应 V$SQL\_HISTORY 的 EXEC\_ID |
| 15 | USER\_ID | INTEGER | 用户 ID |
| 16 | SCH\_ID | INTEGER | 模式 ID |

10） **V$VMS**

显示虚拟机信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 虚拟机 ID |
| 2 | TRX\_ID | BIGINT | 事务 ID |
| 3 | STMT\_ID | INTEGER | 语句 ID |
| 4 | EXP\_FLAG | CHAR(1) | 表达式标识 |
| 5 | VSTACK\_SIZE | INTEGER | 栈大小，单位 8\*BYTE |
| 6 | VSTACK | BIGINT | 栈基址 |
| 7 | VTOP | INTEGER | 栈顶离基址的距离 |
| 8 | VUSED | INTEGER | 栈已用空间的大小，单位 8\*BYTE |
| 9 | MEMOBJ | BIGINT | 内存地址 |
| 10 | STKFRM\_DEPTH | INTEGER | 栈深度 |
| 11 | FREE\_STKFRMS | INTEGER | 已释放的栈 |
| 12 | CURR\_FRM | BIGINT | 当前栈 |
| 13 | IP | BIGINT | IP 地址 |
| 14 | RT\_HEAP | BIGINT | DMSQL 程序所使用的堆 |
| 15 | SQL\_NO | INTEGER | SQL 语句树的序号 |
| 16 | RS\_SEQ\_NO | INTEGER | 结果集序号 |
| 17 | ECPT\_CODE | INTEGER | 返回的 CODE |
| 18 | ERR\_DESC | VARCHAR(256) | 错误描述 |
| 19 | ROW\_AFFECHED | BIGINT | 结果集的行数 |
| 20 | SQL\_TYPE | INTEGER | SQL 语句类型 |
| 21 | N\_FUNS | INTEGER | 已使用函数的数目 |
| 22 | SESS\_ID | BIGINT | 会话 ID，系统内部标识 |
| 23 | MEM\_ADDR | BIGINT | 虚拟机使用的 MEM\_POOL 地址 |

11） **V$STKFRM**

显示虚拟机栈桢信息。该视图必须在 INI 参数 ENABLE\_MONITOR 和 MONITOR\_SQL\_EXEC 都开启时才有信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | VM\_ID | INTEGER | 虚拟机 ID |
| 2 | FRAME\_LEVEL | INTEGER | 栈的层次 |
| 3 | ADDR | BIGINT | 地址 |
| 4 | RET\_IP | BIGINT | 返回的指令地址 |
| 5 | CURR\_METHOD | BIGINT | 当前方法 |
| 6 | LOCAL\_SPACE | INTEGER | 临时变量空间大小，单位是栈帧的个数 |
| 7 | ARG\_SPACE | INTEGER | 参数空间大小，单位是栈帧的个数 |
| 8 | OFF\_LOCALS | BIGINT | 每个变量基于原栈顶的偏移 |
| 9 | OFF\_ARGS | BIGINT | 每个参数基于原栈顶的偏移 |
| 10 | CURR\_BP | BIGINT | 新的栈顶 |
| 11 | IP\_BASE | BIGINT | 指令基址 |
| 12 | SQL\_VM\_NODE | BIGINT | VM 地址 |
| 13 | SQL\_TRX\_IDS | BIGINT | 事务 ID 地址 |
| 14 | SYSTEM\_FLAG | CHAR(1) | 系统标记 |
| 15 | FRAME\_SIZE | INTEGER | 栈的大小，单位 BYTE |

12） **V$STMTS**

显示当前活动会话的最近的语句的相关信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | STMT\_ID | INTEGER | 语句 ID，从 iid 页取得 |
| 2 | TYPE$ | INTEGER | 语句类型，供系统内部使用 |
| 3 | EXEC\_DIRECT | CHAR(1) | 是否立即执行标记 |
| 4 | SESS\_ID | BIGINT | 对应的会话 ID，系统内部标识 |
| 5 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |
| 6 | PLN | BIGINT | 查询计划地址 |
| 7 | DML\_RCNT | BIGINT | DML 操作所影响的行数 |
| 8 | REQ\_RCNT | BIGINT | prepare 或 execute 查询要求返回的行数 |
| 9 | BATCH\_FLAG | CHAR(1) | 是否批量绑定参数 |
| 10 | N\_PARA\_ROWS | INTEGER | 多行参数时的行数目 |
| 11 | NTH\_PARA\_ROW | INTEGER | 多行参数时的当前行序号 |
| 12 | CUR\_PARA\_OFF | INTEGER | 参数的当前偏移 |
| 13 | PARA\_BUF | BIGINT | 参数的内存地址 |
| 14 | SQL\_TEXT | VARCHAR(1000) | SQL 语句 |
| 15 | CURSOR\_FORWARD\_ONLY | CHAR(1) | 是否是只能向前移动的游标 |
| 16 | CURSOR\_NAME | VARCHAR(128) | 游标名字 |
| 17 | CURSOR\_KEEP\_NAME | CHAR(1) | 是否保存游标名字 |
| 18 | CURSOR\_REF\_ID | INTEGER | 引用的游标语句句柄 |
| 19 | CURSOR\_REF\_SEQNO | INTEGER | 引用语句的执行序号 |
| 20 | EXEC\_ID | INTEGER | 语句的执行号 |

13） **V$SQL\_PLAN\_NODE**

当 INI 参数 ENABLE\_MONITOR 和 MONITOR\_SQL\_EXEC 都开启时，显示执行计划的节点信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PLN\_ADDR | VARBINARY(8) | 计划地址 |
| 2 | SQL\_ID | INTEGER | SQL 语句 ID(唯一标识) |
| 3 | NODE\_ADDR | VARBINARY(8) | 节点地址 |
| 4 | PARENT | VARBINARY(8) | 父节点地址 |
| 5 | LEFT\_CHILD | VARBINARY(8) | 左孩子地址 |
| 6 | RIGHT\_CHILD | VARBINARY(8) | 右孩子地址 |
| 7 | HAS\_INVOKE | CHAR(1) | 是否包含函数 |
| 8 | OPERATION | VARCHAR(30) | 操作符名称 |
| 9 | OPTIONS | VARCHAR(30) | 扫描类型 |
| 10 | TABLE# | INTEGER | 表 ID |
| 11 | TABLE\_NAME | VARCHAR(128) | 表名 |
| 12 | TABLE\_ALIAS | VARCHAR(128) | 表别名 |
| 13 | INDEX\_NAME | VARCHAR(128) | 索引名称 |
| 14 | SCHID | INTEGER | 模式 ID |
| 15 | DEPTH | INTEGER | 节点层次 |
| 16 | CARD | BIGINT | 行数 |
| 17 | BYTES | BIGINT | 字节数 |
| 18 | COST | BIGINT | 代价 |
| 19 | CPU\_COST | BIGINT | CPU 代价 |
| 20 | IO\_COST | BIGINT | IO 代价，暂不支持，始终为 0 |
| 21 | SCAN\_RANGE | VARCHAR(128) | 扫描范围 |
| 22 | FILTER | VARCHAR(1000) | 过滤表达式 |
| 23 | JOIN\_COND | VARCHAR(1000) | 连接表达式 |

14） **V$SQL\_SUBPLAN**

显示子计划信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PLN\_ADDR | VARBINARY(8) | 计划地址 |
| 2 | SQL\_ID | INTEGER | SQL 语句 ID（唯一标识） |
| 3 | SUBPLN | VARBINARY(8) | 子计划地址（SUBPLN 在 V$SQL\_PLAN\_DCTREF 中即为 PLN\_ADDR） |

15） **V$SQL\_PLAN\_DCTREF**

显示所有执行计划相关的详细字典对象信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PLN\_ADDR | VARBINARY(8) | 计划地址 |
| 2 | SQL\_ID | INTEGER | SQL 语句 ID(唯一标识) |
| 3 | TYPE | VARCHAR(16) | 字典对象类型（DATABASE、TABLE、VIEW、DYNAMIC VIEW、INDEX、USER、ROLE、PROCEDURE、TRIGGER、CONSTRAINT、SCHEMA、SEQUENCE、LOGIN、DBLINK、SYSROLE、PACKAGE、OBJECT、SYNOM、CRYPTION、CIPHER、IDENTITY、SYS PRIVILEGE、OBJ PRIVILEGE、POLICY、RULE、COLUMN、DOMAIN、CHARSET、COLLATION、CONTEXT INDEX、USER LOGIN、REGEXP REWRITE、NORMAL REWRITE、UNKNOWN） |
| 4 | STATUS | VARCHAR(16) | 字典对象状态。共四种状态（NORMAL、CREATING、ALTERING、DROPPING），本视图中的执行计划只涉及 DML 语句的 NORMAL 状态 |
| 5 | R\_SIZE | INTEGER | 字典对象大小，单位字节 |
| 6 | VERSION | INTEGER | 字典对象版本号 |
| 7 | NAME | VARCHAR(128) | 字典对象名称 |
| 8 | SCHID | INTEGER | 模式 ID |
| 9 | ID | INTEGER | 字典对象 ID |
| 10 | UID | INTEGER | 用户 ID |
| 11 | TS\_ID | INTEGER | 表空间 ID |

16） **V$MTAB\_USED\_HISTORY**

显示系统自启动以来使用 MTAB 空间最多的 500 个操作符信息。当操作符使用 MTAB 空间大于等于 1MB 时才会记录到该视图中。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | EXEC\_ID | BIGINT | 语句的执行 ID |
| 2 | SQL\_TEXT | VARCHAR(1024) | SQL 文本 |
| 3 | STK\_LEVEL | INTEGER | 当前栈帧的级别 |
| 4 | CUR\_SQL\_NODE | BIGINT | 当前的 SQL 节点 |
| 5 | OP\_SEQ\_NO | INTEGER | 操作符在执行计划中序号 |
| 6 | OP\_TYPE$ | INTEGER | 操作符节点类型 |
| 7 | MTAB\_USED\_BY\_M | INTEGER | 操作符使用的 MTAB 空间，单位 MB |
| 8 | MEM\_USED\_BY\_M | INTEGER | MTAB 使用的内存空间，单位 MB |
| 9 | MMT\_FILE\_ALLOC | INTEGER | 操作符使用 MMT 时以 MMT\_SIZE 为大小分配的 MMT 文件个数 |
| 10 | MMT\_PAGES\_USED | INTEGER | 操作符使用 MMT 时实际使用的页数 |
| 11 | MTAB\_TYPE | VARCHAR(10) | MTAB 类型：   FLUSH: 将 ESEND 操作符，TOP 操作符，HUGE 表插入，分析函数，层次查询，闪回查询，哈希连接，归并连接，嵌套连接，哈希表，临时表，动态表、动态视图、等待事件，排序相关操作使用的数据缓冲区写入 MTAB 空间；   DESTORY: 释放 MTAB 空间；   SORT: 排序空间不足时将排序缓冲区数据写入 MTAB 空间 |
| 12 | MAL\_ID | BIGINT | DESTORY: 释放 MTAB 空间； 邮件标识号 |
| 13 | MPP\_EXEC\_ID | BIGINT | SORT: 排序空间不足时将排序缓冲区数据写入 MTAB 空间 MPP 会话句柄上的执行序号，同一个会话上的每个节点上值相同 |
| 14 | START\_TIME | DATETIME(0) | 操作符信息创建的时间(精确到秒) |
| 15 | END\_TIME | DATETIME(0) | 操作符信息最后一次更新的时间(精确到秒) |

17） **V$SORT\_HISTORY**

当 INI 参数 ENABLE\_MONITOR=1 都打开时，显示系统自启动以来使用排序页数最多的 50 个操作符信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | EXEC\_ID | BIGINT | 语句的执行 ID |
| 2 | SQL\_TEXT | VARCHAR(1024) | SQL 文本 |
| 3 | STK\_LEVEL | INTEGER | 当前栈帧的级别 |
| 4 | CUR\_SQL\_NODE | BIGINT | 当前的 SQL 节点 |
| 5 | OP\_SEQ\_NO | INTEGER | 操作符在执行计划中序号 |
| 6 | OP\_TYPE$ | INTEGER | 操作符节点类型 |
| 7 | N\_PAGES | INTEGER | 排序使用的页数 |
| 8 | N\_MERGE\_SORT | INTEGER | 归并排序的趟数 |
| 9 | SORT\_BYTES | INTEGER | 参与排序的每行字节数（估算值） |
| 10 | SORT\_ROWS | BIGINT | 参与排序的行数 |
| 11 | MAL\_ID | BIGINT | 邮件标识号 |
| 12 | MPP\_EXEC\_ID | BIGINT | MPP 会话句柄上的执行序号，同一个会话上的每个节点上值相同 |

18） **V$HASH\_MERGE\_USED\_HISTORY**

HASH MERGE 连接操作符使用的缓存信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TYPE$ | INTEGER | 节点类型 |
| 2 | SEQNO | INTEGER | 序号 |
| 3 | EXEC\_ID | INTEGER | 执行 ID |
| 4 | SQL\_TEXT | VARCHAR(1000) | 执行 SQL 文本 |
| 5 | MERGE\_USED | INTEGER | HASH MERGE 使用的缓存空间，单位 MB |
| 6 | MAL\_ID | BIGINT | 邮件标识号 |
| 7 | MPP\_EXEC\_ID | BIGINT | MPP 环境 SQL 执行号 |

19） **V$PLSQL\_DDL\_HISTORY**

记录 DMSQL 程序中执行的 DDL 语句，主要监控 truncate table 和 Execute immediate DDL 语句的情况。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SEQNO | INTEGER | 该类语句的执行编号 |
| 2 | SESS\_ID | BIGINT | 执行会话 ID，系统内部标识 |
| 3 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |
| 4 | TRX\_ID | BIGINT | 执行事务 ID |
| 5 | EXEC\_ID | BIGINT | 虚拟机的执行序号 |
| 6 | VM\_ID | INTEGER | 虚拟机 ID |
| 7 | STKFRM\_LEVEL | INTEGER | 当前栈帧在虚拟机的层次 |
| 8 | DDL\_FROM | VARCHAR(10) | 若为 TRUNCATE TABLE，则为’TRUNC’，否则为’EXEC’ |
| 9 | SQL\_TEXT | VARCHAR(1000) | 获得该层栈帧执行的 SQL 语句，若字符长度超过 1000，则取前 1000 个字符。 |
| 10 | DDL\_TIME | DATETIME(6) | 语句执行时间 |
| 11 | MAIL\_ID | BIGINT | 邮件标识号 |
| 12 | MPP\_EXEC\_ID | BIGINT | MPP 会话句柄上的执行序号，同一个会话上的每个节点上值相同 |

20） **V$PRE\_RETURN\_HISTORY**

记录大量数据返回结果集的历史信息（查询大量数据产生）。当 INI 参数 ENABLE\_MONITOR 开启时，显示该视图信息；当数据返回的结果集大于等于 INI 参数 FIRST\_ROWS 时，才会记录到该视图中。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SEQNO | INTEGER | 编号 |
| 2 | TRX\_ID | BIGINT | 事务 ID |
| 3 | VM\_ID | INTEGER | 虚拟机 ID |
| 4 | EXEC\_ID | BIGINT | 执行 ID，记录执行的次数 |
| 5 | SESS\_ID | BIGINT | 会话 ID，系统内部标识 |
| 6 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |
| 7 | SQL\_TEXT | VARCHAR(1000) | 返回的 SQL 语句 |
| 8 | N\_ROWS | BIGINT | 返回的行数 |
| 9 | IS\_FIRST | CHAR(1) | 是否第一次返回 |
| 10 | RETURN\_TIME | DATETIME(6) | 记录返回的时间 |
| 11 | MAL\_ID | BIGINT | 邮件标识号 |
| 12 | MPP\_EXEC\_ID | BIGINT | MPP 会话句柄上的执行序号，同一个会话上的每个节点上值相同 |
| 13 | SQL\_ID | INTEGER | SQL 语句 ID(唯一标识) |

21） **V$DMSQL\_EXEC\_TIME**

记录动态监控的 SQL 语句执行时间。当 INI 参数 ENABLE\_MONITOR\_DMSQL=1 时才会记录监控的 SQL 语句，仅监控多条或复杂 SQL，例如包含引用包、嵌套子过程、子方法、动态 SQL 的 SQL 语句。

V$DMSQL\_EXEC\_TIME 的容量（最大记录数）由 INI 参数 DMSQL\_ET\_CNT 指定。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | EXEC\_ID | BIGINT | 语句执行号 |
| 2 | TYPE$ | VARCHAR(32) | 语句类型：SQL、DYNAMIC SQL、METHOD |
| 3 | SEQ | INTEGER | 相对序号：动态 SQL 的指令偏移、SQL 语句序号、方法的指令偏移 |
| 4 | LEVEL | INTEGER | 执行层次 |
| 5 | CALLER | VARCHAR(256) | 调用方法名 |
| 6 | METHOD | VARCHAR(256) | 方法名 |
| 7 | EXEC\_CNT | INTEGER | 执行次数 |
| 8 | LAST\_EXEC\_TICK | BIGINT | 最近一次执行时戳 ，单位微秒 |
| 9 | TIME\_USED | BIGINT | 执行时间 ，单位毫秒 |
| 10 | MAL\_ID | BIGINT | 邮件标识号 |
| 11 | MPP\_EXEC\_ID | BIGINT | MPP 会话句柄上的执行序号，同一个会话上的每个节点上值相同 |
| 12 | SQL\_TEXT | VARCHAR(1000) | 语句脚本 |
| 13 | SQL\_ID | INTEGER | SQL 语句 ID。本字段仅对语句块中的动态 SQL 有效，其它情况输出值均为 NULL |
| 14 | LINE\_NO | INTEGER | 该行所在脚本的行号， 方便定位 |
| 15 | FIRST\_START\_TIME | DATETIME(6) | 首次执行该行的时间 |

22） **V$VIRTUAL\_MACHINE**

显示活动的虚拟机信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 虚拟机 ID |
| 2 | SESSID | BIGINT | 会话 ID |
| 3 | STMT\_ID | INTEGER | 语句 ID |
| 4 | EXP\_FLAG | CHAR(4) | 表达式标识 |
| 5 | VSTACK\_SIZE | INTEGER | 栈大小，单位是栈帧的个数 |
| 6 | VSTACK | BIGINT | 栈基址 |
| 7 | VTOP | INTEGER | 栈顶离基址的距离 |
| 8 | VUSED | INTEGER | 栈已用空间的大小，单位是栈帧的个数 |
| 9 | STKFRM\_DEPTH | INTEGER | 栈深度 |
| 10 | FREE\_STKFRMS | INTEGER | 已释放栈帧的数目 |
| 11 | CURR\_FRM | BIGINT | 当前栈的地址 |
| 12 | IP | BIGINT | IP 地址 |
| 13 | SQL\_NO | INTEGER | SQL 语句树的序号 |
| 14 | REUSE\_CNT | INTEGER | 虚拟机重用次数 |

23） **V$SQLCOMMAND**

显示 SQL 语句的类型。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | SQL 语句的类型 ID |
| 2 | COMMAND\_TYPE | INTEGER | SQL 语句的类型号 |
| 3 | COMMAND\_NAME | VARCHAR(24) | SQL 语句的类型名称 |
| 4 | CON\_ID | INTEGER | 保留字段 |

24） **V$SQL\_BINDDATA\_HISTORY**

当 INI 参数 ENABLE\_MONITOR=1、ENABLE\_MONITOR\_BP=1 时，记录数据库所有语句级绑定参数的类型和值。

该视图可对接口发送至服务器的带参数的方法/过程、INSERT/UPDATE/DELETE/SELECT 语句进行监控记录，但不对 PL/SQL 中动态执行的带参数语句进行监控记录。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | EXEC\_ID | BIGINT | 语句执行号 |
| 2 | BINDDATA | VARBINARY(8188)或 BLOB | 绑定参数的信息。该列的数据类型与 INI 参数 BINDDATA\_COLTYPE 相关，该参数缺省值为 0。当 BINDDATA\_COLTYPE=0 时，数据类型为 VARBINARY，最大长度为 8188 个字节，若绑定参数信息的总长度超过 8188 个字节，则将对 OBJECT（名称/值对）以及 BINARY 两种类型的参数值进行缩减处理；当 BINDDATA\_COLTYPE=1 时，数据类型为 BLOB，最大长度限制为 2GB |

25） **V$PLN\_HISTORY**

显示近期执行的 SQL 语句的执行计划。在 ini 参数 USE\_PLN\_POOL!=0 时才统计。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SQL\_ID | INTEGER | SQL 语句 ID，可与 V$SQL\_HISTORY 关联查看更多信息 |
| 2 | TOP\_SQL\_TEXT | VARCHAR (1000) | SQL 语句 |
| 3 | SQL\_PLAN | CLOB | SQL 语句对应的执行计划，与 explain SQL 结果相同；执行计划大小超过 10MB 的部分不显示 |
| 4 | SQL\_TEXT\_ID | VARCHAR(13) | 语句固定的散列字符；相同的 SQL 散列字符相同 |

26） **V$SQL\_STAT\_THRESHOLD**

显示当前各个监控项的阈值。各个监控项的阈值默认为 0，表示未设置和未限制。可以通过 SP\_SET\_SQL\_STAT\_THRESHOLD()设置监控阈值，超过阈值才开始监控。具体使用参考《DM8\_SQL 语言使用手册》。

除监控项 EXEC\_TIME、PARSE\_TIME、HARD\_PARSE\_TIME、IO\_WAIT\_TIME 在本视图中的单位为毫秒外，其余各监控项的单位与 V$SQL\_STAT 中相同。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 监控项的序号 |
| 2 | STAT\_NAME | VARCHAR(256) | 监控项的名称 |
| 3 | THRESHOLD\_VALUE | BIGINT | 监控项的阈值 |
| 4 | COMMENT | VARCHAR(256) | 监控项的使用描述 |

27） **V$BUSY\_PAGE\_INFO**

记录服务器启动后，最新的 20480 条 DSC LBS 等待信息，仅记录等待不少于 1 秒的信息，每秒更新一次记录。当打开数据页损坏报错功能后，额外记录数据页读超时和 DSC LBS 超时的错误信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SESS\_ID | BIGINT | 会话 ID |
| 2 | TRX\_ID | BIGINT | 事务 ID |
| 3 | TS\_ID | INTEGER | 数据页表空间 ID |
| 4 | FILE\_ID | INTEGER | 数据页文件 ID |
| 5 | PAGE\_NO | INTEGER | 数据页号 |
| 6 | ERR\_CODE | INTEGER | 日志 ID |
| 7 | ERR\_TIME | DATETIME(0) | 报错时间 |
| 8 | WAIT\_TIME | INTEGER | 等待时长，单位 ms |
| 9 | DB\_MAGIC | INTEGER | 数据库魔数 |
| 10 | SQLS | VARCHAR(1024) | 空字符串"" |
| 11 | EXEC\_ID | INTEGER | SQL 执行 ID，对应 V$SQL\_HISTORY 的 EXEC\_ID |

28） **V$INJECT\_HINT\_INFO**

记录服务器启动后 INJECT HINT 的使用情况。需要设置 INI 参数 ENABLE\_INJECT\_HINT=1，并使用 SF\_INJECT\_HINT 为 SQL 指定 HINT。对于模糊匹配，每条 HINT 的监控个数上限为 100，超出时摘除最早记录。当 INI 参数 USE\_PLN\_POOL 取值包含 1 时（即启用执行计划的重用功能），只有在 SQL 语句需要生成执行计划的时候才会记录 INJECT HINT 的使用情况。可以通过系统过程 SP\_DYNAMIC\_VIEW\_DATA\_CLEAR 来清空此视图的历史信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | HASH\_VALUE | INTEGER | SQL 语句的 HASH 值 |
| 2 | SQL\_TEXT | VARCHAR(1000) | 实际执行的 SQL 语句(最多只展示 1000 个字符) |
| 3 | HINT\_NAME | VARCHAR(128) | HINT 规则名称 |
| 4 | HINT\_TEXT | VARCHAR(1000) | 为 SQL 语句指定的 HINT 内容(最多只展示 1000 个字符) |
| 5 | FIRST\_TIME | DATETIME(0) | 第一次使用时间 |
| 6 | LAST\_TIME | DATETIME(0) | 最近一次使用时间 |
| 7 | COUNT | BIGINT | 使用次数 |
| 8 | IS\_FUZZY | CHAR(1) | 是否是模糊匹配 |
| 9 | VALIDATE | VARCHAR(5) | 规则是否生效，取值 TRUE/FALSE |
| 10 | SQL\_TEXT\_ID | VARCHAR(13) | 语句固定的散列字符；相同的 SQL 语句，散列字符相同 |

#### 9\. 事务和检查点

1） **V$TRX**

显示所有活动事务的信息。通过该视图可以查看系统中所有的事务以及相关信息，如锁信息等。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | BIGINT | 当前活动事务的 ID 号 |
| 2 | NEXTID | BIGINT | 下一个事务 ID 号 |
| 3 | MIN\_ACTIVE\_ID | BIGINT | 所有活动事务 ID 号最小者 |
| 4 | STATUS | VARCHAR(20) | 当前事务的状态。   NOT START 未开始任何操作；   ACTIVE 活动；   LOCK WAIT 锁等待；   ROLLING 正在回滚；   ROLLING\_SUSPEND 回滚挂起；   PRE\_COMMIT 两阶段事务的预提交状态；   TO\_RELEASE DPC 环境下分布式事务的等待释放状态。分布式事务完成第二阶段提交后转入 TO\_RELEASE 状态，分布式事务在所有节点都转入 TO\_RELEASE 状态后才允许释放； |
| 5 | ISOLATION | INTEGER | 隔离级。0：读未提交；1：读提交；2：可重复读；3：串行化 |
| 6 | READ\_ONLY | CHAR(6) | 是否是一个只读事务 |
| 7 | SESS\_ID | BIGINT | 当前事务的所在会话 ID，系统内部标识 |
| 8 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |
| 9 | INS\_CNT | INTEGER | 插入回滚记录个数 |
| 10 | DEL\_CNT | INTEGER | 删除回滚记录个数 |
| 11 | UPD\_CNT | INTEGER | 更新回滚记录个数 |
| 12 | UPD\_INS\_CNT | INTEGER | 更新插入回滚记录个数 |
| 13 | UREC\_SEQNO | INTEGER | 当前 UNDO 记录的递增序列号 |
| 14 | WAITING | BIGINT | 事务等待锁的地址，对应 V$LOCK 的 ADDR 字段 |
| 15 | START\_LSN | BIGINT | 事务的起始 LSN |
| 16 | ROLLBACK\_FLAG | INTEGER | 是否在回滚 |
| 17 | XID | VARBINARY(140) | XA 事务唯一标识 |
| 18 | LOCK\_CNT | INTEGER | 使用中的事务锁个数 |
| 19 | IGN\_LOCK\_CNT | INTEGER | IGNORABLE 锁个数 |
| 20 | SAVEPOINT\_CNT | INTEGER | 保存点个数 |
| 21 | THRD\_ID | INTEGER | 当前事务对应的线程 ID |
| 22 | SRC\_SITE | INTEGER | 分布式事务的来源站点 ID |
| 23 | N\_BRANCHES | INTEGER | DPC 下事务涉及的节点数 |
| 24 | N\_WRITES | INTEGER | DPC 下事务涉及的非只读的节点数 |
| 25 | N\_PAGES | INTEGER | 事务实际使用的回滚页数量 |
| 26 | SNAP\_CMTSEQ | BIGINT | 获取可见性视图时的提交序号快照 |
| 27 | N\_LONG | INTEGER | 获取可见性视图时的长事务个数 |
| 28 | CRASH\_FLAG | INTEGER | 是否为故障前的事务：1 表示是，0 表示不是 |
| 29 | START\_TIME | DATETIME(0) | 事务开始时间 |
| 30 | ROLL\_STIME | DATETIME(0) | 事务最近一次回滚的开始时间 |
| 31 | N\_PAGE\_ROLLED | INTEGER | 事务已经回滚的回滚页数量 |

2） **V$TRXWAIT**

显示事务等待信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | BIGINT | 事务 ID |
| 2 | WAIT\_FOR\_ID | BIGINT | 所等待的事务 ID |
| 3 | WAIT\_TIME | INTEGER | 当前等待时间。单位：毫秒 |
| 4 | THRD\_ID | INTEGER | 所等待事务对应的线程 ID |
| 5 | LOCK | BIGINT | 当前事务的锁地址 |
| 6 | WAIT\_FOR\_LOCK | BIGINT | 所等待事务的锁地址 |

3） **V$RECV\_ROLLBACK\_TRX**

显示数据库启动时回滚的所有事务信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TRX\_ID | BIGINT | 事务号 |
| 2 | BEGIN\_LSN | BIGINT | 事务启动逻辑日志的 LSN 值，只在 INI 参数开启逻辑日志情况下有效 |
| 3 | BEGIN\_TIME | DATETIME(6) | 事务启动时间，只在 INI 参数开启逻辑日志情况下有效 |
| 4 | N\_UPAGES | INTEGER | 回滚页总数 |
| 5 | N\_URECS | INTEGER | 回滚记录总数 |

4） **V$LOCK**

显示活动的事务锁信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ADDR | BIGINT | 本地封锁对象的地址 |
| 2 | TRX\_ID | BIGINT | 所属事务 ID |
| 3 | LTYPE | VARCHAR(10) | 锁类型：TID 锁、对象锁 |
| 4 | LMODE | CHAR(2) | 锁模式：S 锁、X 锁、IX 锁、IS 锁 |
| 5 | BLOCKED | INTEGER | 是否处于上锁等待状态。0 表示已上锁成功；1 表示处于上锁等待状态 |
| 6 | TABLE\_ID | INTEGER | 对于对象锁，表示表对象或字典对象的 ID；对于 TID 锁，表示封锁记录对应的表 ID。-1 表示事务启动封锁自身的 TID |
| 7 | ROW\_IDX | BIGINT | TID 锁封锁记录行信息。-1 表示事务启动封锁自身的 TID |
| 8 | TID | BIGINT | TID 锁对象事务 ID |
| 9 | IGN\_FLAG | INTEGER | 锁对象的 IGNORABLE 标记，INI 参数 LOCK\_DICT\_OPT 开启时有效。   取值 0：表示锁正在使用中，IGN\_FLAG 最低位置为 0；   取值 1：表示事务 TRX1 已经提交，但是锁资源未释放，TRX1 重新封锁时可以直接使用，此时 IGN\_FLAG 最低位置为 1；   取值 2：为 0+2 的组合值。当锁正被使用时，另一事务要封锁同一对象，将当前正被使用的锁的 IGN\_FLAG 次低位置为 1；   取值 3：为 1+2 的组合值。当 TRX1 已提交，但锁未释放时，另一事务 TRX2 要封锁同一对象，此时 TRX2 可以忽略此 IGN\_FLAG=1 的锁，但是要将此锁的 IGN\_FLAG 次低位置为 1 |
| 10 | HLCK\_EP | INTEGER | 取值 0：表示锁正在使用中，IGN\_FLAG 最低位置为 0；关联对象 HLCK 所属节点号。DSC 集群环境标识创建 HLCK 对象的节点号，缺省为 255，单机无效 |
| 11 | SPT\_NO | INTEGER | 关联的保存点序号 |
| 12 | THRD\_ID | INTEGER | 锁的创建者线程号 |
| 13 | HASH\_VALUE | BIGINT | 锁的缓存的 HASH 值 |

5） **V$DEADLOCK\_HISTORY**

记录死锁的历史信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SEQNO | INTEGER | 编号 |
| 2 | TRX\_ID | BIGINT | 事务 ID |
| 3 | SESS\_ID | BIGINT | 会话 ID，系统内部标识 |
| 4 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |
| 5 | SQL\_TEXT | VARCHAR(1000) | 产生死锁的 SQL 语句 |
| 6 | HAPPEN\_TIME | DATETIME(6) | 死锁发生的时间 |
| 7 | TOO\_MANY\_CHECKS | CHAR(1) | 当事务发生锁等待时，是否检测到等待锁的数量大于等于 1024。Y 是，此时视为发生死锁；N 否，表示实际死锁 |
| 8 | DEADLOCK\_CYCLE | VARCHAR(4096) | 当 TOO\_MANY\_CHECKS = 'Y’时，格式为： self ->((tid1, sess\_id1), (tid2, sess\_id2),..., (tidn, sess\_idn)), 表示事务等待的锁和会话 ID 列表；当 TOO\_MANY\_CHECKS = 'N’时， 格式为： self -> (tid1, sess\_id1) ->(tid2, sess\_id2) ->... -> self, 表示发生死锁时的等待环。其中 self 表示被牺牲的事务号，对应视图中本行记录的第 2 个字段 TRX\_ID |
| 9 | USER\_ID | INTEGER | 用户 ID |
| 10 | SCH\_ID | INTEGER | 模式 ID |
| 11 | SQL\_TEXT\_ID | VARCHAR(13) | SQL 文本 ID |

6） **V$FLASHBACK\_TRX\_INFO**

显示闪回信息，无法显示只有 Insert 操作的事务。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | START\_TRXID | BIGINT | 闪回开始事务 ID |
| 2 | START\_TIMESTAMP | DATETIME(6) | 开始时间 |
| 3 | COMMIT\_TRXID | BIGINT | 闪回完成事务 ID |
| 4 | COMMIT\_TIMESTAMP | DATETIME(6) | 完成时间 |
| 5 | LOGIN\_USER | VARCHAR(256) | 闪回用户名 |
| 6 | UNDO\_CHANGE# | INTEGER | 回滚记录序号 |
| 7 | OPERATION | CHAR(1) | DML 操作类型。 D：删除；U：修改；I：插入；N：更新插入（专门针对 CLUSTER PRIMARY KEY 的插入）； C：事务提交；P：预提交记录；O：default |
| 8 | TABLE\_NAME | VARCHAR(256) | 表名 |
| 9 | TABLE\_OWNER | VARCHAR(256) | 表所属用户名 |
| 10 | ROW\_ID | BIGINT | ROWID |
| 11 | UNDO\_SQL | VARCHAR(3900) | 回滚 SQL 语句 |
| 12 | COMMIT\_LSN | BIGINT | 闪回完成时的 LSN |

7） **V$LSN\_TIME**

显示 LSN/TIME 映射关系。每 3 秒收集一次映射关系，并且仅支持显示最近 5 天的映射关系。每次系统重启或者主备切换都会重新收集映射关系，目前暂不支持显示系统启动之前的历史映射关系。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TIME\_MP | BIGINT | 当前时间，单位为秒 |
| 2 | TIME\_DP | DATETIME(0) | 当前时间，将 TIME\_MP 转换为用户可读的 DATETIME 类型 |
| 3 | LSN | BIGINT | 当前 LSN |

8） **V$CKPT\_HISTORY**

显示检查点历史信息。该视图需要在开启 ENABLE\_MONITOR 后才能监控检查点信息。

对于未结束的检查点，尚未确定的值输出为 0，例如 TIME\_USED、PAGE\_FLUSHED、FIL、OFF、CKPT\_LSN、FREE\_SPACE 等。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SEQNO | INTEGER | 序列号 |
| 2 | CKPT\_CMD | VARCHAR(24) | 触发检查点的原因。分别如下： INI\_INTERVAL 表示定时触发，由 INI 参数 CKPT\_INTERVAL 确定； INI\_RLOG\_SIZE 表示满足 INI 参数 CKPT\_RLOG\_SIZE 的条件时触发； INI\_DIRTY\_PAGES 表示满足 INI 参数 CKPT\_DIRTY\_PAGE 的条件时触发； UNSAFE/FLUSH\_PAGE 表示强制定时刷页时检测到日志空间不足； UNSAFE/FLUSH\_RLOG 表示日志写入线程检测到日志空间不足； UNSAFE/AFTER\_CKPT 表示检查点线程检测到日志空间不足； CKPT\_MTTR\_TUNE 表示为满足故障恢复时间限制触发； IF\_NECESSARY 表示需要时触发； USER\_CMD 表示用户发起的手工触发； BY\_FORCE 表示由于 DDL 等特殊情况强制触发； OTHER 表示其他情况 |
| 3 | THREAD\_ID | BIGINT | 线程 ID |
| 4 | START\_TIME | DATETIME(6) | 开始时间 |
| 5 | TIME\_USED | BIGINT | 从开始到结束使用时间，单位为微秒（us） |
| 6 | PAGE\_FLUSHED | INTEGER | 刷盘数 |
| 7 | FIL | INTEGER | 文件号 |
| 8 | OFF | BIGINT | 文件偏移量 |
| 9 | CKPT\_LSN | BIGINT | 检查点 LSN |
| 10 | FREE\_SPACE | BIGINT | 检查点完成时刻联机日志文件的空闲空间，单位字节 |
| 11 | IN\_PROCESS | CHAR(1) | 当前检查点是否正在进行中。Y 是；N 否 |

9） **V$CKPT**

显示系统检查点信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | CKPT\_RLOG\_SIZE | INTEGER | 检查点日志大小，单位 MB |
| 2 | CKPT\_DIRTY\_PAGES | INTEGER | 脏页的数量。产生多少脏页后，才强制产生检查点 |
| 3 | CKPT\_INTERVAL | INTEGER | 系统强制产生检查点的时间间隔(s) |
| 4 | CKPT\_FLUSH\_RATE | DEC(5,2) | 每次检查点脏页的刷盘比例 |
| 5 | CKPT\_FLUSH\_PAGES | INTEGER | 每次检查点至少刷盘的脏页数 |
| 6 | LAST\_BEGIN\_TIME | DATETIME(6) | 最近一次执行的开始时间 |
| 7 | LAST\_END\_TIME | DATETIME(6) | 最近一次执行的结束时间 |
| 8 | CKPT\_LSN | BIGINT | 最近一次检查点 LSN |
| 9 | CKPT\_FILE | BIGINT | 最近一次检查点对应的当时的文件号 |
| 10 | CKPT\_OFFSET | BIGINT | 最近一次检查点对应的当时的文件偏移 |
| 11 | STATE | VARCHAR(128) | 检查点状态，只有 2 种。0 NONE，其他 PROCESSING |
| 12 | CKPT\_TOTAL\_COUNT | BIGINT | 检查点已做的个数 |
| 13 | CKPT\_RESERVE\_COUNT | BIGINT | 预先申请日志空间的次数 |
| 14 | CKPT\_FLUSHED\_PAGES | BIGINT | 检查点已刷页的个数 |
| 15 | CKPT\_TIME\_USED | BIGINT | 检查点从开始到结束经历的时间，单位毫秒 |

10） **V$TRX\_SAVEPOINT**

显示所有活动事务的保存点信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TRX\_ID | BIGINT | 当前活动事务的 ID 号 |
| 2 | NAME | VARCHAR(128) | 保存点名字 |
| 3 | SEQ\_NO | INTEGER | 保存点序号 |
| 4 | MSEQ\_NO | INTEGER | MPP 下从 EP 在主 EP 上的对应序号 |
| 5 | LAST\_LOCK | BIGINT | 释放锁的起始地址 |
| 6 | LAST\_OLOCK | BIGINT | 释放 OLOCK 锁的起始地址 |

11） **V$LOCKED\_OBJECT**

显示系统中被锁封锁的对象信息及其所属的会话。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | XIDUSN | INTEGER | 回滚段编号（尚未完善，暂时用 0 代替） |
| 2 | XIDSLOT | INTEGER | 槽号，使用回滚段中的 nth 替代 |
| 3 | XIDSQN | INTEGER | 序列号 |
| 4 | OBJECT\_ID | INTEGER | 被上锁的对象 ID |
| 5 | SESSION\_ID | BIGINT | 会话 ID |
| 6 | USERNAME | VARCHAR(128) | 用户名 |
| 7 | OS\_USER\_NAME | VARCHAR(32) | 系统用户名 |
| 8 | PROCESS | VARCHAR(30) | 进程号与线程号，格式为“进程号：线程号” |
| 9 | LOCKED\_MODE | CHAR(2) | 锁模式；可为：S 锁、X 锁、IX 锁、IS 锁 |
| 10 | LOCKED\_TYPE | VARCHAR(10) | 锁类型；可为：对象锁 |

12） **V$LONG\_TRX**

显示所有活动的长事务的信息, 通过该视图可以查看系统中所有的长事务及其所属站点号。

长事务，指长时间未提交的事务，由最新提交的事务号和系统可分配的总事务号决定。假设系统可分配的总事务号为 N，最新提交的事务号为 N1，那么所有事务号小于(N1 - N/2)的未提交事务都被定义为长事务。长事务总数不能超过 10240，超过后则不再收集。

例如：可分配的总事务号为 1024，当最新提交的事务号为 600 时，计算差值为(600 - 1024/2)=88，则所有事务号小于 88 的未提交事务会被判断为长事务。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TRX\_ID | BIGINT | 当前活动的长事务的 ID 号 |
| 2 | EP\_SEQNO | INTEGER | 事务所在站点号；在单机环境中为 0，在 DSC 环境中为节点号，在 DPC 环境中为 RAFT\_ID |

13） **V$TRX\_VIEW**

显示当前事务可见的所有活动事务视图信息。根据达梦多版本规则，通过该视图可以查询系统中自己所见的事务信息；可以通过与 v$trx 表的连接查询它所见事务的具体信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TRXID | BIGINT | 当前活动事务的 ID 号 |
| 2 | NEXT\_ID | BIGINT | 下一个事务 ID 号，大于等于 next\_id 的事务不可见 |
| 3 | MIN\_ACTIVE\_ID | BIGINT | 所有活动事务最小 ID，小于 min\_active\_id 的事务不可见 |
| 4 | EGTS\_ENO | BIGINT | 刷新视图添加 snap 任务时的 egts 执行号 |
| 5 | TEMP\_ENO | BIGINT | 获取最小事务号时代替 trx 登记缓存事务提交计数的执行号 |
| 6 | TEMP\_CMTSEQ | BIGINT | 获取最小事务号时代替 trx 登记的缓存事务提交计数 |
| 7 | N\_LONG | INTEGER | 长事务数目 |
| 8 | LONG\_TIDS | CLOB | 长事务事务 ID 数组 |
| 9 | N\_PE | INTEGER | 数据页损坏事务信息数目 |
| 10 | PE\_TIDS | CLOB | 数据页损坏事务信息数组 |
| 11 | MVCC\_PAGE\_OPT | INTEGER | 数据页可见性判断优化标记 |
| 12 | LAST\_CMT\_LSN | BIGINT | 上次事务提交产生的 LSN |
| 13 | TRX\_START\_LSN | BIGINT | 第一次分配回滚页时的 LSN |
| 14 | MIN\_LAST\_CMT\_LSN | BIGINT | 可见视图里事务号最小事务的 last\_cmt\_lsn |
| 15 | N\_INHASH\_IDS | INTEGER | 活动事务 ID 数组已使用数目 |
| 16 | INHASH\_IDS | CLOB | 活动事务 ID 数组 |

14） **V$TRX\_CMTARR**

显示当前已提交事务数组信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | CMT\_SEQ | BIGINT | 事务提交计数 |
| 2 | N\_CELL | INTEGER | 可配置数组大小 |
| 3 | N\_CMT\_CELL | INTEGER | 提交事务登记数组大小 |
| 4 | FILL\_POS | BIGINT | 提交事务登记数组填充下标 |
| 5 | LONG\_DIFF | INTEGER | 用于区分长事务计算 |
| 6 | FIRST\_TID | BIGINT | 系统启动后的第一个事务 ID |
| 7 | CMTARR\_MODE\_FLAG | INTEGER | 是否启用基于数组的可见性判断机制 |
| 8 | MIN\_ID | BIGINT | 不包含长事务的最小活动事务 ID |
| 9 | MIN\_START\_LSN | BIGINT | 最小活动事务的启动 LSN |
| 10 | N\_LONG | INTEGER | 长事务数目 |
| 11 | LONG\_ARR | CLOB | 长事务事务 ID 数组 |

#### 10\. 事件

1） **V$EVENT\_NAME**

显示当前系统所支持的等待事件的类型汇总信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | EVENT# | INTEGER | 事件编号 |
| 2 | EVENT | VARCHAR(32) | dbfile read wait：读数据页等待；   dbfile flush wait：写数据页等待；   dbfile remote read：DSC 引起的读磁盘；   dbfile remote write：DSC 引起的写磁盘；   dbfile discard write：buf 不够引起的写磁盘；   dbfile ckpt write：ckpt 引起的写磁盘；   dbfile extend：扩库文件引起的写磁盘；   shared memory pool busy：共享内存并发使用冲突；   buffer busy wait：buffer 并发使用冲突；   dict cache busy：字典 cache 并发使用冲突；   plan cache busy：计划 cache 并发使用冲突；   redo log system busy：redo log 系统并发冲突；   redo log buffer busy：redo log 缓冲区并发冲突；   kernel busy：kernel 并发冲突；   table lock busy：表锁系统并发冲突；   tid lock busy：行锁系统并发冲突；   parallel bdta pool busy：并行 bdta pool 并发冲突；   iid system busy：iid 系统并发冲突；   pseg queue busy：pseg 队列并发冲突；   pseg stack busy：pseg 堆栈并发冲突；   page s latch wait：数据页的 S 闩封锁；   page x latch wait:数据页的 X 闩封锁；   rlog flush wait:日志刷盘；   commit wait:事务提交；   table lock wait：事务间表锁等待发生；   trxid lock wait：事务间行锁等待发生；   scp cache busy：scp 缓存并发冲突；   trx system s busy： 事务系统 s 封锁并发冲突；   trx system x busy：事务系统 x 封锁并发冲突；   trx view s busy：事务可见性 s 封锁并发冲突；   trx view x busy：事务可见性 x 封锁并发冲突；   dscids s busy：dscids s 封锁并发冲突；   dscids x busy：dscids x 封锁并发冲突；   slog single busy：SQL 日志个体并发冲突；   network idle wait：网络处理等待；   preload wait：数据页预加载任务；   session system s latch wait：SESSION 系统的 S 闩封锁；   session system x latch wait：SESSION 系统的 X 闩封锁；   file system s latch wait：文件系统的 S 闩封锁；   file system x latch wait：文件系统的 X 闩封锁；   gtv system s latch wait：DSC 全局事务系统的 S 闩封锁；   gtv system x latch wait：DSC 全局事务系统的 X 闩封锁；   aud system s latch wait：审计缓冲池的 S 闩封锁；   aud system x latch wait：审计缓冲池的 X 闩封锁；   purge tinfo s latch wait：purge 表信息的 S 闩封锁；   purge tinfo x latch wait：purge 表信息的 X 闩封锁；   lbs pool s latch wait：LBS 线程池的 S 闩封锁；   lbs pool x latch wait：LBS 线程池的 X 闩封锁；   fback system s latch wait：可闪回系统的 S 闩封锁；   fback system x latch wait：可闪回系统的 X 闩封锁；   march/rt arch s latch wait：实时归档的 S 闩封锁；   march/rt arch x latch wait：实时归档的 X 闩封锁；   timely arch s latch wait：即时归档的 S 闩封锁；   timely arch x latch wait：即时归档的 X 闩封锁；   bct s latch wait：BCT 的 S 闩封锁；   bct x latch wait：BCT 的 X 闩封锁；   buffer s latch wait：BUFFER 的 S 闩封锁；   buffer x latch wait：BUFFER 的 X 闩封锁；   dict cache s latch wait：字典缓存的 S 闩封锁；   dict cache x latch wait：字典缓存的 X 闩封锁；   pln\_id mapping s latch wait：BP 节点缓存的 S 闩映射封锁；   pln\_id mapping x latch wait：BP 节点缓存的 X 闩映射封锁；   next trxid flush wait：事务 id 刷盘等待；   defer seg create flush wait：延迟段创建刷盘等待；   cmtseq flush wait：提交序号刷盘等待；   lbs ctl s latch wait：DSC 局部缓冲区的 S 闩封锁；   lbs ctl x latch wait：DSC 局部缓冲区的 X 闩封锁；   async\_arch s latch wait：异步归档的 S 闩封锁；   async\_arch x latch wait：异步归档的 X 闩封锁；   sync\_arch s latch wait：同步归档的 S 闩封锁；   sync\_arch x latch wait：同步归档的 X 闩封锁 |
| 3 | WAIT\_CLASS# | INTEGER | 事件类别编号：0(User I/O)、1(SystemI/O)、2(Concurrency)、3(Rlog)、4(Transaction)、5(Memory)、6(Network)、7(Preload)、8(Idle)、9(Cluster)、10(Commit)、11(Arch)、66(Slog) |
| 4 | WAIT\_CLASS | VARCHAR(32) | 事件类别名称：User I/O、System I/O、Concurrency、Rlog、Transaction、Memory、Network、Preload、Idle、Cluster、Commit、arch、Slog |

2） **V$SYSTEM\_EVENT**

显示自系统启动以来所有等待事件的详细信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | EVENT# | INTEGER | 事件编号 |
| 2 | EVENT | VARCHAR(32) | 事件名称。 |
| 3 | TOTAL\_WAITS | BIGINT | 等待次数 |
| 4 | TIME\_WAITED | BIGINT | 等待时间，单位：1/100 秒 |
| 5 | TIME\_WAITED\_MICRO | BIGINT | 等待时间，单位微秒 |
| 6 | AVERAGE\_WAIT\_MICRO | INTEGER | 平均等待时间，单位微秒 |
| 7 | SMAX\_TIME | BIGINT | 最长等待时间，单位微秒 |
| 8 | SMIN\_TIME | INTEGER | 最短等待时间，单位微秒 |
| 9 | WAIT\_CLASS# | INTEGER | 事件类别编号：0(User I/O)、1(SystemI/O)、2(Concurrency)、3(Rlog)、4(Transaction)、5(Memory)、6(Network)、7(Preload)、8(Idle)、9(Cluster)、10(Commit)、11(Arch)、66(Slog) |
| 10 | WAIT\_CLASS | VARCHAR(32) | 事件类别名称：User I/O、System I/O、Concurrency、Rlog、Transaction、Memory、Network、Preload、Idle、Cluster、Commit、arch、Slog |

3） **GV$SYSTEM\_EVENT**

显示自系统启动以来集群所有节点所有等待事件的详细信息。

| 序号 | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INSTANCE\_NAME | VARCHAR(128) | 实例名 |
| 2 | EVENT# | INTEGER | 事件编号 |
| 3 | EVENT | VARCHAR(32) | 事件名称 |
| 4 | TOTAL\_WAITS | BIGINT | 等待次数 |
| 5 | TIME\_WAITED | BIGINT | 等待时间，单位：1/100 秒 |
| 6 | TIME\_WAITED\_MICRO | BIGINT | 等待时间，单位微秒 |
| 7 | AVERAGE\_WAIT\_MICRO | INTEGER | 平均等待时间，单位微秒 |
| 8 | SMAX\_TIME | BIGINT | 最长等待时间，单位微秒 |
| 9 | SMIN\_TIME | INTEGER | 最短等待时间，单位微秒 |
| 10 | WAIT\_CLASS# | INTEGER | 等待事件类别编号 |
| 11 | WAIT\_CLASS | VARCHAR(32) | 等待事件类别名称 |

4） **V$SESSION\_EVENT**

显示当前会话等待事件的所有信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SESSADDR | VARBINARY(8) | 会话地址 |
| 2 | SESSION# | INTEGER | 会话 ID |
| 3 | EVENT# | INTEGER | 事件编号 |
| 4 | EVENT | VARCHAR(32) | 事件名称 |
| 5 | TOTAL\_WAITS | BIGINT | 等待次数 |
| 6 | TIME\_WAITED | BIGINT | 等待时间，单位：1/100 秒 |
| 7 | TIME\_WAITED\_MICRO | BIGINT | 等待时间，单位微秒 |
| 8 | AVERAGE\_WAIT\_MICRO | INTEGER | 平均等待时间，单位微秒 |
| 9 | SMAX\_TIME | BIGINT | 最长等待时间，单位微秒 |
| 10 | SMIN\_TIME | INTEGER | 最短等待时间，单位微秒 |
| 11 | WAIT\_CLASS# | INTEGER | 事件类别编号：0(User I/O)、1(SystemI/O)、2(Concurrency)、3(Rlog)、4(Transaction)、5(Memory)、6(Network)、7(Preload)、8(Idle)、9(Cluster)、10(Commit)、11(Arch)、66(Slog) |
| 12 | WAIT\_CLASS | VARCHAR(32) | 事件类别名称：User I/O、System I/O、Concurrency、Rlog、Transaction、Memory、Network、Preload、Idle、Cluster、Commit、arch、Slog |

5） **GV$SESSION\_EVENT**

显示全局会话等待事件的所有信息。

支持的集群有 DPC、DSC、实时主备、读写分离集群、AFC。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INSTANCE\_NAME | VARCHAR(128) | 实例名 |
| 2 | SESSADDR | VARBINARY(8) | 会话地址 |
| 3 | SESSION# | INTEGER | 会话 ID |
| 4 | EVENT# | INTEGER | 事件编号 |
| 5 | EVENT | VARCHAR(32) | 事件名称 |
| 6 | TOTAL\_WAITS | BIGINT | 等待次数 |
| 7 | TIME\_WAITED | BIGINT | 等待时间，单位：1/100 秒 |
| 8 | TIME\_WAITED\_MICRO | BIGINT | 等待时间，单位微秒 |
| 9 | AVERAGE\_WAIT\_MICRO | INTEGER | 平均等待时间，单位微秒 |
| 10 | SMAX\_TIME | BIGINT | 最长等待时间，单位微秒 |
| 11 | SMIN\_TIME | INTEGER | 最短等待时间，单位微秒 |
| 12 | WAIT\_CLASS# | INTEGER | 事件类别编号：0(User I/O)、1(SystemI/O)、2(Concurrency)、3(Rlog)、4(Transaction)、5(Memory)、6(Network)、7(Preload)、8(Idle)、9(Cluster)、10(Commit)、11(Arch)、66(Slog) |
| 13 | WAIT\_CLASS | VARCHAR(32) | 事件类别名称：User I/O、System I/O、Concurrency、Rlog、Transaction、Memory、Network、Preload、Idle、Cluster、Commit、arch、Slog |

6） **V$SESSION\_WAIT\_HISTORY**

显示当前会话等待事件的历史信息。需要开启 INI 参数 ENABLE\_MONITOR。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SESSADDR | VARBINARY(8) | 会话地址 |
| 2 | SESSION# | INTEGER | 会话 ID |
| 3 | SQL\_ID | INTEGER | SQL 语句 ID |
| 4 | EVENT# | INTEGER | 事件编号 |
| 5 | EVENT | VARCHAR(32) | 事件名称 |
| 6 | P1TEXT | VARCHAR(32) | 等待事件对应的参数 1 说明(如果没有足够参数，则为 NULL，以下参数一样) |
| 7 | P1 | VARCHAR(256) | 等待事件对应的参数 1 值 |
| 8 | P2TEXT | VARCHAR(32) | 等待事件对应的参数 2 说明 |
| 9 | P2 | BIGINT | 等待事件对应的参数 2 值 |
| 10 | P3TEXT | VARCHAR(32) | 等待事件对应的参数 3 说明 |
| 11 | P3 | BIGINT | 等待事件对应的参数 3 值 |
| 12 | P4TEXT | VARCHAR(32) | 等待事件对应的参数 4 说明 |
| 13 | P4 | BIGINT | 等待事件对应的参数 4 值 |
| 14 | TIME\_WAITED | INTEGER | 等待时间，单位：1/100 秒 |
| 15 | TIME\_WAITED\_MICRO | INTEGER | 等待时间，单位微秒 |
| 16 | WAIT\_CLASS# | INTEGER | 事件类别编号：0(User I/O)、1(SystemI/O)、2(Concurrency)、3(Rlog)、4(Transaction)、5(Memory)、6(Network)、7(Preload)、8(Idle)、9(Cluster)、10(Commit)、11(Arch)、66(Slog) |
| 17 | WAIT\_CLASS | VARCHAR(32) | 事件类别名称：User I/O、System I/O、Concurrency、Rlog、Transaction、Memory、Network、Preload、Idle、Cluster、Commit、arch、Slog |
| 18 | P5TEXT | VARCHAR(32) | 等待事件对应的参数 5 说明 |
| 19 | P5 | VARCHAR(1024) | 等待事件对应的参数 5 值，目前仅针对 table lock wait/trxid lock wait 有值，表示等待事务的 trxid 和会话 id |

7） **GV$SESSION\_WAIT\_HISTORY**

显示全局会话等待事件的历史信息。需要开启 INI 参数 ENABLE\_MONITOR。

支持的集群有 DPC、DSC、实时主备、读写分离集群、AFC。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INSTANCE\_NAME | VARCHAR(128) | 实例名 |
| 2 | SESSADDR | VARBINARY(8) | 会话地址 |
| 3 | SESSION# | INTEGER | 会话 ID |
| 4 | SQL\_ID | INTEGER | SQL 语句 ID |
| 5 | EVENT# | INTEGER | 事件编号 |
| 6 | EVENT | VARCHAR(32) | 事件名称 |
| 7 | P1TEXT | VARCHAR(32) | 等待事件对应的参数 1 说明(如果没有足够参数，则为 NULL，以下参数一样) |
| 8 | P1 | VARCHAR(256) | 等待事件对应的参数 1 值 |
| 9 | P2TEXT | VARCHAR(32) | 等待事件对应的参数 2 说明 |
| 10 | P2 | BIGINT | 等待事件对应的参数 2 值 |
| 11 | P3TEXT | VARCHAR(32) | 等待事件对应的参数 3 说明 |
| 12 | P3 | BIGINT | 等待事件对应的参数 3 值 |
| 13 | P4TEXT | VARCHAR(32) | 等待事件对应的参数 4 说明 |
| 14 | P4 | BIGINT | 等待事件对应的参数 4 值 |
| 15 | TIME\_WAITED | INTEGER | 等待时间，单位：1/100 秒 |
| 16 | TIME\_WAITED\_MICRO | INTEGER | 等待时间，单位微秒 |
| 17 | WAIT\_CLASS# | INTEGER | 事件类别编号：0(User I/O)、1(SystemI/O)、2(Concurrency)、3(Rlog)、4(Transaction)、5(Memory)、6(Network)、7(Preload)、8(Idle)、9(Cluster)、10(Commit)、11(Arch)、66(Slog) |
| 18 | WAIT\_CLASS | VARCHAR(32) | 事件类别名称：User I/O、System I/O、Concurrency、Rlog、Transaction、Memory、Network、Preload、Idle、Cluster、Commit、arch、Slog |
| 19 | P5TEXT | VARCHAR(32) | 等待事件对应的参数 5 说明 |
| 20 | P5 | VARCHAR(1024) | 等待事件对应的参数 5 值，目前仅针对 table lock wait/trxid lock wait 有值，表示等待事务的 trxid 和会话 id |

8） **V$DANGER\_EVENT**

记录数据库重要事件或行为信息视图。重要的事件或行为是指 ALTER\_DATABASE、创建表空间、重命名表空间、重命名数据文件和增加数据文件。

当 INI 参数 ENABLE\_MONITOR=1 才有效。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | OPTIME | DATETIME(6) | 重要事件或行为发生的时间 |
| 2 | OPERATION | VARCHAR(1024) | 重要事件或行为执行的语句 |
| 3 | OPUSER | VARCHAR(128) | 执行重要事件或行为的用户 |

9） **V$TASK\_QUEUE**

任务系统中的任务队列信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | READY | BIGINT | 已处理任务数 |
| 2 | TOTAL\_WAIT\_TIME | BIGINT | 已处理任务的总等待时间，单位毫秒 |
| 3 | AVERAGE\_WAIT\_TIME | INTEGER | 已处理任务的平均等待时间，单位毫秒 |
| 4 | STATE | INTEGER | 任务系统状态。0：开启；1：准备关闭；2：关闭 |
| 5 | N\_OPEN\_TASK | INTEGER | OPEN 状态下执行的任务数 |
| 6 | N\_TRIGGER | INTEGER | 正在运行的时间触发器数量 |

10） **V$TRACE\_QUEUE**

跟踪系统中的任务队列信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | WAITING | INTEGER | 等待处理任务数 |
| 2 | READY | BIGINT | 已处理任务数 |
| 3 | TOTAL\_WAIT | BIGINT | 已处理任务的总等待时间，单位毫秒 |
| 4 | AVERAGE\_WAIT | INTEGER | 已处理任务的平均等待时间，单位毫秒 |

11） **V$TASK\_WAITIN**

任务系统中的所有等待任务信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | CMD | VARCHAR(128) | 任务类型 |
| 2 | CREATE\_TIME | DATETIME(0) | 创建时间 |

#### 11\. 进程和线程

1） **V$PROCESS**

显示当前进程信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PID | INTEGER | 进程 ID |
| 2 | PNAME | VARCHAR(256) | 进程名 |
| 3 | TRACE\_NAME | VARCHAR(256) | SQL 日志路径，若 INI 参数 SVR\_LOG 为 0，则值为空串 |
| 4 | TYPE$ | TINYINT | 暂不支持，值始终为 1 |

2） **V$THREADS**

显示系统中所有活动线程的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | BIGINT | 线程 ID |
| 2 | NAME | VARCHAR(128) | 线程名 |
| 3 | START\_TIME | DATETIME(6) | 线程开始时间 |
| 4 | THREAD\_DESC | VARCHAR(1024) | 线程描述 |
| 5 | SESS\_ID | BIGINT | 与本线程关联的会话 ID。NULL 表示无关联的会话 |
| 6 | PROCESSOR\_ID | INTEGER | 线程绑定的 CPU 处理器 ID。65535 表示未绑定 CPU 处理器 |
| 7 | WAIT\_SEQ | INTEGER | 线程等待序号 |
| 8 | WAIT\_STATUS | VARCHAR(128) | 线程等待状态 |
| 9 | WAIT\_TIME | INTEGER | 线程等待时间，单位毫秒，取值-1 表明线程不在等待状态 |

3） **V$THRDS\_POOL**

底层线程池信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | N\_THRDS | INTEGER | 总线程数 |
| 2 | N\_USED\_THRDS | INTEGER | 已使用的线程数 |
| 3 | N\_TEMP\_THRDS | INTEGER | 临时线程数 |
| 4 | MAX\_THRDS | INTEGER | 最大线程数 |
| 5 | MEM\_USED | INTEGER | 内存使用。单位：字节 |

4） **V$THRD\_POOL\_GRP**

上层特定模块中线程池组的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TYPE | VARCHAR(128) | 线程池类型 |
| 2 | ID | INTEGER | 线程池 ID |
| 3 | N\_THRDS | INTEGER | 总线程数 |
| 4 | N\_USED\_THRDS | INTEGER | 使用的线程数 |
| 5 | N\_WAIT\_THRDS | INTEGER | 锁等待的线程数 |
| 6 | N\_SUSPEND\_THRDS | INTEGER | 挂起的线程数 |
| 7 | N\_TASK\_TODO | INTEGER | 等待的任务数 |

#### 12\. 系统信息

1） **V$SYSTEMINFO**

系统信息视图。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | N\_CPU | INTEGER | CPU 个数 |
| 2 | TOTAL\_PHY\_SIZE | BIGINT | 物理内存总大小，单位 BYTE |
| 3 | FREE\_PHY\_SIZE | BIGINT | 剩余物理内存大小，单位 BYTE |
| 4 | TOTAL\_VIR\_SIZE | BIGINT | 虚拟内存总大小，单位 BYTE |
| 5 | FREE\_VIR\_SIZE | BIGINT | 剩余虚拟内存大小，单位 BYTE |
| 6 | TOTAL\_DISK\_SIZE | BIGINT | 磁盘总大小，单位 BYTE |
| 7 | FREE\_DISK\_SIZE | BIGINT | 剩余磁盘大小，单位 BYTE |
| 8 | DRIVER\_NAME | VARCHAR(5) | 驱动器名称 |
| 9 | DRIVER\_TOTAL\_SIZE | BIGINT | 驱动器总空间大小，单位 BYTE |
| 10 | DRIVER\_FREE\_SIZE | BIGINT | 驱动器剩余空间大小，单位 BYTE |
| 11 | LOAD\_ONE\_AVERAGE | DOUBLE | 每分钟平均负载，仅 LINUX 环境有效 |
| 12 | LOAD\_FIVE\_AVERAGE | DOUBLE | 每五分钟平均负载，仅 LINUX 环境有效 |
| 13 | LOAD\_FIFTEEN\_AVERAGE | DOUBLE | 每十五分钟平均负载，仅 LINUX 环境有效 |
| 14 | CPU\_USER\_RATE | DOUBLE | 用户模式占用 CPU 使用率，仅 LINUX 环境有效 |
| 15 | CPU\_SYSTEM\_RATE | DOUBLE | 系统模式占用的 CPU 使用率，仅 LINUX 环境有效 |
| 16 | CPU\_IDLE\_RATE | DOUBLE | 空闲 CPU 百分比，仅 LINUX 环境有效 |
| 17 | SEND\_BYTES\_TOTAL | BIGINT | 发送的总字节数，仅 LINUX 环境有效 |
| 18 | RECEIVE\_BYTES\_TOTAL | BIGINT | 接收的总字节数，仅 LINUX 环境有效 |
| 19 | SEND\_BYTES\_PER\_SECOND | BIGINT | 当前每秒发送字节数，仅 LINUX 环境有效 |
| 20 | RECEIVE\_BYTES\_PER\_SECOND | BIGINT | 当前每秒接收字节数，仅 LINUX 环境有效 |
| 21 | SEND\_PACKAGES\_PER\_SECOND | BIGINT | 当前每秒发送数据包数，仅 LINUX 环境有效 |
| 22 | RECEIVE\_PACKAGES\_PER\_SECOND | BIGINT | 当前每秒接收数据包数，仅 LINUX 环境有效 |
| 23 | USED\_PHY\_SIZE | BIGINT | 当前系统使用的内存大小，单位 BYTE |

2） **V$NETINFO**

网络信息视图。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | RECV\_BYTES | BIGINT | 网络接收的字节数 |
| 2 | SEND\_BYTES | BIGINT | 网络发送的字节数 |

3） **V$CMD\_HISTORY**

通过本视图可以观察系统的一些命令的历史信息。其中 cmd 指的是 SESS\_ALLOC，SESS\_FREE，CKPT，TIMER\_TRIG，SERERR\_TRIG，LOG\_REP，MAL\_LETTER， CMD\_LOGIN 等。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | CMD | VARCHAR(24) | 命令 |
| 2 | THREAD\_ID | BIGINT | 线程 ID |
| 3 | SESS\_ID | BIGINT | 会话 ID，系统内部标识 |
| 4 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |
| 5 | TRX\_ID | BIGINT | 事务 ID |
| 6 | STMT\_ID | INTEGER | 语句 ID |
| 7 | START\_TIME | DATETIME(6) | 命令开始时间 |
| 8 | TIME\_USED | BIGINT | 命令从开始执行到执行结束花费的时间，单位为微秒（us） |

4） **V$RUNTIME\_ERR\_HISTORY**

监控运行时错误历史。异常分为三种：一种是系统异常，用户没有捕获，由 vm\_raise\_runtime\_error 产生；第二种是用户异常，用户捕获错误，并抛出自定义异常，由 nthrow\_exec 产生；第三种是语法异常，语法未通过，由 nsvr\_build\_npar\_cop\_out 产生。

该视图仅在异常被抛出时进行记录，并不会跟踪记录异常是否被处理。对于 DMSQL 程序，即便使用 EXCEPTION 语句对异常进行了处理，仍能在该视图中查询到该异常。

V$RUNTIME\_ERR\_HISTORY 视图中各个列的含义如下：

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SEQNO | INTEGER | 该类语句的执行编号 |
| 2 | SESS\_ID | BIGINT | 执行会话 ID，系统内部标识 |
| 3 | SESS\_SEQ | INTEGER | 会话序列号，每创建一个会话，系统自动为其生成一个全局递增的序列号 |
| 4 | TRX\_ID | BIGINT | 执行事务 ID |
| 5 | EXEC\_ID | BIGINT | 虚拟机的执行序号 |
| 6 | VM\_ID | INTEGER | 虚拟机 ID |
| 7 | STKFRM\_LEVEL | INTEGER | 当前栈帧在虚拟机的层次 |
| 8 | SQL\_TEXT | VARCHAR(1000) | 获得该层栈帧执行的 SQL 语句，若字符长度超过 1000，则取前 1000 个字符 |
| 9 | SU\_FLAG | CHAR(1) | U =用户异常，S =系统异常，P =语法异常 |
| 10 | ECPT\_CODE | INTEGER | 异常错误号 |
| 11 | ECPT\_DESC | VARCHAR(256) | 异常描述 |
| 12 | MAL\_ID | BIGINT | 邮件标识号 |
| 13 | ERR\_TIME | DATETIME(3) | 错误产生的时间 |
| 14 | MPP\_EXEC\_ID | INTEGER | MPP 会话句柄上的执行序号，同一个会话上的每个节点上值相同 |
| 15 | OBJECT\_NAME | VARCHAR(128) | 出错的对象名，当前仅若干特定的错误中获取出错对象名；其他的为 NULL |
| 16 | USER\_NAME | VARCHAR(128) | 记录生成错误时 SESSION 对应的用户名 |
| 17 | APPNAME | VARCHAR(128) | 记录生成错误时 SESSION 所在的应用名 |
| 18 | CLNT\_IP | VARCHAR(128) | 记录生成错误时 SESSION 对应的客户端的地址信息 |
| 19 | SQL\_ID | INTEGER | 记录生成错误时 SESSION 中当前 SQL 语句 ID；为-1 表示错误是在语法分析阶段登记的 |

5） **V$INSTANCE\_LOG\_HISTORY**

用于查询服务器实例运行期间生成的最近 1 万条事件日志。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SEQNO | INTEGER | 日志序号，从 0 开始递增。每次服务器重启后清零 |
| 2 | LOG\_TIME | DATETIME(6) | 日志生成时间，精确到秒 |
| 3 | PID | BIGINT | 生成日志的进程 ID |
| 4 | THREAD\_NAME | VARCHAR(128) | 生成日志的线程名 |
| 5 | LEVEL$ | VARCHAR(20) | 日志级别描述。可取值为：INFO、WARN、ERROR、FATAL |
| 6 | TXT | VARCHAR(2048) | 日志详细内容 |

6） **V$INSTANCE\_RECOVERY**

用于监控提供给用户的用于限制数据库故障恢复 IO 的相关机制。监控的具体相关机制如下：

(1) 设置 FAST\_START\_MTTR\_TARGET；

(2) 设置 CKPT\_INTERVAL；

(3) 设置 CKPT\_RLOG\_SIZE；

(4) 设置 CKPT\_DIRTY\_PAGES

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | RECOVERY\_ESTIMATED\_IOS | BIGINT | 缓存中的脏页数量 |
| 2 | ACTUAL\_REDO\_BLKS | BIGINT | 实际需要恢复的联机日志块数 |
| 3 | TARGET\_REDO\_BLKS | INTEGER | 当前检查点需要处理的联机日志块数，等于 CKPT\_RLOG\_SIZE 参数对应的块个数 |
| 4 | LOG\_FILE\_SIZE\_REDO\_BLKS | INTEGER | 检查点完成前，保证日志不会发生切换所需要的联机日志块数最大值，等于 CKPT\_RLOG\_SIZE 参数对应的块个数 |
| 5 | LOG\_CHKPT\_TIMEOUT\_REDO\_BLKS | INTEGER | 暂不支持 |
| 6 | LOG\_CHKPT\_INTERVAL\_REDO\_BLKS | INTEGER | 检查点间隔，等于 CKPT\_INTERVAL 参数值 |
| 7 | FAST\_START\_IO\_TARGET\_REDO\_BLKS | INTEGER | 暂不支持 |
| 8 | TARGET\_MTTR | INTEGER | 有效的故障恢复平均时间，单位秒。若设置了 FAST\_START\_MTTR\_TARGET，等于该值。未设置则为预估的故障恢复平均时间。 |
| 9 | ESTIMATED\_MTTR | INTEGER | 预估的故障恢复平均时间，单位秒 |
| 10 | CKPT\_BLOCK\_WRITES | BIGINT | 检查点发起的块写入次数 |
| 11 | OPTIMAL\_LOGFILE\_SIZE | INTEGER | 根据联机日志故障恢复所需要的时间推荐的联机日志大小，单位 MB |
| 12 | ESTD\_CLUSTER\_AVAILABLE\_TIME | INTEGER | 共享集群环境下当出现节点故障后可恢复使用的时间。等于预估故障处理需要重演日志的时间 |
| 13 | WRITES\_MTTR | INTEGER | FAST\_START\_MTTR\_TARGET 参数引起的写入次数。等于达到 RLOG\_RESERVE\_THRESHOLD 而触发的检查点次数 |
| 14 | WRITES\_LOGFILE\_SIZE | INTEGER | 日志量达到 CKPT\_LOG\_SIZE 所触发的检查点刷盘次数 |
| 15 | WRITES\_LOG\_CHECKPOINT\_SETTINGS | INTEGER | 达到检查点间隔发起的检查点刷盘次数 |
| 16 | WRITES\_OTHER\_SETTINGS | INTEGER | 达到其他设置条件触发检查点刷盘次数，主要为 CKPT\_DIRTY\_PAGE 达到设定值触发 |
| 17 | WRITES\_AUTOTUNE | INTEGER | 打开 FAST\_START\_MTTR\_TARGET 后，由于 RLOG\_RESERVE\_THRESHOLD 自动调整时所产生的检查点刷盘次数 |
| 18 | WRITES\_FULL\_THREAD\_CKPT | INTEGER | 完全检查点次数。DSC 环境下只要控制节点上发生 |

**7)** **V$INI\_SYNC\_INFO**

记录最后一次 INI 参数同步的时间及错误码。

需要注意：

1. INI 同步动作由备库触发，动态视图在对应备库的查询有效；
2. LAST\_SYNC\_TIME 记录的是真正进行了 INI 同步的时间，而不是触发 INI\_SYNC 的时间。当备库检测到主库 INI 参数没有修改时，备库为避免无效同步动作产生通信资源浪费，即使此时达到 INI\_SYNC 设置的同步间隔，也不会真正进行同步动作，LAST\_SYNC\_TIME 不会变化；
3. INI\_SYNC 参数说明：

开启 INI\_SYNC 参数同步后，参数的同步原则如下：

(1) 静态 INI 参数：仅同步 dm.ini 文件值，不同步内存值，备库需要重启才能使用新的参数值；

(2) 系统级动态 INI 参数：同时同步 dm.ini 文件值与内存值；

(3) 会话级动态 INI 参数：同步全局内存值，不同步会话上的 INI 参数值；

(4) 若是在 INI 同步改进前后的两个版本间执行，不会真正同步，而是直接返回成功；

(5) INI\_FILE 类型的参数，只会写入 INI 文件，需要重启才能生效；

(6) 不论是否开启 INI\_SYNC 参数，对于参数 ENABLE\_AUDIT、PWD\_POLICY、PWD\_MIN\_LEN、MAC\_LABEL\_OPTION、ENABLE\_DDL\_ANY\_PRIV，主库修改后，备库会随重演同步调整 INI 参数值。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | LAST\_SYNC\_TIME | VARCHAR(50) | 最后一次 INI 同步时间，没有进行过同步时，此字段为空 |
| 2 | LAST\_SYNC\_CODE | INTEGER | 最后一次 INI 同步的错误码 CODE，没有进行过同步时，此字段值为 0 |

**8)** **V$SYSTYPES**

返回当前支持的、可用于 DDL 语句的类型名称。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TYPE\_NAME | VARCHAR(32) | 类型名称 |

#### 13\. MAL 系统

1） **V$MAL\_SYS**

MAL 系统信息视图。如果是数据守护环境，则只显示主库的 MAL 系统信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SYS\_STATUS | INTEGER | MAL 系统状态：0:OPEN,1:PRE\_SHUTDOWN,2:SHUTDOWN |
| 2 | STMT\_ID | INTEGER | MAL 系统当前 stmtid |
| 3 | NEXT\_MAL\_ID | BIGINT | 下一个 MAL\_ID |
| 4 | MAL\_PORT | INTEGER | MAL 监听端口 |
| 5 | N\_SITE | INTEGER | MAL 配置的站点数目 |
| 6 | MAL\_NUM | INTEGER | MAL 系统邮箱数目 |
| 7 | MAL\_SEQ\_NO | INTEGER | 站点本身的 MAL 序号 |
| 8 | EMPTY\_LET\_NUM | INTEGER | 空邮件数目 |
| 9 | MAL\_CHECK\_INTERVAL | INTEGER | 链路检测间隔。单位：秒 |
| 10 | MAL\_CONN\_FAIL\_INTERVAL | INTEGER | 认定链路断开的时间间隔。单位：秒 |
| 11 | MAL\_COMPRESS\_LEVEL | INTEGER | 邮件压缩级别。取值范围 0~10。0 代表不进行消息压缩，为默认值   1~9 表示采用 zip 算法，从 1 到 9 表示压缩速度依次递减，压缩率依次递增。   10 表示采用 snappy 算法，压缩速度高于 zip 算法，压缩率相对低 |
| 12 | MAL\_BUF\_SIZE | INTEGER | 单个 MAL 缓存大小限制，单位 MB。当 MAL 的缓存邮件超过此大小，会将邮件存储到文件中。取值范围 0~500000，缺省为 100，配置为 0 表示无限制 |
| 13 | MAL\_SYS\_BUF\_SIZE | INTEGER | MAL 系统总内存大小限制，单位 MB。取值范围 0~500000，缺省为 0，表示无限制 |
| 14 | MAL\_VPOOL\_SIZE | INTEGER | MAL 配置的总的 POOL 大小，单位 MB。取值范围 1~500000，缺省为 128 |
| 15 | MAL\_TEMP\_PATH | VARCHAR(256) | 指定临时文件的目录。当邮件使用的内存超过 MAL\_BUF\_SIZE 或者 MAL\_SYS\_BUF\_SIZE 时，将新产生的邮件保存到临时文件中。如果缺省，则新产生的邮件保存到 temp.dbf 文件 |
| 16 | MAL\_CHECK\_TIMEOUT | INTEGER | 单个实例的 MAL 网络最大延迟时间，0 表示不进行 MAL 网络延迟时间检测。需要和 MAL\_CHECK\_IP 配合使用。仅当 MAL\_CHECK\_INTERVAL 不为 0 时有效。单位毫秒（ms），取值范围 0~65534，缺省为 0 |
| 17 | MAL\_CHECK\_IP | VARCHAR(128) | 第三方确认机器的 IP，用于检测各个实例的 MAL 网络延迟时间。需要和 MAL\_CHECK\_TIMEOUT 配合使用 |
| 18 | MAL\_SEND\_THRESHOLD | INTEGER | 最大待发送邮件数，用于控制待发送邮件总数，防止发送邮件堆积。取值范围 1024~10000，缺省为 2048 |
| 19 | MAL\_LEAK\_CHECK | INTEGER | 是否打开 MAL 内存泄露检查。0：关闭；1：打开。缺省为 0 |
| 20 | MAL\_LOGIN\_TIMEOUT | INTEGER | MPP/DBLINK 等实例间登录时的超时检测间隔 3~1800，单位秒，缺省为 15 |
| 21 | MAL\_COMBIN\_BUF\_SIZE | INTEGER | 指定 MAL 消息合并发送的缓冲区大小，单位 KB。MAL 发送消息时进行合并，减少网络发送次数。取值范围 0~131072。0 表示不进行消息合并，缺省为 0。最小缓冲区大小 128KB，当设置值大于 0 小于 128 时，自动调整为 128 |
| 22 | MAL\_MESSAGE\_CHECK | INTEGER | 是否对 MAL 通信消息启用消息体校验（只有当消息的发送端和接收端都配置为 1 才启用通信体校验）。0：不启用；1：启用。缺省为 1 |
| 23 | MAL\_MSG\_ENCRYPT | INTEGER | MAL 系统通讯加密方式。0：不启用；1、4：启用 SSL 通讯加密；3：启用国密 SSL 通讯加密，DMMPP 和 DMDSC 集群暂不支持国密 SSL 通讯加密。缺省为 0 |
| 24 | MAL\_USE\_RDMA | INTEGER | Linux 环境下，MAL 是否使用 RDMA 通讯方式。0：否；1：是。缺省为 0 |

2） **V$MAL\_INFO**

MAL 邮箱信息视图。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | MAL\_ID | BIGINT | MAL 标识号 |
| 2 | ORG\_SITE\_NO | INTEGER | 创建 MAL 的原始站点号 |
| 3 | DEST\_SITE\_NO | INTEGER | 目标站点号 |
| 4 | MAX\_BUF\_SIZE | BIGINT | 保存邮件的最大缓存大小，单位 BYTE |
| 5 | USED\_BUF\_SIZE | BIGINT | 已经使用的缓存大小，单位 BYTE |
| 6 | RECEIVE\_NUM | INTEGER | 收到的邮件数。该统计字段在参数 ENABLE\_MONITOR=1 的条件下生效 |
| 7 | DISCARD\_NUM | INTEGER | 废弃的邮件数 |
| 8 | LETTER\_NUM | INTEGER | 普通邮件数目 |
| 9 | PLN\_LET\_NUM | INTEGER | 执行计划中的邮件总数目 |
| 10 | WAIT\_FLAG | INTEGER | 等待状态。1：等待 0：非等待 |
| 11 | MCPR\_FLAG | INTEGER | MAL 任务处理情况。0：RESUME； 1：MPLN；2：CACEL；4：PAUSE |
| 12 | SESS\_ID | BIGINT | MAL 对应的会话 ID，和 V$SESSIONS 中的 SESS\_ID 对应 |
| 13 | DONE\_NUM | INTEGER | 处理的邮件数 |
| 14 | TOTAL\_TIME | BIGINT | 邮件处理的总用时，单位秒 |
| 15 | SEND\_LETTER\_NUM | INTEGER | 发送的邮件数。该统计字段在参数 ENABLE\_MONITOR=1 的条件下生效 |
| 16 | SEND\_BYTES | BIGINT | 发送的字节总数。该统计字段在参数 ENABLE\_MONITOR=1 的条件下生效 |
| 17 | RECV\_LETTER\_NUM | INTEGER | 接收的邮件数。该统计字段在参数 ENABLE\_MONITOR=1 的条件下生效 |
| 18 | RECV\_BYTES | BIGINT | 接收的字节总数。该统计字段在参数 ENABLE\_MONITOR=1 的条件下生效 |
| 19 | CURR\_TIME | DATETIME(0) | 当前系统时间 |

3） **V$MAL\_LETTER\_INFO**

MAL 上的信件信息视图。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | MAL\_ID | BIGINT | MAL 标识号 |
| 2 | IS\_IN\_MEM | INTEGER | 是否在缓存中 |
| 3 | FILE\_ID | INTEGER | 所在临时表空间的文件号 |
| 4 | PAGE\_NO | INTEGER | 所在临时表空间的页号 |
| 5 | STMT\_ID | INTEGER | 句柄 ID |
| 6 | PLN\_OP\_ID | INTEGER | 通讯操作符的计划序号 |
| 7 | ORG\_SITE | INTEGER | 原始站点号 |
| 8 | MPP\_EXEC\_ID | BIGINT | 操作符的执行序号 |
| 9 | BUILD\_TIME | BIGINT | 邮件发送序号 |
| 10 | P\_SRC\_SITE | INTEGER | 邮件的物理站点号 |
| 11 | L\_SRC\_SITE | INTEGER | 邮件的逻辑站点号 |
| 12 | MSG\_LEN | INTEGER | 信件的消息长度，单位 BYTE |
| 13 | TMP\_USED\_EXTENT\_NUM | INTEGER | 邮件所占用临时表空间簇的个数 |

4） **V$MAL\_USING\_LETTERS**

服务器中正在使用或者使用过但是没有释放的邮件信息，用于检查 MAL 系统潜在的内存泄露，INI 参数 MAL\_LEAK\_CHECK 为 1 时有效。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | MAL\_ID | BIGINT | MAL 标识号 |
| 2 | STMT\_ID | INTEGER | 句柄 ID |
| 3 | PLN\_OP\_ID | INTEGER | 通讯操作符的计划序号，仅在 MPP 环境下有效 |
| 4 | ORG\_SITE | INTEGER | 原始站点号 |
| 5 | SRC\_SITE | INTEGER | 源站点号 |
| 6 | DEST\_SITE | INTEGER | 目标站点号 |
| 7 | MPP\_EXEC\_ID | BIGINT | 操作符的执行序号 |
| 8 | BUILD\_TIME | BIGINT | 邮件发送序号 |
| 9 | P\_SRC\_SITE | INTEGER | 邮件的物理站点号 |
| 10 | L\_SRC\_SITE | INTEGER | 邮件的逻辑站点号 |
| 11 | CMD\_TYPE | VARCHAR(128) | 邮件的消息类型 |
| 12 | MSG\_LEN | INTEGER | 信件的消息长度，单位 BYTE |
| 13 | FILE\_NAME | VARCHAR(256) | 分配邮件代码的文件名 |
| 14 | LINENO | INTEGER | 分配邮件代码的行号 |

5） **V$ASM\_MAL\_SYS**

ASVRMAL 系统信息视图。仅 DSC 环境可使用。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | MAL\_CHECK\_INTERVAL | INTEGER | 链路检测间隔，单位：秒 |
| 2 | MAL\_CONN\_FAIL\_INTERVAL | INTEGER | 认定链路断开的时间间隔，单位：秒 |
| 3 | MAL\_CHECK\_TIMEOUT | INTEGER | 单个实例的 MAL 网络最大延迟时间，表示不进行 MAL 网络延迟时间检测。需要和 MAL\_CHECK\_IP 配合使用。仅当 MAL\_CHECK\_INTERVAL 不为 0 时有效。单位毫秒（ms），取值范围 0~65535，缺省为 0 |
| 4 | MAL\_CHECK\_IP | VARCHAR(128) | 第三方确认机器的 IP，用于检测各个实例的 MAL 网络延迟时间。需要和 MAL\_CHECK\_TIMEOUT 配合使用 |
| 5 | MAL\_LOGIN\_TIMEOUT | INTEGER | MPP/DBLINK 等实例间登录时的超时检测间隔 3~1800，单位秒，缺省为 15 |
| 6 | MAL\_BUF\_SIZE | INTEGER | 单个 MAL 缓存大小限制，单位 MB。当 MAL 的缓存邮件超过此大小，会将邮件存储到文件中。取值范围 0~500000，缺省为 100，配置为 0 表示无限制 |
| 7 | MAL\_SYS\_BUF\_SIZE | INTEGER | MAL 系统总内存大小限制，单位 MB。取值范围 0~500000，缺省为 0，表示无限制 |
| 8 | MAL\_VPOOL\_SIZE | INTEGER | MAL 配置的总的 POOL 大小，单位 MB。取值范围 1~500000，缺省为 128 |
| 9 | MAL\_MESSAGE\_CHECK | INTEGER | 是否对 MAL 通信消息启用消息体校验（只有当消息的发送端和接收端都配置为 1 才启用通信体校验）。0：不启用；1：启用。缺省为 1 |
| 10 | MAL\_COMPRESS\_LEVEL | INTEGER | 邮件压缩级别 ，取值范围 0~10。0 代表不进行消息压缩，为默认值   1~9 表示采用 zip 算法，从 1 到 9 表示压缩速度依次递减，压缩率依次递增。   10 表示采用 snappy 算法，压缩速度高于 zip 算法，压缩率相对低 |
| 11 | MAL\_USE\_RDMA | INTEGER | Linux 环境下，MAL 是否使用 RDMA 通讯方式。0：否；1：是。缺省为 0 |

6） **V$ASM\_MAL\_INI**

ASVRMAL 参数信息。仅 DSC 环境可使用。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | MAL\_NAME | VARCHAR (128) | MAL 名称 |
| 2 | MAL\_INST\_NAME | VARCHAR (256) | 实例名称 |
| 3 | MAL\_HOST | VARCHAR (256) | IP 地址 |
| 4 | MAL\_PORT | INTEGER | 端口号 |
| 5 | MAL\_INST\_HOST | VARCHAR (256) | 对应实例 IP 地址 |
| 6 | MAL\_INST\_PORT | INTEGER | 对应实例的端口号 |
| 7 | MAL\_LINK\_MAGIC | INTEGER | MAL 链路网段标识 |

7） **V$MAL\_SITE\_INFO**

MAL 站点信息视图。MPP 模式下，自动收集 MPP 各个站点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SRC\_SITE\_SEQ | INTEGER | 发送邮件的源站点 |
| 2 | DEST\_SITE\_SEQ | INTEGER | 目标站点序号 |
| 3 | MAL\_PORT\_NUM | INTEGER | 目标站点到本站点的 MAL 链路数 |
| 4 | BUILD\_TIME | BIGINT | 下一个邮件发送序号 |
| 5 | LBTAPFDS | BIGINT | 收到的邮件中已处理的最后一个邮件的序号 |
| 6 | CUR\_LETTER\_NUM | INTEGER | 当前保存不连续邮件的个数 |
| 7 | MAX\_LETTER\_NUM | INTEGER | 目前为止不连续邮件的最大个数 |
| 8 | TOTAL\_LINK\_NUM | INTEGER | 已创建到目标站点的 MAL\_LINK 数 |
| 9 | FREE\_LINK\_NUM | INTEGER | 当前空闲的 MAL\_LINK 数 |
| 10 | SEND\_LETTER\_NUM | INTEGER | 当前发送的邮件数 |
| 11 | SEND\_BYTES | BIGINT | 当前发送的字节总数 |
| 12 | RECV\_LETTER\_NUM | INTEGER | 当前接收的邮件数 |
| 13 | RECV\_BYTES | BIGINT | 当前接收的字节总数 |
| 14 | CURR\_TIME | DATETIME(0) | 当前系统时间 |

8） **V$MAL\_LINK\_STATUS**

查询本地实例到远程实例的 MAL 链路连接状态。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SRC\_SITE | VARCHAR(256) | 源站点实例名 |
| 2 | DEST\_SITE | VARCHAR(256) | 目的站点实例名 |
| 3 | CTL\_LINK\_STATUS | VARCHAR(256) | 控制链路连接状态，CONNECTED 表示连接已建立，DISCONNECT 表示连接断开 |
| 4 | DATA\_LINK\_STATUS | VARCHAR(256) | 数据链路连接状态，CONNECTED 表示连接已建立，DISCONNECT 表示连接断开 |

9） **V$RDMA\_CONN\_INFO**

MAL 系统使用 RDMA 通信的连接信息视图。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SEND\_SIGNAL\_CNT | INTEGER | 发送带有 SIGNAL 的工作请求个数 |
| 2 | SEND\_CQ\_POLL\_CNT | INTEGER | 发送端 POLL\_CQ(轮询完成队列)次数 |
| 3 | MBLK\_SIZE | INTEGER | 每次接收消息缓存大小 |
| 4 | MAX\_SEND\_WR | INTEGER | 允许发送的最大请求数 |
| 5 | CQ\_MOD | INTEGER | 发送端生成 CQE(完成队列条目)的批量次数，连续执行 CQ\_MOD 次 POST\_SEND 生成一个 CQE |
| 6 | SEND\_NUM | BIGINT | POST\_SEND 执行次数，CQ\_MOD 配合决定是否生成 CQE，与 MAX\_SEND\_WR 配置决定是否等待 ACK 响应 |
| 7 | MAX\_INLINE\_DATA | INTEGER | 发送队列上内联数据最大大小 |
| 8 | MAX\_RECV\_WR | INTEGER | 允许接收的最大请求数 |
| 9 | POLL\_RCNT | BIGINT | 接收操作 POLL\_CQ(轮询完成队列)返回总次数 |
| 10 | COPY\_RCNT | BIGINT | 已经拷贝走的消息块个数 |
| 11 | IS\_CONNECTED | CHAR(1) | 是否成功连接 |
| 12 | MAL\_PORT | INTEGER | MAL 监听端口，用于数据守护、DSC、MPP 等环境中各节点实例之间 MAL 链路配置，监听端端口配置此参数，取值范围 1024~65534，发起连接端的端口在 1024~65535 之间随机分配 |
| 13 | MAL\_HOST | VARCHAR(20) | 节点实例 |
| 14 | CONN\_TYPE | VARCHAR(25) | 连接链路类型，有三种类型：控制链路、数据链路、DSC 链路；DSC 连接链路只有在 DSC 集群环境下才会出现 |

#### 14\. 通讯

1） **V$DBLINK**

动态使用到的数据库链接信息视图。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | LINK\_CONN | BIGINT | DBLINK 连接句柄 |
| 2 | LINK\_ID | INTEGER | dblink 的 ID |
| 3 | LINK\_NAME | VARCHAR(128) | DBLINK 的名称 |
| 4 | SCH\_ID | INTEGER | DBLINK 模式 ID |
| 5 | OWNER\_ID | INTEGER | DBLINK 用户 ID |
| 6 | IS\_PUBLIC | VARCHAR(3) | 是否为 PUBLIC |
| 7 | LOGIN\_NAME | VARCHAR(128) | 登录名 |
| 8 | HOST\_NAME | VARCHAR(1024) | 主库名 |
| 9 | port\_num | integer | 端口号 |
| 10 | LOGGED\_ON | VARCHAR(3) | DBLINK 当前是否已链接 |
| 11 | HETEROGENEOUS | VARCHAR(3) | DBLINK 同步链接为 YES，异步链接为 NO |
| 12 | PROTOCOL | VARCHAR(6) | DBLINK 通信协议 |
| 13 | IN\_USE | VARCHAR(3) | 当前 DBLINK 句柄是否正在被使用 |

#### 15\. 系统包

1） **V$CACHEPKG**

显示当前系统中的包的使用信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 包名 |
| 2 | N\_FIXED | INTEGER | 包被引用的次数 |
| 3 | DISABLED | CHAR(1) | 包是否被禁用。“Y”：是，“N"：否 |
| 4 | MEM\_SIZE | INTEGER | 包的内存大小，单位 BYTE |
| 5 | ADDRESS | VARBINARY(8) | 包的地址 |
| 6 | ID | INTEGER | 包 ID |
| 7 | CUR\_SCHID | INTEGER | 当前的模式 ID |
| 8 | CUR\_USERID | INTEGER | 当前的用户 ID |
| 9 | IS\_DEF\_INVOKE | CHAR(1) | 是否已定义者权限调用 |

2） **V$DBMS\_LOCKS**

显示当前系统中的申请的 DBMS\_LOCK 包封锁情况。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | HANDLE | VARCHAR(128) | 封锁的锁对象句柄 |
| 2 | ID | INTEGER | 封锁的锁对象 ID |
| 3 | MODE | VARCHAR(10) | 封锁的模式 |
| 4 | OWN\_SESS | BIGINT | 申请封锁的 session |
| 5 | WAIT\_SESS | BIGINT | 封锁等待的 session，无等待为 NULL |

3） **V$DB\_PIPES**

记录使用 DBMS\_PIPE 包创建的管道的相关信息。

| **序号** | **列名** | **类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) NOT NULL | 管道的名字 |
| 2 | OWNERID | BIGINT NOT NULL | 管道拥有者 ID |
| 3 | TYPE | VARCHAR(7) | 管道类型:PUBLIC/PRIVATE |
| 4 | PIPE\_SIZE | BIGINT | 管道的长度，单位 BYTE |

4） **V$SCHEDULER\_JOBS\_RUNNING**

记录数据库中所有由 DBMS\_SCHEDULER 包创建且正在执行的作业。

| **序号** | **列名** | **类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SID | BIGINT | 作业执行的会话 ID |
| 2 | OWNER | VARCHAR(128) | 作业执行的所有者 |
| 3 | JOB\_NAME | VARCHAR(128) | 作业名称 |
| 4 | THIS\_DATE | DATETIME(6) | 作业此次开始执的时间 |
| 5 | INSTANCE | INTEGER | 作业执行的实例（节点号） |

5） **V$SYSTEM\_PACKAGES**

显示当前 DM 支持的系统包的有效状态。相比于 SF\_CHECK\_SYSTEM\_PACKAGES，通过本视图能更清晰地看到各系统包的有效状态。部分特殊系统包无法通过该视图查看有效状态，针对视图中无法查到的包，可以查看《DM8 系统包使用手册》等获取相应系统包有效状态的查询方法。

| **序号** | **列名** | **类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 包名 |
| 2 | ID | INTEGER | 包 ID，若尚未创建则为 NULL |
| 3 | SCHNAME | VARCHAR(128) | 包所属的模式 |
| 4 | IS\_VALID | SMALLINT | 包是否有效 |

#### 16\. 审计与加密

1） **V$AUDITRECORDS**

显示审计文件路径下的审计文件的审计记录，审计文件路径由 INI 参数 AUD\_PATH 指定，若未指定，则默认为 SYSTEM\_PATH 路径。

此动态性能视图只有在审计开关打开时，视图内容实时更新；审计开关关闭后，视图保留已有历史数据但不再更新。此视图只有审计用户可以查询。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | USERID | INTEGER | 用户 ID |
| 2 | USERNAME | VARCHAR(128) | 用户名 |
| 3 | ROLEID | INTEGER | 角色 ID。 没有具体角色的用户和 SQL 序列审计，没用角色信息 |
| 4 | ROLENAME | VARCHAR(128) | 角色名。 没有具体角色的用户和 SQL 序列审计，没用角色信息 |
| 5 | IP | VARCHAR(64) | IP 地址 |
| 6 | SCHID | INTEGER | 模式 ID |
| 7 | SCHNAME | VARCHAR(128) | 模式名 |
| 8 | OBJID | INTEGER | 对象 ID |
| 9 | OBJNAME | VARCHAR(128) | 对象名 |
| 10 | OPERATION | VARCHAR(128) | 操作类型名 |
| 11 | SUCC\_FLAG | CHAR(1) | 成功标记 |
| 12 | SQL\_TEXT | VARCHAR(8188) | SQL 文本 |
| 13 | DESCRIPTION | VARCHAR(8188) | 描述信息 |
| 14 | OPTIME | DATETIME(6) | 操作时间 |
| 15 | MAC | VARCHAR(25) | 操作的 MAC 地址 |
| 16 | SEQNO | TINYINT | DMDSC 环境下表示生成审计记录的节点号，非 DMDSC 环境下始终 |
| 17 | BIND\_INFO | VARCHAR(8188) | 绑定参数具体值，如果绑定参数是复杂类型，仅记录类型名，不记录具体值，记录的格式为\[第几个参数，参数类型，参数值\] |

2） **V$AUDIT\_SPACE**

显示审计文件存储空间信息。此动态性能视图只有审计用户可以查询。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | AUD\_PATH | VARCHAR(256) | 审计文件存放路径 |
| 2 | AUDIT\_FILE\_FULL\_MODE | INTEGER | 剩余空间不足时的处理方式：   1：审计文件创建失败，卡住   2：审计文件创建失败，不再审计   3：结合 1 和 2，先尝试删老审计文件，再创建审计文件，失败则不再审计 |
| 3 | AUDIT\_MAX\_FILE\_SIZE | INTEGER | 单个审计文件的最大大小，单位 MB |
| 4 | AUD\_SPACE\_LIMIT | INTEGER | 审计文件总存储空间大小限制，单位 MB |
| 5 | AUD\_SPACE\_FREE | INTEGER | 可用审计文件存储空间大小，单位 MB |
| 6 | AUDIT\_IS\_NORMAL | CHAR(1) | 审计是否正常。Y:是；N:否，不再审计 |

3） **V$CIPHERS**

显示系统加密算法和散列算法信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | CYT\_ID | INTEGER | 算法 ID |
| 2 | CYT\_NAME | VARCHAR(256) | 算法名 |
| 3 | CYT\_TYPE | INTEGER | 算法类型。   1：分组加密算法；   2：流加密算法；   3：非对称加密算法，保留；   4：散列算法 |
| 4 | BLOCK\_SIZE | INTEGER | 分组长度，单位 BYTE |
| 5 | KH\_SIZE | INTEGER | 密钥长度或 HASH 长度，单位 BYTE |
| 6 | EXTEND\_SIZE | INTEGER | 算法扩展长度，单位 BYTE |
| 7 | WORK\_MODE | VARCHAR(128) | 算法模式。   ECB：电子密码本模式；   CBC：密码块连接模式；   CFB：密文反馈模式。CFB 后缀的数值代表每次迭代处理的位数，默认 CFB 为 CFB128；   OFB：输出反馈模式；   ECB\_NOPAD：非填充 ECB 模式；   CBC\_NOPAD：非填充 CBC 模式；   DEFAULT：未指定或不存在；   其他（EXTKEY、STORE、TRANS、KID、AUTH、LOG）：特殊版本专用 |

4） **V$EXTERNAL\_CIPHERS**

显示系统中所有的第三方加密算法信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 算法 ID |
| 2 | NAME | VARCHAR(128) | 算法名 |
| 3 | LIB | VARCHAR(300) | 算法所在的 lib 库文件名 |
| 4 | VALID | CHAR(1) | 算法是否有效。‘Y’：是；‘N’：否 |

5） **V$EXTERNAL\_CIPHER\_LIBS**

显示加密引擎的相关信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 加密引擎的名字 |
| 2 | TYPE | INTEGER | 获取加密引擎类型。0：第三方软加密；1：第三方硬件加密；2：UKEY |
| 3 | LIB\_PATH | VARCHAR(256) | 加密引擎所在的 lib 库文件名 |

6） **V$AUDIT\_FILE**

显示系统中的所有审计文件路径。此动态性能视图只有审计用户可以查询。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | FILEPATH | VARCHAR(256) | 审计文件的完整路径 |
| 2 | SGUID | INTEGER | 服务器的唯一标识，仅用于判断审计文件与库是否匹配 |
| 3 | RT\_FLAG | INTEGER | 是否为实时审计 |
| 4 | HPC\_SEQNO | INTEGER | DSC 节点号 |
| 5 | VERSION | INTEGER | 版本号 |
| 6 | DBNAME | VARCHAR(128) | 库名称 |
| 7 | IS\_FULL | INTEGER | 审计文件是否已满。1：已满；0：未满。 |
| 8 | BEGIN\_TIME | DATETIME(6) | 审计文件的创建时间 |
| 9 | LENGTH | BIGINT | 审计文件的长度，单位 BYTE |

7） **V$DBMSAUDIT\_FILE**

显示 DBMS\_AUDIT 系统包中添加的审计文件路径。此动态性能视图只有审计用户可以查询。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | FILEPATH | VARCHAR(256) | 审计文件的完整路径 |
| 2 | SGUID | INTEGER | 服务器的唯一标识，仅用于判断审计文件与库是否匹配 |
| 3 | RT\_FLAG | INTEGER | 是否为实时审计 |
| 4 | HPC\_SEQNO | INTEGER | DSC 节点号 |
| 5 | VERSION | INTEGER | 版本号 |
| 6 | DBNAME | VARCHAR(128) | 库名称 |
| 7 | IS\_FULL | INTEGER | 审计文件是否已满。1：已满；0：未满。 |
| 8 | BEGIN\_TIME | DATETIME(6) | 审计文件的创建时间 |
| 9 | LENGTH | BIGINT | 审计文件的长度，单位 BYTE |
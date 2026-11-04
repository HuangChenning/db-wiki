---
title: "附录 1"
book: "DM8 系统管理员手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dm8-admin-manual-appendix1.html
tags:
  - dameng
  - dm8
  - administrator
---

## 附录 1 数据字典

DM 提供非常多的数据字典，供用户更好的了解系统的详细信息。数据字典表的模式名为 SYS。例如：SYS.SYSOBJECTS。

例 1 查看系统表 SYS.SYSOBJECTS。

```
SELECT count(*) FROM SYS.SYSOBJECTS;

行号    COUNT(*)

---------- --------------------

1     1126
```

同时，DM 为每个数据字典表建立了同名的全局同义词，因此用户也可以直接使用同义词对数据字典表进行访问。例如：数据字典 SYS.SYSOBJECTS 的同义词即为 SYSOBJECTS。

例 2 通过使用同义词 SYSOBJECTS 进行查询，查询的结果和 SYS.SYSOBJECTS 一致。

```
SELECT count(*) FROM SYSOBJECTS;

行号    COUNT(*)

---------- --------------------

1     1126
```

但是，如果启用了 SVI 角色，则同义词会指向本数据字典的 V 视图，而不再是数据字典。

例 3 先启用 SVI 角色，再使用同义词 SYSOBJECTS 进行查询，查询的结果和 SYS.VSYSOBJECTS 一致。

```
SP_INIT_SVI_SYS(1); //创建V视图
SP_SWITCH_SVI(1);//启用SVI角色
SELECT count(*) FROM SYS.VSYSOBJECTS;
行号    COUNT(*)
---------- --------------------
1     722
 
SELECT count(*) FROM SYSOBJECTS;
行号    COUNT(*)
---------- --------------------
1     722
```

下面详细介绍各数据字典的含义：

1. **SYSOBJECTS**

记录系统中所有对象的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 对象名称 |
| 2 | ID | INTEGER | 对象 ID |
| 3 | SCHID | INTEGER | TYPE$=SCHOBJ 或者 TYPE$=TABOBJ 时表示对象所属的模式 ID，否则为 0。 |
| 4 | TYPE$ | VARCHAR(10) | 对象的主类型。 分为三种：   1）库级：   UR 用户，具体类型看 SUBTYPE$、   SCH 模式、GDBLINK 全局 DBLINK、DSYNOM 全局同义词、DIR 目录、PROFILE 对象   2）模式级：   SCHOBJ 模式内对象，具体类型看 SUBTYPE$；DMNOBJ 域对象，具体类型可为 CONS 约束，为创建域时指定约束由系统生成   3）表级：   TABOBJ 表的下级对象，具体类型看 SUBTYPE$ |
| 5 | SUBTYPE$ | VARCHAR(10) | 对象的子类型。分为三种：   1）用户对象：   USER 用户、ROLE 角色   2）模式对象：   UTAB 用户表、STAB 系统表、VIEW 视图、PROC 过程、SEQ 序列、PKG 包、TRIG 触发器、DBLINK 外部链接、SYNOM 同义词、 CLASS 对象类型（类）、TYPE 数据类型、JCLASS JAVA 类、DOMAIN 域、CLLT 集合、CONTEXT 上下文、PGRP 分区组、OPERATOR 运算符   3）表对象：   INDEX 索引、CNTIND 全文索引、CONS 约束 |
| 6 | PID | INTEGER | 对象的父对象 ID，为-1 表示当前行 PID 列无意义 |
| 7 | VERSION | INTEGER | 对象的版本 |
| 8 | CRTDATE | DATETIME(6) | 对象的创建时间 |
| 9 | INFO1 | INTEGER | 表对象：   表数据所在的缓冲区 ID(0xFF000000)，数据页填充因子(0x00F00000)，BRANCH(0x000FF000)，NOBARNCH(0x00000FF0)，BRANCHTYPE(0x0000000F)   用户对象：BYTE(4)用户类型   视图对象：BIT(0) CHECK，BIT(1) CHECK CASCADE，BIT(2)是否加密,BIT(4)SYSTEM   触发器对象：BIT(1)触发器类型，1 为表级触发器，0 为事件触发器。   BIT(2,3)执行类型(前或后)，BIT(4)是否加密, BIT(5)是否系统级，BIT(13)是否启用   对于表级触发器：BIT(6) RSFLAG，BIT(7) NEW REFED FLAG，BIT(8) OLD REFED FLAG，BIT(9) ALL NEW MDF FLAG   对于事件触发器：BIT(6,7) SCOPE, BIT(8,11) SCHEDUAL TYPE   约束对象：列数   存储过程：BIT(0)是否存储过程，BIT(1)是否加密，BIT(2)是否系统级，BIT(5)是否为 AUTHID CURRENT\_USER 类型，BIT(8) 外部函数是否是标准 C   角色：角色类型   序列：BYTE(0)是否循环，BYTE(1)是否排序，BYTE(2)是否有缓存，BYTE(3)是否 MPP 环境下为本地，BIT(1)是否扩展   同义词：是否带系统标识   包：BIT(1)文本是否加密，BIT(2)是否带系统标识，BIT(5)是否为 AUTHID CURRENT\_USER 类型   自定义对象类型：BIT(6)是否为 create type as object 方式创建 |
| 10 | INFO2 | INTEGER | 表/用户/数据库/表空间：BYTE(4)空间限制值，单位为数据页页数   视图：基表 ID |
| 11 | INFO3 | BIGINT | 序列：起始值, 扩展类型序列写入-1   触发器：BYTE(0-3)EVENTS   表级触发器，BYTE(4)更新操作可触发的字段， BYTE(5)行前触发器中可被触发器修改值的新行字段，BYTE(6)元组级触发器中引用的字段   事件触发器，BYTE(4)间隔，BYTE(5)子间隔，BYTE(6,7)分间隔   表：BYTE(0)表类型或临时表类型；BYTE(1)日志类型、错误响应、不可用标识；bit(17)是否临时表会话级；bit(22)是否允许行迁移；bit(34)表是否带高级日志表；BYTE(5)标记分布表；bit(50)表的超长记录是否可以转换为行外数据存储；bit(51)表是否开启记录物理逻辑日志 ；bit(57)表是否为物化视图预建表   用户：BYTE(0-1)默认表空间 ID，BYTE(2-3)用户索引默认表空间 ID   视图：BYTE(0-3)预建表 ID；bit(32)物化视图表列与定义查询列的精度是否一致；bit(33)物化视图完全刷新时使用 TRUNCATE 方式删除老数据；bit(34)物化视图完全刷新时使用 DELETE 方式删除老数据   约束：BIT(0)check 约束中是否包含 is json 表达式；BIT(1)约束是否是检查老数据 |
| 12 | INFO4 | BIGINT | 序列：增量   表：低 4 字节表示表版本，当表字典对象发生变化时，值加 1；高 4 字节表示大字段数据版本，当大字段数据发生变化时，值加 1   子索引：上级子表或主表索引 ID   子表约束：上级子表或主表约束 ID   触发器：触发器执行节点，低 2 字节保存 DMDPC 下指定触发的 RAFT\_ID |
| 13 | INFO5 | VARBINARY(128) | 表：BYTE(10)BLOB 数据段头   序列：BYTE(8)序列最大值，BYTE(8)序列最小值，BYTE(2)文件 ID，BYTE(4)页号，BYTE(2)序列当前位置   用户：BYTE(4)HASH 散列算法 id，BYTE(1)HASH 加盐选项   视图：BIT(0-3)物化视图最近一次刷新使用的刷新方法，BIT(4-7)物化视图的分类，BYTE(1-8)物化视图最近一次刷新开始时间，BYTE(9-16)物化视图最近一次刷新结束时间 |
| 14 | INFO6 | VARBINARY(2048) | 视图：BYTE(4)表或视图 ID   触发器： 表级触发器，BYTE(2)更新操作可触发字段， BYTE(2)元组级触发器前可能被触发器修改值的字段，BYTE(2)元组级触发器中引用的字段， 事件触发器，BYTE(8)开始/ BYTE(8)结束日期、BYTE(5)开始/ BYTE(5)结束时间 约束对象：(BYTE(4)ID)表列链表   同义词：BYTE(2)模式名和 BYTE(2)对象名   表：BYTE(1-8)普通表 IDENTITY 自增列的 SEED 选项；BYTE(9-16)普通表 IDENTITY 自增列的 INCREMENT 选项；BYTE(17-20)WITH/WITHOUT COUNTER 选项；BYTE(21-24)水平分区根表使用的分区组 ID；BYTE(25-26)普通表的自增列类型，0：无自增列，1：IDENTITY，2：AUTO\_INCREMENT；BYTE(27-30)对象表模板对象的 clsid；BYTE(31)对象表是否允许子类型代替父类型；BYTE(32)对象表 oid 生成信息，0：SYSTEM GENERATED，系统默认生成，1：PRIMARY KEY，基于主键生成；BYTE(33-36)水平分区根表的分区表字典版本；BYTE(37-40)水平分区根表的自增列预分配的序列 ID；BYTE(41-42)水平分区根表的自增列类型，0：无自增列，1：IDENTITY，2：AUTO\_INCREMENT；BYTE(43-44)水平分区根表的自增列的列 ID；BYTE(45-48)建表时指定存储的表空间组 ID；BYTE(49-50)表并行度；BYTE(51-54)引用分区表对应的被引用表 ID   序列：仅扩展类型序列使用 BYTE(0-15) FOR MAXVALUE, BYTE(16-31) FOR MINVALUE, BYTE(32-47) FOR STARTVALUE |
| 15 | INFO7 | BIGINT | BYTE(4)自动重写标记，0：不允许重写；1：允许重写 |
| 16 | INFO8 | VARBINARY(1024) | 外部表：记录控制文件路径   上下文 context：记录访问方式（ACCESSED LOCALLY，即只允许当前会话访问，不允许其他会话访问）   物化视图日志表：记录刷新时间   触发器：BYTE(2)触发器类型，BYTE(4)FOLLOWS 或 PRECEDES 指定的触发器数量，BYTE(4)FOLLOWS 或 PRECEDES 指定的触发器 ID |
| 17 | VALID | CHAR(1) | 对象是否有效，’Y’表示有效，’N’表示失效 |

2. **SYSINDEXES**

记录系统中所有索引定义信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 索引 ID |
| 2 | ISUNIQUE | CHAR(1) | 是否为唯一索引 |
| 3 | GROUPID | SMALLINT | 所在表空间的 ID |
| 4 | ROOTFILE | SMALLINT | 存放根的文件号。取值为 0 表示文件号为 0，是正常取值。   也可能取特殊值-1 或-2，特殊值说明如下：   取值-1：不需要创建 B 树。   通常使用场景：   a)临时表，其地址由会话维护，不需要写入元数据   b)分区表普通索引，在多级分区中间层子表上不创建 B 树   c)分区表全局索引，在子表上的虚索引不创建 B 树   d)非 B 树索引   取值-2：因为延迟段分配，暂未实际分配空间 |
| 5 | ROOTPAGE | INTEGER | 存放根的页号。   特殊值说明：   取值-1：不需要创建 B 树。   通常使用场景：   a)临时表，其地址由会话维护，不需要写入元数据   b)分区表普通索引，在多级分区中间层子表上不创建 B 树   c)分区表全局索引，在子表上的虚索引不创建 B 树   d)非 B 树索引   取值-2：因为延迟段分配，暂未实际分配空间 |
| 6 | TYPE$ | CHAR(2) | 类型。BT：B 树，BM：位图，AR：数组，IF：IVFFLAT 向量，HS：HNSW 向量，MP：BMP 向量，DA：DISKANN 向量 |
| 7 | XTYPE | INTEGER | 标识索引类型。按位取值，10 进制取值如下：   0：聚集索引   1：二级索引   2：函数索引   4：全局索引在水平分区子表上   8：全局索引在水平分区主表上   16：唯一索引   32：扁平索引   64：数组索引   2048：该位图索引是由改造后创建   4096：位图索引   8192：位图连接索引   16384：位图连接索引虚索引   65536：索引不可见   131072：DPC 全局索引的根索引   262144：DPC 全局索引的子索引   1048576：向量 IVFFLAT 索引   2097152：向量 HNSW 索引   4194304：向量 BMP 索引   支持使用上述有效值的组合值，如 9 表示同时符合 1 和 8 |
| 8 | FLAG | INTEGER | 索引标记。按位取值，10 进制取值如下：   0：1~32 以外的情况均为 0   1：系统索引   2：虚索引   4：PK   8：在临时表上   32：fast pool   支持使用上述有效值的组合值，如 9 表示同时符合 1 和 8 |
| 9 | KEYNUM | SMALLINT | 索引包含的键值数目 |
| 10 | KEYINFO | VARBINARY(816) | 索引的键值信息 |
| 11 | INIT\_EXTENTS | SMALLINT | 初始簇数目 |
| 12 | BATCH\_ALLOC | SMALLINT | 下次分配簇数目 |
| 13 | MIN\_EXTENTS | SMALLINT | 最小簇数 |

3. **SYSCOLUMNS**

记录系统中所有列定义的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 列名 |
| 2 | ID | INTEGER | 父对象 ID |
| 3 | COLID | SMALLINT | 列 ID |
| 4 | TYPE$ | VARCHAR(128) | 列数据类型 |
| 5 | LENGTH$ | INTEGER | 列定义长度 |
| 6 | SCALE | SMALLINT | 列定义刻度。对于数值数据类型，SCALE 字段值为标度；对于 VARCHAR(< 长度 > CHAR)数据类型，SCALE 字段值为 7；对于 CHAR(< 长度 > CHAR)数据类型，SCALE 字段值为 8；对于时间数据类型，SCALE 字段值为秒精度，其中针对本地时区类型，SCALE 字段两个字节中的高字节表示 LOCAL 掩码，低字节表示秒精度，针对时间间隔数据类型，SCALE 字段两个字节中的高字节表示时间间隔类型，低字节中的高 4 位表示引导精度，低 4 位表示秒精度；对于其他数据类型，SCALE 字段值为 0 |
| 7 | NULLABLE$ | CHAR(1) | 是否允许为空 |
| 8 | DEFVAL | VARCHAR(2048) | 缺省值 |
| 9 | INFO1 | SMALLINT | 列存储表： BIT(0)压缩标记；BIT(1-12)区大小； BIT(13)列存储的区上是否做最大最小值统计；BIT(14)是否加密列   其他表：BIT(0)压缩标记   视图：BYTE(2)多层视图中在直接上级视图中的列 ID，不支持连接视图   存储过程：BYTE(2)参数类型 |
| 10 | INFO2 | SMALLINT | 普通表：BIT(0)是否自增列； BIT(14)是否加密列   视图：BYTE(2)多层视图中在最原始表中的列 ID，不支持连接视图   列存储表：group\_id |

4. **SYSCONS**

记录系统中除 NOT NULL 约束、NOT VISIBLE 约束以及 CLUSTER KEY 约束之外的所有约束信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 约束 ID |
| 2 | TABLEID | INTEGER | 所属表 ID |
| 3 | COLID | SMALLINT | 列 ID。暂时不支持，无意义。全部为-1 |
| 4 | TYPE$ | CHAR(1) | 约束类型。   P：PRIMARY KEY 约束、\[NOT\] CLUSTER PRIMARY KEY 约束   U：UNIQUE 约束、CLUSTER UNIQUE KEY 约束   F：FOREIGN KEY 约束   C：CHECK 约束 |
| 5 | VALID | CHAR(1) | 约束是否有效 |
| 6 | INDEXID | INTEGER | 索引 ID |
| 7 | CHECKINFO | VARCHAR(2048) | check 约束的文本 |
| 8 | FINDEXID | INTEGER | 外键所引用的索引 ID |
| 9 | FACTION | CHAR(2) | 前一字符对应外键的更新动作，后一字符对应外键的删除动作 |
| 10 | TRIGID | INTEGER | 动作触发器 ID |

5. **SYSSTATS**

用于执行收集统计信息操作之后，记录系统中的统计信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 对象 ID |
| 2 | COLID | SMALLINT | 列 ID，表级统计为-1 |
| 3 | T\_FLAG | CHAR(1) | 对象的标记。标记为：T 表、C 列、I 索引 |
| 4 | T\_TOTAL | BIGINT | 总行数 |
| 5 | N\_SAMPLE | BIGINT | 采样个数 |
| 6 | N\_DISTINCT | BIGINT | 不同值的个数 |
| 7 | N\_NULL | BIGINT | 空值个数 |
| 8 | V\_MIN | VARBINARY(255) | 列的采样数据中的最小值 |
| 9 | V\_MAX | VARBINARY(255) | 列的采样数据中的最大值 |
| 10 | BLEVEL | TINYINT | B 树层次 |
| 11 | N\_LEAF\_PAGES | BIGINT | 叶子段总页数 |
| 12 | N\_LEAF\_USED\_PAGES | BIGINT | 叶子占用的页数 |
| 13 | CLUSTER\_FACTOR | INTEGER | 索引的 cluster\_factor |
| 14 | N\_BUCKETS | SMALLINT | 直方图桶数目 |
| 15 | DATA | BLOB | 直方图数据 |
| 16 | COL\_AVG\_LEN | INTEGER | 平均行长 |
| 17 | LAST\_GATHERED | DATETIME(6) | 最后收集时间 |
| 18 | INFO1 | VARBINARY(255) | 预留列 |
| 19 | INFO2 | VARBINARY(255) | 预留列 |

注：COL\_AVG\_LEN 和 LAST\_GATHERED 两个字段在 V7.1.5.173 版本和之后的版本都能看到。如果使用了该版本及以后的版本服务器后，需要再退回到之前版本的服务器，那么需要在新版本上执行 SP\_UPDATE\_SYSSTATS(0)并正常退出之后，才能使用老版本的服务器。另外，SP\_UPDATE\_SYSSTATS (99)可以在 SYSSTATS 表上增加这两个列，对老库进行升级。SP\_UPDATE\_SYSSTATS 详细使用方法请参考《DM8\_SQL 使用手册》。

6. **SYSDUAL**

为不带表名的查询而设，用户一般不需查看。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 始终为 1 |

7. **SYSTEXTS**

存放字典对象的文本信息。使用时，系统内部临时解析的字典对象才会放入此处。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 所属对象的 ID。对象为：VIEW 视图、 PROC 过程、SEQ 序列、PKG 包、TRIG 触发器、SYNOM 同义词、 CLASS 对象类型（类）、TYPE 数据类型、JCLASS JAVA 类、DOMAIN 域、CLLT 集合、CONTEXT 上下文、USER 用户 |
| 2 | SEQNO | INTEGER | 视图：0 表示视图定义，1 表示视图的查询子句;   包：0 表示包规范，1 表示包体；   用户：0 表示 ALLOW\_ADDR，1 表示 NOT\_ALLOW\_ADDR；   其它：均为 0 |
| 3 | TXT | CLOB | 文本信息 |

8. **SYSGRANTS**

记录系统中权限信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | URID | INTEGER | 被授权用户/角色 ID |
| 2 | OBJID | INTEGER | 授权对象 ID，对于数据库权限为-1 |
| 3 | COLID | INTEGER | 表/视图列 ID，非列权限为-1 |
| 4 | PRIVID | INTEGER | 权限 ID。如果是角色授权为-1 |
| 5 | GRANTOR | INTEGER | 授权者 ID。如果是角色授权为-1 |
| 6 | GRANTABLE | CHAR(1) | 权限是否可转授，Y 可转授，N 不可转授 |

9. **SYSAUDIT**

记录系统中的审计设置。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | LEVEL | SMALLINT | 审计级别 |
| 2 | UID | INTEGER | 用户 ID |
| 3 | TVPID | INTEGER | 表/视图/触发器/存储过程函数 ID |
| 4 | COLID | SMALLINT | 列 ID |
| 5 | TYPE | SMALLINT | 审计类型 |
| 6 | WHENEVER | SMALLINT | 审计情况 |

10. **SYSAUDITRULES**

记录系统中审计规则的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 规则 ID |
| 2 | RULENAME | VARCHAR(128) | 规则名 |
| 3 | USERID | INTEGER | 用户 ID |
| 4 | SCHID | INTEGER | 模式 ID |
| 5 | OBJID | INTEGER | 操作对象 ID |
| 6 | COLID | SMALLINT | 列 ID |
| 7 | OPTYPE | SMALLINT | 操作类型 |
| 8 | WHENEVER$ | SMALLINT | 审计情况 |
| 9 | ALLOW\_IP | VARCHAR(1024) | 允许的 IP |
| 10 | ALLOW\_DT | VARCHAR(1024) | 时间段 |
| 11 | INTERVAL$ | INTEGER | 时间间隔 |
| 12 | TIMES | INTEGER | 操作次数 |

11. **SYSAUDITSQLSEQ**

记录系统中审计语句序列的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 语句序列审计规则名 |
| 2 | SQLSEQ | INTEGER | 语句序列中的 SQL 语句序号 |
| 3 | SQLSTR | VARCHAR(8188) | 语句序列中的 SQL 语句 |

12. **SYSHPARTTABLEINFO**

记录系统中分区表的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | BASE\_TABLE\_ID | INTEGER | 基表 ID |
| 2 | PART\_TABLE\_ID | INTEGER | 分区表 ID |
| 3 | PARTITION\_TYPE | VARCHAR(10) | 分区类型 |
| 4 | PARTITION\_NAME | VARCHAR(128) | 分区名 |
| 5 | HIGH\_VALUE | VARBINARY(8188) | LIST 分区的临界值；   范围分区的分区值；   哈希分区此值为 NULL |
| 6 | INCLUDE\_HIGH\_VALUE | CHAR(1) | 对 LIST 分区表示分区是否包含临界值；   对范围分区始终为 1；对哈希分区此值为 0 |
| 7 | RESVD1 | INTEGER | 对子表记录：同层的第一个(最左边)子表 id   对模板记录：该模板中的子分区个数 |
| 8 | RESVD2 | INTEGER | 保留 |
| 9 | RESVD3 | INTEGER | 保留 |
| 10 | RESVD4 | VARCHAR(128) | 保留 |
| 11 | RESVD5 | VARCHAR(2000) | 保留 |

13. **SYSDISTABLEINFO**

记录 MPP 下范围分布表和 LIST 分布表的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TABLE\_ID | INTEGER | 表 ID |
| 2 | SEQNO | INTEGER | 分布列序号 |
| 3 | DIS\_TYPE | VARCHAR(10) | 分布类型，取值：LIST、RANGE |
| 4 | HIGH\_VALUE | VARBINARY(8188) | LIST 分布的分布值；   范围分布的临界值 |
| 5 | INCLUDE\_HIGH\_VALUE | CHAR(1) | 对范围分布表示分布是否包含临界值；   对 LIST 分布始终为 1 |

14. **SYSMACPLYS**

记录策略定义。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 策略 ID |
| 2 | NAME | VARCHAR(128) | 策略名 |

15. **SYSMACLVLS**

记录策略的等级。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PID | INTEGER | 策略 ID |
| 2 | ID | SMALLINT | 等级 ID |
| 3 | NAME | VARCHAR(128) | 等级名 |

16. **SYSMACCOMPS**

记录策略的范围。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PID | INTEGER | 策略 ID |
| 2 | ID | SMALLINT | 范围 ID |
| 3 | NAME | VARCHAR(128) | 范围名 |

17. **SYSMACGRPS**

记录策略所在组的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PID | INTEGER | 策略 ID |
| 2 | ID | SMALLINT | 组 ID |
| 3 | PARENTID | SMALLINT | 父节点 ID |
| 4 | NAME | VARCHAR(128) | 组名 |

18. **SYSMACLABELS**

记录策略的标记信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PID | INTEGER | 策略 ID |
| 2 | ID | INTEGER | 标记 ID |
| 3 | LABEL | VARCHAR(4000) | 标记信息 |

19. **SYSMACTABPLY**

记录表策略信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TID | INTEGER | 表 ID |
| 2 | PID | INTEGER | 策略 ID |
| 3 | COLID | SMALLINT | 列 ID |
| 4 | OPTIONS | TINYINT | 可见性 |

20. **SYSMACUSRPLY**

记录用户的策略信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | UID | INTEGER | 用户 ID |
| 2 | PID | INTEGER | 策略 ID |
| 3 | MAXREAD | INTEGER | 最大读标记 ID |
| 4 | MINWRITE | INTEGER | 最小写标记 ID |
| 5 | DEFTAG | INTEGER | 默认标记 ID |
| 6 | ROWTAG | INTEGER | 行级标记 ID |
| 7 | PRIVS | TINYINT | 特权 |

21. **SYSMACOBJ**

记录扩展客体标记信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | OBJID | INTEGER | 对象 ID |
| 2 | COLID | SMALLINT | 列 ID |
| 3 | PID | INTEGER | 策略 ID |
| 4 | TAG | INTEGER | 标记 ID |

22. **SYSCOLCYT**

记录列的加密信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TID | INTEGER | 表 ID |
| 2 | CID | SMALLINT | 列 ID |
| 3 | ENC\_ID | INTEGER | 加密类型 ID |
| 4 | ENC\_TYPE | CHAR(1) | 加密类型 |
| 5 | HASH\_ID | INTEGER | 哈希算法 ID |
| 6 | HASH\_TYPE | CHAR(1) | 是否加盐 |
| 7 | CIPHER | VARCHAR(1024) | 密钥 |

23. **SYSACCHISTORIES**

记录登录失败的历史信息。用户登录成功后，会清理当前用户上次成功登录前的登录失败记录，仅保留其他用户的登录失败信息以便查看。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | LOGINID | INTEGER | 登录 ID |
| 2 | LOGINNAME | VARCHAR(128) | 登录名 |
| 3 | TYPE$ | INTEGER | 登录用户类型。0：普通用户；1：AUIDT 审计员；2：SSO 安全员；3：DBO 操作员 |
| 4 | ACCPIP | VARCHAR(128) | 访问 IP |
| 5 | ACCDT | DATETIME(6) | 访问时间 |

24. **SYSPWDCHGS**

记录密码的修改信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | LOGINID | INTEGER | 登录 ID |
| 2 | OLD\_PWD | VARCHAR(512) | 旧密码 |
| 3 | NEW\_PWD | VARCHAR(512) | 新密码 |
| 4 | MODIFIED\_TIME | DATETIME(6) | 修改日期 |

25. **SYSCONTEXTINDEXES**

记录全文索引的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 索引名 |
| 2 | ID | INTEGER | 索引号 |
| 3 | TABLEID | INTEGER | 基表号 |
| 4 | COLID | SMALLINT | 列号 |
| 5 | UPD\_TIMESTAMP | DATETIME(6) | 索引相关 DDL 的更新时间。例如：CREATE、ALTER 全文索引之后该时间均会发生变化 |
| 6 | TIID | INTEGER | CTI$INDEX\_NAME$I 表 ID |
| 7 | TDID | INTEGER | CTI$INDEX\_NAME$D 表 ID |
| 8 | TPID | INTEGER | CTI$INDEX\_NAME$P 表 ID |
| 9 | TNID | INTEGER | CTI$INDEX\_NAME$N 表 ID |
| 10 | TRID | INTEGER | CTI$INDEX\_NAME$R 表 ID |
| 11 | WSEG\_TYPE | SMALLINT | 分词参数类型。0：中文分词，生成尽量少的分词词条；1：中文分词，生成尽量多的分词词条；2：英文分词；3：中文分词，以双字为单位机械式分词，分词结果可能存在无意义的分词 |
| 12 | RESVD | VARBINARY(100) | 保留字段 |

26. **SYSTABLECOMMENTS**

记录表或视图的注释信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SCHNAME | VARCHAR(128) | 模式名 |
| 2 | TVNAME | VARCHAR(128) | 表/视图名 |
| 3 | TABLE\_TYPE | VARCHAR(10) | 对象类型 |
| 4 | COMMENT$ | VARCHAR(40000) | 注释信息 |

27. **SYSCOLUMNCOMMENTS**

记录列的注释信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SCHNAME | VARCHAR(128) | 模式名 |
| 2 | TVNAME | VARCHAR(128) | 表/视图名 |
| 3 | TABLE\_TYPE | VARCHAR(10) | 对象类型 |
| 4 | COMMENT$ | VARCHAR(4000) | 注释信息 |

28. **SYSUSERS**

记录系统中用户信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 用户 ID |
| 2 | PASSWORD | VARCHAR(512) | 用户口令 |
| 3 | AUTHENT\_TYPE | INTEGER | 用户身份验证模式：   1：数据库身份验证；   2：基于操作系统的身份验证、LDAP 身份验证、KERBEROS 身份验证；   4：RADIUS 身份验证；   0：其他情况 |
| 4 | SESS\_PER\_USER | INTEGER | 高位 2 字节表示在所有 DSC 实例中，一个用户可以同时拥有的会话数量，低位 2 字节表示在一个实例中，一个用户可以同时拥有的会话数量 |
| 5 | CONN\_IDLE\_TIME | INTEGER | 用户会话的最大空闲时间，单位由 dm.ini 中安全参数 RESOURCE\_FLAG 决定，取值 1 表示秒，0 表示分钟。 |
| 6 | FAILED\_NUM | INTEGER | 用户登录失败次数限制 |
| 7 | LIFE\_TIME | INTEGER | 口令有效期。单位：天 |
| 8 | REUSE\_TIME | INTEGER | 重用同一个口令的时间间隔。单位：天 |
| 9 | REUSE\_MAX | INTEGER | 重用同一个口令之前，需要修改口令的次数 |
| 10 | LOCK\_TIME | INTEGER | 用户口令锁定时间，单位：分钟 |
| 11 | GRACE\_TIME | INTEGER | 过期口令宽限期。单位：天 |
| 12 | LOCKED\_STATUS | SMALLINT | 用户登录是否锁定：   1：手动锁定   2：未锁定   3：自动锁定（登录失败次数超过上限）   4：自动锁定 (超过指定天数未登录) |
| 13 | LASTEST\_LOCKED | DATETIME(0) | 用户最后一次的锁定时间 |
| 14 | PWD\_POLICY | INTEGER | 用户口令策略。取值意义请参考 INI 参数 PWD\_POLICY |
| 15 | RN\_FLAG | INTEGER | 是否只读，1：只读；0：非只读 |
| 16 | ALLOW\_ADDR | VARCHAR(500) | 允许的 IP 地址，长度超过 500 转入 SYSTEXTS 系统表存储 |
| 17 | NOT\_ALLOW\_ADDR | VARCHAR(500) | 不允许的 IP 地址，长度超 500 转入 SYSTEXTS 系统表存储 |
| 18 | ALLOW\_DT | VARCHAR(500) | 允许登录的时间段 |
| 19 | NOT\_ALLOW\_DT | VARCHAR(500) | 不允许登录的时间段 |
| 20 | LAST\_LOGIN\_DTID | VARCHAR(128) | 上次登录时间（首次设置非活跃时间时或解锁非活跃用户锁时，LAST\_LOGIN\_DTID 更新为本次操作时间） |
| 21 | LAST\_LOGIN\_IP | VARCHAR(128) | 上次登录 IP 地址 |
| 22 | FAILED\_ATTEMPS | INTEGER | 用户自上一次成功登录以来的失败登录次数 |
| 23 | ENCRYPT\_KEY | VARCHAR(256) | 用户登录的存储加密密钥 |
| 24 | OLD\_PASSWORD | VARCHAR(512) | 用户辅助口令 |

29. **SYSOBJINFOS**

记录对象的依赖信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 被依赖类的 ID |
| 2 | TYPE$ | VARCHAR(100) | 对象依赖类型 |
| 3 | INT\_VALUE | INTEGER | 对象类型对应的值 |
| 4 | STR\_VALUE | VARCHAR(2048) | 如果是域对象，表示 DOMAIN+ 域 ID。其他对象暂未利用 |
| 5 | BIN\_VALUE | VARBINARY(2048) | 暂未利用 |

30. **SYSRESOURCES**

记录用户使用系统资源的限制信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 用户 ID |
| 2 | CPU\_PER\_CALL | INTEGER | 用户的一个请求能够使用的 CPU 时间上限，单位秒 |
| 3 | CPU\_PER\_SESSION | INTEGER | 一个会话允许使用的 CPU 时间上限，单位秒 |
| 4 | MEM\_SPACE | INTEGER | 会话占有的私有内存空间上限，单位 MB |
| 5 | READ\_PER\_CALL | INTEGER | 每个请求能够读取的数据页数 |
| 6 | READ\_PER\_SESSION | INTEGER | 一个会话能够读取的总数据页数上限 |
| 7 | INFO1 | VARCHAR(256) | 取值格式为:CONNCET\_TIME. INACTIVE\_ACCOUNT\_TIME   CONNCET\_TIME 表示：一个会话连接、访问和操作数据库服务器的时间上限，单位：10 分钟；   INACTIVE\_ACCOUNT\_TIME 表示：设定的用户的非活跃时间，单位：天 |

31. **SYSCOLINFOS**

记录列的附加信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 表 ID |
| 2 | COLID | SMALLINT | 列 ID |
| 3 | INFO1 | INTEGER | 共计 7 位，从右侧起按位取值，含义如下：   bit(0)：是否是虚拟列   bit(1)：是否是定长 DEC   bit(2)：NUMBER\_MODE=1 时标记是否为 FLOAT   bit(3)：是否兼容 ORACLE 的 DATE 类型格式   bit(4)：设置列缺省值时是否指定了 ON NULL 选项   bit(5)：列上是否隐式添加了 NOT NULL 约束   bit(6): 该列是否设置了 ON UPDATE 自动更新 |
| 4 | INFO2 | INTEGER | 第一字节：NUMBER\_MODE=1 时记录 FLOAT 类型列的精度 |
| 5 | INFO3 | INTEGER | 备用 |

32. **SYSUSERINI**

记录定制的 INI 参数。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | USER\_NAME | VARCHAR(128) | 用户名 |
| 2 | USER\_ID | INTEGER | 用户 ID |
| 3 | PARA\_NAME | VARCHAR(256) | INI 参数名 |
| 4 | INT\_VALUE | BIGINT | 整型参数的值 |
| 5 | DOUBLE\_VALUE | DOUBLE | 浮点类型参数值 |
| 6 | STRING\_VALUE | VARCHAR(4000) | 字符类型参数的值。 |

33. **SYSDEPENDENCIES**

记录对象间的依赖关系。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 对象 ID |
| 2 | TYPE$ | VARCHAR(17) | 对象类型，包括：TABLE，VIEW,MATERIALIZED VIEW,INDEX,   PROCEDURE,FUNCTION,TRIGGER,SEQUENCE,CLASS,CLASS\_BODY,   JCLASS,TYPE,PACKAGE,PACKAGE\_BODY,SYNONYM,DOMAIN |
| 3 | REFED\_ID | INTEGER | 被引用对象 ID |
| 4 | REFED\_TYPE$ | VARCHAR(17) | 被引用对象类型，包括类型同 TYPE$，其中不包含 CLASS\_BODY 与 PACKAGE\_BODY |
| 5 | DEPEND\_TYPE | VARCHAR(4) | 默认为"HARD",当 TYPE$为 MATERIALIZED VIEW 和 INDEX 时，其值为"REF" |

34. **SYSINJECTHINT**

记录为 SQL 语句注入的 HINT 规则。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 规则名称 |
| 2 | DESCRIPTION | VARCHAR(256) | 规则的详细描述 |
| 3 | VALIDATE | VARCHAR(5) | 规则是否生效，取值 TRUE/FALSE |
| 4 | SQL\_TEXT | TEXT | 规则中的 SQL 语句 |
| 5 | HINT\_TEXT | TEXT | 为 SQL 语句注入的 HINT 规则内容 |
| 6 | CREATOR | VARCHAR(128) | 规则创建人 |
| 7 | CRTDATE | DATETIME(6) | 规则创建时间 |
| 8 | INFO1 | INTEGER | SQL 的匹配规则为精准匹配或模糊匹配。0：精确匹配；1：模糊匹配；2 通过 sql\_text\_id 精准匹配 |
| 9 | INFO2 | VARBINARY(128) | HINT 规则的生效类别。可使用 BINTOCHAR 函数将该字段转换为 VARCHAR 类型显示 |
| 10 | INFO3 | VARBINARY(1024) | 保留字段 |

35. **SYSMSTATS**

记录多维统计信息的内容。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | ID 号 |
| 2 | MCOLID | VARBINARY(4096) | 多维的维度信息 |
| 3 | T\_FLAG | CHAR(1) | 保留字段，目前一定是列 ’C’ |
| 4 | N\_DIMENSION | INTEGER | 维度 |
| 5 | N\_TOTAL | BIGINT | 总的行数 |
| 6 | N\_SAMPLE | BIGINT | 采样数 |
| 7 | N\_DISTINCT | BIGINT | 不同值的个数 |
| 8 | N\_NULL | BIGINT | NULL 值的个数 |
| 9 | BLEVEL | TINYINT | 保留字段 |
| 10 | N\_LEAF\_PAGES | BIGINT | 保留字段 |
| 11 | N\_LEAF\_USED\_PAGES | BIGINT | 保留字段 |
| 12 | CLUSTER\_FACTOR | INTEGER | 保留字段 |
| 13 | N\_BUCKETS | SMALLINT | 桶数 |
| 14 | DATA | BLOB | 直方图的信息 |
| 15 | COL\_AVG\_LEN | INTEGER | 保留字段 |
| 16 | LAST\_GATHERED | DATETIME(6) | 最后收集的时间 |

36. **SYSSTATPREFS**

记录指定模式下表的统计信息的静态参数对应的值。

当 INI 参数 AUTO\_STAT\_OBJ 为 1 或 2 时，执行统计信息收集操作之后可以查看到 SYSSTATTABLEIDU 表中数据的变化。当用户通过 DBMS\_STATS.SET\_TABLE\_PREFS 系统包方法设置表 STALE\_PERCENT 属性时，SYSSTATTABLEIDU 表中数据也可能发生变化，具体说明请参见《DM8 系统包使用手册》。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | ID 号 |
| 2 | PNAME | VARCHAR(256) | 参数名 |
| 3 | VALUENUM | DOUBLE | 参数值 |
| 4 | VALUECHAR | VARCHAR(256) | 参数值 |
| 5 | CHGTIME | DATETIME(6) | 修改时间 |
| 6 | RSVD1 | VARBINARY(2000) | 保留信息 |

37. **SYSSTATTABLEIDU**

只有 INI 参数 AUTO\_STAT\_OBJ 为 1 或 2，并执行统计信息收集操作之后才能查看到 SYSSTATTABLEIDU 表中数据的变化。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | ID 号 |
| 2 | TOTAL\_ROWS | BIGINT | 表中数据的总行数。只有发生统计的时候，TOTAL\_ROWS 才会更新 |
| 3 | INSERT\_ROWS | BIGINT | 插入行数。只有系统重启后，才会更新 |
| 4 | DELETE\_ROWS | BIGINT | 删除行数。只有系统重启后，才会更新 |
| 5 | UPDATE\_ROWS | BIGINT | 更新行数。只有系统重启后，才会更新 |
| 6 | LAST\_STAT\_DT | DATETIME(6) | 上一次更新时间 |
| 7 | MONITOR\_FLAG | INTEGER | 监控级别。1：监控级别为所有表；2：监控级别为由 SET\_TABLE\_PREFS 的指定过的表 |
| 8 | RSVD1 | VARBINARY(2000) | 保留信息 |
| 9 | TRUNCATED | INTEGER | 所在表是否有过 TRUNCATE 操作 |

38. **SYSMODIFICATIONS**

监控功能专用。记录所有用户表对象的数据变化情况。其中，是否受统计信息影响表示是否在每次收集统计信息时将之前的监控数据清零。

仅当 INI 参数 MONITOR\_MODIFICATIONS 开启时 SYSMODIFICATIONS 表才会收集数据，根据 INI 参数 MON\_CHECK\_INTERVAL 设置的时间间隔进行收集，也可使用过程 SP\_FLUSH\_MODIFICATIONS\_INFO()手动进行收集。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 表对象 ID |
| 2 | ROOT\_ID | INTEGER | 根表 ID，仅对分区表子表有效，默认值为-1，表示无根表 |
| 3 | BASE\_ID | INTEGER | 父表 ID，仅对分区表子表有效，默认值为-1，表示无父表 |
| 4 | INSERTS | BIGINT | 插入行数，不受统计信息影响 |
| 5 | DELETES | BIGINT | 删除行数，不受统计信息影响 |
| 6 | UPDATES | BIGINT | 更新行数，不受统计信息影响 |
| 7 | TRUNCATED | INTEGER | 是否执行过 TRUNCATE 操作，不受统计信息影响 |
| 8 | PART\_INSERTS | BIGINT | 插入行数，受统计信息影响 |
| 9 | PART\_DELETES | BIGINT | 删除行数，受统计信息影响 |
| 10 | PART\_UPDATES | BIGINT | 更新行数，受统计信息影响 |
| 11 | PART\_TRUNCATED | INTEGER | 是否执行过 TRUNCATE 操作，受统计信息影响 |
| 12 | LAST\_MOD\_TIME | DATETIME(6) | 上次修改的时间 |
| 13 | DROP\_SUB\_TABLES | INTEGER | 删除的分区子表的个数 |
| 14 | MONITOR\_FLAG | INTEGER | 是否为被指定监控的对象 |
| 15 | CHANGED\_AFTER\_STAT | INTEGER | 上次收集统计信息后，数据是否发生过变化 |
| 16 | RSVD1 | VARBINARY(2000) | 保留信息 |

39. **SYSFCOLDEFAULT**

记录表添加列时追加列的默认值。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TABID | INTEGER | 表 ID |
| 2 | COLID | SMALLINT | 列 ID |
| 3 | DEFDATA | VARBINARY(4096) | 追加列默认值，默认值数据最长不允许超过 4000 字节 |

40. **SYS.PROXY\_INFO$**

记录所有代理用户 ID 的信息。只有角色 DBA、DB\_AUDIT\_ADMIN 、DB\_POLICY\_ADMIN 以及 DB\_OBJECT\_ADMIN 才能访问该系统表。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | CLIENT# | INTEGER | 目标登录用户 ID |
| 2 | PROXY# | INTEGER | 代理用户 ID |
| 3 | CREDENTIAL\_TYPE# | TINYINT | 认证方式，只支持 0（不认证） |
| 4 | FLAGS | TINYINT | 代理范围标记，只支持 1（全部角色） |

41. **SYSTUNINGTASK**

记录 SQL 语句调优任务相关信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TASK\_ID | INTEGER | 调优任务 ID |
| 2 | USER\_ID | INTEGER | 任务所属用户 ID |
| 3 | TASK\_NAME | VARCHAR(128) | 任务名称 |
| 4 | SQL\_TEXT | TEXT | 待调优 SQL 语句 |
| 5 | BIND\_LIST | VARCHAR(256) | 绑定参数 |
| 6 | DESCRIPTION | VARCHAR(256) | 任务描述 |
| 7 | CREATE\_TIME | DATETIME(6) | 任务创建时间 |
| 8 | SCOPE | INTEGER | 调优范围，取值： 1：LIMITED； 2：COMPREHENSIVE |
| 9 | TIME\_LIMIT | INTEGER | 任务执行的最大时间，单位秒 |
| 10 | RESVD1 | INTEGER | 保留字段 1 |
| 11 | RESVD2 | VARBINARY(128) | 保留字段 2 |
| 12 | RESVD3 | VARBINARY(512) | 保留字段 3 |

42. **SYSTUNINGEXECUTION**

记录 SQL 语句调优任务每次执行的相关信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | EXEC\_ID | INTEGER | 调优任务执行 ID |
| 2 | TASK\_ID | INTEGER | 任务 ID |
| 3 | EXEC\_NAME | VARCHAR(128) | 执行名称 |
| 4 | DESCRIPTION | VARCHAR(256) | 执行描述 |
| 5 | START\_TIME | DATETIME(6) | 执行开始时间 |
| 6 | END\_TIME | DATETIME(6) | 执行结束时间 |
| 7 | STATUS | INTEGER | 执行状态，取值： 1：INITIAL； 2：EXECUTING； 3：COMPLETED； 4：INTERRUPTED； 5：CANCELLED； 6：FATAL ERROR |
| 8 | RESVD1 | INTEGER | 保留字段 1 |
| 9 | RESVD2 | VARBINARY(128) | 保留字段 2 |
| 10 | RESVD3 | VARBINARY(512) | 保留字段 3 |

43. **SYSTUNINGREPORT**

记录 SQL 语句调优任务的调优报告相关信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | EXEC\_ID | INTEGER | 调优任务执行 ID |
| 2 | SECTION | INTEGER | 显示章节，取值： 1：SUMMARY； 2：FINDING； 3：PLAN； 4：INFORMATION； 5：ERROR； 6：ALL |
| 3 | FINDING\_NO | INTEGER | 统计信息或索引信息。仅当 SECTION=2 时有效 |
| 4 | OBJ\_NO | INTEGER | 涉及多个对象时的对象编号 |
| 5 | BASIC\_MSG | TEXT | 调优报告等级为 BASIC 时的报告内容 |
| 6 | TYPICAL\_MSG | TEXT | 调优报告等级为 TYPICAL 时的报告内容 |
| 7 | ALL\_MSG | TEXT | 调优报告等级为 ALL 时的报告内容 |
| 8 | RESVD1 | INTEGER | 保留字段 1 |
| 9 | RESVD2 | VARBINARY(128) | 保留字段 2 |
| 10 | RESVD3 | VARBINARY(512) | 保留字段 3 |

44. **SYSPROFILES**

记录 PROFILE 配置的资源和密码限制项。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | PROFILE ID |
| 2 | CPU\_PER\_CALL | INTEGER | 用户的一个请求能够使用的 CPU 时间上限，单位秒 |
| 3 | CPU\_PER\_SESSION | INTEGER | 一个会话允许使用的 CPU 时间上限，单位秒 |
| 4 | MEM\_SPACE | INTEGER | 会话占有的私有内存空间上限，单位 MB |
| 5 | READ\_PER\_CALL | INTEGER | 每个请求能够读取的数据页数 |
| 6 | READ\_PER\_SESSION | INTEGER | 一个会话能够读取的总数据页数上限 |
| 7 | CONNECT\_TIME | INTEGER | 一个会话连接、访问和操作数据库服务器的时间上限，单位：10 分钟 |
| 8 | SESS\_PER\_USER | INTEGER | 高位 2 字节表示在所有 DSC 实例中，一个用户可以同时拥有的会话数量，低位 2 字节表示在一个实例中，一个用户可以同时拥有的会话数量 |
| 9 | CONN\_IDLE\_TIME | INTEGER | 用户会话的最大空闲时间，单位由 dm.ini 中安全参数 RESOURCE\_FLAG 决定，取值 1 表示秒，0 表示分钟 |
| 10 | FAILED\_NUM | INTEGER | 用户登录失败次数限制 |
| 11 | LIFE\_TIME | INTEGER | 口令有效期。单位：天 |
| 12 | REUSE\_TIME | INTEGER | 重用同一个口令的时间间隔。单位：天 |
| 13 | REUSE\_MAX | INTEGER | 重用同一个口令之前，需要修改口令的次数 |
| 14 | LOCK\_TIME | INTEGER | 用户口令锁定时间，单位：分钟 |
| 15 | GRACE\_TIME | INTEGER | 过期口令宽限期。单位：天 |
| 16 | INFO1 | VARCHAR(256) | INACTIVE\_ACCOUNT\_TIME：设定的用户非活跃时间，单位：天 |

45. **SYSUSERPROFILES**

记录用户关联的 PROFILE。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | UID | INTEGER | 用户 ID |
| 2 | PID | INTEGER | PROFILE ID |

46. **SYSPKGPROCINFOS**

记录包中的方法信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 方法名 |
| 2 | PKGID | INTEGER | 包 ID |
| 3 | MTDID | INTEGER | 方法 ID，每个包中方法从 0 开始编号（每个包额外存在一条 MTDID 字段值为 NULL 的记录） |
| 4 | OVERLOAD | INTEGER | 方法在包中第几个重载 |
| 5 | AGGREGATE | VARCHAR(10) | 是否是聚合函数，兼容保留字段 |
| 6 | PIPELINED | VARCHAR(10) | 是否是管道化表函数，取值 YES/NO |
| 7 | IMPLTYPEOWNER | VARCHAR(128) | 实现类所属的模式名，兼容保留字段 |
| 8 | IMPLTYPENAME | VARCHAR(128) | 实现类名，兼容保留字段 |
| 9 | PARALLEL | VARCHAR(10) | 是否可以并行，取值 YES/NO |
| 10 | INTERFACE | VARCHAR(10) | 是否是使用 DCI 接口实现的表函数，兼容保留字段 |
| 11 | DETERMINISTIC | VARCHAR(10) | 是否是确定性函数，取值 YES/NO |
| 12 | IS\_PROC | CHAR(1) | 是否是过程，’Y’表示是过程，’N’表示是函数 |
| 13 | INFO1 | VARBINARY(1024) | 表示方法是否支持批量 |

47. **SYSPKGPROCPARAMS**

记录包中方法的参数信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 参数名 |
| 2 | PKGID | INTEGER | 包 ID |
| 3 | MTDID | INTEGER | 方法 ID，每个包中方法从 0 开始编号 |
| 4 | PARAMID | SMALLINT | 参数 ID，每个方法的参数从 1 开始编号，0 表示返回值 |
| 5 | TYPE$ | VARCHAR(128) | 参数类型 |
| 6 | LENGTH$ | INTEGER | 参数长度 |
| 7 | SCALE | SMALLINT | 参数精度 |
| 8 | NULLABLE | CHAR(1) | 参数是否可为空，取值 Y/N |
| 9 | IOFLAG | CHAR(2) | 参数输入输出标记，’I’表示输入，’O’表示输出，’IO’表示输入输出，’R’表示返回值 |
| 10 | DEFVAL | VARCHAR(2000) | 参数缺省值 |
| 11 | COMB\_INFO | VARBINARY(1024) | 参数的复合类型信息 |
| 12 | INFO1 | VARBINARY(1024) | 保留字段 |

48. **SYSCONTEXTLIBS**

记录全文索引所需要的词库信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | LIB\_ID | INTEGER | 词库 ID |
| 2 | LIB\_NAME | VARCHAR(32) | 词库名 |
| 3 | LIB\_PATH | VARCHAR(256) | 词库路径 |
| 4 | DEF\_LIB | CHAR(1) | 是否为默认词库。Y 是，N 否 |
| 5 | RESV1 | VARCHAR(10） | 保留字段 |
| 6 | RESV2 | INTEGER | 保留字段 |
| 7 | RESV3 | INTEGER | 保留字段 |
| 8 | RESV4 | INTEGER | 保留字段 |

49. **SYSTSGROUPS**

记录表空间组相关信息。仅在 DMDPC 环境下有效。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 表空间组名 |
| 2 | ID | INTEGER | 表空间组 ID |
| 3 | DESCRIPTION | VARCHAR(256) | 描述信息 |
| 4 | TS\_NUM | INTEGER | 表空间组包含的表空间个数，每个表空间组最多包含 1536 个表空间 |
| 5 | TS\_INFO | VARBINARY(8192) | 表空间组包含的表空间 ID 信息 |
| 6 | INFO1 | INTEGER | 保留字段 |
| 7 | INFO2 | BIGINT | 保留字段 |
| 8 | INFO3 | VARBINARY(1024) | 保留字段 |

50. **SYSPLNINFO**

记录系统中绑定执行计划持久化的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PLN\_ID | BIGINT | 绑定执行计划 ID |
| 2 | HASH\_VALUE | INTEGER | 执行计划哈希值 |
| 3 | SCHID | INTEGER | 模式 ID |
| 4 | STMT\_TYPE | INTEGER | SQL 语句类型 |
| 5 | SQLSTR | VARCHAR(1000) | 执行计划 SQL 语句 |
| 6 | PLN\_INFO | BLOB | 执行计划信息 |
| 7 | FMT\_VERSION | INTEGER | 格式版本号 |
| 8 | CMD\_VERSION | BIGINT | 指令版本号 |
| 9 | DISABLED | CHAR(1) | 是否禁用 |

51. **SYSPLNOBJID**

记录系统中绑定执行计划对应字典对象的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PLN\_ID | BIGINT | 绑定执行计划 ID |
| 2 | OBJID | INTEGER | 字典对象 ID |

52. **SYSOPARGS**

记录自定义运算符的重载信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 重载对象 ID |
| 2 | PID | INTEGER | 重载对象的父 ID，对应 SYSOBJECTS 中被重载的运算符对象 ID |
| 3 | LEFTARG\_TYPE | VARCHAR(128) | 左运算对象的数据类型 |
| 4 | RIGHTARG\_TYPE | VARCHAR(128) | 右运算对象的数据类型 |
| 5 | CRTDATE | DATETIME(6) | 重载对象的创建时间 |
| 6 | VERSION | INTEGER | 版本号 |
| 7 | VALID | CHAR(1) | 是否有效，Y：有效；N：无效 |
| 8 | INFO1 | VARBINARY(2048) | 记录模式名、函数名等信息 |
| 9 | INFO2 | INTEGER | 是否为系统自定义运算符，0：否；1：是 |
| 10 | INFO3 | BIGINT | 保留字段 |
| 11 | INFO4 | VARBINARY(2048) | 保留字段 |

53. **SYSCRASHTRXS**

记录回滚过程中访问到损坏数据页的事务信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TS\_ID | INTEGER | 数据页所属表空间 ID |
| 2 | FIL\_ID | INTEGER | 数据页所属文件 ID |
| 3 | PAGE\_NO | INTEGER | 数据页号 |
| 4 | TRX\_ID | BIGINT | 事务 ID |
| 5 | TRX\_START\_LSN | BIGINT | 事务启动时系统 LSN 值 |
| 6 | ERRCODE | INTEGER | 错误码 |
| 7 | RECORD\_TIME | DATETIME(6) | 登记时间 |
| 8 | DB\_MAGIC | BIGINT | 数据库 DB\_MAGIC 值 |

54. **SYSPLANHIST**

记录历史执行计划中每个节点的信息。仅当 USE\_PLN\_POOL!=0 和 ENABLE\_MONITOR\_PLNHIST 开启时才将历史执行计划记录到该系统表中。不支持 DMDPC 环境下记录执行计划历史信息。

系统会自动将历史执行计划登记到 SYSPLANHIST 中。对于系统尚未来得及登记的计划信息，用户可执行 SP\_FLUSH\_HIST\_PLAN();进行手动登记。DSC 环境中，普通节点执行 SP\_FLUSH\_HIST\_PLAN();时，普通节点的计划信息发送给控制节点。控制节点并不会直接将计划刷盘至 SYSPLANHIST，需要等待控制节点达到刷盘条件或者执行 SP\_FLUSH\_HIST\_PLAN();时，才会将计划一起记录进 SYSPLANHIST。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PLAN\_HASH\_VALUE | INTEGER | SQL 哈希值 |
| 2 | PLAN\_ADDR | VARBINARY(8) | 计划地址 |
| 3 | SESS\_ID | BIGINT | 会话 ID |
| 4 | SCH\_ID | INTEGER | 模式 ID |
| 5 | SQL\_STR | VARCHAR(1000) | SQL 语句 |
| 6 | PLN\_STR | CLOB | 计划语句 |
| 7 | ID | INTEGER | 标识执行计划的每一步（从 0 开始） |
| 8 | OPERATION | VARCHAR(30) | 操作符 |
| 9 | OPTIONS | VARCHAR(20) | 扫描类型 |
| 10 | TABLE# | INTEGER | 表 ID |
| 11 | TABLE\_NAME | VARCHAR(128) | 表名 |
| 12 | TABLE\_ALIAS | VARCHAR(128) | 表别名 |
| 13 | INDEX\_NAME | VARCHAR(128) | 索引名称 |
| 14 | DEPTH | INTEGER | 层数（从 0 开始） |
| 15 | COST | BIGINT | 代价 |
| 16 | CARDINALITY | BIGINT | 行数 |
| 17 | BYTES | INTEGER | 字节数 |
| 18 | PARTITION\_START | INTEGER | 分区起始编号（仅兼容） |
| 19 | PARTITION\_STOP | INTEGER | 分区结束编号（仅兼容） |
| 20 | CPU\_COST | BIGINT | CPU 代价 |
| 21 | IO\_COST | BIGINT | IO 代价，暂不支持，始终为 0 |
| 22 | ACCESS\_PREDICATES | VARCHAR(128) | 扫描范围 |
| 23 | FILTER\_PREDICATES | VARCHAR(1000) | 过滤条件 |
| 24 | JOIN\_CONDITION | VARCHAR(1000) | 连接条件 |
| 25 | KEY\_CONDITION | VARCHAR(1000) | 键值条件 |
| 26 | REMARKS | VARCHAR(1000) | 评论（仅兼容） |
| 27 | TIMECREATE | DATETIME(6) | 创建时间 |

55. **SYSTYPEATTRINFO**

记录对象的属性信息。

该表不具有 PUBLIC 权限，三权分立下具有 SOI，DB\_AUDIT\_SOI，DB\_POLICY\_SOI 权限，如果是四权分立则额外拥有 DB\_OBJECT\_SOI 权限。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | OID | INTEGER | 存放当前对象的 id |
| 2 | ATTR\_NAME | VARCHAR2(128) | 存放当前对象的属性名 |
| 3 | ATTR\_TYPE\_OID | INTEGER | 属性的类型 id(仅属性为对象类型时有效） |
| 4 | ATTR\_TYPE\_NAME | VARCHAR2(128) | 对象类型属性名 |
| 5 | ATTR\_LENGTH | INTEGER | 属性的长度，仅字符串类型有效 |
| 6 | ATTR\_PRECISION | INTEGER | 对象类型属性精度 |
| 7 | ATTR\_SCALE | INTEGER | 对象类型属性范围 |
| 8 | ATTR\_NO | INTEGER | 属性的序号，即当前属性在对象中是第几个 |
| 9 | ATTR\_CHARSET | INTEGER | 对象类型属性所属字符集，暂时无用 |
| 10 | ATTR\_IS\_INHERI | INTEGER | 对象类型属性是否继承自父类型 |
| 11 | ATTR\_PROPERTIES | NUMBER | 保存当前属性的类型，暂时无用 |
| 12 | ATTR\_INFO1 | BIGINT | 对象类型附加信息 1，暂时无用 |
| 13 | ATTR\_INOF2 | VARBINARY(1024) | 对象类型附加信息 2，暂时无用 |

**56.** **SYSOPENHISTORY**

记录数据库的 Open 历史记录。在 Primary 或 Normal 模式库 Open 时，向系统表写入一条记录（称为 Open 记录）。SYSOPENHISTORY 表最多只维护 128 条 Open 记录，达到 128 条以后会从第一条记录开始自动覆盖，并依次往后循环使用。

DMDPC 多副本系统中的节点以及 DMDPC 中的 BP 节点不会生成 Open 记录。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | RGUID | VARCHAR(48) | 唯一 GUID 串，随机生成 |
| 2 | OPEN\_TIME | DATETIME(6) | 实例 OPEN 时间 |
| 3 | SYS\_MODE | VARCHAR(32) | 实例模式（PRIMARY/STANDBY/NORMAL） |
| 4 | PRIMARY\_INST\_NAME | VARCHAR(32) | 主库实例名 |
| 5 | CUR\_INST\_NAME | VARCHAR(32) | 当前实例名 |
| 6 | PRIMARY\_DB\_MAGIC | BIGINT | 主库 DB\_MAGIC 值 |
| 7 | CUR\_DB\_MAGIC | BIGINT | 当前库 DB\_MAGIC 值 |
| 8 | N\_EP | SMALLINT | 集群节点个数 |
| 9 | PKG\_SEQNO\_0 | BIGINT | 0 号节点最大重演的日志包序号 |
| 10 | PKG\_SEQNO\_1 | BIGINT | 1 号节点最大重演的日志包序号 |
| 11 | PKG\_SEQNO\_2 | BIGINT | 2 号节点最大重演的日志包序号 |
| 12 | PKG\_SEQNO\_3 | BIGINT | 3 号节点最大重演的日志包序号 |
| 13 | PKG\_SEQNO\_4 | BIGINT | 4 号节点最大重演的日志包序号 |
| 14 | PKG\_SEQNO\_5 | BIGINT | 5 号节点最大重演的日志包序号 |
| 15 | PKG\_SEQNO\_6 | BIGINT | 6 号节点最大重演的日志包序号 |
| 16 | PKG\_SEQNO\_7 | BIGINT | 7 号节点最大重演的日志包序号 |
| 17 | PKG\_SEQNO\_8 | BIGINT | 8 号节点最大重演的日志包序号 |
| 18 | PKG\_SEQNO\_9 | BIGINT | 9 号节点最大重演的日志包序号 |
| 19 | PKG\_SEQNO\_10 | BIGINT | 10 号节点最大重演的日志包序号 |
| 20 | PKG\_SEQNO\_11 | BIGINT | 11 号节点最大重演的日志包序号 |
| 21 | PKG\_SEQNO\_12 | BIGINT | 12 号节点最大重演的日志包序号 |
| 22 | PKG\_SEQNO\_13 | BIGINT | 13 号节点最大重演的日志包序号 |
| 23 | PKG\_SEQNO\_14 | BIGINT | 14 号节点最大重演的日志包序号 |
| 24 | PKG\_SEQNO\_15 | BIGINT | 15 号节点最大重演的日志包序号 |
| 25 | APPLY\_LSN\_0 | BIGINT | 0 号节点最大重演的 LSN 值 |
| 26 | APPLY\_LSN\_1 | BIGINT | 1 号节点最大重演的 LSN 值 |
| 27 | APPLY\_LSN\_2 | BIGINT | 2 号节点最大重演的 LSN 值 |
| 28 | APPLY\_LSN\_3 | BIGINT | 3 号节点最大重演的 LSN 值 |
| 29 | APPLY\_LSN\_4 | BIGINT | 4 号节点最大重演的 LSN 值 |
| 30 | APPLY\_LSN\_5 | BIGINT | 5 号节点最大重演的 LSN 值 |
| 31 | APPLY\_LSN\_6 | BIGINT | 6 号节点最大重演的 LSN 值 |
| 32 | APPLY\_LSN\_7 | BIGINT | 7 号节点最大重演的 LSN 值 |
| 33 | APPLY\_LSN\_8 | BIGINT | 8 号节点最大重演的 LSN 值 |
| 34 | APPLY\_LSN\_9 | BIGINT | 9 号节点最大重演的 LSN 值 |
| 35 | APPLY\_LSN\_10 | BIGINT | 10 号节点最大重演的 LSN 值 |
| 36 | APPLY\_LSN\_11 | BIGINT | 11 号节点最大重演的 LSN 值 |
| 37 | APPLY\_LSN\_12 | BIGINT | 12 号节点最大重演的 LSN 值 |
| 38 | APPLY\_LSN\_13 | BIGINT | 13 号节点最大重演的 LSN 值 |
| 39 | APPLY\_LSN\_14 | BIGINT | 14 号节点最大重演的 LSN 值 |
| 40 | APPLY\_LSN\_15 | BIGINT | 15 号节点最大重演的 LSN 值 |

57. **SYSDTYPEALIAS**

记录系统中所有类型别名的信息。该表在执行 SP\_INIT\_DTYPE\_SYS(1);后创建。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 类型别名的名称 |
| 2 | BASE\_NAME | VARCHAR(128) | 基础数据类型名 |
| 3 | LENGTH | SMALLINT | 基础数据类型长度 |
| 4 | SCALE | SMALLINT | 见 SYSCOLUMNS 中的 SCALE 列 |
---
title: "系统视图"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle2.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 系统视图

---

| 视图名称 | 说明 |
| --- | --- |
| DBA\_PROCEDURES | 列出数据库内所有的函数和存储过程 |
| ALL\_PROCEDURES | 列出当前用户可以访问的所有函数和存储过程 |
| USER\_PROCEDURES | 列出当前用户拥有的函数和存储过程 |
| DBA\_SOURCE | 列出数据库内所有的对象 |
| ALL\_SOURCE | 列出当前用户可以访问的对象 |
| USER\_SOURCE | 列出当前用户拥有的对象 |
| DBA\_ARGUMENTS | 列出数据库内所有的函数和存储过程的参数 |
| ALL\_ARGUMENTS | 列出当前用户可以访问的所有函数、存储过程以及包的参数 |
| USER\_ARGUMENTS | 列出当前用户拥有的函数和存储过程的参数 |
| DBA\_DB\_LINKS | 列出数据库中所有数据库链接的信息 |
| ALL\_DB\_LINKS | 列出当前用户能访问的所有数据库链接的信息 |
| USER\_DB\_LINKS | 列出当前用户创建的数据库链接的信息 |
| V$OPEN\_CURSOR | 列出当前会话中打开的游标的信息 |
| V$DBLINK | 列出现有数据库链接的动态信息 |
| GV$DBLINK | 列出全局数据库链接的动态信息 |
| DBA\_DB\_LINK\_SOURCES | 已存在的数据库链接信息 |
| DBA\_SEQUENCES | 列出数据库中所有用户定义序列的信息。 |
| ALL\_SEQUENCES | 列出当前用户可见的数据库中所有用户定义序列的信息。 |
| USER\_SEQUENCES | 列出当前用户创建的序列信息 |
| DBA\_VIEWS | 列出数据库中所有视图描述信息。 |
| ALL\_VIEWS | 列出当前用户可访问的所有视图描述信息。 |
| USER\_VIEWS | 列出当前用户创建的视图描述信息。 |
| DBA\_JOBS | 列出所有作业信息。 |
| ALL\_JOBS | 列出当前用户可访问的所有作业信息。 |
| USER\_JOBS | 列出当前用户创建的作业信息。 |
| DBA\_JOBS\_RUNNING | 列出所有正在运行的作业信息。 |
| DBA\_TABLES | 描述数据库中的所有关系表的相关信息。 |
| ALL\_TABLES | 描述当前用户可以访问的关系表的相关信息。 |
| USER\_TABLES | 描述当前用户拥有的关系表的相关信息。 |
| DBA\_TAB\_COLS | 描述当前数据库中的所有表、视图的列的相关信息。 |
| ALL\_TAB\_COLS | 描述当前用户可以访问的所有表、视图的列的相关信息。 |
| USER\_TAB\_COLS | 描述当前用户拥有的所有表、视图的列的相关信息。 |
| DBA\_TAB\_COLUMNS | 描述当前数据库中的所有表、视图的列相关信息。 |
| ALL\_TAB\_COLUMNS | 描述当前用户可以访问的所有表、视图的列相关信息。 |
| USER\_TAB\_COLUMNS | 描述当前用户拥有的所有表、视图的列相关信息。 |
| DBA\_TAB\_COMMENTS | 描述当前数据库中的所有表和视图的注释信息。 |
| ALL\_TAB\_COMMENTS | 描述当前用户可以访问的所有表和视图的注释信息。 |
| USER\_TAB\_COMMENTS | 描述当前用户拥有的所有表和视图的注释信息。 |
| DBA\_INDEXES | 描述当前数据库中的所有索引的相关信息。 |
| ALL\_INDEXES | 描述当前用户可以访问的所有索引的相关信息。 |
| USER\_INDEXES | 描述当前用户拥有的所有索引的相关信息。 |
| DBA\_IND\_COLUMNS | 描述当前数据库中的所有表上的索引列信息。 |
| ALL\_IND\_COLUMNS | 描述当前用户可以访问的所有表上的索引列信息。 |
| USER\_IND\_COLUMNS | 描述当前用户拥有的所有表上的索引列信息。 |
| DBA\_DEPENDENCIES | 描述当前数据库中的所有对象间的依赖信息。 |
| ALL\_DEPENDENCIES | 描述当前用户可以访问的所有对象间的依赖信息。 |
| USER\_DEPENDENCIES | 描述当前用户拥有的所有对象间的依赖信息。 |
| DBA\_OBJECTS | 描述当前数据库中的所有对象的相关信息。 |
| ALL\_OBJECTS | 描述当前用户可以访问的所有对象的相关信息。 |
| USER\_OBJECTS | 描述当前用户拥有的所有对象的相关信息。 |
| DBA\_TYPES | 描述当前数据库中的所有类型的相关信息。 |
| ALL\_TYPES | 描述当前用户可以访问的所有类型的相关信息。 |
| USER\_TYPES | 描述当前用户拥有的所有类型的相关信息。 |
| DBA\_USERS | 描述当前数据库中的所有用户信息。 |
| ALL\_USERS | 描述当前用户可见的数据库的所有用户信息。 |
| USER\_USERS | 描述当前用户的详细信息。 |
| DBA\_CONSTRAINTS | 描述当前数据库中的所有表上的约束定义。 |
| ALL\_CONSTRAINTS | 描述当前用户可以访问的所有表上的约束定义。 |
| USER\_CONSTRAINTS | 描述当前用户拥有的表上的约束定义。 |
| DBA\_CONS\_COLUMNS | 描述当前数据库中的所有被约束引用的列。 |
| ALL\_CONS\_COLUMNS | 描述当前用户可以访问的被约束引用的列。 |
| USER\_CONS\_COLUMNS | 描述当前用户拥有的被约束引用的列。 |
| DBA\_TAB\_PRIVS | 描述当前数据库中的所有对象的授权信息。 |
| ALL\_TAB\_PRIVS | 描述权限授予情况。 |
| USER\_TAB\_PRIVS | 描述当前用户作为对象所有者、授权者或被授权者的对象权限。 |
| DBA\_TAB\_PARTITIONS | 描述当前数据库中的所有分区的相关信息。 |
| ALL\_TAB\_PARTITIONS | 描述当前用户可以访问的分区的相关信息。 |
| USER\_TAB\_PARTITIONS | 描述当前用户拥有的分区表的相关信息。 |
| DBA\_TRIGGERS | 描述当前数据库中的所有触发器。 |
| ALL\_TRIGGERS | 描述当前用户可访问的表上的触发器。 |
| USER\_TRIGGERS | 描述当前用户拥有的触发器。 |
| DBA\_SYNONYMS | 描述所有同义词。 |
| ALL\_SYNONYMS | 描述当前用户可访问的所有同义词。 |
| USER\_SYNONYMS | 描述当前用户拥有的私有同义词。 |

---

## DBA\_PROCEDURES

DBA\_PROCEDURES列出了数据库中可用的所有函数和存储过程及其相关属性。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) |  | 存储过程所有者 |
| OBJECT\_NAME | VARCHAR2(128) |  | 对象名称:函数、存储过程或包名 |
| PROCEDURE\_NAME | VARCHAR2(128) |  | 存储过程名称 |
| OBJECT\_ID | NUMBER |  | 对象编号 |
| SUBPROGRAM\_ID | NUMBER |  | 子程序唯一标识符 |
| OVERLOAD | VARCHAR2(40) |  | 重载唯一标识符 |
| OBJECT\_TYPE | VARCHAR2(13) |  | 对象类型名称 |
| AGGREGATE | VARCHAR2(3) |  | 指示存储过程是否为聚合函数是：（YES）否：（NO） |
| PIPELINED | VARCHAR2(3) |  | 指示存储过程是否为pipelined表函数是：（YES）否：（NO） |
| IMPLTYPEOWNER | VARCHAR2(128) |  | 实现类型的所有者（如果有） |
| IMPLTYPENAME | VARCHAR2(128) |  | 实现类型的名称（如果有） |
| PARALLEL | VARCHAR2(3) |  | 指示存储过程或函数是否并行启用是：（YES）否：（NO） |
| INTERFACE | VARCHAR2(3) |  | 如果存储过程/函数是使用ODCI接口实现的表函数；则为YES，否则NO。 |
| DETERMINISTIC | VARCHAR2(3) |  | 如果存储过程/函数被声明为确定性；则为YES，否则NO |
| AUTHID | VARCHAR2(12) |  | 指示存储过程/函数是否声明为定义者执行或当前用户（调用方）执行 |
| RESULT\_CACHE | VARCHAR2(3) |  | 指示函数是否为结果缓存（YES）或非结果缓存（NO） |
| ORIGIN\_CON\_ID | VARCHAR2(256) |  | 数据来源的容器的ID。可能的值包括：0:此值用于非CDB中的行。此值不用于CDB。n： 此值用于包含源自容器ID为的容器的数据的行号n（如果行源在根容器下，则n=1） |
| POLYMORPHIC | VARCHAR2(5) |  | 多态表函数的类型：ROWTABLELEAFNULL |
| SQL\_MACRO | VARCHAR2(6) |  | 指示存储过程是否为SQL宏。可能的值：SCALAR：该过程是用于标量表达式的SQL宏TABLE：该过程是表表达式的SQL宏NULL：过程不是SQL宏 |
| BLOCKCHAIN | VARCHAR2(3) |  | 仅限内部使用 |
| BLOCKCHAIN\_MANDATORY\_VOTES | VARCHAR2(4000) |  | 仅限内部使用 |

## ALL\_PROCEDURES

ALL\_PROCEDURES列出了当前用户可以访问的所有函数和过程，以及相关属性。其列与DBA\_PROCEDURES中的列相同。

## USER\_PROCEDURES

USER\_PROCEDURES列出当前用户拥有的所有函数和存储过程及其关联属性。其列（OWNER除外）与DBA\_PROCEDURES中的列相同。

## DBA\_SOURCE

DBA\_SOURCE描述数据库中所有存储对象的源文本。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) | NOT NULL | 对象拥有者 |
| NAME | VARCHAR2(128) | NOT NULL | 对象名称 |
| TYPE | VARCHAR2(12) |  | 对象类型：FUNCTION、PACKAGE、PACKAGE BODY、PROCEDURE |
| LINE | NUMBER | NOT NULL | 源文件行号 |
| TEXT | VARCHAR2(4000) |  | 存储对象的文本源 |
| ORIGIN\_CON\_ID | VARCHAR2(256) |  | 数据来源的容器的ID。可能的值包括：0:此值用于非CDB中的行。此值不用于CDB。n： 此值用于包含源自容器ID为n的容器中的数据的行（如果行源容器下，则n=1） |

## ALL\_SOURCE

ALL\_SOURCE描述当前用户可访问的存储对象的源文本。其列与DBA\_SOURCE中的列相同。

## USER\_SOURCE

USER\_SOURCE描述当前用户拥有的存储对象的源文本。其列（OWNER除外）与ALL\_SOURCE中的列相同。

## DBA\_ARGUMENTS

DBA\_ARGUMENTS列出了数据库中可用的函数和存储过程的参数。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) | NOT NULL | 对象拥有者 |
| OBJECT\_NAME | VARCHAR2(128) |  | 存储过程或函数名称 |
| PACKAGE\_NAME | VARCHAR2(128) |  | 包名称 |
| OBJECT\_ID | NUMBER | NOT NULL | 对象编号 |
| OVERLOAD | VARCHAR2(40) |  | 按其在源中的外观排序的第n个重载；否则为NULL |
| SUBPROGRAM\_ID | NUMBER |  | 子程序唯一标识符 |
| ARGUMENT\_NAME | VARCHAR2(128) |  | 参数的名称空参数名用于表示一个返回函数。 |
| POSITION | NUMBER | NOT NULL | 此列保留此项在参数列表中的位置，或0表示函数返回值。 |
| SEQUENCE | NUMBER | NOT NULL | 定义参数的顺序。参数序列从1开始。首先返回类型，然后是每个参数。 |
| DATA\_LEVEL | NUMBER | NOT NULL | 复合类型参数的嵌套深度 |
| DATA\_TYPE | VARCHAR2(30) |  | 参数数据类型 |
| DEFAULTED | VARCHAR2(1) |  | 指定参数是否为默认值 |
| DEFAULT\_VALUE | LONG |  | 保留供将来使用 |
| DEFAULT\_LENGTH | NUMBER |  | 保留供将来使用 |
| IN\_OUT | VARCHAR2(9) |  | 参数的方向:INOUTIN/OUT |
| DATA\_LENGTH | NUMBER |  | 列的长度（字节） |
| DATA\_PRECISION | NUMBER |  | 以十进制数字（NUMBER）或二进制数字（FLOAT）表示的长度 |
| DATA\_SCALE | NUMBER |  | 数字中小数点右侧的数字 |
| RADIX | NUMBER |  | 数字的参数基数 |
| CHARACTER\_SET\_NAME | VARCHAR2(44) |  | 参数的字符集名称 |
| TYPE\_OWNER | VARCHAR2(128) |  | 参数的类型的属主，默认为NULL |
| TYPE\_NAME | VARCHAR2(128) |  | 参数类型的名称。如果类型是包本地类型（即在包规范中声明），则此列显示包的名称。 |
| TYPE\_SUBNAME | VARCHAR2(128) |  | 仅与包本地类型相关。显示在type\_name列中标识的包中声明类型的名称。 |
| TYPE\_LINK | VARCHAR2(128) |  | 仅当TYPE\_NAME列中标识的包是远程包时，才与包本地类型相关。此列显示用于引用远程包的数据库链接。默认为NULL |
| TYPE\_OBJECT\_TYPE | VARCHAR2(128) |  | 显示由type\_OWNER、type\_NAME和type\_SUBNAME列描述的类型类型。可能的值为：TABLEVIEWPACKAGETYPE |
| PLS\_TYPE | VARCHAR2(30) |  | 对于数字参数，为参数的PL/SQL类型的名称。否则为空。 |
| CHAR\_LENGTH | NUMBER |  | 字符串数据类型的字符限制 |
| CHAR\_USED | VARCHAR2(1) |  | 指示正式符串是字节限制（B）或字符限制（C） |
| ORIGIN\_CON\_ID | VARCHAR2(256) |  | 数据来源的容器的ID。可能的值包括：0:此值用于非CDB中的行。此值不用于CDB。n： 此值用于包含源自容器ID为的容器的数据的行号n（如果行源在根容器下，则n=1） |

## ALL\_ARGUMENTS

列出了当前用户可以访问的函数和过程的参数。其列与DBA\_ARGUMENTS中的列相同。

## USER\_ARGUMENTS

USER\_ARGUMENTS列出了当前用户拥有的存储函数和过程的参数。其列（OWNER除外）与ALL\_ARGUMENTS中的列相同。

## DBA\_DB\_LINKS

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) | NOT NULL | database link的属主 |
| DB\_LINK | VARCHAR2(128) | NOT NULL | database link的名称 |
| USERNAME | VARCHAR2(128) |  | 登录时的用户名 |
| CREDENTIAL\_NAME | VARCHAR2(128) |  | 连接到远程数据库时要使用的凭证名称 |
| CREDENTIAL\_OWNER | VARCHAR2(128) |  | 连接到远程数据库时要使用的凭证的所有者 |
| HOST | VARCHAR2(2000) |  | 链接主机信息 |
| CREATED | DATE | NOT NULL | 创建时间 |
| HIDDEN | VARCHAR2(3) |  | 内部使用 |
| SHARD\_INTERNAL | VARCHAR2(3) |  | 指示数据库链接是否用于支持分片数据库之间的操作。可能的值为：YES：该数据库链接用于并管理以支持分片数据库NO：该数据库链接未被用于并管理以支持分片数据库用户不应更改或删除用于支持分片数据库的数据库链接。 |
| VALID | VARCHAR2(3) |  | 指示数据库链接是否有效且可用。可能的值为：YES：数据库链接有效且可用。NO：数据库链接无效且不可用。 |
| INTRA\_CDB | VARCHAR2(3) |  | 内部使用 |

## ALL\_DB\_LINKS

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) | NOT NULL | database link的属主 |
| DB\_LINK | VARCHAR2(128) | NOT NULL | database link的名称 |
| USERNAME | VARCHAR2(128) |  | 登录时的用户名 |
| CREDENTIAL\_NAME | VARCHAR2(128) |  | 链接主机信息 |
| CREDENTIAL\_OWNER | VARCHAR2(128) |  | 连接到远程数据库时要使用的凭证名称 |
| HOST | VARCHAR2(2000) |  | 连接到远程数据库时要使用的凭证的所有者 |
| CREATED | DATE | NOT NULL | 创建时间 |
| HIDDEN | VARCHAR2(3) |  | 内部使用 |
| SHARD\_INTERNAL | VARCHAR2(3) |  | 指示数据库链接是否用于支持分片数据库之间的操作。可能的值为：YES：该数据库链接用于并管理以支持分片数据库NO：该数据库链接未被用于并管理以支持分片数据库用户不应更改或删除用于支持分片数据库的数据库链接。 |
| VALID | VARCHAR2(3) |  | 指示数据库链接是否有效且可用。可能的值为：YES：数据库链接有效且可用。NO：数据库链接无效且不可用。 |
| INTRA\_CDB | VARCHAR2(3) |  | 内部使用 |

## USER\_DB\_LINKS

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| DB\_LINK | VARCHAR2(128) | NOT NULL | database link的名称 |
| USERNAME | VARCHAR2(128) |  | 登录时的用户名 |
| PASSWORD | VARCHAR2(128) |  | 该列已不再使用，且不会返回任何内容。仅用于向后兼容。 |
| CREDENTIAL\_NAME | VARCHAR2(128) |  | 连接到远程数据库时要使用的凭证名称 |
| CREDENTIAL\_OWNER | VARCHAR2(128) |  | 连接到远程数据库时要使用的凭证的所有者 |
| HOST | VARCHAR2(2000) |  | 链接主机信息 |
| CREATED | DATE | NOT NULL | 创建时间 |
| HIDDEN | VARCHAR2(3) |  | 内部使用 |
| SHARD\_INTERNAL | VARCHAR2(3) |  | 指示数据库链接是否用于支持分片数据库之间的操作。可能的值为：YES：该数据库链接用于并管理以支持分片数据库NO：该数据库链接未被用于并管理以支持分片数据库用户不应更改或删除用于支持分片数据库的数据库链接。 |
| VALID | VARCHAR2(3) |  | 指示数据库链接是否有效且可用。可能的值为：YES：数据库链接有效且可用。NO：数据库链接无效且不可用。 |
| INTRA\_CDB | VARCHAR2(3) |  | 内部使用 |

## V$OPEN\_CURSOR

| 列名 | 数据类型 | 描述 |
| --- | --- | --- |
| SADDR | RAW(4 \| 8) | 会话地址 |
| SID | NUMBER | 会话标识符 |
| USER\_NAME | VARCHAR2(128) | 登录会话的用户名 |
| ADDRESS | RAW(4 \| 8) | 与HASH\_VALUE一起使用，以唯一标识会话中正在执行的 SQL语句 |
| HASH\_VALUE | NUMBER | 与ADDRESS一起使用，以唯一标识会话中正在执行的SQL 语句 |
| SQL\_ID | VARCHAR2(13) | 会话中正在执行的SQL语句的 SQL标识符 |
| SQL\_TEXT | VARCHAR2(60) | 解析为打开游标的 SQL 语句的前60个字符 |
| LAST\_SQL\_ACTIVE\_TIME | DATE | 游标最后执行的时间 |
| SQL\_EXEC\_ID | NUMBER | 如果打开的游标正在执行，则该执行的SQL执行标识符（请参见V$SQL\_MONITOR） |
| CURSOR\_TYPE | VARCHAR2(64) | 游标类型:OPEN PL/SQL - 打开PL/SQL cursorsOPEN - 其他打开游标SESSION CURSOR CACHED - 缓存于通用会话游标缓存中的游标OPEN-RECURSIVE - 打开递归游标DICTIONARY LOOKUP CURSOR CACHED - 缓存于字典查找游标缓存中的游标BUNDLE DICTIONARY LOOKUP CACHED - 缓存于捆绑的字典查找游标缓存中的游标JAVA NAME TRANSLATION CURSOR CACHED - 缓存于 Java 名称翻译游标缓存中的游标REPLICATION TRIGGER CURSOR CACHED - 缓存于复制触发器游标缓存中的游标CONSTRAINTS CURSOR CACHED - 缓存于约束游标缓存中的游标PL/SQL CURSOR CACHED - 缓存于 PL/SQL 游标缓存中的游标 |
| CHILD\_ADDRESS | RAW(4 \| 8) | 子游标的地址 |
| CON\_ID | NUMBER | 与数据相关的容器的ID。可能的值包括：0：该值用于包含与整个CDB 相关的数据的行。此值也用于非CDB中的行。1：该值用于包含仅与根相关的数据的行。n：其中n是包含数据的行的适用容器ID。 |

## V$DBLINK

---

| 列名 | 数据类型 | 描述 |
| --- | --- | --- |
| DB\_LINK | VARCHAR2(128) | database link的名称 |
| OWNER\_ID | NUMBER | database link的属主UID |
| LOGGED\_ON | VARCHAR2(3) | database link是否当前已登录 |
| HETEROGENEOUS | VARCHAR2(3) | database link是否异构 |
| PROTOCOL | VARCHAR2(6) | database link的通信协议 |
| OPEN\_CURSORS | NUMBER | database link是否有打开的游标 |
| IN\_TRANSACTION | VARCHAR2(3) | database link是否当前处于事务中 |
| UPDATE\_SENT | VARCHAR2(3) | database link是否有更新 |
| COMMIT\_POINT\_STRENGTH | NUMBER | database link上事务的提交点强度 |
| CON\_ID | NUMBER | 默认为0 |

---

## GV$DBLINK

| 列名 | 数据类型 | 描述 |
| --- | --- | --- |
| DB\_LINK | VARCHAR2(128) | database link的名字 |
| OWNER\_ID | NUMBER | database link的属主 |
| LOGGED\_ON | VARCHAR2(3) | database link是否当前已登录 |
| HETEROGENEOUS | VARCHAR2(3) | database link是同构（NO）还是异构（YES） |
| PROTOCOL | VARCHAR2(6) | database link通信协议 |
| OPEN\_CURSORS | NUMBER | database link是否有打开的游标 |
| IN\_TRANSACTION | VARCHAR2(3) | database link是否被用于尚未提交或回滚的事务 |
| UPDATE\_SENT | VARCHAR2(3) | database link是否有更新 |
| COMMIT\_POINT\_STRENGTH | NUMBER | 使用database link的事务的提交点强度 |
| INST\_ID | NUMBER | 获取视图信息的实例 |
| CON\_ID | NUMBER | 数据所属容器的 ID。可能的值包括：0 ：此值用于包含属于整个 CDB 的数据的行。此值也用于非 CDB 中的行。1 ：此值用于包含仅属于根的数据的行n ：其中 n 是包含数据的行的适用容器 ID |

## DBA\_DB\_LINK\_SOURCES

---

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| SOURCE\_ID | NUMBER | NOT NULL | 标识传入数据库链接的唯一ID |
| DB\_NAME | VARCHAR2(256) | NOT NULL | 当前连接的数据库名 |
| DBID | NUMBER | NOT NULL | 源数据库的数据库标识符。映射到V$DATABASE中的源数据库的DBID。 |
| DB\_UNIQUE\_NAME | VARCHAR2(256) |  | 源数据库的唯一数据库名称。映射到V$DATABASE中的源数据库的DB\_UNIQUE\_NAME。对于不提供此信息的源数据库，该值为空。 |
| HOST\_NAME | VARCHAR2(256) |  | 已解析的主机名。如果不可用则为空。 |
| IP\_ADDRESS | VARCHAR2(128) |  | 源机器的IP地址。如果不可用则为空。 |
| PROTOCOL | VARCHAR2(64) |  | 支持的协议之一，例如ipc、sdp、tcp或tcps。如果不可用则为空。 |
| USERNAME | VARCHAR2(128) | NOT NULL | 登录本地数据库的用户的Oracle用户名。映射到V$SESSION中的USERNAME列。 |
| USER# | NUMBER | NOT NULL | 登录本地数据库的用户的Oracle用户ID。映射到V$SESSION中的USER#列。 |
| FIRST\_LOGON\_TIME | TIMESTAMP(6) | NOT NULL | 通过此数据库链接的首次连接的UTC时间戳。 |
| LAST\_LOGON\_TIME | TIMESTAMP(6) |  | 通过此数据库链接的最后连接的UTC时间戳。 |
| LOGON\_COUNT | NUMBER |  | 通过此数据库链接建立连接的次数。 |

---

## DBA\_SEQUENCES

描述了数据库中的所有序列。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| SEQUENCE\_OWNER | VARCHAR2(128) | NOT NULL | 序列的所有者 |
| SEQUENCE\_NAME | VARCHAR2(128) | NOT NULL | 序列名称 |
| MIN\_VALUE | NUMBER |  | 序列的最小值 |
| MAX\_VALUE | NUMBER |  | 序列的最大值 |
| INCREMENT\_BY | NUMBER | NOT NULL | 序列的增量值 |
| CYCLE\_FLAG | VARCHAR2(1) |  | 表示序列在达到限制时是否循环（Y）或不循环（N） |
| ORDER\_FLAG | VARCHAR2(1) |  | 表示序列号是否按顺序生成（Y）或不按顺序生成（N） |
| CACHE\_SIZE | NUMBER | NOT NULL | 缓存的序列号数量 |
| LAST\_NUMBER | NUMBER | NOT NULL | 写入磁盘的最后一个序列号。如果序列使用缓存，则写入磁盘的数字是放入序列缓存的最后一个数字。此数字可能大于实际使用的最后一个序列号。对于会话序列，此列的值应被忽略。 |
| SCALE\_FLAG | VARCHAR2(1) |  | 表示该序列是否为可扩展序列（Y）或不是（N） |
| EXTEND\_FLAG | VARCHAR2(1) |  | 表示此可扩展序列生成的值是否超出 MAX\_VALUE 或 MIN\_VALUE（Y）或不超出（N） |
| SHARED\_FLAG | VARCHAR2(1) |  | 表示该序列是否为分片序列（Y）或不是（N） |
| SESSION\_FLAG | VARCHAR2(1) |  | 表示序列值是否为会话私有（Y）或不是（N） |
| KEEP\_VALUE | VARCHAR2(1) |  | 表示在故障重放后是否保留序列值（Y）或不保留（N） |

## ALL\_SEQUENCES

描述了当前用户可以访问的所有序列。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| SEQUENCE\_OWNER | VARCHAR2(128) | NOT NULL | 序列的所有者 |
| SEQUENCE\_NAME | VARCHAR2(128) | NOT NULL | 序列名称 |
| MIN\_VALUE | NUMBER |  | 序列的最小值 |
| MAX\_VALUE | NUMBER |  | 序列的最大值 |
| INCREMENT\_BY | NUMBER | NOT NULL | 序列的增量值 |
| CYCLE\_FLAG | VARCHAR2(1) |  | 表示序列在达到限制时是否循环（Y）或不循环（N） |
| ORDER\_FLAG | VARCHAR2(1) |  | 表示序列号是否按顺序生成（Y）或不按顺序生成（N） |
| CACHE\_SIZE | NUMBER | NOT NULL | 缓存的序列号数量 |
| LAST\_NUMBER | NUMBER | NOT NULL | 写入磁盘的最后一个序列号。如果序列使用缓存，则写入磁盘的数字是放入序列缓存的最后一个数字。此数字可能大于实际使用的最后一个序列号。对于会话序列，此列的值应被忽略。 |
| SCALE\_FLAG | VARCHAR2(1) |  | 表示该序列是否为可扩展序列（Y）或不是（N） |
| EXTEND\_FLAG | VARCHAR2(1) |  | 表示此可扩展序列生成的值是否超出 MAX\_VALUE 或 MIN\_VALUE（Y）或不超出（N） |
| SHARED\_FLAG | VARCHAR2(1) |  | 表示该序列是否为分片序列（Y）或不是（N） |
| SESSION\_FLAG | VARCHAR2(1) |  | 表示序列值是否为会话私有（Y）或不是（N） |
| KEEP\_VALUE | VARCHAR2(1) |  | 表示在故障重放后是否保留序列值（Y）或不保留（N） |

## USER\_SEQUENCES

描述了当前用户拥有的所有序列。此视图不显示SEQUENCE\_OWNER列。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| SEQUENCE\_NAME | VARCHAR2(128) | NOT NULL | 序列名称 |
| MIN\_VALUE | NUMBER |  | 序列的最小值 |
| MAX\_VALUE | NUMBER |  | 序列的最大值 |
| INCREMENT\_BY | NUMBER | NOT NULL | 序列的增量值 |
| CYCLE\_FLAG | VARCHAR2(1) |  | 表示序列在达到限制时是否循环（Y）或不循环（N） |
| ORDER\_FLAG | VARCHAR2(1) |  | 表示序列号是否按顺序生成（Y）或不按顺序生成（N） |
| CACHE\_SIZE | NUMBER | NOT NULL | 缓存的序列号数量 |
| LAST\_NUMBER | NUMBER | NOT NULL | 写入磁盘的最后一个序列号。如果序列使用缓存，则写入磁盘的数字是放入序列缓存的最后一个数字。此数字可能大于实际使用的最后一个序列号。对于会话序列，此列的值应被忽略。 |
| SCALE\_FLAG | VARCHAR2(1) |  | 表示该序列是否为可扩展序列（Y）或不是（N） |
| EXTEND\_FLAG | VARCHAR2(1) |  | 表示此可扩展序列生成的值是否超出 MAX\_VALUE 或 MIN\_VALUE（Y）或不超出（N） |
| SHARED\_FLAG | VARCHAR2(1) |  | 表示该序列是否为分片序列（Y）或不是（N） |
| SESSION\_FLAG | VARCHAR2(1) |  | 表示序列值是否为会话私有（Y）或不是（N） |
| KEEP\_VALUE | VARCHAR2(1) |  | 表示在故障重放后是否保留序列值（Y）或不保留（N） |

## DBA\_VIEWS

描述数据库中所有视图。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) | NOT NULL | 视图的所有者 |
| VIEW\_NAME | VARCHAR2(128) | NOT NULL | 视图的名称 |
| TEXT\_LENGTH | NUMBER |  | 视图文本的长度 |
| TEXT | LONG |  | 视图文本。仅当行来自当前容器时，此列才返回正确的值。在该视图中，BEQUEATH 子句不会作为 TEXT 列的一部分出现。 |
| TEXT\_VC | VARCHAR2(4000) |  | 视图文本。此列可能会截断视图文本。在该视图中，BEQUEATH 子句不会作为TEXT\_VC 列的一部分出现。 |
| TYPE\_TEXT\_LENGTH | NUMBER |  | 类型化视图的类型子句的长度 |
| TYPE\_TEXT | VARCHAR2(4000) |  | 类型化视图的类型子句 |
| OID\_TEXT\_LENGTH | NUMBER |  | 类型化视图的WITH OID 子句的长度 |
| OID\_TEXT | VARCHAR2(4000) |  | 类型化视图的WITH OID 子句 |
| VIEW\_TYPE\_OWNER | VARCHAR2(128) |  | 如果视图是类型化视图，则为视图类型的拥有者 |
| VIEW\_TYPE | VARCHAR2(128) |  | 如果视图是类型化视图，则为视图的类型 |
| SUPERVIEW\_NAME | VARCHAR2(128) |  | 超视图的名称 |
| EDITIONING\_VIEW | VARCHAR2(1) |  | 保留用于未来使用 |
| READ\_ONLY | VARCHAR2(1) |  | 指示视图是否为只读（Y）或不是（N） |
| CONTAINER\_DATA | VARCHAR2(1) |  | 指示视图是否包含容器特定数据。可能的值：Y：如果视图是使用 CONTAINER\_DATA 子句创建的N：其他情况 |
| BEQUEATH | VARCHAR2(12) |  | 可能的值：CURRENT\_USER：当视图是 BEQUEATH CURRENT\_USER 视图DEFINER：当视图是 BEQUEATH DEFINER 视图 |
| ORIGIN\_CON\_ID | VARCHAR2(256) |  | 数据来源的容器 ID。可能的值包括：0：此值用于非 CDB 中的行。在 CDB 中不使用此值。n：此值用于包含来自容器 ID 为 n 的数据的行（如果行来自根容器，则 n = 1） |
| DEFAULT\_COLLATION | VARCHAR2(100) |  | 视图的默认排序规则 |
| CONTAINERS\_DEFAULT | VARCHAR2(3) |  | 指示视图是否默认启用 CONTAINERS()（YES）或不是（NO） |
| CONTAINER\_MAP | VARCHAR2(3) |  | 指示视图是否启用与 container\_map 数据库属性一起使用（YES）或不是（NO） |
| EXTENDED\_DATA\_LINK | VARCHAR2(3) |  | 指示视图是否启用从根获取扩展数据链接（YES）或不是（NO） |
| EXTENDED\_DATA\_LINK\_MAP | VARCHAR2(3) |  | 仅限内部使用 |
| HAS\_SENSITIVE\_COLUMN | VARCHAR2(3) |  | 指示视图是否包含一个或多个敏感列（YES）或不是（NO） |
| ADMIT\_NULL | VARCHAR2(3) |  | 指示视图是否允许 NULL 的 CON\_ID 数据（YES）或不是（NO） |
| PDB\_LOCAL\_ONLY | VARCHAR2(3) |  | 仅限内部使用 |

## ALL\_VIEWS

描述当前用户可以访问到的视图。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) | NOT NULL | 视图的所有者 |
| VIEW\_NAME | VARCHAR2(128) | NOT NULL | 视图的名称 |
| TEXT\_LENGTH | NUMBER |  | 视图文本的长度 |
| TEXT | LONG |  | 视图文本。仅当行来自当前容器时，此列才返回正确的值。在该视图中，BEQUEATH 子句不会作为 TEXT 列的一部分出现。 |
| TEXT\_VC | VARCHAR2(4000) |  | 视图文本。此列可能会截断视图文本。在该视图中，BEQUEATH 子句不会作为TEXT\_VC 列的一部分出现。 |
| TYPE\_TEXT\_LENGTH | NUMBER |  | 类型化视图的类型子句的长度 |
| TYPE\_TEXT | VARCHAR2(4000) |  | 类型化视图的类型子句 |
| OID\_TEXT\_LENGTH | NUMBER |  | 类型化视图的WITH OID 子句的长度 |
| OID\_TEXT | VARCHAR2(4000) |  | 类型化视图的WITH OID 子句 |
| VIEW\_TYPE\_OWNER | VARCHAR2(128) |  | 如果视图是类型化视图，则为视图类型的拥有者 |
| VIEW\_TYPE | VARCHAR2(128) |  | 如果视图是类型化视图，则为视图的类型 |
| SUPERVIEW\_NAME | VARCHAR2(128) |  | 超视图的名称 |
| EDITIONING\_VIEW | VARCHAR2(1) |  | 保留用于未来使用 |
| READ\_ONLY | VARCHAR2(1) |  | 指示视图是否为只读（Y）或不是（N） |
| CONTAINER\_DATA | VARCHAR2(1) |  | 指示视图是否包含容器特定数据。可能的值：Y：如果视图是使用 CONTAINER\_DATA 子句创建的N：其他情况 |
| BEQUEATH | VARCHAR2(12) |  | 可能的值：CURRENT\_USER：当视图是 BEQUEATH CURRENT\_USER 视图DEFINER：当视图是 BEQUEATH DEFINER 视图 |
| ORIGIN\_CON\_ID | VARCHAR2(256) |  | 数据来源的容器 ID。可能的值包括：0：此值用于非 CDB 中的行。在 CDB 中不使用此值。n：此值用于包含来自容器 ID 为 n 的数据的行（如果行来自根容器，则 n = 1） |
| DEFAULT\_COLLATION | VARCHAR2(100) |  | 视图的默认排序规则 |
| CONTAINERS\_DEFAULT | VARCHAR2(3) |  | 指示视图是否默认启用 CONTAINERS()（YES）或不是（NO） |
| CONTAINER\_MAP | VARCHAR2(3) |  | 指示视图是否启用与 container\_map 数据库属性一起使用（YES）或不是（NO） |
| EXTENDED\_DATA\_LINK | VARCHAR2(3) |  | 指示视图是否启用从根获取扩展数据链接（YES）或不是（NO） |
| EXTENDED\_DATA\_LINK\_MAP | VARCHAR2(3) |  | 仅限内部使用 |
| HAS\_SENSITIVE\_COLUMN | VARCHAR2(3) |  | 指示视图是否包含一个或多个敏感列（YES）或不是（NO） |
| ADMIT\_NULL | VARCHAR2(3) |  | 指示视图是否允许 NULL 的 CON\_ID 数据（YES）或不是（NO） |
| PDB\_LOCAL\_ONLY | VARCHAR2(3) |  | 仅限内部使用 |

## USER\_VIEWS

描述当前用户的拥有的视图，视图不包括OWNER 列。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| VIEW\_NAME | VARCHAR2(128) | NOT NULL | 视图的名称 |
| TEXT\_LENGTH | NUMBER |  | 视图文本的长度 |
| TEXT | LONG |  | 视图文本。仅当行来自当前容器时，此列才返回正确的值。在该视图中，BEQUEATH 子句不会作为 TEXT 列的一部分出现。 |
| TEXT\_VC | VARCHAR2(4000) |  | 视图文本。此列可能会截断视图文本。在该视图中，BEQUEATH 子句不会作为TEXT\_VC 列的一部分出现。 |
| TYPE\_TEXT\_LENGTH | NUMBER |  | 类型化视图的类型子句的长度 |
| TYPE\_TEXT | VARCHAR2(4000) |  | 类型化视图的类型子句 |
| OID\_TEXT\_LENGTH | NUMBER |  | 类型化视图的WITH OID 子句的长度 |
| OID\_TEXT | VARCHAR2(4000) |  | 类型化视图的WITH OID 子句 |
| VIEW\_TYPE\_OWNER | VARCHAR2(128) |  | 如果视图是类型化视图，则为视图类型的拥有者 |
| VIEW\_TYPE | VARCHAR2(128) |  | 如果视图是类型化视图，则为视图的类型 |
| SUPERVIEW\_NAME | VARCHAR2(128) |  | 超视图的名称 |
| EDITIONING\_VIEW | VARCHAR2(1) |  | 保留用于未来使用 |
| READ\_ONLY | VARCHAR2(1) |  | 指示视图是否为只读（Y）或不是（N） |
| CONTAINER\_DATA | VARCHAR2(1) |  | 指示视图是否包含容器特定数据。可能的值：Y：如果视图是使用 CONTAINER\_DATA 子句创建的N：其他情况 |
| BEQUEATH | VARCHAR2(12) |  | 可能的值：CURRENT\_USER：当视图是 BEQUEATH CURRENT\_USER 视图DEFINER：当视图是 BEQUEATH DEFINER 视图 |
| ORIGIN\_CON\_ID | VARCHAR2(256) |  | 数据来源的容器 ID。可能的值包括：0：此值用于非 CDB 中的行。在 CDB 中不使用此值。n：此值用于包含来自容器 ID 为 n 的数据的行（如果行来自根容器，则 n = 1） |
| DEFAULT\_COLLATION | VARCHAR2(100) |  | 视图的默认排序规则 |
| CONTAINERS\_DEFAULT | VARCHAR2(3) |  | 指示视图是否默认启用 CONTAINERS()（YES）或不是（NO） |
| CONTAINER\_MAP | VARCHAR2(3) |  | 指示视图是否启用与 container\_map 数据库属性一起使用（YES）或不是（NO） |
| EXTENDED\_DATA\_LINK | VARCHAR2(3) |  | 指示视图是否启用从根获取扩展数据链接（YES）或不是（NO） |
| EXTENDED\_DATA\_LINK\_MAP | VARCHAR2(3) |  | 仅限内部使用 |
| HAS\_SENSITIVE\_COLUMN | VARCHAR2(3) |  | 指示视图是否包含一个或多个敏感列（YES）或不是（NO） |
| ADMIT\_NULL | VARCHAR2(3) |  | 指示视图是否允许 NULL 的 CON\_ID 数据（YES）或不是（NO） |
| PDB\_LOCAL\_ONLY | VARCHAR2(3) |  | 仅限内部使用 |

## DBA\_JOBS

描述数据库中的所有JOB。

---

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| JOB | NUMBER | NOT NULL | 作业的标识符。导入/导出操作或重复执行不会改变此值。 |
| LOG\_USER | VARCHAR2(128) | NOT NULL | 提交作业时的登录用户。 |
| PRIV\_USER | VARCHAR2(128) | NOT NULL | 作业适用的默认权限所属用户。 |
| SCHEMA\_USER | VARCHAR2(128) | NOT NULL | 解析作业时使用的默认模式。例如，如果 SCHEMA\_USER 是 SCOTT，你提交名为 HIRE\_EMP 的过程作为作业，Oracle 数据库将查找 SCOTT.HIRE\_EMP。 |
| LAST\_DATE | DATE |  | 上次成功执行该作业的日期。 |
| LAST\_SEC | VARCHAR2(8) |  | 与 LAST\_DATE 相同。这是上次成功执行开始的时间。 |
| THIS\_DATE | DATE |  | 该作业开始执行的日期（如果未执行，通常为 NULL）。 |
| THIS\_SEC | VARCHAR2(8) |  | 与 THIS\_DATE 相同。这是上次成功执行开始的时间。 |
| NEXT\_DATE | DATE | NOT NULL | 该作业下次将被执行的日期。 |
| NEXT\_SEC | VARCHAR2(8) |  | 与 NEXT\_DATE 相同。作业在该时间到期执行。 |
| TOTAL\_TIME | NUMBER |  | 自此作业首次执行以来，系统在此作业上花费的总时间（以秒为单位）。此值是累积的。 |
| BROKEN | VARCHAR2(1) |  | Y：不会尝试运行此作业；N：会尝试运行此作业。 |
| INTERVAL | VARCHAR2(200) | NOT NULL | 一个日期函数，在执行开始时进行评估，成为下一个 NEXT\_DATE。 |
| FAILURES | NUMBER |  | 自上次成功以来，作业启动并失败的次数。 |
| WHAT | VARCHAR2(4000) |  | 作业执行的匿名 PL/SQL 块的主体。 |
| NLS\_ENV | VARCHAR2(4000) |  | 描述作业的 NLS 环境的会话参数。 |
| MISC\_ENV | RAW(32) |  | 参数兼容。 |
| INSTANCE | NUMBER |  | 参数兼容。 |

---

## ALL\_JOBS

是DBA\_JOBS的同义词。

---

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| JOB | NUMBER | NOT NULL | 作业的标识符。导入/导出操作或重复执行不会改变此值。 |
| LOG\_USER | VARCHAR2(128) | NOT NULL | 提交作业时的登录用户。 |
| PRIV\_USER | VARCHAR2(128) | NOT NULL | 作业适用的默认权限所属用户。 |
| SCHEMA\_USER | VARCHAR2(128) | NOT NULL | 解析作业时使用的默认模式。例如，如果 SCHEMA\_USER 是 SCOTT，你提交名为 HIRE\_EMP 的过程作为作业，Oracle 数据库将查找 SCOTT.HIRE\_EMP。 |
| LAST\_DATE | DATE |  | 上次成功执行该作业的日期。 |
| LAST\_SEC | VARCHAR2(8) |  | 与 LAST\_DATE 相同。这是上次成功执行开始的时间。 |
| THIS\_DATE | DATE |  | 该作业开始执行的日期（如果未执行，通常为 NULL）。 |
| THIS\_SEC | VARCHAR2(8) |  | 与 THIS\_DATE 相同。这是上次成功执行开始的时间。 |
| NEXT\_DATE | DATE | NOT NULL | 该作业下次将被执行的日期。 |
| NEXT\_SEC | VARCHAR2(8) |  | 与 NEXT\_DATE 相同。作业在该时间到期执行。 |
| TOTAL\_TIME | NUMBER |  | 自此作业首次执行以来，系统在此作业上花费的总时间（以秒为单位）。此值是累积的。 |
| BROKEN | VARCHAR2(1) |  | Y：不会尝试运行此作业；N：会尝试运行此作业。 |
| INTERVAL | VARCHAR2(200) | NOT NULL | 一个日期函数，在执行开始时进行评估，成为下一个NEXT\_DATE。 |
| FAILURES | NUMBER |  | 自上次成功以来，作业启动并失败的次数。 |
| WHAT | VARCHAR2(4000) |  | 作业执行的匿名 PL/SQL 块的主体。 |
| NLS\_ENV | VARCHAR2(4000) |  | 描述作业的 NLS 环境的会话参数。 |
| MISC\_ENV | RAW(32) |  | 参数兼容。 |
| INSTANCE | NUMBER |  | 参数兼容。 |

---

## USER\_JOBS

描述了当前用户所拥有的作业。其列与DBA\_JOBS 中的列相同。

---

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| JOB | NUMBER | NOT NULL | 作业的标识符。导入/导出操作或重复执行不会改变此值。 |
| LOG\_USER | VARCHAR2(128) | NOT NULL | 提交作业时的登录用户。 |
| PRIV\_USER | VARCHAR2(128) | NOT NULL | 作业适用的默认权限所属用户。 |
| SCHEMA\_USER | VARCHAR2(128) | NOT NULL | 解析作业时使用的默认模式。例如，如果 SCHEMA\_USER 是 SCOTT，你提交名为 HIRE\_EMP 的过程作为作业，Oracle 数据库将查找 SCOTT.HIRE\_EMP。 |
| LAST\_DATE | DATE |  | 上次成功执行该作业的日期。 |
| LAST\_SEC | VARCHAR2(8) |  | 与 LAST\_DATE 相同。这是上次成功执行开始的时间。 |
| THIS\_DATE | DATE |  | 该作业开始执行的日期（如果未执行，通常为 NULL）。 |
| THIS\_SEC | VARCHAR2(8) |  | 与 THIS\_DATE 相同。这是上次成功执行开始的时间。 |
| NEXT\_DATE | DATE | NOT NULL | 该作业下次将被执行的日期。 |
| NEXT\_SEC | VARCHAR2(8) |  | 与 NEXT\_DATE 相同。作业在该时间到期执行。 |
| TOTAL\_TIME | NUMBER |  | 自此作业首次执行以来，系统在此作业上花费的总时间（以秒为单位）。此值是累积的。 |
| BROKEN | VARCHAR2(1) |  | Y：不会尝试运行此作业；N：会尝试运行此作业。 |
| INTERVAL | VARCHAR2(200) | NOT NULL | 一个日期函数，在执行开始时进行评估，成为下一个 NEXT\_DATE。 |
| FAILURES | NUMBER |  | 自上次成功以来，作业启动并失败的次数。 |
| WHAT | VARCHAR2(4000) |  | 作业执行的匿名 PL/SQL 块的主体。 |
| NLS\_ENV | VARCHAR2(4000) |  | 描述作业的 NLS 环境的会话参数。 |
| MISC\_ENV | RAW(32) |  | 参数兼容。 |
| INSTANCE | NUMBER |  | 参数兼容。 |

---

## DBA\_JOBS\_RUNNING

列出了实例中当前正在运行的所有作业。

---

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| SID | NUMBER |  | 正在执行作业的进程的标识符。参见“V$LOCK”。 |
| JOB | NUMBER |  | 作业的标识符。该作业目前正在执行。 |
| FAILURES | NUMBER |  | 自上次成功以来，该作业启动并失败的次数。 |
| LAST\_DATE | DATE |  | 该作业上次成功执行的日期。 |
| LAST\_SEC | VARCHAR2(8) |  | 与 LAST\_DATE 相同。这是上次成功执行开始的时间。 |
| THIS\_DATE | DATE |  | 该作业开始执行的日期。 |
| THIS\_SEC | VARCHAR2(8) |  | 与 THIS\_DATE 相同。这是上次成功执行开始的时间。 |
| INSTANCE | NUMBER |  | 参数兼容 |

---

## DBA\_TABLES

描述数据库中的所有关系表的相关信息。

该视图在V9.0.5及以后的版本中支持。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) |  | 表的所有者 |
| TABLE\_NAME | VARCHAR2(128) |  | 表名 |
| TABLESPACE\_NAME | VARCHAR2(30) |  | 表所属的TABLESPACE，分区表、临时表、IOT该字段为NULL |
| CLUSTER\_NAME | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| IOT\_NAME | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| STATUS | VARCHAR2(8) |  | 仅列名兼容。返回VALID。 |
| PCT\_FREE | NUMBER |  | 块中保留用于更新的空闲空间百分比，分区表父表该字段为空。默认值根据填充因子计算。 |
| PCT\_USED | NUMBER |  | 仅列名兼容。返回NULL。 |
| INI\_TRANS | NUMBER |  | 仅列名兼容。返回NULL。 |
| MAX\_TRANS | NUMBER |  | 仅列名兼容。返回NULL。 |
| INITIAL\_EXTENT | NUMBER |  | 仅列名兼容。返回NULL。 |
| NEXT\_EXTENT | NUMBER |  | 仅列名兼容。返回NULL。 |
| MIN\_EXTENTS | NUMBER |  | 仅列名兼容。返回NULL。 |
| MAX\_EXTENTS | NUMBER |  | 仅列名兼容。返回NULL。 |
| PCT\_INCREASE | NUMBER |  | 仅列名兼容。返回NULL。 |
| FREELISTS | NUMBER |  | 仅列名兼容。返回NULL。 |
| FREELIST\_GROUPS | NUMBER |  | 仅列名兼容。返回NULL。 |
| LOGGING | VARCHAR2(3) |  | 标识表是否是UNLOGGED表，取值范围\[YES, NO\]。分区表父表该字段为空。 |
| BACKED\_UP | VARCHAR2(1) |  | 仅列名兼容。返回NULL。 |
| NUM\_ROWS | NUMBER |  | 表中数据的行数 |
| BLOCKS | NUMBER |  | 表中数据块的数量 |
| EMPTY\_BLOCKS | NUMBER |  | 仅列名兼容。返回NULL。 |
| AVG\_SPACE | NUMBER |  | 仅列名兼容。返回NULL。 |
| CHAIN\_CNT | NUMBER |  | 仅列名兼容。返回NULL。 |
| AVG\_ROW\_LEN | NUMBER |  | 表中平均行数据长度(B) |
| AVG\_SPACE\_FREELIST\_BLOCKS | NUMBER |  | 仅列名兼容。返回NULL。 |
| NUM\_FREELIST\_BLOCKS | NUMBER |  | 仅列名兼容。返回NULL。 |
| DEGREE | VARCHAR2(10) |  | 仅列名兼容。返回NULL。 |
| INSTANCES | VARCHAR2(10) |  | 仅列名兼容。返回NULL。 |
| CACHE | VARCHAR2(5) |  | 仅列名兼容。返回NULL。 |
| TABLE\_LOCK | VARCHAR2(8) |  | 仅列名兼容。返回NULL。 |
| SAMPLE\_SIZE | NUMBER |  | 仅列名兼容。返回NULL。 |
| LAST\_ANALYZED | DATE |  | 最近一次ANALYZE的时间 |
| PARTITIONED | VARCHAR2(3) |  | 标识是否是分区表，取值范围\[YES, NO\] |
| IOT\_TYPE | VARCHAR2(12) |  | 仅列名兼容。返回NULL。 |
| TEMPORARY | VARCHAR2(1) |  | 是否是临时表，取值范围\[Y, N\] |
| SECONDARY | VARCHAR2(1) |  | 仅列名兼容。返回NULL。 |
| NESTED | VARCHAR2(3) |  | 仅列名兼容。返回NULL。 |
| BUFFER\_POOL | VARCHAR2(7) |  | 仅列名兼容。返回NULL。 |
| FLASH\_CACHE | VARCHAR2(7) |  | 仅列名兼容。返回NULL。 |
| CELL\_FLASH\_CACHE | VARCHAR2(7) |  | 仅列名兼容。返回NULL。 |
| ROW\_MOVEMENT | VARCHAR2(8) |  | 仅列名兼容。返回ENABLED。 |
| GLOBAL\_STATS | VARCHAR2(3) |  | 仅列名兼容。返回YES。 |
| USER\_STATS | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| DURATION | VARCHAR2(15) |  | 临时表的持续时间；SYS$SESSION: 会话级临时表，数据持续到会话结束、SYS$TRANSACTION：事务级临时表，数据持续到事务结束、NULL：普通业务表 |
| SKIP\_CORRUPT | VARCHAR2(8) |  | 扫描时是否跳过坏块，取值范围\[ENABLED, DISABLED\]。默认值参考ZERO\_DAMAGED\_PAGES参数。 |
| MONITORING | VARCHAR2(3) |  | 仅列名兼容。返回NULL。 |
| CLUSTER\_OWNER | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| DEPENDENCIES | VARCHAR2(8) |  | 仅列名兼容。返回DISABLED。 |
| COMPRESSION | VARCHAR2(8) |  | 仅列名兼容。返回DISABLED。 |
| COMPRESS\_FOR | VARCHAR2(30) |  | 仅列名兼容。返回NULL。 |
| DROPPED | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| READ\_ONLY | VARCHAR2(3) |  | 仅列名兼容。返回NULL。 |
| SEGMENT\_CREATED | VARCHAR2(3) |  | 仅列名兼容。返回NULL。 |
| RESULT\_CACHE | VARCHAR2(7) |  | 仅列名兼容。返回NULL。 |
| CLUSTERING | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| ACTIVITY\_TRACKING | VARCHAR2(23) |  | 仅列名兼容。返回NULL。 |
| DML\_TIMESTAMP | VARCHAR2(25) |  | 仅列名兼容。返回NULL。 |
| HAS\_IDENTITY | VARCHAR2(3) |  | 表是否包含标识列，取值范围\[YES, NO\] |
| CONTAINER\_DATA | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| INMEMORY | VARCHAR2(8) |  | 仅列名兼容。返回DISABLED。 |
| INMEMORY\_PRIORITY | VARCHAR2(8) |  | 仅列名兼容。返回NULL。 |
| INMEMORY\_DISTRIBUTE | VARCHAR2(15) |  | 仅列名兼容。返回NULL。 |
| INMEMORY\_COMPRESSION | VARCHAR2(17) |  | 仅列名兼容。返回NULL。 |
| INMEMORY\_DUPLICATE | VARCHAR2(13) |  | 仅列名兼容。返回NULL。 |
| DEFAULT\_COLLATION | VARCHAR2(100) |  | 默认排序规则。默认值为PG\_OBJECT.OPTION\[‘COLLATION’\] |
| DUPLICATED | VARCHAR2(1) |  | 仅列名兼容。返回N。 |
| SHARDED | VARCHAR2(1) |  | 仅列名兼容。返回N。 |
| EXTERNALLY\_SHARDED | VARCHAR2(1) |  | 仅列名兼容。返回N。 |
| EXTERNALLY\_DUPLICATED | VARCHAR2(1) |  | 仅列名兼容。返回N。 |
| EXTERNAL | VARCHAR2(3) |  | 是否是外部表，取值范围\[YES, NO\]。 |
| HYBRID | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| CELLMEMORY | VARCHAR2(24) |  | 仅列名兼容。返回NULL。 |
| CONTAINERS\_DEFAULT | VARCHAR2(3) |  | 仅列名兼容。返回NULL。 |
| CONTAINER\_MAP | VARCHAR2(3) |  | 仅列名兼容。返回NULL。 |
| EXTENDED\_DATA\_LINK | VARCHAR2(3) |  | 仅列名兼容。返回NULL。 |
| EXTENDED\_DATA\_LINK\_MAP | VARCHAR2(3) |  | 仅列名兼容。返回NULL。 |
| INMEMORY\_SERVICE | VARCHAR2(12) |  | 仅列名兼容。返回NULL。 |
| INMEMORY\_SERVICE\_NAME | VARCHAR2(1000) |  | 仅列名兼容。返回NULL。 |
| CONTAINER\_MAP\_OBJECT | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| MEMOPTIMIZE\_READ | VARCHAR2(8) |  | 仅列名兼容。返回DISABLED。 |
| MEMOPTIMIZE\_WRITE | VARCHAR2(8) |  | 仅列名兼容。返回NULL。 |
| HAS\_SENSITIVE\_COLUMN | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| ADMIT\_NULL | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| DATA\_LINK\_DML\_ENABLED | VARCHAR2(3) |  | 仅列名兼容。返回YES。 |
| LOGICAL\_REPLICATION | VARCHAR2(8) |  | 是否启用了逻辑复制功能，取值范围\[ENABLED, DISABLED\] |

备注：

- PCT\_FREE字段说明：如果在建表时通过with (fillfactor =  
	n)指定了填充因子，则该字段取值为100 - n；否则该字段取值为0。
- DURATION字段说明：由于内部原因，当使用兼容PG的语法创建事务级临时表时（CREATE  
	TEMP TABLE...ON COMMIT DELETE  
	ROWS），该字段仍返回SYS$SESSION。使用兼容Oracle的语法创建时，按实际情况返回SYS$SESSION或者SYS$TRANSACTION。

## ALL\_TABLES

描述当前用户可以访问的关系表的相关信息。是dba\_tables的一个子集。

\[该视图在V9.0.5及以后的版本中支持。\]{.mark}

## USER\_TABLES

描述当前用户拥有的关系表的相关信息。是all\_tables的一个子集，不包含owner列。

该视图在V9.0.5及以后的版本中支持。

## DBA\_TAB\_COLS

描述当前数据库中的所有表、视图的列的相关信息。

该视图在V9.0.5及以后的版本中支持。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) |  | 表或视图的所有者 |
| TABLE\_NAME | VARCHAR2(128) |  | 表或视图名 |
| COLUMN\_NAME | VARCHAR2(128) |  | 列名 |
| DATA\_TYPE | VARCHAR2(128) |  | 列的数据类型 |
| DATA\_TYPE\_MOD | VARCHAR2(3) |  | 仅列名兼容。返回NULL。 |
| DATA\_TYPE\_OWNER | VARCHAR2(128) |  | 列类型拥有者 |
| DATA\_LENGTH | NUMBER |  | 列长度(B) |
| DATA\_PRECISION | NUMBER |  | 数据精度 |
| DATA\_SCALE | NUMBER |  | 数字中小数点右侧的位数 |
| NULLABLE | VARCHAR2(1) |  | 标识列是否允许为空值 |
| COLUMN\_ID | NUMBER |  | 列的创建顺序号 |
| DEFAULT\_LENGTH | NUMBER |  | 列的默认值长度 |
| DATA\_DEFAULT | LONG |  | 列的默认值 |
| NUM\_DISTINCT | NUMBER |  | 仅列名兼容。返回NULL。 |
| LOW\_VALUE | RAW(1000) |  | 仅列名兼容。返回NULL。 |
| HIGH\_VALUE | RAW(1000) |  | 仅列名兼容。返回NULL。 |
| DENSITY | NUMBER |  | 仅列名兼容。返回NULL。 |
| NUM\_NULLS | NUMBER |  | 列中空值的数量，即该列为空的数据行的数量 |
| NUM\_BUCKETS | NUMBER |  | 仅列名兼容。返回NULL。 |
| LAST\_ANALYZED | DATE |  | 最近一次ANALYZE的时间 |
| SAMPLE\_SIZE | NUMBER |  | 仅列名兼容。返回NULL。 |
| CHARACTER\_SET\_NAME | VARCHAR2(44) |  | 字符集名称 |
| CHAR\_COL\_DECL\_LENGTH | NUMBER |  | 字符类型列的声明长度 |
| GLOBAL\_STATS | VARCHAR2(3) |  | 仅列名兼容。返回YES。 |
| USER\_STATS | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| AVG\_COL\_LEN | NUMBER |  | 列平均长度(B) |
| CHAR\_LENGTH | NUMBER |  | 字符类型列的长度，仅适用于以下类型： CHAR, VARCHAR2, NCHAR, NVARCHAR2 |
| CHAR\_USED | VARCHAR2(1) |  | 标识列使用的是字节长度B或者字符长度C，取值范围\[B, C\]，仅适用于以下类型： CHAR, VARCHAR2, NCHAR, NVARCHAR2 |
| V80\_FMT\_IMAGE | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| DATA\_UPGRADED | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| HIDDEN\_COLUMN | VARCHAR2(3) |  | 标识该列是否是隐藏列，取值范围\[YES, NO\] |
| VIRTUAL\_COLUMN | VARCHAR2(3) |  | 表示该列是否是虚拟列，取值范围\[YES, NO\] |
| SEGMENT\_COLUMN\_ID | NUMBER |  | 仅列名兼容。返回NULL。 |
| INTERNAL\_COLUMN\_ID | NUMBER |  | 该列的内部序号 |
| HISTOGRAM | VARCHAR2(15) |  | 仅列名兼容。返回NULL。 |
| QUALIFIED\_COL\_NAME | VARCHAR2(4000) |  | 限定列名。默认值同COLUMN\_NAME。 |
| USER\_GENERATED | VARCHAR2(3) |  | 仅列名兼容。返回YES。 |
| DEFAULT\_ON\_NULL | VARCHAR2(3) |  | 标识列是否具有”DEFAULT ON NULL”语义，取值范围\[YES, NO\] |
| IDENTITY\_COLUMN | VARCHAR2(3) |  | 标识该列是否是标识列，取值范围\[YES, NO\] |
| EVALUATION\_EDITION | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| UNUSABLE\_BEFORE | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| UNUSABLE\_BEGINNING | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| ATTCOLLATION | VARCHAR2(100) |  | 列的排序规则，仅适用于字符类型的列 |
| COLLATED\_COLUMN\_ID | NUMBER |  | 仅列名兼容。返回NULL。 |

备注：

- ATTCOLLATION字段说明：在Oracle中对应列名为COLLATION。但是collation在瀚高数据库中被设置为保留关键字，不能用作列名，因此使用ATTCOLLATION代替。

## ALL\_TAB\_COLS

描述当前用户可以访问的所有表、视图的列的相关信息。查询结果是dba\_tab\_cols的一个子集。

该视图在V9.0.5及以后的版本中支持。

## USER\_TAB\_COLS

描述当前用户拥有的所有表、视图的列的相关信息。查询结果是all\_tab\_cols的一个子集，不包含owner列。

该视图在V9.0.5及以后的版本中支持。

## DBA\_TAB\_COLUMNS

描述当前数据库中的所有表、视图的列相关信息。相较于dba\_tab\_cols视图，少了hidden\_column、virtual\_column、segment\_column\_id、internal\_column\_id、qualified\_col\_name、user\_generated和collation\_column\_id列；此外，dba\_tab\_columns视图不包含隐藏列和虚拟列，只包含用户自定义列。

该视图在V9.0.5及以后的版本中支持。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) |  | 表或视图的所有者 |
| TABLE\_NAME | VARCHAR2(128) |  | 表或视图名 |
| COLUMN\_NAME | VARCHAR2(128) |  | 列名 |
| DATA\_TYPE | VARCHAR2(128) |  | 列的数据类型 |
| DATA\_TYPE\_MOD | VARCHAR2(3) |  | 列的数据类型修饰符 |
| DATA\_TYPE\_OWNER | VARCHAR2(128) |  | 列类型拥有者 |
| DATA\_LENGTH | NUMBER |  | 列长度(B) |
| DATA\_PRECISION | NUMBER |  | 数据精度 |
| DATA\_SCALE | NUMBER |  | 数字中小数点右侧的位数 |
| NULLABLE | VARCHAR2(1) |  | 标识列是否允许为空值 |
| COLUMN\_ID | NUMBER |  | 列的创建顺序号 |
| DEFAULT\_LENGTH | NUMBER |  | 列的默认值长度 |
| DATA\_DEFAULT | LONG |  | 列的默认值 |
| NUM\_DISTINCT | NUMBER |  | 仅列名兼容。返回NULL。 |
| LOW\_VALUE | RAW(1000) |  | 仅列名兼容。返回NULL。 |
| HIGH\_VALUE | RAW(1000) |  | 仅列名兼容。返回NULL。 |
| DENSITY | NUMBER |  | 仅列名兼容。返回NULL。 |
| NUM\_NULLS | NUMBER |  | 列中空值的数量，即该列为空的数据行的数量 |
| NUM\_BUCKETS | NUMBER |  | 仅列名兼容。返回NULL。 |
| LAST\_ANALYZED | DATE |  | 最近一次ANALYZE的时间 |
| SAMPLE\_SIZE | NUMBER |  | 仅列名兼容。返回NULL。 |
| CHARACTER\_SET\_NAME | VARCHAR2(44) |  | 字符集名称 |
| CHAR\_COL\_DECL\_LENGTH | NUMBER |  | 字符类型列的声明长度 |
| GLOBAL\_STATS | VARCHAR2(3) |  | 仅列名兼容。返回YES。 |
| USER\_STATS | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| AVG\_COL\_LEN | NUMBER |  | 列平均长度(B) |
| CHAR\_LENGTH | NUMBER |  | 字符类型列的长度，仅适用于以下类型： CHAR, VARCHAR2, NCHAR, NVARCHAR2 |
| CHAR\_USED | VARCHAR2(1) |  | 标识列使用的是字节长度B或者字符长度C，取值范围\[B, C\]，仅适用于以下类型： CHAR, VARCHAR2, NCHAR, NVARCHAR2 |
| V80\_FMT\_IMAGE | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| DATA\_UPGRADED | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| HISTOGRAM | VARCHAR2(15) |  | 仅列名兼容。返回NULL。 |
| DEFAULT\_ON\_NULL | VARCHAR2(3) |  | 标识列是否具有”DEFAULT ON NULL”语义，取值范围\[YES, NO\] |
| IDENTITY\_COLUMN | VARCHAR2(3) |  | 标识该列是否是标识列，取值范围\[YES, NO\] |
| EVALUATION\_EDITION | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| UNUSABLE\_BEFORE | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| UNUSABLE\_BEGINNING | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| ATTCOLLATION | VARCHAR2(100) |  | 列的排序规则，仅适用于字符类型的列 |

备注：

- ATTCOLLATION字段说明：在Oracle中对应列名为COLLATION。但是collation在瀚高数据库中被设置为保留关键字，不能用作列名，因此使用ATTCOLLATION代替。

## ALL\_TAB\_COLUMNS

描述当前用户可以访问的所有表、视图的列相关信息。查询结果是dba\_tab\_columns的一个子集。

该视图在V9.0.5及以后的版本中支持。

## USER\_TAB\_COLUMNS

描述当前用户拥有的所有表、视图的列相关信息。查询结果是all\_tab\_columns的一个子集，不包含owner列。

该视图在V9.0.5及以后的版本中支持。

## DBA\_TAB\_COMMENTS

描述当前数据库中的所有表和视图的注释信息。该视图在V9.0.5及以后的版本中支持。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) |  | 对象拥有者 |
| TABLE\_NAME | VARCHAR2(128) |  | 对象名 |
| TABLE\_TYPE | VARCHAR2(4000) |  | 对象类型 |
| COMMENTS | VARCHAR2(4000) |  | 对象注释信息 |
| ORIGIN\_CON\_ID | NUMBER |  | 仅列名兼容。返回NULL。 |

## ALL\_TAB\_COMMENTS

描述当前用户可以访问的所有表和视图的注释信息。查询结果是dba\_tab\_comments的一个子集。

该视图在V9.0.5及以后的版本中支持。

## USER\_TAB\_COMMENTS

描述当前用户拥有的所有表和视图的注释信息。查询结果是all\_tab\_comments的一个子集，不包含owner列。

该视图在V9.0.5及以后的版本中支持。

## DBA\_INDEXES

描述当前数据库中的所有索引的相关信息。

该视图在V9.0.5及以后的版本中支持。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) |  | 索引拥有者 |
| INDEX\_NAME | VARCHAR2(128) |  | 索引名 |
| INDEX\_TYPE | VARCHAR2(27) |  | 索引类型 |
| TABLE\_OWNER | VARCHAR2(128) |  | 被索引的表的拥有者 |
| TABLE\_NAME | VARCHAR2(128) |  | 被索引的表的表名 |
| TABLE\_TYPE | VARCHAR2(17) |  | 被索引的表的类型 |
| UNIQUENESS | VARCHAR2(9) |  | 标识是否是唯一索引，取值范围\[UNIQUE, NONUNIQUE\] |
| COMPRESSION | VARCHAR2(13) |  | 索引压缩的类型，可选值：ENABLED、ADVANCED HIGH、ADVANCED LOW、DISABLED |
| PREFIX\_LENGTH | NUMBER |  | 仅列名兼容。返回NULL。 |
| TABLESPACE\_NAME | VARCHAR2(30) |  | 索引所在的TABLESPACE名 |
| INI\_TRANS | NUMBER |  | 仅列名兼容。返回NULL。 |
| MAX\_TRANS | NUMBER |  | 仅列名兼容。返回NULL。 |
| INITIAL\_EXTENT | NUMBER |  | 仅列名兼容。返回NULL。 |
| NEXT\_EXTENT | NUMBER |  | 仅列名兼容。返回NULL。 |
| MIN\_EXTENTS | NUMBER |  | 仅列名兼容。返回NULL。 |
| MAX\_EXTENTS | NUMBER |  | 仅列名兼容。返回NULL。 |
| PCT\_INCREASE | NUMBER |  | 仅列名兼容。返回NULL。 |
| PCT\_THRESHOLD | NUMBER |  | 仅列名兼容。返回NULL。 |
| INCLUDE\_COLUMN | NUMBER |  | 仅列名兼容。返回NULL。 |
| FREELISTS | NUMBER |  | 仅列名兼容。返回NULL。 |
| FREELIST\_GROUPS | NUMBER |  | 仅列名兼容。返回NULL。 |
| PCT\_FREE | NUMBER |  | 块中空闲空间的最小百分比 |
| LOGGING | VARCHAR2(3) |  | 标识索引的修改是否需要记录WAL，取值范围\[YES, NO\] |
| BLEVEL | NUMBER |  | 仅列名兼容。返回NULL。 |
| LEAF\_BLOCKS | NUMBER |  | 仅列名兼容。返回NULL。 |
| DISTINCT\_KEYS | NUMBER |  | 仅列名兼容。返回NULL。 |
| AVG\_LEAF\_BLOCKS\_PER\_KEY | NUMBER |  | 仅列名兼容。返回NULL。 |
| AVG\_DATA\_BLOCKS\_PER\_KEY | NUMBER |  | 仅列名兼容。返回NULL。 |
| CLUSTERING\_FACTOR | NUMBER |  | 仅列名兼容。返回NULL。 |
| STATUS | VARCHAR2(8) |  | 标识非分区索引是否有效，取值范围\[VALID, UNUSABLE\] |
| NUM\_ROWS | NUMBER |  | 索引的行数。对于位图索引，此列为不同键值的数量 |
| SAMPLE\_SIZE | NUMBER |  | 仅列名兼容。返回NULL。 |
| LAST\_ANALYZED | DATE |  | 最近一次对该索引进行ANALYZE的时间。默认值为被索引的表的LAST\_ANALYZED。 |
| DEGREE | VARCHAR2(40) |  | 仅列名兼容。返回NULL。 |
| INSTANCES | VARCHAR2(40) |  | 仅列名兼容。返回NULL。 |
| PARTITIONED | VARCHAR2(3) |  | 标识索引是否分区，取值范围\[YES, NO\] |
| TEMPORARY | VARCHAR2(1) |  | 标识索引是否建在临时表上的，取值范围\[Y, N\] |
| GENERATED | VARCHAR2(1) |  | 仅列名兼容。返回N。 |
| SECONDARY | VARCHAR2(1) |  | 仅列名兼容。返回N。 |
| BUFFER\_POOL | VARCHAR2(7) |  | 仅列名兼容。返回NULL。 |
| FLASH\_CACHE | VARCHAR2(7) |  | 仅列名兼容。返回NULL。 |
| CELL\_FLASH\_CACHE | VARCHAR2(7) |  | 仅列名兼容。返回NULL。 |
| USER\_STATS | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| DURATION | VARCHAR2(15) |  | 标识索引的生命周期。SYS$SESSION：在整个回话期间保留行；SYS$TRANSACTION：事务提交后删除行；NULL-普通表 |
| PCT\_DIRECT\_ACCESS | NUMBER |  | 仅列名兼容。返回NULL。 |
| ITYP\_OWNER | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| ITYP\_NAME | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| PARAMETERS | VARCHAR2(1000) |  | 仅列名兼容。返回NULL。 |
| GLOBAL\_STATS | VARCHAR2(3) |  | 仅列名兼容。返回YES。 |
| DOMIDX\_STATUS | VARCHAR2(12) |  | 仅列名兼容。返回NULL。 |
| DOMIDX\_OPSTATUS | VARCHAR2(6) |  | 仅列名兼容。返回NULL。 |
| FUNCIDX\_STATUS | VARCHAR2(8) |  | 函数索引的状态。NULL：非函数索引；ENABLED：启用函数索引；DISABLED：禁用函数索引 |
| JOIN\_INDEX | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| IOT\_REDUNDANT\_PKEY\_ELIM | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| DROPPED | VARCHAR2(3) |  | YES表示索引已经被删除但是还在回收站中，NO表示未被删除。分区表索引为NULL |
| VISIBILITY | VARCHAR2(9) |  | 标识索引是否对优化器可见，取值范围\[VISIBLE, INVISIBLE\] |
| DOMIDX\_MANAGEMENT | VARCHAR2(14) |  | 仅列名兼容。返回NULL。 |
| SEGMENT\_CREATED | VARCHAR2(3) |  | 仅列名兼容。返回NULL。 |
| ORPHANED\_ENTRIES | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| INDEXING | VARCHAR2(7) |  | 仅列名兼容。返回NULL。 |
| AUTO | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| CONSTRAINT\_INDEX | VARCHAR2(3) |  | 标识该索引是否作为约束的一部分被创建，取值范围\[YES, NO\] |

备注：

- COMPRESSION字段取值说明：如果创建索引时添加了with (deduplicate\_items  
	\= yes)子句，则该字段取值为DEDUPLICATE，否则该字段取值为DISABLED。
- PCT\_FREE字段取值说明：如果在建表时通过with (fillfactor =  
	n)指定了填充因子，则该字段取值为100 - n；否则该字段取值为0

## ALL\_INDEXES

描述当前用户可以访问的所有索引的相关信息。查询结果是dba\_indexes的一个子集。

该视图在V9.0.5及以后的版本中支持。

## USER\_INDEXES

描述当前用户拥有的所有索引的相关信息。该视图不显示owner列。

该视图在V9.0.5及以后的版本中支持。

## DBA\_IND\_COLUMNS

描述当前数据库中的所有表上的索引列信息。

该视图在V9.0.5及以后的版本中支持。

---

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| INDEX\_OWNER | VARCHAR2(128) |  | 索引拥有者 |
| INDEX\_NAME | VARCHAR2(128) |  | 索引名 |
| TABLE\_OWNER | VARCHAR2(128) |  | 表的拥有者 |
| TABLE\_NAME | VARCHAR2(128) |  | 表名 |
| COLUMN\_NAME | VARCHAR2(4000) |  | 列名或者列属性。 如果在用户定义的REF列上创建索引，系统会在组成REF列的属性上创建索引，因此，该视图中列将以”REF\_NAME”.”ATTRIBUTE”格式显示 |
| COLUMN\_POSITION | NUMBER |  | 列或属性在索引中的位置 |
| COLUMN\_LENGTH | NUMBER |  | 列的索引长度 |
| CHAR\_LENGTH | NUMBER |  | 列的最大码位长度 |
| DESCEND | VARCHAR2(4) |  | 标识该列是按照降序(DESC)还是升序(ASC)排序 |
| COLLATED\_COLUMN\_ID | NUMBER |  | 为该列提供排序规则的内部序列号 |

---

## ALL\_IND\_COLUMNS

描述当前用户可以访问的所有表上的索引列信息。查询结果是dba\_ind\_columns的一个子集。

该视图在V9.0.5及以后的版本中支持。

## USER\_IND\_COLUMNS

描述当前用户拥有的所有表上的索引列信息。查询结果是all\_ind\_columns的一个子集，不包含index\_owner和table\_owner列。

该视图在V9.0.5及以后的版本中支持。

## DBA\_DEPENDENCIES

描述当前数据库中的所有对象间的依赖信息。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) |  | 对象所有者 |
| NAME | VARCHAR2(256) |  | 对象名 |
| TYPE | VARCHAR2(32) |  | 对象类型 |
| REFERENCED\_OWNER | VARCHAR2(128) |  | 被引用对象的拥有者 |
| REFERENCED\_NAME | VARCHAR2(256) |  | 被引用对象的名称 |
| REFERENCED\_TYPE | VARCHAR2(32) |  | 被引用对象的类型 |
| REFERENCED\_LINK\_NAME | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| DEPENDENCY\_TYPE | VARCHAR2(4) |  | 标识该依赖是否为引用依赖。REF表示是引用依赖，HARD表示硬依赖 |

备注：

- DEPENDENCY\_TYPE字段取值：pg\_depend.deptype字段作用和该字段较为类似，但取值范围和含义不同。

## ALL\_DEPENDENCIES

描述当前用户可以访问的所有对象间的依赖信息。查询结果是dba\_dependencies的一个子集。

该视图在V9.0.5及以后的版本中支持。

## USER\_DEPENDENCIES

描述当前用户拥有的所有对象间的依赖信息。该视图不显示owner列。

该视图在V9.0.5及以后的版本中支持。

## DBA\_OBJECTS

描述当前数据库中的所有对象的相关信息。

该视图在V9.0.5及以后的版本中支持。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) |  | 对象拥有者 |
| OBJECT\_NAME | VARCHAR2(128) |  | 对象名 |
| SUBOBJECT\_NAME | VARCHAR2(128) |  | 子对象名，比如分区表 |
| OBJECT\_ID | NUMBER |  | 对象在数据字典中的唯一标识 |
| DATA\_OBJECT\_ID | NUMBER |  | 包含对象的SEGMENT的字典对象ID，仅对存储数据的对象有效，比如索引、表 |
| OBJECT\_TYPE | VARCHAR2(32) |  | 对象类型，比如：TABLE、INDEX、VIEW |
| CREATED | DATE |  | 对象的创建时间，格式：DD-MM-YY |
| LAST\_DDL\_TIME | DATE |  | 最后一次DDL操作的时间，包括GRANTS、REVOKES，格式：DD-MM-YY |
| TIMESTAMP | VARCHAR2(19) |  | 对象定义的精确时间，格式：YYYY-MM-DD-HH24-MI-SS |
| STATUS | VARCHAR2(7) |  | 对象状态，可选值：VALID、INVALID、N/A |
| TEMPORARY | VARCHAR2(1) |  | 标识是否是临时对象，取值范围\[Y, N\] |
| GENERATED | VARCHAR2(1) |  | 仅列名兼容。返回N。 |
| SECONDARY | VARCHAR2(1) |  | 仅列名兼容。返回N。 |
| NAMESPACE | NUMBER |  | 对象命名空间 |
| EDITION\_NAME | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| SHARING | VARCHAR2(18) |  | 仅列名兼容。返回NULL。 |
| EDITIONABLE | VARCHAR2(1) |  | 可选值： Y：对象标记为EDITIONABLE N：对象标记为NONEDITIONABLE NULL：对于数据库中不可版本化的对象类型。仅适用于PACKAGE。 |
| ORACLE\_MAINTAINED | VARCHAR2(1) |  | 仅列名兼容。返回N。 |
| APPLICATION | VARCHAR2(1) |  | 仅列名兼容。返回N。 |
| DEFAULT\_COLLATION | VARCHAR2(100) |  | 对象的默认排序规则 |
| DUPLICATED | VARCHAR2(1) |  | 仅列名兼容。返回N。 |
| SHARDED | VARCHAR2(1) |  | 仅列名兼容。返回N。 |
| IMPORTED\_OBJECT | VARCHAR2(1) |  | 仅列名兼容。返回N。 |
| CREATED\_APPID | NUMBER |  | 仅列名兼容。返回NULL。 |
| CREATED\_VSNID | NUMBER |  | 仅列名兼容。返回NULL。 |
| MODIFIED\_APPID | NUMBER |  | 仅列名兼容。返回NULL。 |
| MODIFIED\_VSNID | NUMBER |  | 仅列名兼容。返回NULL。 |

备注：

- editionable字段仅在对象类型为package时有效，其他不支持的字段如果在Oracle  
	21C中有取值范围，则根据实际情况赋默认值；如果没有默认值，则设置为空值。
- 支持的对象类型包括：TABLE、TABLE PARTITION、TABLE  
	SUBPARTITION、INDEX、INDEX PARTITION、INDEX  
	SUBPARTITION、VIEW、MATERIALIZED VIEW、SEQUENCE、FOREIGN  
	TABLE、TOAST TABLE、COMPOSITE TYPE、FUNCTION、PROCEDURE、WINDOW  
	FUNCTION、AGGREGATE FUNCTION、PACKAGE、PACKAGE  
	BODY、TYPE、JOB、DBLINK、TRIGGER、SCHEMA、SYNONYM、EXTENSION、LANGUAGE、CONSTRAINT、OPERATOR、DATABASE、TABLESPACE，其中TOAST  
	TABLE、EXTENSION、DATABASE、TABLESPACE、LANGUAGE、WINDOW  
	FUNCTION、AGGREGATE FUNCTION为HGDB V9特有的对象类型。
- status字段取值说明：对于proc类型，取值参考pg\_prostatus字段。
- created、last\_ddl\_time、timestamp字段取值说明：这三个字段仅当对象在pg\_object系统表中有记录时取有效值，其他情况下设置为空值。

## ALL\_OBJECTS

描述当前用户可以访问的所有对象的相关信息。查询结果是dba\_objects的一个子集。该视图在V9.0.5及以后的版本中支持。

## USER\_OBJECTS

描述当前用户拥有的所有对象的相关信息。查询结果是dba\_objects的一个子集，但是该视图不展示owner列。

该视图在V9.0.5及以后的版本中支持。

## DBA\_TYPES

描述当前数据库中的所有类型的相关信息。

该视图在V9.0.5及以后的版本中支持。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) |  | 类型拥有者 |
| TYPE\_NAME | VARCHAR2(128) |  | 类型名称 |
| TYPE\_OID | RAW(16) |  | 类型OID |
| TYPECODE | VARCHAR2(128) |  | 类型的类型代码，可选的值包括：OBJECT、COLLECTION、JAVA、PL/SQL、TABLE、XML、ANYDATA、ANYDATASET、ANYTYPE |
| ATTRIBUTES | NUMBER |  | 类型中的属性数量 |
| METHODS | NUMBER |  | 类型中的方法数量 |
| PREDEFINED | VARCHAR2(3) |  | 标识是否是预定义类型，取值范围\[YES, NO\] |
| INCOMPLETE | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| FINAL | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| INSTANTABLE | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| PERSISTABLE | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| SUPERTYPE\_OWNER | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| SUPERTYPE\_NAME | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| LOCAL\_ATTRIBUTES | NUMBER |  | 仅列名兼容。返回NULL。 |
| LOCAL\_METHODS | NUMBER |  | 仅列名兼容。返回NULL。 |
| TYPEID | RAW(16) |  | 类型的类型ID |

备注：

- predefined字段通过类型的oid来进行区分，oid小于32767则认为是预定义类型。
- typecode字段取值为upper(pg\_type.typname)。

## ALL\_TYPES

描述当前用户可以访问的所有类型的相关信息。查询结果是dba\_types的一个子集。

该视图在V9.0.5及以后的版本中支持。

## USER\_TYPES

描述当前用户拥有的所有类型的相关信息。查询结果是all\_types的一个子集，不包含owner列。

该视图在V9.0.5及以后的版本中支持。

## DBA\_USERS

描述当前数据库中的所有用户信息。

该视图在V9.0.5及以后的版本中支持。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| USERNAME | VARCHAR2(128) |  | 用户名称 |
| USER\_ID | NUMBER |  | 用户ID |
| PASSWORD | VARCHAR2(4000) |  | 仅列名兼容。返回NULL。 |
| ACCOUNT\_STATUS | VARCHAR2(32) |  | 账户状态 |
| LOCK\_DATE | DATE |  | 如果ACCOUNT\_STATUS为LOCKED，标识账户锁定的时间 |
| EXPIRY\_DATE | DATE |  | 仅列名兼容。返回NULL。 |
| DEFAULT\_TABLESPACE | VARCHAR2(30) |  | 仅列名兼容。返回NULL。 |
| TEMPORARY\_TABLESPACE | VARCHAR2(30) |  | 仅列名兼容。返回NULL。 |
| LOCAL\_TEMP\_TABLESPACE | VARCHAR2(30) |  | 仅列名兼容。返回NULL。 |
| CREATED | DATE |  | 仅列名兼容。返回NULL。 |
| PROFILE | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| INITIAL\_RSRC\_CONSUMER\_GROUP | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| EXTERNAL\_NAME | VARCHAR2(4000) |  | 仅列名兼容。返回NULL。 |
| PASSWORD\_VERSION | VARCHAR2(12) |  | 仅列名兼容。返回NULL。 |
| EDITIONS\_ENABLE | VARCHAR2(1) |  | 仅列名兼容。返回N。 |
| AUTHENTICATION\_TYPE | VARCHAR2(8) |  | 表示用户的认证机制类型 |
| PROXY\_ONLY\_CONNECT | VARCHAR2(1) |  | 仅列名兼容。返回NULL。 |
| COMMON | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| LAST\_LOGIN | TIMESTAMP WITH TIME ZONE |  | 仅列名兼容。返回NULL。 |
| ORACLE\_MAINTAINED | VARCHAR2(1) |  | 仅列名兼容。返回N。 |
| INHERITED | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| DEFAULT\_COLLATION | VARCHAR2(100) |  | 仅列名兼容。返回NULL。 |
| IMPLICIT | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| ALL\_SHARD | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| EXTERNAL\_SHARD | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| PASSWORD\_CHANGE\_DATE | DATE |  | 仅列名兼容。返回NULL。 |
| MANDATORY\_PROFILE\_VIOLATION | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |

备注：

- account\_status字段根据pg\_user.valuntil字段和当前系统时间进行判断，若密码未过期，则状态为OPEN。

## ALL\_USERS

描述当前用户可见的数据库的所有用户信息。

该视图在V9.0.5及以后的版本中支持。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| USERNAME | VARCHAR2(128) |  | 用户名 |
| USER\_ID | NUMBER |  | 用户ID |
| CREATED | DATE |  | 仅列名兼容。 |
| COMMON | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| ORACLE\_MAINTAINED | VARCHAR2(1) |  | 仅列名兼容。返回N。 |
| INHERITED | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| DEFAULT\_COLLATION | VARCHAR2(100) |  | 仅列名兼容。返回NULL。 |
| IMPLICIT | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| ALL\_SHARD | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| EXTERNAL\_SHARD | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |

## USER\_USERS

描述当前用户的详细信息。

该视图在V9.0.5及以后的版本中支持。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| USERNAME | VARCHAR2(128) |  | 用户账户名 |
| USER\_ID | NUMBER |  | 用户账户ID |
| ACCOUNT\_STATUS | VARCHAR2(32) |  | 用户账户状态 |
| LOCK\_DATE | DATE |  | 仅列名兼容。返回NULL。 |
| EXPIRY\_DATE | DATE |  | 仅列名兼容。返回NULL。 |
| DEFAULT\_TABLESPACE | VARCHAR2(30) |  | 仅列名兼容。返回NULL。 |
| TEMPORARY\_TABLESPACE | VARCHAR2(30) |  | 仅列名兼容。返回NULL。 |
| LOCAL\_TEMP\_TABLESPACE | VARCHAR2(30) |  | 仅列名兼容。返回NULL。 |
| CREATED | DATE |  | 仅列名兼容。返回NULL。 |
| INITIAL\_RSRC\_CONSUMER\_GROUP | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| EXTERNAL\_NAME | VARCHAR2(4000) |  | 仅列名兼容。返回NULL。 |
| PROXY\_ONLY\_CONNECT | VARCHAR2(1) |  | 仅列名兼容。返回NULL。 |
| COMMON | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| ORACLE\_MAINTAINED | VARCHAR2(1) |  | 仅列名兼容。返回N。 |
| INHERITED | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| DEFAULT\_COLLATION | VARCHAR2(100) |  | 仅列名兼容。返回NULL。 |
| IMPLICIT | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| ALL\_SHARD | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| EXTERNAL\_SHARD | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| PASSWORD\_CHANGE\_DATE | DATE |  | 仅列名兼容。返回NULL。 |
| MANDATORY\_PROFILE\_VIOLATION | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |

## DBA\_CONSTRAINTS

描述当前数据库中的所有表上的约束定义。

该视图在V9.0.5及以后的版本中支持。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) |  | 约束定义的拥有者 |
| CONSTRAINT\_NAME | VARCHAR2(128) |  | 约束名称 |
| CONSTRAINT\_TYPE | VARCHAR2(1) |  | 约束的类型 |
| TABLE\_NAME | VARCHAR2(128) |  | 与包含约束定义的表相关联的表名称 |
| SEARCH\_CONDITION | LONG |  | 检查约束的搜索条件文本 |
| SEARCH\_CONDITION\_VC | VARCHAR2(4000) |  | 检查约束的搜索条件文本，可能会产生截断 |
| R\_OWNER | VARCHAR2(128) |  | 被引用约束中引用的表的拥有者 |
| R\_CONSTRAINT\_NAME | VARCHAR2(128) |  | 被引用表的唯一约束定义名称 |
| DELETE\_RULE | VARCHAR2(11) |  | 删除引用约束的规则，可选值：CASCADE、SET NULL、NO ACTION |
| STATUS | VARCHAR2(8) |  | 仅列名兼容。返回ENABLED。 |
| CONDEFERRABLE | VARCHAR2(14) |  | 标识该约束是否可延迟的，取值范围\[DEFERRABLE, NOT DEFERRABLE\] |
| DEFERRED | VARCHAR2(9) |  | 标识该约束是否初始设置为延迟检查：延迟(DEFERRED)或立即检查(IMMEDIATE) |
| VALIDATED | VARCHAR2(13) |  | 当STATUS=ENABLED时，取值说明如下： VALIDATE：已验证，所有数据均符合约束条件；NOT VALIDATE：未验证，数据可能不完全符合约束条件 当STATUS=DISABLED时，取值说明如下： VALIDATE：已验证，所有数据均符合约束条件，但约束上的唯一索引已被删除；NOT VALIDATE：未验证，数据可能不完全符合约束条件 |
| GENERATED | VARCHAR2(14) |  | 仅列名兼容。返回USER NAME。 |
| BAD | VARCHAR2(3) |  | 仅列名兼容。返回NULL。 |
| RELY | VARCHAR2(4) |  | 仅列名兼容。返回NULL。 |
| LAST\_CHANGE | DATE |  | 仅列名兼容。返回NULL。 |
| INDEX\_OWNER | VARCHAR2(128) |  | 索引拥有者 |
| INDEX\_NAME | VARCHAR2(128) |  | 索引名称，仅适用于UNIQUE或者主键约束 |
| INVALID | VARCHAR2(7) |  | 标识该约束是否失效：失效(INVALID)或者有效(NULL) |
| VIEW\_RELATED | VARCHAR2(14) |  | 仅列名兼容。返回NULL。 |
| ORIGIN\_CON\_ID | NUMBER |  | 仅列名兼容。返回NULL。 |

备注：

- CONDEFERRABLE字段说明：该字段在Oracle中对应为deferrable。在瀚高数据库中deferrable被设置为保留关键字，不能用作列名，使用condeferrable代替。

## ALL\_CONSTRAINTS

描述当前用户可以访问的所有表上的约束定义。查询结果是dba\_constraints的一个子集。该视图在V9.0.5及以后的版本中支持。

## USER\_CONSTRAINTS

描述当前用户拥有的表上的约束定义。查询结果是all\_constraints的一个子集。

该视图在V9.0.5及以后的版本中支持。

## DBA\_CONS\_COLUMNS

描述当前数据库中的所有被约束引用的列。

该视图在V9.0.5及以后的版本中支持。

---

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) |  | 约束定义的拥有者 |
| CONSTRAINT\_NAME | VARCHAR2(128) |  | 约束定义的名称 |
| TABLE\_NAME | VARCHAR2(128) |  | 约束定义所属表的名称 |
| COLUMN\_NAME | VARCHAR2(128) |  | 约束定义中指定的对象类型列(或属性)的名称 |
| POSITION | NUMBER |  | 对象定义中列的位置 |

---

## ALL\_CONS\_COLUMNS

描述当前用户可以访问的被约束引用的列。查询结果是dba\_cons\_conlumns的一个子集。

该视图在V9.0.5及以后的版本中支持。

## USER\_CONS\_COLUMNS

描述当前用户拥有的被约束引用的列。查询结果是all\_cons\_columns的一个子集。

该视图在V9.0.5及以后的版本中支持。

## DBA\_TAB\_PRIVS

描述当前数据库中的所有对象的授权信息。

该视图在V9.0.5及以后的版本中支持。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| GRANTEE | VARCHAR2(128) |  | 被授予访问权限的用户名或角色名 |
| OWNER | VARCHAR2(128) |  | 对象拥有者 |
| TABLE\_NAME | VARCHAR2(128) |  | 对象名 |
| GRANTOR | VARCHAR2(128) |  | 执行授权操作的用户名称 |
| PRIVILEGE | VARCHAR2(40) |  | 对象权限 |
| GRANTABLE | VARCHAR2(3) |  | 标识该权限是否通过’GRANT OPTION’授予 |
| HIERARCHY | VARCHAR2(3) |  | 标识该权限是否通过’HIERARCHY OPTION’授予 |
| COMMON | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| TYPE | VARCHAR2(24) |  | 对象类型 |
| INHERITED | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |

## ALL\_TAB\_PRIVS

描述权限授予情况。包括以下类型的授权：

1. 当前用户作为对象所有者(OWNER)、授权者(GRANTOR)或者被授权者(GRANTEE)的对象授权。
2. 已启用的角色或者PUBLIC作为被授权者的对象授权。

该视图在V9.0.5及以后的版本中支持。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| GRANTOR | VARCHAR2(128) |  | 执行授权操作的用户名称 |
| GRANTEE | VARCHAR2(128) |  | 被授予访问权限的用户名或角色名 |
| TABLE\_SCHEMA | VARCHAR2(128) |  | 对象所属的SCHEMA |
| TABLE\_NAME | VARCHAR2(128) |  | 对象名 |
| PRIVILEGE | VARCHAR2(40) |  | 对象权限 |
| GRANTABLE | VARCHAR2(3) |  | 标识该权限是否通过’GRANT OPTION’授予 |
| HIERARCHY | VARCHAR2(3) |  | 标识该权限是否通过’HIERARCHY OPTION’授予 |
| COMMON | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| TYPE | VARCHAR2(24) |  | 对象类型 |
| INHERITED | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |

## USER\_TAB\_PRIVS

描述当前用户作为对象所有者、授权者或被授权者的对象权限。该视图定义和dba\_tab\_privs定义一致。

该视图在V9.0.5及以后的版本中支持。

## DBA\_TAB\_PARTITIONS

描述当前数据库中的所有分区的相关信息。

该视图在V9.0.5及以后的版本中支持。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| TABLE\_OWNER | VARCHAR2(128) |  | 表的所有者 |
| TABLE\_NAME | VARCHAR2(128) |  | 表名 |
| COMPOSITE | VARCHAR2(3) |  | 标识该表是否为复合分区表，取值范围\[YES, NO\] |
| PARTITION\_NAME | VARCHAR2(128) |  | 分区名 |
| SUBPARTITION\_COUNT | NUMBER |  | 如果是复合分区表，该列值为分区中子分区的数目 |
| HIGH\_VALUE | LONG |  | 分区边界值表达式 |
| HIGH\_VALUE\_LENGTH | NUMBER |  | 分区边界值表达式的长度 |
| PARTITION\_POSITION | NUMBER |  | 分区在表中的位置 |
| TABLESPACE\_NAME | VARCHAR2(30) |  | 分区所在的表空间名 |
| PCT\_FREE | NUMBER |  | 块中最小空闲空间百分比 |
| PCT\_USED | NUMBER |  | 仅列名兼容。返回NULL。 |
| INI\_TRANS | NUMBER |  | 仅列名兼容。返回NULL。 |
| MAX\_TRANS | NUMBER |  | 仅列名兼容。返回为NULL。 |
| INITIAL\_EXTENT | NUMBER |  | 仅列名兼容。返回NULL。 |
| NEXT\_EXTENT | NUMBER |  | 仅列名兼容。返回NULL。 |
| MIN\_EXTENT | NUMBER |  | 仅列名兼容。返回NULL。 |
| MAX\_EXTENT | NUMBER |  | 仅列名兼容。返回NULL。 |
| MAX\_SIZE | NUMBER |  | 仅列名兼容。返回NULL。 |
| PCT\_INCREASE | NUMBER |  | 仅列名兼容。返回NULL。 |
| FREELISTS | NUMBER |  | 仅列名兼容。返回NULL。 |
| FREELIST\_GROUPS | NUMBER |  | 仅列名兼容。返回NULL。 |
| LOGGING | VARCHAR2(3) |  | 标识表是否是UNLOGGED表，取值范围\[YES, NO\]。分区表父表该字段为空 |
| COMPRESSION | VARCHAR2(8) |  | 仅列名兼容。返回DISABLED。 |
| COMPRESS\_FOR | VARCHAR2(30) |  | 仅列名兼容。返回NULL。 |
| NUM\_ROWS | NUMBER |  | 表中数据的行数 |
| BLOCKS | NUMBER |  | 表中数据块的数量 |
| EMPTY\_BLOCKS | NUMBER |  | 仅列名兼容。返回NULL。 |
| AVG\_SPACE | NUMBER |  | 仅列名兼容。返回NULL。 |
| CHAIN\_CNT | NUMBER |  | 仅列名兼容。返回NULL。 |
| AVG\_ROW\_LEN | NUMBER |  | 表中平均行数据长度(B) |
| SAMPLE\_SIZE | NUMBER |  | 仅列名兼容。返回NULL。 |
| LAST\_ANALYZED | DATE |  | 最近一次ANALYZE的时间 |
| BUFFER\_POOL | VARCHAR2(7) |  | 仅列名兼容。返回NULL。 |
| FLASH\_CACHE | VARCHAR2(7) |  | 仅列名兼容。返回NULL。 |
| CELL\_FLASH\_CACHE | VARCHAR2(7) |  | 仅列名兼容。返回NULL。 |
| GLOBAL\_STATS | VARCHAR2(3) |  | 仅列名兼容。返回YES。 |
| USER\_STATS | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| IS\_NESTED | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| PARENT\_TABLE\_PARTITION | VARCHAR2(128) |  | 仅列名兼容。返回NULL。 |
| INTERVAL | VARCHAR2(3) |  | 仅列名兼容。返回NO。 |
| SEGMENT\_CREATED | VARCHAR2(3) |  | 仅列名兼容。返回NULL。 |
| INDEXING | VARCHAR2(4) |  | 仅列名兼容。返回NULL。 |
| READ\_ONLY | VARCHAR2(3) |  | 仅列名兼容。返回NULL。 |
| INMEMORY | VARCHAR2(8) |  | 仅列名兼容。返回DISABLED。 |
| INMEMORY\_PRIORITY | VARCHAR2(8) |  | 仅列名兼容。返回NULL。 |
| INMEMORY\_DISTRIBUTE | VARCHAR2(15) |  | 仅列名兼容。返回NULL。 |
| INMEMORY\_COMPRESSION | VARCHAR2(17) |  | 仅列名兼容。返回NULL。 |
| INMEMORY\_DUPLICATE | VARCHAR2(13) |  | 仅列名兼容。返回NULL。 |
| CELLMEMORY | VARCHAR2(24) |  | 仅列名兼容。返回NULL。 |
| INMEMORY\_SERVICE | VARCHAR2(12) |  | 仅列名兼容。返回NULL。 |
| INMEMORY\_SERVICE\_NAME | VARCHAR2(1000) |  | 仅列名兼容。返回NULL。 |
| MEMOPTIMIZE\_READ | VARCHAR2(8) |  | 仅列名兼容。返回DISABLED。 |
| MEMOPTIMIZE\_WRITE | VARCHAR2(8) |  | 仅列名兼容。返回NULL。 |

备注：

- pct\_free字段取值说明：如果在建表时通过with (fillfactor =  
	n)指定了填充因子，则该字段取值为100 - n；否则该字段取值为0。

## ALL\_TAB\_PARTITIONS

描述当前用户可以访问的分区的相关信息，查询结果是dba\_tab\_partitions的一个子集。

该视图在V9.0.5及以后的版本中支持。

## USER\_TAB\_PARTITIONS

描述当前用户拥有的分区表的相关信息，该视图不包含all\_tab\_partitions中的table\_owner字段。

该视图在V9.0.5及以后的版本中支持。

## DBA\_TRIGGERS

描述当前数据库中的所有触发器。

该视图在V9.0.5及以后的版本中支持。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) |  | 触发器的所有者 |
| TRIGGER\_NAME | VARCHAR2(128) |  | 触发器的名称 |
| TRIGGER\_TYPE | VARCHAR2(16) |  | 触发器触发的时机:BEFORE STATEMENTBEFORE EACH ROWAFTER STATEMENTAFTER EACH ROWINSTEAD OF |
| TRIGGERING\_EVENT | VARCHAR2(246) |  | 触发触发器的 DML、DDL 或数据库事件 |
| TABLE\_OWNER | VARCHAR2(128) |  | 定义触发器的表的所有者 |
| BASE\_OBJECT\_TYPE | VARCHAR2(18) |  | 定义触发器的基础对象:TABLEVIEW |
| TABLE\_NAME | VARCHAR2(128) |  | 指示定义触发器的表或视图名称 |
| COLUMN\_NAME | VARCHAR2(4000) |  | 嵌套表列的名称（如果是嵌套表触发器），否则为 NULL。由于暂不支持嵌套表，目前仅列名兼容 |
| REFERENCING\_NAMES | VARCHAR2(422) |  | 用于从触发器内部引用 OLD 和 NEW 列值的名称 |
| WHEN\_CLAUSE | VARCHAR2(4000) |  | 显示执行 TRIGGER\_BODY的条件 |
| STATUS | VARCHAR2(8) |  | 触发器是启用 ( ENABLED ) 还是禁用 ( DISABLED )；禁用的触发器将不会触发 |
| DESCRIPTION | VARCHAR2(4000) |  | 触发器描述 |
| ACTION\_TYPE | VARCHAR2(11) |  | trigger body的类型:PL/iSQL |
| TRIGGER\_BODY | LONG |  | 触发器触发时执行的语句 |
| CROSSEDITION | VARCHAR2(7) |  | 仅列名兼容 |
| BEFORE\_STATEMENT | VARCHAR2(3) |  | 指示触发器是否具有 BEFORE STATEMENT 部分（ YES ）或无（ NO ） |
| BEFORE\_ROW | VARCHAR2(3) |  | 指示触发器是否具有 BEFORE EACH ROW 部分（ YES ）或无（ NO ） |
| AFTER\_ROW | VARCHAR2(3) |  | 指示触发器是否具有 AFTER EACH ROW 部分（ YES ）或无（ NO ） |
| AFTER\_STATEMENT | VARCHAR2(3) |  | 指示触发器是否具有AFTER STATEMENT 部分（ YES ）或无（ NO ） |
| INSTEAD\_OF\_ROW | VARCHAR2(3) |  | 指示触发器是否具有 INSTEAD OF 部分（ YES ）或无（ NO ） |
| FIRE\_ONCE | VARCHAR2(3) |  | 显示YES，指示触发器仅在用户进程进行更改时触发 |
| APPLY\_SERVER\_ONLY | VARCHAR2(3) |  | 显示NO，指示触发器不在复制应用或 SQL 应用过程中触发 |

## ALL\_TRIGGERS

描述当前用户可访问的表上的触发器。

该视图在V9.0.5及以后的版本中支持。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | VARCHAR2(128) |  | 触发器的所有者 |
| TRIGGER\_NAME | VARCHAR2(128) |  | 触发器的名称 |
| TRIGGER\_TYPE | VARCHAR2(16) |  | 触发器触发的时机:BEFORE STATEMENTBEFORE EACH ROWAFTER STATEMENTAFTER EACH ROWINSTEAD OF |
| TRIGGERING\_EVENT | VARCHAR2(246) |  | 触发触发器的 DML、DDL 或数据库事件 |
| TABLE\_OWNER | VARCHAR2(128) |  | 定义触发器的表的所有者 |
| BASE\_OBJECT\_TYPE | VARCHAR2(18) |  | 定义触发器的基础对象:TABLEVIEW |
| TABLE\_NAME | VARCHAR2(128) |  | 指示定义触发器的表或视图名称 |
| COLUMN\_NAME | VARCHAR2(4000) |  | 嵌套表列的名称（如果是嵌套表触发器），否则为 NULL。由于暂不支持嵌套表，目前仅列名兼容。 |
| REFERENCING\_NAMES | VARCHAR2(422) |  | 用于从触发器内部引用 OLD 和 NEW 列值的名称 |
| WHEN\_CLAUSE | VARCHAR2(4000) |  | 显示执行 TRIGGER\_BODY的条件 |
| STATUS | VARCHAR2(8) |  | 触发器是启用 ( ENABLED ) 还是禁用 ( DISABLED )；禁用的触发器将不会触发 |
| DESCRIPTION | VARCHAR2(4000) |  | 触发器描述 |
| ACTION\_TYPE | VARCHAR2(11) |  | trigger body的类型:PL/iSQL |
| TRIGGER\_BODY | LONG |  | 触发器触发时执行的语句 |
| CROSSEDITION | VARCHAR2(7) |  | 仅列名兼容 |
| BEFORE\_STATEMENT | VARCHAR2(3) |  | 指示触发器是否具有 BEFORE STATEMENT 部分（ YES ）或无（ NO ） |
| BEFORE\_ROW | VARCHAR2(3) |  | 指示触发器是否具有 BEFORE EACH ROW 部分（ YES ）或无（ NO ） |
| AFTER\_ROW | VARCHAR2(3) |  | 指示触发器是否具有 AFTER EACH ROW 部分（ YES ）或无（ NO ） |
| AFTER\_STATEMENT | VARCHAR2(3) |  | 指示触发器是否具有AFTER STATEMENT 部分（ YES ）或无（ NO ） |
| INSTEAD\_OF\_ROW | VARCHAR2(3) |  | 指示触发器是否具有 INSTEAD OF 部分（ YES ）或无（ NO ） |
| FIRE\_ONCE | VARCHAR2(3) |  | 显示YES，指示触发器仅在用户进程进行更改时触发 |
| APPLY\_SERVER\_ONLY | VARCHAR2(3) |  | 显示NO，指示触发器不在复制应用或 SQL 应用过程中触发 |

## USER\_TRIGGERS

描述当前用户拥有的触发器。此视图不显示 OWNER 列。

该视图在V9.0.5及以后的版本中支持。

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| TRIGGER\_NAME | VARCHAR2(128) |  | 触发器的名称 |
| TRIGGER\_TYPE | VARCHAR2(16) |  | 触发器触发的时机:BEFORE STATEMENTBEFORE EACH ROWAFTER STATEMENTAFTER EACH ROWINSTEAD OF |
| TRIGGERING\_EVENT | VARCHAR2(246) |  | 触发触发器的 DML、DDL 或数据库事件 |
| TABLE\_OWNER | VARCHAR2(128) |  | 定义触发器的表的所有者 |
| BASE\_OBJECT\_TYPE | VARCHAR2(18) |  | 定义触发器的基础对象:TABLEVIEW |
| TABLE\_NAME | VARCHAR2(128) |  | 定义触发器的表或视图名称 |
| COLUMN\_NAME | VARCHAR2(4000) |  | 嵌套表列的名称（如果是嵌套表触发器），否则为 NULL。由于暂不支持嵌套表，目前仅列名兼容 |
| REFERENCING\_NAMES | VARCHAR2(422) |  | 用于从触发器内部引用 OLD 和 NEW 列值的名称 |
| WHEN\_CLAUSE | VARCHAR2(4000) |  | 显示执行 TRIGGER\_BODY的条件 |
| STATUS | VARCHAR2(8) |  | 触发器是启用 ( ENABLED ) 还是禁用 ( DISABLED )；禁用的触发器将不会触发 |
| DESCRIPTION | VARCHAR2(4000) |  | 触发器描述 |
| ACTION\_TYPE | VARCHAR2(11) |  | trigger body的类型:PL/iSQL |
| TRIGGER\_BODY | LONG |  | 触发器触发时执行的语句 |
| CROSSEDITION | VARCHAR2(7) |  | 仅列名兼容 |
| BEFORE\_STATEMENT | VARCHAR2(3) |  | 指示触发器是否具有 BEFORE STATEMENT 部分（ YES ）或无（ NO ） |
| BEFORE\_ROW | VARCHAR2(3) |  | 指示触发器是否具有 BEFORE EACH ROW 部分（ YES ）或无（ NO ） |
| AFTER\_ROW | VARCHAR2(3) |  | 指示触发器是否具有 AFTER EACH ROW 部分（ YES ）或无（ NO ） |
| AFTER\_STATEMENT | VARCHAR2(3) |  | 指示触发器是否具有AFTER STATEMENT 部分（ YES ）或无（ NO ） |
| INSTEAD\_OF\_ROW | VARCHAR2(3) |  | 指示触发器是否具有 INSTEAD OF 部分（ YES ）或无（ NO ） |
| FIRE\_ONCE | VARCHAR2(3) |  | 显示YES，指示触发器仅在用户进程进行更改时触发 |
| APPLY\_SERVER\_ONLY | VARCHAR2(3) |  | 显示NO，指示触发器不在复制应用或 SQL 应用过程中触发 |

## DBA\_SYNONYMS

描述当前数据库中的所有同义词。它的列与ALL\_SYNONYMS视图中的列相同。

该视图在V9.0.5及以后的版本中支持。

---

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | REGROLE |  | 同义词的所有者（即创建同义词的用户） |
| SYNONYM\_NAME | NAME |  | 同义词的名称 |
| TABLE\_OWNER | NAME |  | 同义词指向的基对象（如表、视图等）的所有者 |
| TABLE\_NAME | NAME |  | 引用对象的名称 |
| DB\_LINK | NAME |  | 如果引用对象位于远程数据库，则显示数据库链接的名称；若为本地对象，则为NULL |
| ORIGIN\_CON\_ID | TEXT |  | 数据产生的容器的ID，目前显示为NULL |

---

## ALL\_SYNONYMS

描述当前用户能访问的所有同义词。包括：当前用户拥有的私有同义词、所有的公共同义词。

如果一个私有同义词由其他用户创建，并且该同义词是基于数据库链（DBLink）指向远程对象的，则这些同义词不会包含在当前用户视图中。

该视图在V9.0.5及以后的版本中支持。

---

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | REGROLE |  | 同义词的所有者（即创建同义词的用户） |
| SYNONYM\_NAME | NAME |  | 同义词的名称 |
| TABLE\_OWNER | NAME |  | 同义词指向的基对象（如表、视图等）的所有者 |
| TABLE\_NAME | NAME |  | 引用对象的名称 |
| DB\_LINK | NAME |  | 如果引用对象位于远程数据库，则显示数据库链接的名称；若为本地对象，则为NULL |
| ORIGIN\_CON\_ID | TEXT |  | 数据产生的容器的ID，目前显示为NULL |

---

## USER\_SYNONYMS

描述当前用户拥有的私有同义词。该视图在V9.0.5及以后的版本中支持。

---

| 列名 | 数据类型 | 是否可空 | 描述 |
| --- | --- | --- | --- |
| OWNER | REGROLE |  | 同义词的所有者（即当前用户） |
| SYNONYM\_NAME | NAME |  | 同义词的名称 |
| TABLE\_OWNER | NAME |  | 同义词指向的基对象（如表、视图等）的所有者 |
| TABLE\_NAME | NAME |  | 引用对象的名称 |
| DB\_LINK | NAME |  | 如果引用对象位于远程数据库，则显示数据库链接的名称；若为本地对象，则为NULL |
| ORIGIN\_CON\_ID | TEXT |  | 数据产生的容器的ID，目前显示为NULL |
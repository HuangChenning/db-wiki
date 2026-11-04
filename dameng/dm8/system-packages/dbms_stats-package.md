---
title: "DBMS_STATS 包"
book: "DM8 系统包使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dbms_stats-package.html
tags:
  - dameng
  - dm8
  - system-packages
---

## 19 DBMS\_STATS 包

优化统计信息描述了数据库中的对象细节。查询优化使用这些信息选择最合适的执行计划。使用 DBMS\_STATS 包来收集统计、删除信息，将收集的统计信息记录在数据字典中。

## 19.1 数据类型

DBMS\_STATS 包中涉及到类型。如下统一说明。

1. OBJECTELEM 类型

ObjectElem 类型是 DBMS\_STATS 包内专有类型。用户不能引用和改变该记录的内容。ObjectElem 记录类型定义如下：

ObjectElem 类型是 DBMS\_STATS 专有类型。用户不能引用和改变该记录的内容。ObjectElem 记录类型定义如下：

```
TYPE OBJECTELEM IS RECORD (
    OWNNAME             VARCHAR(128) , 
    OBJTYPE             VARCHAR(6) , 
    OBJNAME                VARCHAR(128) , 
    PARTNAME            VARCHAR(128) ,  
    SUBPARTNAME         VARCHAR(128)  
) ;
```

**参数详解**

- ownname
	模式名。
- objtype
	对象类型，table 或 index。
- objname
	对象（表或索引）名称，区分大小写。
- partname
	分区名称，区分大小写。
- subpartname
	子分区名称，区分大小写。

例 ObjectTab 为 ObjectElem 类型的索引表：

```
TYPE ObjectTab is TABLE of ObjectElem INDEX BY INT;
```
2. STATREC 类型

STATREC 类型是 DBMS\_STATS 包内专有类型。用户不能引用和改变该记录的内容。STATREC 记录类型定义如下：

```
TYPE STATREC IS RECORD (
       EPC                NUMBER, 
       MINVAL           VARBINARY(8188), 
       MAXVAL          VARBINARY(8188),  
       EKHCNTS         NUMARRAY,   
       NOVALS          NUMARRAY,  
       CHVALS           CHARARRAY, 
       DTVALS            DATEARRAY, 
       EHCNTS           NUMARRAY,  
       EDCNTS           NUMARRAY 
   );
```

**参数详解**

- EPC
	endpoint 的个数（即桶数）。
- MINVAL
	最小值。
- MAXVAL
	最大值。
- EKHCNTS
	对应 ENDPOINT\_KEYHEIGHT，每个 endpoint 的重复次数。
- NOVALS
	对应 ENDPOINT\_VALUE，具体表示数值类型。
- CHVALS
	对应 ENDPOINT\_VALUE，具体表示字符类型。
- DTVALS
	对应 ENDPOINT\_VALUE，具体表示日期类型。
- EHCNTS
	对应 ENDPOINT\_HEIGHT，小于每个 endpoint 的数据个数。
- EDCNTS
	对应 ENDPOINT\_DISTINCT， 小于每个 endpoint 的唯一值个数。

例 定义一个 STATREC 类型的变量：

```
V_SREC            DBMS_STATS.STATREC;
```
3. NUMARRAY 类型

NUMARRAY 类型是 DBMS\_STATS 包提供的数据类型。自定义列统计信息直方图时，列类型为数字类型的都通过 NUMARRAY 存储，包括 INT、DOUBLE、FLOAT、DEC 等所有支持收集统计信息的数字类型。

```
TYPE NUMARRAY         IS VARRAY(2050) OF NUMBER;
```

例 定义一个 NUMARRAY 类型的变量：

```
ARRAY_COL_VAL             DBMS_STATS.NUMARRAY;
```
4. CHARARRAY 类型

CHARARRAY 类型是 DBMS\_STATS 包提供的数据类型。自定义列统计信息直方图时，列类型为字符类型都通过 CHARARRAY 存储，包括 CHAR、VARCHAR、BINARY 等所有支持收集统计信息的字符类型。

```
TYPE CHARARRAY    IS VARRAY(2050) OF VARCHAR2(4000);
```

例 定义一个 CHARARRAY 类型的变量：

```
ARRAY_COL_VAL        DBMS_STATS.CHARARRAY ;
```
5. DATEARRAY 类型

DATEARRAY 类型是 DBMS\_STATS 包提供的数据类型。自定义列统计信息直方图时，列类型为日期类型都通过 DATEARRAY 存储，包括 DATETIME、DATE、DATETIME WITH TIME ZONE、TIMESTAMP、TIME、TIME WITH TIME ZONE、INTERVAL YEAR TO MONTH、INTERVAL DAY TO SECOND。

```
TYPE DATEARRAY    IS VARRAY(2050) OF VARCHAR2(100);
```

例 定义一个 DATEARRAY 类型的变量：

```
ARRAY_COL_VAL        DBMS_STATS.DATEARRAY;
```

## 19.2 相关方法

DBMS\_STATS 包中包含的过程和函数如下详细介绍。其中，使用表、索引统计信息相关的过程和方法需要具有表查询权限；使用列统计信息相关的过程和方法需要具有列查询权限。

1. COLUMN\_STATS\_SHOW

根据模式名，表名和列名获得该列的统计信息。用于经过 GATHER\_TABLE\_STATS 或 GATHER\_SCHEMA\_STATS 收集之后展示。返回两个结果集：一个是列的统计信息；另一个是直方图的统计信息。

**语法如下：**

```
PROCEDURE COLUMN_STATS_SHOW (
    OWNNAME        IN          VARCHAR(128), 
    TABNAME        IN          VARCHAR(128),
    COLNAME        IN          VARCHAR(128)
);
```

列的统计信息和直方图的统计信息，格式分别如下表 19.1、表 19.2：

表19.1 列统计信息

| **名称** | **解释** |
| --- | --- |
| NUM\_DISTINCT | 不同列值的个数 |
| LOW\_VALUE | 列最小值 |
| HIGH\_VALUE | 列最大值 |
| NUM\_NULLS | 空值的个数 |
| NUM\_BUCKETS | 直方图桶的个数 |
| SAMPLE\_SIZE | 样本容量 |
| HISTOGRAM | 直方图的类型 |

表19.2 直方图的统计信息

| **名称** | **解释** |
| --- | --- |
| OWNER | 模式名 |
| TABLE\_NAME | 表名 |
| COLUMN\_NAME | 列名 |
| HISTOGRAM | 直方图类型 |
| ENDPOINT\_VALUE | 样本值 |
| ENDPOINT\_HEIGHT | 对于频率直方图，样本值的个数；对于等高直方图，小于样本值大于前一个样本值的个数。 |
| ENDPOINT\_KEYHEIGHT | 对于频率直方图无效；对于等高直方图，样本值的个数。 |
| ENDPOINT\_DISTINCT | 对于频率直方图无效；对于等高直方图，小于样本值大于前一个样本值之间不同样本的个数。 |

**参数详解**

- OWNNAME
	模式名，区分大小写。
- TABNAME
	表名，区分大小写。
- COLNAME
	列名，区分大小写。
2. TABLE\_STATS\_SHOW

根据模式名，表名获得该表的统计信息。用于经过 GATHER\_TABLE\_STATS 或 GATHER\_SCHEMA\_STATS 收集之后展示。

**语法如下：**

```
PROCEDURE TABLE_STATS_SHOW (
    OWNNAME        IN          VARCHAR(128), 
    TABNAME        IN          VARCHAR(128)
);
```

表的统计信息，格式如下表 19.3：

表 19.3 表统计信息

| **名称** | **解释** |
| --- | --- |
| NUM\_ROWS | 表的总行数 |
| LEAF\_BLOCKS | 总的页数 |
| LEAF\_USED\_BLOCKS | 已经使用的页数 |

**参数详解**

- OWNNAME
	模式名，区分大小写。
- TABNAME
	表名，区分大小写。
3. INDEX\_STATS\_SHOW

根据模式名，索引名获得该索引的统计信息。用于经过 GATHER\_TABLE\_STATS、GATHER\_INDEX\_STATS 或 GATHER\_SCHEMA\_STATS 收集之后展示。返回两个结果集：一个是索引的统计信息；另一个是直方图的统计信息。

**语法如下：**

```
PROCEDURE INDEX_STATS_SHOW (
    OWNNAME        IN      VARCHAR(128), 
    INDEXNAME    IN          VARCHAR(128)
);
```

索引的统计信息和直方图的统计信息，格式分别如下表 19.4、表 19.5：

表 19.4 索引统计信息

| **名称** | **解释** |
| --- | --- |
| BLEVEL | B\_Tree 的层次 |
| LEAF\_BLOCKS | 页数 |
| DISTINCT\_KEYS | 不同样本的个数 |
| CLUSTERING\_FACTOR | 聚集因子，表示索引的数据分布与物理分布之间的关系，暂不支持 |
| NUM\_ROWS | 行数 |
| SAMPLE\_SIZE | 样本容量 |

表 19.5 直方图的统计信息

| **名称** | **解释** |
| --- | --- |
| OWNER | 模式名 |
| NAME | 索引名 |
| COLUMN\_NAME | 列名 |
| HISTOGRAM | 直方图类型 |
| ENDPOINT\_VALUE | 样本值 |
| ENDPOINT\_HEIGHT | 对于频率直方图，样本值的个数；对于等高直方图，小于样本值大于前一个样本值的个数。 |
| ENDPOINT\_KEYHEIGHT | 对于频率直方图无效；对于等高直方图，样本值的个数。 |
| ENDPOINT\_DISTINCT | 对于频率直方图无效；对于等高直方图，小于样本值大于前一个样本值之间不同样本的个数。 |

**参数详解**

- OWNNAME
	模式名，区分大小写。
- INDEXNAME
	索引名，区分大小写。
4. GATHER\_TABLE\_STATS

根据设定的参数，收集表、表中的列和表上的索引的统计信息。其中，对于表，只搜集表的总行数、总的页数、已经使用的页数等基本信息。本操作会提交当前事务。

**语法如下：**

```
PROCEDURE GATHER_TABLE_STATS (
    OWNNAME            VARCHAR(128), 
    TABNAME            VARCHAR(128), 
    PARTNAME        VARCHAR(128)    DEFAULT NULL,
    ESTIMATE_PERCENT    DOUBLE        DEFAULT TO_ESTIMATE_PERCENT_TYPE(GET_PREFS('ESTIMATE_PERCENT')), 
    BLOCK_SAMPLE    BOOLEAN      DEFAULT FALSE,
    METHOD_OPT        VARCHAR      DEFAULT GET_PREFS('METHOD_OPT'),
    DEGREE            INT           DEFAULT TO_DEGREE_TYPE(GET_PREFS('DEGREE')),
    GRANULARITY        VARCHAR      DEFAULT GET_PREFS('GRANULARITY'), 
    CASCADE            BOOLEAN      DEFAULT TO_CASCADE_TYPE(GET_PREFS('CASCADE')),
    STATTAB            VARCHAR      DEFAULT NULL, 
    STATID            VARCHAR      DEFAULT NULL,
    STATOWN            VARCHAR      DEFAULT NULL,
    NO_INVALIDATE    BOOLEAN        DEFAULT TO_NO_INVALIDATE_TYPE(GET_PREFS('NO_INVALIDATE')),
    FORCE             BOOLEAN      DEFAULT FALSE
    MERGE_STAT       BOOLEAN  DEFAULT FALSE
);
```

**参数详解**

- OWNNAME
	模式名，区分大小写。
- TABNAME
	表名，区分大小写。
- PARTNAME
	分区表名，缺省为 NULL，区分大小写。
- ESTIMATE\_PERCENT
	收集的百分比，范围为 0~100，区间(0,0.000001)内的值，按 0.000001 取值计算。默认系统自定。
- BLOCK\_SAMPLE
	TRUE 表示以数据页为单位采样；FALSE 表示以数据行为单位采样。缺省为 FALSE。
- METHOD\_OPT
	控制列的统计信息集合和直方图的创建的格式，缺省为 FOR ALL COLUMNS SIZE DEFAULT。其中 BLOB、IMAGE、LONGVARBINARY、CLOB、TEXT、LONGVARCHAR、自定义类型列和空间类型列等列类型不能被收集。使用 FOR COLUMNS 语法时，后跟可选填的<size\_clause> 部分和必填的<column\_name> 部分，多个<column\_name> 之间必须用“,”分隔。格式选项如下：
```
FOR ALL [INDEXED | HIDDEN] COLUMNS [<size_clause>]
<size_clause>::= SIZE { integer | REPEAT | AUTO | SKEWONLY}
或者
FOR COLUMNS { <size clause> |  [<size clause>] <column_name> [<size_clause>]}  {, <column_name> [<size_clause>]}
```

各参数解释如下：

- INDEXED | HIDDEN 表示只统计索引或者隐藏的列，缺省为都统计。
- SIZE integer 表示直方图的桶数。其中的 integer 必须指定某个具体的数值，取值范围 1~10000。
- SIZE REPEAT 只统计已经有直方图的列。
- SIZE AUTO 根据数据分布和工作量自动决定统计直方图的列。设置为默认取值 FOR ALL COLUMNS SIZE AUTO 时，DM 会根据数据分布和工作量自动决定统计直方图的列。
- SIZE SKEWONLY 根据数据分布决定统计直方图的列。
- SIZE DEFAULT 表示统计列的直方图且由系统自定义桶数。
- DEGREE
	收集的并行度，缺省为 1。
- GRANULARITY
	收集的粒度，默认为 Auto；GRANULARITY 可选参数如下：AUTO | DEFAULT |ALL | PARTITION | SUBPARTITION | GLOBAL | GLOBAL AND PARTITION。

各参数解释如下：  
◆ALL 收集全部的统计信息（subpartition，partition 和 global）。  
◆AUTO 缺省值，根据分区的类型来决定如何收集。  
◆DEFAULT 和 auto 功能相同。  
◆GLOBAL 收集 global 表的统计信息。  
◆GLOBAL AND PARTITION 收集 GLOBAL 和 PARTITION 表的统计信息。  
◆PARTITION 收集 PARTITION 表的统计信息。  
◆SUBPARTITION 收集 subpartition 表的统计信息。当子分区表个数超过 50 时，因为采用跳跃采样，所以统计信息会有误差。即使采样率为 100，也还是会有误差。可以通过减少统计层次的方式降低这种误差，即将 granularity=>'subpartition'修改成 granularity=>'GLOBAL AND PARTITION'或 granularity=>'GLOBAL'。

- CASCADE
	是否收集索引信息，TRUE 或 FALSE，默认为 TRUE。
- STATTAB
	统计信息存放的表，默认为 NULL。
- STATID
	统计信息的 ID，默认为 NULL。
- STATOWN
	统计信息的模式，默认为 NULL。
- NO\_INVALIDATE
	保留参数，是否让依赖游标失效，缺省为 TRUE。NO\_INVALIDATE 可选参数如下:TRUE | FALSE | DBMS\_STATS.AUTO\_INVALIDATE。
	各参数解释如下：
	◆ TRUE 游标不失效，原有的执行计划保持原状态。
	◆ FALSE 游标失效，移除原有的相关执行计划。
	◆ DBMS\_STATS.AUTO\_INVALIDATE 和 TRUE 用法相同。
- force
	是否忽略统计信息锁，强制收集统计信息，缺省为 FALSE；为 TRUE 表示被锁住也强制收集统计信息，为 FALSE 表示没有被锁住才能收集统计信息。
- merge\_stat
	为分区子表收集统计信息后，是否级联更新祖先对应的统计信息，TRUE 是，FALSE 否；缺省为 FALSE。
5. GATHER\_INDEX\_STATS

根据设定的参数，收集索引的统计信息。本操作会提交当前事务。

**语法如下：**

```
PROCEDURE GATHER_INDEX_STATS (
    OWNNAME                VARCHAR(128), 
    INDNAME                VARCHAR(128), 
    PARTNAME            VARCHAR(128)    DEFAULT NULL,
    ESTIMATE_PERCENT    DOUBLE    DEFAULT TO_ESTIMATE_PERCENT_TYPE(GET_PREFS('ESTIMATE_PERCENT')),
    STATTAB                VARCHAR    DEFAULT NULL, 
    STATID                VARCHAR    DEFAULT NULL,
    STATOWN                VARCHAR    DEFAULT NULL,
    DEGREE                INT        DEFAULT TO_DEGREE_TYPE(GET_PREFS('DEGREE')),
    GRANULARITY            VARCHAR    DEFAULT GET_PREFS('GRANULARITY'),
    NO_INVALIDATE        BOOLEAN  DEFAULT TO_NO_INVALIDATE_TYPE(GET_PREFS('NO_INVALIDATE')),
    FORCE                BOOLEAN    DEFAULT FALSE
);
```

**参数详解**

- OWNNAME
	模式名，区分大小写。
- INDNAME
	索引名，区分大小写。
- PARTNAME
	分区索引名，缺省为 NULL，区分大小写。
- ESTIMATE\_PERCENT
	收集的百分比，范围为 0~100，区间(0,0.000001)内的值，按 0.000001 取值计算。默认系统自定。
- STATTAB
	保留参数，统计信息存放的表，缺省为 NULL。
- STATID
	保留参数，统计信息的 ID，缺省为 NULL。
- STATOWN
	保留参数，统计信息的模式，缺省为 NULL。
- DEGREE
	保留参数，收集的并行度，缺省为 1。
- GRANULARITY
	保留参数，收集的粒度，缺省为 ALL。
- NO\_INVALIDATE
	是否让依赖游标失效，缺省为 TRUE。具体用法请参考 GATHER\_TABLE\_STATS 方法的 NO\_INVALIDATE 参数。
- FORCE
	是否忽略统计信息锁，强制收集统计信息，缺省为 FALSE；为 TRUE 表示被锁住也强制收集统计信息，为 FALSE 表示没有被锁住才能收集统计信息。
6. GATHER\_SCHEMA\_STATS

收集模式下对象的统计信息。只收集有查询权限的对象，对于没有查询权限的对象会直接跳过。本操作会提交当前事务。

**语法如下：**

```
PROCEDURE GATHER_SCHEMA_STATS (
    OWNNAME                VARCHAR(128), 
    ESTIMATE_PERCENT    DOUBLE    DEFAULT TO_ESTIMATE_PERCENT_TYPE(GET_PREFS('ESTIMATE_PERCENT')), 
    BLOCK_SAMPLE        BOOLEAN    DEFAULT FALSE, 
    METHOD_OPT            VARCHAR    DEFAULT GET_PREFS('METHOD_OPT'),
    DEGREE                INT        DEFAULT TO_DEGREE_TYPE(GET_PREFS('DEGREE')), 
    GRANULARITY            VARCHAR    DEFAULT GET_PREFS('GRANULARITY'), 
    CASCADE                BOOLEAN    DEFAULT TO_CASCADE_TYPE(GET_PREFS('CASCADE')), 
    STATTAB                VARCHAR    DEFAULT NULL, 
    STATID                VARCHAR    DEFAULT NULL, 
    OPTIONS                VARCHAR    DEFAULT 'GATHER', 
    OBJLIST        OUT      OBJECTTAB DEFAULT NULL,
    STATOWN                VARCHAR    DEFAULT NULL, 
    NO_INVALIDATE        BOOLEAN    DEFAULT TO_NO_INVALIDATE_TYPE(GET_PREFS('NO_INVALIDATE')),
    FORCE                BOOLEAN    DEFAULT FALSE,
    OBJ_FILTER_LIST        OBJECTTAB DEFAULT NULL
);
```

**参数详解**

- OWNNAME
	模式名，区分大小写。
- ESTIMATE\_PERCENT
	收集的百分比，范围为 0~100，区间(0,0.000001)内的值，按 0.000001 取值计算。默认系统自定。
- BLOCK\_SAMPLE
	TRUE 表示以数据页为单位采样；FALSE 表示以数据行为单位采样。缺省为 FALSE。
- METHOD\_OPT
	控制列的统计信息集合和直方图的创建；缺省为 FOR ALL COLUMNS SIZE DEFAULT；只支持其中一种格式：
```
FOR ALL[INDEXED | HIDDEN] COLUMNS [<size_clause>]
<size_clause>::= SIZE {integer | REPEAT | AUTO | SKEWONLY}
```

各参数解释如下：

- INDEXED | HIDDEN 表示只统计索引或者隐藏的列，缺省为都统计。
- SIZE integer 表示直方图的桶数。其中的 integer 必须指定某个具体的数值，取值范围 1~10000。
- SIZE REPEAT 只统计已经有直方图的列。
- SIZE AUTO 根据数据分布和工作量自动决定统计直方图的列。设置为默认取值 FOR ALL COLUMNS SIZE AUTO 时，DM 会根据数据分布和工作量自动决定统计直方图的列。
- SIZE SKEWONLY 根据数据分布决定统计直方图的列。
- SIZE DEFAULT 表示统计列的直方图且由系统自定义桶数。
- DEGREE
	收集的并行度，缺省为 1。
- GRANULARITY
	收集的粒度，缺省为 ALL。
- CASCADE
	是否收集索引信息，TRUE 或 FALSE。缺省为 TRUE。
- STATTAB
	统计信息存放的表，缺省为 NULL。
- STATID
	统计信息的 ID，默认为 NULL。
- OPTIONS
	控制收集的列，缺省为 GATHER；选项如下：GATHER|GATHER AUTO|GATHER STALE|GATHER EMPTY|LIST AUTO|LIST STALE|LIST EMPTY。各选项解释如下：
	◆GATHER：收集模式下所有对象的统计信息。
	◆GATHER AUTO：自动收集需要的统计信息。系统隐含的决定哪些对象需要新的统计信息，以及怎样收集这些统计信息。此时，只有 ownname，stattab， statid，objlist and statown 有效，返回收集统计信息的对象。
	◆GATHER STALE：对旧的对象收集统计信息。返回找到的旧的对象。
	◆GATHER EMPTY：收集没有统计信息对象的统计信息。返回这些对象。
	◆LIST AUTO：返回 GATHER AUTO 方式处理的对象。
	◆LIST STALE：返回旧的对象信息。
	◆LIST EMPTY：返回没有统计信息的对象。
- OBJLIST
	返回 OPTION 选项对应的链表，缺省为 NULL。
- STATOWN
	统计信息的模式，缺省为 NULL。
- NO\_INVALIDATE
	是否让依赖游标失效，缺省为 TRUE。具体用法请参考 GATHER\_TABLE\_STATS 方法的 NO\_INVALIDATE 参数。
- FORCE
	是否忽略统计信息锁，强制收集统计信息，缺省为 FALSE；为 TRUE 表示被锁住也强制收集统计信息，为 FALSE 表示没有被锁住才能收集统计信息。
- OBJ\_FILTER\_LIST
	存放过滤条件的模式名、表名和子表名，缺省为 NULL。
7. DELETE\_TABLE\_STATS

根据设定参数，删除与表相关对象的统计信息。本操作会提交当前事务。

**语法如下：**

```
PROCEDURE DELETE_TABLE_STATS (
    OWNNAME                VARCHAR(128), 
    TABNAME                VARCHAR(128), 
    PARTNAME            VARCHAR(128)    DEFAULT NULL,
    STATTAB                VARCHAR            DEFAULT NULL, 
    STATID                VARCHAR            DEFAULT NULL,
    CASCADE_PARTS        BOOLEAN            DEFAULT TRUE, 
    CASCADE_COLUMNS        BOOLEAN            DEFAULT TRUE,
    CASCADE_INDEXES        BOOLEAN            DEFAULT TRUE,
    STATOWN                VARCHAR            DEFAULT NULL,
    NO_INVALIDATE        BOOLEAN            DEFAULT TO_NO_INVALIDATE_TYPE(GET_PREFS('NO_INVALIDATE')),
    FORCE                BOOLEAN             DEFAULT FALSE
);
```

**参数详解**

- OWNNAME
	模式名，区分大小写。
- TABNAME
	表名，区分大小写。
- PARTNAME
	分区表名，缺省为 NULL，区分大小写。
- STATTAB
	保留参数，统计信息存放的表，缺省为 NULL。
- STATID
	保留参数，统计信息的 ID，缺省为 NULL。
- CASCADE\_PARTS
	是否级联删除分区表信息，缺省为 TRUE。
- CASCADE\_COLUMNS
	是否级联删除表中列的信息，取值 TRUE 或 FALSE。缺省为 TRUE。
- CASCADE\_INDEXES
	是否级联删除表的索引信息，取值 TRUE 或 FALSE。缺省为 TRUE。
- STATOWN
	保留参数，统计信息的模式，缺省为 NULL。
- NO\_INVALIDATE
	是否让依赖游标失效，缺省为 TRUE。具体用法请参考 GATHER\_TABLE\_STATS 方法的 NO\_INVALIDATE 参数。
- FORCE
	是否忽略统计信息锁，强制删除统计信息，缺省为 FALSE；为 TRUE 表示被锁住也强制删除统计信息，为 FALSE 表示没有被锁住才能删除统计信息。
8. DELETE\_SCHEMA\_STATS

根据设定参数，删除模式下对象的统计信息。本操作会提交当前事务。

**语法如下：**

```
PROCEDURE DELETE_SCHEMA_STATS (
    OWNNAME            VARCHAR(128), 
    STATTAB            VARCHAR         DEFAULT NULL, 
    STATID            VARCHAR         DEFAULT NULL,
    STATOWN            VARCHAR         DEFAULT NULL,
    NO_INVALIDATE    BOOLEAN        DEFAULT TO_NO_INVALIDATE_TYPE(GET_PREFS('NO_INVALIDATE')),
    FORCE            BOOLEAN         DEFAULT FALSE
);
```

**参数详解**

- OWNNAME
	模式名，区分大小写。
- STATTAB
	保留参数，统计信息存放的表，缺省为 NULL。
- STATID
	保留参数，统计信息的 ID，缺省为 NULL。
- STATOWN
	保留参数，统计信息的模式，缺省为 NULL。
- NO\_INVALIDATE
	是否让依赖游标失效，缺省为 TRUE。具体用法请参考 GATHER\_TABLE\_STATS 方法的 NO\_INVALIDATE 参数。
- FORCE
	是否忽略统计信息锁，强制删除统计信息，缺省为 FALSE；为 TRUE 表示被锁住也强制删除统计信息，为 FALSE 表示没有被锁住才能删除统计信息。
9. DELETE\_INDEX\_STATS

根据设定参数，删除索引的统计信息。本操作会提交当前事务。

**语法如下：**

```
PROCEDURE DELETE_INDEX_STATS (
    OWNNAME            VARCHAR(128), 
    INDNAME            VARCHAR(128),
    PARTNAME        VARCHAR(128)         DEFAULT NULL,
    STATTAB            VARCHAR             DEFAULT NULL, 
    STATID            VARCHAR             DEFAULT NULL,
    CASCADE_PARTS    BOOLEAN              DEFAULT TRUE,
    STATOWN            VARCHAR             DEFAULT NULL,
    NO_INVALIDATE    BOOLEAN                DEFAULT TO_NO_INVALIDATE_TYPE(GET_PREFS('NO_INVALIDATE')),
    FORCE            BOOLEAN              DEFAULT FALSE
);
```

**参数详解**

- OWNNAME
	模式名，区分大小写。
- INDNAME
	索引名，区分大小写。
- PARTNAME
	分区索引名，缺省为 NULL，区分大小写。
- STATTAB
	保留参数，统计信息存放的表，缺省为 NULL。
- STATID
	保留参数，统计信息的 ID，缺省为 NULL。
- CASCADE\_PARTS
	是否级联删除分区表信息，TRUE 或 FALSE。缺省为 TRUE。
- STATOWN
	保留参数，统计信息的模式，缺省为 NULL。
- NO\_INVALIDATE
	是否让依赖游标失效，缺省为 TRUE。具体用法请参考 GATHER\_TABLE\_STATS 方法的 NO\_INVALIDATE 参数。
- FORCE
	是否忽略统计信息锁，强制删除统计信息，缺省为 FALSE；为 TRUE 表示被锁住也强制删除统计信息，为 FALSE 表示没有被锁住才能删除统计信息。
10. DELETE\_COLUMN\_STATS

根据设定参数，删除列的统计信息。本操作会提交当前事务。

**语法如下：**

```
PROCEDURE DELETE_COLUMN_STATS (
    OWNNAME            VARCHAR(128), 
    TABNAME            VARCHAR(128), 
    COLNAME            VARCHAR(128), 
    PARTNAME        VARCHAR(128)         DEFAULT NULL,
    STATTAB            VARCHAR             DEFAULT NULL, 
    STATID            VARCHAR             DEFAULT NULL,
    CASCADE_PARTS    BOOLEAN              DEFAULT TRUE,
    STATOWN            VARCHAR             DEFAULT NULL,
    NO_INVALIDATE    BOOLEAN                DEFAULT TO_NO_INVALIDATE_TYPE(GET_PREFS('NO_INVALIDATE')),
    FORCE            BOOLEAN              DEFAULT FALSE,
    COL_STAT_TYPE    VARCHAR             DEFAULT 'ALL'
);
```

**参数详解**

- OWNNAME
	模式名，区分大小写。
- TABNAME
	表名，区分大小写。
- COLNAME
	列名，区分大小写。
- PARTNAME
	分区表名，默认为 NULL，区分大小写。
- STATTAB
	保留参数，统计信息存放的表，缺省为 NULL。
- STATID
	保留参数，统计信息的 ID，缺省为 NULL。
- CASCADE\_PARTS
	是否级联删除分区表信息，TRUE 或 FALSE。缺省为 TRUE。
- STATOWN
	保留参数，统计信息的模式，缺省为 NULL。
- NO\_INVALIDATE
	是否让依赖游标失效，缺省为 TRUE。具体用法请参考 GATHER\_TABLE\_STATS 方法的 NO\_INVALIDATE 参数。
- FORCE
	是否忽略统计信息锁，强制删除统计信息，缺省为 FALSE；为 TRUE 表示被锁住也强制删除统计信息，为 FALSE 表示没有被锁住才能删除统计信息。
- COL\_STAT\_TYPE
	保留参数，是否只删除直方图信息，缺省为 ALL。
11. UPDATE\_ALL\_STATS

更新已有的统计信息。本操作会提交当前事务。

**语法如下：**

```
PROCEDURE UPDATE_ALL_STATS ();
```
12. CONVERT\_RAW\_VALUE

把二进制流转换为指定类型。本操作会提交当前事务。

**语法如下：**

```
PROCEDURE CONVERT_RAW_VALUE (
    I_RAW     VARBINARY(8188),
    M_N     OUT NUMBER
);
```
```
PROCEDURE CONVERT_RAW_VALUE (
    I_RAW     VARBINARY(8188),
    M_N     OUT DATETIME
);
PROCEDURE CONVERT_RAW_VALUE (
    I_RAW     VARBINARY(8188),
    M_N OUT VARCHAR(8188)
);
PROCEDURE CONVERT_RAW_VALUE (
    I_RAW     VARBINARY(8188),
    M_N     OUT DOUBLE
);
```

**参数详解**

- I\_RAW
	输入参数，VARBINARY 类型的最大或最小值，期望来源于 SYSSTATS 表的 V\_MAX 或 V\_MIN 列。
- M\_N
	输出参数，由 I\_RAW 转换而来，支持 NUMBER、DATETIME、VARCHAR(8188)、DOUBLE 类型。
13. CREATE\_STAT\_TABLE

根据用户指定的名称创建一个增加了前缀的临时统计信息表，用于保存待导出的统计信息。统计信息保存到该表中后，可以使用 DM 的数据导入导出工具进行跨实例导入导出。MPP 环境下暂不支持统计信息导入导出功能。本操作会提交当前事务。DMDPC 下 global\_temporary=true 时要求表空间是 TEMP\_TS。

统计信息表属于内建表，为跟普通用户表区分，系统内部会为表名增加前缀“STAT$\_”。例如用户指定统计信息表名为 STATTAB，查询该统计信息表应该使用 STAT$\_STATTAB。对于用户，统计信息表不支持使用 CREATE、DROP、ALTER、TRUNCATE、INSERT、DELETE、UPDATE、GRANT 操作，会报错。统计信息表支持通过包方法 DROP\_STAT\_TABLE 进行删除。

**语法如下：**

```
PROCEDURE CREATE_STAT_TABLE (
    STATOWN                VARCHAR(128),
    STATTAB                VARCHAR(128),
    TABLESPACE            VARCHAR(128)         DEFAULT NULL,
    GLOBAL_TEMPORARY    BOOLEAN             DEFAULT FALSE
);
```

**参数详解**

- STATOWN
	统计信息表的模式名，区分大小写。
- STATTAB
	统计信息表名，区分大小写，系统实际创建的表会增加前缀。
- TABLESPACE
	表空间名，默认为 NULL，区分大小写。
- GLOBAL\_TEMPORARY
	是否创建为会话级的全局临时表。
14. DROP\_STAT\_TABLE

删除统计信息表。本操作会提交当前事务。

**语法如下：**

```
PROCEDURE DROP_STAT_TABLE (
    STATOWN            VARCHAR(128),
    STATTAB            VARCHAR(128)
);
```

**参数详解**

- STATOWN
	统计信息表的模式名，区分大小写。
- STATTAB
	创建时指定的统计信息表名，区分大小写。
15. EXPORT\_TABLE\_STATS

把目标表的统计信息导出到指定统计信息表中。本操作会提交当前事务。

**语法如下：**

```
PROCEDURE EXPORT_TABLE_STATS(
    OWNNAME            VARCHAR(128),
    TABNAME            VARCHAR(128),
    PARTNAME        VARCHAR(128)     DEFAULT NULL,
    STATTAB            VARCHAR(128),
    STATID            VARCHAR(128)     DEFAULT '',
    CASCADE            BOOLEAN           DEFAULT TRUE,
    STATOWN            VARCHAR(128)     DEFAULT NULL,
    STAT_CATEGORY    VARCHAR(128)     DEFAULT NULL
);
```

**参数详解**

- OWNNAME
	目标表的模式名，区分大小写。
- TABNAME
	目标表名，区分大小写。
- PARTNAME
	目标表分区名，如果不指定分区，则一起导出所有子表的统计信息，缺省为 NULL。
- STATTAB
	统计信息表名，区分大小写。
- STATID
	由用户指定的统计信息标识名，缺省认为空字符串。
- CASCADE
	是否连列和索引的统计信息一起导出，缺省为 TRUE
- STATOWN
	统计信息表的模式名，区分大小写，缺省为 NULL。
- STAT\_CATEGORY
	保留参数，无实际意义。
16. IMPORT\_TABLE\_STATS

把统计信息表中的统计信息导入到目标表中。本操作会提交当前事务。

**语法如下：**

```
PROCEDURE IMPORT_TABLE_STATS(
    OWNNAME            VARCHAR(128),
    TABNAME            VARCHAR(128),
    PARTNAME        VARCHAR(128)     DEFAULT NULL,
    STATTAB            VARCHAR(128),
    STATID            VARCHAR(128)    DEFAULT '',
    CASCADE            BOOLEAN           DEFAULT TRUE,
    STATOWN            VARCHAR(128)     DEFAULT NULL,
    NO_INVALIDATE    BOOLEAN            DEFAULT NULL,
    FORCE            BOOLEAN          DEFAULT FALSE, 
    STAT_CATEGORY    VARCHAR(128)     DEFAULT NULL
);
```

**参数详解**

- OWNNAME
	目标表的模式名，区分大小写。
- TABNAME
	目标表名，区分大小写。
- PARTNAME
	目标表分区名，如果不指定分区，则一起导入所有子表的统计信息，缺省为 NULL。
- STATTAB
	统计信息表名，区分大小写。
- STATID
	由用户指定的统计信息标识名，缺省为空字符串。
- CASCADE
	是否连列和索引的统计信息一起导入，缺省为 TRUE
- STATOWN
	统计信息表的模式名，区分大小写，缺省为 NULL。
- NO\_INVALIDATE
	是否让依赖游标失效，缺省为 TRUE。具体用法请参考 GATHER\_TABLE\_STATS 方法的 NO\_INVALIDATE 参数。
- FORCE
	是否忽略统计信息锁，强制把统计信息表中的统计信息导入到目标表中，缺省为 FALSE。为 TRUE 表示目标表被锁住也强制导入，为 FALSE 表示目标表没有被锁住才能导入。
- STAT\_CATEGORY
	保留参数，无实际意义。

**使用说明：**

统计信息导入时，导入对象完全由对象名称来确定，如果存在由系统根据 ID 自动创建的对象，例如在分区表主表上建立索引时，子表上自动建立的索引将根据索引 ID 来命名，统计信息表里存储的索引名称可能与新建立的分区表子表上的索引名称不一致，此时名称不一致的索引统计信息将无法导入。

17. SET\_TABLE\_PREFS

该过程设置普通用户表的静态属性值。本操作会提交当前事务。

**语法如下：**

```
PROCEDURE SET_TABLE_PREFS (
    OWNNAME        VARCHAR(128),
    TABNAME        VARCHAR(128),
    PPNAME        VARCHAR(128),
    PVALUE        VARCHAR(128)
);
```

**参数详解**

- OWNNAME
	模式名，不区分大小写。
- TABNAME
	表名，不区分大小写。
- PPNAME
	属性名，不区分大小写。可以取 STALE\_PERCENT 、ESTIMATE\_PERCENT、METHOD\_OPT、DEGREE、GRANULARITY、CASCADE、NO\_INVALIDATE、PREFERENCE\_OVERRIDES\_PARAMETER、MONITOR\_MODIFICATIONS\_FLAG、MONITOR\_MODIFICATIONS\_RM\_PLN\_FLAG 和 MONITOR\_MODIFICATIONS\_REGATHER\_COL。
	STALE\_PERCENT 决定表的统计信息过时且需要重新收集统计信息时表的行数百分比。有效取值范围 0~100，缺省值是 10，即一张表有超过 10% 的数据改变则可认为统计信息过时。将该值置为 0 时，系统会自动将该表的 STALE\_PERCENT 属性值置为缺省值 10。特别的，当 INI 参数 AUTO\_STAT\_OBJ=0 或 2 时，对表 T 设置 STALE\_PERCENT=0，表示不再监控表 T，将其从系统表 SYSSTATTABLEIDU 中移除（设置的动作即表示将表 T 从系统表 SYSSTATTABLEIDU 中移除，尽管此时查询 STALE\_PERCENT 值仍为缺省值 10）；对表 T 设置 STALE\_PERCENT>0，表示要监控表 T，将其加入系统表 SYSSTATTABLEIDU，并将系统表对应记录的 MONITOR\_FLAG 列置为 2。当 INI 参数 AUTO\_STAT\_OBJ=1（表示对所有表进行监控）时，对表 T 设置 STALE\_PERCENT=0 仍会监控表 T，且当系统表 SYSSTATTABLEIDU 存在该表信息时会将 MONITOR\_FLAG 列置为 1，若不存在则当该表发生数据变动时将该表加入系统表 SYSSTATTABLEIDU 中（进行收集统计信息操作后可以查询到），并将 MONITOR\_FLAG 列置为 1；对表 T 设置 STALE\_PERCENT>0 表示要监控表 T，将其加入系统表 SYSSTATTABLEIDU，并将 MONITOR\_FLAG 列置为 2。
	PREFERENCE\_OVERRIDES\_PARAMETER 决定是否用静态属性值覆盖参数的输入值。为 TRUE 时，忽略参数的输入值，使用对应的属性值；为 FALSE 时，使用参数的输入值。
	MONITOR\_MODIFICATIONS\_FLAG 决定是否对表进行数据变化监控。为 TRUE 时，监控表的数据变化；为 FALSE 时，不监控表的数据变化。默认值为 TRUE。
	MONITOR\_MODIFICATIONS\_RM\_PLN\_FLAG 决定对表进行数据变化监控时，当数据变化达到该阈值时，会移除该表相关的缓存计划，同时按照指定方式重新收集该表的统计信息，取值范围\[-1,2147483647\]。若后续未指定 MONITOR\_MODIFICATIONS\_REGATHER\_COL，则重新对该表所有存在频率直方图统计信息的列和索引收集统计信息；若后续指定了 MONITOR\_MODIFICATIONS\_REGATHER\_COL，则只检测 MONITOR\_MODIFICATIONS\_REGATHER\_COL 监控的列及包含该列的索引，并只对存在统计信息的重新收集统计信息，同一张表上可指定多个不同的列。必须先指定 MONITOR\_MODIFICATIONS\_RM\_PLN\_FLAG，才可以指定 MONITOR\_MODIFICATIONS\_REGATHER\_COL。
	其他属性值范围可以参考 GATHER\_TABLE\_STATS 中的参数描述。
- PVALUE
	属性名对应的属性值，不区分大小写。
18. GET\_PREFS

该函数返回普通用户表的静态属性值。

**语法如下：**

```
FUNCTION GET_PREFS(
    PPNAME          VARCHAR(128),
    OWNNAME          VARCHAR(128),
    TABNAME          VARCHAR(128)
)RETURN VARCHAR;
```

**参数详解**

- PPNAME
	属性名，不区分大小写。可以取 STALE\_PERCENT 、ESTIMATE\_PERCENT、METHOD\_OPT、DEGREE、GRANULARITY、CASCADE、NO\_INVALIDATE、PREFERENCE\_OVERRIDES\_PARAMETER、MONITOR\_MODIFICATIONS\_FLAG、MONITOR\_MODIFICATIONS\_RM\_PLN\_FLAG 和 MONITOR\_MODIFICATIONS\_REGATHER\_COL。
	特别的，当 PPNAME 指定为 MONITOR\_MODIFICATIONS\_REGATHER\_COL 时，返回的数值代表对应列在表中的序号（第一列的序号为 0，第二列的序号是 1，如此类推）；若存在多列，则返回诸如"0,1,3"这样的形式。
- OWNNAME
	模式名，不区分大小写。
- TABNAME
	表名，不区分大小写。
19. COPY\_TABLE\_STATS

该过程将基表中指定源分区的统计信息复制到同一基表的指定的目的分区，目的分区原有统计信息将被覆盖。本操作会提交当前事务。

**语法如下：**

```
PROCEDURE COPY_TABLE_STATS(
    OWNNAME               VARCHAR(128),
    TABNAME               VARCHAR(128),
    SRCPARTNAME          VARCHAR(128),
    DSTPARTNAME          VARCHAR(128),
    SCALE_FACTOR         VARCHAR(128) DEFAULT '1',
    FORCE                 BOOLEAN      DEFAULT FALSE
);
```

**参数详解**

- OWNNAME
	模式名，区分大小写。
- TABNAME
	基表名，区分大小写。
- SRCPARTNAME
	源分区名，区分大小写。
- DSTPARTNAME
	目标分区名，区分大小写。
- SCALE\_FACTOR
	保留参数，无实际意义。
- FORCE
	是否忽略统计信息锁，强制将基表中指定源分区的统计信息复制到同一基表的指定的目的分区，缺省为 FALSE。为 TRUE 表示基表被锁住也强制复制，为 FALSE 表示基表没有被锁住才能复制。
20. SET\_TABLE\_STATS

该过程设置指定表的指定统计信息。本操作会提交当前事务。

**语法如下：**

```
PROCEDURE SET_TABLE_STATS (
    OWNNAME         VARCHAR2,
    TABNAME         VARCHAR2,
    PARTNAME        VARCHAR2 DEFAULT NULL,
    STATTAB         VARCHAR2 DEFAULT NULL,
    STATID          VARCHAR2 DEFAULT NULL,
    NUMROWS         NUMBER DEFAULT NULL,
    NUMBLKS         NUMBER DEFAULT NULL,
    AVGRLEN         NUMBER DEFAULT NULL,
    FLAGS            NUMBER DEFAULT NULL,
    STATOWN         VARCHAR2 DEFAULT NULL,
    NO_INVALIDATE  BOOLEAN  DEFAULT TRUE,
    CACHEDBLK       NUMBER  DEFAULT NULL,
    CACHEHIT        NUMBER  DEFAULT NULL,
    FORCE           BOOLEAN DEFAULT FALSE,
    IM_IMCU_COUNT  NUMBER  DEFAULT NULL,
    IM_BLOCK_COUNT NUMBER  DEFAULT NULL,
    SCANRATE        NUMBER  DEFAULT NULL
);
```

**参数详解**

- OWNNAME
	模式名，区分大小写。
- TABNAME
	表名，区分大小写。
- PARTNAME
	分区表名，区分大小写；缺省为 NULL。
- STATTAB
	自定义统计信息表，区分大小写；缺省为 NULL，统计信息将直接更新到系统视图 SYS.SYSSTATS 中。
- STATID
	统计信息 ID，只有当 stattab 不为 NULL 的时候有效；缺省为 NULL。
- NUMROWS
	表/分区行数，缺省为 NULL，为 NULL 时如果待设置统计信息的表(stattab/SYS.SYSSTATS)中存在行数时不做修改，否则插入默认值 2000；若不为 NULL，则更新为指定行数，大小不超过 9223372036854775807(2^63-1)。
- NUMBLKS
	表/分区块数，缺省为 NULL，为 NULL 时如果待设置统计信息的表(stattab/SYS.SYSSTATS)中存在块数时不做修改，否则插入默认值 100；若不为 NULL，则更新为指定块数，大小不超过 9223372036854775807(2^63-1)。
- AVGRLEN
	表/分区平均行长，缺省为 NULL，为 NULL 时如果待设置统计信息的表(stattab/SYS.SYSSTATS)中存在平均列宽时不做修改，否则插入默认值 100；若不为 NULL，则更新为指定行长，大小不超过 2147483647(2^31-1)。
- FLAGS
	保留参数，仅供内部使用。
- STATOWN
	自定义统计信息表所属的模式名。
- NO\_INVALIDATE
	是否让依赖游标失效，缺省为 TRUE。目前仅为保留参数，无实际作用。
- CACHEDBLK
	保留参数，段(索引/表/索引分区/表分区)在 buffer cache 中的平均块数；缺省为 NULL，仅供内部使用。
- CACHEHIT
	保留参数，段的平均缓存命中率；缺省为 NULL；仅供内部使用。
- FORCE
	是否忽略统计信息锁，强制设置指定表的指定统计信息，缺省为 FALSE；为 TRUE 表示被锁住也设置统计删除信息，为 FALSE 表示没有被锁住才能设置统计信息。
- IM\_IMCU\_COUNT
	表/分区中内存压缩单元的个数。目前仅为保留参数，无实际作用。
- IM\_BLOCK\_COUNT
	表/分区中内存块的个数。目前仅为保留参数，无实际作用。
- SCANRATE
	数据库扫描外部表的速率，以 MB/s 为单位。目前仅为保留参数，无实际作用。
21. IMPORT\_SCHEMA\_STATS

将所有对象的统计信息从指定的 STATTAB 导入到由 OWNNAME 标识的用户中，并将统计信息存入系统表。

统计信息导入时，导入对象完全由对象名称来确定，如果存在由系统根据 ID 自动创建的对象，例如在分区表主表上建立索引时，子表上自动建立的索引将根据索引 ID 来命名，统计信息表里存储的索引名称可能与新建立的分区表子表上的索引名称不一致，此时名称不一致的索引统计信息将无法导入。

不支持多列统计信息的导入。本操作会提交当前事务。

**语法如下：**

```
PROCEDURE IMPORT_SCHEMA_STATS(
        OWNNAME     VARCHAR(128), 
        STATTAB        VARCHAR(128), 
        STATID         VARCHAR(128) DEFAULT '',  
        STATOWN       VARCHAR(128) DEFAULT NULL,   
        NO_INVALIDATE  BOOLEAN to_no_invalidate_type(GET_PREFS('NO_INVALIDATE')), 
        FORCE          BOOLEAN      DEFAULT FALSE,   
        STAT_CATEGORY  VARCHAR(128) DEFAULT NULL 
);
```

**参数详解**

- OWNNAME
	待导入统计信息的 SCHEMA 名，区分大小写；缺省为当前模式。
- STATTAB
	存储统计信息的表，区分大小写。
- STATID
	统计信息 ID，用于区分表存储在同一个 stattab 中的多份统计信息； 缺省为空字符串。
- STATOWN
	STATTAB 所在的模式，区分大小写；缺省为当前模式。
- NO\_INVALIDATE
	是否让依赖游标失效，缺省为 TRUE。具体用法参考 GATHER\_TABLE\_STATS 方法的 NO\_INVALIDATE 参数。
- FORCE
	忽略统计信息锁；为 TRUE 表示即使表锁住了也导入统计信息，FALSE 表示只导入未上锁的统计信息；缺省为 FALSE。
- STAT\_CATEGORY
	仅作兼容 oracle 用，无实际作用。
22. IMPORT\_DATABASE\_STATS

将所有对象的统计信息从指定的 STATTAB 导入到数据库中，并将统计信息存入系统表。

统计信息导入时，导入对象完全由对象名称来确定，如果存在由系统根据 ID 自动创建的对象，例如在分区表主表上建立索引时，子表上自动建立的索引将根据索引 ID 来命名，统计信息表里存储的索引名称可能与新建立的分区表子表上的索引名称不一致，此时名称不一致的索引统计信息将无法导入。

不支持多列统计信息的导入。本操作会提交当前事务。

**语法如下**

```
PROCEDURE IMPORT_DATABASE_STATS(
        STATTAB         VARCHAR(128),
        STATID          VARCHAR(128) DEFAULT '',  
        STATOWN        VARCHAR(128) DEFAULT NULL,
        NO_INVALIDATE   BOOLEAN  to_no_invalidate_type(GET_PREFS('NO_INVALIDATE')),
        FORCE           BOOLEAN    DEFAULT FALSE,  
        STAT_CATEGORY   VARCHAR(128) DEFAULT NULL 
);
```

**参数详解**

- STATTAB
	指定要存储统计信息的表，区分大小写。
- STATID
	统计信息 ID，用于区分表存储在同一个 stattab 中的多份统计信息； 缺省为空字符串。
- STATOWN
	存储统计信息表的拥有者，区分大小写；缺省为当前模式。
- NO\_INVALIDATE
	是否让依赖游标失效，缺省为 TRUE。具体用法参考 GATHER\_TABLE\_STATS 方法的 NO\_INVALIDATE 参数。
- FORCE
	忽略统计信息锁；TRUE 表示即使表锁住了也导入统计信息，FALSE 表示只导入未上锁的统计信息；缺省为 FALSE。
- STAT\_CATEGORY
	仅作兼容 oracle 用，无实际作用
23. EXPORT\_SCHEMA\_STATS

导出由 ownname 标识的 schema 中全部对象的统计信息，并将它们存储到由 stattab 标识的用户统计信息表。

不支持多列统计信息的导出。本操作会提交当前事务。

**语法如下**

```
PROCEDURE EXPORT_SCHEMA_STATS(
     OWNNAME        VARCHAR(128), 
     STATTAB          VARCHAR(128),  
     STATID            VARCHAR(128) DEFAULT '',   
     STATOWN          VARCHAR(128) DEFAULT NULL,  
     STAT_CATEGORY   VARCHAR(128) DEFAULT NULL
);
```

**参数详解**

- OWNNAME
	待导出统计信息的 SCHEMA 名，区分大小写；缺省为当前模式。
- STATTAB
	指定要存储统计信息的表，区分大小写。
- STATID
	统计信息 ID，用于区分表存储在同一个 stattab 中的多份统计信息； 缺省为空字符串。
- STATOWN
	存储统计信息表的拥有者，区分大小写；缺省为当前模式。
- STAT\_CATEGORY
	仅作兼容 oracle 用，无实际作用。
24. EXPORT\_DATABASE\_STATS

导出数据库中所有对象的统计信息，并存储将他们存储到由 statown.stattab 标识的用户统计信息表。

不支持多列统计信息的导出。本操作会提交当前事务。

**语法如下：**

```
PROCEDURE EXPORT_DATABASE_STATS(
     STATTAB          VARCHAR(128),  
     STATID            VARCHAR(128) DEFAULT '',  
     STATOWN          VARCHAR(128) DEFAULT NULL,  
     STAT_CATEGORY   VARCHAR(128) DEFAULT NULL
);
```

**参数详解**

- STATTAB
	指定要存储统计信息的表，区分大小写。
- STATID
	统计信息 ID，用于区分表存储在同一个 stattab 中的多份统计信息； 缺省为空字符串。
- STATOWN
	存储统计信息表的拥有者，区分大小写；缺省为当前模式。
- STAT\_CATEGORY
	仅作兼容 oracle 用，无实际作用。
25. CONV\_DATA

用于将给定数据的字符串形式转换成系统表 SYSSTATS 中的 MIN/MAX 的格式。

例如：

(1)输入 INT 类型数据对应的字符串'1038'，最终输出'0x0E040000'。

(2)输入 interval year to month 类型数据的字符串'INTERVAL ''1-02'' YEAR(2) TO MONTH'（数据中有'需要转移成''），最终输出'010000000200000026010000'。

实际上，在当前包方法的处理中，即使通过该函数设置了 MIN/MAX，执行 set\_column\_stats 时也会检查直方图中的数据，根据用户自定义桶边界 ENDPOINT\_VALUE 重新设置 MIN/MAX 以保证直方图合法。

**语法如下：**

```
PROCEDURE CONV_DATA(
        OWNNAME              VARCHAR(128),   
        TABNAME                VARCHAR(128), 
        COLNAME               VARCHAR(128), 
        DATA                     VARCHAR2, 
        RESVAL                   OUT    VARCHAR2
   );
```

**参数详解**

- OWNNAME
	用户名，区分大小写。输入参数。
- TABNAME
	表名，区分大小写。只能是普通表表名或者分区表根表表名。输入参数。
- COLNAME
	列名，区分大小写。输入参数。
- DATA
	待转换数据的字符串形式。输入参数。
- RESVAL
	输出的数据。输出参数。
26. GET\_COLUMN\_STATS

用于从系统表 SYSSTATS 或者用户自定义统计信息表 STATTAB 中获取统计信息，输出到用户自定义的变量中。

默认从系统表 SYSSTATS 中读取数据；当指定用户自定义统计信息表 STATTAB 时，从 STATTAB 中读取。如果系统表 SYSSTATS 或者用户自定义统计信息表 STATTAB 中没有对应表的统计信息时会报错。

使用该方法时，可以输出的信息包括：DISTCNT、NULLCNT、SREC.EPC、SREC.MINVAL、SREC.MAXVAL、AVGCLEN，其他直方图信息仍需要用户手动设置。

**语法如下：**

```
PROCEDURE GET_COLUMN_STATS(
        OWNNAME        VARCHAR2,  
        TABNAME         VARCHAR2,   
        COLNAME         VARCHAR2,           
        PARTNAME        VARCHAR2 DEFAULT NULL,  
        STATTAB           VARCHAR2 DEFAULT NULL,   
        STATID             VARCHAR2 DEFAULT NULL,   
        DISTCNT            OUT NUMBER,  
        DENSITY         OUT NUMBER,   
        NULLCNT           OUT NUMBER,    
        SREC                OUT STATREC,      
        AVGCLEN           OUT NUMBER,     
        STATOWN           VARCHAR2 DEFAULT NULL,  
        REALTIME_STATS  BOOLEAN DEFAULT TRUE  
    );
```

**参数详解**

- OWNNAME
	用户名，区分大小写。输入参数。
- TABNAME
	表名，区分大小写。输入参数。
- COLNAME
	列名，区分大小写。输入参数。
- PARTNAME
	分区名，区分大小写。输入参数。
- STATTAB
	自定义统计信息表名，区分大小写。输入参数。
- STATID
	自定义统计信息 ID。输入参数。
- STATOWN
	自定义统计信息表所属用户。输入参数。
- REALTIME\_STATS
	无实际作用，仅做兼容 ORACLE 使用。输入参数。
- DISTCNT
	唯一值个数。输出参数。
- DENSITY
	无实际作用，仅做兼容 ORACLE 使用。输出参数。
- NULLCNT
	空值个数。输出参数。
- SREC
	存储自定义统计信息相关信息的内部结构。输出参数。
- AVGCLEN
	平均列宽。输出参数。
27. PREPARE\_COLUMN\_VALUES

用于将用户自定义的桶边界数组写入到自定义的 STATREC 结构中。

**语法如下：**

```
PROCEDURE  PREPARE_COLUMN_VALUES(
    SREC        IN OUT STATREC,
    CHARVALS    CHARARRAY
);
PROCEDURE PREPARE_COLUMN_VALUES(
    SREC        IN OUT STATREC,
    NUMVALS     NUMARRAY
);
PROCEDURE PREPARE_COLUMN_VALUES(
    SREC        IN OUT STATREC,
    TSVALS        DATEARRAY
);
```

**参数详解**

- CHARVALS
	字符类型都通过 CHARARRAY 类型存储，包括 CHAR、VARCHAR、BINARY 等所有支持收集统计信息的字符类型。输入参数。
- NUMVALS
	数字类型都通过 NUMARRAY 类型存储，包括 INT、DOUBLE、FLOAT、DEC 等所有支持收集统计信息的数字类型。输入参数。
- TSVALS
	日期类型都通过 DATEARRAY 类型存储，包括 DATETIME、DATE、DATETIME WITH TIME ZONE、TIMESTAMP、TIME、TIME WITH TIME ZONE、INTERVAL YEAR TO MONTH、INTERVAL DAY TO SECOND。输入参数。
- SREC.CHVALS
	输出参数，存储自定义统计信息相关信息的内部结构，当输入为 CHARVALS 时，将输出此项。
- SREC.NOVALS
	输出参数，存储自定义统计信息相关信息的内部结构，当输入为 NUMVALS 时，将输出此项。
- SREC.DTVALS
	输出参数，存储自定义统计信息相关信息的内部结构，当输入为 TSVALS 时，将输出此项。
28. SET\_COLUMN\_STATS

用于将用户自定义的统计信息写入到指定的统计信息表。

默认写入系统表 SYSSTATS；当指定用户自定义统计信息表 STATTAB 时，写入 STATTAB。

**语法如下：**

```
PROCEDURE SET_COLUMN_STATS(
        OWNNAME          VARCHAR2,  
         TABNAME             VARCHAR2,  
        COLNAME            VARCHAR2,  
        PARTNAME           VARCHAR2    DEFAULT NULL,  
        STATTAB               VARCHAR2    DEFAULT NULL,  
        STATID                  VARCHAR2    DEFAULT '',  
        DISTCNT               NUMBER      DEFAULT NULL,  
        DENSITY           NUMBER      DEFAULT NULL,
        NULLCNT              NUMBER      DEFAULT NULL,  
        SREC                     STATREC     DEFAULT NULL, 
        AVGCLEN              NUMBER      DEFAULT NULL,  
        FLAGS                   NUMBER      DEFAULT NULL,  
        STATOWN              VARCHAR2    DEFAULT NULL,  
        NO_INVALIDATE    BOOLEAN     DEFAULT NULL, 
        FORCE                    BOOLEAN     DEFAULT FALSE
);
```

**参数详解**

- OWNNAME
	用户名，区分大小写。
- TABNAME
	表名，区分大小写。
- COLNAME
	列名，区分大小写。
- PARTNAME
	分区名，区分大小写。
- STATTAB
	自定义统计信息表，区分大小写。
- STATID
	自定义统计信息表中的 ID。
- DISTCNT
	唯一值个数，缺省为 NULL。
- DENSITY
	无实际作用，仅做兼容 ORACLE 使用。
- NULLCNT
	空值个数，缺省为 NULL。
- SREC
	存储自定义统计信息相关信息的内部结构，缺省为 NULL。
- AVGCLEN
	平均列宽，缺省为 NULL。
- FLAGS
	无实际作用，仅做兼容 ORACLE 使用。
- STATOWN
	存储自定义统计信息相关信息的用户。
- NO\_INVALIDATE
	是否让依赖游标失效，缺省为 TRUE。
- FORCE
	忽略统计信息锁；TRUE 表示即使表锁住了也允许设置自定义统计信息，FALSE 表示只允许设置未上锁的统计信息。

**使用说明：**

用户自定义统计信息不能生成合法的直方图时，系统将进行报错提示，如下表所示。

表19.6 SET\_COLUMN\_STATS错误码

| **代码** | **解释** |
| --- | --- |
| \-4138 | 桶内数据个数数组 SREC.EHCNTS 或桶内数据唯一值个数数组 SREC.EDCNTS 错误 |
| \-4139 | 桶边界数组错误，可能是 SREC.NOVALS、SREC.CHVALS、SREC.DTVALS |
| \-4140 | 自定义数据超过表行数，可能是 DISTCNT、SAMPLE、SREC.EPC、SAMPLE+NULLCNT |
| \-4141 | 桶边界数组未严格按升序排序，可能是 SREC.NOVALS、SREC.CHVALS、SREC.DTVALS |
| \-4142 | 桶边界个数数组 SREC.EKHCNTS 或 桶内数据唯一值个数数组 SREC.EDCNTS 错误 |
| \-4143 | 不支持的数据类型 |

29. IMPORT\_TABLE\_STATS\_CUSTOM

把统计信息表中的统计信息导入到目标表中。

**语法如下：**

```
PROCEDURE IMPORT_TABLE_STATS_CUSTOM(
    OWNNAME                VARCHAR(128),
    TABNAME                VARCHAR(128),
    PARTNAME            VARCHAR(128)     DEFAULT NULL,
    STATTAB                VARCHAR(128),
    STATID                VARCHAR(128)    DEFAULT '',
    CASCADE                BOOLEAN        DEFAULT TRUE,
    STATOWN                VARCHAR(128)     DEFAULT NULL,
    NO_INVALIDATE        BOOLEAN            DEFAULT NULL,
    FORCE                BOOLEAN            DEFAULT FALSE,
    STAT_CATEGORY        VARCHAR(128)     DEFAULT NULL,
    SRC_OWNNAME            VARCHAR(128)     DEFAULT NULL,
    SRC_TABNAME            VARCHAR(128)     DEFAULT NULL,
    SRC_PARTNAME        VARCHAR(128)     DEFAULT NULL
);
```

**参数详解**

- OWNNAME
	目标表的模式名，区分大小写。
- TABNAME
	目标表名，区分大小写。
- PARTNAME
	目标表分区名，如果不指定分区，则一起导入所有子表的统计信息，缺省为 NULL。
- STATTAB
	统计信息表名，区分大小写。
- STATID
	由用户指定的统计信息标识名，缺省为空字符串。
- CASCADE
	是否连列和索引的统计信息一起导出，缺省为 TRUE。
- STATOWN
	统计信息表的模式名，区分大小写，缺省为 NULL。
- NO\_INVALIDATE
	是否让依赖游标失效，缺省为 TRUE。具体用法请参考 GATHER\_TABLE\_STATS 方法的 NO\_INVALIDATE 参数。
- FORCE
	是否忽略统计信息锁，强制把统计信息表中的统计信息导入到目标表中，缺省为 FALSE。为 TRUE 时表示忽略统计信息锁，强制向被锁住的目标表导入统计信息；为 FALSE 时表示仅当目标表没有被锁住才能导入统计信息。
- STAT\_CATEGORY
	保留参数，无实际意义。
- SRC\_OWNNAM
	源表模式名，区分大小写；如果不指定源表模式名，则默认为目标表的模式名。
- SRC\_TABNAME
	源表名，区分大小写；如果不指定源表名，则默认为目标表名。
- SRC\_PARTNAME
	源表分区名；如果不指定分区名，则一起导入所有子表的统计信息，缺省为 NULL。

**使用说明：**

使用 IMPORT\_TABLE\_STATS\_CUSTOM 进行统计信息导入时需要注意：

（1）如果 SRC\_OWNNAME、SRC\_TABNAME、SRC\_PARTNAME 均设置为 NULL，则方法功能与 IMPORT\_TABLE\_STATS 无区别；

（2）如果设置了 SRC\_OWNNAME、SRC\_TABNAME、SRC\_PARTNAME，导入对象统计信息时将根据源对象名称来确定；用户名和表名不一致时，分区名\\列名\\索引名一致允许导入对应的统计信息，否则跳过不导入；目标表和源表的层次一致时，允许导入统计信息，否则报错“-4136，源分区和目的分区类型不同”。

如下例表示把自定义统计信息表 USER1.STAT\_TAB 中，STATID 为 A，OWNNAME 为'USER1'，TABNAME=>'T1'的统计信息导入到 USER2.T2 中。

```
DBMS_STATS.IMPORT_TABLE_STATS_CUSTOM(OWNNAME=>'USER2',TABNAME=>'T2',STATTAB=>'STAT_TAB',STATID=>'A',STATOWN=>'USER1',SRC_OWNNAME=>'USER1',SRC_TABNAME=>'T1');
```

## 19.3 约束

以下对象不支持统计信息：

1. 视图、物化视图、外部表、DBLINK 远程表、动态视图表、记录类型数组所用的临时表、局部临时表。
2. 位图索引、位图连接索引、虚索引、空间索引、数组索引、无效的索引。
3. 所在表空间为 OFFLINE 的对象。
4. BLOB、IMAGE、LONGVARBINARY、CLOB、TEXT、LONGVARCHAR、自定义类型列和空间类型列等列类型不支持统计信息，在使用 GATHER\_TABLE\_STATS()方法收集列统计信息时，这些类型的列会被忽略。
5. ROWID，ROWNUM 等特殊列。

## 19.4 举例说明

使用包内的过程和函数之前，如果还未创建过系统包，请先调用系统过程创建系统包。

```
SP_CREATE_SYSTEM_PACKAGES (1,'DBMS_STATS');
SET SERVEROUTPUT ON;  //PRINT需要设置这条语句，才能打印出消息
```

例 1 收集模式 PERSON 下表 ADDRESS 的统计信息，并打印收集的表信息。

```
BEGIN
    DECLARE 
    OBJTAB DBMS_STATS.OBJECTTAB;
    OBJ_FILTER_LIST DBMS_STATS.OBJECTTAB;
    BEGIN
        OBJ_FILTER_LIST(0).OWNNAME = 'PERSON';
        OBJ_FILTER_LIST(0).OBJTYPE = 'TABLE';
        OBJ_FILTER_LIST(0).OBJNAME = 'ADDRESS';
    DBMS_STATS.GATHER_SCHEMA_STATS(
        'PERSON', 
        100,
        FALSE,
        'FOR ALL COLUMNS SIZE AUTO',
        1,
        'AUTO',
        TRUE,
        NULL,
        NULL,
        'GATHER',
        OBJTAB,
        NULL,
        TRUE,
        TRUE,
        OBJ_FILTER_LIST
    );
    PRINT OBJTAB.COUNT;
        FOR I IN 0..OBJTAB.COUNT-1 LOOP
            PRINT OBJTAB(I).OWNNAME;
            PRINT OBJTAB(I).OBJTYPE;
            PRINT OBJTAB(I).OBJNAME;
            PRINT '-------- ';
        END LOOP;
    END;
END;
/
```

打印结果如下：

```
1
PERSON
TABLE
ADDRESS
--------
```

例 2 获得 PERSON 模式下表 ADDRESS 中列 ADDRESSID 的统计信息。

```
DBMS_STATS.COLUMN_STATS_SHOW('PERSON','ADDRESS','ADDRESSID');
```

返回结果集 1：

```
LINEID NUM_DISTINCT  LOW_VALUE  HIGH_VALUE  NUM_NULLS  NUM_BUCKETS  SAMPLE_SIZE          HISTOGRAM
---------- -------------------- --------- ---------- -----------------------------------------------
1          6        1         6          0            6           6        FREQUENCY
```

结果集 2：

```
OWNER TABLE_NAME COLUMN_NAME HISTOGRAM ENDPOINT_VALUE ENDPOINT_HEIGHT ENDPOINT_KEYHEIGHT ENDPOINT_DISTINCT
PERSON ADDRESS ADDRESSID FREQUENCY 1 1 NULL NULL
PERSON ADDRESS ADDRESSID FREQUENCY 2 1 NULL NULL
PERSON ADDRESS ADDRESSID FREQUENCY 3 1 NULL NULL
PERSON ADDRESS ADDRESSID FREQUENCY 4 1 NULL NULL
PERSON ADDRESS ADDRESSID FREQUENCY 5 1 NULL NULL
PERSON ADDRESS ADDRESSID FREQUENCY 6 1 NULL NULL
```

例 3 删除 PERSON 模式下表 ADDRESS 的统计信息。

```
BEGIN
    DBMS_STATS.DELETE_TABLE_STATS ('PERSON', 'ADDRESS');
END;
/
```

例 4 自动收集用户表的统计信息。

第一步，打开监控。

设置 INI 参数 AUTO\_STAT\_OBJ 为 1 或 2。1：对所有表进行监控；2：只对用户通过 DBMS\_STATS. SET\_TABLE\_PREFS 设置过 STALE\_PERCENT 属性的表对象进行监控。如果 AUTO\_STAT\_OBJ=2，需进一步使用 DBMS\_STATS.SET\_TABLE\_PREFS 设置 STALE\_PERCENT 属性。

用 AUTO\_STAT\_OBJ=1 打开对 T 表的监控。

```
create table t(a int);
SP_SET_PARA_VALUE(1,'AUTO_STAT_OBJ',1);
```

用 AUTO\_STAT\_OBJ=2 打开对 T 表的监控。

```
create table t(a int);
SP_SET_PARA_VALUE(1,'AUTO_STAT_OBJ',2);
DBMS_STATS.SET_TABLE_PREFS('SYSDBA','T','STALE_PERCENT',15);
--对修改行数占比达到STALE_PERCENT要求即占比达到15%的对象收集统计信息
```

下面以 AUTO\_STAT\_OBJ=2 为例。

第二步，执行统计信息收集操作。自动收集统计信息使用 SP\_CREATE\_AUTO\_STAT\_TRIGGER 设置触发器。

```
SP_CREATE_AUTO_STAT_TRIGGER(1, 1, 1, 1,'11:20', '2024/12/10',0,1);
```

此处，也可将自动收集方法换成手动收集方法，其它三步用法不变。

第三步，对用户表 T 进行增删改操作。

```
insert into t select level connect by level<=20;
commit;
```

第四步，通过系统表 SYSSTATTABLEIDU 和动态视图 V$AUTO\_STAT\_TABLE\_IDU 查看监控信息，通过系统表 SYSSTATS 查看统计信息。

打开监控后并执行统计信息收集操作之后才能查看到 SYSSTATTABLEIDU 和 SYSSTATS 的变化。SYSSTATTABLEIDU 为 AUTO\_STAT\_OBJ 等于 1 或 2 时对上一次的统计信息的监控。V$AUTO\_STAT\_TABLE\_IDU 为 AUTO\_STAT\_OBJ 等于 1 时的统计信息实时监控，不需要执行收集统计信息操作也能查看。

下面以 AUTO\_STAT\_OBJ=2 为例。

查看监控信息：

```
//在触发器触发之后查看
SELECT * FROM SYSSTATTABLEIDU;

行号       ID          TOTAL_ROWS           INSERT_ROWS          DELETE_ROWS          UPDATE_ROWS      LAST_STAT_DT         MONITOR_FLAG RSVD1      TRUNCATED
---------- ----------- -------------------- -------------------- 
1          1061        20                   0                    0                    0                    2024-12-19 14:09:16.978000 2            0XFFFFFFFF 0
```

查看统计信息：

```
SELECT * FROM SYSSTATS WHERE ID=1061;
LINEID   ID    COLID   T_FLAG T_TOTAL  N_SAMPLE   N_DISTINCT   N_NULL   V_MIN      V_MAX  BLEVEL   N_LEAF_PAGES  N_LEAF_USED_PAGES  CLUSTER_FACTOR N_BUCKETS  
DATA   COL_AVG_LEN LAST_GATHERED  INFO1      INFO2   
--------------------------------- -------------------------- -------------------
1          1061        -1          T      20                   0                    0                    0                    NULL       NULL       0           1                    1
           0              0
           0X0000FFFF00000700
           -1          2024-12-19 14:09:17.001081 NULL       NULL

2          1061        0           C      20                   20                   20                   0                    0X01000000 0X14000000 0           1                    1
           0              20
0X1400010008000700010000000100000001000000020000000100000003000000010000000400000001000000050000000100000006000000010000000700000001000000080000000100000009000000010000000A000000010000000B000000010000000C000000010000000D000000010000000E000000010000000F00000001000000100000000100000011000000010000001200000001000000130000000100000014000000
           4           2024-12-19 14:09:16.998000 NULL       NULL
```

如果用户想进一步对监控统计信息进行收集，可以参考《DM8 系统管理员手册》的 22.5 统计信息章节 SYSDBA.GET\_AUTO\_STAT\_INFO\_FUNC 用法。
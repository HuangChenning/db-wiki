---
title: "间隔分区"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle28.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 间隔分区

间隔（interval）分区是一种特殊的范围分区。当插入或更新的数据找不到匹配的分区时，可以根据间隔值自动创建分区。这种方法简化了分区管理，避免了手动创建新分区的繁琐过程。目前仅支持interval分区的基本功能。

说明：

该功能仅在oracle模式下可以使用。

该功能在V9.0.5及以后的版本中支持。

间隔分区目前支持的功能有：

- 创建interval分区表和interval复合分区表
- 自动创建interval分区
- 手动创建interval分区
- 修改interval分区间隔
- 其他功能保持同范围分区一致

## 创建interval分区表

支持手动创建和自动创建interval分区两种方式。

### 手动创建interval分区

#### 说明

语法:

CREATE TABLE partition\_table\_name

( \[column\_name data\_type\]

\[,... \]

) PARTITION BY RANGE (partition\_key) **INTERVAL (interval\_expr)**

CREATE TABLE table\_name

PARTITION OF parent\_table \[ (

{ column\_name \[ WITH OPTIONS \] \[ column\_constraint \[... \] \]

| table\_constraint }

\[,... \]

) \] { FOR VALUES partition\_bound\_spec }

and partition\_bound\_spec is:

FROM ( { partition\_bound\_expr | MINVALUE | MAXVALUE } \[,...\] )

TO ( { partition\_bound\_expr | MINVALUE | MAXVALUE } \[,...\] )

说明：

- \[在原有的范围表语法上新增INTERVAL语句（加粗部分）\]{.mark}；
- partition\_key是分区键列，只支持数值和日期类型：int、float、number、numeric、date、timestamp，这些数据类型具有明确的顺序和范围，便于数据库根据其值来判断是否需要创建新的分区；
- interval\_expr是任何无变量表达式（不允许子查询、窗口函数、聚合函数和集返回函数），它的数据类型必须与相应分区键列的数据类型相匹配，表达式在表创建时只计算一次。

#### 示例

创建分区表之后，需要手动创建初始分区，初始分区中的范围高值不能是MAXVALUE，将初始分区的高值作为基准值base\_value。

CREATE TABLE sales (id int) PARTITION BY RANGE(id) INTERVAL (10);

CREATE TABLE sales\_first PARTITION OF sales FOR VALUES FROM (MINVALUE)  
TO (10);

### 自动创建interval分区

#### 说明

插入或更新的数据不能匹配到已有的分区时，分区表会自动创建分区。分区自动继承分区表的全部列定义、主外键索引和约束、唯一索引和约束、NOT  
NULL约束和CHECK约束。分区自动继承分区表的全局或者本地临时表属性。

创建interval分区时对分区表加SHARE UPDATE  
EXCLUSIVE，不阻塞正常的读写操作。

将第一个分区的高值作为基准值base\_value，新插入的数据的分区键值大于等于base\_value时会就会触发新建分区。后续自动创建的分区范围为：(  
base\_value + interval\_value \* n, base\_value + interval\_value \* (n+1)  
)，其中n >= 1。

#### 示例

drop table sales;

CREATE TABLE sales (id int) PARTITION BY RANGE(id) INTERVAL (10);

CREATE TABLE sales\_first PARTITION OF sales FOR VALUES FROM (MINVALUE)  
TO (10);

\-- 插入数据，自动创建interval分区

INSERT INTO sales VALUES(11);

### 创建interval复合分区表

#### 说明

支持创建interval复合分区表。由于不支持子分区模板，子分区表需要手动创建。支持自动创建interval分区。

语法：

CREATE TABLE partition\_table\_name

( \[column\_name data\_type\]

\[,... \]

) PARTITION BY RANGE (partition\_key) INTERVAL (interval\_expr)

CREATE TABLE table\_name

PARTITION OF parent\_table \[ (

{ column\_name \[ WITH OPTIONS \] \[ column\_constraint \[... \] \]

| table\_constraint }

\[,... \]

) \] { FOR VALUES partition\_bound\_spec }

\[ PARTITION BY { RANGE | LIST | HASH } ( { column\_name | (  
expression ) } \[ COLLATE collation \] \[ opclass \] \[,... \] ) \]

#### 示例

drop table sales;

CREATE TABLE sales (id int) PARTITION BY RANGE(id) INTERVAL (10);

\-- 创建sales\_first分区，该分区又是一张分区表

CREATE TABLE sales\_first PARTITION OF sales FOR VALUES FROM (MINVALUE)  
TO (10) PARTITION BY LIST(id);

\-- 创建sales\_first的二级分区

CREATE TABLE sales\_first\_p1 PARTITION OF sales\_first FOR VALUES IN  
(0,1,2,3,4);

CREATE TABLE sales\_first\_p2 PARTITION OF sales\_first FOR VALUES IN  
(5,6,7,8,9);

\-- 自动创建interval分区

INSERT INTO sales values(17);

## 维护interval分区表

支持对interval分区进行修改、删除、附加和分离操作。也支持对范围分区表和interval分区表进行转换。

### 修改interval分区表的分区间隔

修改分区间隔后，会将基准值更新为当前所有分区的最高值。

语法：

ALTER TABLE partition\_table\_name SET INTERVAL(interval\_expr);

#### 示例

drop table sales;

CREATE TABLE sales (id int) PARTITION BY RANGE(id) INTERVAL (10);

CREATE TABLE sales\_first PARTITION OF sales FOR VALUES FROM (MINVALUE)  
TO (10);

\-- 自动创建interval分区

INSERT INTO sales values(17);

\-- 查看表结构

\[highgo=# \\d sales\_first\]{.mark}

数据表 "public.sales\_first"

栏位 | 类型 | 校对规则 | 可空的 | 预设

\------+---------+----------+--------+------

id | integer | | |

分区: sales FOR VALUES FROM (MINVALUE) TO (10)

\-- 查看自动创建的表的结构

\[highgo=# \\d sales\_sys\_p\]{.mark}

数据表 "public.sales\_sys\_p"

栏位 | 类型 | 校对规则 | 可空的 | 预设

\------+---------+----------+--------+------

id | integer | | |

分区: sales FOR VALUES FROM (10) TO (20)

\--修改分区间隔

ALTER TABLE sales SET INTERVAL(20);

\-- 此时，插入数据21

INSERT INTO sales values(21);

\-- 会看到新建了一个表sales\_sys\_p1，表结构如下：

\[highgo=# \\d sales\_sys\_p1\]{.mark}

数据表 "public.sales\_sys\_p1"

栏位 | 类型 | 校对规则 | 可空的 | 预设

\------+---------+----------+--------+------

id | integer | | |

分区: sales FOR VALUES FROM (20) TO (40)

### 删除interval分区表

同其他分区表一致，使用DROP TABLE删除interval分区表，删除interval分区表时自动删除其所有的分区。

### 删除interval分区

同其他分区表一致，使用DROP TABLE删除分区。如果删除的分区范围大于基准值，再次插入该范围内数据时会重新创建相应的分区。

#### 示例

drop table sales;

CREATE TABLE sales (id int) PARTITION BY RANGE(id) INTERVAL (10);

CREATE TABLE sales\_first PARTITION OF sales FOR VALUES FROM (MINVALUE)  
TO (10);

INSERT INTO sales VALUES(11);

\-- 删除分区

DROP TABLE sales\_sys\_p;

### 附加/分离interval分区

同HGDB V9的范围分区表的附加/分离功能完全一致。

附加的分区需要满足interval分区表的范围限制，即：( base\_value + interval\_value \* n, base\_value + interval\_value \* (n+1) )，其中n >=  
1。

语法：

ALTER TABLE partition\_table\_name ATTACH PARTITION table\_name...;

ALTER TABLE partition\_table\_name DETACH PARTITION table\_name...;

#### 示例

drop table sales;

CREATE TABLE sales (id int) PARTITION BY RANGE(id) INTERVAL (10);

CREATE TABLE sales\_first PARTITION OF sales FOR VALUES FROM (MINVALUE)  
TO (10);

\-- 分离sales\_first分区

ALTER TABLE sales DETACH PARTITION sales\_first;

\-- 将sales\_first表附加到sales分区表上

ALTER TABLE sales attach PARTITION sales\_first for values from (0) to  
(10);

### 范围分区表和interval分区表的转换

对范围分区表设置间隔值则转换为interval分区表，将interval分区表的间隔设置为空则转换为范围分区表。如果范围分区表的高值不存在（比如范围值设置了MAXVALUE），则无法设置interval，SET INTERVAL将报错。

语法：

ALTER TABLE partition\_table\_name SET INTERVAL(interval\_expr);

ALTER TABLE partition\_table\_name SET INTERVAL();

#### 示例

\--创建分区表

drop table sales;

CREATE TABLE sales (id int) PARTITION BY RANGE(id) INTERVAL (10);

CREATE TABLE sales\_first PARTITION OF sales FOR VALUES FROM (MINVALUE)  
TO (10);

\-- 插入数据，自动创建一个分区

INSERT INTO sales VALUES(11);

\-- 查看父表的表信息

highgo=# \\d+ sales

分区表 "public.sales"

栏位 | 类型 | 校对规则 | 可空的 | 预设 | 存储 | 压缩 | 统计目标  
| 描述

\------+---------+----------+--------+------+-------+------+----------+------

id | integer | | | | plain | | |

分区键值: RANGE (id)

Range interval: INTERVAL (10) BASEVALUE (10)

分区: sales\_first FOR VALUES FROM (MINVALUE) TO (10),

sales\_sys\_p FOR VALUES FROM (10) TO (20)

\-- 将interval分区表转换为范围分区表

ALTER TABLE sales SET INTERVAL();

\-- 再次查看表结构

highgo=# \\d+ sales

分区表 "public.sales"

栏位 | 类型 | 校对规则 | 可空的 | 预设 | 存储 | 压缩 | 统计目标  
| 描述

\------+---------+----------+--------+------+-------+------+----------+------

id | integer | | | | plain | | |

分区键值: RANGE (id)

分区: sales\_first FOR VALUES FROM (MINVALUE) TO (10),

sales\_sys\_p FOR VALUES FROM (10) TO (20)

\-- 将范围分区表转换为interval分区表

ALTER TABLE sales SET INTERVAL(20);

\-- 查看表结构

highgo=# \\d+ sales

分区表 "public.sales"

栏位 | 类型 | 校对规则 | 可空的 | 预设 | 存储 | 压缩 | 统计目标  
| 描述

\------+---------+----------+--------+------+-------+------+----------+------

id | integer | | | | plain | | |

分区键值: RANGE (id)

Range interval: INTERVAL (20) BASEVALUE (20)

分区: sales\_first FOR VALUES FROM (MINVALUE) TO (10),

sales\_sys\_p FOR VALUES FROM (10) TO (20)

## 备份恢复

### 支持interval分区的备份和恢复

备份和恢复基本上同范围分区一致，唯一的区别是interval分区在创建范围分区表后需要执行ALTER table partition\_table\_name SET INTERVAL(interval\_expr)将其设置为interval分区。

#### 示例

执行上一章节的命令后，执行pg\_dump：

pg\_dump -U highgo -p 1521 highgo > interval.sql

备份文件大概内容如下：

CREATE TABLE public.sales (

id integer

)

PARTITION BY RANGE (id) INTERVAL (20) BASEVALUE (20);

ALTER TABLE public.sales OWNER TO highgo;

\--

\-- Name: sales\_first; Type: TABLE; Schema: public; Owner: highgo

\--

CREATE TABLE public.sales\_first (

id integer

);

ALTER TABLE public.sales\_first OWNER TO highgo;

\--

\-- Name: sales\_sys\_p; Type: TABLE; Schema: public; Owner: highgo

\--

CREATE TABLE public.sales\_sys\_p (

id integer

);

ALTER TABLE public.sales\_sys\_p OWNER TO highgo;

ALTER TABLE ONLY public.sales ATTACH PARTITION public.sales\_first FOR  
VALUES FROM (MINVALUE) TO (10);

\--

\-- Name: sales\_sys\_p; Type: TABLE ATTACH; Schema: public; Owner: highgo

\--

ALTER TABLE ONLY public.sales ATTACH PARTITION public.sales\_sys\_p FOR  
VALUES FROM (10) TO (20);

## 使用限制

INTERVAL分区表的使用限制如下：

- INTERVAL分区表限制为单个分区键，该键必须是数字或日期范围。
- 必须为INTERVAL分区表定义至少一个分区。
- 不能为INTEVAL分区表定义DEFAULT和MAXVALUE。
- 在复合分区中，INTERVAL分区可用于主分区机制，不支持子分区级别。
- 不能在分区键列中指定NULL、infinity值。
- INTERVAL分区表达式必须为常量，且不能为负数。

另外，HGDB V9原生分区表的使用限制仍然存在：

- 分区表上的唯一约束（以及主键）必须包括所有分区键列。这种限制的存在是因为构成约束的各个索引只能直接在它们自己的分区内强制唯一性；因此，分区结构本身必须保证不同分区中不存在重复项。
- 无法创建跨越整个分区表的排它约束。只能单独对每个分区设置这样的约束。同样，这种限制源于无法实施跨分区限制。
- 在 INSERT上的BEFORE ROW触发器无法更改新行的最终目标分区。
- 不允许在同一个分区树中混杂临时关系和持久关系。因此，如果分区表是持久的，则其分区也必须是持久的，反之亦然。在使用临时关系时，分区数的所有成员都必须来自于同一个会话。
- 分区不能包含父分区中不存在的列。使用CREATE  
	TABLE创建分区时不可能指定列，也不可能在事后使用ALTER  
	TABLE向分区添加列。只有当表的列与父级完全匹配时，才可以使用ALTER  
	TABLE... ATTACH PARTITION将表添加为分区。
- 分区表的CHECK和NOT  
	NULL约束总是由其所有分区继承。不允许在分区表上创建标记为NO INHERIT  
	的CHECK约束。如果父表中存在相同的约束，则不能在分区的列上删除NOT  
	NULL约束。
- 只要不存在分区，就只支持使用ONLY在分区表上添加或删除约束。一旦存在分区，使用ONLY将导致错误。相反，可以添加和删除分区本身的约束（如果它们不在父表中）。
- 由于分区表本身没有任何数据，尝试在分区表上使用TRUNCATE，ONLY将始终返回错误。
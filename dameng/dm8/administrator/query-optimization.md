---
title: "查询优化"
book: "DM8 系统管理员手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/query-optimization.html
tags:
  - dameng
  - dm8
  - administrator
---

数据库执行一条语句有多种方式，为了选择最优的执行方式，产生了查询优化器。查询优化器分析语句运行时的所有因素，选择最优的方式去执行，提高了查询效率。因此，查询优化是数据库执行 SQL 语句的重要过程，决定了数据库的查询性能。

## 22.1 优化目标

达梦数据库查询优化器的优化目标为最快响应时间。通过设置参数 FIRST\_ROWS 来决定优先返回多少条记录给用户，而不需要等待全部结果确定后再输出，FIRST\_ROWS 设置范围为 1~1000000，单位为行。例如：FIRST\_ROWS = 10，意思是查询出 10 条结果就立即返回给用户。可以根据实际情况，调整参数值。

## 22.2 查询优化器

查询优化器通过分析可用的执行方式和查询所涉及的对象统计信息来生成最优的执行计划。此外，如果存在 HINT 优化提示，优化器还需要考虑优化提示的因素。

查询优化器的处理过程包括：

1. 优化器生成所有可能的执行计划集合；
2. 优化器基于字典信息的数据分布统计值、执行语句涉及到的表、索引和分区的存储特点来估算每个执行计划的代价。代价是指 SQL 语句使用某种执行方式所消耗的系统资源的估算值。其中，系统资源消耗包括 I/O、CPU 使用情况、内存消耗等；
3. 优化器选择代价最小的执行方式作为该条语句的最终执行计划。

优化器所做的操作有：查询转换、估算代价、生成计划。

### 22.2.1 查询转换

查询转换是指把经过语法、语义分析的查询块之间的连接类型、嵌套关系进行调整，生成一个更好的查询计划。常用的查询转换技术包括过滤条件的下放、相关子查询的去相关性。

1. 过滤条件下放：在连接查询中，把部分表的过滤条件下移，在连接之前先过滤，可以减少连接操作的数据量，提升语句性能；
2. 相关子查询的去相关性：把与子查询相关的外表与内表采用半连接的方式执行，放弃默认采取的嵌套连接方式，对性能有较大提升。

### 22.2.2 估算代价

估算代价是指对执行计划的成本进行估算。执行节点之间的代价值相关性较强，一个执行节点的代价包括该节点包含的子节点代价。代价衡量指标包括选择率、基数、代价。

**1.选择率**

选择率是指满足条件的记录占总记录数的百分比。记录集可以是基表、视图、连接或分组操作的结果集。选择率和查询谓词相关，如 name = ‘韩梅梅’；或者是谓词的连接，如 name =‘韩梅梅’ and no =‘0123’。一个谓词可以看作是一个过滤器，过滤掉结果集中不满足条件的记录。选择率的范围从 0 到 1。其中，0 表示没有记录被选中，1 表示行集中所有记录都被选中。

如果没有统计信息，则优化器依据过滤条件的类型来设置对应的选择率。例如，等值条件的选择率低于范围条件选择率。这些假定是根据经验值，认为等值条件返回的结果集最少。

如果有统计信息，则可以使用统计信息来估算选择率。例如，对于等值谓词（name =‘韩梅梅’），如果 name 列有 N 个不同值，那么，选择率是 N 分之一。

**2.基数**

基数是指整个行集的行数，该行集可以是基表、视图、连接或分组操作的结果集。

**3.代价**

代价表示资源的使用情况。查询优化器使用磁盘 I/O、CPU 占用和内存使用作为代价计算的依据，所以代价可以用 I/O 数、CPU 使用率和内存使用一组值来表示。所有操作都可以进行代价计算，例如扫描基表、索引扫描、连接操作或者对结果集排序等。

访问路径决定了从一个基表中获取数据所需要的代价。访问路径可以是基表扫描、索引扫描等。在进行基表扫描或索引扫描时，一次 I/O 读多个页，所以，基表扫描或索引全扫描的代价依赖于表的数据页数和多页读的参数值。二级索引扫描的代价依赖于 B 树的层次、需扫描的叶子块树以及根据 ROWID 访问聚集索引的记录数。

连接代价是指访问两个连接的结果集代价与连接操作的代价之和。

### 22.2.3 生成计划

生成计划指计划生成器对给定的查询按照连接方式、连接顺序、访问路径生成不同的执行计划，选择代价最小的一个作为最终的执行计划。

连接顺序指不同连接项的处理顺序。连接项可以是基表、视图、或者是一个中间结果集。例如表 t1、t2、t3 的连接顺序是先访问 t1，再访问 t2，然后对 t1 与 t2 做连接生成结果集 r1，最后把 t3 与 r1 做连接。一个查询语句可能的计划数量是与 FROM 语句中连接项的数量成正比的，随着连接项的数量增加而增加。

## 22.3 数据访问路径

访问路径指从数据库中检索数据的方法。一般情况下，索引访问用于检索表的小部分数据，全表扫描用于访问表的大部分数据。OLTP 应用中，一般使用索引访问路径，因为 OLTP 中包含了许多高选择率的 SQL 语句。而决策支持系统则倾向于执行全表扫描来获取数据。从数据库中定位和检索数据的方法有：全表扫描、聚集索引扫描、二级索引扫描等。

全表扫描是指从基表中检索数据时，扫描该表中所有的数据。全表扫描方式适合检索表中大部分数据，这时比索引扫描更加有效率。

索引扫描是指通过指定语句中的索引列进行遍历来检索表中的数据。索引扫描是从基于一列或多列的索引中检索数据。索引不仅包含索引值，还包含对应表中数据的 ROWID。如果需要访问的不是索引列，这时需要通过 ROWID 或聚集索引来找到表中的数据行。

索引扫描包含聚集索引扫描和二级索引扫描。由于在聚集索引中，包含了表中所有的列值，所以检索数据时只需要扫描这一个索引就可以得到所有需要的数据。如果是二级索引，由于只包含索引列以及对应的 ROWID，如果查询列不在二级索引中则还需要扫描聚集索引来得到所需要的数据。

查询优化器选择访问路径基于以下几个因素：

1. 执行语句中可能的访问路径；
2. 估算每条执行路径的代价。为了选择一个访问路径，优化器首先会通过检查语句中的 FROM 子句和 WHERE 子句中的条件表达式来决定哪一个访问路径可以使用。优化器会根据可用的访问路径生成可能的执行计划集合，然后使用索引、列和表的统计信息来估算每个计划的代价。最后，优化器选择最小代价的那个执行计划。

影响优化器选择访问路径的因素有语句中的提示（HINT）和统计信息。用户可以在执行的语句中使用 HINT 来指定访问路径。而统计信息会根据表中数据的分布情况决定采用哪个访问路径会产生最小的代价。

## 22.4 连接

查询语句中 FROM 子句包含多个表时，我们称为连接查询。如 SELECT \* FROM t1,t2 就是连接查询。

生成连接查询的执行计划，需要考虑三方面因素：

1. **访问路径**

对于每张表采用何种方式来获取数据。例如：全表扫描、索引扫描等。

查询优化器会估算每种扫描方式的代价，选择代价较小的访问路径。

2. **连接方式**

确定两张表之间采用哪种连接方式。连接方式分为物理连接方式和逻辑连接方式。常见的物理连接方式有：哈希连接、嵌套连接、归并连接等。常见的逻辑连接方式有：内连接、外连接、半连接、反连接等。

一般的：存在等值连接条件可以选择哈希连接；不存在等值连接条件时可以选择嵌套连接；连接列均为索引列且连接条件是索引列之间的等值连接条件时，可以选择归并连接。

- 物理连接方式（连接算法实现）
1. 嵌套连接：嵌套连接又称嵌套循环连接（NEST LOOP JOIN）。相当于两张表进行笛卡尔积操作。此时，优化器会选择一张代价较小的表作为外表(驱动表)，另一张表作为内表，外表的每条记录与内表进行一次连接操作。嵌套连接可以经过优化实现索引连接（即索引嵌套连接）。索引连接与普通的嵌套连接不同的是，索引连接要求至少一侧有索引，且在有索引的一侧可以利用索引范围扫描替代全表扫描，从而实现比普通嵌套连接更好的性能。
2. 哈希连接：两张表进行等值连接时，可以选择哈希连接。以一张表的连接列为哈希键，构造哈希表，另一张表的连接列进行哈希探测，找到满足条件的记录。哈希连接的代价包括建立哈希表和哈希探测的代价。如果哈希连接键的数据倾斜性严重，导致某个哈希桶数据分布过于集中，可能影响对这个哈希桶的哈希探测性能。
3. 归并连接：两张表的连接列均有序且连接条件是连接列的等值连接，则可以进行归并连接，一趟归并就可以找出满足条件的记录。连接列有序可以通过索引扫描实现，如果查询列也属于索引列的子集，则归并连接只需扫描索引，会有更好的性能表现。此外连接列数据的有序性也可以通过额外增加排序实现。
- 逻辑连接方式
1. 内连接：内连接是指根据连接条件，结果集仅包含满足全部连接条件的记录。
2. 外连接：外连接是指根据连接条件，结果集除了包括满足全部连接条件的记录外，也额外返回特定侧不匹配的记录，并为不匹配记录的列填充 NULL 值。外连接分为左外连接，右外连接和全外连接。根据特定侧是仅左表，仅右表，左表和右表，分别对应左外连接，右外连接和全外连接。
3. 半连接：半连接分为左半连接和右半连接。用于检查外表中的行是否在内表中存在匹配行，只要找到一个匹配行就立刻停止搜索，并返回外表中的该行，内表数据不返回。左半连接指的是左表作为外表，右半连接指的是右表作为外表。
4. 反连接：反连接即反半连接。用于检查外表中的行是否不在内表中存在匹配行，返回外表在内表中没有匹配行的所有行。内表数据不返回。

例 1 左外连接

```
SELECT * FROM t1 LEFT OUTER JOIN t2 ON t1.c1=t2.d1;
```

例 1 中 t1 表为外表(左表)，如果 t2 表中不存在与 t1.c1 相等的记录，t2 表的该行记录用 NULL 填充。右外连接与左外类似。

例 2 全外连接

```
SELECT * FROM t1 FULL OUTER JOIN t2 ON t1.c1=t2.d1;
```

例 2 中分别以 t1 为左表进行左外和右外连接，两次结果进行 union，返回最终结果。

子查询会转换成半连接。共有四种半连接方式：哈希半连接、索引半连接、嵌套半连接、归并半连接。等值连接条件会选择哈希\\索引\\归并半连接，非等值连接条件会选择嵌套半连接。

1. 哈希半连接：以外表的连接列为 KEY 构造哈希表，内表的连接列进行探测来查找满足连接条件的记录；
2. 索引半连接：如果子查询的连接列为索引前导列，可采用索引半连接。处理过程为外表的数据对子查询使用索引查找，返回满足条件的记录；
3. 归并半连接：如果相关子查询的连接条件列均为索引列，可采用归并半连接。按照 索引顺序，对外表、内表进行同步扫描，返回满足条件的记录；
4. 嵌套半连接：如果连接条件为非等值，可转换为嵌套半连接。处理过程为外表的每条记录去遍历内表，返回满足条件的记录。
3. **连接顺序**

当超过 2 张表进行连接时，就需要考虑表之间的连接顺序。不合适的连接顺序对执行效率有较大影响。一般原则是，经过连接可以产生较小结果集的表优先处理。

一个连接查询通常会对应多个执行计划，查询优化器会根据优化规则、代价估算挑选最优的执行计划。

## 22.5 统计信息

对象统计信息描述了对象数据的分布特征。统计信息是优化器的代价计算的依据，可以帮助优化器较精确地估算成本，对执行计划的选择起着至关重要的作用。统计信息的收集频率是一把双刃剑，频率太低导致统计信息滞后，频率太高又影响查询性能，因此，系统管理员需要根据实际情况，合理安排统计信息收集的频率。

### 22.5.1 统计信息简介

#### 22.5.1.1 种类

达梦数据库的统计数据对象分三种：表统计信息、列统计信息和索引统计信息。统计信息生成过程分三个步骤：

1. 确定采样的对象：根据数据对象，确定需要分析哪些数据。  
	1）表：计算表的行数、所占的页数目。  
	2）列：统计列数据的分布特征。  
	3）索引：统计索引列的数据分布特征。
2. 确定采样率。用户根据统计数据对象的大小，确定采样率。如缺省，则默认通过内部算法确定数据的采样率。
3. 生成统计信息。根据不同的数据对象生成不同的统计信息。  
	1）表：表的行数、所占的页数目等汇总数据。  
	2）列和索引：将采样的数据按照不同的分布特征生成相应的直方图。有两种类型的直方图：频率直方图和等高直方图。根据算法分析表的数据分布特征（以不同值的数据量 1 万个为分界线），确定直方图的类型。频率直方图的每个桶(保存统计信息的对象)的高度不同，等高直方图每个桶的高度相同。生成直方图时，如果不同值少于 1 万个则用频率直方图，否则用等高直方图。

#### 22.5.1.2 作用

在执行查询时，如果数据对象存在统计信息，代价算法可以根据统计信息中的数据，比较精确地计算出操作所需花费的成本，以此来确定连接方式、对象访问路径、连接顺序，选择最优的执行计划。

#### 22.5.1.3 收集时机

收集统计信息的时机有两种：一是在查询之前进行静态收集；二是在查询的同时进行动态收集。

静态收集是在查询之前完成。和查询操作互不干涉，因此不影响查询性能。

动态收集是在查询的过程中完成。具体为在构造查询计划阶段进行，统计信息收集完成之后再继续构造计划，因此会影响计划阶段性能，特别是在高并发场景中。

从性能角度考虑，推荐用户使用静态收集。

### 22.5.2 统计信息用法

统计信息的使用方法有：收集统计信息（静态或动态）、查看统计信息和监控统计信息等。

#### 22.5.2.1 收集统计信息

##### 22.5.2.1.1 静态收集

静态收集统计信息有两种方式。一是自动收集；二是手动收集。采用任意一种即可。静态收集的结果均会保存到系统表中。

###### 22.5.2.1.1.1 自动收集

在 INI 参数 AUTO\_STAT\_OBJ 为 1 或 2 时，执行 SP\_CREATE\_AUTO\_STAT\_TRIGGER 过程实现自动收集。

在主备环境或 AFC 环境中使用该功能，重启后需重新手动执行语句 SP\_SET\_PARA\_VALUE(1,'AUTO\_STAT\_OBJ',1/2);。

###### 22.5.2.1.1.2 手动收集

手动收集有三种可选方式。下面分别介绍：

1. 通过《DM8 系统包使用手册》里 DBMS\_STATS 包中的方法（GATHER\_TABLE\_STATS、GATHER\_INDEX\_STATS 或 GATHER\_SCHEMA\_STATS）进行生成并收集统计信息。
2. 通过《DM8\_SQL 语言使用手册》中设置 STAT 语法为表、列、索引生成统计信息。

例 对 SYSOBJECTS 表上 ID 列生成统计信息，采样率的百分比为 30%。使用按新比例收集的列统计信息覆盖之前老的统计信息。

```
STAT 30 ON SYS.SYSOBJECTS (ID);
```
3. 通过《DM8\_SQL 语言使用手册》附录 3 中统计信息章节的系统存储过程和函数进行生成。

例 对 SYSOBJECTS 表上所有的索引生成统计信息。

```
CALL SP_TAB_INDEX_STAT_INIT ('SYS', 'SYSOBJECTS');
```

##### 22.5.2.1.2 动态收集

当已收集的统计信息失效或未曾收集时，用户可通过配置 DM.INI 参数 OPTIMIZER\_DYNAMIC\_SAMPLING，开启动态收集统计信息。

OPTIMIZER\_DYNAMIC\_SAMPLING 为动态会话级参数，取值范围：0~12。0：不启用；1~10：启用，采用率 10%~100%，收集动态统计信息，但收集结果不会保存到系统表；11：启用，由优化器自动确定采样率（0.1%~99.9%），收集结果也不会保存到系统表；12：和 11 相同，但收集的结果会保存到系统表。

#### 22.5.2.2 查看统计信息

执行过生成统计信息操作后，可通过下面多种方式查看到具体的统计信息。其中，动态收集中只有 OPTIMIZER\_DYNAMIC\_SAMPLING=12 可以被查询到。

1. 系统表 SYSSTATS

用于执行收集统计信息操作之后，记录系统中的统计信息。

2. 系统表 SYSMSTATS

记录多维统计信息的内容。

3. 系统表 SYSSTATPREFS

记录指定模式下表的统计信息的静态参数对应的值。

4. 系统表 SYSSTATTABLEIDU

记录用户表上一次收集统计信息时的总行数和增删改的影响行数以及是否有过 TRUNCATE 操作。

5. 通过 DBMS\_STATS 包中 COLUMN\_STATS\_SHOW、TABLE\_STATS\_SHOW 和 INDEX\_STATS\_SHOW 查看表、列、索引的统计信息。只有在生成统计信息之后才可以查看，可以用 DBMS\_STATS 包中 GATHER\_TABLE\_STATS、GATHER\_INDEX\_STATS 或 GATHER\_SCHEMA\_STATS 生成收集信息。具体参考 22.5.2.1 收集统计信息。

#### 22.5.2.3 监控统计信息

支持对自动收集统计信息的过程进行监控。

通过创建确定的过程 SYSDBA.GET\_AUTO\_STAT\_INFO\_FUNC，用以接收服务器在自动收集统计信息时的相关信息。该过程的模块体为开放式，用户可以根据自己的需求来编写如何使用统计信息的代码。

**语法如下：**

```
CREATE OR REPLACE PROCEDURE  SYSDBA.GET_AUTO_STAT_INFO_FUNC(
TASK_ID INT,
TOTAL_STAT INT,
TABLE_ID INT, 
SCH_NAME VARCHAR(24), 
TABLE_NAME VARCHAR(24),
CURR_GATH_TAB_ID INT, 
CURR_GATH_SCH_NAME VARCHAR(24), 
CURR_GATH_TAB_NAME VARCHAR(24),
SUCCESS_STAT INT,
FAIL_STAT INT,
TASK_START_TIME DATETIME, 
TASK_END_TIME DATETIME,
GATHER_TBL_START_TIME DATETIME,
GATHER_TBL_END_TIME DATETIME
) AS
BEGIN
/*用户自定义如何使用统计信息的代码*/
END;
/
```

**参数详解**

● task\_id 任务 id，同一个任务的 task\_id 相同。

● total\_stat 一次任务需要收集的表的总个数。

● table\_id 收集完成的一个表 table 的 id，每收集完一个表的统计信息，就会调用一次 SYSDBA.GET\_AUTO\_STAT\_INFO\_FUNC，传出一次数据，用户可自定义该过程，自定义处理接收到的数据。

● sch\_name 对应 table\_id 的模式名。

● table\_name 对应 table\_id 的表名。

● curr\_gath\_tab\_id 当前正在收集的表 id。收集完一个表 table 后，传出数据时，该字段为接下来要收集的表 id，也是服务器当前正要或正在收集的表。

● curr\_gath\_sch\_name 对应 curr\_gath\_tab\_id 的模式名。

● curr\_gath\_tab\_name 对应 curr\_gath\_tab\_id 的表名。

● success\_stat 截止到目前这次收集任务一共成功收集了多少张表。

● fail\_stat 截止到目前这次收集任务一共失败收集了多少张表。

● task\_start\_time 这次任务的开始时间。

● task\_end\_time 这次任务的结束时间，未结束为 NULL。

● gather\_tbl\_start\_time 收集完一个表 table 时，该表收集的开始时间。

● gather\_tbl\_end\_time 收集完一个表 table 时，该表收集的结束时间，收集失败，则结束时间为 NULL。

### 22.5.3 应用实例

#### 22.5.3.1 自动收集

在打开 INI 监控参数 AUTO\_STAT\_OBJ（为 1 或 2）的前提下，可使用 SP\_CREATE\_AUTO\_STAT\_TRIGGER 过程对表的监控信息进行自动收集。

下面详细介绍使用 SP\_CREATE\_AUTO\_STAT\_TRIGGER 过程自动收集用户表的统计信息的完整过程。

第一步，打开监控。

设置 INI 参数 AUTO\_STAT\_OBJ 为 1 或 2。1：对所有表进行监控；2：只对用户通过 DBMS\_STATS.SET\_TABLE\_PREFS 设置过 STALE\_PERCENT 属性的表对象进行监控。AUTO\_STAT\_OBJ=1 时，STALE\_PERCENT 为缺省值 10，即数据变化率 >=10% 时需要更新统计信息。如果 AUTO\_STAT\_OBJ=2，需进一步使用 DBMS\_STATS.SET\_TABLE\_PREFS 设置 STALE\_PERCENT 属性。

```
//用AUTO_STAT_OBJ=1打开对T表的监控。
CREATE TABLE T(A INT);
SP_SET_PARA_VALUE(1,'AUTO_STAT_OBJ',1);

//用AUTO_STAT_OBJ=2打开对T表的监控。
CREATE TABLE T(A INT);
SP_SET_PARA_VALUE(1,'AUTO_STAT_OBJ',2);
DBMS_STATS.SET_TABLE_PREFS('SYSDBA','T','STALE_PERCENT',15);//对修改行数占总行数的比达到STALE_PERCENT要求的对象和总行数为0的对象收集统计信息
```

下面以 AUTO\_STAT\_OBJ=2 为例。

第二步，执行统计信息收集操作。自动收集统计信息使用 SP\_CREATE\_AUTO\_STAT\_TRIGGER 设置触发器。

```
SP_CREATE_AUTO_STAT_TRIGGER(1, 1, 1, 1,'11:20', '2021/1/11',0,1);
```

第三步，对用户表 T 进行增删改操作。

```
insert into t select level connect by level<=20;

commit;
```

第四步，通过系统表 SYSSTATTABLEIDU 和动态视图 V$AUTO\_STAT\_TABLE\_IDU 查看监控信息，通过系统表 SYSSTATS 查看统计信息。

当打开监控（设置 AUTO\_STAT\_OBJ 为 1 或 2）并执行统计信息收集操作之后可以查看到 SYSSTATTABLEIDU 和 SYSSTATS 的变化。SYSSTATTABLEIDU 中的记录为对上一次的统计信息的监控。V$AUTO\_STAT\_TABLE\_IDU 中的记录为对统计信息的实时监控，不需要执行收集统计信息操作也能查看。

本例中 AUTO\_STAT\_OBJ=2。查看监控信息：

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

行号   ID    COLID   T_FLAG T_TOTAL  N_SAMPLE   N_DISTINCT   N_NULL   V_MIN      V_MAX  BLEVEL   N_LEAF_PAGES  N_LEAF_USED_PAGES  CLUSTER_FACTOR N_BUCKETS  
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

第五步，监控统计信息收集过程。接着上一步的例子，展示监控的完整过程。

首先，创建一个用户表 AUTO\_STAT\_INFO，用以保存自动收集过程的相关信息。

```
create table AUTO_STAT_INFO(

task_id INT,

total_stat INT,

table_id INT, 

sch_name varchar(24), 

table_name varchar(24),

curr_gath_tab_id INT, 

curr_gath_sch_name varchar(24), 

curr_gath_tab_name varchar(24),

success_stat INT,

fail_stat INT,

task_start_time DATETIME, 

task_end_time DATETIME,

gather_tbl_start_time DATETIME,

gather_tbl_end_time DATETIME

);
```

其次，创建过程 SYSDBA.GET\_AUTO\_STAT\_INFO\_FUNC，接收服务器在自动收集统计信息时的过程信息。并在模块体编写用户代码，将过程收集的统计信息写入 AUTO\_STAT\_INFO 中。

```
CREATE OR REPLACE PROCEDURE  SYSDBA.GET_AUTO_STAT_INFO_FUNC(task_id INT,total_stat INT,table_id INT, sch_name varchar(24), table_name varchar(24),curr_gath_tab_id INT, curr_gath_sch_name varchar(24), curr_gath_tab_name varchar(24),success_stat INT,fail_stat INT,task_start_time DATETIME, task_end_time DATETIME,gather_tbl_start_time DATETIME,gather_tbl_end_time DATETIME) as
BEGIN
//下面是用户自定义的代码，将SYSDBA.GET_AUTO_STAT_INFO_FUNC过程的信息插入到用户表AUTO_STAT_INFO 中
    INSERT INTO AUTO_STAT_INFO VALUES(task_id,total_stat,table_id, sch_name,table_name,curr_gath_tab_id, curr_gath_sch_name, curr_gath_tab_name,success_stat ,fail_stat,task_start_time,task_end_time,gather_tbl_start_time,gather_tbl_end_time);
    commit;
EXCEPTION
    WHEN OTHERS THEN
        NULL;
END;
/
```

最后，解读表 AUTO\_STAT\_INFO，介绍一次自动收集统计信息任务的相关过程信息。如果 SP\_CREATE\_AUTO\_STAT\_TRIGGER 触发一次自动收集统计信息，在任务开始时，会先记录当前任务的开始时间，当前任务的待收集表的总个数，以及接下来待收集的表的 id。之后每收集完成一个表的统计信息，就会记录该表 table 的 id 及收集该表的开始和结束时间，和截至目前收集成功失败的表个数情况，以及接下来待收集的表的 id。其中“接下来待收集的表的 id”即 current\_gather\_tab\_id，为当前服务器正在收集的表 id。

#### 22.5.3.2 手动收集

例 使用 DBMS\_STATS 包中 GATHER\_TABLE\_STATS 方法手动收集用户表的统计信息的完整过程。

使用包内的过程和函数之前，如果还未创建过系统包。请先调用系统过程创建系统包。

```
SP_CREATE_SYSTEM_PACKAGES (1,'DBMS_STATS');
SET SERVEROUTPUT ON; //PRINT需要设置这条语句，才能打印出消息
```

收集模式 PERSON 下表 ADDRESS 的统计信息，并打印收集的表信息。

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
        1.0,
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
            PRINT OBJTAB(I).PARTNAME;
            PRINT OBJTAB(I).SUBPARTNAME;
            PRINT '-------- ';
         END LOOP;
    END;
END;
/
```

打印结果：

```
1

PERSON

TABLE

ADDRESS

NULL

NULL
```

## 22.6 执行计划

执行计划是 SQL 语句的执行方式，由查询优化器为语句设计的执行方式，交给执行器去执行。

（一）在 SQL 命令行使用 EXPLAIN 可以打印出语句的执行计划。

例如：

建表和建索引语句：

```
CREATE TABLE T1(C1 INT,C2 CHAR);
CREATE TABLE T2(D1 INT,D2 CHAR);
CREATE  INDEX  IDX_T1_C1  ON  T1(C1);
INSERT INTO T1 VALUES(1,'A');
INSERT INTO T1 VALUES(2,'B');
INSERT INTO T1 VALUES(3,'C');
INSERT INTO T1 VALUES(4,'D');
INSERT INTO T2 VALUES(1,'A');
INSERT INTO T2 VALUES(2,'B');
INSERT INTO T2 VALUES(5,'C');
INSERT INTO T2 VALUES(6,'D');
```

打印执行计划：

```
EXPLAIN SELECT A.C1+1,B.D2 FROM T1 A, T2 B WHERE A.C1 = B.D1;
```

执行计划如下：

```
1   #NSET2: [1, 12, 56] 
2     #PRJT2: [1, 12, 56]; exp_num(2), is_atom(FALSE); INFO_BITS(0); BATCH_EXP_NUM(1); spl_info(NULL)
3       #NEST LOOP INDEX JOIN2: [1, 12, 56] 
4         #CSCN2: [1, 4, 52]; INDEX33555490(T2 as B); btr_scan(1); need_slct(0); prejudge_iescn(0)
5         #SSEK2: [1, 3, 4]; scan_type(ASC), IDX_T1_C1(T1 as A), scan_range[B.D1,B.D1], is_global(0)
```

这个执行计划看起来就像一棵树，执行过程为：控制流从上向下传递，数据流从下向上传递。其中，类似\[0, 16, 9\]这样的三个数字，分别表示估算的操作符代价、处理的记录行数和每行记录的字节数。同一层次中的操作符，如本例中的 CSCN2 和 SSEK2，由父节点 NEST LOOP INDEX JOIN2 控制它们的执行顺序。

该计划的大致执行流程如下：

1. CSCN2: 扫描 T2 表的聚集索引，数据传递给父节点索引连接；
2. NEST LOOP INDEX JOIN2: 当左孩子有数据返回时取右侧数据；
3. SSEK2: 利用 T2 表当前的 D1 值作为二级索引 IDX\_T1\_C1 定位查找的 KEY，返回结果给父节点；
4. NEST LOOP INDEX JOIN2: 如果右孩子有数据则将结果传递给父节点 PRJT2，否则继续取左孩子的下一条记录；
5. PRJT2: 进行表达式计算 C1+1, D2；
6. NSET2: 输出最后结果；
7. 重复过程 1) ~ 4)直至左侧 CSCN2 数据全部取完。

用户如果想了解更多关于操作符的知识，请查看动态视图 V$SQL\_NODE\_NAME，手册的 附录 4 执行计划操作符 给出了常用操作符的说明。

在执行计划的输出结果中，单独展示谓词信息（Predicate Information），用于说明各执行计划节点对应的条件表达式。谓词信息位于执行计划主体信息之后，以 Predicate Information 的形式集中列出。标准结构如下：

```
Predicate Information ( identified by operation id):
---------------------------------------------------------------------------------
<operation_id> - <predicate_type> (<predicate_expression>)
```

**参数说明**

1. <operation\_id>：谓词信息显示的操作编号，对应执行计划中的节点编号，指明该谓词隶属于执行计划中的哪一个节点，每个谓词只对应一个节点，一个节点可以包含多个谓词。
2. <predicate\_type>：谓词类型，有 access 和 filter 两类。连接条件使用 access 类型，过滤条件、连接的 join condition 使用 filter 类型。
3. <predicate\_expres\`sion>：优化器内部解析后的条件表达式。

例如：

打印执行计划：

```
EXPLAIN SELECT name, schid FROM sysobjects WHERE subtype$='STAB' AND name NOT IN (SELECT name FROM sysobjects WHERE name in (SELECT name FROM sysobjects WHERE SUBTYPE$='STAB')  AND TYPE$='DSYNOM');
```

执行计划如下：

```
1   #NSET2: [1, 28, 100] 
2     #PRJT2: [1, 28, 100]; exp_num(2), is_atom(FALSE); INFO_BITS(0);BATCH_EXP_NUM(0); spl_info(NULL)
3       #HASH LEFT SEMI JOIN2: [1, 28, 100]; (ANTI), KEY_NUM(1), KEY(SYSOBJECTS.NAME = DMTEMPVIEW_889215893.colname), KEY_NULL_EQU(0)
4         #SLCT2: [1, 28, 100]; SYSOBJECTS.SUBTYPE$ = 'STAB'; slct_pushdown(1); spl_info(NULL); flt_batch_exec(1)
5           #CSCN2: [1, 1130, 100]; SYSINDEXSYSOBJECTS(SYSOBJECTS as SYSOBJECTS); btr_scan(1); need_slct(1); prejudge_iescn(0)
6         #PRJT2: [1, 1, 96]; exp_num(1), is_atom(FALSE); INFO_BITS(0);BATCH_EXP_NUM(0); spl_info(NULL)
7           #INDEX JOIN SEMI JOIN2: [1, 1, 96];  join condition(SYSOBJECTS.SUBTYPE$ = 'STAB'), flt_batch_exec(0)
8             #CSEK2: [1, 28, 96]; scan_type(ASC), SYSINDEXSYSOBJECTS(SYSOBJECTS as SYSOBJECTS), scan_range[('DSYNOM',min,min),('DSYNOM',max,max))
9             #BLKUP2: [1, 3, 96]; SYSINDEXNAMESYSOBJECTS(SYSOBJECTS); use_clu_addr(0)
10              #SSEK2: [1, 3, 96]; scan_type(ASC), SYSINDEXNAMESYSOBJECTS(SYSOBJECTS as SYSOBJECTS), scan_range[SYSOBJECTS.NAME,SYSOBJECTS.NAME], is_global(0)

Predicate Information (identified by operation id):
---------------------------------------------------
3 - access(SYSOBJECTS.NAME = DMTEMPVIEW_889215893.colname)
4 - filter(SYSOBJECTS.SUBTYPE$ = 'STAB')
7 - filter(SYSOBJECTS.SUBTYPE$ = 'STAB')
```

其中，以下谓词信息对应执行计划中 3 #HASH LEFT SEMI JOIN2 的连接条件 KEY(SYSOBJECTS.NAME = DMTEMPVIEW\_889215893.colname)。

```
3 - access(SYSOBJECTS.NAME = DMTEMPVIEW_889215893.colname)
```

以下谓词信息对应执行计划中 4 #SCLT2 中的过滤条件 SYSOBJECTS.SUBTYPE$ = 'STAB'。

```
4 - filter(SYSOBJECTS.SUBTYPE$ = 'STAB')
```

以下谓词信息对应执行计划中 7 #INDEX JOIN SEMI JOIN2 中连接的 join condition(SYSOBJECTS.SUBTYPE$ = 'STAB')。

```
7 - filter(SYSOBJECTS.SUBTYPE$ = 'STAB')
```

（二）可以使用 EXPLAIN FOR 进行执行计划的查看。

例如：

```
EXPLAIN FOR SELECT A.C1+1,B.D2 FROM T1 A, T2 B WHERE A.C1 = B.D1;
```

执行结果如下：

```
LINEID     PLAN_ID     PLAN_NAME CREATE_TIME                LEVEL_ID    OPERATION             TAB_NAME
---------- ----------- --------- -------------------------- ----------- --------------------- --------
           IDX_NAME                SCAN_TYPE SCAN_RANGE  ROW_NUMS             BYTES       COST            
           ----------------------- --------- ----------- -------------------- ----------- --------------------
           CPU_COST             IO_COST              FILTER JOIN_COND ADVICE_INFO PSTART      PSTOP  
           -------------------- -------------------- ------ --------- ----------- ----------- -----------
1          1           NULL      2026-04-10 10:48:39.000000 0           NSET2                 NULL
           NULL                    NULL      NULL        12                   56          1
           0                    0                    NULL   NULL      NULL        0           0

LINEID     PLAN_ID     PLAN_NAME CREATE_TIME                LEVEL_ID    OPERATION             TAB_NAME
---------- ----------- --------- -------------------------- ----------- --------------------- --------
           IDX_NAME                SCAN_TYPE SCAN_RANGE  ROW_NUMS             BYTES       COST            
           ----------------------- --------- ----------- -------------------- ----------- --------------------
           CPU_COST             IO_COST              FILTER JOIN_COND ADVICE_INFO PSTART      PSTOP  
           -------------------- -------------------- ------ --------- ----------- ----------- -----------
2          1           NULL      2026-04-10 10:48:39.000000 1           PRJT2                 NULL
           NULL                    NULL      NULL        12                   56          1
           0                    0                    NULL   NULL      NULL        0           0

LINEID     PLAN_ID     PLAN_NAME CREATE_TIME                LEVEL_ID    OPERATION             TAB_NAME
---------- ----------- --------- -------------------------- ----------- --------------------- --------
           IDX_NAME                SCAN_TYPE SCAN_RANGE  ROW_NUMS             BYTES       COST            
           ----------------------- --------- ----------- -------------------- ----------- --------------------
           CPU_COST             IO_COST              FILTER JOIN_COND ADVICE_INFO PSTART      PSTOP  
           -------------------- -------------------- ------ --------- ----------- ----------- -----------
3          1           NULL      2026-04-10 10:48:39.000000 2           NEST LOOP INDEX JOIN2 NULL
           NULL                    NULL      NULL        12                   56          1
           0                    0                    NULL   NULL      NULL        0           0

LINEID     PLAN_ID     PLAN_NAME CREATE_TIME                LEVEL_ID    OPERATION             TAB_NAME
---------- ----------- --------- -------------------------- ----------- --------------------- --------
           IDX_NAME                SCAN_TYPE SCAN_RANGE  ROW_NUMS             BYTES       COST            
           ----------------------- --------- ----------- -------------------- ----------- --------------------
           CPU_COST             IO_COST              FILTER JOIN_COND ADVICE_INFO PSTART      PSTOP  
           -------------------- -------------------- ------ --------- ----------- ----------- -----------
4          1           NULL      2026-04-10 10:48:39.000000 3           CSCN2                 T2
           INDEX33555479           NULL      NULL        4                    52          1
           0                    0                    NULL   NULL      NULL        0           0

LINEID     PLAN_ID     PLAN_NAME CREATE_TIME                LEVEL_ID    OPERATION             TAB_NAME
---------- ----------- --------- -------------------------- ----------- --------------------- --------
           IDX_NAME                SCAN_TYPE SCAN_RANGE  ROW_NUMS             BYTES       COST            
           ----------------------- --------- ----------- -------------------- ----------- --------------------
           CPU_COST             IO_COST              FILTER JOIN_COND ADVICE_INFO PSTART      PSTOP  
           -------------------- -------------------- ------ --------- ----------- ----------- -----------
5          1           NULL      2026-04-10 10:48:39.000000 3           SSEK2                 T1
           IDX_T1_C1[is_global(0)] ASC       [B.D1,B.D1] 3                    4           1
           0                    0                    NULL   NULL      NULL        0           0
```

EXPLAIN FOR 的每一列定义如下：

| 序号 | 列 | 说明 |
| --- | --- | --- |
| 1 | PLAN\_ID | 执行计划 ID |
| 2 | PLAN\_NAME | 执行计划名称 |
| 3 | CREATE\_TIME | 执行计划生成时间 |
| 4 | LEVEL\_ID | 执行计划操作符在计划树第几层 |
| 5 | OPERATION | 执行计划操作符名称 |
| 6 | TAB\_NAME | 表名 |
| 7 | IDX\_NAME | 索引名 |
| 8 | SCAN\_TYPE | 扫描类型 |
| 9 | SCAN\_RANGE | 扫描范围 |
| 10 | ROW\_NUMS | 执行计划操作符结果集预测行数 |
| 11 | BYTES | 执行计划操作符行数据处理长度 |
| 12 | COST | 代价 |
| 13 | CPU\_COST | CPU 代价 |
| 14 | IO\_COST | IO 代价 |
| 15 | FILTER | 执行计划操作符上过滤条件 |
| 16 | JOIN\_COND | 连接条件 |
| 17 | ADVICE\_INFO | 给用户的优化建议 |
| 18 | PSTART | 分区表起始分区 |
| 19 | PSTOP | 分区表结束分区 |

### 22.6.1 自适应计划

在 DM 优化器进行代价估算时，如果子节点是一个复杂查询，可能使得对于子节点的代价估算不准确，导致最终选择的计划在执行时并非最优计划。因此，DM 引入了自适应计划机制。

将 INI 参数 OPTIMIZER\_MODE 和 ADAPTIVE\_NPLN\_FLAG 都置为 1，启用自适应计划机制。此时，优化器会自动判断在某些情况下，复杂查询的子节点可能导致代价估算不准确，则会为该节点生成一个备用计划节点。在实际执行到该节点时，根据准确的代价信息确定是否需要采用备用计划。

例如：

建表、插入数据并建索引：

```
DROP TABLE T1;
DROP TABLE T2;

CREATE TABLE T1(C1 INT,C2 INT);
CREATE TABLE T2(D1 INT,D2 INT);

INSERT INTO T1 VALUES(1,1);
INSERT INTO T1 VALUES(1,2);
INSERT INTO T2 VALUES(1,1);
INSERT INTO T2 VALUES(2,1);
INSERT INTO T2 VALUES(3,1);
INSERT INTO T2 VALUES(4,1);
INSERT INTO T2 VALUES(5,1);
COMMIT;

CREATE INDEX IND1 ON T1(C2);
```

打印执行计划：

```
EXPLAIN SELECT * FROM T1 ,T2 ,T1 T3 WHERE T2.D1= T3.C1 AND T1.C2=T2.D2;
```

执行计划如下：

```
1   #NSET2: [1, 5, 24] 
2     #PRJT2: [1, 5, 24]; exp_num(6), is_atom(FALSE); INFO_BITS(0);BATCH_EXP_NUM(0); spl_info(NULL)
3       #HASH2 INNER JOIN: [1, 5, 24];  KEY_NUM(1); KEY(T2.D2=T1.C2) KEY_NULL_EQU(0)
4         #NEST LOOP INDEX JOIN2: [1, 5, 24] 
5           #ACTRL: [1, 5, 24]
6             #HASH2 INNER JOIN: [1, 5, 16];  KEY_NUM(1); KEY(T3.C1=T2.D1) KEY_NULL_EQU(0)
7               #CSCN2: [1, 2, 8]; INDEX33555539(T1 as T3); btr_scan(1); need_slct(0); prejudge_iescn(0)
8               #CSCN2: [1, 5, 8]; INDEX33555540(T2); btr_scan(1); need_slct(0); prejudge_iescn(0)
9           #BLKUP2: [1, 1, 4]; IND1(T1); use_clu_addr(0)
10            #SSEK2: [1, 1, 4]; scan_type(ASC), IND1(T1), scan_range[T2.D2,T2.D2], is_global(0)
11        #CSCN2: [1, 2, 8]; INDEX33555539(T1); btr_scan(1); need_slct(0); prejudge_iescn(0)

Predicate Information (identified by operation id):
---------------------------------------------------
3 - access(T2.D2 = T1.C2)
6 - access(T3.C1 = T2.D1)
```

可以看到执行计划中有一个 ACTRL 操作符，它说明优化器为这一条 SQL 语句生成了备用计划。ACTRL 是控制备用计划转换的操作符，其上面一层 NEST LOOP INDEX JOIN2 为默认的主计划，再上面一层 HASH2 INNER JOIN 则为备用计划。ACTRL 操作符计算下层孩子节点的代价，决定采用默认主计划还是备用计划。

需要说明的是，MPP 和并行查询不支持自适应计划。

## 22.7 使用索引

为了提高查询效率，用户一般会在表中创建索引。查询中的条件列为索引列时，如果索引扫描代价最小，优化器就会采用索引扫描。索引扫描有多种方式，例如，索引等值查询、索引范围查询。如果查询列属于索引列的子集，则通过索引扫描就可以获得数据，否则，还需要根据 ROWID 或者 PK 在聚集索引中定位记录。

常用的索引类型有唯一索引、组合索引、函数索引。各自有不同的使用场景。

1. 条件列具有 UNIQUE 约束，则可以创建唯一索引，减少索引扫描次数；
2. 条件列是多个列，而且可以过滤掉大部分数据，可以在多个列上创建组合索引，把等值条件列作为组合索引的首列；
3. 条件列使用确定性函数(同样环境下多次执行得到相同的结果)，可以创建函数索引，会把函数值进行存储，使用方式与普通索引一样；

## 22.8 并行查询

并行查询（Parallel Query，PQ）是一种多个线程或进程间协作、共同完成 SQL 计划的优化技术。

根据参与执行的 DM 服务器实例个数，并行查询可以划分为多机并行查询和单机并行查询。单机并行查询仅利用了单机的 CPU、磁盘、内存等机器资源，因此又称为本地并行查询。

DM 支持本地并行和多机并行，并行查询具体实现上采用对称并行技术，即每一个执行者（进程或线程）都执行相同的计划。主要执行者负责向其他并行执行者分发计划、搜集数据并向客户返回最终结果。不管是主执行者，还是从执行者，它们执行的计划都是完全相同的。

### 22.8.1 多机并行查询

多机并行查询是指在分布式数据库系统中，利用集群中的多台机器同时完成用户请求。

例如，DM MPP 就是一个支持多机并行的数据库系统。用户登录到某个 EP 执行查询操作时，查询计划会被自动打包发送给集群中其它 EP，多个 EP 协同合作完成用户请求。为了使得数据能够在多个 EP 间流动，MPP 引入了专门的数据分发操作符如 MPP GATHER（MGAT）、MPP COLLECT（MCLCT）、MPP BROADCAST（MBRO）和 MPP SCATTER（MSCT）。详情请参考《DM8 大规模并行处理 MPP》。

### 22.8.2 本地并行查询

本地并行查询（Local Parallel Query，LPQ）是指利用一台数据库服务器的多个线程同时执行查询操作。只有当主机具有多个 CPU 内核时，开启 LPQ 才能提高查询任务的性能。

### 22.8.2.1 本地并行步骤

达梦数据库通过三个步骤来完成本地并行查询：首先，启动本地并行查询；其次，确定并行度；再次，确定并行工作线程总个数；最后，执行查询。

并行查询相关参数见下表：

表22.1 并行查询相关参数

| **参数名** | **缺省值** | **属性** | **说明** |
| --- | --- | --- | --- |
| MAX\_PARALLEL\_DEGREE | 1 | 动态，会话级 | 用于设置并行度（即最大并行线程数）。取值范围：1~128，同时要小于等于 PARALLEL\_THRD\_NUM。1 表示不并行 |
| PARALLEL\_POLICY | 0 | 动态，会话级 | 用来设置并行策略。取值范围：0、1 和 2。   0：关闭并行；   1：开启自动并行模式，使用 INI 参数 MAX\_PARALLEL\_DEGREE 作为并行度。如果同时使用了 HINT 参数 PARALLEL 指定并行度，则 HINT 优先；   2：开启手动并行模式，使用 HINT 参数 PARALLEL 指定并行度，不指定表示不并行。在 DMDPC 环境下，取值 2 等同于取值 1。   不支持 HINT 方式指定该参数 |
| PARALLEL\_THRD\_NUM | 10 | 静态 | 用来设置并行工作线程个数。取值范围 1~65535 |

#### 22.8.2.1.1 启用本地并行查询

使用 PARALLEL\_POLICY 开启或关闭 LPQ。0 表示禁止 LPQ。1 采用自动并行，即系统对任何一个 SQL 都试图使用 LPQ，除非使用了 HINT 限制并行任务个数。2 采用手动并行，即除非使用了 HINT 指定了并行任务个数，否则都不采用 LPQ。

#### 22.8.2.1.2 确定并行度

当 PARALLEL\_POLICY=1 时，表示自动并行，使用 INI 参数 MAX\_PARALLEL\_DEGREE 作为并行度。如果同时使用了 HINT 参数 PARALLEL 指定并行度，则 HINT 优先。

当 PARALLEL\_POLICY=2 时，表示手动并行，只能使用 HINT 参数 PARALLEL 指定并行度。在 DMDPC 环境下，取值 2 等同于取值 1。

**1．** **在 INI 参数中设置默认值**

当 PARALLEL\_POLICY=1 时，使用 MAX\_PARALLEL\_DEGREE 设置单个查询或并行创建索引等操作的并行度。

例 在 INI 参数中将 MAX\_PARALLEL\_DEGREE 设置为 3 的格式如下：

```
MAX_PARALLEL_DEGREE   3
```

然后，使用一般的 SQL 语句查询即可执行并行查询，不需要使用 HINT。如：

```
SELECT * FROM SYSOBJECTS;
```

**2．** **在 SQL 语句中使用“PARALLEL”关键字特别指定**

当 PARALLEL\_POLICY=1 时，也可在 SQL 语句中通过 HINT PARALLEL 指定并行度。当 INI 参数 MAX\_PARALLEL\_DEGREE 和 HINIT PARALLEL 同时指定并行度时，HINT 优先。

当 PARALLEL\_POLICY=2 时，只能在 SQL 语句中通过 HINT PARALLEL 指定并行度，否则不并行。

“PARALLEL”关键字的用法是在数据查询语句的 SELECT 关键字后，增加 HINT 子句来实现。

**语法格式**

```
/*+ PARALLEL([<表名>] <并行度>) */
```

**参数说明**

< 并行度 >：用于设置并行度，即最大并行线程数。取值范围：1~ MAX\_PARALLEL\_DEGREE。1 表示不并行。

另外，每个语句中仅能设置一次并行任务个数，如果设置了多次，则以第一次设置为准，而且任务个数在全语句中生效。

例 下面的例子中，使用的并行任务个数为 4。

```
SELECT /*+ PARALLEL(4) *//*+ PARALLEL(5) */ * FROM SYSOBJECTS;
```

这种方式能够为单条查询语句设置额外的并行任务个数，以此来提高某些特殊查询任务的性能。

在 DM 分布计算集群（DMDPC）环境中，还支持另一种并行度调整的语法。

**语法格式**

```
/*+ PARALLEL(#<子任务序号> <并行度>) */
```

**参数说明**

< 子任务序号 >：子任务（又称子计划）的序号。如果给定的子任务序号不存在，或者所给定子任务的并行度不支持调整（如使用了 USE\_SQC\_NO 访问粒度的子任务），则该 HINT 会被忽略。另外，DPC\_OPT\_FLAG 优化取值 1024 会对各子任务并行度进行调整从而覆盖该 HINT 的作用。

< 并行度 >：用于设置单个子任务的并行度（即最大并行线程数）。取值范围：1~ MAX\_PARALLEL\_DEGREE。1 表示不并行。

#### 22.8.2.1.3 确定并行工作线程总个数

在执行并行查询任务之前，您需要指定完成并行查询的并行工作线程总个数。并行工作线程总数是系统启动时，创建的并行工作线程的总个数，一般不超过 CPU 内核个数的 2 倍。

值得注意的是，实际使用的线程数并非总是等于并行工作线程总数。并行工作线程总数是在 INI 参数中设定的，实际使用并行工作线程数是根据系统的实际状况确定的。

**1．** **并行工作线程数，在 INI 参数中设定**

首先，使用 PARALLEL\_POLICY 参数来设置并行策略。

当开启本地并行（PARALLEL\_POLICY>0）时，需要指定 PARALLEL\_THRD\_NUM。PARALLEL\_THRD\_NUM 重启生效。需要注意的是，若 PARALLEL\_POLICY=1，如果 PARALLEL\_THRD\_NUM=1, 则按照 CPU 个数创建并行线程。

例 设置并行策略 PARALLEL\_POLICY 为 2，即手动设置并行工作线程数；同时设置 PARALLEL\_THRD\_NUM 为 4。

```
PARALLEL_POLICY      2

PARALLEL_THRD_NUM    4
```

当然，并非所有的查询都适合使用并行查询。大量占用 CPU 周期的查询最适合采用并行查询的功能。例如，大型表的连接查询、大量数据的聚合和大型结果集的排序等都很适合采用并行查询。对于简单查询（常用于事务处理应用程序）而言，执行并行查询所需的额外协调工作会大于潜在的性能提升。所以，数据库管理员在确定是否需要使用并行策略的时候，需要慎重。

**2．** **实际使用的线程数，达梦数据库会根据每个并行查询操作自动检测**

实际使用线程数是执行计划准备执行之前，系统根据并行度和实际空闲的并行工作线程数来自动确定的，不需要用户去干预。此操作所依据的条件如下：首先，检测达梦数据库是否运行在具有多个 CPU 的计算机上。只有具有多个 CPU 的计算机才能使用并行查询。这是一个硬性的限制条件。其次，检测可用的空闲工作线程是否足够。并行查询到底采用多少线程数，除了跟操作的复杂程度相关外，还跟当时的服务器状态相关，如是否有足够的可用的空闲工作线程数量等。每个并行查询操作都要求一定的工作线程数量才能够执行；而且执行并行计划比执行串行计划需要更多的线程，所需要的线程数量也会随着任务个数的提高而增加。当无法满足特定并行查询执行的线程要求时，数据库引擎就会自动减少任务个数，甚至会放弃并行查询而改为串行计划。所以，即使同一个操作在不同时候可能会采用不同的线程数。

例如，即使设置并行度为 4。而实际使用的线程数可能只有 3 个，或者更少。

#### 22.8.2.1.4 执行查询

当以上内容确定好之后，数据库就会执行具体的查询任务。例如，当开启了自动并行模式 PARALLEL\_POLICY=1，并行度为 16，并行线程总个数为 32。在这种搭配下，当以 16 路并行时，最多可以有 2 个 SQL 采用并行查询，并行线程总数不超过 32，此时，如果有其他 SQL，只能采用非并行查询。

### 22.8.2.2 并行操作符

为了使得数据在同一进程的不同线程间流动，引入了下述用于本地数据分发的操作符。

表22.2 LPQ并行执行计划通讯操作符

| **操作符名称** | **功能** |
| --- | --- |
| LOCAL GATHER （LGAT） | 主线程收集所有线程数据，从线程将数据发送到主线程 |
| LOCAL DISTRIBUTE （LDIS） | 各线程间相互分发数据，按照分发列计算行数据的目标线程并发送过去，目标线程负责接收 |
| LOCAL BROADCAST （LBRO） | 各个线程将本线程数据发送到其他所有线程 |
| LOCAL SCATTER （LSCT） | 主线程发送完整数据到所有从线程，保证每个线程数据都完整，一般和 LGAT 配合使用 |
| LOCAL COLLECT（LCLCT） | 数据收集到主线程处理，用于替换顶层的 LOCAL GATHER。相较于 LOCAL GATHER 有额外的处理如数据同步、处理邮件堆积等 |

### 22.8.2.3 使用场景

使用手动并行模式时，只需要在 INI 参数中设置好如下 2 个参数，然后执行并行 SQL 查询语句时，需手动指定并行度。若不指定，将不使用并行。设置的 2 个参数如下：

```
PARALLEL_POLICY      2

PARALLEL_THRD_NUM    4
```

使用自动并行模式时，一般指定如下三个参数：

```
MAX_PARALLEL_DEGREE   3

PARALLEL_POLICY       1

PARALLEL_THRD_NUM     10
```

另外，当 PARALLEL\_POLICY 为 0 时，即使有并行任务，也不支持并行。

然后，执行语法格式类似“SELECT \* FROM SYSOBJECTS;”的并行 SQL 语句即可，本条语句使用的并行度为 3。

当然，如果单条查询语句不想使用默认并行任务数，可以通过在 SQL 语句中增加 HINT，通过“PARALLEL”关键字来特别指定。此时，执行的并行 SQL 语句格式为“SELECT /\*+ PARALLEL(SYSOBJECTS 4) \*/ \* FROM SYSOBJECTS;”，本条语句使用的并行任务数为 4。

### 22.8.3 多机和本地并行查询

在 DM MPP 系统中开启 LPQ，计划执行时就会用到多机并行和本地并行。如下面 TPCH 的 Q1 查询语句。

```
--##建表脚本
CREATE HUGE TABLE LINEITEM
(
L_ORDERKEY              BIGINT NOT NULL,
L_PARTKEY               INT NOT NULL,
L_SUPPKEY               INT NOT NULL,
L_LINENUMBER            INT NOT NULL,
L_QUANTITY              FLOAT NOT NULL,
L_EXTENDEDPRICE         FLOAT NOT NULL,
L_DISCOUNT              FLOAT NOT NULL,
L_TAX                   FLOAT NOT NULL,
L_RETURNFLAG            CHAR(1) NOT NULL,
L_LINESTATUS            CHAR(1) NOT NULL, 
L_SHIPDATE              DATE NOT NULL,
L_COMMITDATE            DATE NOT NULL,
L_RECEIPTDATE           DATE NOT NULL,
L_SHIPINSTRUCT          CHAR(25) NOT NULL,
L_SHIPMODE              CHAR(10) NOT NULL, 
L_COMMENT               VARCHAR(44) NOT NULL,
PRIMARY KEY(L_ORDERKEY, L_LINENUMBER)
)
DISTRIBUTED BY (L_ORDERKEY);
--执行查询
SELECT
l_returnflag, 
l_linestatus, 
sum(l_quantity) as sum_qty, 
sum(l_extendedprice) as sum_base_price, 
sum(l_extendedprice*(1-l_discount)) as sum_disc_price, 
sum(l_extendedprice*(1-l_discount)*(1+l_tax)) as sum_charge, 
avg(l_quantity) as avg_qty, 
avg(l_extendedprice) as avg_price, 
avg(l_discount) as avg_disc, 
count(*) as count_order 
FROM lineitem 
WHERE l_shipdate <= date' 1998-12-01' - interval '90' day 
GROUP BY l_returnflag, l_linestatus 
ORDER BY l_returnflag, l_linestatus;
```

该查询为单表过滤后的分组和排序。一个可能的计划形态如下：

```
1   #NSET2: [5, 1, 141] 
2     #PRJT2: [5, 1, 141]; exp_num(10), is_atom(FALSE); INFO_BITS(0)
3       #SORT3: [5, 1, 141]; key_num(2), partition_key_num(0), is_distinct(FALSE), top_flag(0), is_adaptive(0)
4         #HAGR2: [4, 1, 141]; grp_num(2), sfun_num(8), distinct_flag[0,0,0,0,0,0,0,0]; slave_empty(0) keys(DMTEMPVIEW_889214018.TMPCOL0, DMTEMPVIEW_889214018.TMPCOL1) 
5           #MPP COLLECT: [1, 4, 141]; op_id(2) n_grp_by (0) n_cols(0) n_keys(0) for_sync(FALSE)
6             #LOCAL COLLECT: [1, 1, 141]; op_id(1) n_grp_by (0) n_cols(0) n_keys(0) for_sync(FALSE)
7               #PRJT2: [1, 1, 141]; exp_num(7), is_atom(FALSE); INFO_BITS(0)
8                 #HFLKUP2: [1, 1, 141]; (LINEITEM)
9                   #SLCT2: [1, 1, 141]; LINEITEM.L_SHIPDATE <= var2; slct_pushdown(0)
10                    #HFSEK2: [1, 1, 141]; (LINEITEM), scan_type(LE)(null2,1998-12-01-exp12]

Predicate Information (identified by operation id):
---------------------------------------------------
9 - filter(LINEITEM.L_SHIPDATE <= var2)
```

假定上述计划执行在 EP1~EP4 共四个 EP 上执行，每个 EP 设置的并行度为 8，那么该计划一共有 8 \* 4= 32 个线程协作完成。执行的大体流程是，首先每个 EP 的 8 路线程各自获取 LIMEITEM 表数据，经过查询条件过滤、检索和投影等运算后得到各自线程的最终结果，各自线程的结果经过本地收集（#6），交由各 EP 内的主线程 x，每个 EP 的主线程再将结果汇总至主 EP（#5），主 EP 再进行分组聚合等操作，得到最终结果。

## 22.9 查询计划重用

如果同一条语句执行频率较高，或者每次执行的语句仅仅是常量值不同，则可以考虑使用计划重用机制。避免每次执行都需要优化器进行分析处理，可以直接从计划缓存中获取已有的执行计划，减少了分析优化过程，提高执行率。

对于计划重用，达梦数据库提供了 INI 参数 USE\_PLN\_POOL 来控制，当置为非 0 时，会启用计划重用。

## 22.10 结果集重用

执行计划的生成与优化是一个非常依赖 CPU 的操作，而执行一个查询获得结果集也是一个非常消耗资源的操作。当系统连续执行两个完全相同的 SQL 语句，其执行计划和结果集很有可能是相同的，如果重新生成和执行计划，会大大浪费系统资源。这时如果使用计划重用和结果集重用，系统的响应速度可以大大提升。

结果集重用是基于计划重用的，如果查询的计划不能缓存，则其查询结果集必然不能缓存。此外，当语句的游标属性为 FORWARD ONLY 时，默认查询不会生成结果集。而参数 BUILD\_FORWARD\_RS 可以强制在此类查询中生成结果集，以便进行结果集重用。

可通过设置 INI 参数 RS\_CAN\_CACHE 来控制结果集重用。当置为 0 时表示禁止重用结果集；置为 1 时表示强制模式（FORCE），在此模式下默认缓存所有可缓存结果集，但是 DBA 也可以通过新增的配置参数以及语句提示等方法取消某些不合适的结果集缓存；置为 2 时表示手动模式（MANUAL），在此模式下默认不缓存查询结果集，但是 DBA 可以通过语句提示等方法指示系统对必要的查询结果集进行缓存。

当 RS\_CAN\_CACHE 为 1 时，还可以通过设置 INI 参数 RS\_CACHE\_TABLES 和 RS\_CACHE\_MIN\_TIME 对缓存的结果集进行限制和过滤。RS\_CACHE\_TABLES 指定可以缓存结果集的基表清单，只有查询涉及的所有基表全部在参数指定范围内，此查询才会缓存结果集。RS\_CACHE\_MIN\_TIME 则指定了缓存结果集的查询语句执行时间的下限，只有实际执行时间不少于指定值的查询结果集才会缓存。

DBA 可以通过在 SQL 语句中设置 “RESULT\_CACHE”或“NO\_RESULT\_CACHE” HINT 手动指示查询的结果集是否缓存。如：

```
select /*+ RESULT_CACHE */ id, name from sysobjects;
```

或者

```
select /*+ NO_RESULT_CACHE */ id, name from sysobjects;
```

在语句中使用 HINT 指定结果集缓存的优先级要高于 INI 中相关参数的设置。

还可以使用系统过程 SP\_SET\_PLN\_RS\_CACHE 来强制设置指定计划结果集缓存的生效及失效。这个系统过程对结果集缓存的指定高于其它所有结果集缓存的设置。

在以下情况下，DM 不支持结果缓存：

1. 必须是单纯的查询语句计划，PL 脚本中包含查询语句也不能缓存结果集。
2. 查询语句的计划本身必须是缓存的。
3. 守护环境中的备库不支持结果集缓存。
4. MPP 等集群环境下不支持结果集缓存（3、4 两点限制都是因为无法精确控制基表的数据更新时戳）。
5. 查询语句中包含以下任意一项，其结果集都不能缓存：
	1. 包含临时表；
		2. 包含序列的 CURVAL 或 NEXTVAL；
		3. 包含非确定的 SQL 函数或包方法（现有逻辑是不支持所有 SQL 函数或包方法）；
		4. 包含 RAND、SYSDATE 等返回值实时变化的系统函数；
		5. 包含其它的一些实时要素。
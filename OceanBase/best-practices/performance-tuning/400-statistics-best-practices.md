---
title: "收集统计信息生成高效执行计划的最佳实践"
book: "性能调优"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000001489643.html"
tags:
  - oceanbase
  - best-practices
  - performance-tuning
---

# 收集统计信息生成高效执行计划的最佳实践

## 为什么要收集统计信息

优化器在生成和选择执行计划时，会评估和比较各个可用的计划的执行代价，因此执行计划的代价评估准确性至关重要。优化器根据代价模型和各算子估算的行数，评估执行计划的代价，而统计信息则在这一过程中扮演着关键角色。统计信息的准确性直接影响算子的行数估算，进而影响执行计划的代价计算和选择。因此，保持统计信息的准确性对于生成高效的执行计划至关重要。

## 原理说明

统计信息以普通数据的形式存储在内部表中，并且会在本地维护相应的缓存，以提高优化器对统计信息的访问速度。优化器通过使用统计信息来评估各种查询路径的成本，选择执行效率最高的计划。统计信息定期更新以反映数据的变化，有助于保持查询性能的优化。

## 应用场景

- 复杂查询优化：在执行复杂的 JOIN 或子查询时，准确的统计信息可以通过选择更合适的表连接顺序以及表连接方法，从而显著提高查询性能。
- 索引选择：优化器利用统计信息判断是否使用某个索引，从而提高访问速度。
- 数据分布变化：当表中数据显著变化时，例如批量插入、删除或更新，统计信息的更新显得尤为重要。

## 注意事项和说明

- 收集频率：统计信息收集不宜过于频繁或过于稀疏，需根据数据变化规律设定适当的频率。
- 资源占用：收集统计信息会消耗一定的系统资源，建议在系统负载较低时进行。
- 准确性：确保统计信息的准确性非常重要，否则可能导致优化器无法选择到较好的执行计划。

## 统计信息的默认收集策略

系统默认在每个工作日（周一至周五）22:00 开始收集统计信息，最长持续 4 小时；在非工作日（每周六、日）6:00 开始，最长持续 20 小时。这一时间段被称为统计信息维护窗口。在每个维护窗口内，优化器会重新收集所有过期的表或分区的统计信息。

满足下面统计信息的过期判定标准任意一个条件，就可以认为统计信息需要重新收集：

- 表/分区自上次收集后，从未有成功收集统计信息。
- 表/分区的增删改数据量超过上次收集时该表/分区行数的 10%。

收集统计信息时，默认的策略如下所示：

| **配置名称** | **含义** | **默认策略** |
|----|----|----|
| degree | 并行度 | 1（单线程扫描） |
| method_opt | 列级统计信息收集策略 | 收集所有列的基础统计信息及存在数据倾斜列的直方图 |
| granularity | 收集颗粒 | 非分区表直接收集全局级统计信息，分区表收集分区级统计信息并推导出全局统计信息 |
| estimate_percent | 采样比例 | 不采样，通过全表扫描收集统计信息 |
| block_sample | 是否使用块采样 | 不使用块采样，使用行采样 |

## 统计信息收集策略的配置

采用默认的统计信息收集策略可以满足大多数表的需求，但在特定场景下，用户可能需要根据业务特点进行适当调整。以下是一些常见场景及其配置策略：

### 业务高峰与统计信息维护窗口重叠

默认的统计信息维护窗口可能与业务高峰时段重叠，比如在工作日的晚上。此时，统计信息收集可能会与业务 SQL 争夺资源，从而影响业务性能。解决方案是调整统计信息维护窗口的开始时间，确保与业务高峰错开。

``` sql
-- MySQL 业务租户, 比如现在是 2024-03-07, 周四早上 11 点, 需要调整为从周五凌晨 2 点开始:
call dbms_scheduler.set_attribute('MONDAY_WINDOW', 'NEXT_DATE', '2024-03-11 02:00:00');
call dbms_scheduler.set_attribute('TUESDAY_WINDOW', 'NEXT_DATE', '2024-03-12 02:00:00');
call dbms_scheduler.set_attribute('WEDNESDAY_WINDOW', 'NEXT_DATE', '2024-03-13 02:00:00');
call dbms_scheduler.set_attribute('THURSDAY_WINDOW', 'NEXT_DATE', '2024-03-14 02:00:00');
call dbms_scheduler.set_attribute('FRIDAY_WINDOW', 'NEXT_DATE', '2024-03-08 02:00:00');
call dbms_scheduler.set_attribute('SATURDAY_WINDOW', 'NEXT_DATE', '2024-03-09 02:00:00');
call dbms_scheduler.set_attribute('SUNDAY_WINDOW', 'NEXT_DATE', '2024-03-10 02:00:00');


-- Oracle 业务租户需要在对应的 sys 用户下执行, 比如现在是 2024-03-07, 周四早上 11 点, 需要调整为从周五凌晨 2 点开始:
SET NLS_DATE_FORMAT='YYYY-MM-DD HH24:MI:SS';
SET NLS_TIMESTAMP_FORMAT='YYYY-MM-DD HH24:MI:SS.FF';
SET NLS_TIMESTAMP_TZ_FORMAT='YYYY-MM-DD HH24:MI:SS.FF TZR TZD';
call dbms_scheduler.set_attribute('MONDAY_WINDOW', 'NEXT_DATE', '2024-03-11 02:00:00');
call dbms_scheduler.set_attribute('TUESDAY_WINDOW', 'NEXT_DATE', '2024-03-12 02:00:00');
call dbms_scheduler.set_attribute('WEDNESDAY_WINDOW', 'NEXT_DATE', '2024-03-13 02:00:00');
call dbms_scheduler.set_attribute('THURSDAY_WINDOW', 'NEXT_DATE', '2024-03-14 02:00:00');
call dbms_scheduler.set_attribute('FRIDAY_WINDOW', 'NEXT_DATE', '2024-03-08 02:00:00');
call dbms_scheduler.set_attribute('SATURDAY_WINDOW', 'NEXT_DATE', '2024-03-09 02:00:00');
call dbms_scheduler.set_attribute('SUNDAY_WINDOW', 'NEXT_DATE', '2024-03-10 02:00:00');
```

### 超大表导致统计信息收集不完整的解决方案

统计信息收集的默认策略下，需要单并发全表扫描待收集统计信息的表/分区。如果待收集统计信息的表/分区的数据量特别大，或者占用的磁盘空间特别多，会导致统计信息收集耗时过长影响后续其它表的统计信息收集，甚至当前表可能会收集超时。当业务环境下存在数据量过亿，或者磁盘空间占用超过 20G 的表时，建议参考以下方案配置统计信息收集策略。

在 OceanBase 数据库 V4.2.1 版本之前，`estimate_percent` 参数可以同时控制基础统计信息采样和直方图采样的比例。使用`estimate_percent` 参数调整基础统计信息的采样比例时，可能会导致直方图采样比例增加，因此建议不与收集直方图的命令一起使用。

OceanBase 数据库 V4.2.1 版本及以上，`estimate_percent` 参数仅控制基础统计信息的采样比例。您可以根据需要直接设置该参数，而无需担心影响直方图采样比例。

#### 对于非分区表

1.  **跳过大对象**：避免在统计信息中收集大对象，例如 TEXT 列，配置时只收集非大对象列的统计信息。MySQL 模式下默认会收集 TEXT 列的统计信息，如果 TEXT 列中保存的都是大对象，可能会导致收集特别慢。如下示例中，第四个参数配置收集哪些列的统计信息，需要把除大对象外的所有列都加上。

    ``` sql
    call dbms_stats.set_table_prefs(
      'database_name',
      'table_name',
      'method_opt',
      'for columns col1,col2,col3,... size auto');
    ```

2.  **提高并行度或配置块采样**：提高并行度可以让统计信息收集时使用更多的线程同时收集，通过消耗更多的资源达到快速收集的效果。使用块采样通过采样的方式减少了统计信息收集时要处理的数据量到快速收集的效果。两者都可以达到提升统计信息收集效率的，区别在于提高采样并行度的方式通过牺牲资源保证了统计信息的准确性，块采样的方式通过牺牲一定的统计信息准确性来节约了资源消耗。用户可根据自己的需要选择其中一种方式进行配置。

    ``` sql
    -- 表级配置并行方法：提高并行度
    call dbms_stats.set_table_prefs('database_name', 'table_name', 'degree', '4');

    -- 表级配置开启块采样：启用块采样
    call dbms_stats.set_table_prefs(
      'databse_name',
      'table_name',
      'block_sample',
      'True');
    -- 配置采样比例，可根据表的数量级进行配置，通常情况下采集千万级的数据即可充分反应一个表的数据特征
    call dbms_stats.set_table_prefs(
      'databse_name',
      'table_name',
      'estimate_percent',
      '0.1');
    ```

#### 对于分区表

1.  **跳过大对象**：同样需要避免收集 TEXT 列的数据。MySQL 模式下默认会收集 TEXT 列的统计信息，如果 TEXT 列中保存的都是大对象，可能会导致收集特别慢。如下示例中，第四个参数配置收集哪些列的统计信息，需要把除大对象外的所有列都加上。

    ``` sql
    -- 标记配置跳过大对象
    call dbms_stats.set_table_prefs(
      'database_name',
      'table_name',
      'method_opt',
      'for columns col1,col2,col3,... size auto');
    ```

2.  **不收集全局统计信息**：为一级分区或二级分区表设定只收集特定级别的统计信息，并确保全局统计信息被删除。如下示例中，第四个参数配置收集什么级别的统计信息，一级分区表可配置只收集一级分区的统计信息，二级分区表可配置只收集二级分区的统计信息。需要注意的是，如果采用这种策略，需要删除全局统计信息（一级分区表和二级分区表时）和一级分区统计信息（仅二级分区表时）。

    ``` sql
    -- 配置不收集全局统计信息
    -- 对于一级分区表
    call dbms_stats.set_table_prefs('database_name', 'table_name', 'granularity', 'PARTITION');

    -- 对于二级分区表
    call dbms_stats.set_table_prefs('database_name', 'table_name', 'granularity', 'SUBPARTITION');
    ```

3.  **提高并行度或配置块采样**：使用与非分区表相似的配置，确保统计信息收集在业务低峰期完成。提高并行度可以让统计信息收集时使用更多的线程同时收集，通过消耗更多的资源达到快速收集的效果。使用此方式需要注意将统计信息收集的时间与业务高峰错开。使用块采样通过采样的方式减少了统计信息收集时要处理的数据量到快速收集的效果，也可以避免大量读数据盘导致服务器IO被打的也别高。两者都可以达到提升统计信息收集效率的，区别在于提高采样并行度的方式通过牺牲资源保证了统计信息的准确性，块采样的方式通过牺牲一定的统计信息准确性来节约了资源消耗。用户可根据自己的需要选择其中一种方式进行配置。

    ``` sql
    -- 表级配置并行方法：提高并行度
    call dbms_stats.set_table_prefs('database_name', 'table_name', 'degree', '4');

    -- 表级配置开启块采样：启用块采样
    call dbms_stats.set_table_prefs(
      'databse_name',
      'table_name',
      'block_sample',
      'True');
    -- 配置采样比例，可根据表的数量级进行配置，通常情况下采集千万级的数据即可充分反应一个表的数据特征
    call dbms_stats.set_table_prefs(
      'databse_name',
      'table_name',
      'estimate_percent',
      '0.1');
    ```

#### 选择直方图策略进行统计信息收集

OceanBase 数据库优化器支持三种直方图：频率直方图、Topk 直方图和混合直方图。

在频率直方图中，每个不同的列值对应于直方图的单个桶，要求指定的桶的个数不低于列的 NDV 值。

Topk 直方图是频率直方图的变体，基于 Lossy Counting 算法，通过取部分数据特征来估算整体的数据分布，要求它所记录的数据数与总数据数的比例不低于 1-(1/bucket_size)。

混合直方图主要通过采集指定的的数据量进行直方图构建，是对频率直方图和 Topk 直方图的功能补充。

在处理大表场景时，OceanBase 数据库优化器引入了混合直方图以高效构建统计信息。这种方法通过采集预定数量的数据，构造直方图。混合直方图的每个桶可以容纳多个不同的值，从而将采集到的数据根据桶的数量进行分段，并将每段内的所有数据放置在相应的桶中，旨在以更少的桶来描述更大范围的数据分布。

- **条件一**：如果指定列的不同值数量（NDV，Number of Distinct Values）小于等于 254，则使用频率直方图。

- **条件二**：如果 NDV 大于 254，则优先使用 TopK 直方图。具体操作为：在统计列信息后，按照桶的频次从高到低进行排序，剔除序号大于 254 的桶，但必须确保这 254 个桶中统计的数据占总数据的比例不低于 1 - (1/bucket_size)，默认值为 99.6%。

- 如果不满足上述条件二，则使用混合直方图。

通过存储过程 `set_column_stats` 显式指定列级别的基本统计信息。参考示例如下：

``` sql
-- 调用 dbms_stats 包中的 set_column_stats 程序
-- 用于设置表 'tbl1' 中列 'col1' 的统计信息
-- 'user1'：指定表所在的用户/schema
-- 'tbl1'：指定要设置统计信息的表名称
-- 'col1'：指定要设置统计信息的列名称
-- distcnt => 254：指定列中不同值的数量为 254
-- nullcnt => 10：指定列中 NULL 值的数量为 10
CALL dbms_stats.set_column_stats('user1', 'tbl1', 'col1', distcnt => 254, nullcnt => 10);
```

#### 手动进行统计信息收集

利用手动收集统计信息，可以更好地控制收集时机和方法，降低对业务的影响。OceanBase 数据库优化器针对手动统计信息收集提供了两种方式：`DBMS_STATS`（推荐）、`ANALYZE` 命令行；推荐使用 `DBMS_STATS` 系统包进行手动统计信息收集，因为 `DBMS_STATS` 系统包支持的功能会更加丰富。

**示例：使用 `DBMS_STATS` 系统包收集统计信息**

``` sql
-- 收集用户 TEST 的表 T_PART1 的分区级别的统计信息，并行度 64，只收集数据分布不均匀的列的直方图
CALL dbms_stats.gather_table_stats('TEST', 'T_PART1', degree => 64, granularity => 'PARTITION', method_opt => 'FOR ALL COLUMNS SIZE SKEWONLY');
```

**示例：使用 `ANALYZE` 命令行收集统计信息**

``` sql
-- 收集用户 TEST 的表 T_PART1 的 GLOBAL 级别的统计信息, 只收集数据分布不均匀的列的直方图
ANALYZE TABLE T_PART1 PARTITION ('T_PART1') COMPUTE STATISTICS FOR ALL COLUMNS SIZE skewonly;
```

对于超大表的统计信息收集，依然可以根据数据量和表结构采用分段收集和手动收集的策略。分段收集可以有效减少单次统计信息收集的负载，而手动方式则使得收集过程更加灵活且可控。

### 处理跑批任务后的查询

在批量导入数据后，默认情况下统计信息不会被立即更新。若业务中存在需要在导入后立即查询的场景，建议在数据导入后手动收集一次统计信息。

### 处理按日期预建分区的查询

对于按日期预建分区的表，部分预建分区如果在数据导入后没有及时更新统计信息，优化器可能生成不佳的执行计划。建议在导入数据后手动收集相关分区的统计信息，确保优化器能够优化执行计划。

## 相关文档

您可以阅读下述文档及其子章节，了解更多关于**统计信息**的内容：

- [统计信息概述](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001053014)
- [统计信息和估行机制概述](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001052898)

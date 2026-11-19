---
title: "诊断实践：使用 SQL_PLAN_MONITOR 分析性能问题"
book: OceanBase AP
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577428.html"
tags:
  - oceanbase
  - standalone
  - obap
---

# 诊断实践：使用 SQL_PLAN_MONITOR 分析性能问题

SQL 在 AP 场景下缺乏算子级别的执行监控，例如并行执行任务划分了多少个，是否有倾斜，HASH 冲突是否严重，执行 hang 住时卡在了哪个算子上等等问题，诊断问题依赖于日志。为了解决这些问题，OceanBase 数据库引入了 Oracle 兼容视图 GV\$SQL_PLAN_MONITOR，通过该视图可以精确了解每个算子的执行关键细节。

## 视图介绍

支持 SQL 算子级监控，每一行对应一个算子实例运行时的监控数据，包含一般性监控数据和算子特有监控数据，一般性监控数据如算子处理的数据行数、open 和 close 的时间、占用内存多少等，特有监控数据如 HASH 冲突率、GI 切分 block 数、table scan 扫描行数等。

视图中重点字段的详细介绍如下。

[TABLE]

不同算子可以赋予 OTHERSTAT_N_VALUE 不同的含义，填不同的值。

具体可以利用 OTHERSTAT_N_ID 的值，查询 V\$SQL_MONITOR_STATNAME 表对 ID 列进行过滤。

## 性能问题分析示例

SQL_PLAN_MONITOR 常用于分析性能问题。

### 索引不优问题分析

``` cpp
obclient [SYS]> select output_rows, plan_operation, OTHERSTAT_3_VALUE scans from gv$sql_plan_monitor where trace_id = 'xxx' and plan_operation like '%TABLE_SCAN';
+-------------+--------------------+--------+
| OUTPUT_ROWS | PLAN_OPERATION     | SCANS  |
+-------------+--------------------+--------+
|           5 | PHY_VEC_TABLE_SCAN | 500072 |
```

利用上面的 SQL 可以查询出 table scan 算子扫描的行数和输出的行数，当二者相差较大时，比如上面的例子扫描了 50 万行只输出了 5 行，说明该表上缺少合适的索引。

### JOIN 方法选择不优问题分析

常见的是应该走 hash join，实际生成了 nested-loop join, 左表行数较多时，会 rescan 右表非常多次，性能较差。可以使用下面的 SQL 查询算子最大 rescan 次数，如果这个值比较大，极有可能发生了 join 方法选错的问题。

``` cpp
select max(starts) rescans from gv$sql_plan_monitor where trace_id = 'xxx';
```

### 通用分析方法

逐个判断是否存在上面的问题可能有点麻烦，大多数情况下，可以直接使用通用方法判断是计划中哪个部分比较耗时。

1.  首先使用下面的 SQL 查询出这条 query 对应的 SQL_PLAN_MONITOR 记录。查询结果包含了每个算子 open、close、输出第一行和输出最后一行的时间。

    ``` sql
    select plan_line_id, concat(lpad(' ', plan_depth, ' '), plan_operation) op, sum(output_rows) rowss, sum(STARTS) rescan, min(first_refresh_time) open_time, max(last_refresh_time) close_time, min(first_change_time) first_row_time, max(last_change_time) last_row_eof_time, count(1) threads from gv$sql_plan_monitor where trace_id = 'xxx' group by plan_line_id, plan_operation, plan_depth order by 1;
    ```

2.  从上向下观察查询结果。首先最顶层的 0 号算子，它的 LAST_ROW_EOF_TIME 应该约等于 CLOSE_TIME， 假设它是 hash join 算子，hash join 执行时是先从左侧收取全部数据构建 hash 表，再从右侧子节点取数据逐行 probe hash 表。那么我们可以观察 1 号算子即 hash join 左子节点的 LAST_ROW_EOF_TIME。

    1.  如果 1 号算子的 LAST_ROW_EOF_TIME 比较大，说明大部分时间在执行 hash join 的左支，那么可以继续观察 1 号算子下面的子计划。
    2.  如果 1 号算子的 LAST_ROW_EOF_TIME 比较小，说明大部分时间都在执行 hash join 的右支，以及进行 hash 表的探测，那么可以继续观察 0 号 hash join 右子节点的子计划。

以下面的计划为例说明如何分析。

首先观察到顶层是个 merge join 算子，该算子会先从左子节点拿一行，再从右子节点拿一行。可以看到算子的 open 时间是 25.792777 秒，merge join 左子节点输出第一行的时间是 25.793831，merge join 右子节点输出第一行的时间是 27.572661，由此可见，merge join 右支为了输出第一行数据耗费了一秒多的时间。

继续观察 merge join 右子节点，发现是一个 sort 算子，该算子会接收下层所有数据，排序后再向上层输出，从 ROWSS 字段可以看到该算子收取了 160 万行数据，对其进行排序会耗费大量时间。可以通过在排序键上建立索引消除排序，提升性能。

``` sql
| ==========================================================        |
| |ID|OPERATOR                  |NAME|EST.ROWS|EST.TIME(us)|        |
| ----------------------------------------------------------        |
| |0 |MERGE JOIN                |    |1       |5           |        |
| |1 |├─SORT                    |    |1       |3           |        |
| |2 |│ └─COLUMN TABLE FULL SCAN|T1  |1       |3           |        |
| |3 |└─SORT                    |    |1       |3           |        |
| |4 |  └─TABLE FULL SCAN       |T0  |1       |3           |        |
| ==========================================================        |
```

``` sql
select plan_line_id, concat(lpad(' ', plan_depth, ' '), plan_operation) op, sum(output_rows) rowss, sum(STARTS) rescan, min(first_refresh_time) open_time, max(last_refresh_time) close_time, min(first_change_time) first_row_time, max(last_change_time) last_row_eof_time, count(1) threads from gv$sql_plan_monitor where trace_id = 'YC3500BA2DAC4-0006198CC947196A-0-0' group by plan_line_id, plan_operation, plan_depth order by 1;
```

``` sql
+--------------+-----------------------+---------+--------+----------------------------+----------------------------+----------------------------+----------------------------+---------+
| PLAN_LINE_ID | OP                    | ROWSS   | RESCAN | OPEN_TIME                  | CLOSE_TIME                 | FIRST_ROW_TIME             | LAST_ROW_EOF_TIME          | THREADS |
+--------------+-----------------------+---------+--------+----------------------------+----------------------------+----------------------------+----------------------------+---------+
|            0 | PHY_MERGE_JOIN        |       0 |      0 | 2024-05-29 16:29:25.792777 | 2024-05-29 16:29:27.664014 | NULL                       | 2024-05-29 16:29:27.664014 |       1 |
|            1 |  PHY_SORT             |       2 |      0 | 2024-05-29 16:29:25.792777 | 2024-05-29 16:29:27.664014 | 2024-05-29 16:29:25.793831 | NULL                       |       1 |
|            2 |   PHY_VEC_TABLE_SCAN  |       2 |      0 | 2024-05-29 16:29:25.792777 | 2024-05-29 16:29:27.664014 | 2024-05-29 16:29:25.793831 | 2024-05-29 16:29:25.793831 |       1 |
|            3 |  PHY_SORT             | 1599984 |      0 | 2024-05-29 16:29:25.792777 | 2024-05-29 16:29:27.664014 | 2024-05-29 16:29:27.572661 | 2024-05-29 16:29:27.664014 |       1 |
|            4 |   PHY_VEC_TABLE_SCAN  | 1599984 |      0 | 2024-05-29 16:29:25.792777 | 2024-05-29 16:29:27.664014 | 2024-05-29 16:29:25.793831 | 2024-05-29 16:29:26.642023 |       1 |
+--------------+-----------------------+---------+--------+----------------------------+----------------------------+----------------------------+----------------------------+---------+
```

可以发现，要通过 SQL PLAN MONITOR 分析性能问题，需要对不同算子的执行方式有一定的了解。下面列出了一些常见算子的执行方式。

1.  流式输出。一边从下层收数据，一边向上层输出数据。

    limit, merge group by, merge distinct, subplan scan

2.  阻塞式。从下层收取全部数据后再向上层输出数据。

    sort, hash group by, hash distinct, material

3.  其他

    | **算子** | **执行方式** |
    |----|----|
    | merge join/union/intersect/except | 同时从两个子节点收取数据，先从左侧收起。 |
    | nested-loop join, subplan filter | 逐行从第一个子节点收取数据，然后 rescan 其他子节点并收取数据。 |
    | hash join/union/intersect/except | 先从左子节点收取全部数据，再从右子节点收取数据。 |

## 相关文档

- 关于 GV\$SQL_PLAN_MONITOR 视图的详细介绍，参见 [GV\$SQL_PLAN_MONITOR（MySQL 模式）](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015172) 和 [GV\$SQL_PLAN_MONITOR（Oracle 模式）](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002014143)。

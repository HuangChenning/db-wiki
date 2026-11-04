---
title: Extensible Optimizer Interface
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/ext_opt_ref.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 21 Extensible Optimizer Interface

This chapter describes the functions and procedures that comprise the interface to the extensible optimizer.

This chapter contains these topics:

- Extensible Optimizer Interface
- User-Defined ODCIStats Functions

## Extensible Optimizer Interface

This section discusses the components of the Extensible Optimizer interface.

The extensible optimizer interfaces support working with partitioned tables and domain indexes. This is accomplished in two ways:

- Additional attributes have been added to some system-defined object types that are parameters to the `ODCIStats` interface methods. For example, the `ODCIColInfo` type is enhanced to add information about the column's partition.
- Arguments or semantics of the arguments have changed for some `ODCIStats` methods.

Note that you must update your code for `ODCIStats2` version of the `ODCIStats` interfaces to use your statistics type with an indextype that implements the `ODCIIndex2` version of the extensible indexing interfaces.

Example 21-1 Using Statistics Functions in an Extensible Optimizer Interface

Consider an example of how the statistics functions might be used. Suppose, in the schema `HR`, we define the following:

```
CREATE OPERATOR Contains binding (VARCHAR2(4000), VARCHAR2(30))
   RETURN NUMBER USING Contains_fn;

CREATE TYPE stat1 (
   ...,
   STATIC FUNCTION ODCIStatsSelectivity(pred ODCIPredInfo, sel OUT NUMBER,
      args ODCIArgDescList, start NUMBER, stop NUMBER, doc VARCHAR2(4000),
      key VARCHAR2(30)) return NUMBER,
   STACTIC FUNCTION ODCIStatsFunctionCost(func ODCIFuncInfo, cost OUT
      ODCICost, args ODCIArgDescList, doc VARCHAR2(4000), key VARCHAR2(30))
      return NUMBER,
   STATIC FUNCTION ODCIStatsIndexCost(ia ODCIIndexInfo, sel NUMBER,
      cost OUT ODCICost, qi ODCIQueryInfo, pred ODCIPredInfo,
      args ODCIArgDescList, start NUMBER, stop NUMBER,
      key VARCHAR2(30)) return NUMBER,
   ...
);

CREATE TABLE T (resume VARCHAR2(4000));

CREATE INDEX T_resume on T(resume) INDEXTYPE IS indtype;

ASSOCIATE STATISTICS WITH FUNCTIONS Contains_fn USING stat1;

ASSOCIATE STATISTICS WITH INDEXTYPE indtype USING stat1 
   WITH SYSTEM MANAGED STORAGE TABLES;
```

When the optimizer encounters the query

```
SELECT * FROM T WHERE Contains(resume, 'ORACLE') = 1,
```

it computes the selectivity of the predicate by invoking the user-defined selectivity function for the functional implementation of the `Contains` operator. In this case, the selectivity function is `stat1.ODCIStatsSelectivity`. It is called as follows:

```
stat1.ODCIStatsSelectivity (
   ODCIPredInfo('HR', 'Contains_fn', NULL, 29),
   sel,
   ODCIArgDescList(
      ODCIArgDesc(ODCIConst.ArgLit,
                  NULL, NULL, NULL, NULL, NULL, NULL),
      ODCIArgDesc(ODCIConst.ArgLit,
                  NULL, NULL, NULL, NULL, NULL, NULL),
      ODCIArgDesc(ODCIConst.ArgCol, 'T', 'HR', '"RESUME"', NULL, NULL, NULL),
      ODCIArgDesc(ODCIConst.ArgLit,
                  NULL, NULL, NULL, NULL, NULL, NULL)),
      1,
      1,
      NULL,
      'ORACLE')
```

Suppose the selectivity function returns a selectivity of 3 (percent). When the domain index is being evaluated, then the optimizer calls the user-defined index cost function as follows:

```
stat1.ODCIStatsIndexCost (   ODCIIndexInfo('HR', 'T_RESUME',      ODCIColInfoList(ODCIColInfo('HR', 'T', '"RESUME"', NULL, NULL, NULL, 0, 0, 0, 0)), NULL, 0, 0, 0, 0),      3,      cost,      NULL,      ODCIPredInfo('HR', 'Contains', NULL, 13),      ODCIArgDescList( ODCIArgDesc(ODCIConst.ArgLit,                                   NULL, NULL, NULL, NULL, NULL, NULL),                       ODCIArgDesc(ODCIConst.ArgLit,                                   NULL, NULL, NULL, NULL, NULL, NULL),                       ODCIArgDesc(ODCIConst.ArgLit,                                   NULL, NULL, NULL, NULL, NULL, NULL)),      1,      1,      'ORACLE')
```

Suppose that the optimizer decides not to use the domain index because it is too expensive. Then it calls the user-defined cost function for the functional implementation of the operator as follows:

```
stat1.ODCIStatsFunctionCost (
   ODCIFuncInfo('HR', 'Contains_fn', NULL, 1),
   cost,
   ODCIArgDescList(  ODCIArgDesc(ODCIConst.ArgCol, 
                       'T', 'HR', '"RESUME"', NULL, NULL, NULL),
                     ODCIArgDesc(ODCIConst.ArgLit, 
                        NULL, NULL, NULL, NULL, NULL, NULL)),
   NULL,
   'ORACLE')
```

The following sections describe each statistics type function in greater detail.

### EXPLAIN PLAN

`EXPLAIN` `PLAN` shows the user-defined CPU and I/O costs for domain indexes in the `CPU_COST` and `IO_COST` columns of `PLAN_TABLE`. For example, suppose we have a table `Emp_tab` and a user-defined operator `Contains`. Further, suppose that there is a domain index `EmpResume_indx` on the `Resume_col` column of `Emp_tab`, and that the indextype of `EmpResume_indx` supports the operator `Contains`. Then, the query

```
SELECT * FROM Emp_tab WHERE Contains(Resume_col, 'Oracle') = 1
```

might have the following plan:

| OPERATION | OPTIONS | OBJECT\_NAME | CPU\_COST | IO\_COST |
| --- | --- | --- | --- | --- |
| ``` SELECT STATEMENT ``` |  |  |  |  |
| ``` TABLE ACCESS ``` | ``` BY ROWID ``` | ``` EMP_TAB ``` |  |  |
| ``` DOMAIN INDEX ``` |  | ``` EMPRESUME_INDX ``` | ``` 300 ``` | ``` 4 ``` |

### INDEX Hint

The index hint applies to domain indexes. In other words, the index hint forces the optimizer to use the hinted index for a user-defined operator, if possible.

### ORDERED\_PREDICATES Hint

The hint `ORDERED_PREDICATES` forces the optimizer to preserve the order of predicate evaluation (except predicates used for index keys) as specified in the `WHERE` clause of a SQL DML statement.

## User-Defined ODCIStats Functions

User-defined `ODCIStats` functions are used for table columns, functions, package, type, indextype or domain indexes. These functions are described in the following sections.

Table 21-1 Summary of User-Defined ODCIStats Functions

| Function | Description |
| --- | --- |
| ODCIGetInterfaces() | Discover which version of the `ODCIStats` interface the user has implemented. |
| ODCIStatsCollect() | Called by the `DBMS_STATS` package to collect user-defined statistics on a table, a partition of a table, an index, or a partition of an index. |
| ODCIStatsDelete() | Deletes user-defined statistics on a table, a partition of a table, an index, or a partition of an index. |
| ODCIStatsFunctionCost() | Computes the cost of a function. |
| ODCIStatsExchangePartition() | Exchanges domain index statistics when an `ALTER TABLE EXCHANGE PARTITION ... INCLULDING INDEXES` command is issued. |
| ODCIStatsIndexCost() | Calculates the cost of a domain index scan. |
| ODCIStatsSelectivity() | Specifies the selectivity of a predicate. |
| ODCIStatsTableFunction() | Provides cardinality statistics for table functions and input cursor expressions. |
| ODCIStatsUpdPartStatistics() | Updates statistics during partition maintenance operations. Patches the domain index statistics. |

### ODCIGetInterfaces()

`ODCIGetInterfaces` is invoked by the server to discover which version of the `ODCIStats` interface the user has implemented in the methods of the user-defined statistics type.

Syntax

```
FUNCTION ODCIGetInterfaces(
   ifclist OUT ODCIObjectList)
RETURN NUMBER;
```

| Parameter | IN/OUT | Description |
| --- | --- | --- |
| ``` ifclist ``` | ``` OUT ``` | The version of the `ODCIStats` interfaces implemented by the statistics type. This value should be `SYS.ODCISTATS2`. |

Returns

`ODCIConst.Success` on success, `ODCIConst.Error` otherwise.

### ODCIStatsCollect()

Called by the `DBMS_STATS` package to collect user-defined statistics.

| Syntax | Description |
| --- | --- |
| ``` FUNCTION ODCIStatsCollect(    col ODCIColInfo,     options ODCIStatsOptions,     statistics OUT RAW,    env ODCIEnv)  return NUMBER; ``` | Called by the `DBMS_STATS` package to collect user-defined statistics on a table or a partition of a table. |
| ``` FUNCTION ODCIStatsCollect(    ia ODCIIndexInfo,     options ODCIStatsOptions,     statistics OUT RAW,    env ODCIEnv)  return NUMBER; ``` | Called to collect user-defined statistics on an index or a partition of an index. |

| Parameter | IN/OUT | Description |
| --- | --- | --- |
| `col` |  | Column for which statistics are being collected |
| `options` |  | Options passed to `DBMS_STATS` |
| `statistics` |  | User-defined statistics collected |
| env |  | Contains general information about the environment in which the routine is executing |
| `ia` |  | Domain index for which statistics are being collected |

Returns

The function returns `ODCIConst.Success`, `ODCIConst.Error`, or `ODCIConst.Warning.`

Usage Notes

- This function should be implemented as a `STATIC` type method.
- If statistics are being collected for only one partition, the `TablePartition` field in the `ODCIColInfo` type is filled in with the name of the partition. Otherwise (if statistics must be collected for all the partitions or for the entire table), the `TablePartition` field is null.
- If the `DBMS_STATS` package methods are executed to collect user-defined statistics on a partitioned table, then `n+1` `ODCIStatsCollect` calls are made, where `n` is the number of partitions in the table. The first `n` calls are made with the `TablePartition` attribute in `ODCIColInfo` filled in with the partition name and the `ODCIStatsOptions.CallProperty` set to `IntermediateCall`. The last call is made with `ODCIEnv.CallPropertyflag` set to `FinalCall` to allow you to collect aggregate statistics for the entire table.
- If user-defined statistics are being collected for only one partition of the table, two `ODCIStatsCollect` calls are made. In the first, you should collect statistics for the partition. For this call, the `TablePartition` attribute of the `ODCIColInfo` structure is filled in and the `ODCIEnv.CallProperty` is set to `FirstCall`.
- In the second call you can update the aggregate statistics of the table based upon the new statistics collected for the partition. In this call, the `ODCIEnv.CallPropertyflag` is set to `FinalCall` to indicate that it is the second call. The `ODCIColInfo.TablePartition` is filled in with the partition name in both the calls.
- The ODCIStatsCollect() method is invoked only one time for a non-partitioned domain index, a partitioned domain index and a partition in a domain index. If the statistics are being collected only for one partition in a domain index, the `IndexPartitionNum` field in the `ODCIIndexInfo` type is filled in with the partition number. Otherwise, the `IndexPartitionNum` field is `null`.
- Because the statistics `OUT RAW` argument of statistics is not used in the new interface, the cartridge developer should store the user-defined statistics result in some user-defined tables.
- If a non-partitioned domain index is being `ANALYZE` d, the user should collect statistics for the domain index.
- If a partitioned domain index is being `ANALYZE` d,
	- `ODCIEnv.CallProperty = StatsGlobalAndPartition` means that the user should collect statistics for all partitions in the domain index and then aggregate statistics of the domain index based upon the statistics collected for all the partitions
		- `ODCIEnv.CallProperty = StatsGlobal` means that the user should aggregate domain index statistics from the statistics of all the domain index partitions.
		- `ODCIEnv.CallProperty = StatsPartition` means that the user should collect statistics for all index partitions in the domain index.
- If only one partition of the domain index is being `ANALYZE` d,
	- `ODCIEnv.CallProperty = StatsGlobalAndPartition` means that the user should collect statistics for the single index partition and then aggregate statistics of the domain index based upon the statistics of all the partitions.
		- `ODCIEnv.CallProperty = StatsGlobal` means that the user should aggregate domain index statistics from the statistics of all the index partitions.
		- `ODCIEnv.CallProperty = StatsPartition` means that the user should collect statistics for the single index partition.
- Note that when `ODCIEnv.CallProperty = StatsGlobalAndPartition` or `StatsGlobal`, the user should aggregate statistics for the domain index, depending on the availability of the statistics collected for the other index partitions. If the statistics for all the index partitions are available, aggregate these statistics. If any one statistics for an index partition is absent, do nothing.

### ODCIStatsDelete()

`ODCIStatsDelete` is called to delete user-defined statistics.

| Syntax | Description |
| --- | --- |
| ``` FUNCTION ODCIStatsDelete(    col ODCIColInfo,     statistics OUT RAW,    env ODCIEnv)  return NUMBER; ``` | Deletes user-defined statistics on a table or a partition of a table. |
| ``` FUNCTION ODCIStatsDelete(    ia ODCIIndexInfo,     statistics OUT RAW,     env ODCIEnv)  return NUMBER; ``` | Deletes user-defined statistics on an index or a partition of an index. |

| Parameter | IN/OUT | Description |
| --- | --- | --- |
| `col` |  | Column for which statistics are being deleted |
| `statistics` | ``` OUT ``` | Contains table-level aggregate statistics for a partitioned table or index |
| `env` |  | Contains general information about the environment in which the routine is executing |
| `ia` |  | Domain index for which statistics are deleted |

Returns

`ODCIConst.Success`, `ODCIConst.Error`, or `ODCIConst.Warning.`

Usage Notes

- This function should be implemented as a `STATIC` method.
- When the function is called for a non-partitioned table, the `statistics` argument in the `ODCIStatsDelete` interface is ignored.
- If the statistics are being deleted for a partitioned table, the `ODCIStatsDelete` is called `n+1` times. The first `n` calls are with the partition name filled in the `ODCIColInfo` structure and the `ODCIEnv.CallProperty` set to `IntermediateCall`. The last call is made with the `ODCIEnv.CallProperty` set to `FinalCall`.
- In the first call, delete the statistics for the specific partitions; and in the last call drop or clean up any structures created for holding statistics for the deleted table. The `ODCIColInfo.TablePartition` is set to null in the last call. In the first call, the `TablePartition` field is filled in.
- If statistics are being deleted for only one partition and the `_minimal_stats_aggregation` parameter is set to `FALSE`, two `ODCIStatsDelete` calls are made. In each call, `ODCIColInfo.TablePartition` is filled in with the partition name. On the first call, delete any user-defined statistics collected for that partition. On the second call, update the aggregate statistics for the table.
- If statistics are being deleted for one partition and `_minimal_stats_aggregation` is set to `TRUE`, `ODCIStatsDelete` is only called one to delete any user-defined statistics collected for that partition.
- The initial value of `_minimal_stats_aggregation` is `TRUE`.
- The ODCIStatsDelete() method is invoked only one time for non-partitioned domain index, partitioned domain index, or an index partition.
- If the statistics is being deleted for a non-partitioned domain index, the user should delete user-defined statistics for the domain index.
- If the statistics is being deleted for a partitioned domain index, the user should delete the aggregated statistics of the domain index and optionally delete user-defined statistics for all domain index partitions, depending on `Options` in `ODCIEnv.CallProperty`:
	- `ODCIEnv.CallProperty = StatsGlobalAndPartition` means that the user should delete statistics for all the domain index partitions and aggregated statistics of the domain index.
		- `ODCIEnv.CallProperty = StatsGlobal` means that the user should delete the aggregated statistics of the domain index.
		- `ODCIEnv.CallProperty = StatsPartition` is not valid option.
- If the statistics is being deleted for only one partition of the index, the user should delete user-defined statistics for the index partition.

### ODCIStatsFunctionCost()

Computes the cost of a function.

Syntax

```
FUNCTION ODCIStatsFunctionCost(
   func ODCIFuncInfo, 
   cost OUT ODCICost, 
   args ODCIArgDescList, 
   list,
   env ODCIEnv) 
return NUMBER;
```

| Parameter | IN/OUT | Description |
| --- | --- | --- |
| ``` func ``` |  | Function or type method for which the cost is being computed |
| ``` cost ``` | ``` OUT ``` | Computed cost (must be positive whole numbers) |
| ``` args ``` |  | Descriptor of actual arguments with which the function or type method was called. If the function has n arguments, the `args` array contains n elements, each describing the actual arguments of the function or type method |
| ``` list ``` |  | List of actual parameters to the function or type method; the number, position, and type of each argument must be identical in the function or type method. |
| ``` env ``` |  | Contains general information about the environment in which the routine is executing |

Returns

`ODCIConst.Success`, `ODCIConst.Error`, or `ODCIConst.Warning.`

Usage Notes

This function should be implemented as a static type method.

### ODCIStatsExchangePartition()

Exchanges domain index statistics when an `ALTER TABLE EXCHANGE PARTITION ... INCLULDING INDEXES` command is issued.

Syntax

```
FUNCTION ODCIStatsExchangePartition(
   ia ODCIIndexInfo, 
   ia1 ODCIIndexInfo,
   env ODCIEnv) 
return NUMBER;
```

| Parameter | IN/OUT | Description |
| --- | --- | --- |
| ``` ia ``` |  | Information about the partition that must be exchanged |
| ``` sia1 ``` |  | Information about the index of the n-n-partitioned table with which the partition is exchanged |
| ``` env ``` |  | Contains general information about the environment in which the routine is executing |

Returns

`ODCIConst.Success`, `ODCIConst.Error`, or `ODCIConst.Warning`

Usage Notes

- This method should be implemented as a `STATIC` type.
- This method should be capable of converting the statistics associated with a domain index partition into statistics associated with a non-partitioned domain index, and the reverse. If the statistics are missing for one of the indexes or index partitions, the user should be able to delete these statistics.

### ODCIStatsIndexCost()

Calculates the cost of a domain index scan, either a scan of the entire index or a scan of one or more index partitions if a local domain index has been built.

Syntax

```
FUNCTION ODCIStatsIndexCost(
   ia ODCIIndexInfo, 
   sel NUMBER, 
   cost OUT ODCICost, 
   qi ODCIQueryInfo, 
   pred ODCIPredInfo, 
   args ODCIArgDescList,
   start operator_return_type,
   stop operator_return_type,
   list, 
   env ODCIEnv) 
return NUMBER;
```

| Parameter | IN/OUT | Description |
| --- | --- | --- |
| ``` ia ``` |  | domain index for which statistics are being collected |
| ``` sel ``` |  | the user-computed selectivity of the predicate |
| ``` cost ``` |  | computed cost (must be positive whole numbers) |
| ``` qi ``` |  | Information about the query |
| ``` pred ``` |  | Information about the predicate |
| ``` args ``` |  | Descriptor of `start`, `stop`, and actual value arguments with which the operator was called. If the operator has n arguments, the `args` array contains n+1 elements, the first element describing the start value, the second element describing the stop value, and the remaining n-1 elements describing the actual value arguments of the operator (that is, the arguments after the first) |
| ``` start ``` |  | Lower bound of the operator (for example, 2 for a predicate `fn(...)` > `2)` |
| ``` stop ``` |  | Upper bound of the operator (for example, 5 for a predicate `fn(...)` `<` `5`) |
| ``` list ``` |  | List of actual parameters to the operator (excluding the first); the number, position, and type of each argument must be identical to the one in the operator. |
| ``` env ``` |  | Contains general information about the environment in which the routine is executing |

Returns

`ODCIConst.Success`, `ODCIConst.Error`, or `ODCIConst.Warning`

Usage Notes

- For each table in the query, the optimizer uses partition pruning to determine the range of partitions that may be accessed. These partitions are called interesting partitions. The set of interesting partitions for a table is also the set of interesting partitions for all domain indexes on that table. The cost of a domain index can depend on the set of interesting partitions, so the optimizer passes a list of interesting index partitions to `ODCIStatsIndexCost` in the `args` argument (the type of this argument, `ODCIArgDescList`, is a list of `ODCIArgDesc` argument descriptor types) for those arguments that are columns. For non-partitioned domain indexes or for cases where no partition pruning is possible, no partition list is passed to `ODCIStatsIndexCost`, and you should assume that the entire index is accessed.
- The domain index key can contain multiple column arguments (for example, the indexed column and column arguments from other tables appearing earlier in a join order). For each column appearing in the index key, the `args` argument contains the list of interesting partitions for the table. For example, for an index key
	```
	op(T1.c1, T2.c2) = 1
	```
	the optimizer passes a list of interesting partitions for tables `T1` and `T2` if they are partitioned and there is partition pruning for them.
- This function should be implemented as a static type method.
- Only a single call is made to the ODCIStatsIndexCost() function for queries on partitioned or non-partitioned tables. For queries on partitioned tables, additional information is passed in the ODCIStatsIndexCost() function. Note that some partitions in the list passed to ODCIStatsIndexCost() may not actually be accessed by the query. The list of interesting partitions chiefly serves to exclude partitions that are definitely not accessed.
- When the ODCIStatsIndexCost() function is invoked, users can fill in a string in the `IndexCostInfo` field of the cost attribute to supply any additional information that might be helpful. The string (255 characters maximum) is displayed in the `OPTIONS` column in the `EXPLAIN PLAN` output when an execution plan chooses a domain index scan.
- Users implementing this function must return `'SYS.ODCISTATS2'` in the ODCIGetInterfaces() call.

### ODCIStatsSelectivity()

Specifies the selectivity of a predicate. The selectivity of a predicate involving columns from a single table is the fraction of rows of that table that satisfy the predicate. For predicates involving columns from multiple tables (for example, join predicates), the selectivity should be computed as a fraction of rows in the Cartesian product of those tables.

Syntax

```
FUNCTION ODCIStatsSelectivity(
   pred ODCIPredInfo, 
   sel OUT NUMBER, 
   args ODCIArgDescList, 
   start function_return_type, 
   stop function_return_type, 
   list, 
   env ODCIEnv) 
return NUMBER;
```

| Parameter | IN/OUT | Description |
| --- | --- | --- |
| `pred` |  | Predicate for which the selectivity is being computed |
| `sel` |  | The computed selectivity, expressed as a number between (and including) 0 and 100, representing a percentage. |
| `args` |  | Descriptor of `start`, `stop`, and actual arguments with which the function, type method, or operator was called. If the function has n arguments, the `args` array contains n+2 elements, the first element describing the start value, the second element describing the stop value, and the remaining n elements describing the actual arguments of the function, method, or operator |
| `start` |  | Lower bound of the function (for example, 2 for a predicate `fn(...)` `>` `2`) |
| `stop` |  | Upper bound of the function (for example, 5 for a predicate `fn(...)` `<` `5)` |
| `list` |  | List of actual parameters to the function or type method; the number, position, and type of each argument must be identical to the one in the function, type method, or operator. |
| `env` |  | Contains general information about the environment in which the routine is executing |

Returns

`ODCIConst.Success`, `ODCIConst.Error`, or `ODCIConst.Warning`

Usage Notes

- As in `ODCIStatsIndexCost`, the args argument contains a list of interesting partitions for the tables whose columns are referenced in the predicate for which the selectivity has to be computed. These interesting partitions are partitions that cannot be eliminated by partition pruning as possible candidates to be accessed. The set of interesting partitions is passed to the function only if partition pruning has occurred (in other words, the interesting partitions are a strict subset of all the partitions).
- For example, when `ODCIStatsSelectivity` is called to compute the selectivity of the predicate:
	```
	f(T1.c1, T2.c2) > 4
	```
	the optimizer passes the list of interesting partitions for the table `T1` (in the argument descriptor for column `T1.c1`) if partition pruning is possible; similarly for the table `T2`.
	If a predicate contains columns from several tables, this information is indicated by the flag bit `PredMultiTable`, set in the `Flags` attribute of the `pred` argument.
- This function should be implemented as a static type method.
- Users implementing this interface must return `'SYS.ODCISTATS2'` in the `ODCIGetInterfaces` call.
- The selectivity of a predicate involving columns from a single table is the fraction of rows of that table that satisfy the predicate. For predicates involving columns from multiple tables (for example, join predicates), the selectivity should be computed as a fraction of rows in the Cartesian product of those tables. For tables with partition pruning, the selectivity should be expressed relative to the cardinalities of the interesting partitions of the tables involved.
	The selectivity of predicates involving columns on partitioned tables is computed relative to the rows in the interesting partitions. Thus, the selectivity of the predicate
	```
	g(T1.c1) < 5
	```
	is the percentage of rows in the set of interesting partitions (or all partitions if no partition pruning is possible) that satisfies this predicate. For predicates with columns from multiple tables, the selectivity must be relative to the number of rows in the cartesian product of the tables.
- For example, consider the predicate:
	```
	f(T1.c1, T2.c2) > 4
	```
	Suppose that the number of rows in the interesting partitions is 1000 for `T1` and 5000 for `T2`. The selectivity of this predicate must be expressed as the percentage of the 5,000,000 rows in the Cartesian product of `T1` and `T2` that satisfy the predicate.
- If a predicate contains columns from several tables, this information is indicated by the flag bit `PredMultiTable` set in the `Flags` attribute of the `pred` argument.
- A selectivity expressed relative to the base cardinalities of the tables involved may be only an approximation of the true selectivity if cardinalities (and other statistics) of the tables have been reduced based on single-table predicates or other joins earlier in the join order. However, this approximation to the true selectivity should be acceptable to most applications.
- Only one call is made to the `ODCIStatsSelectivity` function for queries on partitioned or non-partitioned tables. In the case of queries on partitioned tables, additional information is passed while calling the `ODCIStatsSelectivity` function.

### ODCIStatsTableFunction()

This function provides cardinality statistics for table functions and input cursor expressions.

Syntax

```
STATIC FUNCTION ODCIStatsTableFunction(
   func IN SYS.ODCIFuncInfo, 
   outStats OUT SYS.ODCITabFuncStats, 
   argDesc IN SYS.ODCIArgDescList, 
   list)
RETURN NUMBER;
```

| Parameter | IN/OUT | Description |
| --- | --- | --- |
| `func` |  | Table function name |
| `outStats` |  | Number of rows expected to be returned |
| `argDesc` |  | Description of the arguments to the table function |
| `list` |  | The arguments' compile-time values. Expressions that only have values at run time are represented by nulls. |

Returns

`ODCIConst.Success`, `ODCIConst.Error`, or `ODCIConst.Warning.`

### ODCIStatsUpdPartStatistics()

Updates statistics during partition maintenance operations. This lets the statistics type patch up the domain index statistics to correctly reflect the partition maintenance operation.

Syntax

```
STATIC FUNCTION ODCIStatsCollect(
   ia ODCIIndexInfo,
   palist ODCIPartInfoList,
   env ODCIEnv) 
RETURN NUMBER
```

| Parameter | IN/OUT | Description |
| --- | --- | --- |
| `ia` |  | Contains information about the domain index. It does not contain any partition specific information |
| palist |  | Contains information about the partitions that are to be dropped or added |
| ``` env ``` |  | Environment handle passed to the routine |

Returns

`ODCIConst.Success`, `ODCIConst.Error`, or `ODCIConst.Warning.`

- When the statistics type is specified by the `SYSTEM MANAGED` approach, then the ODCIStatsUpdPartStatistics() method is invoked only one time during PMO. Only DML and query are allowed in the method implementation.
- If the user maintains the domain index statistics in a global non-partitioned table, then the user should delete the entry for the user-defined statistics for the dropped partition (and optionally add a `NULL` entry for added partition). They can then check if `ODCIEnv.CallProperty` is `StatsGlobalAndPartition` or `StatsPartition`. If `ODCIEnv.CallProperty` is `StatsGlobalAndPartition` then they should aggregate all the available index partition statistics. If `ODCIEnv.CallProperty` is `StatsPartition` they can simply delete the aggregate statistics, or leave the aggregate statistics as they are. `ODCIEnv.CallProperty` cannot be `StatsGlobal` for this call.
- The user should use the information passed in by the `ODCIEnv.CallProperty` to determine the type of statistics to delete and adjust.
- If the method returns `ODCIConst.Error`, the error is ignored and the partition management operation continues.
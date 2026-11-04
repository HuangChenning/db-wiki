---
title: Using Extensible Optimizer
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/ext_optimizer.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 10 Using Extensible Optimizer

This chapter introduces the Oracle Database extensible optimizer, descibes the concepts of optimization, statistics, selectivity, and cost analysis, provides usage examples, and explains predicate ordering and the dependency model of optimizer.

This chapter contains these topics:

## Overview of Query Optimization

Query Optimization is the process of choosing the most efficient way to execute a SQL statement. When the cost-based optimizer was offered for the first time with Oracle7, Oracle supported only standard relational data. The introduction of objects extended the supported data types and functions. The Extensible Indexing feature discussed in [Chapter 9, "Defining Operators"](operators.md) introduces user-defined access methods.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for an introduction to optimization
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for information about using hints in SQL statements
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for information about `DBMS_STATS`

The extensible optimizer feature allows authors of user-defined functions and indexes to create statistics collection, selectivity, and cost functions that are used by the optimizer in choosing a query plan. The optimizer cost model is extended to integrate information supplied by the user to assess CPU and the I/O cost, where CPU cost is the number of machine instructions used, and I/O cost is the number of data blocks fetched.

Specifically, you can:

- Associate cost functions and default costs with domain indexes (partitioned or non-partitioned), indextypes, packages, and standalone functions. The optimizer can obtain the cost of scanning a single partition of a domain index, multiple domain index partitions, or an entire index.
- Associate selectivity functions and default selectivity with methods of object types, package functions, and standalone functions. The optimizer can estimate user-defined selectivity for a single partition, multiple partitions, or the entire table involved in a query.
- Associate statistics collection functions with domain indexes and columns of tables. The optimizer can collect user-defined statistics at both the partition level and the object level for a domain index or a table.
- Order predicates with functions based on cost.
- Select a user-defined access method (domain index) for a table based on access cost.
- Use the `DBMS_STATS` package to invoke user-defined statistics collection and deletion functions.
- Use new data dictionary views to include information about the statistics collection, cost, or selectivity functions associated with columns, domain indexes, indextypes or functions.
- Add a hint to preserve the order of evaluation for function predicates.

Please note that only the cost-based optimizer has been enhanced; Oracle has not altered the operation of the rule-based optimizer.

The optimizer generates an execution plan for SQL queries and DML statements `SELECT`, `INSERT`, `UPDATE`, or `DELETE`. For simplicity, we describe the generation of an execution plan in terms of a `SELECT` statement, but the process for DML statements is similar.

An execution plan includes an access method for each table in the `FROM` clause, and an ordering, called the join order, of the tables in the `FROM` clause. System-defined access methods include indexes, hash clusters, and table scans. The optimizer chooses a plan by generating a set of join orders, or permutations, by computing the cost of each, and then by selecting the process with the lowest cost. For each table in the join order, the optimizer computes the cost of each possible access method and join method and chooses the one with the lowest cost. The cost of the join order is the sum of the access method and join method costs. The costs are calculated using algorithms that comprise the cost model. The cost model includes varying level of detail about the physical environment in which the query is executed.

The optimizer uses statistics about the objects referenced in the query to compute the selectivity and costs. The statistics are gathered using the `DBMS_STATS` package. The selectivity of a predicate is the fraction of rows in a table that is chosen by the predicate, and it is a number between `0` and `1`.

The Extensible Indexing feature allows users to define new operators, indextypes, and domain indexes. For user-defined operators and domain indexes, the Extensible Optimizer feature enables you to control the three main components used by the optimizer to select an execution plan statistics, selectivity, and cost. In the following sections, we describe each of these components in greater detail.

### Statistics

Statistics for tables and indexes can be generated by using the `DBMS_STATS` package. In general, the more accurate the statistics, the better the execution plan generated by the optimizer.

#### User-Defined Statistics

The Extensible Optimizer feature lets you define statistics collection functions for domain indexes, indextypes, data types, individual table columns, and partitions. This means that whenever a domain index is analyzed, a call is made to the user-specified statistics collection function. The database does not know the representation and meaning of the user-collected statistics.

In addition to domain indexes, Oracle supports user-defined statistics collection functions for individual columns of a table, and for user-defined data types. In the former case, whenever a column is analyzed, the user-defined statistics collection function is called to collect statistics in addition to any standard statistics that the database collects. If a statistics collection function exists for a data type, it is called for each column of the table being analyzed that has the required type.

The cost of evaluating a user-defined function depends on the algorithm and the statistical properties of its arguments. It is not practical to store statistics for all possible combinations of columns that could be used as arguments for all functions. Therefore, Oracle maintains only statistics on individual columns. It is also possible that function costs depend on the different statistical properties of each argument. Every column could require statistics for every argument position of every applicable function. Oracle does not support such a proliferation of statistics and cost functions because it would decrease performance.

A user-defined function to drop statistics is required whenever there is a user-defined statistics collection function.

#### User-Defined Statistics for Partitioned Objects

When using system-managed local domain indexes, you must implement two methods of the ODCIStats interface: [ODCIStatsExchangePartition()](ext_opt_ref.md), and [ODCIStatsUpdPartStatistics()](ext_opt_ref.md).

### Selectivity

The optimizer uses statistics to calculate the selectivity of predicates. The selectivity is the fraction of rows in a table or partition that is chosen by the predicate. It is a number between `0` and `1`. The selectivity of a predicate is used to estimate the cost of a particular access method; it is also used to determine the optimal join order. A poor choice of join order by the optimizer could result in a very expensive execution plan.

Currently, the optimizer uses a standard algorithm to estimate the selectivity of selection and join predicates. However, the algorithm does not always work well in cases in which predicates contain functions or type methods. In addition, predicates can contain user-defined operators about which the optimizer does not have any information. In that case the optimizer cannot compute an accurate selectivity.

#### User-Defined Selectivity

For greater control over the optimizer's selectivity estimation, this feature lets you specify user-defined selectivity functions for predicates containing user-defined operators, standalone functions, package functions, or type methods. The user-defined selectivity function is called by the optimizer whenever it encounters a predicate with one of the forms shown in Example 10-1:

Example 10-1 Three Predicate Forms that Trigger a Call to the Optimizer

```
operator(...) relational_operator constant
constant relational_operator operator(...)
operator(...) LIKE constant
```

where

- `operator(...)` is a user-defined operator, standalone function, package function, or type method,
- `relational_operator` is one of `{<, <=, =, >=, >}`, and
- `constant` is a constant value expression or bind variable.

For such cases, users can define selectivity functions associated with `operator(...)`. The arguments to `operator` can be columns, constants, bind variables, or attribute references. When optimizer encounters such a predicate, it calls the user-defined selectivity function and passes the entire predicate as an argument (including the operator, function, or type method and its arguments, the relational operator `relational_operator`, and the constant expression or bind variable). The return value of the user-defined selectivity function must be expressed as a percent, and be between 0 and 100 inclusive; the optimizer ignores values outside this range.

Wherever possible, the optimizer uses user-defined selectivity values. However, this is not possible in the following cases:

- The user-defined selectivity function returns an invalid value (less than `0` or greater than `100`).
- There is no user-defined selectivity function defined for the operator, function, or method in the predicate.
- The predicate does not have one of the forms listed in Example 10-1; it may also be of the form `operator(...) + 3 relational_operator` `constant`.

In each of these cases, the optimizer uses heuristics to estimate the selectivity.

### Cost

The optimizer estimates the cost of various access paths to choose an optimal plan. For example, it computes the CPU and I/O cost of using an index and a full table scan to choose between the two. However the optimizer does not know the internal storage structure of domain indexes, and so it cannot compute a good estimate of the cost of a domain index.

#### User-Defined Cost

For greater flexibility, the cost model has been extended to let you define costs for domain indexes, index partitions, and user-defined standalone functions, package functions, and type methods. The user-defined costs can be in the form of default costs that the optimizer looks up, or they can be full-fledged cost functions which the optimizer calls to compute the cost.

Like user-defined selectivity statistics, user-defined cost statistics are optional. If no user-defined cost is available, the optimizer uses heuristics to compute an estimate. However, in the absence of sufficient useful information about the storage structures in user-defined domain indexes and functions, such estimates can be very inaccurate and result in the choice of a sub-optimal execution plan.

User-defined cost functions for domain indexes are called by the optimizer only if a domain index is a valid access path for a user-defined operator (for details regarding when this is true, see the discussion of user-defined indexing in the previous chapter). User-defined cost functions for functions, methods and domain indexes are only called when a predicate has one of the forms outlined in Example 10-1, which is identical to the conditions for user-defined selectivity functions.

User-defined cost functions can return three cost values, each value representing the cost of a single execution of a function or domain index implementation:

- `CPU` — the number of machine cycles executed by the function or domain index implementation. This does not include the overhead of invoking the function.
- `I/O` — the number of data blocks read by the function or domain index implementation. For a domain index, this does not include accesses to the Oracle table. The multiblock I/O factor is not passed to the user-defined cost functions.
- `NETWORK` — the number of data blocks transmitted. This is valid for distributed queries, functions, andand domain index implementations. For Oracle this cost component is not used and is ignored; however, as described in the following sections, the user is required to stipulate a value so that backward compatibility is facilitated when this feature is introduced.

The optimizer computes a composite cost from these cost values.

The package `DBMS_ODCI` contains a function `estimate_cpu_units` to help get the CPU and I/O cost from input consisting of the elapsed time of a user function. `estimate_cpu_units` measures CPU units by multiplying the elapsed time by the processor speed of the machine and returns the approximate number of CPU instructions associated with the user function. For a multiprocessor machine, `estimate_cpu_units` considers the speed of a single processor.

The cost of a query is a function of the cost values. The settings of optimizer initialization parameters determine which cost to minimize. If `optimizer_mode` is `first_rows`, the resource cost of returning a single row is minimized, and the optimizer mode is passed to user-defined cost functions. Otherwise, the resource cost of returning all rows is minimized.

## Defining Statistics, Selectivity, and Cost Functions

You can compute and store user-defined statistics for domain indexes and columns. User-defined selectivity and cost functions for functions and domain indexes can use both standard and user-defined statistics in their computation. The internal representation of these statistics need not be known to Oracle, but you must provide methods for their collection. You are solely responsible for defining the representation of such statistics and for maintaining them. Note that user-collected statistics are used only by user-defined selectivity and cost functions; the optimizer uses only its standard statistics.

User-defined statistics collection, selectivity, and cost functions must be defined in a user-defined type. Depending on the functionality you want it to support, this type must implement as methods some or all of the functions defined in the system interface `ODCIStats`, Oracle Data Cartridge Interface Statistics, in [Chapter 21, "Extensible Optimizer Interface"](ext_opt_ref.md).

Example 10-2 shows a type definition (or the outline of one) that implements all the functions in the `ODCIStats` interface.

Example 10-2 Defining a Statistics Type

```
CREATE TYPE my_statistics AS OBJECT (

  -- Function to get current interface
  FUNCTION ODCIGetInterfaces(ifclist OUT ODCIObjectList) RETURN NUMBER,

   -- User-defined statistics functions
  FUNCTION ODCIStatsCollect(col ODCIColInfo, options ODCIStatsOptions,
    statistics OUT RAW, env ODCIEnv) RETURN NUMBER,
  FUNCTION ODCIStatsCollect(ia ODCIIndexInfo, options ODCIStatsOptions,
    statistics OUT RAW, env ODCIEnv) RETURN NUMBER,
  FUNCTION ODCIStatsDelete(col ODCIColInfo, statistics OUT RAW, env ODCIEnv) 
    RETURN NUMBER,
  FUNCTION ODCIStatsDelete(ia ODCIIndexInfo, statistics OUT RAW, env ODCIEnv) 
    RETURN NUMBER,
   
  -- User-defined statistics functions for local domain index
  FUNCTION ODCIStatsUpdPartStatistics(ia ODCIIndexInfo, palistODCIPartInfoList,
    env ODCIEnv) RETURN NUMBER;
  FUNCTION ODCIStatsExchangePartition(ia ODCIIndexInfo, ia1 ODCIIndexInfo, 
    env ODCIEnv) RETURN NUMBER;

  -- User-defined selectivity function
  FUNCTION ODCIStatsSelectivity(pred ODCIPredInfo, sel OUT NUMBER, args
    ODCIArgDescList, start <function_return_type>,
    stop <function_return_type>, <list of function arguments>, 
    env ODCIEnv) RETURN NUMBER,

  -- User-defined cost function for functions and type methods
  FUNCTION ODCIStatsFunctionCost(func ODCIFuncInfo, cost OUT ODCICost,
    args ODCIArgDescList, <list of function arguments>) RETURN NUMBER,

  -- User-defined cost function for domain indexes
  FUNCTION ODCIStatsIndexCost(ia ODCIIndexInfo, sel NUMBER,
    cost OUT ODCICost, qi ODCIQueryInfo, pred ODCIPredInfo,         
    args ODCIArgDescList, start <operator_return_type>,
    stop <operator_return_type>, <list of operator value arguments>, 
    env ODCIEnv) RETURN NUMBER
)
```

The object type that you define, referred to as a statistics type, need not implement all the functions from `ODCIStats`. User-defined statistics collection, selectivity, and cost functions are optional, so a statistics type may contain only a subset of the functions in `ODCIStats`. Table 10-1 lists the type methods and default statistics associated with different kinds of schema objects.

Table 10-1 Statistics Methods and Default Statistics for Various Schema Objects

| ASSOCIATE STATISTICS | Statistics Type Methods Used | Default Statistics |
| --- | --- | --- |
| column | [ODCIStatsCollect()](ext_opt_ref.md), [ODCIStatsDelete()](ext_opt_ref.md) |  |
| object type | [ODCIStatsCollect()](ext_opt_ref.md), [ODCIStatsDelete()](ext_opt_ref.md), [ODCIStatsFunctionCost()](ext_opt_ref.md), [ODCIStatsSelectivity()](ext_opt_ref.md) | cost, selectivity |
| function | [ODCIStatsFunctionCost()](ext_opt_ref.md), [ODCIStatsSelectivity()](ext_opt_ref.md) | cost, selectivity |
| package | [ODCIStatsFunctionCost()](ext_opt_ref.md), [ODCIStatsSelectivity()](ext_opt_ref.md) | cost, selectivity |
| index | [ODCIStatsCollect()](ext_opt_ref.md), [ODCIStatsDelete()](ext_opt_ref.md), [ODCIStatsIndexCost()](ext_opt_ref.md) | cost |
| indextype | [ODCIStatsCollect()](ext_opt_ref.md), [ODCIStatsDelete()](ext_opt_ref.md), [ODCIStatsIndexCost()](ext_opt_ref.md), [ODCIStatsUpdPartStatistics()](ext_opt_ref.md), [ODCIStatsExchangePartition()](ext_opt_ref.md) | cost |

The types of the parameters of statistics type methods are system-defined ODCI data types. These are described in [Chapter 21, "Extensible Optimizer Interface"](ext_opt_ref.md).

The selectivity and cost functions must not change any database or package state. Consequently, no SQL DDL or DML operations are permitted in the selectivity and cost functions. If such operations are present, the functions are not called by the optimizer.

### User-Defined Statistics Functions

There are two user-defined statistics collection functions, one for collecting statistics and the other for deleting them.

The first, [ODCIStatsCollect()](ext_opt_ref.md), is used to collect user-defined statistics; its interface depends on whether a column or domain index is being analyzed. It is called when analyzing a column of a table or a domain index and takes two parameters:

- `col` for the column being analyzed, or `ia` for the domain index being analyzed;
- `options` for options specified in the `DBMS_STATS` package.

As mentioned, the database does not interpret statistics collected by [ODCIStatsCollect()](ext_opt_ref.md). For system-managed domain index statistics, you don't return the statistics collected by [ODCIStatsCollect()](ext_opt_ref.md). You should store these statistics in a user-managed format, as described in section "Generating Statistics for System-Managed Domain Indexes", and illustrated in Figure 10-1, Figure 10-2, and Figure 10-3.

User-collected statistics are deleted by calling the [ODCIStatsDelete()](ext_opt_ref.md) function whose interface depends on whether the statistics for a column or domain index are being dropped. It takes a single parameter: `col`, for the column whose user-defined statistics must be deleted, or `ia`, for the domain index whose statistics are to be deleted.

If a user-defined [ODCIStatsCollect()](ext_opt_ref.md) function is present in a statistics type, the corresponding [ODCIStatsDelete()](ext_opt_ref.md) function must also be present.

The return values of the [ODCIStatsCollect()](ext_opt_ref.md) and [ODCIStatsDelete()](ext_opt_ref.md) functions must be `Success`, `Error`, or `Warning`; these return values are defined in a system package `ODCIConst`.

### User-Defined Selectivity Functions

User-defined selectivity functions are used only for predicate forms listed in Example 10-1.

A user-defined selectivity function [ODCIStatsSelectivity()](ext_opt_ref.md) takes five sets of input parameters that describe the predicate:

- The `pred` parameter describes the function `operator` and the relational operator `relational_operator`.
- The `args` parameter describes the start and stop values (that is, < `constant` >) of the function and the actual arguments to the function (`operator()`).
- The `start` parameter, whose data type is identical to that of the function's return value, describes the start value of the function.
- The `stop` parameter, whose data type is identical to that of the function's return value, describes the stop value of the function.
- A list of function arguments whose number, position, and type must match the arguments of the function `operator`.

The computed selectivity is returned in the output parameter `sel` as a number between `0` and `100` (inclusive) that represents a percentage. The optimizer ignores numbers less than `0` or greater than `100` as invalid values.

The return value of the [ODCIStatsSelectivity()](ext_opt_ref.md) function must be one of `Success`, `Error`, or `Warning`.

As an example, consider a function `myFunction`, as defined in Example 10-3.

Example 10-3 Defining a User-Defined Function

```
myFunction (a NUMBER, b VARCHAR2(10)) return NUMBER
```

A user-defined selectivity function [ODCIStatsSelectivity()](ext_opt_ref.md) is detailed in [Chapter 21, "Extensible Optimizer Interface"](ext_opt_ref.md).

If `myFunction()` is called using literal arguments, such as `myFunction(2, 'TEST') > 5`, then the selectivity function is called as out lined in Example 10-4.

Example 10-4 Calling a Selectivity Function Using Literal Arguments

```
ODCIStatsSelectivity(ODCIPredInfo_constructor, sel,
   ODCIArgDescList_constructor, 5, NULL, 2, 'TEST', ODCIEnv_flag)
```

If, on the other hand, `myFunction()` is called with some non-literals arguments, such as `myFunction(Test_tab.col_a, 'TEST')> 5`, where `col_a` is a column in table `Test_tab`, then the selectivity function is called as outlined in Example 10-5.

Example 10-5 Calling a Selectivity Function Using Non-Literal Arguments

```
ODCIStatsSelectivity(ODCIPredInfo_constructor, sel,
   ODCIArgDescList_constructor, 5, NULL, NULL, 'TEST', ODCIEnv_flag)
```

In summary, the start, stop, and function argument values are passed to the selectivity function only if they are literals; otherwise they are `NULL`. [ODCIArgDescList](ext_types_ref.md) describes all the arguments that follow it.

### User-Defined Cost Functions for Functions

User-defined cost functions are only used for predicate forms listed in Example 10-1.

You can define a function, [ODCIStatsFunctionCost()](ext_opt_ref.md), for computing the cost of standalone functions, package functions, or type methods. This function takes three sets of input parameters describing the predicate:

- The `func` parameter describes the function `operator`.
- The `args` parameter describes the actual arguments to the function `operator`.
- A list of function arguments whose number, position, and type must match the arguments of the function `operator`.

The [ODCIStatsFunctionCost()](ext_opt_ref.md) function returns its computed cost in the `cost` parameter. The returned cost can have two components, a CPU cost and an I/O cost, which are combined by the optimizer to compute a composite cost. The costs returned by user-defined cost functions must be positive whole numbers. Invalid values are ignored by the optimizer.

The return value of the [ODCIStatsFunctionCost()](ext_opt_ref.md) function must be one of `Success`, `Error`, or `Warning`.

Consider a `myFunction()`, defined in Example 10-3.

A user-defined cost function [ODCIStatsFunctionCost()](ext_opt_ref.md) is detailed in [Chapter 21, "Extensible Optimizer Interface"](ext_opt_ref.md).

If `myFunction()` is called using literal arguments, such as `myFunction(2, 'TEST') > 5`, where `col_a` is a column in table `Test_tab`, then the cost function is called as out lined in Example 10-6.

Example 10-6 Calling a Cost Function Using Literal Arguments

```
ODCIStatsFunctionCost(ODCIFuncInfo_constructor, cost,
   ODCIArgDescList_constructor, 2, 'TEST', ODCIEnv_flag)
```

If, on the other hand, `myFunction()` is called with non-literal arguments, such as `myFunction(Test_tab.col_a, 'TEST') > 5`, where `col_a` is a column in table `Test_tab`, then the cost function is called as out lined in Example 10-7.

Example 10-7 Calling a Cost Function Using Non-Literal Arguments

```
ODCIStatsFunctionCost(ODCIFuncInfo_constructor, cost,
   ODCIArgDescList_constructor, NULL, 'TEST', ODCIEnv_flag)
```

In summary, function argument values are passed to the cost function only if they are literals; otherwise, they are `NULL`. [ODCIArgDescList](ext_types_ref.md) describes all the arguments that follow it.

### User-Defined Cost Functions for Domain Indexes

User-defined cost functions for domain indexes are used for the same type of predicates mentioned previously, except that `operator` must be a user-defined operator for which a valid domain index access path exists.

The [ODCIStatsIndexCost()](ext_opt_ref.md) function takes these sets of parameters:

- `ia` describing the domain index
- `sel` representing the user-computed selectivity of the predicate
- `cost` giving the computed cost
- `qi` containing additional information about the query
- `pred` describing the predicate
- `args` describing the start and stop values (that is, < `constant` >) of the operator and the actual arguments to the operator `operator`
- `start`, whose data type is identical to that of the operator's return value, describing the start value of the operator
- `stop` whose data type is identical to that of the operator's return value, describing the stop value of the operator
- a list of operator value arguments whose number, position, and type must match the arguments of the operator `operator`. The value arguments of an operator are the arguments excluding the first argument.
- `env`, an environment flag set by the server to indicate which call is being made in cases where multiple calls are made to the same routine. The flag is reserved for future use; currently it is always set to `0`.

The computed cost of the domain index is returned in the output parameter, `cost`.

[ODCIStatsIndexCost()](ext_opt_ref.md) returns `Success`, `Error` or `Warning`.

Consider an operator defined in Example 10-8, which returns `1` or `0` depending on whether or not the string `b_string` is contained in the string `a_string`. Further, assume that the operator is implemented by a domain index.

Example 10-8 Defining an Operator

```
Contains(a_string VARCHAR2(2000), b_string VARCHAR2(10))
```

A user-defined index cost function [ODCIStatsIndexCost()](ext_opt_ref.md) is detailed in [Chapter 21, "Extensible Optimizer Interface"](ext_opt_ref.md).

If `contains()` is called using non-literal arguments, such as `Contains(Test_tab.col_c,'TEST') <= 1`, then the index cost function is called as out lined in Example 10-9.

Example 10-9 Calling an Index Cost Function Using Non-Literal Arguments

```
ODCIStatsIndexCost(ODCIIndexInfo_constructor, sel, cost,
   ODCIQueryInfo_constructor, ODCIPredInfo_constructor, 
   ODCIArgDescList_constructor, NULL, 1, 'TEST', ODCIEnv_flag)
```

Note that the first argument, `a_string`, of `Contains` does not appear as a parameter of [ODCIStatsIndexCost()](ext_opt_ref.md). This is because the first argument to an operator must be a column for the domain index to be used, and this column information is passed in through the `ODCIIndexInfo` parameter. Only the operator arguments after the first (the value arguments) must appear as parameters to the [ODCIStatsIndexCost()](ext_opt_ref.md) function.

In summary, the start, stop, and operator argument values are passed to the index cost function only if they are literals; otherwise they are `NULL`. [ODCIArgDescList](ext_types_ref.md) describes all the arguments that follow it.

### Generating Statistics for System-Managed Domain Indexes

If you choose the system-managed approach to maintain domain indexes and must associate a statistics type with the domain index or the indextype, then the statistics type must also be managed by the system.

Statistics may be collected when issuing an [ODCIStatsCollect()](ext_opt_ref.md) call for a system-managed domain index. For a non-partitioned index, the statistics may be stored with the index storage table, as a separate table, or in a data cartridge metadata table with index name qualified rows.

For local partitioned domain indexes, there are three options for storing statistics. All use the [ODCIStatsUpdPartStatistics()](ext_opt_ref.md) method during a partition maintenance operation in the following ways. Please note that in all the following examples, no DDLs are executed inside the [ODCIStatsUpdPartStatistics()](ext_opt_ref.md) call, and only DML and query instructions are allowed in the implementation of [ODCIStatsUpdPartStatistics()](ext_opt_ref.md).

1. The system calls the [ODCIStatsUpdPartStatistics()](ext_opt_ref.md) method If the statistics are stored with the indexed data in the index storage (system-partitioned) tables, as illustrated in Figure 10-1. The method can optionally maintain any statistics-related partition metadata, or be a null operation. The server deletes or drops the statistics for the affected partitions along with the index data specific to these partitions.
	Figure 10-1 Storing Index-Specific Statistics with Index Tables
	![Description of Figure 10-1 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci049.gif "Description of Figure 10-1 follows")  
	[Description of "Figure 10-1 Storing Index-Specific Statistics with Index Tables"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci049.htm)
2. If the statistics are stored in separate system-partitioned tables, as illustrated in Figure 10-2, the server tracks the creation of these system partitioned tables of store statistics during an [ODCIStatsCollect()](ext_opt_ref.md) call. These tables are maintained by the server in the same manner as for index storage tables.
	Figure 10-2 Storing Index-Specific Statistics in a Separate Table
	![Description of Figure 10-2 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci050.gif "Description of Figure 10-2 follows")  
	[Description of "Figure 10-2 Storing Index-Specific Statistics in a Separate Table"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci050.htm)
3. If the statistics are stored in a non-partitioned table as either schema-name, index-name, or partition-name qualified rows, as illustrated in Figure 10-3, then you have to maintain the partition-level statistics with a call to [ODCIStatsUpdPartStatistics()](ext_opt_ref.md). The server does not perform any operation on these tables.
	Figure 10-3 Storing Index-Partition Statistics in a Common Table
	![Description of Figure 10-3 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci051.gif "Description of Figure 10-3 follows")  
	[Description of "Figure 10-3 Storing Index-Partition Statistics in a Common Table"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci051.htm)

## Using User-Defined Statistics, Selectivity, and Cost

Statistics types act as interfaces for user-defined functions that influence the choice of an execution plan by the optimizer. However, for the optimizer to be able to use a statistics type, it requires a mechanism to bind the statistics type to a database object such as a column, a standalone function, an object type, an index, an indextype or a package. You cannot associate a statistics type with a partition of a table or a partition of a domain index. The `ASSOCIATE` `STATISTICS` command creates this association. The following sections describe this command in more detail.

### User-Defined Statistics

User-defined statistics functions are relevant for columns that use both standard SQL data types and object types, and for domain indexes. The functions [ODCIStatsSelectivity()](ext_opt_ref.md), [ODCIStatsFunctionCost()](ext_opt_ref.md), and [ODCIStatsIndexCost()](ext_opt_ref.md) are not used for user-defined statistics, so statistics types used only to collect user-defined statistics need not implement these functions. The following sections describe how to collect column and index user-defined statistics.

Users could create their own tables. This approach requires that privileges on these tables be administered properly, backup and restoration of these tables be done along with other dictionary tables, and point-in-time recovery considerations be resolved.

#### Column Statistics

Consider a table `Test_tab`, defined as in Example 10-10, where `typ1` is an object type.

Example 10-10 Creating a Table with an Object Type Column

```
CREATE TABLE Test_tab (
   col_a    NUMBER,
   col_b    typ1,
   col_c    VARCHAR2(2000)
)
```

Suppose that `stat` is a statistics type that implements [ODCIStatsCollect()](ext_opt_ref.md) and [ODCIStatsDelete()](ext_opt_ref.md) functions.User-defined statistics are collected by the `DBMS_STATS` package for the column `col_b` if we bind a statistics type with the column, as demonstrated in Example 10-11:

Example 10-11 Associating Statistics with Columns for User-Defined Statistics

```
ASSOCIATE STATISTICS WITH COLUMNS Test_tab.col_b USING stat
```

A list of columns can be associated with the statistics type `stat`. Note that Oracle supports only associations with top-level columns, not attributes of object types; if you wish, the [ODCIStatsCollect()](ext_opt_ref.md) function can collect individual attribute statistics by traversing the column.

Another way to collect user-defined statistics is to declare an association with a data type, as in Example 10-12, which declares `stat_typ1` as the statistics type for the type `typ1`. When the table `Test_tab` is analyzed with this association, user-defined statistics are collected for the column `col_b` using the [ODCIStatsCollect()](ext_opt_ref.md) function of statistics type `stat_typ1`.

Example 10-12 Associating Statistics with Data Types for User-Defined Statistics

```
ASSOCIATE STATISTICS WITH TYPES typ1 USING stat_typ1
```

Individual column associations always have precedence over associations with types. Thus, in the preceding example, if both `ASSOCIATE` `STATISTICS` commands are issued, `DBMS_STATS` would use the statistics type `stat` (and not `stat_typ1`) to collect user-defined statistics for column `col_b`. It is also important to note that standard statistics, if possible, are collected along with user-defined statistics.

User-defined statistics are deleted using the [ODCIStatsDelete()](ext_opt_ref.md) function from the same statistics type that was used to collect the statistics.

Associations defined by the `ASSOCIATE` `STATISTICS` command are stored in a dictionary table called `ASSOCIATION$`.

Only user-defined data types can have statistics types associated with them; you cannot declare associations for standard SQL data types.

#### Domain Index Statistics

A domain index has an indextype. A statistics type for a system-managed domain index is defined by associating it only with its indextype. Example 10-13 demonstrates how to create an indextype, an index, and an operator on the table `Test_tab` from Example 10-10:

Example 10-13 Creating an Indextype, an Index and an Operator for User-Defined Statistics

```
CREATE INDEXTYPE indtype
FOR userOp(NUMBER)
USING imptype WITH SYSTEM MANAGED STORAGE TABLES;

CREATE INDEX Test_indx ON Test_tab(col_a)
INDEXTYPE IS indtype PARAMETERS('example');

CREATE OPERATOR userOp BINDING (NUMBER) RETURN NUMBER
USING userOp_func;
```

Here, `indtype` is the indextype, `userOp` is a user-defined operator supported by `indtype`, `userOp_func` is the functional implementation of `userOp`, and `imptype` is the implementation type of the indextype `indtype`.

A statistics type `stat_indtype` can be associated with the system-managed indextype, as demonstrated in Example 10-14. When the domain index `Test_indx` that has an indextype `indtype` is analyzed, user-defined statistics for the index are collected by calling the [ODCIStatsCollect()](ext_opt_ref.md) function of `stat_indtype`.

Example 10-14 Associating Statistics with System-Managed Indextypes

```
ASSOCIATE STATISTICS WITH INDEXTYPES indtype USING stat_indtype
WITH SYSTEM MANAGED STORAGE TABLES
```

To drop index statistics, use the [ODCIStatsDelete()](ext_opt_ref.md) method which is defined for the same statistics type that defined the earlier [ODCIStatsCollect()](ext_opt_ref.md) method.

### User-Defined Selectivity

The optimizer uses selectivity functions to compute the selectivity of predicates in a query. The predicates must have one of the appropriate forms and can contain user-defined operators, standalone functions, package functions, or type methods. The following sections describe selectivity computation for each.

#### User-Defined Operators

Suppose that the association in Example 10-15 is declared. If the optimizer encounters the `userOp(Test_tab.col_a) = 1` predicate, it calls the [ODCIStatsSelectivity()](ext_opt_ref.md) function (if present) in the statistics type `stat_userOp_func` that is associated with the functional implementation of the `userOp_func` of the `userOp` operator.

Example 10-15 Associating Statistics with User-Defined Operators

```
ASSOCIATE STATISTICS WITH FUNCTIONS userOp_func USING stat_userOp_func
```

#### Standalone Functions

If the association in Example 10-16 is declared for a standalone function `myFunction`, then the optimizer calls the [ODCIStatsSelectivity()](ext_opt_ref.md) function (if present) in the statistics type `stat_myFunction` for the `myFunction(Test_tab.col_a, 'TEST') = 1` predicate.

Example 10-16 Associating Statistics with Standalone Functions

```
ASSOCIATE STATISTICS WITH FUNCTIONS myFunction USING stat_MyFunction
```

#### Package Functions

If the association in Example 10-17 is declared for a package `Demo_pack`, then the optimizer calls the [ODCIStatsSelectivity()](ext_opt_ref.md) function (if present) in the statistics type `stat_Demo_pack` for the `Demo_pack.myDemoPackFunction(Test_tab.col_a, 'TEST') = 1` predicate, where `myDemoPackFunction` is a function in `Demo_pack`.

Example 10-17 Associating Statistics with Package Functions

```
ASSOCIATE STATISTICS WITH PACKAGES Demo_pack USING stat_Demo_pack
```

#### Type Methods

If the association in Example 10-18 is declared for a type `Example_typ`, then the optimizer calls the [ODCIStatsSelectivity()](ext_opt_ref.md) function (if present) in the statistics type `stat_Example_typ` for the `myExampleTypMethod(Test_tab.col_b) = 1` predicate, where `myExampleTypMethod` is a method in `Example_typ`.

Example 10-18 Associating Statistics with Type Methods

```
ASSOCIATE STATISTICS WITH TYPES Example_typ USING stat_Example_typ
```

#### Default Selectivity

An alternative to selectivity functions is user-defined default selectivity. The default selectivity is a value between `0` and `100%`; the optimizer looks it up instead of calling a selectivity function. Default selectivities can be used for predicates with user-defined operators, standalone functions, package functions, or type methods.

The association in Example 10-19 declares that the `myFunction(Test_tab.col_a) = 1` predicate always has a selectivity of `20%` (or `0.2`), regardless of the parameters of `myFunction,` the comparison operator `=`, or the constant `1`. The optimizer uses this default selectivity instead of calling a selectivity function.

Example 10-19 Associating Statistics with Default Selectivity

```
ASSOCIATE STATISTICS WITH FUNCTIONS myFunction DEFAULT SELECTIVITY 20
```

An association can be declared using either a statistics type or a default selectivity, but not both. Thus, the following statement is illegal:

```
ASSOCIATE STATISTICS WITH FUNCTIONS myFunction USING stat_myFunction
   DEFAULT SELECTIVITY 20
```

Other examples of default selectivity declarations include:

```
ASSOCIATE STATISTICS WITH PACKAGES Demo_pack DEFAULT SELECTIVITY 20
ASSOCIATE STATISTICS WITH TYPES Example_typ DEFAULT SELECTIVITY 20
```

### User-Defined Cost

The optimizer uses user-defined cost functions to compute the cost of predicates in a query. The predicates must have one of the forms listed earlier and can contain user-defined operators, standalone functions, package functions, or type methods. In addition, user-defined cost functions are also used to compute the cost of domain indexes. The following sections describe cost computation for each.

#### User-Defined Operators

If the association in Example 10-20 is declared, consider the `userOp(Test_tab.col_a) = 1` predicate. If the optimizer evaluates the domain index `Test_indx` with an `indtype` indextype that implements `userOp`, it calls the [ODCIStatsIndexCost()](ext_opt_ref.md) method (if present) in the statistics type `stat_indtype`. If the domain index is not used, however, the optimizer calls the [ODCIStatsFunctionCost()](ext_opt_ref.md) (if present) in the statistics type `stat_userOp` to compute the cost of the functional implementation of the operator `userOp`.

Example 10-20 Associating Statistics with User-Defined Operators

```
ASSOCIATE STATISTICS WITH INDEXTYPES indtype USING stat_indtype
  WITH SYSTEM MANAGED STORAGE TABLES
ASSOCIATE STATISTICS WITH FUNCTIONS userOp USING stat_userOp_func
```

#### Standalone Functions

If the association in Example 10-21 is declared for a standalone function `myFunction`, then the optimizer calls the [ODCIStatsFunctionCost()](ext_opt_ref.md) function (if present) in the statistics type `stat_myFunction` for the `myFunction(Test_tab.col_a, 'TEST') = 1` predicate.

Example 10-21 Associating Statistics with Standalone Functions

```
ASSOCIATE STATISTICS WITH FUNCTIONS myFunction USING stat_myFunction;
```

User-defined function costs do not influence the choice of access methods; they are only used for ordering predicates, described in [Chapter 21, "Extensible Optimizer Interface"](ext_opt_ref.md).

#### Package Functions

If the association in Example 10-22 is declared for a package `Demo_pack`, then the optimizer calls the [ODCIStatsFunctionCost()](ext_opt_ref.md) function, if present, in the statistics type `stat_Demo_pack` for the `Demo_pack.myDemoPackFunction(Test_tab.col_a) = 1` predicate, where `myDemoPackFunction` is a function in `Demo_pack`.

Example 10-22 Associating Statistics with Package Functions

```
ASSOCIATE STATISTICS WITH PACKAGES Demo_pack USING stat_Demo_pack;
```

#### Type Methods

If the association is declared, as in Example 10-23, for a type `Example_typ`, then the optimizer calls the [ODCIStatsFunctionCost()](ext_opt_ref.md) function, if present, in the statistics type `stat_Example_typ` for the `myExampleTypMethod(Test_tab.col_b) = 1` predicate, where `myExampleTypMethod` is a method in `Example_typ`.

Example 10-23 Associating Statistics with Type Methods

```
ASSOCIATE STATISTICS WITH TYPES Example_typ USING stat_Example_typ;
```

#### Default Cost

Like default selectivity, default costs can be used for predicates with user-defined operators, standalone functions, package functions, or type methods. The command in Example 10-24 declares that using the domain index `Test_indx` to implement the `userOp(Test_tab.col_a) = 1` predicate always has a CPU cost of `100`, an I/O cost of `5`, and a network cost of `0` (the network cost is ignored in Oracle), regardless of the parameters of `userOp`, the comparison operator " `=` ", or the constant " `1` ". The optimizer uses this default cost instead of calling the [ODCIStatsIndexCost()](ext_opt_ref.md) function.

Example 10-24 Associating Statistics with Default Cost

```
ASSOCIATE STATISTICS WITH INDEXES Test_indx DEFAULT COST (100, 5, 0);
```

You can declare an association using either a statistics type or a default cost but not both. Thus, the following statement is illegal:

```
ASSOCIATE STATISTICS WITH INDEXES Test_indx USING stat_Test_indx
   DEFAULT COST (100, 5, 0)
```

The following are some more examples of default cost declarations:

```
ASSOCIATE STATISTICS WITH FUNCTIONS myFunction DEFAULT COST (100, 5, 0)
ASSOCIATE STATISTICS WITH PACKAGES Demo_pack DEFAULT COST (100, 5, 0)
ASSOCIATE STATISTICS WITH TYPES Example_typ DEFAULT COST (100, 5, 0)
ASSOCIATE STATISTICS WITH INDEXTYPES indtype DEFAULT COST (100, 5, 0)
```

### Declaring a NULL Association for an Index or Column

An association of a statistics type defined for an indextype or object type is inherited by index instances of that indextype and by columns of that object type. An inherited association can be overridden by explicitly defining a different association for an index instance or column, but there may be occasions when you would prefer an index or column not to have any association at all. For example, for a particular query the benefit of a better plan may not outweigh the additional compilation time incurred by invoking the cost or selectivity functions. For cases like this, you can use the `ASSOCIATE` command to declare a `NULL` association for a column or index, as in Example 10-25.

Example 10-25 Declaring NULL Statistics Associations for Columns and Indexes

```
ASSOCIATE STATISTICS WITH COLUMNS columns NULL;
ASSOCIATE STATISTICS WITH INDEXES indexes NULL;
```

If the `NULL` association is specified, the schema object does not inherit any statistics type from the column type or the indextype. A `NULL` association also precludes default values.

### How Statistics Are Affected by DDL Operations

Partition-level and schema object-level aggregate statistics are affected by DDL operations in the same way as standard statistics. Table 10-2 summarizes the effects.

Table 10-2 Effects of DDL on Partition and Global Statistics

| Operation | Effect on Partition Statistics | Effect on Global Statistics |
| --- | --- | --- |
| ``` ADD PARTITION ``` | None | No Action |
| ``` DROP PARTITION ``` | Statistics deleted | Statistics recalculated (if \_ `minimal_stats_aggregation` is `FALSE`, otherwise no effect) |
| ``` SPLIT PARTITION ``` | Statistics deleted | None |
| ``` MERGE PARTITION ``` | Statistics deleted | None |
| ``` TRUNCATE PARTITION ``` | Statistics deleted | None |
| ``` EXCHANGE PARTITION ``` | Statistics deleted | Statistics recalculated (if \_ `minimal_stats_aggregation` is `FALSE`, otherwise no effect) |
| ``` REBUILD PARTITION ``` | None | None |
| ``` MOVE PARTITION ``` | None | None |
| ``` RENAME PARTITION ``` | None | None |

If an existing partition is exchanged, or dropped with an `ALTER TABLE DROP PARTITION` statement, and the `_minimal_stats_aggregation` parameter is set to `FALSE`, the statistics for that partition are deleted, and the aggregate statistics of the table or index are recalculated.

## Predicate Ordering

In the absence of an `ORDERED_PREDICATES` hint, predicates (except those used for index keys) are evaluated in the order specified by the following rules:

- Predicates without any user-defined functions, type methods, or subqueries are evaluated first, in the order specified in the `WHERE` clause.
- Predicates with user-defined functions and type methods which have user-computed costs are evaluated in increasing order of their cost.
- Predicates with user-defined functions and type methods that have no user-computed cost are evaluated next, in the order specified in the `WHERE` clause.
- Predicates not specified in the `WHERE` clause (for example, predicates transitively generated by the optimizer) are evaluated next.
- Predicates with subqueries are evaluated last in the order specified in the `WHERE` clause.

## Dependency Model

The dependency model reflects the actions that are taken when you issue any of the SQL commands described in Table 10-3.

Table 10-3 Dependency Model for DDLs

| Command | Action |
| --- | --- |
| ``` DROP statistics_type ``` | If an association is defined with `statistics_type`, the command fails, otherwise the type is dropped. |
| ``` DROP statistics_type FORCE ``` | Calls `DISASSOCIATE` `FORCE` for all objects associated with the `statistics_type`; drops `statistics_type`. |
| ``` DROP object ``` | Calls `DISASSOCIATE`, drops `object_type` if `DISASSOCIATE` succeeds. |
| ``` ALTER TABLE DROP COLUMN ``` | If association is present for the column, this calls `DISASSOCIATE` `FORCE` with column; if no entry in `ASSOCIATION$` but there are entries in type `USATS$,` then [ODCIStatsDelete()](ext_opt_ref.md) for the columns is invoked. |
| ``` DISASSOCIATE ``` | If user-defined statistics collected with the `statistics_type` are present, the command fails. |
| ``` DISASSOCIATE FORCE ``` | Deletes the entry in `ASSOCIATION$` and calls [ODCIStatsDelete()](ext_opt_ref.md). |
| Delete index statistics using the `DBMS_STATISTICS` package | The [ODCIStatsDelete()](ext_opt_ref.md) function is invoked; if any errors are raised, statistics deletion fails and an error is reported. |
| ``` ASSOCIATE ``` | If an association or user-defined statistics are present for the associated object, the command fails. |

## Restrictions and Suggestions

A statistics type is an ordinary object type. Since an object type must have at least one attribute, so must a statistics type. However, because it is never be accessed or set, this is a dummy attribute.

### Distributed Execution

Oracle's distributed implementation does not support adding functions to the remote capabilities list. All functions referencing remote tables are executed as filters. The placement of the filters occurs outside the optimizer. The cost model reflects this implementation and does not attempt to optimize placement of these predicates.

Since predicates are not shipped to the remote site, you cannot use domain indexes on remote tables. Therefore, the `DESCRIBE` protocol is unchanged, and remote domain indexes are not visible from the local site.

### System-Managed Storage Tables and ASSOCIATE STATISTICS

If you are creating an indextype `WITH SYSTEM MANAGED STORAGE TABLES`, you should also create its associated statistics type `WITH SYSTEM MANAGED STORAGE TABLES`. If you are collecting statistics on the local indexed column using system partitioned tables, then the Oracle server maintains the system-partitioned statistics tables for them during partition maintenance operations. You can only use the `WITH SYSTEM MANAGED STORAGE TABLES` option when an indextype is associated with the statistics type; otherwise the system raises an error.

### Aggregate Object-Level Statistics

When using local indexes, it may be useful to maintain both partition-level and aggregate object-level statistics. During partition maintenance operations, the partition level statistics are deleted, while the aggregate object-level statistics are either adjusted to reflect the operation or left "as is" for later recomputation.

The decision to adjust or recompute the aggregate statistics is made based on `_minimal_stats_aggregation` parameter in the server. If the parameter is `FALSE`, the aggregate statistics are recomputed. If the parameter is `TRUE`, the statistics are not recomputed.

### System-Managed Domain Indexing

The system-managed domain indexing approach supports system-managed statistics that are associated with indextypes; indextype itself should also be system-managed.

### Performance

The cost of execution of the queries remains the same with the extensible optimizer if the same plan is chosen. If a different plan is chosen, the execution time should be better assuming that the user-defined cost, selectivity, and statistics collection functions are accurate. In light of this, you are strongly encouraged to provide statistics collection, selectivity, and cost functions for user-defined structures because the optimizer defaults can be inaccurate and lead to an expensive execution plan.
---
title: SQL Tuning Guide
book: SQL Tuning Guide
doc_id: E85762-06
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/tgsql/reading-execution-plans.html
tags:
  - oracle
  - 12c
  - sql-tuning-guide
---

Execution plans are represented as a tree of operations.

This chapter contains the following topics:

### 7.1 Reading Execution Plans: Basic

This section uses `EXPLAIN PLAN` examples to illustrate execution plans.

The following query displays the execution plans:

```
SELECT PLAN_TABLE_OUTPUT 
  FROM TABLE(DBMS_XPLAN.DISPLAY(NULL, 'statement_id','BASIC'));
```

Examples of the output from this statement are shown in Example 7-4 and Example 7-1.

Example 7-1 EXPLAIN PLAN for Statement ID ex\_plan1

The following plan shows execution of a `SELECT` statement. The table `employees` is accessed using a full table scan. Every row in the table `employees` is accessed, and the `WHERE` clause criteria is evaluated for every row.

```
EXPLAIN PLAN 
  SET statement_id = 'ex_plan1' FOR
  SELECT phone_number 
  FROM   employees
  WHERE  phone_number LIKE '650%';

---------------------------------------
| Id  | Operation         | Name      |
---------------------------------------
|   0 | SELECT STATEMENT  |           |
|   1 |  TABLE ACCESS FULL| EMPLOYEES |
---------------------------------------
```

Example 7-2 EXPLAIN PLAN for Statement ID ex\_plan2

This following plan shows the execution of a `SELECT` statement. In this example, the database range scans the `EMP_NAME_IX` index to evaluate the `WHERE` clause criteria.

```
EXPLAIN PLAN 
  SET statement_id = 'ex_plan2' FOR
  SELECT last_name 
  FROM   employees
  WHERE  last_name LIKE 'Pe%';

SELECT PLAN_TABLE_OUTPUT 
  FROM TABLE(DBMS_XPLAN.DISPLAY(NULL, 'ex_plan2','BASIC'));

----------------------------------------
| Id  | Operation        | Name        |
----------------------------------------
|   0 | SELECT STATEMENT |             |
|   1 |  INDEX RANGE SCAN| EMP_NAME_IX |
----------------------------------------
```

### 7.2 Reading Execution Plans: Advanced

In some cases, execution plans can be complicated and challenging to read.

This section contains the following topics:

#### 7.2.1 Reading Adaptive Query Plans

The adaptive optimizer is a feature of the optimizer that enables it to adapt plans based on run-time statistics. All adaptive mechanisms can execute a final plan for a statement that differs from the default plan.

An [adaptive query plan](glossary.md) chooses among subplans during the current statement execution. In contrast, [automatic reoptimization](glossary.md) changes a plan only on executions that occur after the current statement execution.

You can determine whether the database used adaptive query optimization for a SQL statement based on the comments in the `Notes` section of plan. The comments indicate whether row sources are dynamic, or whether automatic reoptimization adapted a plan.

Assumptions

This tutorial assumes the following:

- The `STATISTICS_LEVEL` initialization parameter is set to `ALL`.
- The database uses the default settings for adaptive execution.
- As user `oe`, you want to issue the following separate queries:
	```
	SELECT o.order_id, v.product_name
	FROM   orders o,
	       (  SELECT order_id, product_name
	          FROM   order_items o, product_information p
	          WHERE  p.product_id = o.product_id
	          AND    list_price < 50
	          AND    min_price < 40  ) v
	WHERE  o.order_id = v.order_id
	SELECT product_name
	FROM   order_items o, product_information p  
	WHERE  o.unit_price = 15 
	AND    quantity > 1
	AND    p.product_id = o.product_id
	```
- Before executing each query, you want to query `DBMS_XPLAN.DISPLAY_PLAN` to see the default plan, that is, the plan that the optimizer chose before applying its adaptive mechanism.
- After executing each query, you want to query `DBMS_XPLAN.DISPLAY_CURSOR` to see the final plan and adaptive query plan.
- `SYS` has granted `oe` the following privileges:
	- `GRANT SELECT ON V_$SESSION TO oe`
		- `GRANT SELECT ON V_$SQL TO oe`
		- `GRANT SELECT ON V_$SQL_PLAN TO oe`
		- `GRANT SELECT ON V_$SQL_PLAN_STATISTICS_ALL TO oe`

To see the results of adaptive optimization:

1. Start SQL\*Plus, and then connect to the database as user `oe`.
2. Query `orders`.
	For example, use the following statement:
	```
	SELECT o.order_id, v.product_name
	FROM   orders o,
	       (  SELECT order_id, product_name
	          FROM   order_items o, product_information p
	          WHERE  p.product_id = o.product_id
	          AND    list_price < 50
	          AND    min_price < 40  ) v
	WHERE  o.order_id = v.order_id;
	```
3. View the plan in the cursor.
	For example, run the following commands:
	```
	SET LINESIZE 165
	SET PAGESIZE 0
	SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(FORMAT=>'+ALLSTATS'));
	```
	The following sample output has been reformatted to fit on the page. In this plan, the optimizer chooses a nested loops join. The original optimizer estimates are shown in the `E-Rows` column, whereas the actual statistics gathered during execution are shown in the `A-Rows` column. In the `MERGE JOIN` operation, the difference between the estimated and actual number of rows is significant.
	```
	--------------------------------------------------------------------------------------------
	|Id| Operation             | Name          |Start|E-Rows|A-Rows|A-Time|Buff|OMem|1Mem|O/1/M|
	--------------------------------------------------------------------------------------------
	| 0| SELECT STATEMENT      |                |   1|   | 269|00:00:00.09|1338|    |    |     |
	| 1|  NESTED LOOPS         |                |   1|  1| 269|00:00:00.09|1338|    |    |     |
	| 2|   MERGE JOIN CARTESIAN|                |   1|  4|9135|00:00:00.03|  33|    |    |     |
	|*3|    TABLE ACCESS FULL  |PRODUCT_INFORMAT|   1|  1|  87|00:00:00.01|  32|    |    |     |
	| 4|    BUFFER SORT        |                |  87|105|9135|00:00:00.01|   1|4096|4096|1/0/0|
	| 5|     INDEX FULL SCAN   | ORDER_PK       |   1|105| 105|00:00:00.01|   1|    |    |     |
	|*6|   INDEX UNIQUE SCAN   | ORDER_ITEMS_UK |9135|  1| 269|00:00:00.03|1305|    |    |     |
	--------------------------------------------------------------------------------------------
	 
	Predicate Information (identified by operation id):
	---------------------------------------------------
	 
	   3 - filter(("MIN_PRICE"<40 AND "LIST_PRICE"<50))
	   6 - access("O"."ORDER_ID"="ORDER_ID" AND "P"."PRODUCT_ID"="O"."PRODUCT_ID")
	```
4. Run the same query of `orders` that you ran in Step 2.
5. View the execution plan in the cursor by using the same `SELECT` statement that you ran in Step 3.
	The following example shows that the optimizer has chosen a different plan, using a hash join. The Note section shows that the optimizer used statistics feedback to adjust its cost estimates for the second execution of the query, thus illustrating automatic reoptimization.
	```
	--------------------------------------------------------------------------------------------
	|Id| Operation              |Name    |Start|E-Rows|A-Rows|A-Time|Buff|Reads|OMem|1Mem|O/1/M|
	--------------------------------------------------------------------------------------------
	| 0| SELECT STATEMENT       |               | 1 |   |269|00:00:00.02|60|1|     |     |     |
	| 1|  NESTED LOOPS          |               | 1 |269|269|00:00:00.02|60|1|     |     |     |
	|*2|   HASH JOIN            |               | 1 |313|269|00:00:00.02|39|1|1000K|1000K|1/0/0|
	|*3|    TABLE ACCESS FULL   |PRODUCT_INFORMA| 1 | 87| 87|00:00:00.01|15|0|     |     |     |
	| 4|    INDEX FAST FULL SCAN|ORDER_ITEMS_UK | 1 |665|665|00:00:00.01|24|1|     |     |     |
	|*5|   INDEX UNIQUE SCAN    |ORDER_PK       |269|  1|269|00:00:00.01|21|0|     |     |     |
	--------------------------------------------------------------------------------------------
	 
	Predicate Information (identified by operation id):
	---------------------------------------------------
	 
	   2 - access("P"."PRODUCT_ID"="O"."PRODUCT_ID")
	   3 - filter(("MIN_PRICE"<40 AND "LIST_PRICE"<50))
	   5 - access("O"."ORDER_ID"="ORDER_ID")
	 
	Note
	-----
	   - statistics feedback used for this statement
	```
6. Query `V$SQL` to verify the performance improvement.
	The following query shows the performance of the two statements (sample output included).
	```
	SELECT CHILD_NUMBER, CPU_TIME, ELAPSED_TIME, BUFFER_GETS
	FROM   V$SQL
	WHERE  SQL_ID = 'gm2npz344xqn8';
	 
	CHILD_NUMBER   CPU_TIME ELAPSED_TIME BUFFER_GETS
	------------ ---------- ------------ -----------
	           0      92006       131485        1831
	           1      12000        24156          60
	```
	The second statement executed, which is child number `1`, used statistics feedback. CPU time, elapsed time, and buffer gets are all significantly lower.
7. Explain the plan for the query of `order_items`.
	For example, use the following statement:
	```
	EXPLAIN PLAN FOR
	  SELECT product_name 
	  FROM   order_items o, product_information p  
	  WHERE  o.unit_price = 15
	  AND    quantity > 1  
	  AND    p.product_id = o.product_id
	```
8. View the plan in the plan table.
	For example, run the following statement:
	```
	SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);
	```
	Sample output appears below:
	```
	-------------------------------------------------------------------------------
	|Id| Operation                 | Name             |Rows|Bytes|Cost (%CPU)|Time|
	-------------------------------------------------------------------------------
	| 0| SELECT STATEMENT             |                      |4|128|7 (0)|00:00:01|
	| 1|  NESTED LOOPS                |                      | |   |     |        |
	| 2|   NESTED LOOPS               |                      |4|128|7 (0)|00:00:01|
	|*3|    TABLE ACCESS FULL         |ORDER_ITEMS           |4|48 |3 (0)|00:00:01|
	|*4|    INDEX UNIQUE SCAN         |PRODUCT_INFORMATION_PK|1|   |0 (0)|00:00:01|
	| 5|   TABLE ACCESS BY INDEX ROWID|PRODUCT_INFORMATION   |1|20 |1 (0)|00:00:01|
	-------------------------------------------------------------------------------
	 
	Predicate Information (identified by operation id):
	---------------------------------------------------
	 
	   3 - filter("O"."UNIT_PRICE"=15 AND "QUANTITY">1)
	   4 - access("P"."PRODUCT_ID"="O"."PRODUCT_ID")
	```
	In this plan, the optimizer chooses a nested loops join.
9. Run the query that you previously explained.
	For example, use the following statement:
	```
	SELECT product_name 
	FROM   order_items o, product_information p  
	WHERE  o.unit_price = 15
	AND    quantity > 1  
	AND    p.product_id = o.product_id
	```
10. View the plan in the cursor.
	For example, run the following commands:
	```
	SET LINESIZE 165
	SET PAGESIZE 0
	SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY(FORMAT=>'+ADAPTIVE'));
	```
	Sample output appears below. Based on statistics collected at run time (Step 4), the optimizer chose a hash join rather than the nested loops join. The dashes (`-`) indicate the steps in the nested loops plan that the optimizer considered but do not ultimately choose. The switch illustrates the adaptive query plan feature.
	```
	-------------------------------------------------------------------------------
	|Id | Operation                     | Name     |Rows|Bytes|Cost(%CPU)|Time    |
	-------------------------------------------------------------------------------
	|  0| SELECT STATEMENT              |                     |4|128|7(0)|00:00:01|
	| *1|  HASH JOIN                    |                     |4|128|7(0)|00:00:01|
	|- 2|   NESTED LOOPS                |                     | |   |    |        |
	|- 3|    NESTED LOOPS               |                     | |128|7(0)|00:00:01|
	|- 4|     STATISTICS COLLECTOR      |                     | |   |    |        |
	| *5|      TABLE ACCESS FULL        | ORDER_ITEMS         |4| 48|3(0)|00:00:01|
	|-*6|     INDEX UNIQUE SCAN         | PRODUCT_INFORMATI_PK|1|   |0(0)|00:00:01|
	|- 7|    TABLE ACCESS BY INDEX ROWID| PRODUCT_INFORMATION |1| 20|1(0)|00:00:01|
	|  8|   TABLE ACCESS FULL           | PRODUCT_INFORMATION |1| 20|1(0)|00:00:01|
	-------------------------------------------------------------------------------
	Predicate Information (identified by operation id):
	---------------------------------------------------
	   1 - access("P"."PRODUCT_ID"="O"."PRODUCT_ID")
	   5 - filter("O"."UNIT_PRICE"=15 AND "QUANTITY">1)
	   6 - access("P"."PRODUCT_ID"="O"."PRODUCT_ID")
	Note
	-----
	   - this is an adaptive plan (rows marked '-' are inactive)
	```

See Also:

- " [Adaptive Query Plans](query-optimizer-concepts.md) "
- " Table 7-8 "
- " [Controlling Adaptive Optimization](influencing-the-optimizer.md) "
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=REFRN10214) to learn about the `STATISTICS_LEVEL` initialization parameter
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=ARPLS68408) to learn more about `DBMS_XPLAN`

#### 7.2.2 Viewing Parallel Execution with EXPLAIN PLAN

Plans for parallel queries differ in important ways from plans for serial queries.

This section contains the following topics:

##### 7.2.2.1 About EXPLAIN PLAN and Parallel Queries

Tuning a parallel query begins much like a non-parallel query tuning exercise by choosing the driving table. However, the rules governing the choice are different.

In the serial case, the best driving table produces the fewest numbers of rows after applying limiting conditions. The database joins a small number of rows to larger tables using non-unique indexes.

For example, consider a table hierarchy consisting of `customer`, `account`, and `transaction`.

Figure 7-1 A Table Hierarchy

![Figure 7-1 A Table Hierarchy](img/pfgrf211.gif)

> This illustration shows a table hierarchy with three tables—Customer, Account, and Transaction—in order of smallest to largest.
>
> End of image description.


In this example, `customer` is the smallest table, whereas `transaction` is the largest table. A typical OLTP query retrieves transaction information about a specific customer account. The query drives from the `customer` table. The goal is to minimize logical I/O, which typically minimizes other critical resources including physical I/O and CPU time.

For parallel queries, the driving table is usually the largest table. It would not be efficient to use parallel query in this case because only a few rows from each table are accessed. However, what if it were necessary to identify all customers who had transactions of a certain type last month? It would be more efficient to drive from the `transaction` table because no limiting conditions exist on the `customer` table. The database would join rows from the `transaction` table to the `account` table, and then finally join the result set to the `customer` table. In this case, the used on the `account` and `customer` table are probably highly selective primary key or unique indexes rather than the non-unique indexes used in the first query. Because the `transaction` table is large and the column is not selective, it would be beneficial to use parallel query driving from the `transaction` table.

Parallel operations include the following:

- `PARALLEL_TO_PARALLEL `
- `PARALLEL_TO_SERIAL `
	A `PARALLEL_TO_SERIAL` operation is always the step that occurs when the query coordinator consumes rows from a parallel operation. Another type of operation that does not occur in this query is a `SERIAL` operation. If these types of operations occur, then consider making them parallel operations to improve performance because they too are potential bottlenecks.
- `PARALLEL_FROM_SERIAL `
- `PARALLEL_TO_PARALLEL `
	If the workloads in each step are relatively equivalent, then the `PARALLEL_TO_PARALLEL` operations generally produce the best performance.
- `PARALLEL_COMBINED_WITH_CHILD `
- `PARALLEL_COMBINED_WITH_PARENT `
	A `PARALLEL_COMBINED_WITH_PARENT` operation occurs when the database performs the step simultaneously with the parent step.

If a parallel step produces many rows, then the QC may not be able to consume the rows as fast as they are produced. Little can be done to improve this situation.

See Also:

The `OTHER_TAG` column in " PLAN\_TABLE Columns "

##### 7.2.2.2 Viewing Parallel Queries with EXPLAIN PLAN: Example

When using `EXPLAIN PLAN` with parallel queries, the database compiles and executes one parallel plan. This plan is derived from the serial plan by allocating row sources specific to the parallel support in the QC plan.

The table queue row sources (`PX` `Send` and `PX` `Receive`), the granule iterator, and buffer sorts, required by the two parallel execution server set PQ model, are directly inserted into the parallel plan. This plan is the same plan for all parallel execution servers when executed in parallel or for the QC when executed serially.

Example 7-3 Parallel Query Explain Plan

The following simple example illustrates an `EXPLAIN` `PLAN` for a parallel query:

```
CREATE TABLE emp2 AS SELECT * FROM employees;

ALTER TABLE emp2 PARALLEL 2;

EXPLAIN PLAN FOR
  SELECT SUM(salary) 
  FROM   emp2 
  GROUP BY department_id;

SELECT PLAN_TABLE_OUTPUT FROM TABLE(DBMS_XPLAN.DISPLAY());

-------------------------------------------------------------------------------------
|Id | Operation              | Name   |Rows| Bytes |Cost %CPU| TQ |IN-OUT|PQ Distrib|
-------------------------------------------------------------------------------------
|0| SELECT STATEMENT         |        |107| 2782 | 3 (34) |       |      |          |
|1|  PX COORDINATOR          |        |   |      |        |       |      |          |
|2|   PX SEND QC (RANDOM)    |:TQ10001|107| 2782 | 3 (34) | Q1,01 | P->S |QC (RAND) |
|3|    HASH GROUP BY         |        |107| 2782 | 3 (34) | Q1,01 | PCWP |          |
|4|     PX RECEIVE           |        |107| 2782 | 3 (34) | Q1,01 | PCWP |          |
|5|      PX SEND HASH        |:TQ10000|107| 2782 | 3 (34) | Q1,00 | P->P |HASH      |
|6|       HASH GROUP BY      |        |107| 2782 | 3 (34) | Q1,00 | PCWP |          |
|7|        PX BLOCK ITERATOR |        |107| 2782 | 2 (0)  | Q1,00 | PCWP |          |
|8|         TABLE ACCESS FULL|EMP2    |107| 2782 | 2 (0)  | Q1,00 | PCWP |          |
-------------------------------------------------------------------------------------
```

One set of parallel execution servers scans `EMP2` in parallel, while the second set performs the aggregation for the `GROUP BY` operation. The `PX BLOCK ITERATOR` row source represents the splitting up of the table `EMP2` into pieces to divide the scan workload between the parallel execution servers. The `PX SEND` and `PX RECEIVE` row sources represent the pipe that connects the two sets of parallel execution servers as rows flow up from the parallel scan, get repartitioned through the `HASH` table queue, and then read by and aggregated on the top set. The `PX SEND QC` row source represents the aggregated values being sent to the QC in random (RAND) order. The `PX COORDINATOR` row source represents the QC or Query Coordinator which controls and schedules the parallel plan appearing below it in the plan tree.

#### 7.2.3 Viewing Bitmap Indexes with EXPLAIN PLAN

Index row sources using bitmap indexes appear in the `EXPLAIN PLAN` output with the word `BITMAP` indicating the type of the index.

Note:

Queries using bitmap join index indicate the bitmap join index access path. The operation for bitmap join index is the same as bitmap index.

Example 7-4 EXPLAIN PLAN with Bitmap Indexes

In this example, the predicate `c1=2` yields a bitmap from which a subtraction can take place. From this bitmap, the bits in the bitmap for `c2=6` are subtracted. Also, the bits in the bitmap for `c2 IS NULL` are subtracted, explaining why there are two `MINUS` row sources in the plan. The `NULL` subtraction is necessary for semantic correctness unless the column has a `NOT NULL` constraint. The `TO ROWIDS` option generates the rowids necessary for the table access.

```
EXPLAIN PLAN FOR  SELECT * 
  FROM   t
  WHERE  c1 = 2 
  AND    c2 <> 6 
  OR     c3 BETWEEN 10 AND 20;

SELECT STATEMENT
   TABLE ACCESS T BY INDEX ROWID
      BITMAP CONVERSION TO ROWID
         BITMAP OR
            BITMAP MINUS
               BITMAP MINUS
                  BITMAP INDEX C1_IND SINGLE VALUE
                  BITMAP INDEX C2_IND SINGLE VALUE
               BITMAP INDEX C2_IND SINGLE VALUE
            BITMAP MERGE
               BITMAP INDEX C3_IND RANGE SCAN
```

#### 7.2.4 Viewing Result Cache with EXPLAIN PLAN

When your query contains the `result_cache` hint, the `ResultCache` operator is inserted into the execution plan.

For example, consider the following query:

```
SELECT /*+ result_cache */ deptno, avg(sal) 
FROM   emp 
GROUP BY deptno;
```

To view the `EXPLAIN PLAN` for this query, use the following command:

```
EXPLAIN PLAN FOR 
  SELECT /*+ result_cache */ deptno, avg(sal) 
  FROM emp 
  GROUP BY deptno;

SELECT PLAN_TABLE_OUTPUT FROM TABLE (DBMS_XPLAN.DISPLAY());
```

The `EXPLAIN PLAN` output for this query should look similar to the following:

```
--------------------------------------------------------------------------------
|Id| Operation          | Name                     |Rows|Bytes|Cost(%CPU)|Time |
--------------------------------------------------------------------------------
|0| SELECT STATEMENT    |                          | 11 | 77 | 4 (25)| 00:00:01|
|1|  RESULT CACHE       |b06ppfz9pxzstbttpbqyqnfbmy|    |    |       |         |
|2|   HASH GROUP BY     |                          | 11 | 77 | 4 (25)| 00:00:01|
|3|    TABLE ACCESS FULL| EMP                      |107 | 749| 3 (0) | 00:00:01|
--------------------------------------------------------------------------------
```

In this `EXPLAIN PLAN`, the `ResultCache` operator is identified by its `CacheId`, which is `b06ppfz9pxzstbttpbqyqnfbmy`. You can now run a query on the `V$RESULT_CACHE_OBJECTS` view by using this `CacheId`.

#### 7.2.5 Viewing Partitioned Objects with EXPLAIN PLAN

Use `EXPLAIN PLAN` to determine how Oracle Database accesses partitioned objects for specific queries.

Partitions accessed after pruning are shown in the `PARTITION START` and `PARTITION STOP` columns. The row source name for the range partition is `PARTITION RANGE`. For hash partitions, the row source name is `PARTITION HASH`.

A join is implemented using partial partition-wise join if the `DISTRIBUTION` column of the plan table of one of the joined tables contains `PARTITION(KEY)`. Partial partition-wise join is possible if one of the joined tables is partitioned on its join column and the table is parallelized.

A join is implemented using full partition-wise join if the partition row source appears before the join row source in the `EXPLAIN PLAN` output. Full partition-wise joins are possible only if both joined tables are equipartitioned on their respective join columns. Examples of execution plans for several types of partitioning follow.

This section contains the following topics:

##### 7.2.5.1 Displaying Range and Hash Partitioning with EXPLAIN PLAN: Examples

This example illustrates pruning by using the `emp_range` table, which partitioned by range on `hire_date`.

Assume that the tables `employees` and `departments` from the Oracle Database sample schema exist.

```
CREATE TABLE emp_range 
PARTITION BY RANGE(hire_date) 
( 
  PARTITION emp_p1 VALUES LESS THAN (TO_DATE('1-JAN-1992','DD-MON-YYYY')),
  PARTITION emp_p2 VALUES LESS THAN (TO_DATE('1-JAN-1994','DD-MON-YYYY')),
  PARTITION emp_p3 VALUES LESS THAN (TO_DATE('1-JAN-1996','DD-MON-YYYY')),
  PARTITION emp_p4 VALUES LESS THAN (TO_DATE('1-JAN-1998','DD-MON-YYYY')),
  PARTITION emp_p5 VALUES LESS THAN (TO_DATE('1-JAN-2001','DD-MON-YYYY')) 
) 
AS SELECT * FROM employees;
```

For the first example, consider the following statement:

```
EXPLAIN PLAN FOR 
  SELECT * FROM emp_range;
```

Oracle Database displays something similar to the following:

```
--------------------------------------------------------------------
|Id| Operation           | Name      |Rows| Bytes|Cost|Pstart|Pstop|
--------------------------------------------------------------------
| 0| SELECT STATEMENT    |           |  105| 13965 | 2 |   |       |
| 1|  PARTITION RANGE ALL|           |  105| 13965 | 2 | 1 |     5 |
| 2|   TABLE ACCESS FULL | EMP_RANGE |  105| 13965 | 2 | 1 |     5 |
--------------------------------------------------------------------
```

The database creates a partition row source on top of the table access row source. It iterates over the set of partitions to be accessed. In this example, the partition iterator covers all partitions (option `ALL`), because a predicate was not used for pruning. The `PARTITION_START` and `PARTITION_STOP` columns of the `PLAN_TABLE` show access to all partitions from 1 to 5.

For the next example, consider the following statement:

```
EXPLAIN PLAN FOR 
  SELECT * 
  FROM   emp_range 
  WHERE  hire_date >= TO_DATE('1-JAN-1996','DD-MON-YYYY');

-----------------------------------------------------------------------
| Id | Operation                | Name   |Rows|Bytes|Cost|Pstart|Pstop|
-----------------------------------------------------------------------
|  0 | SELECT STATEMENT         |         | 3 | 399 |   2 |     |     |
|  1 |  PARTITION RANGE ITERATOR|         | 3 | 399 |   2 |   4 |   5 |
| *2 |   TABLE ACCESS FULL      |EMP_RANGE| 3 | 399 |   2 |   4 |   5 |
-----------------------------------------------------------------------
```

In the previous example, the partition row source iterates from partition 4 to 5 because the database prunes the other partitions using a predicate on `hire_date`.

Finally, consider the following statement:

```
EXPLAIN PLAN FOR 
  SELECT *
  FROM   emp_range
  WHERE  hire_date < TO_DATE('1-JAN-1992','DD-MON-YYYY'); 

-----------------------------------------------------------------------
| Id  | Operation            | Name      |Rows|Bytes|Cost|Pstart|Pstop|
-----------------------------------------------------------------------
|   0 | SELECT STATEMENT       |           |    1 |   133 | 2 |   |   |
|   1 |  PARTITION RANGE SINGLE|           |    1 |   133 | 2 | 1 | 1 |
|*  2 |   TABLE ACCESS FULL    | EMP_RANGE |    1 |   133 | 2 | 1 | 1 |
-----------------------------------------------------------------------
```

In the previous example, only partition 1 is accessed and known at compile time; thus, there is no need for a partition row source.

Note:

Oracle Database displays the same information for hash partitioned objects, except the partition row source name is `PARTITION HASH` instead of `PARTITION RANGE`. Also, with hash partitioning, pruning is only possible using equality or `IN` -list predicates.

##### 7.2.5.2 Pruning Information with Composite Partitioned Objects: Examples

To illustrate how Oracle Database displays pruning information for composite partitioned objects, consider the table `emp_comp`. It is range-partitioned on `hiredate` and subpartitioned by hash on `deptno`.

```
CREATE TABLE emp_comp PARTITION BY RANGE(hire_date) 
      SUBPARTITION BY HASH(department_id) SUBPARTITIONS 3 
( 
PARTITION emp_p1 VALUES LESS THAN (TO_DATE('1-JAN-1992','DD-MON-YYYY')),
PARTITION emp_p2 VALUES LESS THAN (TO_DATE('1-JAN-1994','DD-MON-YYYY')),
PARTITION emp_p3 VALUES LESS THAN (TO_DATE('1-JAN-1996','DD-MON-YYYY')),
PARTITION emp_p4 VALUES LESS THAN (TO_DATE('1-JAN-1998','DD-MON-YYYY')),
PARTITION emp_p5 VALUES LESS THAN (TO_DATE('1-JAN-2001','DD-MON-YYYY')) 
) 
AS SELECT * FROM employees;
```

For the first example, consider the following statement:

```
EXPLAIN PLAN FOR 
  SELECT * FROM emp_comp; 

-----------------------------------------------------------------------
|Id| Operation           | Name     | Rows  | Bytes |Cost|Pstart|Pstop|
-----------------------------------------------------------------------
| 0| SELECT STATEMENT    |          | 10120 |  1314K| 78 |    |       |
| 1|  PARTITION RANGE ALL|          | 10120 |  1314K| 78 |  1 |     5 |
| 2|   PARTITION HASH ALL|          | 10120 |  1314K| 78 |  1 |     3 |
| 3|    TABLE ACCESS FULL| EMP_COMP | 10120 |  1314K| 78 |  1 |    15 |
-----------------------------------------------------------------------
```

This example shows the plan when Oracle Database accesses all subpartitions of all partitions of a composite object. The database uses two partition row sources for this purpose: a range partition row source to iterate over the partitions, and a hash partition row source to iterate over the subpartitions of each accessed partition.

In the following example, the range partition row source iterates from partition 1 to 5, because the database performs no pruning. Within each partition, the hash partition row source iterates over subpartitions 1 to 3 of the current partition. As a result, the table access row source accesses subpartitions 1 to 15. In other words, the database accesses all subpartitions of the composite object.

```
EXPLAIN PLAN FOR 
  SELECT * 
  FROM   emp_comp 
  WHERE  hire_date = TO_DATE('15-FEB-1998', 'DD-MON-YYYY'); 

-----------------------------------------------------------------------
| Id | Operation              | Name    |Rows|Bytes |Cost|Pstart|Pstop|
-----------------------------------------------------------------------
|  0 | SELECT STATEMENT       |          | 20 | 2660 | 17 |     |     |
|  1 |  PARTITION RANGE SINGLE|          | 20 | 2660 | 17 |   5 |   5 |
|  2 |   PARTITION HASH ALL   |          | 20 | 2660 | 17 |   1 |   3 |
|* 3 |    TABLE ACCESS FULL   | EMP_COMP | 20 | 2660 | 17 |  13 |  15 |
-----------------------------------------------------------------------
```

In the previous example, only the last partition, partition 5, is accessed. This partition is known at compile time, so the database does not need to show it in the plan. The hash partition row source shows accessing of all subpartitions within that partition; that is, subpartitions 1 to 3, which translates into subpartitions 13 to 15 of the `emp_comp` table.

Now consider the following statement:

```
EXPLAIN PLAN FOR 
  SELECT * 
  FROM   emp_comp 
  WHERE  department_id = 20; 

------------------------------------------------------------------------
| Id | Operation              |Name    |Rows | Bytes |Cost|Pstart|Pstop|
------------------------------------------------------------------------
|  0 | SELECT STATEMENT       |          | 101 | 13433 | 78 |    |     |
|  1 |  PARTITION RANGE ALL   |          | 101 | 13433 | 78 |  1 |   5 |
|  2 |   PARTITION HASH SINGLE|          | 101 | 13433 | 78 |  3 |   3 |
|* 3 |    TABLE ACCESS FULL   | EMP_COMP | 101 | 13433 | 78 |    |     |
------------------------------------------------------------------------
```

In the previous example, the predicate `deptno=20` enables pruning on the hash dimension within each partition. Therefore, Oracle Database only needs to access a single subpartition. The number of this subpartition is known at compile time, so the hash partition row source is not needed.

Finally, consider the following statement:

```
VARIABLE dno NUMBER; 
EXPLAIN PLAN FOR 
  SELECT * 
  FROM   emp_comp 
  WHERE  department_id = :dno; 

-----------------------------------------------------------------------
| Id| Operation              | Name    |Rows| Bytes |Cost|Pstart|Pstop|
-----------------------------------------------------------------------
| 0 | SELECT STATEMENT       |          | 101| 13433 | 78 |     |     |
| 1 |  PARTITION RANGE ALL   |          | 101| 13433 | 78 |   1 |   5 |
| 2 |   PARTITION HASH SINGLE|          | 101| 13433 | 78 | KEY | KEY |
|*3 |    TABLE ACCESS FULL   | EMP_COMP | 101| 13433 | 78 |     |     |
-----------------------------------------------------------------------
```

The last two examples are the same, except that `department_id` =:`dno` replaces `deptno=20`. In this last case, the subpartition number is unknown at compile time, and a hash partition row source is allocated. The option is `SINGLE` for this row source because Oracle Database accesses only one subpartition within each partition. In Step 2, both `PARTITION` \_ `START` and `PARTITION` \_ `STOP` are set to `KEY`. This value means that Oracle Database determines the number of subpartitions at run time.

##### 7.2.5.3 Examples of Partial Partition-Wise Joins

In these examples, the `PQ_DISTRIBUTE` hint explicitly forces a partial partition-wise join because the query optimizer could have chosen a different plan based on cost in this query.

Example 7-5 Partial Partition-Wise Join with Range Partition

In the following example, the database joins `emp_range_did` on the partitioning column `department_id` and parallelizes it. The database can use a partial partition-wise join because the `dept2` table is not partitioned. Oracle Database dynamically partitions the `dept2` table before the join.

```
CREATE TABLE dept2 AS SELECT * FROM departments;
ALTER TABLE dept2 PARALLEL 2;

CREATE TABLE emp_range_did PARTITION BY RANGE(department_id)
   (PARTITION emp_p1 VALUES LESS THAN (150),
    PARTITION emp_p5 VALUES LESS THAN (MAXVALUE) )
  AS SELECT * FROM employees;

ALTER TABLE emp_range_did PARALLEL 2;

EXPLAIN PLAN FOR 
  SELECT /*+ PQ_DISTRIBUTE(d NONE PARTITION) ORDERED */ e.last_name, 
         d.department_name 
  FROM   emp_range_did e, dept2 d 
  WHERE  e.department_id = d.department_id;

-------------------------------------------------------------------------------------------
|Id| Operation                    |Name   |Row|Byte|Cost|Pstart|Pstop|TQ|IN-OUT|PQ Distrib|
-------------------------------------------------------------------------------------------
| 0| SELECT STATEMENT             |             |284 |16188|6|  | |       |    |          |
| 1|  PX COORDINATOR              |             |    |     | |  | |       |    |          |
| 2|   PX SEND QC (RANDOM)        |:TQ10001     |284 |16188|6|  | | Q1,01 |P->S|QC (RAND) |
|*3|    HASH JOIN                 |             |284 |16188|6|  | | Q1,01 |PCWP|          |
| 4|     PX PARTITION RANGE ALL   |             |284 |7668 |2|1 |2| Q1,01 |PCWC|          |
| 5|      TABLE ACCESS FULL       |EMP_RANGE_DID|284 |7668 |2|1 |2| Q1,01 |PCWP|          |
| 6|     BUFFER SORT              |             |    |     | |  | | Q1,01 |PCWC|          |
| 7|      PX RECEIVE              |             | 21 | 630 |2|  | | Q1,01 |PCWP|          |
| 8|       PX SEND PARTITION (KEY)|:TQ10000     | 21 | 630 |2|  | |       |S->P|PART (KEY)|
| 9|        TABLE ACCESS FULL     |DEPT2        | 21 | 630 |2|  | |       |    |          |
-------------------------------------------------------------------------------------------
```

The execution plan shows that the table `dept2` is scanned serially and all rows with the same partitioning column value of `emp_range_did (department_id)` are sent through a `PART (KEY)`, or partition key, table queue to the same parallel execution server doing the partial partition-wise join.

Example 7-6 Partial Partition-Wise Join with Composite Partition

In the following example, `emp_comp` is joined on the partitioning column and is parallelized, enabling use of a partial partition-wise join because `dept2` is not partitioned. The database dynamically partitions `dept2` before the join.

```
ALTER TABLE emp_comp PARALLEL 2; 

EXPLAIN PLAN FOR 
  SELECT /*+ PQ_DISTRIBUTE(d NONE PARTITION) ORDERED */ e.last_name, 
         d.department_name 
  FROM   emp_comp e, dept2 d 
  WHERE  e.department_id = d.department_id;

SELECT PLAN_TABLE_OUTPUT FROM TABLE(DBMS_XPLAN.DISPLAY());

-------------------------------------------------------------------------------------------
| Id| Operation              | Name  |Rows |Bytes |Cost|Pstart|Pstop|TQ |IN-OUT|PQ Distrib|
-------------------------------------------------------------------------------------------
| 0 | SELECT STATEMENT            |        | 445 |17800| 5 |  |   |       |    |          |
| 1 |  PX COORDINATOR             |        |     |     |   |  |   |       |    |          |
| 2 |   PX SEND QC (RANDOM)       |:TQ10001| 445 |17800| 5 |  |   | Q1,01 |P->S| QC (RAND)|
|*3 |    HASH JOIN                |        | 445 |17800| 5 |  |   | Q1,01 |PCWP|          |
| 4 |     PX PARTITION RANGE ALL  |        | 107 | 1070| 3 |1 | 5 | Q1,01 |PCWC|          |
| 5 |      PX PARTITION HASH ALL  |        | 107 | 1070| 3 |1 | 3 | Q1,01 |PCWC|          |
| 6 |       TABLE ACCESS FULL     |EMP_COMP| 107 | 1070| 3 |1 | 15| Q1,01 |PCWP|          |
| 7 |     PX RECEIVE              |        |  21 |  630| 1 |  |   | Q1,01 |PCWP|          |
| 8 |      PX SEND PARTITION (KEY)|:TQ10000|  21 |  630| 1 |  |   | Q1,00 |P->P|PART (KEY)|
| 9 |       PX BLOCK ITERATOR     |        |  21 |  630| 1 |  |   | Q1,00 |PCWC|          |
|10 |        TABLE ACCESS FULL    |DEPT2   |  21 |  630| 1 |  |   | Q1,00 |PCWP|          |
-------------------------------------------------------------------------------------------
```

The plan shows that the optimizer selects partial partition-wise join from one of two columns. The `PX SEND` node type is `PARTITION (KEY)` and the `PQ Distrib` column contains the text `PART (KEY)`, or partition key. This implies that the table `dept2` is re-partitioned based on the join column `department_id` to be sent to the parallel execution servers executing the scan of `EMP_COMP` and the join.

##### 7.2.5.4 Example of Full Partition-Wise Join

In this example, `emp_comp` and `dept_hash` are joined on their hash partitioning columns, enabling use of a full partition-wise join.

The `PARTITION HASH` row source appears on top of the join row source in the plan table output.

```
CREATE TABLE dept_hash
   PARTITION BY HASH(department_id)
   PARTITIONS 3
   PARALLEL 2
   AS SELECT * FROM departments;

EXPLAIN PLAN FOR 
  SELECT /*+ PQ_DISTRIBUTE(e NONE NONE) ORDERED */ e.last_name,
         d.department_name
  FROM   emp_comp e, dept_hash d
  WHERE  e.department_id = d.department_id;

-------------------------------------------------------------------------------------------
|Id| Operation                  | Name |Rows|Bytes|Cost|Pstart|Pstop|TQ |IN-OUT|PQ Distrib|
-------------------------------------------------------------------------------------------
| 0| SELECT STATEMENT           |          | 106 | 2544 |8|  |   |       |      |         |
| 1|  PX COORDINATOR            |          |     |      | |  |   |       |      |         |
| 2|   PX SEND QC (RANDOM)      |:TQ10000  | 106 | 2544 |8|  |   | Q1,00 | P->S |QC (RAND)|
| 3|    PX PARTITION HASH ALL   |          | 106 | 2544 |8|1 | 3 | Q1,00 | PCWC |         |
|*4|     HASH JOIN              |          | 106 | 2544 |8|  |   | Q1,00 | PCWP |         |
| 5|      PX PARTITION RANGE ALL|          | 107 | 1070 |3|1 | 5 | Q1,00 | PCWC |         |
| 6|       TABLE ACCESS FULL    |EMP_COMP  | 107 | 1070 |3|1 |15 | Q1,00 | PCWP |         |
| 7|      TABLE ACCESS FULL     |DEPT_HASH |  27 |  378 |4|1 | 3 | Q1,00 | PCWP |         |
-------------------------------------------------------------------------------------------
```

The `PX PARTITION HASH` row source appears on top of the join row source in the plan table output while the `PX PARTITION RANGE` row source appears over the scan of `emp_comp`. Each parallel execution server performs the join of an entire hash partition of `emp_comp` with an entire partition of `dept_hash`.

##### 7.2.5.5 Examples of INLIST ITERATOR and EXPLAIN PLAN

An `INLIST ITERATOR` operation appears in the `EXPLAIN PLAN` output if an index implements an `IN` -list predicate.

Consider the following statement:

```
SELECT * FROM emp WHERE empno IN (7876, 7900, 7902);
```

The `EXPLAIN PLAN` output appears as follows:

```
OPERATION          OPTIONS           OBJECT_NAME
----------------   ---------------   -------------- 
SELECT STATEMENT
INLIST ITERATOR
TABLE ACCESS       BY ROWID          EMP
INDEX              RANGE SCAN        EMP_EMPNO
```

The `INLIST ITERATOR` operation iterates over the next operation in the plan for each value in the `IN` -list predicate. The following sections describe the three possible types of `IN` -list columns for partitioned tables and indexes.

This section contains the following topics:

###### 7.2.5.5.1 When the IN-List Column is an Index Column: Example

If the `IN` -list column `empno` is an index column but not a partition column, then the `IN` -list operator appears before the table operation but after the partition operation in the plan.

```
OPERATION        OPTIONS              OBJECT_NAME PARTIT_START PARTITI_STOP
---------------- ------------         ----------- ------------ ------------ 
SELECT STATEMENT 
PARTITION RANGE  ALL                             KEY(INLIST)    KEY(INLIST)
INLIST ITERATOR
TABLE ACCESS     BY LOCAL INDEX ROWID EMP          KEY(INLIST)  KEY(INLIST)
INDEX            RANGE SCAN           EMP_EMPNO    KEY(INLIST)  KEY(INLIST)
```

The `KEY(INLIST)` designation for the partition start and stop keys specifies that an `IN` -list predicate appears on the index start and stop keys.

###### 7.2.5.5.2 When the IN-List Column is an Index and a Partition Column: Example

If `empno` is an indexed and a partition column, then the plan contains an `INLIST ITERATOR` operation before the partition operation.

```
OPERATION        OPTIONS              OBJECT_NAME PARTITION_START PARTITION_STOP
---------------- ------------         ----------- --------------- --------------
SELECT STATEMENT
INLIST ITERATOR
PARTITION RANGE  ITERATOR                         KEY(INLIST)     KEY(INLIST)
TABLE ACCESS     BY LOCAL INDEX ROWID EMP         KEY(INLIST)     KEY(INLIST)
INDEX            RANGE SCAN           EMP_EMPNO   KEY(INLIST)     KEY(INLIST)
```

###### 7.2.5.5.3 When the IN-List Column is a Partition Column: Example

If `empno` is a partition column and no indexes exist, then no `INLIST ITERATOR` operation is allocated.

```
OPERATION         OPTIONS        OBJECT_NAME   PARTITION_START   PARTITION_STOP
----------------  ------------   -----------   ---------------   --------------
SELECT STATEMENT
PARTITION RANGE   INLIST                       KEY(INLIST)       KEY(INLIST)
TABLE ACCESS      FULL           EMP           KEY(INLIST)       KEY(INLIST)
```

If `emp_empno` is a bitmap index, then the plan is as follows:

```
OPERATION          OPTIONS           OBJECT_NAME
----------------   ---------------   -------------- 
SELECT STATEMENT
INLIST ITERATOR
TABLE ACCESS       BY INDEX ROWID    EMP
BITMAP CONVERSION  TO ROWIDS
BITMAP INDEX       SINGLE VALUE      EMP_EMPNO
```

##### 7.2.5.6 Example of Domain Indexes and EXPLAIN PLAN

You can use `EXPLAIN PLAN` to derive user-defined CPU and I/O costs for domain indexes.

`EXPLAIN PLAN` displays domain index statistics in the `OTHER` column of `PLAN_TABLE`. For example, assume table `emp` has user-defined operator `CONTAINS` with a domain index `emp_resume` on the `resume` column, and the index type of `emp_resume` supports the operator `CONTAINS`. You explain the plan for the following query:

```
SELECT * FROM emp WHERE CONTAINS(resume, 'Oracle') = 1
```

The database could display the following plan:

```
OPERATION            OPTIONS      OBJECT_NAME     OTHER 
-----------------    -----------  ------------    ----------------
SELECT STATEMENT 
TABLE ACCESS         BY ROWID     EMP
DOMAIN INDEX                      EMP_RESUME      CPU: 300, I/O: 4
```

#### 7.2.6 PLAN\_TABLE Columns

The `PLAN_TABLE` used by the `EXPLAIN PLAN` statement contains the columns listed in this topic.

Table 7-1 PLAN\_TABLE Columns

| Column | Type | Description |
| --- | --- | --- |
| `STATEMENT_ID ` | `VARCHAR2(30) ` | Value of the optional `STATEMENT_ID` parameter specified in the `EXPLAIN PLAN` statement. |
| `PLAN_ID` | `NUMBER` | Unique identifier of a plan in the database. |
| `TIMESTAMP ` | `DATE ` | Date and time when the `EXPLAIN PLAN` statement was generated. |
| `REMARKS ` | `VARCHAR2(80) ` | Any comment (of up to 80 bytes) you want to associate with each step of the explained plan. This column indicates whether the database used an outline or SQL profile for the query.  If you need to add or change a remark on any row of the `PLAN_TABLE`, then use the `UPDATE` statement to modify the rows of the `PLAN_TABLE`. |
| `OPERATION ` | `VARCHAR2(30) ` | Name of the internal operation performed in this step. In the first row generated for a statement, the column contains one of the following values:  - `DELETE STATEMENT` - `INSERT STATEMENT` - `SELECT STATEMENT` - `UPDATE STATEMENT`  See Table 7-3 for more information about values for this column. |
| `OPTIONS ` | `VARCHAR2(225) ` | A variation on the operation described in the `OPERATION` column.  See Table 7-3 for more information about values for this column. |
| `OBJECT_NODE ` | `VARCHAR2(128) ` | Name of the database link used to reference the object (a table name or view name). For local queries using parallel execution, this column describes the order in which the database consumes output from operations. |
| `OBJECT_OWNER ` | `VARCHAR2(30) ` | Name of the user who owns the schema containing the table or index. |
| `OBJECT_NAME ` | `VARCHAR2(30) ` | Name of the table or index. |
| `OBJECT_ALIAS` | `VARCHAR2(65) ` | Unique alias of a table or view in a SQL statement. For indexes, it is the object alias of the underlying table. |
| `OBJECT_INSTANCE ` | `NUMERIC ` | Number corresponding to the ordinal position of the object as it appears in the original statement. The numbering proceeds from left to right, outer to inner for the original statement text. View expansion results in unpredictable numbers. |
| `OBJECT_TYPE ` | `VARCHAR2(30) ` | Modifier that provides descriptive information about the object; for example, `NON` - `UNIQUE` for indexes. |
| `OPTIMIZER ` | `VARCHAR2(255) ` | Current mode of the optimizer. |
| `SEARCH_COLUMNS ` | `NUMBERIC ` | Not currently used. |
| `ID ` | `NUMERIC ` | A number assigned to each step in the execution plan. |
| `PARENT_ID ` | `NUMERIC ` | The ID of the next execution step that operates on the output of the `ID` step. |
| `DEPTH` | `NUMERIC` | Depth of the operation in the row source tree that the plan represents. You can use the value to indent the rows in a plan table report. |
| `POSITION ` | `NUMERIC ` | For the first row of output, this indicates the optimizer's estimated cost of executing the statement. For the other rows, it indicates the position relative to the other children of the same parent. |
| `COST ` | `NUMERIC ` | Cost of the operation as estimated by the optimizer's query approach. Cost is not determined for table access operations. The value of this column does not have any particular unit of measurement; it is a weighted value used to compare costs of execution plans. The value of this column is a function of the `CPU_COST` and `IO_COST` columns. |
| `CARDINALITY ` | `NUMERIC ` | Estimate by the query optimization approach of the number of rows that the operation accessed. |
| `BYTES ` | `NUMERIC ` | Estimate by the query optimization approach of the number of bytes that the operation accessed. |
| `OTHER_TAG ` | `VARCHAR2(255) ` | Describes the contents of the `OTHER` column. Values are:  - `SERIAL` (blank): Serial execution. Currently, SQL is not loaded in the `OTHER` column for this case. - `SERIAL_FROM_REMOTE (S -> R)`: Serial execution at a remote site. - `PARALLEL_FROM_SERIAL (S -> P)`: Serial execution. Output of step is partitioned or broadcast to parallel execution servers. - `PARALLEL_TO_SERIAL (P -> S)`: Parallel execution. Output of step is returned to serial QC process. - `PARALLEL_TO_PARALLEL (P -> P)`: Parallel execution. Output of step is repartitioned to second set of parallel execution servers. - `PARALLEL_COMBINED_WITH_PARENT (PWP)`: Parallel execution; Output of step goes to next step in same parallel process. No interprocess communication to parent. - `PARALLEL_COMBINED_WITH_CHILD (PWC)`: Parallel execution. Input of step comes from prior step in same parallel process. No interprocess communication from child. |
| `PARTITION_START ` | `VARCHAR2(255) ` | Start partition of a range of accessed partitions. It can take one of the following values:  n indicates that the start partition has been identified by the SQL compiler, and its partition number is given by n.  `KEY` indicates that the start partition is identified at run time from partitioning key values.  `ROW REMOVE_LOCATION` indicates that the database computes the start partition (same as the stop partition) at run time from the location of each retrieved record. The record location is obtained by a user or from a global index.  `INVALID` indicates that the range of accessed partitions is empty. |
| `PARTITION_STOP ` | `VARCHAR2(255) ` | Stop partition of a range of accessed partitions. It can take one of the following values:  n indicates that the stop partition has been identified by the SQL compiler, and its partition number is given by n.  `KEY` indicates that the stop partition is identified at run time from partitioning key values.  `ROW REMOVE_LOCATION` indicates that the database computes the stop partition (same as the start partition) at run time from the location of each retrieved record. The record location is obtained by a user or from a global index.  `INVALID` indicates that the range of accessed partitions is empty. |
| `PARTITION_ID ` | `NUMERIC ` | Step that has computed the pair of values of the `PARTITION_START` and `PARTITION_STOP` columns. |
| `OTHER ` | `LONG ` | Other information that is specific to the execution step that a user might find useful. See the `OTHER_TAG` column. |
| `DISTRIBUTION ` | `VARCHAR2(30) ` | Method used to distribute rows from producer query servers to consumer query servers.  See Table 7-2 for more information about the possible values for this column. For more information about consumer and producer query servers, see [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=GUID-1C6BC851-DE4A-4651-9813-3E70023C8264). |
| `CPU_COST ` | `NUMERIC ` | CPU cost of the operation as estimated by the query optimizer's approach. The value of this column is proportional to the number of machine cycles required for the operation. For statements that use the rule-based approach, this column is null. |
| `IO_COST ` | `NUMERIC ` | I/O cost of the operation as estimated by the query optimizer's approach. The value of this column is proportional to the number of data blocks read by the operation. For statements that use the rule-based approach, this column is null. |
| `TEMP_SPACE` | `NUMERIC ` | Temporary space, in bytes, that the operation uses as estimated by the query optimizer's approach. For statements that use the rule-based approach, or for operations that do not use any temporary space, this column is null. |
| `ACCESS_PREDICATES` | `VARCHAR2(4000)` | Predicates used to locate rows in an access structure. For example, start or stop predicates for an index range scan. |
| `FILTER_PREDICATES` | `VARCHAR2(4000)` | Predicates used to filter rows before producing them. |
| `PROJECTION` | `VARCHAR2(4000)` | Expressions produced by the operation. |
| `TIME` | `NUMBER(20,2)` | Elapsed time in seconds of the operation as estimated by query optimization. For statements that use the rule-based approach, this column is null. The `DBMS_XPLAN.DISPLAY_PLAN` out, the time is in the `HH:MM:SS` format. |
| `QBLOCK_NAME` | `VARCHAR2(30)` | Name of the query block, either system-generated or defined by the user with the `QB_NAME` hint. |

Table 7-2 describes the values that can appear in the `DISTRIBUTION` column:

Table 7-2 Values of DISTRIBUTION Column of the PLAN\_TABLE

| DISTRIBUTION Text | Interpretation |
| --- | --- |
| `PARTITION (ROWID) ` | Maps rows to query servers based on the partitioning of a table or index using the rowid of the row to `UPDATE` or `DELETE`. |
| `PARTITION (KEY) ` | Maps rows to query servers based on the partitioning of a table or index using a set of columns. Used for partial partition-wise join, `PARALLEL INSERT`, `CREATE TABLE AS SELECT` of a partitioned table, and `CREATE PARTITIONED GLOBAL INDEX`. |
| `HASH ` | Maps rows to query servers using a hash function on the join key. Used for `PARALLEL JOIN` or `PARALLEL GROUP BY`. |
| `RANGE ` | Maps rows to query servers using ranges of the sort key. Used when the statement contains an `ORDER BY` clause. |
| `ROUND-ROBIN ` | Randomly maps rows to query servers. |
| `BROADCAST` | Broadcasts the rows of the entire table to each query server. Used for a parallel join when one table is very small compared to the other. |
| `QC (ORDER)` | The QC consumes the input in order, from the first to the last query server. Used when the statement contains an `ORDER BY` clause. |
| `QC (RANDOM)` | The QC consumes the input randomly. Used when the statement does not have an `ORDER` `BY` clause. |

Table 7-3 lists each combination of `OPERATION` and `OPTIONS` produced by the `EXPLAIN PLAN` statement and its meaning within an execution plan.

Table 7-3 OPERATION and OPTIONS Values Produced by EXPLAIN PLAN

| Operation | Option | Description |
| --- | --- | --- |
| `AND-EQUAL` |  | Operation accepting multiple sets of rowids, returning the intersection of the sets, eliminating duplicates. Used for the single-column indexes access path. |
| `BITMAP` | `CONVERSION ` | `TO ROWIDS` converts bitmap representations to actual rowids that you can use to access the table.  `FROM ROWIDS` converts the rowids to a bitmap representation.  `COUNT` returns the number of rowids if the actual values are not needed. |
| `BITMAP ` | `INDEX ` | `SINGLE VALUE` looks up the bitmap for a single key value in the index.  `RANGE SCAN` retrieves bitmaps for a key value range.  `FULL SCAN` performs a full scan of a bitmap index if there is no start or stop key. |
| `BITMAP ` | `MERGE ` | Merges several bitmaps resulting from a range scan into one bitmap. |
| `BITMAP ` | `MINUS ` | Subtracts bits of one bitmap from another. Row source is used for negated predicates. Use this option only if there are nonnegated predicates yielding a bitmap from which the subtraction can take place. An example appears in " Viewing Bitmap Indexes with EXPLAIN PLAN ". |
| `BITMAP ` | `OR ` | Computes the bitwise `OR` of two bitmaps. |
| `BITMAP ` | `AND ` | Computes the bitwise `AND` of two bitmaps. |
| `BITMAP ` | `KEY ITERATION ` | Takes each row from a table row source and finds the corresponding bitmap from a bitmap index. This set of bitmaps are then merged into one bitmap in a following `BITMAP MERGE` operation. |
| `CONNECT BY ` |  | Retrieves rows in hierarchical order for a query containing a `CONNECT BY` clause. |
| `CONCATENATION ` |  | Operation accepting multiple sets of rows returning the union-all of the sets. |
| `COUNT` |  | Operation counting the number of rows selected from a table. |
| `COUNT` | `STOPKEY` | Count operation where the number of rows returned is limited by the `ROWNUM` expression in the `WHERE` clause. |
| `CUBE SCAN` |  | Uses inner joins for all cube access. |
| `CUBE SCAN` | `PARTIAL OUTER` | Uses an outer join for at least one dimension, and inner joins for the other dimensions. |
| `CUBE SCAN` | `OUTER` | Uses outer joins for all cube access. |
| `DOMAIN INDEX ` |  | Retrieval of one or more rowids from a domain index. The options column contain information supplied by a user-defined domain index cost function, if any. |
| `FILTER ` |  | Operation accepting a set of rows, eliminates some of them, and returns the rest. |
| `FIRST ROW ` |  | Retrieval of only the first row selected by a query. |
| `FOR UPDATE ` |  | Operation retrieving and locking the rows selected by a query containing a `FOR UPDATE` clause. |
| `HASH` | `GROUP BY` | Operation hashing a set of rows into groups for a query with a `GROUP BY` clause. |
| `HASH` | `GROUP BY PIVOT` | Operation hashing a set of rows into groups for a query with a `GROUP BY` clause. The `PIVOT` option indicates a pivot-specific optimization for the `HASH GROUP BY` operator. |
| `HASH JOIN `  (These are join operations.) |  | Operation joining two sets of rows and returning the result. This join method is useful for joining large data sets of data (DSS, Batch). The join condition is an efficient way of accessing the second table.  Query optimizer uses the smaller of the two tables/data sources to build a hash table on the join key in memory. Then it scans the larger table, probing the hash table to find the joined rows. |
| `HASH JOIN ` | `ANTI ` | Hash (left) antijoin |
| `HASH JOIN ` | `SEMI ` | Hash (left) semijoin |
| `HASH JOIN ` | `RIGHT ANTI ` | Hash right antijoin |
| `HASH JOIN ` | `RIGHT SEMI ` | Hash right semijoin |
| `HASH JOIN ` | `OUTER ` | Hash (left) outer join |
| `HASH JOIN ` | `RIGHT OUTER ` | Hash right outer join |
| `INDEX `  (These are access methods.) | `UNIQUE SCAN ` | Retrieval of a single rowid from an index. |
| `INDEX` | `RANGE SCAN ` | Retrieval of one or more rowids from an index. Indexed values are scanned in ascending order. |
| `INDEX` | `RANGE SCAN DESCENDING ` | Retrieval of one or more rowids from an index. Indexed values are scanned in descending order. |
| `INDEX` | `FULL SCAN ` | Retrieval of all rowids from an index when there is no start or stop key. Indexed values are scanned in ascending order. |
| `INDEX` | `FULL SCAN DESCENDING ` | Retrieval of all rowids from an index when there is no start or stop key. Indexed values are scanned in descending order. |
| `INDEX ` | `FAST FULL SCAN ` | Retrieval of all rowids (and column values) using multiblock reads. No sorting order can be defined. Compares to a full table scan on only the indexed columns. Only available with the cost based optimizer. |
| `INDEX ` | `SKIP SCAN ` | Retrieval of rowids from a concatenated index without using the leading column(s) in the index. Only available with the cost based optimizer. |
| `INLIST ITERATOR ` |  | Iterates over the next operation in the plan for each value in the `IN` -list predicate. |
| `INTERSECTION ` |  | Operation accepting two sets of rows and returning the intersection of the sets, eliminating duplicates. |
| `MERGE JOIN `  (These are join operations.) |  | Operation accepting two sets of rows, each sorted by a value, combining each row from one set with the matching rows from the other, and returning the result. |
| `MERGE JOIN ` | `OUTER ` | Merge join operation to perform an outer join statement. |
| `MERGE JOIN ` | `ANTI ` | Merge antijoin. |
| `MERGE JOIN ` | `SEMI ` | Merge semijoin. |
| `MERGE JOIN ` | `CARTESIAN ` | Can result from 1 or more of the tables not having any join conditions to any other tables in the statement. Can occur even with a join and it may not be flagged as `CARTESIAN` in the plan. |
| `CONNECT BY ` |  | Retrieval of rows in hierarchical order for a query containing a `CONNECT BY` clause. |
| `MAT_VIEW REWITE ACCESS `  (These are access methods.) | `FULL` | Retrieval of all rows from a materialized view. |
| `MAT_VIEW REWITE ACCESS ` | `SAMPLE ` | Retrieval of sampled rows from a materialized view. |
| `MAT_VIEW REWITE ACCESS ` | `CLUSTER ` | Retrieval of rows from a materialized view based on a value of an indexed cluster key. |
| `MAT_VIEW REWITE ACCESS ` | `HASH ` | Retrieval of rows from materialized view based on hash cluster key value. |
| `MAT_VIEW REWITE ACCESS ` | `BY ROWID RANGE ` | Retrieval of rows from a materialized view based on a rowid range. |
| `MAT_VIEW REWITE ACCESS ` | `SAMPLE BY ROWID RANGE ` | Retrieval of sampled rows from a materialized view based on a rowid range. |
| `MAT_VIEW REWITE ACCESS` | `BY USER ROWID ` | If the materialized view rows are located using user-supplied rowids. |
| `MAT_VIEW REWITE ACCESS ` | `BY INDEX ROWID ` | If the materialized view is nonpartitioned and rows are located using index(es). |
| `MAT_VIEW REWITE ACCESS ` | `BY GLOBAL INDEX ROWID ` | If the materialized view is partitioned and rows are located using only global indexes. |
| `MAT_VIEW REWITE ACCESS ` | `BY LOCAL INDEX ROWID ` | If the materialized view is partitioned and rows are located using one or more local indexes and possibly some global indexes.  Partition Boundaries:  The partition boundaries might have been computed by:  A previous `PARTITION` step, in which case the `PARTITION_START` and `PARTITION_STOP` column values replicate the values present in the `PARTITION` step, and the `PARTITION_ID` contains the ID of the `PARTITION` step. Possible values for `PARTITION_START` and `PARTITION_STOP` are `NUMBER` (n), `KEY`, `INVALID`.  The `MAT_VIEW REWRITE ACCESS` or `INDEX` step itself, in which case the `PARTITION_ID` contains the `ID` of the step. Possible values for `PARTITION_START` and `PARTITION_STOP` are `NUMBER` (n), `KEY`, `ROW` `REMOVE_LOCATION` (`MAT_VIEW REWRITE` `ACCESS` only), and `INVALID`. |
| `MINUS` |  | Operation accepting two sets of rows and returning rows appearing in the first set but not in the second, eliminating duplicates. |
| `NESTED LOOPS`  (These are join operations.) |  | Operation accepting two sets of rows, an outer set and an inner set. Oracle Database compares each row of the outer set with each row of the inner set, returning rows that satisfy a condition. This join method is useful for joining small subsets of data (OLTP). The join condition is an efficient way of accessing the second table. |
| `NESTED LOOPS ` | `OUTER` | Nested loops operation to perform an outer join statement. |
| `PARTITION` |  | Iterates over the next operation in the plan for each partition in the range given by the `PARTITION_START` and `PARTITION_STOP` columns. `PARTITION` describes partition boundaries applicable to a single partitioned object (table or index) or to a set of equipartitioned objects (a partitioned table and its local indexes). The partition boundaries are provided by the values of `PARTITION_START` and `PARTITION_STOP` of the `PARTITION`. Refer to Table 7-1 for valid values of partition start and stop. |
| `PARTITION` | `SINGLE` | Access one partition. |
| `PARTITION` | `ITERATOR` | Access many partitions (a subset). |
| `PARTITION` | `ALL` | Access all partitions. |
| `PARTITION` | `INLIST` | Similar to iterator, but based on an `IN` -list predicate. |
| `PARTITION` | `INVALID` | Indicates that the partition set to be accessed is empty. |
| `PX` `ITERATOR` | `BLOCK`, `CHUNK` | Implements the division of an object into block or chunk ranges among a set of parallel execution servers. |
| `PX` `COORDINATOR` |  | Implements the query coordinator that controls, schedules, and executes the parallel plan below it using parallel execution servers. It also represents a serialization point, as the end of the part of the plan executed in parallel and always has a `PX SEND QC` operation below it. |
| `PX` `PARTITION` |  | Same semantics as the regular `PARTITION` operation except that it appears in a parallel plan. |
| `PX` `RECEIVE` |  | Shows the consumer/receiver parallel execution node reading repartitioned data from a send/producer (QC or parallel execution server) executing on a `PX SEND` node. This information was formerly displayed into the `DISTRIBUTION` column. See Table 7-2. |
| `PX` `SEND` | `QC` `(RANDOM), HASH`, `RANGE` | Implements the distribution method taking place between two parallel execution servers. Shows the boundary between two sets and how data is repartitioned on the send/producer side. This information was formerly displayed into the `DISTRIBUTION` column. See Table 7-2. |
| `REMOTE` |  | Retrieval of data from a remote database. |
| `SEQUENCE` |  | Operation involving accessing values of a sequence. |
| `SORT` | `AGGREGATE` | Retrieval of a single row that is the result of applying a group function to a group of selected rows. |
| `SORT` | `UNIQUE` | Operation sorting a set of rows to eliminate duplicates. |
| `SORT` | `GROUP` `BY` | Operation sorting a set of rows into groups for a query with a `GROUP BY` clause. |
| `SORT` | `GROUP BY PIVOT` | Operation sorting a set of rows into groups for a query with a `GROUP` `BY` clause. The `PIVOT` option indicates a pivot-specific optimization for the `SORT GROUP BY` operator. |
| `SORT ` | `JOIN ` | Operation sorting a set of rows before a merge-join. |
| `SORT ` | `ORDER BY ` | Operation sorting a set of rows for a query with an `ORDER BY` clause. |
| `TABLE ACCESS `  (These are access methods.) | `FULL ` | Retrieval of all rows from a table. |
| `TABLE ACCESS ` | `SAMPLE ` | Retrieval of sampled rows from a table. |
| `TABLE ACCESS ` | `CLUSTER ` | Retrieval of rows from a table based on a value of an indexed cluster key. |
| `TABLE ACCESS ` | `HASH ` | Retrieval of rows from table based on hash cluster key value. |
| `TABLE ACCESS ` | `BY ROWID RANGE ` | Retrieval of rows from a table based on a rowid range. |
| `TABLE ACCESS ` | `SAMPLE BY ROWID RANGE ` | Retrieval of sampled rows from a table based on a rowid range. |
| `TABLE ACCESS` | `BY USER ROWID ` | If the table rows are located using user-supplied rowids. |
| `TABLE ACCESS` | `BY INDEX ROWID` | If the table is nonpartitioned and rows are located using indexes. |
| `TABLE ACCESS` | `BY GLOBAL INDEX ROWID` | If the table is partitioned and rows are located using only global indexes. |
| `TABLE ACCESS ` | `BY LOCAL INDEX ROWID ` | If the table is partitioned and rows are located using one or more local indexes and possibly some global indexes.  Partition Boundaries:  The partition boundaries might have been computed by:  A previous `PARTITION` step, in which case the `PARTITION_START` and `PARTITION_STOP` column values replicate the values present in the `PARTITION` step, and the `PARTITION_ID` contains the ID of the `PARTITION` step. Possible values for `PARTITION_START` and `PARTITION_STOP` are `NUMBER` (n), `KEY`, `INVALID`.  The `TABLE ACCESS` or `INDEX` step itself, in which case the `PARTITION_ID` contains the `ID` of the step. Possible values for `PARTITION_START` and `PARTITION_STOP` are `NUMBER` (n), `KEY`, `ROW REMOVE_LOCATION` (`TABLE ACCESS` only), and `INVALID`. |
| `TRANSPOSE` |  | Operation evaluating a `PIVOT` operation by transposing the results of `GROUP BY` to produce the final pivoted data. |
| `UNION ` |  | Operation accepting two sets of rows and returns the union of the sets, eliminating duplicates. |
| `UNPIVOT ` |  | Operation that rotates data from columns into rows. |
| `VIEW ` |  | Operation performing a view's query and then returning the resulting rows to another operation. |

See Also:

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=REFRN29510) for more information about `PLAN_TABLE`

### 7.3 Execution Plan Reference

This section describes `V$` views and `PLAN_COLUMN` columns.

This section contains the following topics:

#### 7.3.1 Execution Plan Views

The following dynamic performance and data dictionary views provide information on execution plans.

Table 7-4 Execution Plan Views

| View | Description |
| --- | --- |
| `V$SQL_SHARED_CURSOR` | Explains why a particular child cursor is not shared with existing child cursors. Each column identifies a specific reason why the cursor cannot be shared.  The `USE_FEEDBACK_STATS` column shows whether a child cursor fails to match because of reoptimization. |
| `V$SQL_PLAN` | Includes a superset of all rows appearing in all final plans. `PLAN_LINE_ID` is consecutively numbered, but for a single final plan, the IDs may not be consecutive. |
| `V$SQL_PLAN_STATISTICS_ALL` | Contains memory usage statistics for row sources that use SQL memory (sort or hash join). This view concatenates information in `V$SQL_PLAN` with execution statistics from `V$SQL_PLAN_STATISTICS` and `V$SQL_WORKAREA`. |

#### 7.3.2 PLAN\_TABLE Columns

The `PLAN_TABLE` is used by the `EXPLAIN PLAN` statement.

`PLAN_TABLE` contains the columns listed in Table 7-5.

Table 7-5 PLAN\_TABLE Columns

| Column | Type | Description |
| --- | --- | --- |
| `STATEMENT_ID ` | `VARCHAR2(30) ` | Value of the optional `STATEMENT_ID` parameter specified in the `EXPLAIN` `PLAN` statement. |
| `PLAN_ID` | `NUMBER` | Unique identifier of a plan in the database. |
| `TIMESTAMP ` | `DATE ` | Date and time when the `EXPLAIN` `PLAN` statement was generated. |
| `REMARKS ` | `VARCHAR2(80) ` | Any comment (of up to 80 bytes) you want to associate with each step of the explained plan. This column indicates whether the database used an outline or SQL profile for the query.  If you need to add or change a remark on any row of the `PLAN_TABLE`, then use the `UPDATE` statement to modify the rows of the `PLAN_TABLE`. |
| `OPERATION ` | `VARCHAR2(30) ` | Name of the internal operation performed in this step. In the first row generated for a statement, the column contains one of the following values:  - `DELETE STATEMENT` - `INSERT STATEMENT` - `SELECT STATEMENT` - `UPDATE STATEMENT`  See Table 7-6 for more information about values for this column. |
| `OPTIONS ` | `VARCHAR2(225) ` | A variation on the operation that the `OPERATION` column describes.  See Table 7-6 for more information about values for this column. |
| `OBJECT_NODE ` | `VARCHAR2(128) ` | Name of the database link used to reference the object (a table name or view name). For local queries using parallel execution, this column describes the order in which the database consumes output from operations. |
| `OBJECT_OWNER ` | `VARCHAR2(30) ` | Name of the user who owns the schema containing the table or index. |
| `OBJECT_NAME ` | `VARCHAR2(30) ` | Name of the table or index. |
| `OBJECT_ALIAS` | `VARCHAR2(65) ` | Unique alias of a table or view in a SQL statement. For indexes, it is the object alias of the underlying table. |
| `OBJECT_INSTANCE ` | `NUMERIC ` | Number corresponding to the ordinal position of the object as it appears in the original statement. The numbering proceeds from left to right, outer to inner for the original statement text. View expansion results in unpredictable numbers. |
| `OBJECT_TYPE ` | `VARCHAR2(30) ` | Modifier that provides descriptive information about the object; for example, `NONUNIQUE` for indexes. |
| `OPTIMIZER ` | `VARCHAR2(255) ` | Current mode of the optimizer. |
| `SEARCH_COLUMNS ` | `NUMBERIC ` | Not currently used. |
| `ID ` | `NUMERIC ` | A number assigned to each step in the execution plan. |
| `PARENT_ID ` | `NUMERIC ` | The ID of the next execution step that operates on the output of the `ID` step. |
| `DEPTH` | `NUMERIC` | Depth of the operation in the row source tree that the plan represents. You can use this value to indent the rows in a plan table report. |
| `POSITION ` | `NUMERIC ` | For the first row of output, this indicates the optimizer's estimated cost of executing the statement. For the other rows, it indicates the position relative to the other children of the same parent. |
| `COST ` | `NUMERIC ` | Cost of the operation as estimated by the optimizer's query approach. Cost is not determined for table access operations. The value of this column does not have any particular unit of measurement; it is a weighted value used to compare costs of execution plans. The value of this column is a function of the `CPU_COST` and `IO_COST` columns. |
| `CARDINALITY ` | `NUMERIC ` | Estimate by the query optimization approach of the number of rows that the operation accessed. |
| `BYTES ` | `NUMERIC ` | Estimate by the query optimization approach of the number of bytes that the operation accessed. |
| `OTHER_TAG ` | `VARCHAR2(255) ` | Describes the contents of the `OTHER` column. Values are:  - `SERIAL` (blank): Serial execution. Currently, SQL is not loaded in the `OTHER` column for this case. - `SERIAL_FROM_REMOTE` ` (S -> R)`: Serial execution at a remote site. - `PARALLEL_FROM_SERIAL (S -> P)`: Serial execution. Output of step is partitioned or broadcast to parallel execution servers. - `PARALLEL_TO_SERIAL (P -> S)`: Parallel execution. Output of step is returned to serial QC process. - `PARALLEL_TO_PARALLEL (P -> P)`: Parallel execution. Output of step is repartitioned to second set of parallel execution servers. - `PARALLEL_COMBINED_WITH_PARENT (PWP)`: Parallel execution; Output of step goes to next step in same parallel process. No interprocess communication to parent. - `PARALLEL_COMBINED_WITH_CHILD (PWC)`: Parallel execution. Input of step comes from prior step in same parallel process. No interprocess communication from child. |
| `PARTITION_START ` | `VARCHAR2(255) ` | Start partition of a range of accessed partitions. It can take one of the following values:  n indicates that the start partition has been identified by the SQL compiler, and its partition number is given by n.  `KEY` indicates that the start partition is identified at run time from partitioning key values.  `ROW LOCATION` indicates that the database computes the start partition (same as the stop partition) at run time from the location of each retrieved record. The record location is obtained by a user-specified ROWID or from a global index.  `INVALID` indicates that the range of accessed partitions is empty. |
| `PARTITION_STOP ` | `VARCHAR2(255) ` | Stop partition of a range of accessed partitions. It can take one of the following values:  n indicates that the stop partition has been identified by the SQL compiler, and its partition number is given by n.  `KEY` indicates that the stop partition is identified at run time from partitioning key values.  `ROW LOCATION` indicates that the database computes the stop partition (same as the start partition) at run time from the location of each retrieved record. The record location is obtained by a user or from a global index.  `INVALID` indicates that the range of accessed partitions is empty. |
| `PARTITION_ID ` | `NUMERIC ` | Step that has computed the pair of values of the `PARTITION_START` and `PARTITION_STOP` columns. |
| `OTHER ` | `LONG ` | Other information that is specific to the execution step that a user might find useful. See the `OTHER_TAG` column. |
| `DISTRIBUTION ` | `VARCHAR2(30) ` | Method used to distribute rows from producer query servers to consumer query servers.  See " Table 7-6 " for more information about the possible values for this column. For more information about consumer and producer query servers, see [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=GUID-1C6BC851-DE4A-4651-9813-3E70023C8264). |
| `CPU_COST ` | `NUMERIC ` | CPU cost of the operation as estimated by the query optimizer's approach. The value of this column is proportional to the number of machine cycles required for the operation. For statements that use the rule-based approach, this column is null. |
| `IO_COST ` | `NUMERIC ` | I/O cost of the operation as estimated by the query optimizer's approach. The value of this column is proportional to the number of data blocks read by the operation. For statements that use the rule-based approach, this column is null. |
| `TEMP_SPACE ` | `NUMERIC ` | Temporary space, in bytes, used by the operation as estimated by the query optimizer's approach. For statements that use the rule-based approach, or for operations that do not use any temporary space, this column is null. |
| `ACCESS_PREDICATES` | `VARCHAR2(4000)` | Predicates used to locate rows in an access structure. For example, start or stop predicates for an index range scan. |
| `FILTER_PREDICATES` | `VARCHAR2(4000)` | Predicates used to filter rows before producing them. |
| `PROJECTION` | `VARCHAR2(4000)` | Expressions produced by the operation. |
| `TIME` | `NUMBER(20,2)` | Elapsed time in seconds of the operation as estimated by query optimization. For statements that use the rule-based approach, this column is null. |
| `QBLOCK_NAME` | `VARCHAR2(30)` | Name of the query block, either system-generated or defined by the user with the `QB_NAME` hint. |

Table 7-6 Values of DISTRIBUTION Column of the PLAN\_TABLE

| DISTRIBUTION Text | Interpretation |
| --- | --- |
| `PARTITION (ROWID) ` | Maps rows to query servers based on the partitioning of a table or index using the rowid of the row to `UPDATE` / `DELETE`. |
| `PARTITION (KEY) ` | Maps rows to query servers based on the partitioning of a table or index using a set of columns. Used for partial partition-wise join, `PARALLEL INSERT`, `CREATE TABLE AS SELECT` of a partitioned table, and `CREATE PARTITIONED GLOBAL INDEX`. |
| `HASH ` | Maps rows to query servers using a hash function on the join key. Used for `PARALLEL JOIN` or `PARALLEL GROUP BY`. |
| `RANGE ` | Maps rows to query servers using ranges of the sort key. Used when the statement contains an `ORDER BY` clause. |
| `ROUND-ROBIN ` | Randomly maps rows to query servers. |
| `BROADCAST` | Broadcasts the rows of the entire table to each query server. Used for a parallel join when one table is very small compared to the other. |
| `QC (ORDER)` | The QC consumes the input in order, from the first to the last query server. Used when the statement contains an `ORDER BY` clause. |
| `QC (RANDOM)` | The QC consumes the input randomly. Used when the statement does not have an `ORDER BY` clause. |

Table 7-7 lists each combination of `OPERATION` and `OPTIONS` produced by the `EXPLAIN` `PLAN` statement and its meaning within an execution plan.

Table 7-7 OPERATION and OPTIONS Values Produced by EXPLAIN PLAN

| Operation | Option | Description |
| --- | --- | --- |
| `AND-EQUAL` |  | Operation accepting multiple sets of rowids, returning the intersection of the sets, eliminating duplicates. Used for the single-column indexes access path. |
| `BITMAP` | `CONVERSION ` | `TO ROWIDS` converts bitmap representations to actual rowids that you can use to access the table.  `FROM ROWIDS` converts the rowids to a bitmap representation.  `COUNT` returns the number of rowids if the actual values are not needed. |
| `BITMAP ` | `INDEX ` | `SINGLE VALUE` looks up the bitmap for a single key value in the index.  `RANGE SCAN` retrieves bitmaps for a key value range.  `FULL SCAN` performs a full scan of a bitmap index if there is no start or stop key. |
| `BITMAP ` | `MERGE ` | Merges several bitmaps resulting from a range scan into one bitmap. |
| `BITMAP ` | `MINUS ` | Subtracts bits of one bitmap from another. Row source is used for negated predicates. This option is usable only if there are non-negated predicates yielding a bitmap from which the subtraction can take place. |
| `BITMAP ` | `OR ` | Computes the bitwise `OR` of two bitmaps. |
| `BITMAP ` | `AND ` | Computes the bitwise `AND` of two bitmaps. |
| `BITMAP ` | `KEY ITERATION ` | Takes each row from a table row source and finds the corresponding bitmap from a bitmap index. This set of bitmaps are then merged into one bitmap in a following `BITMAP` `MERGE` operation. |
| `CONNECT BY ` |  | Retrieves rows in hierarchical order for a query containing a `CONNECT BY` clause. |
| `CONCATENATION ` |  | Operation accepting multiple sets of rows returning the union-all of the sets. |
| `COUNT` |  | Operation counting the number of rows selected from a table. |
| `COUNT` | `STOPKEY` | Count operation where the number of rows returned is limited by the `ROWNUM` expression in the `WHERE` clause. |
| `CUBE JOIN` |  | Joins a table or view on the left and a cube on the right.  See [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=SQLRF55589) to learn about the `NO_USE_CUBE` and `USE_CUBE` hints. |
| `CUBE JOIN` | `ANTI` | Uses an antijoin for a table or view on the left and a cube on the right. |
| `CUBE JOIN` | `ANTI SNA` | Uses an antijoin (single-sided null aware) for a table or view on the left and a cube on the right. The join column on the right (cube side) is `NOT NULL`. |
| `CUBE JOIN` | `OUTER` | Uses an outer join for a table or view on the left and a cube on the right. |
| `CUBE JOIN` | `RIGHT SEMI` | Uses a right semijoin for a table or view on the left and a cube on the right. |
| `CUBE SCAN` |  | Uses inner joins for all cube access. |
| `CUBE SCAN` | `PARTIAL OUTER` | Uses an outer join for at least one dimension, and inner joins for the other dimensions. |
| `CUBE SCAN` | `OUTER` | Uses outer joins for all cube access. |
| `DOMAIN INDEX ` |  | Retrieval of one or more rowids from a domain index. The options column contain information supplied by a user-defined domain index cost function, if any. |
| `FILTER ` |  | Operation accepting a set of rows, eliminates some of them, and returns the rest. |
| `FIRST ROW ` |  | Retrieval of only the first row selected by a query. |
| `FOR UPDATE ` |  | Operation retrieving and locking the rows selected by a query containing a `FOR` `UPDATE` clause. |
| `HASH` | `GROUP BY` | Operation hashing a set of rows into groups for a query with a `GROUP` `BY` clause. |
| `HASH` | `GROUP BY PIVOT` | Operation hashing a set of rows into groups for a query with a `GROUP` `BY` clause. The `PIVOT` option indicates a pivot-specific optimization for the `HASH GROUP BY` operator. |
| `HASH JOIN `  (These are join operations.) |  | Operation joining two sets of rows and returning the result. This join method is useful for joining large data sets of data (DSS, Batch). The join condition is an efficient way of accessing the second table.  Query optimizer uses the smaller of the two tables/data sources to build a hash table on the join key in memory. Then it scans the larger table, probing the hash table to find the joined rows. |
| `HASH JOIN ` | `ANTI ` | Hash (left) antijoin |
| `HASH JOIN ` | `SEMI ` | Hash (left) semijoin |
| `HASH JOIN ` | `RIGHT ANTI ` | Hash right antijoin |
| `HASH JOIN ` | `RIGHT SEMI ` | Hash right semijoin |
| `HASH JOIN ` | `OUTER ` | Hash (left) outer join |
| `HASH JOIN ` | `RIGHT OUTER ` | Hash right outer join |
| `INDEX `  (These are access methods.) | `UNIQUE SCAN ` | Retrieval of a single rowid from an index. |
| `INDEX` | `RANGE SCAN ` | Retrieval of one or more rowids from an index. Indexed values are scanned in ascending order. |
| `INDEX` | `RANGE SCAN DESCENDING ` | Retrieval of one or more rowids from an index. Indexed values are scanned in descending order. |
| `INDEX` | `FULL SCAN ` | Retrieval of all rowids from an index when there is no start or stop key. Indexed values are scanned in ascending order. |
| `INDEX` | `FULL SCAN DESCENDING ` | Retrieval of all rowids from an index when there is no start or stop key. Indexed values are scanned in descending order. |
| `INDEX ` | `FAST FULL SCAN ` | Retrieval of all rowids (and column values) using multiblock reads. No sorting order can be defined. Compares to a full table scan on only the indexed columns. Only available with the cost based optimizer. |
| `INDEX ` | `SKIP SCAN ` | Retrieval of rowids from a concatenated index without using the leading column(s) in the index. Only available with the cost based optimizer. |
| `INLIST ITERATOR ` |  | Iterates over the next operation in the plan for each value in the `IN` -list predicate. |
| `INTERSECTION ` |  | Operation accepting two sets of rows and returning the intersection of the sets, eliminating duplicates. |
| `MERGE JOIN `  (These are join operations.) |  | Operation accepting two sets of rows, each sorted by a value, combining each row from one set with the matching rows from the other, and returning the result. |
| `MERGE JOIN ` | `OUTER ` | Merge join operation to perform an outer join statement. |
| `MERGE JOIN ` | `ANTI ` | Merge antijoin. |
| `MERGE JOIN ` | `SEMI ` | Merge semijoin. |
| `MERGE JOIN ` | `CARTESIAN ` | Can result from 1 or more of the tables not having any join conditions to any other tables in the statement. Can occur even with a join and it may not be flagged as `CARTESIAN` in the plan. |
| `CONNECT BY ` |  | Retrieval of rows in hierarchical order for a query containing a `CONNECT` `BY` clause. |
| `MAT_VIEW REWITE ACCESS `  (These are access methods.) | `FULL` | Retrieval of all rows from a materialized view. |
| `MAT_VIEW REWITE ACCESS ` | `SAMPLE ` | Retrieval of sampled rows from a materialized view. |
| `MAT_VIEW REWITE ACCESS ` | `CLUSTER ` | Retrieval of rows from a materialized view based on a value of an indexed cluster key. |
| `MAT_VIEW REWITE ACCESS ` | `HASH ` | Retrieval of rows from materialized view based on hash cluster key value. |
| `MAT_VIEW REWITE ACCESS ` | `BY ROWID RANGE ` | Retrieval of rows from a materialized view based on a rowid range. |
| `MAT_VIEW REWITE ACCESS ` | `SAMPLE BY ROWID RANGE ` | Retrieval of sampled rows from a materialized view based on a rowid range. |
| `MAT_VIEW REWITE ACCESS` | `BY USER ROWID ` | If the materialized view rows are located using user-supplied rowids. |
| `MAT_VIEW REWITE ACCESS ` | `BY INDEX ROWID ` | If the materialized view is nonpartitioned and rows are located using indexes. |
| `MAT_VIEW REWITE ACCESS ` | `BY GLOBAL INDEX ROWID ` | If the materialized view is partitioned and rows are located using only global indexes. |
| `MAT_VIEW REWITE ACCESS ` | `BY LOCAL INDEX ROWID ` | If the materialized view is partitioned and rows are located using one or more local indexes and possibly some global indexes.  Partition Boundaries:  The partition boundaries might have been computed by:  A previous `PARTITION` step, in which case the `PARTITION_START` and `PARTITION_STOP` column values replicate the values present in the `PARTITION` step, and the `PARTITION_ID` contains the ID of the `PARTITION` step. Possible values for `PARTITION_START` and `PARTITION_STOP` are `NUMBER` (n), `KEY`, and `INVALID`.  The `MAT_VIEW REWRITE ACCESS` or `INDEX` step itself, in which case the `PARTITION_ID` contains the `ID` of the step. Possible values for `PARTITION_START` and `PARTITION_STOP` are `NUMBER` (n), `KEY`, `ROW LOCATION` (`MAT_VIEW REWRITE` `ACCESS` only), and `INVALID`. |
| `MINUS` |  | Operation accepting two sets of rows and returning rows appearing in the first set but not in the second, eliminating duplicates. |
| `NESTED LOOPS`  (These are join operations.) |  | Operation accepting two sets of rows, an outer set and an inner set. Oracle Database compares each row of the outer set with each row of the inner set, returning rows that satisfy a condition. This join method is useful for joining small subsets of data (OLTP). The join condition is an efficient way of accessing the second table. |
| `NESTED LOOPS ` | `OUTER` | Nested loops operation to perform an outer join statement. |
| `PARTITION` |  | Iterates over the next operation in the plan for each partition in the range given by the `PARTITION_START` and `PARTITION_STOP` columns. `PARTITION` describes partition boundaries applicable to a single partitioned object (table or index) or to a set of equipartitioned objects (a partitioned table and its local indexes). The partition boundaries are provided by the values of `PARTITION_START` and `PARTITION_STOP` of the `PARTITION`. Refer to Table 7-4 for valid values of partition start and stop. |
| `PARTITION` | `SINGLE` | Access one partition. |
| `PARTITION` | `ITERATOR` | Access many partitions (a subset). |
| `PARTITION` | `ALL` | Access all partitions. |
| `PARTITION` | `INLIST` | Similar to iterator, but based on an `IN` -list predicate. |
| `PARTITION` | `INVALID` | Indicates that the partition set to be accessed is empty. |
| `PX` `ITERATOR` | `BLOCK`, `CHUNK` | Implements the division of an object into block or chunk ranges among a set of parallel execution servers. |
| `PX` `COORDINATOR` |  | Implements the Query Coordinator which controls, schedules, and executes the parallel plan below it using parallel execution servers. It also represents a serialization point, as the end of the part of the plan executed in parallel and always has a `PX SEND QC` operation below it. |
| `PX` `PARTITION` |  | Same semantics as the regular `PARTITION` operation except that it appears in a parallel plan. |
| `PX` `RECEIVE` |  | Shows the consumer/receiver parallel execution node reading repartitioned data from a send/producer (QC or parallel execution server) executing on a PX SEND node. This information was formerly displayed into the `DISTRIBUTION` column. See Table 7-5. |
| `PX` `SEND` | `QC` `(RANDOM), HASH`, `RANGE` | Implements the distribution method taking place between two sets of parallel execution servers. Shows the boundary between two sets and how data is repartitioned on the send/producer side (QC or side. This information was formerly displayed into the `DISTRIBUTION` column. See Table 7-5. |
| `REMOTE` |  | Retrieval of data from a remote database. |
| `SEQUENCE` |  | Operation involving accessing values of a sequence. |
| `SORT` | `AGGREGATE` | Retrieval of a single row that is the result of applying a group function to a group of selected rows. |
| `SORT` | `UNIQUE` | Operation sorting a set of rows to eliminate duplicates. |
| `SORT` | `GROUP` `BY` | Operation sorting a set of rows into groups for a query with a `GROUP` `BY` clause. |
| `SORT` | `GROUP BY PIVOT` | Operation sorting a set of rows into groups for a query with a `GROUP` `BY` clause. The `PIVOT` option indicates a pivot-specific optimization for the `SORT GROUP BY` operator. |
| `SORT ` | `JOIN ` | Operation sorting a set of rows before a merge-join. |
| `SORT ` | `ORDER BY ` | Operation sorting a set of rows for a query with an `ORDER` `BY` clause. |
| `TABLE ACCESS `  (These are access methods.) | `FULL ` | Retrieval of all rows from a table. |
| `TABLE ACCESS ` | `SAMPLE ` | Retrieval of sampled rows from a table. |
| `TABLE ACCESS ` | `CLUSTER ` | Retrieval of rows from a table based on a value of an indexed cluster key. |
| `TABLE ACCESS ` | `HASH ` | Retrieval of rows from table based on hash cluster key value. |
| `TABLE ACCESS ` | `BY ROWID RANGE ` | Retrieval of rows from a table based on a rowid range. |
| `TABLE ACCESS ` | `SAMPLE BY ROWID RANGE ` | Retrieval of sampled rows from a table based on a rowid range. |
| `TABLE ACCESS` | `BY USER ROWID ` | If the table rows are located using user-supplied rowids. |
| `TABLE ACCESS ` | `BY INDEX ROWID ` | If the table is nonpartitioned and rows are located using index(es). |
| `TABLE ACCESS ` | `BY GLOBAL INDEX ROWID ` | If the table is partitioned and rows are located using only global indexes. |
| `TABLE ACCESS ` | `BY LOCAL INDEX ROWID ` | If the table is partitioned and rows are located using one or more local indexes and possibly some global indexes.  Partition Boundaries:  The partition boundaries might have been computed by:  A previous `PARTITION` step, in which case the `PARTITION_START` and `PARTITION_STOP` column values replicate the values present in the `PARTITION` step, and the `PARTITION_ID` contains the ID of the `PARTITION` step. Possible values for `PARTITION_START` and `PARTITION_STOP` are `NUMBER` (n), `KEY`, and `INVALID`.  The `TABLE` `ACCESS` or `INDEX` step itself, in which case the `PARTITION_ID` contains the `ID` of the step. Possible values for `PARTITION_START` and `PARTITION_STOP` are `NUMBER` (n), `KEY`, `ROW LOCATION` (`TABLE` `ACCESS` only), and `INVALID`. |
| `TRANSPOSE` |  | Operation evaluating a `PIVOT` operation by transposing the results of `GROUP BY` to produce the final pivoted data. |
| `UNION ` |  | Operation accepting two sets of rows and returns the union of the sets, eliminating duplicates. |
| `UNPIVOT ` |  | Operation that rotates data from columns into rows. |
| `VIEW ` |  | Operation performing a view's query and then returning the resulting rows to another operation. |

See Also:

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=REFRN29510) for more information about `PLAN_TABLE`

#### 7.3.3 DBMS\_XPLAN Display Functions

You can use the `DBMS_XPLAN` display functions to show plans.

The display functions accept options for displaying the plan table output. You can specify:

- A plan table name if you are using a table different from `PLAN_TABLE`
- A statement ID if you have set a statement ID with the `EXPLAIN PLAN`
- A format option that determines the level of detail: `BASIC`, `SERIAL`, `TYPICAL`, `ALL`, and in some cases `ADAPTIVE`

Table 7-8 DBMS\_XPLAN Display Functions

| Display Functions | Notes |
| --- | --- |
| `DISPLAY` | This table function displays the contents of the plan table.  In addition, you can use this table function to display any plan (with or without statistics) stored in a table as long as the columns of this table are named the same as columns of the plan table (or `V$SQL_PLAN_STATISTICS_ALL` if statistics are included). You can apply a predicate on the specified table to select rows of the plan to display.  The `format` parameter controls the level of the plan. It accepts the values `BASIC`, `TYPICAL`, `SERIAL`, and `ALL`. |
| `DISPLAY_AWR` | This table function displays the contents of an execution plan stored in AWR.  The `format` parameter controls the level of the plan. It accepts the values `BASIC`, `TYPICAL`, `SERIAL`, and `ALL`. |
| `DISPLAY_CURSOR` | This table function displays the explain plan of any cursor loaded in the cursor cache. In addition to the explain plan, various plan statistics (such as. I/O, memory and timing) can be reported (based on the `V$SQL_PLAN_STATISTICS_ALL VIEWS`).  The `format` parameter controls the level of the plan. It accepts the values `BASIC`, `TYPICAL`, `SERIAL`, `ALL`, and `ADAPTIVE`. When you specify `ADAPTIVE`, the output includes:  - The final plan. If the execution has not completed, then the output shows the current plan. This section also includes notes about run-time optimizations that affect the plan. - Recommended plan. In reporting mode, the output includes the plan that would be chosen based on execution statistics. - Dynamic plan. The output summarizes the portions of the plan that differ from the default plan chosen by the optimizer. - Reoptimization. The output displays the plan that would be chosen on a subsequent execution because of reoptimization. |
| `DISPLAY_PLAN` | This table function displays the contents of the plan table in a variety of formats with `CLOB` output type.  The `format` parameter controls the level of the plan. It accepts the values `BASIC`, `TYPICAL`, `SERIAL`, `ALL`, and `ADAPTIVE`. When you specify `ADAPTIVE`, the output includes the default plan. For each dynamic subplan, the plan shows a list of the row sources from the original that may be replaced, and the row sources that would replace them.  If the `format` argument specifies the outline display, then the function displays the hints for each option in the dynamic subplan. If the plan is not an adaptive query plan, then the function displays the default plan. When you do not specify `ADAPTIVE`, the plan is shown as-is, but with additional comments in the Note section that show any row sources that are dynamic. |
| `DISPLAY_SQL_PLAN_BASELINE` | This table function displays one or more execution plans for the specified SQL handle of a SQL plan baseline.  This function uses plan information stored in the plan baseline to explain and display the plans. The `plan_id` stored in the SQL management base may not match the `plan_id` of the generated plan. A mismatch between the stored `plan_id` and generated `plan_id` means that it is a non-reproducible plan. Such a plan is deemed invalid and is bypassed by the optimizer during SQL compilation. |
| `DISPLAY_SQLSET` | This table function displays the execution plan of a given statement stored in a SQL tuning set.  The `format` parameter controls the level of the plan. It accepts the values `BASIC`, `TYPICAL`, `SERIAL`, and `ALL`. |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=ARPLS68408) to learn more about `DBMS_XPLAN` display functions
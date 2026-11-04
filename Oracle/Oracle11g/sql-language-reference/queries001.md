---
title: About Queries and Subqueries
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/queries001.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

A query is an operation that retrieves data from one or more tables or views. In this reference, a top-level `SELECT` statement is called a query, and a query nested within another SQL statement is called a subquery.

This section describes some types of queries and subqueries and how to use them. The top level of the syntax is shown in this chapter. Refer to [SELECT](statements_10002.md) for the full syntax of all the clauses and the semantics of this statement.

select::=

![select](img/select.gif)

> ```
> subquery [ for_update_clause ] ;
> ```
  
  

subquery::=

![subquery](img/subquery.gif)

> ```
> { query_block
> | subquery { UNION [ALL] | INTERSECT | MINUS } subquery
>     [ { UNION [ALL] | INTERSECT | MINUS } subquery ]...
> | ( subquery )
> } [ order_by_clause ]
> ```
  
  

query\_block::=

![query_block](img/query_block.gif)

> ```
> [ subquery_factoring_clause ]
> SELECT [ hint ] [ { { DISTINCT | UNIQUE } | ALL } ] select_list
>   FROM { table_reference | join_clause | ( join_clause ) }
>          [ , { table_reference | join_clause | (join_clause) } ] ...
>   [ where_clause ]
>   [ hierarchical_query_clause ]
>   [ group_by_clause ]
>   [ model_clause ]
> ```

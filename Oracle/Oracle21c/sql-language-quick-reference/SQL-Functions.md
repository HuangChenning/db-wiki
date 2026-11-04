---
title: SQL Language Quick Reference
book: SQL Language Quick Reference
doc_id: F31302-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlqr/SQL-Functions.html
tags:
  - oracle
  - 21c
  - sql-language-quick-reference
---

This chapter presents the syntax for SQL functions.

This chapter includes the following section:

- Syntax for SQL Functions

### Syntax for SQL Functions

A function is a command that manipulates data items and returns a single value.

The sections that follow show each SQL function and its related syntax. Refer to [Subclauses](Subclauses.md) for the syntax of the subclauses.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF006) for detailed information about SQL functions

[ABS](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00601)

```
ABS(n)
```

[ACOS](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00602)

```
ACOS(n)
```

[ADD\_MONTHS](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00603)

```
ADD_MONTHS(date, integer)
```

[aggregate\_function](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF20035)

Aggregate functions return a single result row based on groups of rows, rather than on single rows.

[analytic\_function](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-527832F7-63C0-4445-8C16-307FA5084056)

```
analytic_function([ arguments ]) OVER { window_name | (analytic_clause)}
```

[ANY\_VALUE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-A3C47D5E-B145-40B2-93D2-CA3BA65C2D81)

```
ANY_VALUE ( [ DISTINCT | ALL ] expr )
```

[APPROX\_COUNT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-7D07E04A-3F9A-425E-BADE-EDA9C6162E9C)

```
APPROX_COUNT ( ( expr [ , expr 'MAX_ERROR' ] ...) )
```

[APPROX\_COUNT\_DISTINCT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF56900)

```
APPROX_COUNT_DISTINCT(expr)
```

[APPROX\_COUNT\_DISTINCT\_AGG](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF57340)

```
APPROX_COUNT_DISTINCT_AGG(detail)
```

[APPROX\_COUNT\_DISTINCT\_DETAIL](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF57344)

```
APPROX_COUNT_DISTINCT_DETAIL(expr)
```

[APPROX\_MEDIAN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF57348)

```
APPROX_MEDIAN( expr [ DETERMINISTIC ] [, { 'ERROR_RATE' | 'CONFIDENCE' } ] )
```

[APPROX\_PERCENTILE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF57354)

```
APPROX_PERCENTILE( expr [ DETERMINISTIC ] [, { 'ERROR_RATE' | 'CONFIDENCE' } ] ) 
  WITHIN GROUP ( ORDER BY expr [ DESC | ASC ] )
```

[APPROX\_PERCENTILE\_AGG](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF57360)

```
APPROX_PERCENTILE_AGG(expr)
```

[APPROX\_PERCENTILE\_DETAIL](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF57364)

```
APPROX_PERCENTILE_DETAIL( expr [ DETERMINISTIC ] )
```

[APPROX\_RANK](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-4F20978C-3188-4225-863D-0F7A25FD78FD)

```
APPROX_RANK ( expr [ PARTITION BY partition_by_clause ] [ ORDER BY order_by_clause DESC] )
```

[APPROX\_SUM](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-AC2A72A7-24E5-4FB8-B012-BD35CB560D6B)

```
APPROX_SUM ( expr [ , expr 'MAX_ERROR' ] ...)
```

[ASCII](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00604)

```
ASCII(char)
```

[ASCIISTR](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00605)

```
ASCIISTR(char)
```

[ASIN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00606)

```
ASIN(n)
```

[ATAN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00607)

```
ATAN(n)
```

[ATAN2](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00608)

```
ATAN2(n1 , n2)
```

[AVG](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00609)

```
AVG([ DISTINCT | ALL ] expr) [ OVER(analytic_clause) ]
```

[BFILENAME](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00610)

```
BFILENAME('directory', 'filename')
```

[BIN\_TO\_NUM](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00611)

```
BIN_TO_NUM(expr [, expr ]... )
```

[BITAND](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00612)

```
BITAND(expr1, expr2)
```

[BIT\_AND\_AGG](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-82497098-6D77-48D3-89EF-C1041BF8A258)

```
BIT_AND_AGG ( [DISTINCT | ALL | UNIQUE] expr )
```

[BITMAP\_BIT\_POSITION](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-B57660B6-FDFA-4339-ADD3-DBE818C37BE6)

```
BITMAP_BIT_POSITION  ( expr )
```

[BITMAP\_BUCKET\_NUMBER](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-6368CC51-B7C5-4BD9-9276-DE449BBC2CF3)

```
BITMAP_BUCKET_NUMBER ( expr )
```

[BITMAP\_CONSTRUCT\_AGG](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-AD768466-C6FF-45D7-AB26-5B1315E76B84)

```
BITMAP_CONSTRUCT_AGG (  expr  )
```

[BITMAP\_COUNT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-F1A3261E-7DA9-4FEF-8413-E38907C856BA)

```
BITMAP_COUNT ( expr )
```

[BITMAP\_OR\_AGG](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-8C99C362-BE95-4495-9E50-4C1B572CCBEF)

```
BITMAP_OR_AGG ( expr )
```

[BIT\_OR\_AGG](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-18B0E3CB-1C90-4625-8E36-B422FA4E04A8)

```
BIT_OR_AGG ( [DISTINCT | ALL | UNIQUE] expr )
```

[BIT\_XOR\_AGG](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-1563FB7E-9CC9-4D03-859E-BE336AF01F1D)

```
BIT_XOR_AGG ( [DISTINCT | ALL | UNIQUE] expr )
```

[CARDINALITY](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06305)

```
CARDINALITY(nested_table)
```

[CAST](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00613)

```
CAST({ expr | MULTISET (subquery) } AS type_name
  [ DEFAULT return_value ON CONVERSION ERROR ]
  [, fmt [, 'nlsparam' ] ])
```

[CEIL](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00614)

```
CEIL(n)
```

[CHARTOROWID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00615)

```
CHARTOROWID(char)
```

[CHECKSUM](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-3F55C5DF-F23A-4B2F-BC6F-E03B34B78BA8)

```
CHECKSUM ( [ALL | DISTINCT | UNIQUE] expr )
```

[CHR](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00616)

```
CHR(n [ USING NCHAR_CS ])
```

[CLUSTER\_DETAILS (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55703)

```
CLUSTER_DETAILS ( [ schema . ] model 
                  [ , cluster_id [ , topN ] ] [ DESC | ASC | ABS ]
                  mining_attribute_clause )
```

[CLUSTER\_DETAILS (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55707)

```
CLUSTER_DETAILS ( INTO n
                  [ , cluster_id [ , topN ] ] [ DESC | ASC | ABS ]
                  mining_attribute_clause )
                OVER ( mining_analytic_clause )
```

[CLUSTER\_DISTANCE (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55712)

```
CLUSTER_DISTANCE ( [ schema . ] model [ , cluster_id ] mining_attribute_clause )
```

[CLUSTER\_DISTANCE (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55716)

```
CLUSTER_DISTANCE ( INTO n [, cluster_id] mining_attribute_clause )
                 OVER ( mining_analytic_clause )
```

[CLUSTER\_ID (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06213)

```
CLUSTER_ID ( [ schema . ] model mining_attribute_clause )
```

[CLUSTER\_ID (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55724)

```
CLUSTER_ID ( INTO n mining_attribute_clause )
           OVER ( mining_analytic_clause )
```

[CLUSTER\_PROBABILITY (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06214)

```
CLUSTER_PROBABILITY ( [ schema . ] model [, cluster_id ] mining_attribute_clause )
```

[CLUSTER\_PROBABILITY (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55728)

```
CLUSTER_PROBABILITY ( INTO n [, cluster_id] mining_attribute_clause )
                    OVER ( mining_analytic_clause )
```

[CLUSTER\_SET (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06215)

```
CLUSTER_SET ( [ schema . ] model [ , topN [ , cutoff ] ] mining_attribute_clause )
```

[CLUSTER\_SET (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55732)

```
CLUSTER_SET ( INTO n [, topN [, cutoff]] mining_attribute_clause )
            OVER ( mining_analytic_clause )
```

[COALESCE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00617)

```
COALESCE(expr [, expr ]...)
```

[COLLATION](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-70A694BA-C1A0-4F5A-9492-58A5943D9BDD)

```
COLLATION(expr)
```

[COLLECT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06304)

```
COLLECT( [ DISTINCT | UNIQUE ] column [ ORDER BY expr ] )
```

[COMPOSE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00618)

```
COMPOSE(char)
```

[CON\_DBID\_TO\_ID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF56629)

```
CON_DBID_TO_ID(container_dbid)
```

[CON\_GUID\_TO\_ID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF56633)

```
CON_GUID_TO_ID(container_guid)
```

[CON\_ID\_TO\_CON\_NAME](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-85BFFF80-142A-43EF-B807-60890FB64F65)

```
CON_ID_TO_CON_NAME(container_guid)
```

[CON\_ID\_TO\_DBID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-4305B1BC-5829-4AAD-B4DF-AEE17EB8F18D)

```
CON_ID_TO_DBID(container_guid)
```

[CON\_ID\_TO\_GUID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-2B5AB386-2254-46A6-83B6-ED0504008F03)

```
CON_ID_TO_GUID(container_guid)
```

[CON\_ID\_TO\_UID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-0C8239D7-5848-4C23-8680-E0B19490C48B)

```
CON_ID_TO_UID(container_guid)
```

[CON\_NAME\_TO\_ID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF56637)

```
CON_NAME_TO_ID(container_name)
```

[CON\_UID\_TO\_ID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF56641)

```
CON_UID_TO_ID(container_uid)
```

[CONCAT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00619)

```
CONCAT(char1, char2)
```

[CONVERT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00620)

```
CONVERT(char, dest_char_set[, source_char_set ])
```

[CORR](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00621)

```
CORR(expr1, expr2) [ OVER (analytic_clause) ]
```

[CORR\_K](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06314), [CORR\_S](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06314)

```
{ CORR_K | CORR_S }
   (expr1, expr2
     [, { COEFFICIENT
        | ONE_SIDED_SIG
        | ONE_SIDED_SIG_POS
        | ONE_SIDED_SIG_NEG
        | TWO_SIDED_SIG
        }
     ]
   )
```

[COS](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00622)

```
COS(n)
```

[COSH](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00623)

```
COSH(n)
```

[COUNT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00624)

```
COUNT({ * | [ DISTINCT | ALL ] expr }) [ OVER (analytic_clause) ]
```

[COVAR\_POP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00625)

```
COVAR_POP(expr1, expr2)
   [ OVER (analytic_clause) ]
```

[COVAR\_SAMP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00626)

```
COVAR_SAMP(expr1, expr2) [ OVER (analytic_clause) ]
```

[CUBE\_TABLE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF20027)

```
CUBE_TABLE
( ' { schema.cube [ {HIERARCHY | HRR} dimension hierarchy ]...
    | schema.dimension [ {HIERARCHY | HRR} [dimension] hierarchy ]
    }
  '
)
```

[CUME\_DIST (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00627)

```
CUME_DIST(expr[,expr ]...) WITHIN GROUP
  (ORDER BY expr [ DESC | ASC ]
                 [ NULLS { FIRST | LAST } ] 
            [, expr [ DESC | ASC ]
                    [ NULLS { FIRST | LAST } ]
            ]...
  )
```

[CUME\_DIST (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF51332)

```
CUME_DIST() OVER ([ query_partition_clause ] order_by_clause)
```

[CURRENT\_DATE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00628)

```
CURRENT_DATE
```

[CURRENT\_TIMESTAMP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00629)

```
CURRENT_TIMESTAMP [ (precision) ]
```

[CV](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06175)

```
CV([ dimension_column ])
```

[DATAOBJ\_TO\_MAT\_PARTITION](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-195AC748-0C9E-4A68-B2BC-2411DE435375)

```
DATAOBJ_TO_MAT_PARTITION( table, partition_id )
```

[DATAOBJ\_TO\_PARTITION](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF20028)

```
DATAOBJ_TO_PARTITION( table, partition_id )
```

[DBTIMEZONE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00630)

```
DBTIMEZONE
```

[DECODE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00631)

```
DECODE(expr, search, result [, search, result ]... [, default ])
```

[DECOMPOSE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00632)

```
DECOMPOSE( string [, { 'CANONICAL' | 'COMPATIBILITY' } ] )
```

[DENSE\_RANK (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00633)

```
DENSE_RANK(expr [, expr ]...) WITHIN GROUP
  (ORDER BY expr [ DESC | ASC ]
                 [ NULLS { FIRST | LAST } ]
            [,expr [ DESC | ASC ]
                   [ NULLS { FIRST | LAST } ]
            ]...
  )
```

[DENSE\_RANK (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF51362)

```
DENSE_RANK( ) OVER([ query_partition_clause ] order_by_clause)
```

[DEPTH](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06176)

```
DEPTH(correlation_integer)
```

[DEREF](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00634)

```
DEREF(expr)
```

[DUMP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00635)

```
DUMP(expr[, return_fmt [, start_position [, length ] ]])
```

[EMPTY\_BLOB](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00636), [EMPTY\_CLOB](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00636)

```
{ EMPTY_BLOB | EMPTY_CLOB }( )
```

[EXISTSNODE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00637)

```
EXISTSNODE(XMLType_instance, XPath_string [, namespace_string ])
```

[EXP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00638)

```
EXP(n)
```

[EXTRACT (datetime)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00639)

```
EXTRACT( { YEAR
         | MONTH
         | DAY
         | HOUR
         | MINUTE
         | SECOND
         | TIMEZONE_HOUR
         | TIMEZONE_MINUTE
         | TIMEZONE_REGION
         | TIMEZONE_ABBR
         }
         FROM { expr }
       )
```

[EXTRACT (XML)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00640)

```
EXTRACT(XMLType_instance, XPath_string [, namespace_string ])
```

[EXTRACTVALUE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06173)

```
EXTRACTVALUE(XMLType_instance, XPath_string [, namespace_string ])
```

[FEATURE\_COMPARE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-3D4E179F-F5D2-4FCF-AB42-4D0C8CC7D514)

```
FEATURE_COMPARE ( [ schema . ] model
  mining_attribute_clause AND mining_attribute_clause )
```

[FEATURE\_DETAILS (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55734)

```
FEATURE_DETAILS ( [ schema . ] model
                  [ , feature_id [ , topN ] ] [ DESC | ASC | ABS ]
                  mining_attribute_clause )
```

[FEATURE\_DETAILS (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55738)

```
FEATURE_DETAILS ( INTO n
                  [ , feature_id [ , topN ] ] [ DESC | ASC | ABS ]
                  mining_attribute_clause )
                OVER ( mining_analytic_clause )
```

[FEATURE\_ID (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06216)

```
FEATURE_ID( [ schema . ] model mining_attribute_clause )
```

[FEATURE\_ID (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55745)

```
FEATURE_ID ( INTO n mining_attribute_clause )
           OVER ( mining_analytic_clause )
```

[FEATURE\_SET (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06217)

```
FEATURE_SET ( [ schema . ] model [, topN [, cutoff ]] mining_attribute_clause )
```

[FEATURE\_SET (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55749)

```
FEATURE_SET ( INTO n [, topN [, cutoff ] ] mining_attribute_clause )
            OVER ( mining_analytic_clause )
```

[FEATURE\_VALUE (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06218)

```
FEATURE_VALUE ( [ schema . ] model [, feature_id ] mining_attribute_clause )
```

[FEATURE\_VALUE (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55753)

```
FEATURE_VALUE ( INTO n [ , feature_id ] mining_attribute_clause )
              OVER ( mining_analytic_clause )
```

[FIRST](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00641)

```
aggregate_function
   KEEP
   (DENSE_RANK FIRST ORDER BY
    expr [ DESC | ASC ]
         [ NULLS { FIRST | LAST } ]
    [, expr [ DESC | ASC ]
            [ NULLS { FIRST | LAST } ]
    ]...
   )
   [ OVER ( [query_partition_clause] ) ]
```

[FIRST\_VALUE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00642)

```
FIRST_VALUE 
  { (expr) [ {RESPECT | IGNORE} NULLS ]
  | (expr [ {RESPECT | IGNORE} NULLS ])
  }
  OVER (analytic_clause)
```

[FLOOR](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00643)

```
FLOOR(n)
```

[FROM\_TZ](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00644)

```
FROM_TZ (timestamp_value, time_zone_value)
```

[GREATEST](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00645)

```
GREATEST(expr [, expr ]...)
```

[GROUP\_ID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00646)

```
GROUP_ID( )
```

[GROUPING](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00647)

```
GROUPING(expr)
```

[GROUPING\_ID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00648)

```
GROUPING_ID(expr [, expr ]...)
```

[HEXTORAW](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00649)

```
HEXTORAW(char)
```

[INITCAP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00650)

```
INITCAP(char)
```

[INSTR](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00651)

```
{ INSTR
| INSTRB
| INSTRC
| INSTR2
| INSTR4
}
(string , substring [, position [, occurrence ] ])
```

[ITERATION\_NUMBER](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06328)

```
ITERATION_NUMBER
```

[JSON\_ARRAY](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-46CDB3AF-5795-455B-85A8-764528CEC43B)

```
JSON_ARRAY
  ( JSON_ARRAY_content ) | JSON [ JSON_ARRAY_content ]
```

[JSON\_ARRAYAGG](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-6D56077D-78DE-4CC0-9498-225DDC42E054)

```
JSON_ARRAYAGG
  ( expr [ FORMAT JSON ] [ order_by_clause ]
    [ JSON_on_null_clause ] [ JSON_returning_clause ]
    [ STRICT ] )
```

[JSON\_CONSTRUCTOR](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-2B598841-A327-4610-91B9-602F480A8314)

```
JSON_CONSTRUCTOR ( expr )
```

[JSON\_DATAGUIDE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-4CF32887-0F46-4925-8381-AE2B74343933)

```
JSON_DATAGUIDE ( expr [ , format [ , flag ] ] )
```

[JSON\_MERGEPATCH](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-2004F536-BE60-4457-A1A8-AB908FFF5399)

```
JSON_MERGEPATCH
   ( JSON_target_expr , JSON_patch_expr [ JSON_returning_clause ] [ PRETTY ] [ ASCII ] 
     [ TRUNCATE ] [ JSON_on_error_clause ] )
```

[JSON\_OBJECT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-1EF347AE-7FDA-4B41-AFE0-DD5A49E8B370)

```
JSON_OBJECT
    ( JSON_OBJECT_content ) | JSON { JSON_OBJECT_content }
```

[JSON\_OBJECTAGG](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-09422D4A-936C-4D38-9991-C64101283D98)

```
JSON_OBJECTAGG
  ( [ KEY ] key_expr VALUE val_expr [ FORMAT JSON ]
    [ JSON_on_null_clause ] [ JSON_returning_clause ]
    [ STRICT ] [ WITH UNIQUE KEYS ]  )
```

[JSON\_QUERY](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF56718)

```
JSON_QUERY
  ( expr [ FORMAT JSON ], JSON_basic_path_expression
    [ JSON_query_returning_clause ] [ JSON_query_wrapper_clause ]
    [ JSON_query_on_error_clause ] [ JSON_query_on_empty_clause ]
    [ JSON_query_on_mismatch_clause ]
  )
```

[JSON\_SCALAR](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-F05BD523-F827-4A5F-9A82-8CBC2DB04E2E)

```
JSON_SCALAR ( expr [ SQL | JSON ] [ NULL ON NULL ] )
```

[JSON\_SERIALIZE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-01B769C6-A7B3-4136-977F-63CA05963D21)

```
JSON_SERIALIZE 
( expr [ JSON_returning_clause ] [ PRETTY ] [ASCII ] [ TRUNCATE ] 
   [ { NULL | ERROR | ( EMPTY { ARRAY | OBJECT } ) } ON ERROR ] 
)
```

[JSON\_TABLE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF56973)

```
JSON_TABLE
  ( expr [ FORMAT JSON ] [ , JSON_basic_path_expression ]
    [ JSON_table_on_error_clause ] JSON_columns_clause )
```

[JSON\_TRANSFORM](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-DD2A821B-C688-4310-81B5-5F45090B9366)

```
JSON_TRANSFORM ( input_expr , operation [ , operation ]...
    [ JSON_passing_clause ] 
    [ JSON_TRANSFORM_returning_clause ] )
```

[JSON\_VALUE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF56668)

```
JSON_VALUE
  ( expr [ FORMAT JSON ] [ , JSON_basic_path_expression ]
    [ JSON_value_returning_clause ] [ JSON_value_on_error_clause ]
    [ JSON_value_on_empty_clause ] [ JSON_value_on_mismatch_clause ]
  )
```

[KURTOSIS\_POP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-F820DFF7-B758-460E-AECC-053915069B9F)

```
KURTOSIS_POP ( [ {DISTINCT | ALL | UNIQUE} ]  expr )
```

[KURTOSIS\_SAMP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-487DE503-A015-415F-B6CD-F9D095B91178)

```
KURTOSIS_SAMP ( [ {DISTINCT | ALL | UNIQUE} ] x expr )
```

[LAG](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00652)

```
LAG
  { ( value_expr [, offset [, default]]) [ { RESPECT | IGNORE } NULLS ] 
  | ( value_expr [ { RESPECT | IGNORE } NULLS ] [, offset [, default]] )
  }
  OVER ([ query_partition_clause ] order_by_clause)
```

[LAST](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00653)

```
aggregate_function KEEP
  (DENSE_RANK LAST ORDER BY
    expr [ DESC | ASC ]
         [ NULLS { FIRST | LAST } ]
    [, expr [ DESC | ASC ]
            [ NULLS { FIRST | LAST } ]
    ]...
  )
  [ OVER ( [query_partition_clause] ) ]
```

[LAST\_DAY](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00654)

```
LAST_DAY(date)
```

[LAST\_VALUE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00655)

```
LAST_VALUE
  { (expr) [ { RESPECT | IGNORE } NULLS ]
  | (expr [ { RESPECT | IGNORE } NULLS ])
  OVER (analytic_clause)
```

[LEAD](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00656)

```
LEAD
  { ( value_expr [, offset [, default]] ) [ { RESPECT | IGNORE } NULLS ] 
  | ( value_expr [ { RESPECT | IGNORE } NULLS ] [, offset [, default]] )
  }
  OVER ([ query_partition_clause ] order_by_clause)
```

[LEAST](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00657)

```
LEAST(expr [, expr ]...)
```

[LENGTH](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00658)

```
{ LENGTH
| LENGTHB
| LENGTHC
| LENGTH2
| LENGTH4
}
(char)
```

[LISTAGG](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF30030)

```
LISTAGG( [ALL | DISTINCT ] measure_expr 
           [, 'delimiter'] [listagg_overflow_clause] )
           [ WITHIN GROUP order_by_clause ]
           [OVER query_partition_clause]
```

[LN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00659)

```
LN(n)
```

[LNNVL](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06327)

```
LNNVL(condition)
```

[LOCALTIMESTAMP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00660)

```
LOCALTIMESTAMP [ (timestamp_precision) ]
```

[LOG](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00661)

```
LOG(n2, n1)
```

[LOWER](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00662)

```
LOWER(char)
```

[LPAD](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00663)

```
LPAD(expr1, n [, expr2 ])
```

[LTRIM](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00664)

```
LTRIM(char [, set ])
```

[MAKE\_REF](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00665)

```
MAKE_REF({ table | view } , key [, key ]...)
```

[MAX](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00666)

```
MAX([ DISTINCT | ALL ] expr) [ OVER (analytic_clause) ]
```

[MEDIAN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06315)

```
MEDIAN(expr) [ OVER (query_partition_clause) ]
```

[MIN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00667)

```
MIN([ DISTINCT | ALL ] expr) [ OVER (analytic_clause) ]
```

[MOD](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00668)

```
MOD(n2, n1)
```

[MONTHS\_BETWEEN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00669)

```
MONTHS_BETWEEN(date1, date2)
```

[NANVL](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06311)

```
NANVL(n2, n1)
```

[NCHR](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00670)

```
NCHR(number)
```

[NEW\_TIME](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00671)

```
NEW_TIME(date, timezone1, timezone2)
```

[NEXT\_DAY](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00672)

```
NEXT_DAY(date, char)
```

[NLS\_CHARSET\_DECL\_LEN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00673)

```
NLS_CHARSET_DECL_LEN(byte_count, char_set_id)
```

[NLS\_CHARSET\_ID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00674)

```
NLS_CHARSET_ID(string)
```

[NLS\_CHARSET\_NAME](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00675)

```
NLS_CHARSET_NAME(number)
```

[NLS\_COLLATION\_ID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-69EA3869-28E3-4CF8-9678-CD4F9878EE99)

```
NLS_COLLATION_ID(expr)
```

[NLS\_COLLATION\_NAME](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-24848987-2A02-4B09-A690-D3C87308FB3A)

```
NLS_COLLATION_NAME(expr [, flag ])
```

[NLS\_INITCAP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00676)

```
NLS_INITCAP(char [, 'nlsparam' ])
```

[NLS\_LOWER](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00677)

```
NLS_LOWER(char [, 'nlsparam' ])
```

[NLS\_UPPER](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00679)

```
NLS_UPPER(char [, 'nlsparam' ])
```

[NLSSORT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00678)

```
NLSSORT(char [, 'nlsparam' ])
```

[NTH\_VALUE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF30031)

```
NTH_VALUE(measure_expr, n)
  [ FROM { FIRST | LAST } ][ { RESPECT | IGNORE } NULLS ] 
  OVER (analytic_clause)
```

[NTILE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00680)

```
NTILE(expr) OVER ([ query_partition_clause ] order_by_clause)
```

[NULLIF](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00681)

```
NULLIF(expr1, expr2)
```

[NUMTODSINTERVAL](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00682)

```
NUMTODSINTERVAL(n, 'interval_unit')
```

[NUMTOYMINTERVAL](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00683)

```
NUMTOYMINTERVAL(n, 'interval_unit')
```

[NVL](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00684)

```
NVL(expr1, expr2)
```

[NVL2](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00685)

```
NVL2(expr1, expr2, expr3)
```

[ORA\_DM\_PARTITION\_NAME](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-F9ADE9AD-C306-42D1-8274-3F73C2FBAC19)

```
ORA_DM_PARTITION_NAME ( [ schema . ] model mining_attribute_clause )
```

[ORA\_DST\_AFFECTED](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF30032)

```
ORA_DST_AFFECTED(datetime_expr)
```

[ORA\_DST\_CONVERT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF30034)

```
ORA_DST_CONVERT(datetime_expr [, integer [, integer ]])
```

[ORA\_DST\_ERROR](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF30033)

```
ORA_DST_ERROR(datetime_expr)
```

[ORA\_HASH](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06313)

```
ORA_HASH(expr [, max_bucket [, seed_value ] ])
```

[ORA\_INVOKING\_USER](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55902)

```
ORA_INVOKING_USER
```

[ORA\_INVOKING\_USERID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55906)

```
ORA_INVOKING_USERID
```

[PATH](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06177)

```
PATH(correlation_integer)
```

[PERCENT\_RANK (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00686)

```
PERCENT_RANK(expr [, expr ]...) WITHIN GROUP
  (ORDER BY
   expr [ DESC | ASC ]
        [NULLS { FIRST | LAST } ]
   [, expr [ DESC | ASC ]
           [NULLS { FIRST | LAST } ]
   ]...
  )
```

[PERCENT\_RANK (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF51601)

```
PERCENT_RANK( )
   OVER ([ query_partition_clause ] order_by_clause)
```

[PERCENTILE\_CONT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00687)

```
PERCENTILE_CONT(expr) WITHIN GROUP
  (ORDER BY expr [ DESC | ASC ])
  [ OVER (query_partition_clause) ]
```

[PERCENTILE\_DISC](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00688)

```
PERCENTILE_DISC(expr) WITHIN GROUP
  (ORDER BY expr [ DESC | ASC ])
  [ OVER (query_partition_clause) ]
```

[POWER](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00689)

```
POWER(n2, n1)
```

[POWERMULTISET](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06306)

```
POWERMULTISET(expr)
```

[POWERMULTISET\_BY\_CARDINALITY](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06307)

```
POWERMULTISET_BY_CARDINALITY(expr, cardinality)
```

[PREDICTION (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06219)

```
PREDICTION ( [ grouping_hint ] [ schema . ] model
  [ cost_matrix_clause ] mining_attribute_clause )
```

[PREDICTION (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55757)

```
PREDICTION ( ( OF ANOMALY | FOR expr ) [ cost_matrix_clause ] mining_attribute_clause )
           OVER ( mining_analytic_clause )
```

[PREDICTION\_BOUNDS](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF20020)

```
PREDICTION_BOUNDS ( [schema.] model [, confidence_level [, class_value]]
                    mining_attribute_clause )
```

[PREDICTION\_COST (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06210)

```
PREDICTION_COST ( [ schema . ] model [ , class ] cost_matrix_clause mining_attribute_clause )
```

[PREDICTION\_COST (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55761)

```
PREDICTION_COST ( ( OF ANOMALY | FOR expr ) [ , class ]
                  cost_matrix_clause mining_attribute_clause )
                OVER (mining_analytic_clause)
```

[PREDICTION\_DETAILS (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06211)

```
PREDICTION_DETAILS ( [ schema . ] model 
                     [ , class_value [ , topN ] ] [ DESC | ASC | ABS ]
                     mining_attribute_clause )
```

[PREDICTION\_DETAILS (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55765)

```
PREDICTION_DETAILS ( ( OF ANOMALY | FOR expr ) [ , class_value [ , topN ] ]
                     [ DESC | ASC | ABS ] mining_attribute_clause )
                   OVER ( mining_analytic_clause )
```

[PREDICTION\_PROBABILITY (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06212)

```
PREDICTION_PROBABILITY ( [ schema . ] model [ , class ] mining_attribute_clause )
```

[PREDICTION\_PROBABILITY (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55769)

```
PREDICTION_PROBABILITY ( ( OF ANOMALY | FOR expr ) [ , class ]
                         mining_attribute_clause )
                       OVER (mining_analytic_clause )
```

[PREDICTION\_SET (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06233)

```
PREDICTION_SET ( [ schema . ] model [ , bestN [ , cutoff ] ] 
                 [ cost_matrix_clause ] mining_attribute_clause )
```

[PREDICTION\_SET (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55773)

```
PREDICTION_SET ( ( OF ANOMALY | FOR "expr" ) [ , bestN [ , cutoff ] ]
                 [ cost_matrix_clause ] mining_attribute_clause )
               OVER ( mining_analytic_clause )
```

[PRESENTNNV](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06178)

```
PRESENTNNV(cell_reference, expr1, expr2)
```

[PRESENTV](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06179)

```
PRESENTV(cell_reference, expr1, expr2)
```

[PREVIOUS](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06180)

```
PREVIOUS(cell_reference)
```

[RANK (aggregate)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00690)

```
RANK(expr [, expr ]...) WITHIN GROUP
   (ORDER BY
    expr [ DESC | ASC ]
         [ NULLS { FIRST | LAST } ]
    [, expr [ DESC | ASC ]
            [ NULLS { FIRST | LAST } ]
    ]...
   )
```

[RANK (analytic)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF51663)

```
RANK( )
   OVER ([ query_partition_clause ] order_by_clause)
```

[RATIO\_TO\_REPORT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00691)

```
RATIO_TO_REPORT(expr)
   OVER ([ query_partition_clause ])
```

[RAWTOHEX](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00692)

```
RAWTOHEX(raw)
```

[RAWTONHEX](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00693)

```
RAWTONHEX(raw)
```

[REF](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00694)

```
REF (correlation_variable)
```

[REFTOHEX](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00695)

```
REFTOHEX (expr)
```

[REGEXP\_COUNT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF20014)

```
REGEXP_COUNT (source_char, pattern [, position [, match_param]])
```

[REGEXP\_INSTR](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06300)

```
REGEXP_INSTR ( source_char, pattern
               [, position
                  [, occurrence
                     [, return_opt
                        [, match_param
                           [, subexpr ]
                        ]
                     ]
                  ]
               ]
             )
```

[REGEXP\_REPLACE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06302)

```
REGEXP_REPLACE ( source_char, pattern
                 [, replace_string
                    [, position
                       [, occurrence
                          [, match_param ]
                       ]
                    ]
                 ]
               )
```

[REGEXP\_SUBSTR](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06303)

```
REGEXP_SUBSTR ( source_char, pattern
                [, position
                   [, occurrence
                      [, match_param
                         [, subexpr ]
                      ]
                   ]
                ]
              )
```

[REGR\_AVGX](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00696), [REGR\_AVGY](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00696), [REGR\_COUNT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00696), [REGR\_INTERCEPT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00696), [REGR\_R2](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00696), [REGR\_SLOPE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00696), [REGR\_SXX](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00696), [REGR\_SXY](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00696), [REGR\_SYY](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00696)

```
{ REGR_SLOPE 
| REGR_INTERCEPT 
| REGR_COUNT 
| REGR_R2 
| REGR_AVGX
| REGR_AVGY 
| REGR_SXX 
| REGR_SYY 
| REGR_SXY
}
(expr1 , expr2)
[ OVER (analytic_clause) ]
```

[REMAINDER](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06312)

```
REMAINDER(n2, n1)
```

[REPLACE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00697)

```
REPLACE(char, search_string
        [, replacement_string ]
       )
```

[ROUND (date)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00699)

```
ROUND(date [, fmt ])
```

[ROUND (number)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00698)

```
ROUND(n [, integer ])
```

[ROUND\_TIES\_TO\_EVEN (number)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-49919B6B-4337-4812-A248-B5D98F102DBD)

```
ROUND_TIES_TO_EVEN ( n [, integer ] )
```

[ROW\_NUMBER](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06100)

```
ROW_NUMBER( )
   OVER ([ query_partition_clause ] order_by_clause)
```

[ROWIDTOCHAR](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06101)

```
ROWIDTOCHAR(rowid)
```

[ROWIDTONCHAR](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06102)

```
ROWIDTONCHAR(rowid)
```

[RPAD](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06103)

```
RPAD(expr1 , n [, expr2 ])
```

[RTRIM](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06104)

```
RTRIM(char [, set ])
```

[SCN\_TO\_TIMESTAMP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06325)

```
SCN_TO_TIMESTAMP(number)
```

[SESSIONTIMEZONE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06105)

```
SESSIONTIMEZONE
```

[SET](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06308)

```
SET (nested_table)
```

[SIGN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06106)

```
SIGN(n)
```

[SIN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06107)

```
SIN(n)
```

[SINH](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06108)

```
SINH(n)
```

[SKEWNESS\_POP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-DF34158F-B681-4933-BA27-0A3885A9F43C)

```
SKEWNESS_POP [ DISTINCT | ALL | UNIQUE ] ( expr )
```

[SKEWNESS\_SAMP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-E71D9AEC-0AAA-4A6C-BF70-29EE9AD8F7EC)

```
SKEWNESS_SAMP [DISTINCT | ALL | UNIQUE] ( expr )
```

[SOUNDEX](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06109)

```
SOUNDEX(char)
```

[SQRT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06110)

```
SQRT(n)
```

[STANDARD\_HASH](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55647)

```
STANDARD_HASH(expr [, 'method' ])
```

[STATS\_BINOMIAL\_TEST](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06316)

```
STATS_BINOMIAL_TEST(expr1, expr2, p
                    [, { TWO_SIDED_PROB
                       | EXACT_PROB
                       | ONE_SIDED_PROB_OR_MORE
                       | ONE_SIDED_PROB_OR_LESS
                       }
                    ]
                   )
```

[STATS\_CROSSTAB](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06317)

```
STATS_CROSSTAB(expr1, expr2
               [, { CHISQ_OBS
                  | CHISQ_SIG
                  | CHISQ_DF
                  | PHI_COEFFICIENT
                  | CRAMERS_V
                  | CONT_COEFFICIENT
                  | COHENS_K
                  }
               ]
              )
```

[STATS\_F\_TEST](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06318)

```
STATS_F_TEST(expr1, expr2
             [, { { STATISTIC
                  | DF_NUM
                  | DF_DEN
                  | ONE_SIDED_SIG
    } , expr3
                | TWO_SIDED_SIG
                }
             ]
            )
```

[STATS\_KS\_TEST](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06319)

```
STATS_KS_TEST(expr1, expr2
              [, { STATISTIC | SIG } ]
             )
```

[STATS\_MODE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06320)

```
STATS_MODE(expr)
```

[STATS\_MW\_TEST](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06321)

```
STATS_MW_TEST(expr1, expr2
              [, { STATISTIC
                 | U_STATISTIC
                 | ONE_SIDED_SIG , expr3
                 | TWO_SIDED_SIG
                 }
              ]
             )
```

[STATS\_ONE\_WAY\_ANOVA](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06322)

```
STATS_ONE_WAY_ANOVA(expr1, expr2
                    [, { SUM_SQUARES_BETWEEN
                       | SUM_SQUARES_WITHIN
                       | DF_BETWEEN
                       | DF_WITHIN
                       | MEAN_SQUARES_BETWEEN
                       | MEAN_SQUARES_WITHIN
                       | F_RATIO
                       | SIG
                       }
                    ]
                   )
```

[STATS\_T\_TEST\_INDEP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06323), [STATS\_T\_TEST\_INDEPU](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06323), [STATS\_T\_TEST\_ONE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06323), [STATS\_T\_TEST\_PAIRED](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06323)

```
{
  STATS_T_TEST_ONE ( expr1 [, expr2 ]
|
  { { STATS_T_TEST_PAIRED
    | STATS_T_TEST_INDEP
    | STATS_T_TEST_INDEPU
    } ( expr1, expr2
  }
}
[, { { STATISTIC | ONE_SIDED_SIG } , expr3 | TWO_SIDED_SIG | DF } ] )
```

[STATS\_WSR\_TEST](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06324)

```
STATS_WSR_TEST(expr1, expr2
               [, { STATISTIC
                  | ONE_SIDED_SIG
                  | TWO_SIDED_SIG
                  }
               ]
              )
```

[STDDEV](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06111)

```
STDDEV([ DISTINCT | ALL ] expr)
   [ OVER (analytic_clause) ]
```

[STDDEV\_POP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06112)

```
STDDEV_POP(expr)
   [ OVER (analytic_clause) ]
```

[STDDEV\_SAMP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06113)

```
STDDEV_SAMP(expr)
   [ OVER (analytic_clause) ]
```

[SUBSTR](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06114)

```
{ SUBSTR
| SUBSTRB
| SUBSTRC
| SUBSTR2
| SUBSTR4
}
(char, position [, substring_length ])
```

[SUM](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06115)

```
SUM([ DISTINCT | ALL ] expr)
   [ OVER (analytic_clause) ]
```

[SYS\_CONNECT\_BY\_PATH](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06116)

```
SYS_CONNECT_BY_PATH(column, char)
```

[SYS\_CONTEXT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06117)

```
SYS_CONTEXT('namespace', 'parameter' [, length ])
```

[SYS\_DBURIGEN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06118)

```
SYS_DBURIGEN({ column | attribute }
             [ rowid ]
               [, { column | attribute }
                  [ rowid ]
               ]...
             [, 'text ( )' ]
            )
```

[SYS\_EXTRACT\_UTC](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06119)

```
SYS_EXTRACT_UTC(datetime_with_timezone)
```

[SYS\_GUID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06120)

```
SYS_GUID( )
```

[SYS\_OP\_ZONE\_ID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF56848)

```
SYS_OP_ZONE_ID( [ [ schema. ] table. | t_alias. ] rowid [, scale ] )
```

[SYS\_TYPEID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06121)

```
SYS_TYPEID(object_type_value)
```

[SYS\_XMLAGG](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06122)

```
SYS_XMLAGG(expr [, fmt ])
```

[SYS\_XMLGEN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06123)

```
SYS_XMLGEN(expr [, fmt ])
```

[SYSDATE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06124)

```
SYSDATE
```

[SYSTIMESTAMP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06125)

```
SYSTIMESTAMP
```

[TAN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06126)

```
TAN(n)
```

[TANH](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06127)

```
TANH(n)
```

[TIMESTAMP\_TO\_SCN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06326)

```
TIMESTAMP_TO_SCN(timestamp)
```

[TO\_APPROX\_COUNT\_DISTINCT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF57369)

```
TO_APPROX_COUNT_DISTINCT(detail)
```

[TO\_APPROX\_PERCENTILE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF57373)

```
TO_APPROX_PERCENTILE(detail, expr, 'datatype'
  [, { 'DESC' | 'ASC' | 'ERROR_RATE' | 'CONFIDENCE' } ])
```

[TO\_BINARY\_DOUBLE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06309)

```
TO_BINARY_DOUBLE(expr [ DEFAULT return_value ON CONVERSION ERROR ]
  [, fmt [, 'nlsparam' ] ])
```

[TO\_BINARY\_FLOAT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06310)

```
TO_BINARY_FLOAT(expr [ DEFAULT return_value ON CONVERSION ERROR ]
  [, fmt [, 'nlsparam' ] ])
```

[TO\_BLOB (bfile)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-232A1599-53C9-464B-904F-4DBA336B4EBC)

```
TO_BLOB( bfile [, mime_type] )
```

[TO\_BLOB (raw)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF30029)

```
TO_BLOB( raw_value )
```

[TO\_CHAR (bfile|blob)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-F12F3C5A-8E3C-4FE1-BD7D-4AC0B79EA5A5)

```
TO_CHAR( { bfile | blob } [, csid] )
```

[TO\_CHAR (character)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06128)

```
TO_CHAR(nchar | clob | nclob)
```

[TO\_CHAR (datetime)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06129)

```
TO_CHAR({ datetime | interval } [, fmt [, 'nlsparam' ] ])
```

[TO\_CHAR (number)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06130)

```
TO_CHAR(n [, fmt [, 'nlsparam' ] ])
```

[TO\_CLOB (bfile|blob)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-FD7D58FE-B97C-4B75-85A9-5F82FB1DE96A)

```
TO_CLOB( { bfile | blob } [, csid] [, mime_type] )
```

[TO\_CLOB (character)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06131)

```
TO_CLOB(lob_column | char)
```

[TO\_DATE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06132)

```
TO_DATE(char [ DEFAULT return_value ON CONVERSION ERROR ]
  [, fmt [, 'nlsparam' ] ])
```

[TO\_DSINTERVAL](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06133)

```
TO_DSINTERVAL ( ' { sql_format | ds_iso_format } '
  [ DEFAULT return_value ON CONVERSION ERROR ] )
```

[TO\_LOB](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06134)

```
TO_LOB(long_column)
```

[TO\_MULTI\_BYTE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06135)

```
TO_MULTI_BYTE(char)
```

[TO\_NCHAR (character)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06136)

```
TO_NCHAR({char | clob | nclob})
```

[TO\_NCHAR (datetime)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06137)

```
TO_NCHAR({ datetime | interval }
         [, fmt [, 'nlsparam' ] ]
        )
```

[TO\_NCHAR (number)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06138)

```
TO_NCHAR(n [, fmt [, 'nlsparam' ] ])
```

[TO\_NCLOB](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06139)

```
TO_NCLOB(lob_column | char)
```

[TO\_NUMBER](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06140)

```
TO_NUMBER(expr [ DEFAULT return_value ON CONVERSION ERROR ]
  [, fmt [, 'nlsparam' ] ])
```

[TO\_SINGLE\_BYTE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06141)

```
TO_SINGLE_BYTE(char)
```

[TO\_TIMESTAMP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06142)

```
TO_TIMESTAMP(char [ DEFAULT return_value ON CONVERSION ERROR ]
  [, fmt [, 'nlsparam' ] ])
```

[TO\_TIMESTAMP\_TZ](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06143)

```
TO_TIMESTAMP_TZ(char [ DEFAULT return_value ON CONVERSION ERROR ]
  [, fmt [, 'nlsparam' ] ])
```

[TO\_UTC\_TIMESTAMP\_TZ](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-1728EE3E-EC0C-4FA8-B404-99C0A445CE82)

```
TO_UTC_TIMESTAMP_TZ ( varchar )
```

[TO\_YMINTERVAL](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06144)

```
TO_YMINTERVAL
  ( '  { [+|-] years - months 
       | ym_iso_format 
       } '
    [ DEFAULT return_value ON CONVERSION ERROR ]
  )
```

[TRANSLATE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06145)

```
TRANSLATE(expr, from_string, to_string)
```

[TRANSLATE... USING](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06146)

```
TRANSLATE ( char USING
          { CHAR_CS | NCHAR_CS }
          )
```

[TREAT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06148)

```
TREAT(expr AS ([ REF ] [ schema. ]type) | JSON )
```

[TRIM](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06149)

```
TRIM([ { { LEADING | TRAILING | BOTH }
         [ trim_character ]
       | trim_character
       }
       FROM 
     ]
     trim_source
    )
```

[TRUNC (date)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06151)

```
TRUNC(date [, fmt ])
```

[TRUNC (number)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06150)

```
TRUNC(n1 [, n2 ])
```

[TZ\_OFFSET](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06152)

```
TZ_OFFSET({ 'time_zone_name'
          | '{ + | - } hh : mi'
          | SESSIONTIMEZONE
          | DBTIMEZONE
          }
         )
```

[UID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06153)

```
UID
```

[UNISTR](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06154)

```
UNISTR( string )
```

[UPPER](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06155)

```
UPPER(char)
```

[USER](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06156)

```
USER
```

[user-defined function](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06181)

```
[ schema. ]
{ [ package. ]function | user_defined_operator }
[ @ dblink. ]
[ ( [ [ DISTINCT | ALL ] expr [, expr ]... ] ) ]
```

[USERENV](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06157)

```
USERENV('parameter')
```

[VALIDATE\_CONVERSION](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF57388)

```
VALIDATE_CONVERSION(expr AS type_name
  [, fmt [, 'nlsparam' ] ])
```

[VALUE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06158)

```
VALUE(correlation_variable)
```

[VAR\_POP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06159)

```
VAR_POP(expr) [ OVER (analytic_clause) ]
```

[VAR\_SAMP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06160)

```
VAR_SAMP(expr) [ OVER (analytic_clause) ]
```

[VARIANCE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06161)

```
VARIANCE([ DISTINCT | ALL ] expr)
        [ OVER (analytic_clause) ]
```

[VSIZE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06162)

```
VSIZE(expr)
```

[WIDTH\_BUCKET](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06163)

```
WIDTH_BUCKET
   (expr, min_value, max_value, num_buckets)
```

[XMLAGG](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06165)

```
XMLAGG(XMLType_instance [ order_by_clause ])
```

[XMLCAST](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF20012)

```
XMLCAST ( value_expression AS datatype )
```

[XMLCDATA](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06205)

```
XMLCDATA ( value_expr )
```

[XMLCOLATTVAL](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06166)

```
XMLCOLATTVAL
  (value_expr [ AS { c_alias  | EVALNAME value_expr } ]
    [, value_expr [ AS { c_alias  | EVALNAME value_expr } ]
      ]...
  )
```

[XMLCOMMENT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06206)

```
XMLCOMMENT ( value_expr )
```

[XMLCONCAT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06167)

```
XMLCONCAT(XMLType_instance [, XMLType_instance ]...)
```

[XMLDIFF](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF20025)

```
XMLDIFF ( XMLType_document, XMLType_document [ , integer, string ] )
```

[XMLELEMENT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06168)

```
XMLELEMENT ( [ ENTITYESCAPING | NOENTITYESCAPING ]
   { ( [ NAME ] identifier ) | ( EVALNAME value_expr ) }
   [ , XML_attributes_clause ]
   [ , value_expr [ [ AS ] c_alias ]]...
 )
```

[XMLEXISTS](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF20013)

```
XMLEXISTS ( XQuery_string [ XML_passing_clause ] )
```

[XMLFOREST](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06169)

```
XMLFOREST
  ( value_expr [ AS { c_alias | EVALNAME value_expr } ]
    [, value_expr [ AS { c_alias | EVALNAME value_expr } ]
      ]...
  )
```

[XMLISVALID](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06147)

```
XMLISVALID ( XMLType_instance [, XMLSchema_URL [, element ]] )
```

[XMLPARSE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06207)

```
XMLPARSE
  ({ DOCUMENT | CONTENT } value_expr [ WELLFORMED ]
  )
```

[XMLPATCH](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF20026)

```
XMLPATCH ( XMLType_document, XMLType_document )
```

[XMLPI](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06208)

```
XMLPI
 ( { ( [ NAME ] identifier ) | ( EVALNAME value_expr ) } 
     [ , value_expr ]
 )
```

[XMLQUERY](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06209)

```
XMLQUERY
 ( XQuery_string 
   [ XML_passing_clause ] 
   RETURNING CONTENT [NULL ON EMPTY] 
 )
```

[XMLSEQUENCE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06170)

```
XMLSEQUENCE( XMLType_instance
           | sys_refcursor_instance [, fmt ]
           )
```

[XMLSERIALIZE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06231)

```
XMLSERIALIZE
  ( { DOCUMENT | CONTENT } value_expr [ AS datatype ]
    [ ENCODING xml_encoding_spec ]
    [ VERSION string_literal ]
    [ NO INDENT | { INDENT [SIZE = number] } ]
    [ { HIDE | SHOW } DEFAULTS ]
  )
```

[XMLTABLE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06232)

```
XMLTABLE
 ( 
  [ XMLnamespaces_clause , ] XQuery_string XMLTABLE_options 
 )
```

[XMLTRANSFORM](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF06171)

```
XMLTRANSFORM(XMLType_instance, { XMLType_instance
                               | string
                               }
            )
```
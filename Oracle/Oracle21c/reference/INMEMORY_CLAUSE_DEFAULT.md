---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INMEMORY_CLAUSE_DEFAULT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.151 INMEMORY\_CLAUSE\_DEFAULT

`INMEMORY_CLAUSE_DEFAULT` enables you to specify a default In-Memory Column Store (IM column store) clause for new tables and materialized views.

Note:

The setting of his parameter has no effect on In-Memory external tables or hybrid partitioned tables.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `INMEMORY_CLAUSE_DEFAULT = '[INMEMORY] [NO INMEMORY] [other-clauses]` ' |
| Syntax | other-clauses::=  `[compression-clause] [priority-clause] [rac-clause]` |
| Syntax | compression-clause::=  `NO MEMCOMPRESS \| MEMCOMPRESS FOR { DML \| QUERY [ LOW \| HIGH ] \| CAPACITY [LOW \| HIGH] }` <sup>Foot 1</sup> |
| Syntax | priority-clause::=  `PRIORITY { LOW \| MEDIUM \| HIGH \| CRITICAL \| NONE }` <sup>Foot 1</sup> |
| Syntax | rac-clause::=  `[distribute-clause] [duplicate-clause]` <sup>Foot 1</sup> |
| Syntax | distribute-clause::=  `DISTRIBUTE [ AUTO \| BY ROWID RANGE ]` <sup>Foot 1</sup> |
| Syntax | duplicate-clause::=  `NO DUPLICATE \| DUPLICATE [ ALL ]` <sup>Foot 1</sup> |
| Default value | An empty string |
| Modifiable | `ALTER SESSION, ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | All instances should use the same value |

<sup>Footnote 1</sup> See Table 2-2 for more information about this clause.

If the `INMEMORY_CLAUSE_DEFAULT` parameter is unset or set to an empty string (the default), only tables and materialized views explicitly specified as `INMEMORY` will be populated into the IM column store. Setting the value of the `INMEMORY_CLAUSE_DEFAULT` parameter to `NO INMEMORY` has the same effect as setting it to the default value.

If the `INMEMORY_CLAUSE_DEFAULT` parameter is set, then any newly created table or materialized view specified as `INMEMORY` will inherit unspecified attributes from this parameter. This can force certain in-memory options by default that are not explicitly specified in the syntax. For example, if the `INMEMORY_CLAUSE_DEFAULT` parameter is set to `MEMCOMPRESS FOR CAPACITY LOW` and a table is created as `INMEMORY PRIORITY HIGH`, then the table is treated as if it was declared as `INMEMORY MEMCOMPRESS FOR CAPACITY LOW PRIORITY HIGH`.

If `INMEMORY` is specified as part of this parameter, then all newly created tables and materialized views will be populated into the IM column store, except tables and materialized views explicitly specified as `NO INMEMORY`. For example, if this parameter is set to `INMEMORY MEMCOMPRESS FOR CAPACITY HIGH`, then all new tables will be created as if this clause were present in the SQL `CREATE TABLE` statement. If there is a default `INMEMORY` value for the tablespace for a given segment, then it will override the value for this parameter.

Table 2-2 Meaning of INMEMORY\_CLAUSE\_DEFAULT Parameter Values

| Syntax | Description |
| --- | --- |
| `INMEMORY` | Specifies that all newly-created tables and materialized views populate the IM column store unless they are specified as `NO INMEMORY` in the SQL `CREATE TABLE` or `CREATE MATERIALIZED VIEW` statement |
| `NO INMEMORY` | Specifies that only tables and materialized views explicitly specified as `INMEMORY` in the SQL `CREATE TABLE` or `CREATE MATERIALIZED VIEW` statements populate the IM column store |
| `compression-clause` | Specifies that in-memory compression should be used for the instance. Use the `MEMCOMPRESS FOR` values to specify the in-memory compression level. |
| `NO MEMCOMPRESS` | When `NO MEMCOMPRESS` is specified, no in-memory compression is done in the IM column store. |
| `MEMCOMPRESS FOR` | `MEMCOMPRESS FOR` is used to indicate the in-memory compression level for the IM column store. |
| `DML` | When `DML` is specified, the IM column store is optimized for DML operations, and some lightweight in-memory compression may be done. |
| `QUERY` | When `QUERY` is specified, the in-memory compression level is for high performance. If `QUERY` is specified without `LOW` or `HIGH`, it defaults to `QUERY LOW`. |
| `QUERY LOW` | When `QUERY LOW` is specified, the in-memory compression level provides the highest performance. |
| `QUERY HIGH` | When `QUERY HIGH` is specified, the in-memory compression level provides a balance between compression and performance, weighted toward performance. |
| `CAPACITY` | When `CAPACITY` is specified without `LOW` or `HIGH`, it defaults to `CAPACITY LOW`. |
| `CAPACITY LOW` | When `CAPACITY LOW` is specified, the in-memory compression level is a balance between compression and performance, weighted toward capacity. |
| `CAPACITY HIGH` | When `CAPACITY HIGH` is specified, the in-memory compression level is for highest capacity. |
| `priority-clause` | Specifies the priority to use when populating tables in the IM column store. Use the `PRIORITY` values to specify the priority.  By default, the population of a table in the IM column store can be delayed until the database determines it is useful.  On database instance startup, tables are populated in priority order. |
| `PRIORITY NONE` | When `PRIORITY NONE` is specified, the population of a table in the IM column store can be delayed until the database determines it is useful.  This is the default value when no priority is specified. |
| `PRIORITY LOW` | When `PRIORITY LOW` is specified for a table or tables, the population of those tables in the IM column store is done before tables that have no priority specified. |
| `PRIORITY MEDIUM` | When `PRIORITY MEDIUM` is specified for a table or tables, the population of those tables in the IM column store is done before tables that have no priority and `PRIORITY LOW` specified. |
| `PRIORITY HIGH` | When `PRIORITY HIGH` is specified for a table or tables, the population of those tables in the IM column store is done before tables that have no priority, `PRIORITY LOW`, and `PRIORITY MEDIUM` specified. |
| `PRIORITY CRITICAL` | When `PRIORITY CRITICAL` is specified for a table or tables, the population of those tables in the IM column store is done before tables that have no priority, `PRIORITY LOW`, `PRIORITY MEDIUM`, and `PRIORITY HIGH` specified. |
| `rac-clause` | Specifies how tables in the IM column store will be managed among Oracle Real Application Clusters (Oracle RAC) instances. Use the `distribute-clause` and `duplicate-clause` to specify how tables in the IM store will be managed in Oracle RAC instances.  For a non-Oracle RAC database, these settings have no effect, because the whole table or partition has to be on the single instance. |
| `distribute-clause` | Specifies how a table is distributed among Oracle RAC instances. |
| `DISTRIBUTE AUTO` | Specifies that the database will automatically decide how to distribute tables in the IM column store across the Oracle RAC instances based on the type of partitioning and the value of the `duplicate-clause`.  `DISTRIBUTE AUTO` is the default, and it is also used when `DISTRIBUTE` is specified by itself. |
| `DISTRIBUTE BY ROWID RANGE` | Specifies that the tables in the IM column store will be distributed by rowid range to different Oracle RAC instances. |
| `duplicate-clause` | Specifies how many copies of each In-Memory Compression Unit (IMCU) of the tables in the IM column store will be spread across all the Oracle RAC instances.  Note: The `duplicate-clause` is only applicable if you are using Oracle Real Application Clusters (Oracle RAC) on an engineered system. Otherwise, the `duplicate-clause` is ignored and there is only one copy of each IMCU in memory. |
| `NO DUPLICATE` | Data is not duplicated across Oracle RAC instances. This is the default. |
| `DUPLICATE` | Data is duplicated on another Oracle RAC instance, resulting in data existing on a total of two Oracle RAC instances. |
| `DUPLICATE ALL` | Data is duplicated across all Oracle RAC instances. If you specify `DUPLICATE ALL`, then the database uses the `DISTRIBUTE AUTO` setting, regardless of whether or how you specify the `distribute-clause`. |

Examples

The following statement causes no tables to populate the IM column store:

```
alter system set INMEMORY_CLAUSE_DEFAULT='NO INMEMORY'
scope=both;
```

The following statement causes new tables and materialized views (except those specified as `NO INMEMORY`) to populate the IM column store at the high capacity compression level:

```
alter system set
INMEMORY_CLAUSE_DEFAULT='INMEMORY MEMCOMPRESS FOR CAPACITY HIGH'
scope=both;
```

The following statement causes new tables (even those specified as `NO INMEMORY`) to populate the IM column store at the highest performance compression level at `LOW` priority:

```
alter system set
INMEMORY_CLAUSE_DEFAULT='INMEMORY MEMCOMPRESS FOR QUERY LOW PRIORITY LOW'
scope=both;
```

The following statement causes new tables (even those specified as `NO INMEMORY`) to populate the IM column store without any in-memory compression:

```
alter system set
INMEMORY_CLAUSE_DEFAULT='INMEMORY NO MEMCOMPRESS'
scope=both;
```

The following statement causes tables in the IM column store to be duplicated on every Oracle RAC instance, unless on a non-engineered system. For a non-engineered system, the `duplicate-clause` (`DUPLICATE ALL`) will be ignored and tables in the column store will be automatically distributed across the Oracle RAC instance, with only one copy of each IMCU in the tables in the IM column store:

```
alter system set
INMEMORY_CLAUSE_DEFAULT='INMEMORY MEMCOMPRESS FOR QUERY
DISTRIBUTE AUTO DUPLICATE ALL'
scope=both;
```

The following statement sets the value of the `INMEMORY_CLAUSE_DEFAULT` parameter back to its default value, the empty string:

```
alter system set
INMEMORY_CLAUSE_DEFAULT=''
scope=both;
```

See Also:

- " [INMEMORY\_FORCE](INMEMORY_FORCE.md) "
- " [INMEMORY\_QUERY](INMEMORY_QUERY.md) "
- " [INMEMORY\_SIZE](INMEMORY_SIZE.md) "
- " [V$IM\_SEGMENTS](V-IM_SEGMENTS.md) "
- " [V$IM\_USER\_SEGMENTS](V-IM_USER_SEGMENTS.md) "
- " [QUERY\_REWRITE\_INTEGRITY](QUERY_REWRITE_INTEGRITY.md) "
- [Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=INMEM-GUID-BFA53515-7643-41E5-A296-654AB4A9F9E7) for an introduction to the IM column store
- [Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=INMEM-GUID-EEA265EE-8FBA-4457-8C3F-315B9EEA2224) for more information about the IM column store
- [Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=INMEM-GUID-1965B8FE-B34E-42D9-9E97-45D6579162A4) for more information on IM column store compression methods
- [Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=INMEM-GUID-B37DCA18-7CDA-425A-883B-036B70714F85) for more information on priority levels for populating a database object in the IM column store
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF01402) for more information on the CREATE TABLE statement
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF01302) for more information on the CREATE MATERIALIZED VIEW statement
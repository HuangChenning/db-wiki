---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_XSTREAM_ADM.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 221 DBMS\_XSTREAM\_ADM

This `DBMS_XSTREAM_ADM` package provides interfaces for streaming database changes between an Oracle database and other systems. XStream enables applications to stream out or stream in database changes.

This chapter contains the following topic:

See Also:

- [Oracle Database XStream Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=XSTRM)
- [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=LNOCI16769)
- [Oracle Database XStream Java API Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=STXJV)

### 221.1 DBMS\_XSTREAM\_ADM Overview

The package provides interfaces for configuring outbound servers that stream database changes from an Oracle database to other systems. The package also provides interfaces for configuring inbound servers that stream database changes from other systems to an Oracle database.

In both cases, the database changes are encapsulated in logical change records (LCRs). Also, the other systems can be Oracle systems or a non-Oracle systems, such as non-Oracle databases or file systems.

XStream outbound servers can stream out LCRs from an Oracle database programmatically using C or Java. After receiving the LCRs, the other system can process them in any customized way. For example, the other system can save the contents of the LCRs to a file, send the LCRs to an Oracle database through an XStream inbound server, or generate SQL statements and execute them on any Oracle or non-Oracle databases.

XStream inbound servers accept LCRs from another system and either apply them to an Oracle database or process them in a customized way using apply handlers.

XStream can be used in a multitenant container database (CDB). A CDB is an Oracle database that includes zero, one, or many user-created pluggable databases (PDBs).

See Also:

- [Oracle Database XStream Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=XSTRM)
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=CNCPT89233) for more information about CDBs and PDBs

### 221.2 DBMS\_XSTREAM\_ADM Security Model

To ensure that the user who runs the subprograms in this package has the necessary privileges, configure an XStream administrator and connect as the XStream administrator when using this package.

An administrator must be granted the `DBA` role when the administrator is performing any of the following actions:

- Running the `ADD_OUTBOUND` procedure while connected as a user that is different from the configured connect user for an outbound server
- Running the `ALTER_OUTBOUND` procedure to change the capture user for a capture process or the connect user for an outbound server
- Running the `CREATE_OUTBOUND` procedure, because this procedure creates a capture process
- Running the `ALTER_INBOUND` procedure to change the apply user for an inbound server
- Running the `ADD_INBOUND` procedure while connected as a user that is different from the configured apply user for an inbound server

When the administrator does not need to perform the preceding tasks, the `DBA` role is not required.

See Also:

- [GRANT\_ADMIN\_PRIVILEGE Procedure](DBMS_XSTREAM_AUTH.md)
- [Oracle Database XStream Guide, Chapter 4, "XStream Out and Security"](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=XSTRM1111) for more information about XStream and security.

### 221.3 DBMS\_XSTREAM\_ADM Operational Notes

Some subprograms in the `DBMS_APPLY_ADM` package can manage XStream outbound servers, and some subprograms in the `DBMS_APPLY_ADM` package can manage XStream inbound servers.

See Also:

[DBMS\_APPLY\_ADM](DBMS_APPLY_ADM.md) for details about which subprograms can manage outbound servers and inbound servers

### 221.4 Summary of DBMS\_XSTREAM\_ADM Subprograms

This table lists the `DBMS_XSTREAM_ADM` subprograms and briefly describes them.

Table 221-1 DBMS\_XSTREAM\_ADM Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_COLUMN Procedure | Either adds or removes a declarative rule-based transformation which adds a column to a row logical change record (row LCR) that satisfies the specified rule |
| ADD\_GLOBAL\_PROPAGATION\_RULES Procedure | Either adds global rules to the positive rule set for a propagation, or adds global rules to the negative rule set for a propagation, and creates the specified propagation if it does not exist |
| ADD\_GLOBAL\_RULES Procedure | Adds global rules to either the positive or negative rule set of a capture process or apply process, and creates the specified capture process or apply process if it does not exist |
| ADD\_OUTBOUND Procedure | Creates an XStream outbound server that dequeues LCRs from the specified queue |
| ADD\_SCHEMA\_PROPAGATION\_RULES Procedure | Either adds schema rules to the positive rule set for a propagation, or adds schema rules to the negative rule set for a propagation, and creates the specified propagation if it does not exist |
| ADD\_SCHEMA\_RULES Procedure | Adds rules to a rule set of XStream clients. |
| ADD\_SUBSET\_OUTBOUND\_RULES Procedure | Adds subset rules to an outbound server configuration |
| ADD\_SUBSET\_PROPAGATION\_RULES Procedure | Adds subset rules to the positive rule set for a propagation, and creates the specified propagation if it does not exist |
| ADD\_SUBSET\_RULES Procedure | Adds subset rules to the positive rule set of a capture process or apply process, and creates the specified capture process or apply process if it does not exist |
| ADD\_TABLE\_PROPAGATION\_RULES Procedure | Either adds table rules to the positive rule set for a propagation, or adds table rules to the negative rule set for a propagation, and creates the specified propagation if it does not exist |
| ADD\_TABLE\_RULES Procedure | This procedure adds rules to a rule set of an XStream client. |
| ALTER\_INBOUND Procedure | Modifies an XStream inbound server |
| ALTER\_OUTBOUND Procedure | Modifies an XStream outbound server |
| CREATE\_INBOUND Procedure | Creates an XStream inbound server and its queue |
| CREATE\_OUTBOUND Procedure | Creates an XStream outbound server, queue, and capture process to enable XStream client applications to stream out Oracle database changes encapsulated in LCRs |
| DELETE\_COLUMN Procedure | Either adds or removes a declarative rule-based transformation which deletes a column from a row LCR that satisfies the specified rule |
| DROP\_INBOUND Procedure | Removes an inbound server configuration |
| DROP\_OUTBOUND Procedure | Removes an outbound server configuration |
| ENABLE\_GG\_XSTREAM\_FOR\_STREAMS Procedure | Enables XStream performance optimizations for Oracle Replication components |
| GET\_MESSAGE\_TRACKING Function | Returns the tracking label for the current session |
| GET\_TAG Function | Gets the binary tag for all redo entries generated by the current session |
| IS\_GG\_XSTREAM\_FOR\_STREAMS Function | Returns `TRUE` if XStream performance optimizations are enabled for Oracle Replication components, or returns `FALSE` if XStream performance optimizations are disabled for Oracle Replication components |
| KEEP\_COLUMNS Procedure | Either adds or removes a declarative rule-based transformation which keeps a list of columns in a row LCR that satisfies the specified rule |
| MERGE\_STREAMS Procedure | Merges a stream flowing from one capture process with a stream flowing from another capture process |
| MERGE\_STREAMS\_JOB Procedure | Determines whether the original capture process and the cloned capture are within the specified merge threshold and, if they are, runs the `MERGE_STREAMS` procedure to merge the two streams |
| PURGE\_SOURCE\_CATALOG Procedure | Removes all Oracle Replication data dictionary information at the local database for the specified object |
| RECOVER\_OPERATION Procedure | Provides options for a split and merge operation that stopped because it encountered an error. This procedure either rolls forward the operation, rolls back the operation, or purges all of the metadata about the operation. |
| REMOVE\_QUEUE Procedure | Removes the specified `ANYDATA` queue |
| REMOVE\_RULE Procedure | Removes the specified rule or all rules from the rule set associated with the specified capture process, apply process, or propagation. |
| REMOVE\_SUBSET\_OUTBOUND\_RULES Procedure | Removes subset rules from an outbound server configuration |
| REMOVE\_XSTREAM\_CONFIGURATION Procedure | Removes the XStream configuration at the local database |
| RENAME\_COLUMN Procedure | Either adds or removes a declarative rule-based transformation which renames a column in a row LCR that satisfies the specified rule |
| RENAME\_SCHEMA Procedure | Either adds or removes a declarative rule-based transformation which renames a schema in a row LCR that satisfies the specified rule |
| RENAME\_TABLE Procedure | Either adds or removes a declarative rule-based transformation which renames a table in a row LCR that satisfies the specified rule |
| SET\_MESSAGE\_TRACKING Procedure | Sets the tracking label for logical change records (LCRs) produced by the current session |
| SET\_PARAMETER Procedure | Sets a parameter for an outbound server, an inbound server, or an outbound server's capture process |
| SET\_TAG Procedure | Sets the binary tag for all redo entries subsequently generated by the current session |
| SET\_UP\_QUEUE Procedure | Creates a queue table and a queue for use with the capture, propagate, and apply functionality of XStream |
| SPLIT\_STREAMS Procedure | Splits one stream flowing from a capture process off from all of the other streams flowing from the capture process |
| START\_OUTBOUND Procedure | Starts an XStream outbound server |
| STOP\_OUTBOUND Procedure | Stops an XStream outbound server |

Note:

All subprograms commit unless specified otherwise.

#### 221.4.1 ADD\_COLUMN Procedure

This procedure either adds or removes a declarative rule-based transformation which adds a column to a row logical change record (row LCR) that satisfies the specified rule.

For the transformation to be performed when the specified rule evaluates to `TRUE`, the rule must be in the positive rule set of an XStream client. XStream clients include capture processes, propagations, and apply processes.

This procedure is overloaded. The `column_value` and `column_function` parameters are mutually exclusive.

Note:

- `ADD_COLUMN` transformations cannot add columns of the following data types: `BLOB`, `CLOB`, `NCLOB`, `BFILE`, `LONG`, `LONG` `RAW`, `ROWID`, user-defined types (including object types, `REF` s, varrays, nested tables), and Oracle-supplied types (including any types, XML types, spatial types, and media types).
- Declarative transformations can transform row LCRs only. Therefore, a DML rule must be specified when you run this procedure. If a DDL rule is specified, then the procedure raises an error.

See Also:

[Oracle Database XStream Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=XSTRM72752) for more information about declarative rule-based transformations

Syntax

```
DBMS_XSTREAM_ADM.ADD_COLUMN(
   rule_name     IN  VARCHAR2,
   table_name    IN  VARCHAR2,
   column_name   IN  VARCHAR2,
   column_value  IN  ANYDATA,
   value_type    IN  VARCHAR2     DEFAULT 'NEW',
   step_number   IN  NUMBER       DEFAULT 0,
   operation     IN  VARCHAR2     DEFAULT 'ADD');
```
```
DBMS_XSTREAM_ADM.ADD_COLUMN(
   rule_name        IN  VARCHAR2,
   table_name       IN  VARCHAR2,
   column_name      IN  VARCHAR2,
   column_function  IN  VARCHAR2,
   value_type       IN  VARCHAR2     DEFAULT 'NEW',
   step_number      IN  NUMBER       DEFAULT 0,
   operation        IN  VARCHAR2     DEFAULT 'ADD');
```

Parameters

Table 221-2 ADD\_COLUMN Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_name` | The name of the rule, specified as `[``schema_name``.]` `rule_name`. If `NULL`, then the procedure raises an error.  For example, to specify a rule in the `hr` schema named `employees12`, enter `hr.employees12`. If the schema is not specified, then the current user is the default. |
| `table_name` | The name of the table to which the column is added in the row LCR, specified as `[``schema_name``.]` `object_name`. For example, `hr.employees`. If the schema is not specified, then the current user is the default. |
| `column_name` | The name of the column added to each row LCR that satisfies the rule. |
| `column_value` | The value of the added column. Specify the appropriate `ANYDATA` function for the column datatype and the column value. For example, if the datatype of the column being added is `NUMBER` and the value is `NULL`, then specify the `ANYDATA.ConvertNumber(NULL)` function.  This parameter cannot be specified if the `column_function` parameter is specified. |
| `column_function` | Either the `'SYSDATE'` or the `'SYSTIMESTAMP'` SQL function.  The `'SYSDATE'` SQL function places the current date and time set for the operating system on which the database resides. The datatype of the returned value is `DATE`, and the format returned depends on the value of the `NLS_DATE_FORMAT` initialization parameter.  The `'SYSTIMESTAMP'` SQL function returns the system date, including fractional seconds and time zone, of the system on which the database resides. The return type is `TIMESTAMP` `WITH` `TIME` `ZONE`.  The function executes when the rule evaluates to `TRUE`.  This parameter cannot be specified if the `column_value` parameter is specified. |
| `value_type` | Specify `'NEW'` to add the column to the new values in the row LCR.  Specify `'OLD'` to add the column to the old values in the row LCR. |
| `step_number` | The order of execution of the transformation.  See Also: [Oracle Database XStream Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=XSTRM72754) for more information about transformation ordering |
| `operation` | Specify `'ADD'` to add the transformation to the rule.  Specify `'REMOVE'` to remove the transformation from the rule. |

Usage Notes

When `'REMOVE'` is specified for the `operation` parameter, all of the add column declarative rule-based transformations for the specified rule are removed that match the specified `table_name`, `column_name`, and `step_number` parameters. Nulls specified for these parameters act as wildcards. The following table lists the behavior of the `ADD_COLUMN` procedures when one or more of these parameters is `NULL`:

| table\_name | column\_name | step\_number | Result |
| --- | --- | --- | --- |
| `NULL` | `NULL` | `NULL` | Remove all add column transformations for the specified rule. |
| `NULL` | `NULL` | non- `NULL` | Remove all add column transformations with the specified `step_number` for the specified rule. |
| `NULL` | non- `NULL` | non- `NULL` | Remove all add column transformations with the specified `column_name` and `step_number` for the specified rule. |
| non- `NULL` | `NULL` | `non-NULL` | Remove all add column transformations with the specified `table_name` and `step_number` for the specified rule. |
| `NULL` | `non-NULL` | `NULL` | Remove all add column transformations with the specified `column_name` for the specified rule. |
| non- `NULL` | non- `NULL` | `NULL` | Remove all add column transformations with the specified `table_name` and `column_name` for the specified rule. |
| non- `NULL` | `NULL` | `NULL` | Remove all add column transformations with the specified `table_name` for the specified rule. |
| non- `NULL` | non- `NULL` | non- `NULL` | Remove all add column transformations with the specified `table_name`, `column_name`, and `step_number` for the specified rule. |

#### 221.4.2 ADD\_GLOBAL\_PROPAGATION\_RULES Procedure

This procedure either adds global rules to the positive rule set for a propagation, or adds global rules to the negative rule set for a propagation, and creates the specified propagation if it does not exist.

This procedure is overloaded. One version of this procedure contains two `OUT` parameters, and the other does not.

Syntax

```
DBMS_XSTREAM_ADM.ADD_GLOBAL_PROPAGATION_RULES(
   streams_name            IN   VARCHAR2  DEFAULT NULL,
   source_queue_name       IN   VARCHAR2,
   destination_queue_name  IN   VARCHAR2,
   include_dml             IN   BOOLEAN   DEFAULT TRUE,
   include_ddl             IN   BOOLEAN   DEFAULT FALSE,
   include_tagged_lcr      IN   BOOLEAN   DEFAULT FALSE,
   source_database         IN   VARCHAR2  DEFAULT NULL,
   dml_rule_name           OUT  VARCHAR2,
   ddl_rule_name           OUT  VARCHAR2,
   inclusion_rule          IN   BOOLEAN   DEFAULT TRUE,
   and_condition           IN   VARCHAR2  DEFAULT NULL,
   queue_to_queue          IN   BOOLEAN   DEFAULT NULL);

DBMS_XSTREAM_ADM.ADD_GLOBAL_PROPAGATION_RULES(
   streams_name            IN   VARCHAR2  DEFAULT NULL,
   source_queue_name       IN   VARCHAR2,
   destination_queue_name  IN   VARCHAR2,
   include_dml             IN   BOOLEAN   DEFAULT TRUE,
   include_ddl             IN   BOOLEAN   DEFAULT FALSE,
   include_tagged_lcr      IN   BOOLEAN   DEFAULT FALSE,
   source_database         IN   VARCHAR2  DEFAULT NULL,
   inclusion_rule          IN   BOOLEAN   DEFAULT TRUE,
   and_condition           IN   VARCHAR2  DEFAULT NULL,
   queue_to_queue          IN   BOOLEAN   DEFAULT NULL);
```

Parameters

Table 221-3 ADD\_GLOBAL\_PROPAGATION\_RULES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `streams_name` | The name of the propagation. Do not specify an owner.  If the specified propagation does not exist, then the procedure creates it automatically.  If `NULL` and a propagation exists for the same source queue and destination queue (including database link), then the procedure uses this propagation.  If `NULL` and no propagation exists for the same source queue and destination queue (including database link), then the procedure creates a propagation automatically with a system-generated name. |
| `source_queue_name` | The name of the source queue, specified as `[``schema_name``.]` `queue_name`. The current database must contain the source queue, and the queue must be `ANYDATA` type.  For example, to specify a source queue named `streams_queue` in the `strmadmin` schema, enter `strmadmin.streams_queue` for this parameter.  If the schema is not specified, then the current user is the default. |
| `destination_queue_name` | The name of the destination queue, including a database link, specified as `[``schema_name``.]` `queue_name` `[``@dblink_name``]`, if the destination queue is in a remote database. The queue must be `ANYDATA` type.  For example, to specify a destination queue named `streams_queue` in the `strmadmin` schema and use a database link named `dbs2.net`, enter `strmadmin.streams_queue@dbs2.net` for this parameter.  If the schema is not specified, then the current user is the default.  If the database link is omitted, then the procedure uses the global name of the current database, and the source queue and destination queue must be in the same database.  Note: Connection qualifiers are not allowed. |
| `include_dml` | If `TRUE`, then the procedure creates a rule for DML changes. If `FALSE`, then the procedure does not create a DML rule. `NULL` is not permitted. |
| `include_ddl` | If `TRUE`, then the procedure creates a rule for DDL changes. If `FALSE`, then the procedure does not create a DDL rule. `NULL` is not permitted. |
| `include_tagged_lcr` | If `TRUE`, then the procedure does not add a condition regarding Oracle Replication tags to the generated rules. Therefore, these rules can evaluate to `TRUE` regardless of whether a logical change record (LCR) has a non- `NULL` tag. If the rules are added to the positive rule set for the propagation, then an LCR is always considered for propagation, regardless of whether it has a non- `NULL` tag. If the rules are added to a positive rule set, then setting this parameter to `TRUE` is appropriate for a full (for example, standby) copy of a database. If the rules are added to the negative rule set for the propagation, then whether an LCR is discarded does not depend on the tag for the LCR.  If `FALSE`, then the procedure adds a condition to each generated rule that causes the rule to evaluate to `TRUE` only if an LCR has a `NULL` Oracle Replication tag. If the rules are added to the positive rule set for the propagation, then an LCR is considered for propagation only when the LCR contains a `NULL` tag. If the rules are added to a positive rule set, then setting this parameter to `FALSE` might be appropriate in update-anywhere configurations to avoid sending a change back to its source database. If the rules are added to the negative rule set for the propagation, then an LCR can be discarded only if it has a `NULL` tag.  Usually, specify `TRUE` for this parameter if the `inclusion_rule` parameter is set to `FALSE`. |
| `source_database` | The global name of the source database. The source database is where the changes originated. If `NULL`, then the procedure does not add a condition regarding the source database to the generated rules.  If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify `DBS1` and the domain is `.NET`, then the procedure specifies `DBS1.NET` automatically.  Oracle recommends that you specify a source database for propagation rules. |
| `dml_rule_name` | If `include_dml` is `TRUE`, then this parameter contains the DML rule name.  If `include_dml` is `FALSE`, then this parameter contains a `NULL`. |
| `ddl_rule_name` | If `include_ddl` is `TRUE`, then this parameter contains the DDL rule name.  If `include_ddl` is `FALSE`, then this parameter contains a `NULL`. |
| `inclusion_rule` | If `inclusion_rule` is `TRUE`, then the procedure adds the rules to the positive rule set for the propagation.  If `inclusion_rule` is `FALSE`, then the procedure adds the rules to the negative rule set for the propagation.  In either case, the system creates the rule set if it does not exist. |
| `and_condition` | If non- `NULL`, appends the specified condition to the system-generated rule condition using an `AND` clause in the following way:  ``` (system_condition) AND (and_condition) ```  The variable in the specified condition must be `:lcr`. For example, to specify that the global rules generated by the procedure evaluate to `TRUE` only if the Oracle Replication tag is the hexadecimal equivalent of `'02'`, specify the following condition:  ``` :lcr.get_tag() = HEXTORAW(''02'') ```  The `:lcr` in the specified condition is converted to `:dml` or `:ddl`, depending on the rule that is being generated. If you are specifying an LCR member subprogram that is dependent on the LCR type (row or DDL), then make sure the procedure only generates the appropriate rule.  Specifically, if you specify an LCR member subprogram that is valid only for row LCRs, then specify `TRUE` for the `include_dml` parameter and `FALSE` for the `include_ddl` parameter. If you specify an LCR member subprogram that is valid only for DDL LCRs, then specify `FALSE` for the `include_dml` parameter and `TRUE` for the `include_ddl` parameter.  See Also: [Logical Change Record TYPEs](Logical-Change-Record-TYPEs.md) |
| `queue_to_queue` | If `TRUE` or `NULL`, then a new propagation created by this procedure is a queue to queue propagation. A queue-to-queue propagation always has its own propagation job and uses a service for automatic failover when the destination queue is a buffered queue in an Oracle Real Application Clusters (Oracle RAC) database.  If `FALSE`, then a new propagation created by this procedure is a queue-to-dblink propagation. A queue-to-dblink propagation can share a propagation job with other propagations that use the same database link and does not support automatic failover in an Oracle RAC environment.  The procedure cannot change the queue to queue property of an exiting propagation. If the specified propagation exists, then the procedure behaves in the following way for each setting:  - If `TRUE` and the specified propagation is not a queue to queue propagation, then the procedure raises an error. - If `FALSE` and the specified propagation is a queue to queue propagation, then the procedure raises an error. - If `NULL`, then the procedure does not change the queue to queue property of the propagation. |

Usage Notes

This procedure configures propagation using the current user. Only one propagation is allowed between a particular source queue and destination queue.

This procedure creates DML and DDL rules automatically based on `include_dml` and `include_ddl` parameter values, respectively. Each rule has a system-generated rule name that consists of the database name with a sequence number appended to it. The sequence number is used to avoid naming conflicts. If the database name plus the sequence number is too long, then the database name is truncated. A propagation uses the rules for filtering.

Examples

The following is an example of a global rule condition created for DML changes:

```
(:dml.is_null_tag() = 'Y' and :dml.get_source_database_name() = 'DBS1.NET' )
```

#### 221.4.3 ADD\_GLOBAL\_RULES Procedure

This procedure adds rules to an XStream clients rule set.

It adds rules to a rule set of one of the following types of XStream clients:

- When the `streams_type` parameter is set to `capture`, this procedure adds capture process rules for capturing changes to an entire database.
	This procedure creates the specified capture process if it does not exist.
- When the `streams_type` parameter is set to `apply` and the `streams_name` parameter specifies the name of an apply process, outbound server, or inbound server, this procedure adds apply rules for applying all logical change records (LCRs) it receives. The rules can specify that the LCRs must be from a particular source database.
	This procedure creates an apply process if no apply process, outbound server, or inbound server exists with the specified `streams_name`. This procedure can add rules to an outbound server or inbound server, but it cannot create an outbound server or inbound server.

This procedure is overloaded. One version of this procedure contains two `OUT` parameters, and the other does not.

Note:

If you add global rules to the positive rule set for a capture process, then make sure you add rules to the negative capture process rule set to exclude database objects that are not supported by Oracle Replication. Query the `DBA_XSTREAM_OUT_SUPPORT_MODE` data dictionary view to determine which database objects are not supported by Oracle Replication. If unsupported database objects are not excluded, then capture errors will result.

Syntax

```
DBMS_XSTREAM_ADM.ADD_GLOBAL_RULES(
   streams_type           IN   VARCHAR2,
   streams_name           IN   VARCHAR2  DEFAULT NULL,
   queue_name             IN   VARCHAR2  DEFAULT 'streams_queue',
   include_dml            IN   BOOLEAN   DEFAULT TRUE,
   include_ddl            IN   BOOLEAN   DEFAULT FALSE,
   include_tagged_lcr     IN   BOOLEAN   DEFAULT FALSE,
   source_database        IN   VARCHAR2  DEFAULT NULL,
   dml_rule_name          OUT  VARCHAR2,
   ddl_rule_name          OUT  VARCHAR2,
   inclusion_rule         IN   BOOLEAN   DEFAULT TRUE,
   and_condition          IN   VARCHAR2  DEFAULT NULL,
   source_root_name       IN   VARCHAR2  DEFAULT NULL,
   source_container_name  IN   VARCHAR2  DEFAULT NULL);

DBMS_XSTREAM_ADM.ADD_GLOBAL_RULES(
   streams_type           IN   VARCHAR2,
   streams_name           IN   VARCHAR2  DEFAULT NULL,
   queue_name             IN   VARCHAR2  DEFAULT 'streams_queue',
   include_dml            IN   BOOLEAN   DEFAULT TRUE,
   include_ddl            IN   BOOLEAN   DEFAULT FALSE,
   include_tagged_lcr     IN   BOOLEAN   DEFAULT FALSE,
   source_database        IN   VARCHAR2  DEFAULT NULL,
   inclusion_rule         IN   BOOLEAN   DEFAULT TRUE,
   and_condition          IN   VARCHAR2  DEFAULT NULL,
   source_root_name       IN   VARCHAR2  DEFAULT NULL,
   source_container_name  IN   VARCHAR2  DEFAULT NULL);
```

Parameters

Table 221-4 ADD\_GLOBAL\_RULES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `streams_type` | The type of XStream client:  - Specify `capture` for a capture process. - Specify `apply` for an apply process. |
| `streams_name` | The name of the capture process or apply process. Do not specify an owner.  If `NULL`, if `streams_type` is `capture`, and if one relevant capture process for the queue exists, then the relevant XStream client is used. If no relevant XStream client exists for the queue, then an XStream client is created automatically with a system-generated name. If `NULL` and multiple XStream clients of the specified `streams_type` for the queue exist, then the procedure raises an error.  If `NULL`, if `streams_type` is `apply`, and if one relevant apply process exists, then the procedure uses the relevant apply process. The relevant apply process is identified in one of the following ways:  - If one existing apply process has the source database specified in `source_database` and uses the queue specified in `queue_name`, then the procedure uses this apply process. - If `source_database` is `NULL` and one existing apply process is using the queue specified in `queue_name`, then the procedure uses this apply process.  If `NULL` and no relevant apply process exists, then the procedure creates an apply process automatically with a system-generated name.  If `NULL` and multiple relevant apply processes exist, then the procedure raises an error.  Each apply process must have a unique name. |
| `queue_name` | The name of the local queue, specified as `[``schema_name``.]` `queue_name`. The current database must contain the queue, and the queue must be `ANYDATA` type.  For example, to specify a queue named `streams_queue` in the `strmadmin` schema, enter `strmadmin.streams_queue` for this parameter. If the schema is not specified, then the current user is the default.  For capture process rules, this is the queue into which a capture process enqueues LCRs. For outbound server rules, this is the queue from which the outbound server dequeues LCRs. For inbound server rules, this is the queue into which an inbound server enqueues error transactions. |
| `include_dml` | If `TRUE`, then the procedure creates a rule for DML changes. If `FALSE`, then the procedure does not create a DML rule. `NULL` is not permitted. |
| `include_ddl` | If `TRUE`, then the procedure creates a rule for DDL changes. If `FALSE`, then the procedure does not create a DDL rule. `NULL` is not permitted. |
| `include_tagged_lcr` | If `TRUE`, then the procedure does not add a condition regarding Oracle Replication tags to the generated rules. Therefore, these rules can evaluate to `TRUE` regardless of whether a redo entry or LCR has a non- `NULL` tag. If the rules are added to the positive rule set for the process, then a redo entry is always considered for capture, and an LCR is always considered for apply, regardless of whether the redo entry or LCR has a non- `NULL` tag. If the rules are added to a positive rule set, then setting this parameter to `TRUE` is appropriate for a full (for example, standby) copy of a database. If the rules are added to the negative rule set for the process, then whether a redo entry or LCR is discarded does not depend on the tag.  If `FALSE`, then the procedure adds a condition to each generated rule that causes the rule to evaluate to `TRUE` only if a redo entry or LCR has a `NULL` Oracle Replication tag. If the rules are added to the positive rule set for the process, then a redo entry is considered for capture, and an LCR is considered for apply, only when the redo entry or LCR contains a `NULL` tag. If the rules are added to a positive rule set, then setting this parameter to `FALSE` might be appropriate in update-anywhere configurations to avoid sending a change back to its source database. If the rules are added to the negative rule set for the process, then a redo entry or LCR can be discarded only if it has a `NULL` tag.  Usually, specify `TRUE` for this parameter if the `inclusion_rule` parameter is set to `FALSE`. |
| `source_database` | The global name of the source database. If `NULL`, then the procedure does not add a condition regarding the source database to the generated rules.  For capture process rules, specify `NULL` or the global name of the local database if you are creating a capture process locally at the source database. If you are adding rules to a downstream capture process rule set at a downstream database, then specify the source database of the changes that will be captured.  For apply process rules, specify the source database of the changes that will be applied by the apply process. The source database is the database where the changes originated. If an apply process applies captured LCRs, then the apply process can apply LCRs from only one capture process at one source database.  In a CDB, specify the global name of the container to which the rules pertain. The container can be the root or a PDB. For example, `mycdb.example.com` or `hrpdb.example.com`. See [Oracle Database XStream Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=XSTRM72988) for more information about setting this parameter in a CDB.  If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify `DBS1` and the domain is `.NET`, then the procedure specifies `DBS1.NET` automatically. |
| `dml_rule_name` | If `include_dml` is `TRUE`, then this parameter contains the DML rule name.  If `include_dml` is `FALSE`, then this parameter contains a `NULL`. |
| `ddl_rule_name` | If `include_ddl` is `TRUE`, then this parameter contains the DDL rule name.  If `include_ddl` is `FALSE`, then this parameter contains a `NULL`. |
| `inclusion_rule` | If `inclusion_rule` is `TRUE`, then the procedure adds the rules to the positive rule set for the XStream client.  If `inclusion_rule` is `FALSE`, then the procedure adds the rules to the negative rule set for the XStream client.  In either case, the system creates the rule set if it does not exist. |
| `and_condition` | If non- `NULL`, appends the specified condition to the system-generated rule condition using an `AND` clause in the following way:  ``` (system_condition) AND (and_condition) ```  The variable in the specified condition must be `:lcr`. For example, to specify that the global rules generated by the procedure evaluate to `TRUE` only if the Oracle Replication tag is the hexadecimal equivalent of `'02'`, specify the following condition:  ``` :lcr.get_tag() = HEXTORAW(''02'') ```  The `:lcr` in the specified condition is converted to `:dml` or `:ddl`, depending on the rule that is being generated. If you are specifying an LCR member subprogram that is dependent on the LCR type (row or DDL), then make sure this procedure only generates the appropriate rule.  Specifically, if you specify an LCR member subprogram that is valid only for row LCRs, then specify `TRUE` for the `include_dml` parameter and `FALSE` for the `include_ddl` parameter. If you specify an LCR member subprogram that is valid only for DDL LCRs, then specify `FALSE` for the `include_dml` parameter and `TRUE` for the `include_ddl` parameter.  See Also: [Logical Change Record TYPEs](Logical-Change-Record-TYPEs.md) |
| `source_root_name` | The global name of the root in the source CDB. For example, `mycdb.example.com`.  If this parameter is `NULL`, then the global name of the root in the local CDB is used. If you are configuring downstream capture, then this parameter must be a non- `NULL` value, and it must specify the global name of the root in the remote source CDB. See [Oracle Database XStream Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=XSTRM72988) for more information about setting this parameter in a CDB.  If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify `DBS1` and the domain is `EXAMPLE.COM`, then the procedure specifies `DBS1.EXAMPLE.COM` automatically.  Note: This parameter only applies to a CDB. |
| `source_container_name` | The short name of the source container. The container can be the root or a PDB. For example, `CDB$ROOT` or `hrpdb`. See [Oracle Database XStream Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=XSTRM72988) for more information about setting this parameter in a CDB.  Note: This parameter only applies to a CDB. |

Usage Notes

This procedure creates DML and DDL rules automatically based on `include_dml` and `include_ddl` parameter values, respectively. Each rule has a system-generated rule name that consists of the database name with a sequence number appended to it. The sequence number is used to avoid naming conflicts. If the database name plus the sequence number is too long, then the database name is truncated. A capture process or apply process uses the rules for filtering.

See Also:

- " Operational Notes "
- " Security Model "

Examples

The following is an example of a global rule condition created for DML changes:

```
(:dml.is_null_tag() = 'Y' and :dml.get_source_database_name() = 'DBS1.NET' )
```

#### 221.4.4 ADD\_OUTBOUND Procedure

This procedure creates an XStream outbound server that dequeues LCRs from the specified queue. The outbound server streams out the LCRs to an XStream client application.

This procedure creates neither a capture process nor a queue. To create an outbound server, a capture process, and a queue with one procedure call, use the CREATE\_OUTBOUND Procedure.

To create the capture process individually, use one of the following packages:

- `DBMS_XSTREAM_ADM`
- `DBMS_CAPTURE_ADM`

To create a queue individually, use the `SET_UP_QUEUE` procedure in the `DBMS_XSTREAM_ADM` package.

This procedure is overloaded. One `table_names` parameter is type `VARCHAR2` and the other `table_names` parameter is type `DBMS_UTILITY.UNCL_ARRAY`. Also, one `schema_names` parameter is type `VARCHAR2` and the other `schema_names` parameter is type `DBMS_UTILITY.UNCL_ARRAY`. These parameters enable you to enter the lists of tables and schemas in different ways and are mutually exclusive.

Note:

- A client application can create multiple sessions. Each session can attach to only one outbound server, and each outbound server can serve only one session at a time. However, different client application sessions can connect to different outbound servers. See [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=LNOCI) and [Oracle Database XStream Java API Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=STXJV) for information about attaching to an outbound server.
- This procedure enables the outbound server that it creates.
- Starting with Oracle Database 11g Release 2 (11.2.0.2), the `capture_name`, `start_scn`, and `start_time` parameters are included in this procedure.

Syntax

```
DBMS_XSTREAM_ADM.ADD_OUTBOUND(
   server_name            IN  VARCHAR2,
   queue_name             IN  VARCHAR2   DEFAULT NULL,
   source_database        IN  VARCHAR2   DEFAULT NULL,
   table_names            IN  DBMS_UTILITY.UNCL_ARRAY,
   schema_names           IN  DBMS_UTILITY.UNCL_ARRAY,
   connect_user           IN  VARCHAR2   DEFAULT NULL,
   comment                IN  VARCHAR2   DEFAULT NULL,
   capture_name           IN  VARCHAR2   DEFAULT NULL,
   start_scn              IN  NUMBER     DEFAULT NULL,
   start_time             IN  TIMESTAMP  DEFAULT NULL,
   include_dml            IN  BOOLEAN   DEFAULT TRUE,
   include_ddl            IN  BOOLEAN   DEFAULT FALSE,
   source_root_name       IN  VARCHAR2  DEFAULT NULL,
   source_container_name  IN  VARCHAR2  DEFAULT NULL,
   lcrid_version          IN  NUMBER    DEFAULT NULL);

DBMS_XSTREAM_ADM.ADD_OUTBOUND(
   server_name            IN  VARCHAR2,
   queue_name             IN  VARCHAR2   DEFAULT NULL,
   source_database        IN  VARCHAR2   DEFAULT NULL,
   table_names            IN  VARCHAR2   DEFAULT NULL,
   schema_names           IN  VARCHAR2   DEFAULT NULL,
   connect_user           IN  VARCHAR2   DEFAULT NULL,
   comment                IN  VARCHAR2   DEFAULT NULL,
   capture_name           IN  VARCHAR2   DEFAULT NULL,
   start_scn              IN  NUMBER     DEFAULT NULL,
   start_time             IN  TIMESTAMP  DEFAULT NULL,
   include_dml            IN  BOOLEAN   DEFAULT TRUE,
   include_ddl            IN  BOOLEAN   DEFAULT FALSE,
   source_root_name       IN  VARCHAR2  DEFAULT NULL,
   source_container_name  IN  VARCHAR2  DEFAULT NULL,
   lcrid_version          IN  NUMBER    DEFAULT NULL);
```

Parameters

Table 221-5 ADD\_OUTBOUND Procedure Parameters

| Parameter | Description |
| --- | --- |
| `server_name` | The name of the outbound server being created. A `NULL` specification is not allowed. Do not specify an owner.  The specified name must not match the name of an existing outbound server, inbound server, apply process, or messaging client.  Note: The `server_name` setting cannot exceed 30 bytes, and it cannot be altered after the outbound server is created. |
| `queue_name` | The name of the local queue from which the outbound server dequeues LCRs, specified as `[``schema_name``.]` `queue_name`. The current database must contain the queue, and the queue must be `ANYDATA` type.  For example, to specify a queue named `xstream_queue` in the `xstrmadmin` schema, enter `xstrmadmin.xstream_queue` for this parameter. If the schema is not specified, then the current user is the default.  If `NULL`, the procedure raises an error. |
| `source_database` | The global name of the source database. If `NULL`, then the procedure does not add a condition regarding the source database to the generated rules.  In a CDB, specify the global name of the container to which the rules pertain. The container can be the root or a PDB. For example, `mycdb.example.com` or `hrpdb.example.com`. See [Oracle Database XStream Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=XSTRM72988) for more information about setting this parameter in a CDB.  If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify `DBS1` and the domain is `.NET`, then the procedure specifies `DBS1.NET` automatically. |
| `table_names` | The tables for which data manipulation language (DML) and data definition language (DDL) changes are streamed out to the XStream client application. The tables can be specified in the following ways:  - Comma-delimited list of type `VARCHAR2`. - A PL/SQL associative array of type `DBMS_UTILITY.UNCL_ARRAY`, where each element is the name of a table. Specify the first table in position 1. The last position must be `NULL`.  Each table should be specified as `[``schema_name``.]` `table_name`. For example, you can specify `hr.employees`. If the schema is not specified, then the current user is the default.  See Also: " Usage Notes " for more information about this parameter |
| `schema_names` | The schemas for which DML and DDL changes are streamed out to the XStream client application. The schemas can be specified in the following ways:  - Comma-delimited list of type `VARCHAR2`. - A PL/SQL associative array of type `DBMS_UTILITY.UNCL_ARRAY`, where each element is the name of a schema. Specify the first schema in position 1. The last position must be `NULL`.  Note: This procedure does not concatenate the `schema_names` parameter with the `table_names` parameter. To specify tables, enter fully qualified table names in the `table_names` parameter (`schema_name.table_name`).  See Also: " Usage Notes " for more information about this parameter |
| `connect_user` | The user who can attach to the specified outbound server to retrieve the LCR stream. The client application must attach to the outbound server as the specified connect user. See " CREATE\_OUTBOUND Procedure " for information about the privileges required by a connect user.  If `NULL`, then the current user is the default. |

[^1]: Creates a new queue at the database running the capture process. The new queue is called the cloned queue because it is a clone of the queue used by the original stream. The new queue will be used by the new, cloned capture process, and it will be the source queue for the new, cloned propagation.

[^undefined]: Creates a new propagation that propagates LCRs from the source queue created in Step 1 to the existing destination queue. The new propagation is called the cloned propagation because it is a clone of the propagation used by the original stream. The cloned propagation uses the same rule set as the original propagation.

[^undefined]: Stops the capture process.

[^2]: Queries the acknowledge SCN for the original propagation. The acknowledged SCN is the last SCN acknowledged by the apply process that applies the changes sent by the propagation.

[^undefined]: Creates a new capture process. The new capture process is called the cloned capture process because it is a clone of the capture process used by the original stream. The procedure sets the start SCN for the cloned capture process to the value of the queried acknowledged SCN. The cloned capture process uses the same rule set as the original capture process.

[^undefined]: Drops the original propagation.

[^undefined]: Starts the original capture process with the start SCN set to the acknowledged SCN queried in Step 4.

[^undefined]: If the `auto_merge_threshold` parameter is set to a positive number, then creates an Oracle Scheduler job to run the `MERGE_STREAMS_JOB` procedure at set intervals according to its schedule. When the two streams are within the specified merge threshold, the `MERGE_STREAMS_JOB` procedure runs the `MERGE_STREAMS` procedure to merge the streams automatically.
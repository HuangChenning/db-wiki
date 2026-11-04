---
title: DBMS_STREAMS_ADM
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_streams_adm.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 145 DBMS\_STREAMS\_ADM

The `DBMS_STREAMS_ADM` package, one of a set of Oracle Streams packages, provides subprograms for configuring Oracle Streams environments. This package also includes subprograms for adding and removing simple rules for capture, propagation, apply, and dequeue at the table, schema, and database level. This package also includes subprograms for configuring and managing XStream outbound servers and inbound servers.

This chapter contains the following topics:

- Using DBMS\_STREAMS\_ADM
	- Overview
		- Deprecated Subprograms
		- Security Model
		- Operational Notes
- Summary of DBMS\_STREAMS\_ADM Subprograms

---

## Using DBMS\_STREAMS\_ADM

This section contains topics that relate to using the `DBMS_STREAMS_ADM` package.

---

### Overview

The `DBMS_STREAMS_ADM` package, one of a set of Oracle Streams packages, provides subprograms for configuring an Oracle Streams environment. This package also includes subprograms for adding and removing simple rules for capture, propagation, apply, and dequeue at the table, schema, and database level. These rules support logical change records (LCRs), which include row LCRs and data definition language (DDL) LCRs. This package also contains subprograms for creating message rules for specific message types. This package also contains subprograms for creating queues, and for managing Oracle Streams metadata, such as data dictionary information.

If you require more sophisticated rules, then refer to [Chapter 127, "DBMS\_RULE"](d_rule.md) package.

See Also:

- [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm), [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/toc.htm), and [Oracle Database 2 Day + Data Replication and Integration Guide](https://docs.oracle.com/cd/E11882_01/server.112/e17516/toc.htm) for more information about this package and Oracle Streams
- [Chapter 127, "DBMS\_RULE"](d_rule.md)

---

### Deprecated Subprograms

Note:

Oracle recommends that you do not use deprecated subprograms. Support for deprecated features is for backward compatibility only.

The following subprograms are deprecated with Oracle Database 10g Release 2 and later:

- `MAINTAIN_SIMPLE_TABLESPACE`
	This procedure is replaced by the `MAINTAIN_SIMPLE_TTS` procedure.
	See Also:
	MAINTAIN\_SIMPLE\_TTS Procedure
- `MAINTAIN_TABLESPACES`
	This procedure is replaced by the `MAINTAIN_TTS` procedure.
	See Also:
	MAINTAIN\_TTS Procedure

---

### Security Model

Security on this package can be controlled in either of the following ways:

- Granting `EXECUTE` on this package to selected users or roles.
- Granting `EXECUTE_CATALOG_ROLE` to selected users or roles.

If subprograms in the package are run from within a stored procedure, then the user who runs the subprograms must be granted `EXECUTE` privilege on the package directly. It cannot be granted through a role.

A user is associated with each Oracle Streams client. The following sections describe these users:

- Oracle Streams Administrator
- Capture User
- Propagation User
- Apply User for an Oracle Streams Apply Process
- Apply User for an XStream Inbound Server
- Messaging Client User

Note:

The user must be granted additional privileges to perform some administrative tasks using the subprograms in this package, such as creating a synchronous capture. If additional privileges are required for a subprogram, then the privileges are documented in the section that describes the subprogram.

#### Oracle Streams Administrator

To ensure that the user who runs the subprograms in this package has the necessary privileges, configure an Oracle Streams administrator and connect as the Oracle Streams administrator when using this package.

See Also:

[Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/prep_rep.htm#STREP200) for information about configuring an Oracle Streams administrator

#### Capture User

The following procedures can create a capture process:

- ADD\_GLOBAL\_RULES Procedure
- ADD\_SCHEMA\_RULES Procedure
- ADD\_SUBSET\_RULES Procedure
- ADD\_TABLE\_RULES Procedure

The following procedures can create a synchronous capture:

- ADD\_SUBSET\_RULES Procedure
- ADD\_TABLE\_RULES Procedure

If one of these procedures creates a capture process or a synchronous capture, then it configures the current user as the capture user. The capture user is the user in whose security domain a capture process or synchronous capture captures changes that satisfy its rule set(s) and runs custom rule-based transformations configured for these rules. This user must have the necessary privileges to capture changes. The procedure grants the capture user `ENQUEUE` privilege on the queue used by the capture process or synchronous capture and configures the user as a secure queue user of the queue.

See Also:

[CREATE\_CAPTURE Procedure](d_cap_a.md) and [CREATE\_SYNC\_CAPTURE Procedure](d_cap_a.md) for information about the privileges required to capture changes (refer to the `capture_user` parameter)

#### Propagation User

The following procedures can create a propagation:

- ADD\_GLOBAL\_PROPAGATION\_RULES Procedure
- ADD\_MESSAGE\_PROPAGATION\_RULE Procedure
- ADD\_SCHEMA\_PROPAGATION\_RULES Procedure
- ADD\_SUBSET\_PROPAGATION\_RULES Procedure
- ADD\_TABLE\_PROPAGATION\_RULES Procedure

When a propagation is created, a propagation job also might be created. If a propagation job is created when one of these procedures is run, then the user who runs the procedure owns the propagation job. Each propagation job is an Oracle Scheduler job. You can adjust the schedule of a propagation job using Oracle Scheduler.

Note:

- The source queue owner performs the propagation, but the propagation job is owned by the user who creates it. These two users might or might not be the same.
- For a propagation to work properly, the owner of the source queue must have the necessary privileges to propagate messages.

See Also:

- [CREATE\_PROPAGATION Procedure](d_prop_a.md) for more information about the required privileges
- "Propagation Rules for LCRs" for information about when a propagation job is created

#### Apply User for an Oracle Streams Apply Process

The following procedures can create an apply process:

- ADD\_GLOBAL\_RULES Procedure
- ADD\_MESSAGE\_RULE Procedure
- ADD\_SCHEMA\_RULES Procedure
- ADD\_SUBSET\_RULES Procedure
- ADD\_TABLE\_RULES Procedure

If one of these procedures creates an apply process, then it configures the current user as the apply user. For an apply process, the apply user is the user in whose security domain an apply process dequeues messages that satisfy its rule sets.

An apply user applies messages directly to database objects, runs custom rule-based transformations configured for apply process rules, and runs apply handlers configured for the apply process. This user must have the necessary privileges to apply changes. The procedure grants the apply user `DEQUEUE` privilege on the queue used by the apply process and configures the user as a secure queue user of the queue.

See Also:

[CREATE\_APPLY Procedure](d_apply.md) for information about the privileges required to apply changes (refer to the `apply_user` parameter)

#### Apply User for an XStream Inbound Server

The following procedures in can create an XStream inbound server:

- ADD\_GLOBAL\_RULES Procedure
- ADD\_SCHEMA\_RULES Procedure
- ADD\_SUBSET\_RULES Procedure
- ADD\_TABLE\_RULES Procedure

Note:

These procedures cannot create an outbound server.

If the `streams_name` parameter is set to `NULL` and no relevant apply process, inbound server, or outbound server exists, then the procedure creates an apply process automatically with a system-generated name.

The apply process remains an apply process if it receives captured logical change records (LCRs) from a capture process. The apply process can become an inbound server if an XStream client application attaches to it before it receives captured LCRs from a capture process. After the initial contact, an apply process cannot be changed into an inbound server, and an inbound server cannot be changed into an apply process.

If one of these procedures creates an inbound server, then it configures the current user as the apply user. The apply user is the user in whose security domain an XStream client application attaches to an Oracle database.

An apply user applies changes directly to database objects, runs custom rule-based transformations configured for inbound server rules, and runs apply handlers configured for the inbound server. This user must have the necessary privileges to apply changes. The procedure grants the apply user `DEQUEUE` privilege on the queue used by the inbound server and configures the user as a secure queue user.

Each inbound server must have a unique name. The name cannot be used by an apply process, outbound server, or messaging client in the same database, and the name cannot be used by another inbound server in the same database.

If a relevant apply process, inbound server, or outbound server exists, then the procedure does not create an inbound server. Instead, the procedure uses the relevant apply process, inbound server, or outbound server. If the `streams_name` parameter specifies an existing apply process, inbound server, or outbound server, then the specified client is used.

When `streams_name` parameter is `NULL` and the `streams_type` parameter is set to `apply`, the relevant apply process, inbound server, or outbound server is identified in one of the following ways:

- If one existing apply process or outbound server has the source database specified in the `source_database` parameter and uses the queue specified in the `queue_name` parameter, then the procedure uses this apply process or outbound server.
- If the `source_database` parameter is set to `NULL` and one existing apply process, inbound server, or outbound server is using the queue specified in the `queue_name` parameter, then the procedure uses this apply process, inbound server, or outbound server.

If the `streams_name` parameter is set to `NULL` and multiple relevant apply processes, inbound servers, or outbound servers exist, then the procedure raises an error.

Note:

Using XStream requires purchasing a license for the Oracle GoldenGate product. See [Oracle Database XStream Guide](https://docs.oracle.com/cd/E11882_01/server.112/e16545/xstrm_intro.htm#XSTRM72545).

#### Messaging Client User

The following procedures can create a messaging client:

- ADD\_GLOBAL\_RULES Procedure
- ADD\_MESSAGE\_RULE Procedure
- ADD\_SCHEMA\_RULES Procedure
- ADD\_SUBSET\_RULES Procedure
- ADD\_TABLE\_RULES Procedure

If one of these procedures creates a messaging client, then the user who runs this procedure is granted the privileges to dequeue from the queue using the messaging client. The procedure configures this user as a secure queue user of the queue, and only this user can use the messaging client.

---

### Operational Notes

Several procedures in this package create rules for Oracle Streams clients and XStream clients, and several procedures configure an Oracle Streams environment. The following sections provide information about using these procedures:

- Procedures That Create Rules for Oracle Streams Clients and XStream Clients
- Procedures That Configure an Oracle Streams Environment

#### Procedures That Create Rules for Oracle Streams Clients and XStream Clients

Oracle Streams clients include capture processes, synchronous captures, propagations, apply processes, and messaging clients. XStream clients include XStream outbound servers and inbound servers. Some of the procedures in the `DBMS_STREAMS_ADM` package add rules to the rule sets of Oracle Streams clients and XStream clients. The rules can pertain to changes in the redo log, to data manipulation language (DML) changes made to a table, to logical change records (LCRs), or to user messages.

An LCR represents either a row change that results from a DML operation or a data definition language (DDL) change. An LCR that represents a row change is a row LCR, and an LCR that represents a DDL change is a DDL LCR. LCRs can either represent changes that were captured by a capture process or a synchronous capture, or they can represent changes created by a user or application. A user message is a custom message that is based on a user-defined type and created by users or applications.

A capture process, propagation, apply process, messaging client, outbound server, or inbound server can have both positive and negative rule sets. A synchronous capture can have only a positive rule set.

For all of the procedures except the ones that create subset rules, and for all clients except for synchronous captures, you use the `inclusion_rule` parameter to specify the type of rule set (either positive or negative) for the created rules. If the client does not have a rule set of the specified type, then a rule set is created automatically, and the rules are added to the rule set. Other rules in an existing rule set for the client are not affected. Additional rules can be added to a rule set using either the `DBMS_STREAMS_ADM` package or the `DBMS_RULE_ADM` package. If an client has both a positive and a negative rule set, then the negative rule set is always evaluated first.

The following sections describe each type of rule in detail:

- Capture Process Rules for Changes in the Redo Log
- Synchronous Capture Rules for DML Changes to Tables
- Propagation Rules for LCRs
- Propagation Rules for User Messages
- Apply Process Rules for LCRs
- Apply Process Rules for User Messages
- Messaging Client Rules for LCRs
- Messaging Client Rules for User Messages
- XStream Outbound Server Rules for LCRs
- XStream Inbound Server Rules for LCRs

Note:

Using XStream requires purchasing a license for the Oracle GoldenGate product. See [Oracle Database XStream Guide](https://docs.oracle.com/cd/E11882_01/server.112/e16545/xstrm_intro.htm#XSTRM72545).

See Also:

[Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_rules.htm#STRMS006) for more information about how rules are used in Oracle Streams

##### Capture Process Rules for Changes in the Redo Log

The following procedures add rules to a rule set of a capture process when you specify `capture` for the `streams_type` parameter:

- The `ADD_GLOBAL_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for all changes made to a source database. See ADD\_GLOBAL\_RULES Procedure.
- The `ADD_SCHEMA_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for changes made to a specified schema. See ADD\_SCHEMA\_RULES Procedure.
- The `ADD_SUBSET_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for DML changes made to a subset of rows in a specified table. See ADD\_SUBSET\_RULES Procedure.
- The `ADD_TABLE_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for changes made to a specified table. See ADD\_TABLE\_RULES Procedure.

If one of these procedures adds rules to the positive rule set for a capture process, then the capture process captures row changes resulting from DML changes, or DDL changes, or both from a source database and enqueues these changes into the specified queue. If one of these procedures adds rules to the negative rule set for a capture process, then the capture process discards row changes, or DDL changes, or both from a source database.

A capture process can capture changes locally at a source database or remotely at a downstream database. Therefore, for capture process rules, you should execute the procedure either at the source database or at a downstream database.

If the capture process is a local capture process, or if the capture process is a downstream capture process that uses a database link to the source database, then these procedures automatically prepare the appropriate database objects for instantiation:

- `ADD_GLOBAL_RULES` invokes the `PREPARE_GLOBAL_INSTANTIATION` procedure in the `DBMS_CAPTURE_ADM` package at the source database.
- `ADD_SCHEMA_RULES` invokes the `PREPARE_SCHEMA_INSTANTIATION` procedure in the `DBMS_CAPTURE_ADM` package at the source database.
- `ADD_SUBSET_RULES` and `ADD_TABLE_RULES` invoke the `PREPARE_TABLE_INSTANTIATION` procedure in the `DBMS_CAPTURE_ADM` package at the source database.

These procedures also enable supplemental logging for the primary key, unique key, foreign key, and bitmap index columns in the tables prepared for instantiation. The primary key columns are unconditionally logged. The unique key, foreign key, and bitmap index columns are conditionally logged.

If the capture process is a downstream capture process that does not use a database link to the source database, then you must prepare the appropriate objects for instantiation and specify the necessary supplemental logging manually at the source database.

If one of these procedures is executed at a downstream database, then you specify the source database using the `source_database` parameter, and the specified capture process must exist. The procedure cannot create a capture process if it is run at a downstream database. You can create a capture process at a downstream database using the `CREATE_CAPTURE` procedure in the `DBMS_CAPTURE_ADM` package.

See Also:

[Chapter 32, "Summary of DBMS\_CAPTURE\_ADM Subprograms"](d_cap_a.md) for more information about the `CREATE_CAPTURE` procedure and the procedures that prepare database objects for instantiation

##### Synchronous Capture Rules for DML Changes to Tables

The following procedures add rules to the rule set of a synchronous capture when you specify `sync_capture` for the `streams_type` parameter:

- The `ADD_SUBSET_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for DML changes made to a subset of rows in a specified table. See ADD\_SUBSET\_RULES Procedure.
- The `ADD_TABLE_RULES` procedure adds a rule whose rule condition evaluates to `TRUE` for DML changes made to a specified table. See ADD\_TABLE\_RULES Procedure.

If one of these procedures adds rules to the positive rule set for a synchronous capture, then the synchronous capture captures row changes resulting from DML changes to the table at the source database and enqueues these changes into the specified queue. A synchronous capture cannot have a negative rule set.

A synchronous capture captures changes locally at the database where it is configured. This database is the source database for changes captured by the synchronous capture. Therefore, for synchronous capture rules, you should execute the procedure at the source database.

These procedures automatically prepare the appropriate tables for instantiation by invoking the `PREPARE_SYNC_INSTANTIATION` function in the `DBMS_CAPTURE_ADM` package at the source database.

Note:

- A synchronous capture ignores rules in its rule set that were created by a procedure other than `ADD_SUBSET_RULES` or `ADD_TABLE_RULES`.
- When the `ADD_TABLE_RULES` or the `ADD_SUBSET_RULES` procedure adds rules to a synchronous capture rule set, the procedure must obtain an exclusive lock on the specified table. If there are outstanding transactions on the specified table, then the procedure waits until it can obtain a lock.

##### Propagation Rules for LCRs

The following procedures add propagation rules for LCRs to a rule set of a propagation:

- The `ADD_GLOBAL_PROPAGATION_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for all LCRs in a source queue. See ADD\_GLOBAL\_PROPAGATION\_RULES Procedure.
- The `ADD_SCHEMA_PROPAGATION_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for LCRs in a source queue containing changes made to a specified schema. See ADD\_SCHEMA\_PROPAGATION\_RULES Procedure.
- The `ADD_SUBSET_PROPAGATION_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for row LCRs in a source queue containing the results of DML changes made to a subset of rows in a specified table. See "ADD\_SUBSET\_PROPAGATION\_RULES Procedure".
- The `ADD_TABLE_PROPAGATION_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for LCRs in a source queue containing changes made to a specified table. See "ADD\_TABLE\_PROPAGATION\_RULES Procedure".

If one of these procedures adds rules to the positive rule set for the propagation, then the rules specify that the propagation propagates LCRs in a source queue to a destination queue. If one of these procedures adds rules to the negative rule set for the propagation, then the rules specify that the propagation discards LCRs in a source queue. When you create rules with one of these procedures, and you specify a value for the `source_databse` parameter, then the rules include conditions for the specified source database.

##### Propagation Rules for User Messages

The `ADD_MESSAGE_PROPAGATION_RULE` procedure adds a message rule to a rule set of a propagation. If this procedure adds a rule to the positive rule set for the propagation, then the rule specifies that the propagation propagates the user messages of a specific message type that evaluate to `TRUE` for the rule condition from a source queue to a destination queue. If this procedure adds a rule to the negative rule set for the propagation, then the rule specifies that the propagation discards the user messages in a source queue of a specific message type that evaluate to `TRUE` for the rule condition. This procedure generates a rule name for the rule.

See Also:

"ADD\_MESSAGE\_PROPAGATION\_RULE Procedure"

##### Apply Process Rules for LCRs

The following procedures add rules to a rule set of an apply process when you specify `apply` for the `streams_type` parameter and an apply process for the `streams_name` parameter:

- The `ADD_GLOBAL_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for all LCRs in the apply process's queue. See "ADD\_GLOBAL\_RULES Procedure".
- The `ADD_SCHEMA_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for LCRs in the apply process's queue containing changes made to a specified schema. See "ADD\_SCHEMA\_RULES Procedure".
- The `ADD_SUBSET_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for row LCRs in the apply process's queue containing the results of DML changes made to a subset of rows in a specified table. See "ADD\_SUBSET\_RULES Procedure".
- The `ADD_TABLE_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for LCRs in the apply process's queue containing changes made to a specified table. See "ADD\_TABLE\_RULES Procedure".

If one of these procedures adds rules to the positive rule set for the apply process, then the rules specify that the apply process applies LCRs in its queue. If one of these procedures adds rules to the negative rule set for the apply process, then the rules specify that the apply process discards LCRs in its queue. For apply process rules, you should execute these procedures at the destination database.

Changes applied by an apply process created by one of these procedures generate tags in the redo log at the destination database with a value of `'00'` (double zero). You can use the `ALTER_APPLY` procedure in the `DBMS_APPLY_ADM` package to alter the tag value after the apply process is created, if necessary.

An apply process can apply captured LCRs from only one source database. If one of these procedures creates an apply process, then specify the source database for the apply process using the `source_database` parameter. If the `source_database` parameter is `NULL`, and one of these procedures creates an apply process, then the source database name of the first LCR received by the apply process is used for the source database.

The rules in the apply process rule sets determine which messages are dequeued by the apply process. When you create rules with one of these procedures, and you specify a value for the `source_database` parameter, then the rules include conditions for the specified source database. If the apply process dequeues an LCR with a source database that is different from the source database for the apply process, then an error is raised. In addition, when adding rules to an existing apply process, the database specified in the `source_database` parameter cannot be different from the source database for the apply process. You can determine the source database for an apply process by querying the `DBA_APPLY_PROGRESS` data dictionary view.

An apply process created by one of these procedures can apply messages only at the local database and can apply only captured messages. To create an apply process that applies messages at a remote database or an apply process that applies user messages, use the `CREATE_APPLY` procedure in the `DBMS_APPLY_ADM` package.

You can also use the `DBMS_APPLY_ADM.CREATE_APPLY` procedure to specify nondefault values for the `apply_captured`, `apply_user`, `apply_database_link`, and `apply_tag` parameters when you run that procedure. You can use one of the procedures in the `DBMS_STREAMS_ADM` package to add rules to a rule set used by the apply process after you create it.

See Also:

- ["ALTER\_APPLY Procedure"](d_apply.md)
- ["CREATE\_APPLY Procedure"](d_apply.md)

##### Apply Process Rules for User Messages

The `ADD_MESSAGE_RULE` procedure adds a message rule to a rule set of an apply process when you specify `apply` for the `streams_type` parameter. For an apply process rule, you should execute this procedure at the destination database.

If this procedure adds a rule to the positive rule set for an apply process, then the apply process dequeues user messages of a specific message type that satisfy the apply process rule and sends these messages to its message handler. If no message handler is specified for the apply process, then use the `ALTER_APPLY` procedure in the `DBMS_APPLY_ADM` package to set the message handler. If this procedure adds a rule to the negative rule set for an apply process, then the apply process discards user messages of a specific message type that satisfy the apply process rule.

See Also:

- ADD\_MESSAGE\_RULE Procedure
- [ALTER\_APPLY Procedure](d_apply.md)

##### Messaging Client Rules for LCRs

The following procedures add rules to a rule set of a messaging client when you specify `dequeue` for the `streams_type` parameter:

- The `ADD_GLOBAL_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for all LCRs in the messaging client's queue. See "ADD\_GLOBAL\_RULES Procedure".
- The `ADD_SCHEMA_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for LCRs in the messaging client's queue containing changes made to a specified schema. See "ADD\_SCHEMA\_RULES Procedure".
- The `ADD_SUBSET_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for row LCRs in the messaging client's queue containing the results of DML changes made to a subset of rows in a specified table. See "ADD\_SUBSET\_RULES Procedure".
- The `ADD_TABLE_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for LCRs in the messaging client's queue containing changes made to a specified table. See "ADD\_TABLE\_RULES Procedure".

If one of these procedures adds rules to the positive rule set for a messaging client, then the messaging client can dequeue persistent row LCRs, or DDL LCRs, or both that originated at the source database that matches the `source_database` parameter. If one of these procedures adds rules to the negative rule set for a messaging client, then the messaging client discards persistent row LCRs, or DDL LCRs, or both that originated at the source database that matches the `source_database` parameter. You should execute these procedures at the database where you want to dequeue the messages with the messaging client.

##### Messaging Client Rules for User Messages

The `ADD_MESSAGE_RULE` procedure adds a message rule to a rule set of a messaging client when you specify `dequeue` for the `streams_type` parameter. You should execute this procedure at the database that will dequeue messages.

If this procedure adds a rule to the positive rule set for a messaging client, then the messaging client dequeues user messages of a specific message type that satisfy the message rule. If this procedure adds a rule to the negative rule set for a messaging client, then the messaging client discards user messages of a specific message type that satisfy the message rule.

See Also:

"ADD\_MESSAGE\_RULE Procedure"

##### XStream Outbound Server Rules for LCRs

When you specify `apply` for the `streams_type` parameter and an XStream outbound server for the `streams_name` parameter, the following procedures add rules to a rule set of the specified outbound server:

- The `ADD_GLOBAL_RULES` procedure adds rules whose rule conditions evaluate to `TRUE` for all LCRs.
- The `ADD_SCHEMA_RULES` procedure adds rules whose rule conditions evaluate to `TRUE` for LCRs that contain changes made to a specified schema.
- The `ADD_SUBSET_RULES` procedure adds rules whose rule conditions evaluate to `TRUE` for row LCRs that contain the results of DML changes made to a subset of rows in a specified table.
- The `ADD_TABLE_RULES` procedure adds rules whose rule conditions evaluate to `TRUE` for LCRs that contain changes made to a specified table.

These rules are evaluated against LCRs in the outbound server's queue.

If one of the preceding procedures adds rules to the positive rule set for the outbound server, then the rules specify that the outbound server sends LCRs in its queue to the XStream client application. If one of these procedures adds rules to the negative rule set for the outbound server, then the rules specify that the outbound server discards LCRs in its queue. For outbound server rules, execute these procedures at the database to which the XStream client application attaches.

An outbound server can process captured LCRs from only one source database. The source database is the database where the changes originated. If one of these procedures adds rules to the rule set of an outbound server, then specify the source database for the outbound server using the `source_database` parameter.

The rules in the outbound server's rule sets determine which LCRs are dequeued by the outbound server. When you create rules with one of these procedures, and you specify a value for the `source_database` parameter, then the rules include conditions for the specified source database. If the outbound server dequeues an LCR with a source database that is different from the source database for the outbound server, then an error is raised. In addition, when adding rules to an existing outbound server, the database specified in the `source_database` parameter cannot be different from the source database for the outbound server. You can determine the source database for an outbound server by querying the `DBA_XSTREAM_OUTBOUND` data dictionary view.

Note:

These procedures cannot create an XStream outbound server. You can use one of the procedures in the `DBMS_STREAMS_ADM` package to add rules to a rule set used by the outbound server after you create it.

See Also:

[Oracle Database XStream Guide](https://docs.oracle.com/cd/E11882_01/server.112/e16545/xstrm_config.htm#XSTRM1496) for information about creating an outbound server

##### XStream Inbound Server Rules for LCRs

When you specify `apply` for the `streams_type` parameter and an XStream inbound server for the `streams_name` parameter, the following procedures add rules to a rule set of the specified inbound server:

- The `ADD_GLOBAL_RULES` procedure adds rules whose rule conditions evaluate to `TRUE` for all LCRs sent to the inbound server.
- The `ADD_SCHEMA_RULES` procedure adds rules whose rule conditions evaluate to `TRUE` for LCRs sent to the inbound server that contain changes made to a specified schema.
- The `ADD_SUBSET_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for row LCRs sent to the inbound server that contain the results of data definition language (DML) changes made to a subset of rows in a specified table.
- The `ADD_TABLE_RULES` procedure adds rules whose rule condition evaluates to `TRUE` for LCRs sent to the inbound server that contain changes made to a specified table.

If one of the preceding procedures adds rules to the positive rule set for the inbound server, then the rules specify that the inbound server applies LCRs sent to it by the XStream client application. If one of these procedures adds rules to the negative rule set for the inbound server, then the rules specify that the inbound server discards LCRs sent to it by the XStream client application. For inbound server rules, execute these procedures at the database to which the XStream client application attaches. If an inbound server has no rule sets, then it applies all of the LCRs sent to it by the XStream client application.

Changes applied by an inbound server created by one of these procedures generate tags in the redo log at the destination database with a value of `'00'` (double zero). You can use the `ALTER_APPLY` procedure in the `DBMS_APPLY_ADM` package to alter the tag value after the inbound server is created, if necessary.

The rules in the XStream inbound server rule sets determine which LCRs are either applied or discarded after the LCRs are received from the XStream client application. An inbound server can only process LCRs sent from an XStream client application.

When one of these procedures creates rules for an inbound server, the procedure ignores the `source_database` parameter.

Note:

If the name specified in the `streams_name` parameter does not exist, then these procedures always create an apply process. The apply process remains an apply process if it receives captured LCRs from a capture process. The apply process can become an inbound server if an XStream client application attaches to it before it receives LCRs from a capture process. After the initial contact, an apply process cannot be changed into an inbound server, and an inbound server cannot be changed into an apply process.

See Also:

[Oracle Database XStream Guide](https://docs.oracle.com/cd/E11882_01/server.112/e16545/xstrm_config.htm#XSTRM1496) for information about creating an inbound server

#### Procedures That Configure an Oracle Streams Environment

The following procedures in this package configure an environment that is maintained by Oracle Streams:

- MAINTAIN\_CHANGE\_TABLE Procedure configures an Oracle Streams environment that records in a change table the data manipulation language (DML) changes made to a source table. Optionally, this procedure can also configure one-way replication of the table from the source database to the destination database.
- MAINTAIN\_GLOBAL Procedure configures an Oracle Streams environment that replicates changes at the database level between two databases.
- MAINTAIN\_SCHEMAS Procedure configures an Oracle Streams environment that replicates changes to specified schemas between two databases.
- MAINTAIN\_SIMPLE\_TTS Procedure clones a simple tablespace from a source database at a destination database and configures an Oracle Streams environment that replicates changes to specified tablespace between these two databases.
- MAINTAIN\_TABLES Procedure configures an Oracle Streams environment that replicates changes to specified tables between two databases.
- MAINTAIN\_TTS Procedure clones a set of tablespaces from a source database at a destination database and configures an Oracle Streams environment that replicates changes to specified tablespaces between these two databases.
- PRE\_INSTANTIATION\_SETUP Procedure and POST\_INSTANTIATION\_SETUP Procedure

The `PRE_INSTANTIATION_SETUP` and `POST_INSTANTIATION_SETUP` procedures must be used together to complete the Oracle Streams replication configuration. Typically, the `PRE_INSTANTIATION_SETUP` and `POST_INSTANTIATION_SETUP` procedures are used to perform database maintenance operations with little or no down time. See [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/ap_strmnt.htm#STRMS165) for more information.

The following sections contain information about using these procedures:

- Automatic Platform Conversion
- Actions Performed by These Procedures
- Configuration Progress and Recoverability
- Requirements for Running These Procedures
- Common Parameters for the Configuration Procedures

See Also:

[Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/config_simple.htm#STREP020) for more information about using these procedures

Automatic Platform Conversion

If the source and destination databases run on different platforms, then these procedures, or the scripts generated by these procedures, convert transferred datafiles to the appropriate platform automatically.

Actions Performed by These Procedures

To view all of the actions performed by one of these procedures in detail, use the procedure to generate a script, and view the script in a text editor.

Configuration Progress and Recoverability

When one of these procedures is run with the `perform_actions` parameter set to `TRUE`, metadata about its configuration actions is recorded in the following data dictionary views: `DBA_RECOVERABLE_SCRIPT`, `DBA_RECOVERABLE_SCRIPT_PARAMS`, `DBA_RECOVERABLE_SCRIPT_BLOCKS`, and `DBA_RECOVERABLE_SCRIPT_ERRORS`. If the procedure stops because it encounters an error, then you can use the `RECOVER_OPERATION` procedure to complete the configuration after you correct the conditions that caused the error.

Note:

When one of these procedures is run with the `perform_actions` parameter set to `FALSE`, these views are not populated. Also, the views are not populated when a script generated by one of these procedures is run.

See Also:

"RECOVER\_OPERATION Procedure"

Requirements for Running These Procedures

Meet the following requirements when you use one of these procedures:

- Run the procedure at the capture database. The capture database is the database that will contain the capture process that captures changes made to the source database. If the capture database is the same as the source database, then a local capture process is configured. If the capture database is different from the source database, then a downstream capture process is configured. See [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/prep_rep.htm#STREP225) for more information about the capture database.
- The user who runs the procedure must be able to use a database link from the source database to the destination database. This database link should have the same name as the global name of the destination database.
- If the procedure configures downstream capture, then the corresponding user at the capture database must be able to use a database link to access the source database. This database link should have the same name as the global name of the source database.
- If the procedure configures downstream capture, and the capture database is different from the destination database, then the corresponding user at the capture database must be able to use a database link to access the destination database. This database link should have the same name as the global name of the destination database.
- Both databases must be open during configuration. If the procedure is generating a script only, then the database specified in the `destination_database` parameter does not need to be open when you run the procedure, but both databases must be open when you run the generated script.
- Grant the user who runs the procedure the `DBA` role. This user must have the necessary privileges to complete the following actions:
	- Create `ANYDATA` queues, capture processes, propagations, and apply processes.
		- Specify supplemental logging
		- Run subprograms in the `DBMS_STREAMS_ADM` and `DBMS_AQADM` packages.
		- Access the database specified in the `destination_database` parameter through a database link. This database link should have the same name as the global name of the destination database.
	Typically, the `DBA` role can be revoked from the user, if necessary, after the configuration is complete.
- The procedure, or the scripts generated by these procedure, must be run at an Oracle Database 10g Release 2 or later database.
- If the `perform_actions` parameter is set to `TRUE` in the procedure to configure the Oracle Streams environment directly, then all of the databases configured by the procedure must be Oracle Database 10g Release 2 or later databases.
- If the `perform_actions` parameter is set to `FALSE` in the procedure, and the environment is configured with a generated script, then the databases configured by the script must be Oracle Database 10g Release 1 or later databases. If the script configures an Oracle Database 10g Release 1 database, then the script must be modified so that it does not configure features that are available only in Oracle Database 10g Release 2 or later, such as queue-to-queue propagation.
- Each specified directory object must be created using the SQL statement `CREATE` `DIRECTORY`, and the user who invokes the procedure must have `READ` and `WRITE` privilege on each one.
- For procedures that include the `bi_directional` parameter, if the `bi_directional` parameter is set to `TRUE`, or if the source database is not the capture database, then the `source_database` parameter must specify a database that contains the database objects to be shared. The database specified in the `destination_database` parameter might or might not contain these database objects. If the destination database does not contain the shared database objects, then the procedure instantiates the database objects at the destination database (excluding the `PRE_INSTANTIATION_SETUP` and `POST_INSTANTIATION_SETUP` procedures).
- For procedures that include the `bi_directional` parameter, if the `bi_directional` parameter is set to `TRUE` or if a network instantiation will be performed, then the corresponding user at the destination database must be able to use a database link to access the source database. This database link should have the same name as the global name of the source database.

To ensure that the user who runs these procedures has the necessary privileges, you should configure an Oracle Streams administrator at each database, and each database link should be should be created in the Oracle Streams administrator's schema.

See Also:

[Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/prep_rep.htm#STREP200) for information about configuring an Oracle Streams administrator

Common Parameters for the Configuration Procedures

Table 145-1 describes the common parameters for the procedures in this package that configure an Oracle Streams environment. Some of the procedures do not include all of the parameters in Table 145-1.

Table 145-1 Common Parameters for Configuration Procedures

| Parameter | Description |
| --- | --- |
| `perform_actions` | If `TRUE`, then the procedure performs the necessary actions to configure the environment directly.  If `FALSE`, then the procedure does not perform the necessary actions to configure the environment directly.  Specify `FALSE` when this procedure is generating a script that you can edit and then run. The procedure raises an error if you specify `FALSE` and either of the following parameters is `NULL`:  - `script_name` - `script_directory_object` |
| `script_name` | If non- `NULL` and the `perform_actions` parameter is `FALSE`, then specify the name of the script generated by this procedure. The script contains all of the statements used to configure the environment. If a file with the specified script name exists in the specified directory for the `script_directory_object` parameter, then the procedure appends the statements to the existing file.  If non- `NULL` and the `perform_actions` parameter is `TRUE`, then the procedure generates the specified script and performs the actions to configure the environment directly.  If `NULL` and the `perform_actions` parameter is `TRUE`, then the procedure performs the actions to configure the environment directly and does not generate a script.  If `NULL` and the `perform_actions` parameter is `FALSE`, then the procedure raises an error. |
| `script_directory_object` | The directory object for the directory on the local computer system into which the generated script is placed.  If the `script_name` parameter is `NULL`, then the procedure ignores this parameter and does not generate a script.  If `NULL` and the `script_name` parameter is non- `NULL`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle Automatic Storage Management (ASM) disk group. |
| `capture_name` | The name of each capture process configured to capture changes. Do not specify an owner. If the `bi_directional` parameter is set to `TRUE`, then each capture process created by this procedure has the specified name.  If the specified name matches the name of an existing capture process, then the procedure uses the existing capture process and adds the rules for capturing changes to the database to the positive capture process rule set.  If `NULL`, then the system generates a name for each capture process it creates.  Note: The capture process name cannot be altered after the capture process is created. |
| `capture_queue_table` | The name of the queue table for each queue used by a capture process, specified as `[``schema_name``.]` `queue_table_name`. For example, `strmadmin.streams_queue_table`. If the schema is not specified, then the current user is the default.  If `NULL`, then the system generates a name for the queue table of each queue used by a capture process, and the current user is the owner of each queue table. |
| `capture_queue_name` | The name of each queue used by a capture process, specified as `[``schema_name``.]` `queue_name`. For example, `strmadmin.streams_queue`.  If the schema is not specified, then the queue table owner is the default. The queue owner automatically has privileges to perform all queue operations on the queue.  If `NULL`, then the system generates a name for each queue used by a capture process. |
| `capture_queue_user` | The name of the user who requires `ENQUEUE` and `DEQUEUE` privileges for the queue at the source database. This user also is configured as a secure queue user of the queue. The queue user cannot grant these privileges to other users because they are not granted with the `GRANT` option.  If `NULL`, then the procedure does not grant any privileges. You can also grant queue privileges to the appropriate users using the `DBMS_AQADM` package. |
| `propagation_name` | The name of each propagation configured to propagate changes. Do not specify an owner.  If the specified name matches the name of an existing propagation, then the procedure uses the existing propagation and adds the rules for propagating changes to the positive propagation rule set.  If `NULL`, then the system generates a name for each propagation it creates.  Note: The propagation name cannot be altered after the propagation is created. |
| `apply_name` | The name of each apply process configured to apply changes. Do not specify an owner.  If the specified name matches the name of an existing apply process, then the procedure uses the existing apply process and adds the rules for applying changes to the positive apply process rule set.  The specified name must not match the name of an existing messaging client at the destination database.  If `NULL`, then the system generates a name for each apply process it creates. When set to `NULL`, no apply process that applies changes from the source database can exist on the destination database. If an apply process that applies changes from the source database exists at the destination database, then specify a non- `NULL` value for this parameter.  Note: The apply process name cannot be altered after the apply process is created. |
| `apply_queue_table` | The name of the queue table for each queue used by an apply process, specified as `[``schema_name``.]` `queue_table_name`. For example, `strmadmin.streams_queue_table`. If the schema is not specified, then the current user is the default.  If `NULL`, then the system generates a name for the queue table of each queue used by an apply process, and the current user is the owner of each queue table. |
| `apply_queue_name` | The name of each queue used by an apply process, specified as `[``schema_name``.]` `queue_name`. For example, `strmadmin.streams_queue`.  If the schema is not specified, then the queue table owner is the default. The queue owner automatically has privileges to perform all queue operations on the queue.  If `NULL`, then the system generates a name for each queue used by an apply process. |
| `apply_queue_user` | The name of the user who requires `ENQUEUE` and `DEQUEUE` privileges for the queue at the destination database. This user also is configured as a secure queue user of the queue. The queue user cannot grant these privileges to other users because they are not granted with the `GRANT` option.  If `NULL`, then the procedure does not grant any privileges. You can also grant queue privileges to the appropriate users using the `DBMS_AQADM` package. |
| `bi_directional` | Specify `TRUE` to configure bi-directional replication between the database specified in `source_database` and the database specified in `destination_database`. Both databases are configured as source and destination databases, a capture and apply process is configured to capture changes to both databases, and propagations are configured to propagate these changes. If `TRUE`, then a database link from the destination database to the source database with the same global name as the source database must exist.  Specify `FALSE` to configure one way replication from the database specified in `source_database` and the database specified in `destination_database`. A capture process is configured at the current database and an apply process is configured at the destination database. A propagation is configured if necessary.  See Also: [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/config_simple.htm#STREP210) for information about when propagations are configured |
| `include_ddl` | Specify `TRUE` to configure an Oracle Streams replication environment that maintains both DML and DDL changes.  Specify `FALSE` to configure an Oracle Streams replication environment that maintains DML changes only. When this parameter is set to `FALSE`, DDL changes, such as `ALTER` `TABLE`, are not replicated. |

---

## Summary of DBMS\_STREAMS\_ADM Subprograms

Table 145-2 DBMS\_STREAMS\_ADM Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_COLUMN Procedure | Either adds or removes a declarative rule-based transformation which adds a column to a row logical change record (row LCR) that satisfies the specified rule |
| ADD\_GLOBAL\_PROPAGATION\_RULES Procedure | Either adds global rules to the positive rule set for a propagation, or adds global rules to the negative rule set for a propagation, and creates the specified propagation if it does not exist |
| ADD\_GLOBAL\_RULES Procedure | Adds global rules to either the positive or negative rule set of a capture process, apply process, or messaging client, and creates the specified capture process, apply process, or messaging client if it does not exist |
| ADD\_MESSAGE\_PROPAGATION\_RULE Procedure | Either adds a message rule to the positive rule set for a propagation, or adds a message rule to the negative rule set for a propagation, and creates the specified propagation if it does not exist |
| ADD\_MESSAGE\_RULE Procedure | Adds a message rule to either the positive or negative rule set of an apply process or messaging client, and creates the specified apply process or messaging client if it does not exist |
| ADD\_SCHEMA\_PROPAGATION\_RULES Procedure | Either adds schema rules to the positive rule set for a propagation, or adds schema rules to the negative rule set for a propagation, and creates the specified propagation if it does not exist |
| ADD\_SCHEMA\_RULES Procedure | Adds schema rules to either the positive or negative rule set of a capture process, apply process, or messaging client, and creates the specified capture process, apply process, or messaging client if it does not exist |
| ADD\_SUBSET\_PROPAGATION\_RULES Procedure | Adds subset rules to the positive rule set for a propagation, and creates the specified propagation if it does not exist |
| ADD\_SUBSET\_RULES Procedure | Adds subset rules to the positive rule set of a capture process, synchronous capture, apply process, or messaging client, and creates the specified capture process, synchronous capture, apply process, or messaging client if it does not exist |
| ADD\_TABLE\_PROPAGATION\_RULES Procedure | Either adds table rules to the positive rule set for a propagation, or adds table rules to the negative rule set for a propagation, and creates the specified propagation if it does not exist |
| ADD\_TABLE\_RULES Procedure | Adds table rules to the rule set of a capture process, synchronous capture, apply process, or messaging client, and creates the specified capture process, synchronous capture, apply process, or messaging client if it does not exist |
| CLEANUP\_INSTANTIATION\_SETUP Procedure | Removes an Oracle Streams replication configuration that was set up by the `PRE_INSTANTIATION_SETUP` and `POST_INSTANTIATION_SETUP` procedures in this package |
| DELETE\_COLUMN Procedure | Either adds or removes a declarative rule-based transformation which deletes a column from a row LCR that satisfies the specified rule |
| GET\_MESSAGE\_TRACKING Function | Returns the tracking label for the current session |
| GET\_SCN\_MAPPING Procedure | Gets information about the system change number (SCN) values to use for Oracle Streams capture and apply processes in an Oracle Streams replication environment |
| GET\_TAG Function | Gets the binary tag for all redo entries generated by the current session |
| KEEP\_COLUMNS Procedure | Either adds or removes a declarative rule-based transformation which keeps a list of columns in a row LCR that satisfies the specified rule |
| MAINTAIN\_CHANGE\_TABLE Procedure | Configures an Oracle Streams environment that records in a change table the data manipulation language (DML) changes made to a source table. Optionally, this procedure can also configure one-way replication of the table from the source database to the destination database |
| MAINTAIN\_GLOBAL Procedure | Configures an Oracle Streams environment that replicates changes at the database level between two databases |
| MAINTAIN\_SCHEMAS Procedure | Configures an Oracle Streams environment that replicates changes to specified schemas between two databases |
| MAINTAIN\_SIMPLE\_TABLESPACE Procedure | Clones a simple tablespace from a source database at a destination database and uses Oracle Streams to maintain this tablespace at both databases. This procedure is deprecated. |
| MAINTAIN\_SIMPLE\_TTS Procedure | Clones a simple tablespace from a source database at a destination database and uses Oracle Streams to maintain this tablespace at both databases |
| MAINTAIN\_TABLES Procedure | Configures an Oracle Streams environment that replicates changes to specified tables between two databases |
| MAINTAIN\_TABLESPACES Procedure | Clones a set of tablespaces from a source database at a destination database and uses Oracle Streams to maintain these tablespaces at both databases. This procedure is deprecated. |
| MAINTAIN\_TTS Procedure | Clones a set of tablespaces from a source database at a destination database and uses Oracle Streams to maintain these tablespaces at both databases |
| MERGE\_STREAMS Procedure | Merges a stream flowing from one capture process with a stream flowing from another capture process |
| MERGE\_STREAMS\_JOB Procedure | Determines whether the original capture process and the cloned capture are within the specified merge threshold and, if they are, runs the `MERGE_STREAMS` procedure to merge the two streams |
| POST\_INSTANTIATION\_SETUP Procedure | Performs the actions required after instantiation to configure an Oracle Streams replication environment |
| PRE\_INSTANTIATION\_SETUP Procedure | Performs the actions required before instantiation to configure an Oracle Streams replication environment |
| PURGE\_SOURCE\_CATALOG Procedure | Removes all Oracle Streams data dictionary information at the local database for the specified object |
| RECOVER\_OPERATION Procedure | Provides options for an Oracle Streams replication configuration operation that stopped because it encountered an error. This procedure either rolls forward the operation, rolls back the operation, or purges all of the metadata about the operation. |
| REMOVE\_QUEUE Procedure | Removes the specified `ANYDATA` queue |
| REMOVE\_RULE Procedure | Removes the specified rule or all rules from the rule set associated with the specified capture process, synchronous capture, propagation, apply process, or messaging client. |
| REMOVE\_STREAMS\_CONFIGURATION Procedure | Removes the Oracle Streams configuration at the local database |
| RENAME\_COLUMN Procedure | Either adds or removes a declarative rule-based transformation which renames a column in a row LCR that satisfies the specified rule |
| RENAME\_SCHEMA Procedure | Either adds or removes a declarative rule-based transformation which renames a schema in a row LCR that satisfies the specified rule |
| RENAME\_TABLE Procedure | Either adds or removes a declarative rule-based transformation which renames a table in a row LCR that satisfies the specified rule |
| SET\_MESSAGE\_NOTIFICATION Procedure | Sets a notification for messages that can be dequeued by a specified Oracle Streams messaging client from a specified queue |
| SET\_MESSAGE\_TRACKING Procedure | Sets the tracking label for logical change records (LCRs) produced by the current session |
| SET\_RULE\_TRANSFORM\_FUNCTION Procedure | Sets or removes the transformation function name for a rule-based transformation |
| SET\_TAG Procedure | Sets the binary tag for all redo entries subsequently generated by the current session |
| SET\_UP\_QUEUE Procedure | Creates a queue table and a queue for use with the capture, propagate, and apply functionality of Oracle Streams |
| SPLIT\_STREAMS Procedure | Splits one stream flowing from a capture process off from all of the other streams flowing from the capture process |

Note:

All subprograms commit unless specified otherwise.

---

### ADD\_COLUMN Procedure

This procedure either adds or removes a declarative rule-based transformation which adds a column to a row logical change record (row LCR) that satisfies the specified rule.

For the transformation to be performed when the specified rule evaluates to `TRUE`, the rule must be in the positive rule set of an Oracle Streams client. Oracle Streams clients include capture processes, synchronous captures, propagations, apply processes, and messaging clients.

This procedure is overloaded. The `column_value` and `column_function` parameters are mutually exclusive.

Note:

- `ADD_COLUMN` transformations cannot add columns of the following data types: `BLOB`, `CLOB`, `NCLOB`, `BFILE`, `LONG`, `LONG` `RAW`, `ROWID`, user-defined types (including object types, `REF` s, varrays, nested tables), and Oracle-supplied types (including any types, XML types, spatial types, and media types).
- Declarative transformations can transform row LCRs only. These row LCRs can be captured by a capture process, captured by a synchronous capture, or constructed and enqueued by an application. Therefore, a DML rule must be specified when you run this procedure. If a DDL is specified, then the procedure raises an error.

See Also:

[Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_transform.htm#STRMS151) for more information about declarative rule-based transformations

Syntax

```
DBMS_STREAMS_ADM.ADD_COLUMN(
   rule_name     IN  VARCHAR2,
   table_name    IN  VARCHAR2,
   column_name   IN  VARCHAR2,
   column_value  IN  ANYDATA,
   value_type    IN  VARCHAR2     DEFAULT 'NEW',
   step_number   IN  NUMBER       DEFAULT 0,
   operation     IN  VARCHAR2     DEFAULT 'ADD');
```
```
DBMS_STREAMS_ADM.ADD_COLUMN(
   rule_name        IN  VARCHAR2,
   table_name       IN  VARCHAR2,
   column_name      IN  VARCHAR2,
   column_function  IN  VARCHAR2,
   value_type       IN  VARCHAR2     DEFAULT 'NEW',
   step_number      IN  NUMBER       DEFAULT 0,
   operation        IN  VARCHAR2     DEFAULT 'ADD');
```

Parameters

Table 145-3 ADD\_COLUMN Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_name` | The name of the rule, specified as `[``schema_name``.]` `rule_name`. If `NULL`, then the procedure raises an error.  For example, to specify a rule in the `hr` schema named `employees12`, enter `hr.employees12`. If the schema is not specified, then the current user is the default. |
| `table_name` | The name of the table to which the column is added in the row LCR, specified as `[``schema_name``.]` `object_name`. For example, `hr.employees`. If the schema is not specified, then the current user is the default. |
| `column_name` | The name of the column added to each row LCR that satisfies the rule. |
| `column_value` | The value of the added column. Specify the appropriate `ANYDATA` function for the column data type and the column value. For example, if the data type of the column being added is `NUMBER` and the value is `NULL`, then specify the `ANYDATA.ConvertNumber(NULL)` function.  This parameter cannot be specified if the `column_function` parameter is specified. |
| `column_function` | Either the `'SYSDATE'` or the `'SYSTIMESTAMP'` SQL function.  The `'SYSDATE'` SQL function places the current date and time set for the operating system on which the database resides. The data type of the returned value is `DATE`, and the format returned depends on the value of the `NLS_DATE_FORMAT` initialization parameter.  The `'SYSTIMESTAMP'` SQL function returns the system date, including fractional seconds and time zone, of the system on which the database resides. The return type is `TIMESTAMP` `WITH` `TIME` `ZONE`.  The function executes when the rule evaluates to `TRUE`.  This parameter cannot be specified if the `column_value` parameter is specified. |
| `value_type` | Specify `'NEW'` to add the column to the new values in the row LCR.  Specify `'OLD'` to add the column to the old values in the row LCR. |
| `step_number` | The order of execution of the transformation.  See Also: [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_transform.htm#STRMS145) for more information about transformation ordering |
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

---

### ADD\_GLOBAL\_PROPAGATION\_RULES Procedure

This procedure either adds global rules to the positive rule set for a propagation, or adds global rules to the negative rule set for a propagation, and creates the specified propagation if it does not exist.

This procedure is overloaded. One version of this procedure contains two `OUT` parameters, and the other does not.

Syntax

```
DBMS_STREAMS_ADM.ADD_GLOBAL_PROPAGATION_RULES(
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

DBMS_STREAMS_ADM.ADD_GLOBAL_PROPAGATION_RULES(
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

Table 145-4 ADD\_GLOBAL\_PROPAGATION\_RULES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `streams_name` | The name of the propagation. Do not specify an owner.  If the specified propagation does not exist, then the procedure creates it automatically.  If `NULL` and a propagation exists for the same source queue and destination queue (including database link), then the procedure uses this propagation.  If `NULL` and no propagation exists for the same source queue and destination queue (including database link), then the procedure creates a propagation automatically with a system-generated name. |
| `source_queue_name` | The name of the source queue, specified as `[``schema_name``.]` `queue_name`. The current database must contain the source queue, and the queue must be `ANYDATA` type.  For example, to specify a source queue named `streams_queue` in the `strmadmin` schema, enter `strmadmin.streams_queue` for this parameter.  If the schema is not specified, then the current user is the default. |
| `destination_queue_name` | The name of the destination queue, including a database link, specified as `[``schema_name``.]` `queue_name` `[``@dblink_name``]`, if the destination queue is in a remote database. The queue must be `ANYDATA` type.  For example, to specify a destination queue named `streams_queue` in the `strmadmin` schema and use a database link named `dbs2.net`, enter `strmadmin.streams_queue@dbs2.net` for this parameter.  If the schema is not specified, then the current user is the default.  If the database link is omitted, then the procedure uses the global name of the current database, and the source queue and destination queue must be in the same database.  Note: Connection qualifiers are not allowed. |
| `include_dml` | If `TRUE`, then the procedure creates a rule for DML changes. If `FALSE`, then the procedure does not create a DML rule. `NULL` is not permitted. |
| `include_ddl` | If `TRUE`, then the procedure creates a rule for DDL changes. If `FALSE`, then the procedure does not create a DDL rule. `NULL` is not permitted. |
| `include_tagged_lcr` | If `TRUE`, then the procedure does not add a condition regarding Oracle Streams tags to the generated rules. Therefore, these rules can evaluate to `TRUE` regardless of whether a logical change record (LCR) has a non- `NULL` tag. If the rules are added to the positive rule set for the propagation, then an LCR is always considered for propagation, regardless of whether it has a non- `NULL` tag. If the rules are added to a positive rule set, then setting this parameter to `TRUE` is appropriate for a full (for example, standby) copy of a database. If the rules are added to the negative rule set for the propagation, then whether an LCR is discarded does not depend on the tag for the LCR.  If `FALSE`, then the procedure adds a condition to each generated rule that causes the rule to evaluate to `TRUE` only if an LCR has a `NULL` Oracle Streams tag. If the rules are added to the positive rule set for the propagation, then an LCR is considered for propagation only when the LCR contains a `NULL` tag. If the rules are added to a positive rule set, then setting this parameter to `FALSE` might be appropriate in update-anywhere configurations to avoid sending a change back to its source database. If the rules are added to the negative rule set for the propagation, then an LCR can be discarded only if it has a `NULL` tag.  Usually, specify `TRUE` for this parameter if the `inclusion_rule` parameter is set to `FALSE`.  See Also: [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/rep_tags.htm#STREP008) for more information about tags |
| `source_database` | The global name of the source database. The source database is where the changes originated. If `NULL`, then the procedure does not add a condition regarding the source database to the generated rules.  If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify `DBS1` and the domain is `.NET`, then the procedure specifies `DBS1.NET` automatically.  Oracle recommends that you specify a source database for propagation rules. |
| `dml_rule_name` | If `include_dml` is `TRUE`, then this parameter contains the DML rule name.  If `include_dml` is `FALSE`, then this parameter contains a `NULL`. |
| `ddl_rule_name` | If `include_ddl` is `TRUE`, then this parameter contains the DDL rule name.  If `include_ddl` is `FALSE`, then this parameter contains a `NULL`. |
| `inclusion_rule` | If `inclusion_rule` is `TRUE`, then the procedure adds the rules to the positive rule set for the propagation.  If `inclusion_rule` is `FALSE`, then the procedure adds the rules to the negative rule set for the propagation.  In either case, the system creates the rule set if it does not exist. |
| `and_condition` | If non- `NULL`, appends the specified condition to the system-generated rule condition using an `AND` clause in the following way:  ``` (system_condition) AND (and_condition) ```  The variable in the specified condition must be `:lcr`. For example, to specify that the global rules generated by the procedure evaluate to `TRUE` only if the Oracle Streams tag is the hexadecimal equivalent of `'02'`, specify the following condition:  ``` :lcr.get_tag() = HEXTORAW(''02'') ```  The `:lcr` in the specified condition is converted to `:dml` or `:ddl`, depending on the rule that is being generated. If you are specifying an LCR member subprogram that is dependent on the LCR type (row or DDL), then make sure the procedure only generates the appropriate rule.  Specifically, if you specify an LCR member subprogram that is valid only for row LCRs, then specify `TRUE` for the `include_dml` parameter and `FALSE` for the `include_ddl` parameter. If you specify an LCR member subprogram that is valid only for DDL LCRs, then specify `FALSE` for the `include_dml` parameter and `TRUE` for the `include_ddl` parameter.  See Also: [Chapter 249, "Logical Change Record TYPEs"](t_lcr.md) |
| `queue_to_queue` | If `TRUE` or `NULL`, then a new propagation created by this procedure is a queue to queue propagation. A queue-to-queue propagation always has its own propagation job and uses a service for automatic failover when the destination queue is a buffered queue in an Oracle Real Application Clusters (Oracle RAC) database.  If `FALSE`, then a new propagation created by this procedure is a queue-to-dblink propagation. A queue-to-dblink propagation can share a propagation job with other propagations that use the same database link and does not support automatic failover in an Oracle RAC environment.  The procedure cannot change the queue to queue property of an exiting propagation. If the specified propagation exists, then the procedure behaves in the following way for each setting:  - If `TRUE` and the specified propagation is not a queue to queue propagation, then the procedure raises an error. - If `FALSE` and the specified propagation is a queue to queue propagation, then the procedure raises an error. - If `NULL`, then the procedure does not change the queue to queue property of the propagation.  See Also: [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_prop.htm#STRMS155) for more information about queue-to-queue propagations |

Usage Notes

This procedure configures propagation using the current user. Only one propagation is allowed between a particular source queue and destination queue.

This procedure creates DML and DDL rules automatically based on `include_dml` and `include_ddl` parameter values, respectively. Each rule has a system-generated rule name that consists of the database name with a sequence number appended to it. The sequence number is used to avoid naming conflicts. If the database name plus the sequence number is too long, then the database name is truncated. A propagation uses the rules for filtering.

See Also:

- "Operational Notes" and "Propagation Rules for LCRs" for more information about the rules created by this procedure
- "Propagation User"

Examples

The following is an example of a global rule condition created for DML changes:

```
(:dml.is_null_tag() = 'Y' and :dml.get_source_database_name() = 'DBS1.NET' )
```

---

### ADD\_GLOBAL\_RULES Procedure

This procedure adds rules to a rule set of one of the following types of Oracle Streams clients:

- When the `streams_type` parameter is set to `capture`, this procedure adds capture process rules for capturing changes to an entire database. See "Capture Process Rules for Changes in the Redo Log" for more information about these rules.
- When the `streams_type` parameter is set to `apply` and the `streams_name` parameter specifies the name of an apply process, this procedure adds apply process rules for applying all logical change records (LCRs) in a queue. The rules can specify that the LCRs must be from a particular source database. See "Apply Process Rules for LCRs" for more information about these rules.
- When the `streams_type` parameter is set to `dequeue`, this procedure adds messaging client rules for dequeuing all persistent LCRs from a queue. The rules can specify that the LCRs must be from a particular source database. See "Messaging Client Rules for LCRs" for more information about these rules.

This procedure creates the specified capture process, apply process, or messaging client if it does not exist.

This procedure is overloaded. One version of this procedure contains two `OUT` parameters, and the other does not.

Caution:

If you add global rules to the positive rule set for a capture process, then make sure you add rules to the negative capture process rule set to exclude database objects that are not support by Oracle Streams. Query the `DBA_STREAMS_UNSUPPORTED` data dictionary view to determine which database objects are not supported by Oracle Streams. If unsupported database objects are not excluded, then capture errors will result.

Note:

Currently, messaging clients cannot dequeue buffered messages.

Syntax

```
DBMS_STREAMS_ADM.ADD_GLOBAL_RULES(
   streams_type        IN   VARCHAR2,
   streams_name        IN   VARCHAR2  DEFAULT NULL,
   queue_name          IN   VARCHAR2  DEFAULT 'streams_queue',
   include_dml         IN   BOOLEAN   DEFAULT TRUE,
   include_ddl         IN   BOOLEAN   DEFAULT FALSE,
   include_tagged_lcr  IN   BOOLEAN   DEFAULT FALSE,
   source_database     IN   VARCHAR2  DEFAULT NULL,
   dml_rule_name       OUT  VARCHAR2,
   ddl_rule_name       OUT  VARCHAR2,
   inclusion_rule      IN   BOOLEAN   DEFAULT TRUE,
   and_condition       IN   VARCHAR2  DEFAULT NULL);

DBMS_STREAMS_ADM.ADD_GLOBAL_RULES(
   streams_type        IN   VARCHAR2,
   streams_name        IN   VARCHAR2  DEFAULT NULL,
   queue_name          IN   VARCHAR2  DEFAULT 'streams_queue',
   include_dml         IN   BOOLEAN   DEFAULT TRUE,
   include_ddl         IN   BOOLEAN   DEFAULT FALSE,
   include_tagged_lcr  IN   BOOLEAN   DEFAULT FALSE,
   source_database     IN   VARCHAR2  DEFAULT NULL,
   inclusion_rule      IN   BOOLEAN   DEFAULT TRUE,
   and_condition       IN   VARCHAR2  DEFAULT NULL);
```

Parameters

Table 145-5 ADD\_GLOBAL\_RULES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `streams_type` | The type of Oracle Streams client:  - Specify `capture` for a capture process. - Specify `apply` for an apply process. - Specify `dequeue` for a messaging client. |
| `streams_name` | The name of the capture process, apply process, or messaging client. Do not specify an owner.  If `NULL`, if `streams_type` is `capture` or `dequeue`, and if one relevant capture process or messaging client for the queue exists, then the relevant Oracle Streams client is used. If no relevant Oracle Streams client exists for the queue, then an Oracle Streams client is created automatically with a system-generated name. If `NULL` and multiple Oracle Streams clients of the specified `streams_type` for the queue exist, then the procedure raises an error.  If `NULL`, if `streams_type` is `apply`, and if one relevant apply process exists, then the procedure uses the relevant apply process. The relevant apply process is identified in one of the following ways:  - If one existing apply process has the source database specified in `source_database` and uses the queue specified in `queue_name`, then the procedure uses this apply process. - If `source_database` is `NULL` and one existing apply process is using the queue specified in `queue_name`, then the procedure uses this apply process.  If `NULL` and no relevant apply process exists, then the procedure creates an apply process automatically with a system-generated name.  If `NULL` and multiple relevant apply processes exist, then the procedure raises an error.  Each apply process and messaging client must have a unique name. |
| `queue_name` | The name of the local queue, specified as `[``schema_name``.]` `queue_name`. The current database must contain the queue, and the queue must be `ANYDATA` type.  For example, to specify a queue named `streams_queue` in the `strmadmin` schema, enter `strmadmin.streams_queue` for this parameter. If the schema is not specified, then the current user is the default.  For capture process rules, this is the queue into which a capture process enqueues LCRs. For apply process rules, this is the queue from which an apply process dequeues messages. For messaging client rules, this is the queue from which a messaging client dequeues messages. |
| `include_dml` | If `TRUE`, then the procedure creates a rule for DML changes. If `FALSE`, then the procedure does not create a DML rule. `NULL` is not permitted. |
| `include_ddl` | If `TRUE`, then the procedure creates a rule for DDL changes. If `FALSE`, then the procedure does not create a DDL rule. `NULL` is not permitted. |
| `include_tagged_lcr` | If `TRUE`, then the procedure does not add a condition regarding Oracle Streams tags to the generated rules. Therefore, these rules can evaluate to `TRUE` regardless of whether a redo entry or LCR has a non- `NULL` tag. If the rules are added to the positive rule set for the process, then a redo entry is always considered for capture, and an LCR is always considered for apply, regardless of whether the redo entry or LCR has a non- `NULL` tag. If the rules are added to a positive rule set, then setting this parameter to `TRUE` is appropriate for a full (for example, standby) copy of a database. If the rules are added to the negative rule set for the process, then whether a redo entry or LCR is discarded does not depend on the tag.  If `FALSE`, then the procedure adds a condition to each generated rule that causes the rule to evaluate to `TRUE` only if a redo entry or LCR has a `NULL` Oracle Streams tag. If the rules are added to the positive rule set for the process, then a redo entry is considered for capture, and an LCR is considered for apply, only when the redo entry or LCR contains a `NULL` tag. If the rules are added to a positive rule set, then setting this parameter to `FALSE` might be appropriate in update-anywhere configurations to avoid sending a change back to its source database. If the rules are added to the negative rule set for the process, then a redo entry or LCR can be discarded only if it has a `NULL` tag.  Usually, specify `TRUE` for this parameter if the `inclusion_rule` parameter is set to `FALSE`.  See Also: [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/rep_tags.htm#STREP008) for more information about tags |
| `source_database` | The global name of the source database. If `NULL`, then the procedure does not add a condition regarding the source database to the generated rules.  For capture process rules, specify `NULL` or the global name of the local database if you are creating a capture process locally at the source database. If you are adding rules to a downstream capture process rule set at a downstream database, then specify the source database of the changes that will be captured.  For apply process rules, specify the source database of the changes that will be applied by the apply process. The source database is the database where the changes originated. If an apply process applies captured messages, then the apply process can apply messages from only one capture process at one source database.  For messaging client rules, specify `NULL` if you do not want the rules created by this procedure to have a condition for the source database. Specify a source database if you want the rules created by this procedure to have a condition for the source database. The source database is part of the information in an LCR, and user-constructed LCRs might or might not have this information.  If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify `DBS1` and the domain is `.NET`, then the procedure specifies `DBS1.NET` automatically. |
| `dml_rule_name` | If `include_dml` is `TRUE`, then this parameter contains the DML rule name.  If `include_dml` is `FALSE`, then this parameter contains a `NULL`. |
| `ddl_rule_name` | If `include_ddl` is `TRUE`, then this parameter contains the DDL rule name.  If `include_ddl` is `FALSE`, then this parameter contains a `NULL`. |
| `inclusion_rule` | If `inclusion_rule` is `TRUE`, then the procedure adds the rules to the positive rule set for the Oracle Streams client.  If `inclusion_rule` is `FALSE`, then the procedure adds the rules to the negative rule set for the Oracle Streams client.  In either case, the system creates the rule set if it does not exist. |
| `and_condition` | If non- `NULL`, appends the specified condition to the system-generated rule condition using an `AND` clause in the following way:  ``` (system_condition) AND (and_condition) ```  The variable in the specified condition must be `:lcr`. For example, to specify that the global rules generated by the procedure evaluate to `TRUE` only if the Oracle Streams tag is the hexadecimal equivalent of `'02'`, specify the following condition:  ``` :lcr.get_tag() = HEXTORAW(''02'') ```  The `:lcr` in the specified condition is converted to `:dml` or `:ddl`, depending on the rule that is being generated. If you are specifying an LCR member subprogram that is dependent on the LCR type (row or DDL), then make sure this procedure only generates the appropriate rule.  Specifically, if you specify an LCR member subprogram that is valid only for row LCRs, then specify `TRUE` for the `include_dml` parameter and `FALSE` for the `include_ddl` parameter. If you specify an LCR member subprogram that is valid only for DDL LCRs, then specify `FALSE` for the `include_dml` parameter and `TRUE` for the `include_ddl` parameter.  See Also: [Chapter 249, "Logical Change Record TYPEs"](t_lcr.md) |

Usage Notes

This procedure creates DML and DDL rules automatically based on `include_dml` and `include_ddl` parameter values, respectively. Each rule has a system-generated rule name that consists of the database name with a sequence number appended to it. The sequence number is used to avoid naming conflicts. If the database name plus the sequence number is too long, then the database name is truncated. A capture process, apply process, or messaging client uses the rules for filtering.

See Also:

- "Operational Notes"
- "Security Model"

Examples

The following is an example of a global rule condition created for DML changes:

```
(:dml.is_null_tag() = 'Y' and :dml.get_source_database_name() = 'DBS1.NET' )
```

---

### ADD\_MESSAGE\_PROPAGATION\_RULE Procedure

This procedure adds a message rule to the positive rule set for a propagation, or adds a message rule to the negative rule set for a propagation, and creates the specified propagation if it does not exist.

This procedure is overloaded. One version of this procedure contains the `OUT` parameter `rule_name`, and the other does not.

Syntax

```
DBMS_STREAMS_ADM.ADD_MESSAGE_PROPAGATION_RULE(
   message_type            IN   VARCHAR2,    
   rule_condition          IN   VARCHAR2,    
   streams_name            IN   VARCHAR2  DEFAULT NULL,    
   source_queue_name       IN   VARCHAR2,    
   destination_queue_name  IN   VARCHAR2,    
   inclusion_rule          IN   BOOLEAN   DEFAULT TRUE,
   rule_name               OUT  VARCHAR2,
   queue_to_queue          IN   BOOLEAN   DEFAULT NULL);

DBMS_STREAMS_ADM.ADD_MESSAGE_PROPAGATION_RULE(
   message_type            IN   VARCHAR2,    
   rule_condition          IN   VARCHAR2,    
   streams_name            IN   VARCHAR2  DEFAULT NULL,    
   source_queue_name       IN   VARCHAR2,    
   destination_queue_name  IN   VARCHAR2,    
   inclusion_rule          IN   BOOLEAN   DEFAULT TRUE,
   queue_to_queue          IN   BOOLEAN   DEFAULT NULL);
```

Parameters

Table 145-6 ADD\_MESSAGE\_PROPAGATION\_RULE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `message_type` | The type of the message. The type can be an Oracle built-in type, such as `VARCHAR2` or `NUMBER`, or it can be a user-defined type.  If the type is not an Oracle built-in type, then it is specified as `[``schema_name``.]` `type_name`. If the schema is not specified, then the current user is the default.  For example, to specify `VARCHAR2`, enter `VARCHAR2(``n``)`, where `n` is the size specification. To specify a type named `usr_msg` in the `strmadmin` schema, enter `strmadmin.usr_msg` for this parameter.  The following data types require a size specification: `VARCHAR2`, `NVARCHAR2`, and `RAW`.  See Also: [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/sql_elements001.htm#SQLRF0021) for more information about data types |
| `rule_condition` | The rule condition for this message type. The rule variable name specified in the rule condition must be the following:  ``` :msg ```  See Also: "Examples" |
| `streams_name` | The name of the propagation. Do not specify an owner.  If the specified propagation does not exist, then the procedure creates it automatically.  If `NULL` and a propagation exists for the same source queue and destination queue (including database link), then the procedure uses this propagation.  If `NULL` and no propagation exists for the same source queue and destination queue (including database link), then the procedure creates a propagation automatically with a system-generated name. |
| `source_queue_name` | The name of the source queue, specified as `[``schema_name``.]` `queue_name`. The current database must contain the source queue, and the queue must be `ANYDATA` type.  For example, to specify a source queue named `streams_queue` in the `strmadmin` schema, enter `strmadmin.streams_queue` for this parameter.  If the schema is not specified, then the current user is the default. |
| `destination_queue_name` | The name of the destination queue, including a database link, specified as `[``schema_name``.]` `queue_name` `[``@dblink_name``]`, if the destination queue is in a remote database. The queue must be `ANYDATA` type.  For example, to specify a destination queue named `streams_queue` in the `strmadmin` schema and use a database link named `dbs2.net`, enter `strmadmin.streams_queue@dbs2.net` for this parameter.  If the schema is not specified, then the current user is the default.  If the database link is omitted, then the procedure uses the global name of the current database, and the source queue and destination queue must be in the same database.  Note: Connection qualifiers are not allowed. |
| `inclusion_rule` | If `inclusion_rule` is `TRUE`, then the procedure adds the rule to the positive rule set for the propagation.  If `inclusion_rule` is `FALSE`, then the procedure adds the rule to the negative rule set for the propagation.  In either case, the system creates the rule set if it does not exist. |
| `rule_name` | Contains the rule name |
| `queue_to_queue` | If `TRUE` or `NULL`, then a new propagation created by this procedure is a queue to queue propagation. A queue-to-queue propagation always has its own propagation job and uses a service for automatic failover when the destination queue is a buffered queue in an Oracle Real Application Clusters (Oracle RAC) database.  If `FALSE`, then a new propagation created by this procedure is a queue-to-dblink propagation. A queue-to-dblink propagation can share a propagation job with other propagations that use the same database link and does not support automatic failover in an Oracle RAC environment.  This procedure cannot change the queue to queue property of an exiting propagation. If the specified propagation exists, then the procedure behaves in the following way for each setting:  - If `TRUE` and the specified propagation is not a queue to queue propagation, then the procedure raises an error. - If `FALSE` and the specified propagation is a queue to queue propagation, then the procedure raises an error. - If `NULL`, then the procedure does not change the queue to queue property of the propagation.  See Also: [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_prop.htm#STRMS155) for more information about queue-to-queue propagations |

Usage Notes

This procedure configures propagation using the current user. Only one propagation is allowed between a particular source queue and destination queue.

When you use this procedure to create a rule set for a message rule, the new rule set does not have an evaluation context. If no evaluation context exists for the specified message type, then this procedure creates a new evaluation context and associates it with the new rule. The evaluation context also has a system-generated name. If you create new rules that use an existing message type, then the new rules use the existing evaluation context for the message type.

See Also:

- "Operational Notes" and "Propagation Rules for User Messages" for more information about the rules created by this procedure
- "Propagation User"

Examples

Suppose the message type is `VARCHAR2(128)`. Given this type, the following rule condition can be specified:

```
':msg = ''HQ'''
```

This rule condition evaluates to `TRUE` if a user message of type `VARCHAR2(128)` has `HQ` for its value.

Suppose the message type is `usr_msg`, and that this type has the following attributes: `source_dbname`, `owner`, `name`, and `message`. Given this type, the following rule condition can be specified:

```
':msg.source_dbname = ''DBS1.NET'' AND ' || ':msg.owner = ''HR'' AND  ' ||
':msg.name = ''EMPLOYEES'''
```

This rule condition evaluates to `TRUE` if a user message of type `usr_msg` has `DBS1.NET` for its `source_dbname` attribute, `HR` for its `owner` attribute, and `EMPLOYEES` for its `name` attribute.

Note:

The quotation marks in the preceding examples are all single quotation marks.

---

### ADD\_MESSAGE\_RULE Procedure

This procedure adds a message rule to a rule set of one of the following types of Oracle Streams clients:

- When the `streams_type` parameter is set to `apply`, this procedure adds an apply process rule for dequeuing user messages of a specific message type from a queue. See "Apply Process Rules for User Messages" for more information about such rules.
- When the `streams_type` parameter is set to `dequeue`, this procedure adds a messaging client rule for dequeuing user messages of a specific message type from a queue. See "Messaging Client Rules for User Messages" for more information about such rules.

This procedure also creates the specified Oracle Streams client if it does not exist.

This procedure is overloaded. One version of this procedure contains the `OUT` parameter `rule_name`, and the other does not.

Note:

Currently, messaging clients cannot dequeue buffered messages.

Syntax

```
DBMS_STREAMS_ADM.ADD_MESSAGE_RULE(
   message_type    IN   VARCHAR2,    
   rule_condition  IN   VARCHAR2,    
   streams_type    IN   VARCHAR2,
   streams_name    IN   VARCHAR2  DEFAULT NULL,    
   queue_name      IN   VARCHAR2  DEFAULT 'streams_queue',    
   inclusion_rule  IN   BOOLEAN   DEFAULT TRUE,
   rule_name       OUT  VARCHAR2);

DBMS_STREAMS_ADM.ADD_MESSAGE_RULE(
   message_type    IN   VARCHAR2,    
   rule_condition  IN   VARCHAR2,    
   streams_type    IN   VARCHAR2,
   streams_name    IN   VARCHAR2  DEFAULT NULL,    
   queue_name      IN   VARCHAR2  DEFAULT 'streams_queue',    
   inclusion_rule  IN   BOOLEAN   DEFAULT TRUE);
```

Parameters

Table 145-7 ADD\_MESSAGE\_RULE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `message_type` | The type of the message. The type can be an Oracle built-in type, such as `VARCHAR2` or `NUMBER`, or it can be a user-defined type.  If the type is not an Oracle built-in type, then it is specified as `[``schema_name``.]` `type_name`. If the schema is not specified, then the current user is the default.  For example, to specify `VARCHAR2`, enter `VARCHAR2(``n``)`, where `n` is the size specification. To specify a type named `usr_msg` in the `strmadmin` schema, enter `strmadmin.usr_msg` for this parameter.  The following data types require a size specification: `VARCHAR2`, `NVARCHAR2`, and `RAW`.  See Also: [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/sql_elements001.htm#SQLRF0021) for more information about data types |
| `rule_condition` | The rule condition for this message type. The rule variable name specified in the rule condition must be the following:  ``` :msg ```  See Also: "Examples" |
| `streams_type` | The type of message consumer, either `apply` for apply process or `dequeue` for messaging client |
| `streams_name` | The name of the Oracle Streams apply process or messaging client.  If the specified `streams_type` is `apply`, then specify the name of the apply process. Do not specify an owner. If the specified apply process does not exist, then the procedure creates it automatically with a system-generated name.  If the specified `streams_type` is `dequeue`, then specify the messaging client. For example, if the user `strmadmin` is the messaging client, then specify `strmadmin`.  If `NULL` and a relevant apply process or messaging client for the queue exists, then the procedure uses the relevant apply process or messaging client. If `NULL` and multiple relevant apply processes or messaging clients for the queue exist, then the procedure raises an error.  If `NULL` and no Oracle Streams client of the specified `streams_type` exists for the queue, then the procedure creates an apply process or messaging client automatically with a system-generated name.  An apply process and a messaging client cannot have the same name. |
| `queue_name` | The name of the local queue from which messages will be dequeued, specified as `[``schema_name``.]` `queue_name`. The current database must contain the queue, and the queue must be `ANYDATA` type.  For example, to specify a queue named `streams_queue` in the `strmadmin` schema, enter `strmadmin.streams_queue` for this parameter. If the schema is not specified, then the current user is the default. |
| `inclusion_rule` | If `inclusion_rule` is `TRUE`, then the procedure adds the rule to the positive rule set for the apply process or messaging client.  If `inclusion_rule` is `FALSE`, then the procedure adds the rule to the negative rule set for the apply process or messaging client.  In either case, the system creates the rule set if it does not exist. |
| `rule_name` | Contains the rule name |

Usage Notes

If an apply process rule is added, then this procedure creates the apply process if it does not exist. An apply process created by this procedure can apply only user messages, and dequeued messages are sent to the message handler for the apply process. If a messaging client rule is added, then this procedure creates a messaging client if it does not exist.

When you use this procedure to create a rule set for a message rule, the new rule set does not have an evaluation context. If no evaluation context exists for the specified message type, then this procedure creates a new evaluation context and associates it with the new rule. The evaluation context also has a system-generated name. If you create new rules that use an existing message type, then the new rules use the existing evaluation context for the message type.

See Also:

- "Operational Notes"
- "Security Model"
- [ALTER\_APPLY Procedure](d_apply.md) for more information about setting a message handler for an apply process

Examples

Suppose the message type is `VARCHAR2(128)`. Given this type, the following rule condition can be specified:

```
':msg = ''HQ'''
```

This rule condition evaluates to `TRUE` if a user message of type `VARCHAR2(128)` has `HQ` for its value.

Suppose the message type is `usr_msg`, and that this type has the following attributes: `source_dbname`, `owner`, `name`, and `message`. Given this type, the following rule condition can be specified:

```
':msg.source_dbname = ''DBS1.NET'' AND ' || ':msg.owner = ''HR'' AND  ' ||
':msg.name = ''EMPLOYEES'''
```

This rule condition evaluates to `TRUE` if a user message of type `usr_msg` has `DBS1.NET` for its `source_dbname` attribute, `HR` for its `owner` attribute, and `EMPLOYEES` for its `name` attribute.

Note:

The quotation marks in the preceding examples are all single quotation marks.

---

### ADD\_SCHEMA\_PROPAGATION\_RULES Procedure

This procedure either adds schema rules to the positive rule set for a propagation, or adds schema rules to the negative rule set for a propagation, and creates the specified propagation if it does not exist.

This procedure is overloaded. One version of this procedure contains two `OUT` parameters, and the other does not.

Syntax

```
DBMS_STREAMS_ADM.ADD_SCHEMA_PROPAGATION_RULES(
   schema_name             IN   VARCHAR2,
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

DBMS_STREAMS_ADM.ADD_SCHEMA_PROPAGATION_RULES(
   schema_name             IN   VARCHAR2,
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

Table 145-8 ADD\_SCHEMA\_PROPAGATION\_RULES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the schema. For example, `hr`. |
| `streams_name` | The name of the propagation. Do not specify an owner.  If the specified propagation does not exist, then the procedure creates it automatically.  If `NULL` and a propagation exists for the same source queue and destination queue (including database link), then the procedure uses this propagation.  If `NULL` and no propagation exists for the same source queue and destination queue (including database link), then the procedure creates a propagation automatically with a system-generated name. |
| `source_queue_name` | The name of the source queue, specified as `[``schema_name``.]` `queue_name`. The current database must contain the source queue, and the queue must be `ANYDATA` type.  For example, to specify a source queue named `streams_queue` in the `strmadmin` schema, enter `strmadmin.streams_queue` for this parameter.  If the schema is not specified, then the current user is the default. |
| `destination_queue_name` | The name of the destination queue, including a database link, specified as `[``schema_name``.]` `queue_name` `[``@dblink_name``]`, if the destination queue is in a remote database. The queue must be `ANYDATA` type.  For example, to specify a destination queue named `streams_queue` in the `strmadmin` schema and use a database link named `dbs2.net`, enter `strmadmin.streams_queue@dbs2.net` for this parameter.  If the schema is not specified, then the current user is the default.  If the database link is omitted, then the procedure uses the global name of the current database, and the source queue and destination queue must be in the same database.  Note: Connection qualifiers are not allowed. |
| `include_dml` | If `TRUE`, then the procedure creates a rule for DML changes. If `FALSE`, then the procedure does not create a DML rule. `NULL` is not permitted. |
| `include_ddl` | If `TRUE`, then the procedure creates a rule for DDL changes. If `FALSE`, then the procedure does not create a DDL rule. `NULL` is not permitted. |
| `include_tagged_lcr` | If `TRUE`, then the procedure does not add a condition regarding Oracle Streams tags to the generated rules. Therefore, these rules can evaluate to `TRUE` regardless of whether a logical change record (LCR) has a non- `NULL` tag. If the rules are added to the positive rule set for the propagation, then an LCR is always considered for propagation, regardless of whether it has a non- `NULL` tag. If the rules are added to a positive rule set, then setting this parameter to `TRUE` is appropriate for a full (for example, standby) copy of a database. If the rules are added to the negative rule set for the propagation, then whether an LCR is discarded does not depend on the tag for the LCR.  If `FALSE`, then the procedure adds a condition to each generated rule that causes the rule to evaluate to `TRUE` only if an LCR has a `NULL` Oracle Streams tag. If the rules are added to the positive rule set for the propagation, then an LCR is considered for propagation only when the LCR contains a `NULL` tag. If the rules are added to a positive rule set, then setting this parameter to `FALSE` might be appropriate in update-anywhere configurations to avoid sending a change back to its source database. If the rules are added to the negative rule set for the propagation, then an LCR can be discarded only if it has a `NULL` tag.  Usually, specify `TRUE` for this parameter if the `inclusion_rule` parameter is set to `FALSE`.  See Also: [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/rep_tags.htm#STREP008) for more information about tags |
| `source_database` | The global name of the source database. The source database is where the change originated. If `NULL`, then the procedure does not add a condition regarding the source database to the generated rules.  If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify `DBS1` and the domain is `.NET`, then the procedure specifies `DBS1.NET` automatically.  Oracle recommends that you specify a source database for propagation rules. |
| `dml_rule_name` | If `include_dml` is `TRUE`, then this parameter contains the DML rule name.  If `include_dml` is `FALSE`, then this parameter contains a `NULL`. |
| `ddl_rule_name` | If `include_ddl` is `TRUE`, then this parameter contains the DDL rule name.  If `include_ddl` is `FALSE`, then this parameter contains a `NULL`. |
| `inclusion_rule` | If `inclusion_rule` is `TRUE`, then the procedure adds the rules to the positive rule set for the propagation.  If `inclusion_rule` is `FALSE`, then the procedure adds the rules to the negative rule set for the propagation.  In either case, the system creates the rule set if it does not exist. |
| `and_condition` | If non- `NULL`, appends the specified condition to the system-generated rule condition using an `AND` clause in the following way:  ``` (system_condition) AND (and_condition) ```  The variable in the specified condition must be `:lcr`. For example, to specify that the schema rules generated by the procedure evaluate to `TRUE` only if the Oracle Streams tag is the hexadecimal equivalent of `'02'`, specify the following condition:  ``` :lcr.get_tag() = HEXTORAW(''02'') ```  The `:lcr` in the specified condition is converted to `:dml` or `:ddl`, depending on the rule that is being generated. If you are specifying an LCR member subprogram that is dependent on the LCR type (row or DDL), then make sure this procedure only generates the appropriate rule.  Specifically, if you specify an LCR member subprogram that is valid only for row LCRs, then specify `TRUE` for the `include_dml` parameter and `FALSE` for the `include_ddl` parameter. If you specify an LCR member subprogram that is valid only for DDL LCRs, then specify `FALSE` for the `include_dml` parameter and `TRUE` for the `include_ddl` parameter.  See Also: [Chapter 249, "Logical Change Record TYPEs"](t_lcr.md) |
| `queue_to_queue` | If `TRUE` or `NULL`, then a new propagation created by this procedure is a queue to queue propagation. A queue-to-queue propagation always has its own propagation job and uses a service for automatic failover when the destination queue is a buffered queue in an Oracle Real Application Clusters (Oracle RAC) database.  If `FALSE`, then a new propagation created by this procedure is a queue-to-dblink propagation. A queue-to-dblink propagation can share a propagation job with other propagations that use the same database link and does not support automatic failover in an Oracle RAC environment.  This procedure cannot change the queue to queue property of an exiting propagation. If the specified propagation exists, then the procedure behaves in the following way for each setting:  - If `TRUE` and the specified propagation is not a queue to queue propagation, then the procedure raises an error. - If `FALSE` and the specified propagation is a queue to queue propagation, then the procedure raises an error. - If `NULL`, then the procedure does not change the queue to queue property of the propagation.  See Also: [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_prop.htm#STRMS155) for more information about queue-to-queue propagations |

Usage Notes

This procedure configures propagation using the current user. Only one propagation is allowed between a particular source queue and destination queue.

This procedure creates DML and DDL rules automatically based on `include_dml` and `include_ddl` parameter values, respectively. Each rule has a system-generated rule name that consists of the schema name with a sequence number appended to it. The sequence number is used to avoid naming conflicts. If the schema name plus the sequence number is too long, then the schema name is truncated. A propagation uses the rules for filtering.

See Also:

- "Operational Notes" and "Propagation Rules for LCRs" for more information about the rules created by this procedure
- "Propagation User"

Examples

The following is an example of a schema rule condition created for DML changes:

```
((:dml.get_object_owner() = 'HR') and :dml.is_null_tag() = 'Y' 
and :dml.get_source_database_name() = 'DBS1.NET' )
```

---

### ADD\_SCHEMA\_RULES Procedure

This procedures adds rules to a rule set of one of the following types of Oracle Streams clients:

- When the `streams_type` parameter is set to `capture`, this procedure adds capture process rules for capturing changes to a specified schema. See "Capture Process Rules for Changes in the Redo Log" for more information about these rules.
- When the `streams_type` parameter is set to `apply` and the `streams_name` parameter specifies the name of an apply process, this procedure adds apply process rules for applying logical change records (LCRs) in a queue that contain changes to a specified schema. The rules can specify that the LCRs must be from a particular source database. See "Apply Process Rules for LCRs" for more information about these rules.
- When the `streams_type` parameter is set to `dequeue`, this procedure adds messaging client rules for dequeuing persistent LCRs from a queue that contain changes to a specified schema. The rules can specify that the LCRs must be from a particular source database. See "Messaging Client Rules for LCRs" for more information about these rules.

This procedure creates the specified capture process, apply process, or messaging client if it does not exist.

This procedure is overloaded. One version of this procedure contains two `OUT` parameters, and the other does not.

Caution:

If you add schema rules to the positive rule set for a capture process, then make sure you add rules to the negative capture process rule set to exclude database objects in the schema that are not support by Oracle Streams. Query the `DBA_STREAMS_UNSUPPORTED` data dictionary view to determine which database objects are not supported by Oracle Streams. If unsupported database objects are not excluded, then capture errors will result.

Note:

Currently, messaging clients cannot dequeue buffered messages.

Syntax

```
DBMS_STREAMS_ADM.ADD_SCHEMA_RULES(
   schema_name         IN   VARCHAR2,
   streams_type        IN   VARCHAR2,
   streams_name        IN   VARCHAR2  DEFAULT NULL,
   queue_name          IN   VARCHAR2  DEFAULT 'streams_queue',
   include_dml         IN   BOOLEAN   DEFAULT TRUE,
   include_ddl         IN   BOOLEAN   DEFAULT FALSE,
   include_tagged_lcr  IN   BOOLEAN   DEFAULT FALSE,
   source_database     IN   VARCHAR2  DEFAULT NULL,
   dml_rule_name       OUT  VARCHAR2,
   ddl_rule_name       OUT  VARCHAR2,
   inclusion_rule      IN   BOOLEAN   DEFAULT TRUE,
   and_condition       IN   VARCHAR2  DEFAULT NULL);

DBMS_STREAMS_ADM.ADD_SCHEMA_RULES(
   schema_name         IN   VARCHAR2,
   streams_type        IN   VARCHAR2,
   streams_name        IN   VARCHAR2  DEFAULT NULL,
   queue_name          IN   VARCHAR2  DEFAULT 'streams_queue',
   include_dml         IN   BOOLEAN   DEFAULT TRUE,
   include_ddl         IN   BOOLEAN   DEFAULT FALSE,
   include_tagged_lcr  IN   BOOLEAN   DEFAULT FALSE,
   source_database     IN   VARCHAR2  DEFAULT NULL,
   inclusion_rule      IN   BOOLEAN   DEFAULT TRUE,
   and_condition       IN   VARCHAR2  DEFAULT NULL);
```

Parameters

Table 145-9 ADD\_SCHEMA\_RULES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the schema. For example, `hr`.  You can specify a schema that does not yet exist, because Oracle Streams does not validate the existence of the schema. |
| `streams_type` | The type of Oracle Streams client:  - Specify `capture` for a capture process. - Specify `apply` for an apply process. - Specify `dequeue` for a messaging client. |
| `streams_name` | The name of the capture process, apply process, or messaging client. Do not specify an owner.  If `NULL`, if `streams_type` is `capture` or `dequeue`, and if one relevant capture process or messaging client for the queue exists, then the relevant Oracle Streams client is used. If no relevant Oracle Streams client exists for the queue, then an Oracle Streams client is created automatically with a system-generated name. If `NULL` and multiple Oracle Streams clients of the specified `streams_type` for the queue exist, then the procedure raises an error.  If `NULL`, if `streams_type` is `apply`, and if one relevant apply process exists, then the procedure uses the relevant apply process. The relevant apply process is identified in one of the following ways:  - If one existing apply process has the source database specified in `source_database` and uses the queue specified in `queue_name`, then the procedure uses this apply process. - If `source_database` is `NULL` and one existing apply process is using the queue specified in `queue_name`, then the procedure uses this apply process.  If `NULL` and no relevant apply process exists, then the procedure creates an apply process automatically with a system-generated name.  If `NULL` and multiple relevant apply processes exist, then the procedure raises an error.  Each apply process and messaging client must have a unique name. |
| `queue_name` | The name of the local queue, specified as `[``schema_name``.]` `queue_name`. The current database must contain the queue, and the queue must be `ANYDATA` type.  For example, to specify a queue named `streams_queue` in the `strmadmin` schema, enter `strmadmin.streams_queue` for this parameter. If the schema is not specified, then the current user is the default.  For capture process rules, this is the queue into which a capture process enqueues LCRs. For apply process rules, this is the queue from which an apply process dequeues messages. For messaging client rules, this is the queue from which a messaging client dequeues messages. |
| `include_dml` | If `TRUE`, then the procedure creates a rule for DML changes. If `FALSE`, then the procedure does not create a DML rule. `NULL` is not permitted. |
| `include_ddl` | If `TRUE`, then the procedure creates a rule for DDL changes. If `FALSE`, then the procedure does not create a DDL rule. `NULL` is not permitted. |
| `include_tagged_lcr` | If `TRUE`, then the procedure does not add a condition regarding Oracle Streams tags to the generated rules. Therefore, these rules can evaluate to `TRUE` regardless of whether a redo entry or LCR has a non- `NULL` tag. If the rules are added to the positive rule set for the process, then a redo entry is always considered for capture, and an LCR is always considered for apply, regardless of whether the redo entry or LCR has a non- `NULL` tag. If the rules are added to a positive rule set, then setting this parameter to `TRUE` is appropriate for a full (for example, standby) copy of a database. If the rules are added to the negative rule set for the process, then whether a redo entry or LCR is discarded does not depend on the tag.  If `FALSE`, then the procedure adds a condition to each generated rule that causes the rule to evaluate to `TRUE` only if a redo entry or LCR has a `NULL` Oracle Streams tag. If the rules are added to the positive rule set for the process, then a redo entry is considered for capture, and an LCR is considered for apply, only when the redo entry or LCR contains a `NULL` tag. If the rules are added to a positive rule set, then setting this parameter to `FALSE` might be appropriate in update-anywhere configurations to avoid sending a change back to its source database. If the rules are added to the negative rule set for the process, then a redo entry or LCR can be discarded only if it has a `NULL` tag.  Usually, specify `TRUE` for this parameter if the `inclusion_rule` parameter is set to `FALSE`.  See Also: [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/rep_tags.htm#STREP008) for more information about tags |
| `source_database` | The global name of the source database. If `NULL`, then the procedure does not add a condition regarding the source database to the generated rules.  For capture process rules, specify `NULL` or the global name of the local database if you are creating a capture process locally at the source database. If you are adding rules to a downstream capture process rule set at a downstream database, then specify the source database of the changes that will be captured.  For apply process rules, specify the source database of the changes that will be applied by the apply process. The source database is the database where the changes originated. If an apply process applies captured messages, then the apply process can apply messages from only one capture process at one source database.  For messaging client rules, specify `NULL` if you do not want the rules created by this procedure to have a condition for the source database. Specify a source database if you want the rules created by this procedure to have a condition for the source database. The source database is part of the information in an LCR, and user-constructed LCRs might or might not have this information.  If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify `DBS1` and the domain is `.NET`, then the procedure specifies `DBS1.NET` automatically. |
| `dml_rule_name` | If `include_dml` is `TRUE`, then this parameter contains the DML rule name.  If `include_dml` is `FALSE`, then this parameter contains a `NULL`. |
| `ddl_rule_name` | If `include_ddl` is `TRUE`, then this parameter contains the DDL rule name.  If `include_ddl` is `FALSE`, then this parameter contains a `NULL`. |
| `inclusion_rule` | If `inclusion_rule` is `TRUE`, then the procedure adds the rules to the positive rule set for the Oracle Streams client.  If `inclusion_rule` is `FALSE`, then the procedure adds the rules to the negative rule set for the Oracle Streams client.  In either case, the system creates the rule set if it does not exist. |
| `and_condition` | If non- `NULL`, appends the specified condition to the system-generated rule condition using an `AND` clause in the following way:  ``` (system_condition) AND (and_condition) ```  The variable in the specified condition must be `:lcr`. For example, to specify that the schema rules generated by the procedure evaluate to `TRUE` only if the Oracle Streams tag is the hexadecimal equivalent of `'02'`, specify the following condition:  ``` :lcr.get_tag() = HEXTORAW(''02'') ```  The `:lcr` in the specified condition is converted to `:dml` or `:ddl`, depending on the rule that is being generated. If you are specifying an LCR member subprogram that is dependent on the LCR type (row or DDL), then make sure this procedure only generates the appropriate rule.  Specifically, if you specify an LCR member subprogram that is valid only for row LCRs, then specify `TRUE` for the `include_dml` parameter and `FALSE` for the `include_ddl` parameter. If you specify an LCR member subprogram that is valid only for DDL LCRs, then specify `FALSE` for the `include_dml` parameter and `TRUE` for the `include_ddl` parameter.  See Also: [Chapter 249, "Logical Change Record TYPEs"](t_lcr.md) |

Usage Notes

This procedure creates DML and DDL rules automatically based on `include_dml` and `include_ddl` parameter values, respectively. Each rule has a system-generated rule name that consists of the schema name with a sequence number appended to it. The sequence number is used to avoid naming conflicts. If the schema name plus the sequence number is too long, then the schema name is truncated. A capture process, apply process, or messaging client uses the rules for filtering.

See Also:

- "Operational Notes"
- "Security Model"

Examples

The following is an example of a schema rule condition created for DML changes:

```
((:dml.get_object_owner() = 'HR') and :dml.is_null_tag() = 'Y' 
and :dml.get_source_database_name() = 'DBS1.NET' )
```

---

### ADD\_SUBSET\_PROPAGATION\_RULES Procedure

This procedures adds propagation rules that propagate the logical change records (LCRs) related to a subset of the rows in the specified table in a source queue to a destination queue, and creates the specified propagation if it does not exist.

This procedure is overloaded. One version of this procedure contains three `OUT` parameters, and the other does not.

Syntax

```
DBMS_STREAMS_ADM.ADD_SUBSET_PROPAGATION_RULES(
   table_name               IN   VARCHAR2,
   dml_condition            IN   VARCHAR2,
   streams_name             IN   VARCHAR2  DEFAULT NULL,
   source_queue_name        IN   VARCHAR2,
   destination_queue_name   IN   VARCHAR2,
   include_tagged_lcr       IN   BOOLEAN   DEFAULT FALSE,
   source_database          IN   VARCHAR2  DEFAULT NULL,
   insert_rule_name         OUT  VARCHAR2,
   update_rule_name         OUT  VARCHAR2,
   delete_rule_name         OUT  VARCHAR2,
   queue_to_queue           IN   BOOLEAN   DEFAULT NULL);

DBMS_STREAMS_ADM.ADD_SUBSET_PROPAGATION_RULES(
   table_name               IN   VARCHAR2,
   dml_condition            IN   VARCHAR2,
   streams_name             IN   VARCHAR2  DEFAULT NULL,
   source_queue_name        IN   VARCHAR2,
   destination_queue_name   IN   VARCHAR2,
   include_tagged_lcr       IN   BOOLEAN   DEFAULT FALSE,
   source_database          IN   VARCHAR2  DEFAULT NULL,
   queue_to_queue           IN   BOOLEAN   DEFAULT NULL);
```

Parameters

Table 145-10 ADD\_SUBSET\_PROPAGATION\_RULES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `table_name` | The name of the table specified as `[``schema_name``.]` `object_name`. For example, `hr.employees`. If the schema is not specified, then the current user is the default.  The specified table must exist in the same database as the propagation. Also, the specified table cannot have any LOB, `LONG`, `LONG` `RAW`, or `XMLType` columns currently or in the future. |
| `dml_condition` | The subset condition. Specify this condition similar to the way you specify conditions in a `WHERE` clause in SQL.  For example, to specify rows in the `hr.employees` table where the `salary` is greater than `4000` and the `job_id` is `SA_MAN`, enter the following as the condition:  `' salary > 4000 and job_id = ''SA_MAN'' '`  Note: The quotation marks in the preceding example are all single quotation marks. |
| `streams_name` | The name of the propagation. Do not specify an owner.  If the specified propagation does not exist, then the procedure creates it automatically.  If `NULL` and a propagation exists for the same source queue and destination queue (including database link), then the procedure uses this propagation.  If `NULL` and no propagation exists for the same source queue and destination queue (including database link), then the procedure creates a propagation automatically with a system-generated name. |
| `source_queue_name` | The name of the source queue, specified as `[``schema_name``.]` `queue_name`. The current database must contain the source queue, and the queue must be `ANYDATA` type.  For example, to specify a source queue named `streams_queue` in the `strmadmin` schema, enter `strmadmin.streams_queue` for this parameter.  If the schema is not specified, then the current user is the default. |
| `destination_queue_name` | The name of the destination queue, including a database link, specified as `[``schema_name``.]` `queue_name` `[``@dblink_name``]`, if the destination queue is in a remote database. The queue must be `ANYDATA` type.  For example, to specify a destination queue named `streams_queue` in the `strmadmin` schema and use a database link named `dbs2.net`, enter `strmadmin.streams_queue@dbs2.net` for this parameter.  If the schema is not specified, then the current user is the default.  If the database link is omitted, then the procedure uses the global name of the current database, and the source queue and destination queue must be in the same database.  Note: Connection qualifiers are not allowed. |
| `include_tagged_lcr` | If `TRUE`, then an LCR is always considered for propagation, regardless of whether it has a non- `NULL` tag. This setting is appropriate for a full (for example, standby) copy of a database.  If `FALSE`, then an LCR is considered for propagation only when the LCR contains a `NULL` tag. A setting of `FALSE` is often specified in update-anywhere configurations to avoid sending a change back to its source database.  See Also: [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/rep_tags.htm#STREP008) for more information about tags |
| `source_database` | The global name of the source database. The source database is where the change originated. If `NULL`, then the procedure does not add a condition regarding the source database to the generated rules.  If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify `DBS1` and the domain is `.NET`, then the procedure specifies `DBS1.NET` automatically.  Oracle recommends that you specify a source database for propagation rules. |
| `insert_rule_name` | Contains the system-generated `INSERT` rule name. This rule handles inserts and updates that must be converted into inserts. |
| `update_rule_name` | Contains the system-generated `UPDATE` rule name. This rule handles updates that remain updates. |
| `delete_rule_name` | Contains the system-generated `DELETE` rule name. This rule handles deletes and updates that must be converted into deletes |
| `queue_to_queue` | If `TRUE` or `NULL`, then a new propagation created by this procedure is a queue to queue propagation. A queue-to-queue propagation always has its own propagation job and uses a service for automatic failover when the destination queue is a buffered queue in an Oracle Real Application Clusters (Oracle RAC) database.  If `FALSE`, then a new propagation created by this procedure is a queue-to-dblink propagation. A queue-to-dblink propagation can share a propagation job with other propagations that use the same database link and does not support automatic failover in an Oracle RAC environment.  This procedure cannot change the queue to queue property of an exiting propagation. If the specified propagation exists, then the procedure behaves in the following way for each setting:  - If `TRUE` and the specified propagation is not a queue to queue propagation, then the procedure raises an error. - If `FALSE` and the specified propagation is a queue to queue propagation, then the procedure raises an error. - If `NULL`, then the procedure does not change the queue to queue property of the propagation.  See Also: [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_prop.htm#STRMS155) for more information about queue-to-queue propagations |

Usage Notes

This procedure configures propagation using the current user. Only one propagation is allowed between a particular source queue and destination queue.

Running this procedure generates three rules for the specified propagation: one for `INSERT` statements, one for `UPDATE` statements, and one for `DELETE` statements. For `INSERT` and `DELETE` statements, only row LCRs that satisfy the condition specified for the `dml_condition` parameter are propagated. For `UPDATE` statements, the following variations are possible:

- If both the new and old values in a row LCR satisfy the specified `dml_condition`, then the row LCR is propagated without any changes.
- If neither the new or old values in a row LCR satisfy the specified `dml_condition`, then the row LCR is not propagated.
- If the old values for a row LCR satisfy the specified `dml_condition`, but the new values do not, then the update row LCR is converted into a delete row LCR.
- If the new values for a row LCR satisfy the specified `dml_condition`, but the old values do not, then the update row LCR is converted to an insert row LCR.

When an update is converted into an insert or a delete, it is called row migration.

A propagation uses the rules for filtering. If the propagation does not have a positive rule set, then the procedure creates a positive rule set automatically, and the rules for propagating changes to the table are added to the positive rule set. A subset rule can be added to positive rule set only, not to a negative rule set. Other rules in an existing positive rule set for the propagation are not affected. Additional rules can be added using either the `DBMS_STREAMS_ADM` package or the `DBMS_RULE_ADM` package.

Rules for `INSERT`, `UPDATE`, and `DELETE` statements are created automatically when you run this procedure, and these rules are given a system-generated rule name. Each rule has a system-generated rule name that consists of the table name with a sequence number appended to it. The sequence number is used to avoid naming conflicts. If the table name plus the sequence number is too long, then the table name is truncated. The `ADD_SUBSET_RULES` procedure is overloaded, and the system-generated rule names for `INSERT`, `UPDATE`, and `DELETE` statements are returned.

When you create propagation subset rules for a table, you should create an unconditional supplemental log group at the source database with all the columns in the table. Supplemental logging is required if an update must be converted to an insert. The propagation rule must have all the column values to be able to perform this conversion correctly.

Attention:

Subset rules should only reside in positive rule sets. You should not add subset rules to negative rule sets. Doing so might have unpredictable results because row migration would not be performed on LCRs that are not discarded by the negative rule set.

See Also:

- "Operational Notes" and "Propagation Rules for LCRs" for more information about the rules created by this procedure
- "Propagation User"

Examples

The following is an example of a rule condition created for filtering a row LCR containing an update operation when the `dml_condition` is `region_id = 2`, the `table_name` is `hr.regions`, and the `source_database` is `dbs1.net`:

```
:dml.get_object_owner()='HR' AND :dml.get_object_name()='REGIONS' 
AND :dml.is_null_tag()='Y' AND :dml.get_source_database_name()='DBS1.NET' 
AND :dml.get_command_type()='UPDATE' 
AND (:dml.get_value('NEW','"REGION_ID"') IS NOT NULL) 
AND (:dml.get_value('OLD','"REGION_ID"') IS NOT NULL) 
AND (:dml.get_value('OLD','"REGION_ID"').AccessNumber()=2) 
AND (:dml.get_value('NEW','"REGION_ID"').AccessNumber()=2)
```

---

### ADD\_SUBSET\_RULES Procedure

This procedure adds rules to a rule set of one of the following types of Oracle Streams clients:

- When the `streams_type` parameter is set to `capture`, this procedure adds capture process rules for capturing changes to a subset of rows in a specified table. See "Capture Process Rules for Changes in the Redo Log" for more information about these rules.
- When the `streams_type` parameter is set to `sync_capture`, this procedure adds rules for capturing changes to a subset of rows in a specified table. See "Synchronous Capture Rules for DML Changes to Tables" for more information about these rules.
- When the `streams_type` parameter is set to `apply` and the `streams_name` parameter specifies the name of an apply process, this procedure adds apply process rules for applying logical change records (LCRs) in a queue that contain changes to a subset of rows in a specified table. The rules can specify that the LCRs must be from a particular source database. See "Apply Process Rules for LCRs" for more information about these rules.
- When the `streams_type` parameter is set to `dequeue`, this procedure adds messaging client rules for dequeuing persistent LCRs from a queue that contain changes to a subset of rows in a specified table. The rules can specify that the LCRs must be from a particular source database. See "Messaging Client Rules for LCRs" for more information about these rules.

This procedure creates the specified capture process, synchronous capture, apply process, or messaging client if it does not exist.

This procedure is overloaded. One version of this procedure contains three `OUT` parameters, and the other does not.

Note:

- Currently, messaging clients cannot dequeue buffered messages.
- The invoking user must be granted the `DBA` role to create a synchronous capture.

Syntax

```
DBMS_STREAMS_ADM.ADD_SUBSET_RULES(
   table_name          IN   VARCHAR2,
   dml_condition       IN   VARCHAR2,
   streams_type        IN   VARCHAR2 DEFAULT 'apply',
   streams_name        IN   VARCHAR2 DEFAULT NULL,
   queue_name          IN   VARCHAR2 DEFAULT 'streams_queue',
   include_tagged_lcr  IN   BOOLEAN  DEFAULT FALSE,
   source_database     IN   VARCHAR2 DEFAULT NULL,
   insert_rule_name    OUT  VARCHAR2,
   update_rule_name    OUT  VARCHAR2,
   delete_rule_name    OUT  VARCHAR2);

DBMS_STREAMS_ADM.ADD_SUBSET_RULES(
   table_name          IN   VARCHAR2,
   dml_condition       IN   VARCHAR2,
   streams_type        IN   VARCHAR2 DEFAULT 'apply',
   streams_name        IN   VARCHAR2 DEFAULT NULL,
   queue_name          IN   VARCHAR2 DEFAULT 'streams_queue',
   include_tagged_lcr  IN   BOOLEAN  DEFAULT FALSE,
   source_database     IN   VARCHAR2 DEFAULT NULL);
```

Parameters

Table 145-11 ADD\_SUBSET\_RULES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `table_name` | The name of the table specified as `[``schema_name``.]` `object_name`. For example, `hr.employees`. If the schema is not specified, then the current user is the default.  The specified table must exist in the same database as the capture process, synchronous capture, apply process, or messaging client. Also, the specified table cannot have any LOB, `LONG`, `LONG` `RAW`, or `XMLType` columns currently or in the future. |
| `dml_condition` | The subset condition. Specify this condition similar to the way you specify conditions in a `WHERE` clause in SQL.  For example, to specify rows in the `hr.employees` table where the `salary` is greater than `4000` and the `job_id` is `SA_MAN`, enter the following as the condition:  `' salary > 4000 and job_id = ''SA_MAN'' '`  Note: The quotation marks in the preceding example are all single quotation marks. |
| `streams_type` | The type of Oracle Streams client:  - Specify `capture` for a capture process. - Specify `sync_capture` for a synchronous capture. - Specify `apply` for an apply process. - Specify `dequeue` for a messaging client. |
| `streams_name` | The name of the capture process, synchronous capture, apply process, or messaging client. Do not specify an owner.  If `NULL`, if `streams_type` is `capture`, `sync_capture`, or `dequeue`, and if one relevant capture process, synchronous capture, or messaging client for the queue exists, then the procedure uses the relevant Oracle Streams client. If no relevant Oracle Streams client exists for the queue, then the procedure creates an Oracle Streams client automatically with a system-generated name. If `NULL` and multiple Oracle Streams clients of the specified `streams_type` for the queue exist, then the procedure raises an error.  If `NULL`, if `streams_type` is `apply`, and if one relevant apply process exists, then the procedure uses the relevant apply process. The relevant apply process is identified in one of the following ways:  - If one existing apply process has the source database specified in `source_database` and uses the queue specified in `queue_name`, then the procedure uses this apply process. - If `source_database` is `NULL` and one existing apply process is using the queue specified in `queue_name`, then the procedure uses this apply process.  If `NULL` and no relevant apply process exists, then the procedure creates an apply process automatically with a system-generated name.  If `NULL` and multiple relevant apply processes exist, then the procedure raises an error.  Each apply process and messaging client must have a unique name. |
| `queue_name` | The name of the local queue, specified as `[``schema_name``.]` `queue_name`. The current database must contain the queue, and the queue must be `ANYDATA` type.  For example, to specify a queue named `streams_queue` in the `strmadmin` schema, enter `strmadmin.streams_queue` for this parameter. If the schema is not specified, then the current user is the default.  For capture process or synchronous capture rules, this is the queue into which a capture process or synchronous capture enqueues LCRs. For apply process rules, this is the queue from which an apply process dequeues messages. For messaging client rules, this is the queue from which a messaging client dequeues messages. |
| `include_tagged_lcr` | If `TRUE`, then the Oracle Streams client performs its action regardless of the tag:  - A redo entry is always considered for capture by a capture process, regardless of whether the redo entry has a non- `NULL` tag. - A change is always considered for capture by a synchronous capture, regardless of whether the session that makes the change has a non- `NULL` tag. - An LCR is always considered for apply by an apply process or dequeue by a messaging client, regardless of whether redo entry or LCR has a non- `NULL` tag.  If `FALSE`, then an Oracle Streams client performs its action only when the tag is `NULL`:  - A redo entry is considered for capture by a capture process only when the redo entry contains a `NULL` tag. - A change is considered for capture by a synchronous capture only when the session that makes the change has a `NULL` tag. - An LCR is considered for apply by an apply process or dequeue by a messaging client only if the LCR contains a `NULL` tag.  A setting of `FALSE` is often specified in update-anywhere configurations to avoid sending a change back to its source database.  See Also: [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/rep_tags.htm#STREP008) for more information about tags |
| `source_database` | The global name of the source database. If `NULL`, then the procedure does not add a condition regarding the source database to the generated rules.  For capture process rules, specify `NULL` or the global name of the local database if you are creating a capture process locally at the source database. If you are adding rules to a downstream capture process rule set at a downstream database, then specify the source database of the changes that will be captured.  For synchronous capture rules, specify the name of the local database.  For apply process rules, specify the source database of the changes that will be applied by the apply process. The source database is the database where the changes originated. If an apply process applies captured messages, then the apply process can apply messages from only one capture process at one source database.  For messaging client rules, specify `NULL` if you do not want the rules created by this procedure to have a condition for the source database. Specify a source database if you want the rules created by this procedure to have a condition for the source database. The source database is part of the information in an LCR, and user-constructed LCRs might or might not have this information.  If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify `DBS1` and the domain is `.NET`, then the procedure specifies `DBS1.NET` automatically. |
| `insert_rule_name` | Contains the system-generated `INSERT` rule name. This rule handles inserts and updates that must be converted into inserts. |
| `update_rule_name` | Contains the system-generated `UPDATE` rule name. This rule handles updates that remain updates. |
| `delete_rule_name` | Contains the system-generated `DELETE` rule name. This rule handles deletes and updates that must be converted into deletes |

Usage Notes

Running this procedure generates three rules for the specified capture process, synchronous capture, apply process, or messaging client: one for `INSERT` statements, one for `UPDATE` statements, and one for `DELETE` statements. For `INSERT` and `DELETE` statements, only DML changes that satisfy the condition specified for the `dml_condition` parameter are captured, applied, or dequeued. For `UPDATE` statements, the following variations are possible:

- If both the new and old values in a DML change satisfy the specified `dml_condition`, then the DML change is captured, applied, or dequeued without any changes.
- If neither the new or old values in a DML change satisfy the specified `dml_condition`, then the DML change is not captured, applied, or dequeued.
- If the old values for a DML change satisfy the specified `dml_condition`, but the new values do not, then the DML change is converted into a delete.
- If the new values for a DML change satisfy the specified `dml_condition`, but the old values do not, then the DML change is converted to an insert.

When an update is converted into an insert or a delete, it is called row migration.

A capture process, synchronous capture, apply process, or messaging client uses the rules for filtering. If the Oracle Streams client does not have a positive rule set, then this procedure creates a positive rule set automatically, and adds the rules for the table to the positive rule set. A subset rule can be added to positive rule set only, not to a negative rule set. Other rules in an existing rule set for the process are not affected. Additional rules can be added using either the `DBMS_STREAMS_ADM` package or the `DBMS_RULE_ADM` package.

Rules for `INSERT`, `UPDATE`, and `DELETE` statements are created automatically when you run this procedure, and these rules are given a system-generated rule name. Each rule has a system-generated rule name that consists of the table name with a sequence number appended to it. The sequence number is used to avoid naming conflicts. If the table name plus the sequence number is too long, then the table name is truncated. The `ADD_SUBSET_RULES` procedure is overloaded, and the system-generated rule names for `INSERT`, `UPDATE`, and `DELETE` statements are returned.

Attention:

Subset rules should only reside in positive rule sets. You should not add subset rules to negative rule sets. Doing so might have unpredictable results because row migration would not be performed on LCRs that are not discarded by the negative rule set.

See Also:

- "Operational Notes"
- "Security Model"

Examples

The following is an example of a rule condition created for filtering DML changes containing an update operation when the `dml_condition` is `region_id = 2`, the `table_name` is `hr.regions`, and the `source_database` is `dbs1.net`:

```
:dml.get_object_owner()='HR' AND :dml.get_object_name()='REGIONS' 
AND :dml.is_null_tag()='Y' AND :dml.get_source_database_name()='DBS1.NET' 
AND :dml.get_command_type()='UPDATE' 
AND (:dml.get_value('NEW','"REGION_ID"') IS NOT NULL) 
AND (:dml.get_value('OLD','"REGION_ID"') IS NOT NULL) 
AND (:dml.get_value('OLD','"REGION_ID"').AccessNumber()=2) 
AND (:dml.get_value('NEW','"REGION_ID"').AccessNumber()=2)
```

---

### ADD\_TABLE\_PROPAGATION\_RULES Procedure

This procedures adds table rules to the positive rule set for a propagation, or adds table rules to the negative rule set for a propagation, and creates the specified propagation if it does not exist.

This procedure is overloaded. One version of this procedure contains two `OUT` parameters, and the other does not.

Syntax

```
DBMS_STREAMS_ADM.ADD_TABLE_PROPAGATION_RULES(
   table_name              IN   VARCHAR2,
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

DBMS_STREAMS_ADM.ADD_TABLE_PROPAGATION_RULES(
   table_name              IN   VARCHAR2,
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

Table 145-12 ADD\_TABLE\_PROPAGATION\_RULES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `table_name` | The name of the table specified as `[``schema_name``.]` `table_name`. For example, `hr.employees`. If the schema is not specified, then the current user is the default. |
| `streams_name` | The name of the propagation. Do not specify an owner.  If the specified propagation does not exist, then the procedure creates it automatically.  If `NULL` and a propagation exists for the same source queue and destination queue (including database link), then the procedure uses this propagation.  If `NULL` and no propagation exists for the same source queue and destination queue (including database link), then the procedure creates a propagation automatically with a system-generated name. |
| `source_queue_name` | The name of the source queue, specified as `[``schema_name``.]` `queue_name`. The current database must contain the source queue, and the queue must be `ANYDATA` type.  For example, to specify a source queue named `streams_queue` in the `strmadmin` schema, enter `strmadmin.streams_queue` for this parameter.  If the schema is not specified, then the current user is the default. |
| `destination_queue_name` | The name of the destination queue, including a database link, specified as `[``schema_name``.]` `queue_name` `[``@dblink_name``]`, if the destination queue is in a remote database. The queue must be `ANYDATA` type.  For example, to specify a destination queue named `streams_queue` in the `strmadmin` schema and use a database link named `dbs2.net`, enter `strmadmin.streams_queue@dbs2.net` for this parameter.  If the schema is not specified, then the current user is the default.  If the database link is omitted, then the procedure uses the global name of the current database, and the source queue and destination queue must be in the same database.  Note: Connection qualifiers are not allowed. |
| `include_dml` | If `TRUE`, then the procedure creates a rule for DML changes. If `FALSE`, then the procedure does not create a DML rule. `NULL` is not permitted. |
| `include_ddl` | If `TRUE`, then the procedure creates a rule for DDL changes. If `FALSE`, then the procedure does not create a DDL rule. `NULL` is not permitted.  The generated rule evaluates to `TRUE` for any DDL change that operates on the table or on an object that is part of the table, such as an index or trigger on the table. The rule evaluates to `FALSE` for any DDL change that either does not refer to the table or refers to the table in a subordinate way. For example, the rule evaluates to `FALSE` for changes that create synonyms or views based on the table. The rule also evaluates to `FALSE` for a change to a PL/SQL subprogram that refers to the table. |
| `include_tagged_lcr` | If `TRUE`, then the procedure does not add a condition regarding Oracle Streams tags to the generated rules. Therefore, these rules can evaluate to `TRUE` regardless of whether a logical change record (LCR) has a non- `NULL` tag. If the rules are added to the positive rule set for the propagation, then an LCR is always considered for propagation, regardless of whether it has a non- `NULL` tag. If the rules are added to a positive rule set, then setting this parameter to `TRUE` is appropriate for a full (for example, standby) copy of a database. If the rules are added to the negative rule set for the propagation, then whether an LCR is discarded does not depend on the tag for the LCR.  If `FALSE`, then the procedure adds a condition to each generated rule that causes the rule to evaluate to `TRUE` only if an LCR has a `NULL` Oracle Streams tag. If the rules are added to the positive rule set for the propagation, then an LCR is considered for propagation only when the LCR contains a `NULL` tag. If the rules are added to a positive rule set, then setting this parameter to `FALSE` might be appropriate in update-anywhere configurations to avoid sending a change back to its source database. If the rules are added to the negative rule set for the propagation, then an LCR can be discarded only if it has a `NULL` tag.  Usually, specify `TRUE` for this parameter if the `inclusion_rule` parameter is set to `FALSE`.  See Also: [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/rep_tags.htm#STREP008) for more information about tags |
| `source_database` | The global name of the source database. The source database is where the change originated. If `NULL`, then the procedure does not add a condition regarding the source database to the generated rules.  If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify `DBS1` and the domain is `.NET`, then the procedure specifies `DBS1.NET` automatically.  Oracle recommends that you specify a source database for propagation rules. |
| `dml_rule_name` | If `include_dml` is `TRUE`, then this parameter contains the DML rule name.  If `include_dml` is `FALSE`, then this parameter contains a `NULL`. |
| `ddl_rule_name` | If `include_ddl` is `TRUE`, then this parameter contains the DDL rule name.  If `include_ddl` is `FALSE`, then this parameter contains a `NULL`. |
| `inclusion_rule` | If `inclusion_rule` is `TRUE`, then the procedure adds the rules to the positive rule set for the propagation.  If `inclusion_rule` is `FALSE`, then the procedure adds the rules to the negative rule set for the propagation.  In either case, the system creates the rule set if it does not exist. |
| `and_condition` | If non- `NULL`, appends the specified condition to the system-generated rule condition using an `AND` clause in the following way:  ``` (system_condition) AND (and_condition) ```  The variable in the specified condition must be `:lcr`. For example, to specify that the table rules generated by the procedure evaluate to `TRUE` only if the Oracle Streams tag is the hexadecimal equivalent of `'02'`, specify the following condition:  ``` :lcr.get_tag() = HEXTORAW(''02'') ```  The `:lcr` in the specified condition is converted to `:dml` or `:ddl`, depending on the rule that is being generated. If you are specifying an LCR member subprogram that is dependent on the LCR type (row or DDL), then make sure this procedure only generates the appropriate rule.  Specifically, if you specify an LCR member subprogram that is valid only for row LCRs, then specify `TRUE` for the `include_dml` parameter and `FALSE` for the `include_ddl` parameter. If you specify an LCR member subprogram that is valid only for DDL LCRs, then specify `FALSE` for the `include_dml` parameter and `TRUE` for the `include_ddl` parameter.  See Also: [Chapter 249, "Logical Change Record TYPEs"](t_lcr.md) |
| `queue_to_queue` | If `TRUE` or `NULL`, then a new propagation created by this procedure is a queue to queue propagation. A queue-to-queue propagation always has its own propagation job and uses a service for automatic failover when the destination queue is a buffered queue in an Oracle Real Application Clusters (Oracle RAC) database.  If `FALSE`, then a new propagation created by this procedure is a queue-to-dblink propagation. A queue-to-dblink propagation can share a propagation job with other propagations that use the same database link and does not support automatic failover in an Oracle RAC environment.  This procedure cannot change the queue to queue property of an exiting propagation. If the specified propagation exists, then the procedure behaves in the following way for each setting:  - If `TRUE` and the specified propagation is not a queue to queue propagation, then the procedure raises an error. - If `FALSE` and the specified propagation is a queue to queue propagation, then the procedure raises an error. - If `NULL`, then the procedure does not change the queue to queue property of the propagation.  See Also: [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_prop.htm#STRMS155) for more information about queue-to-queue propagations |

Usage Notes

This procedure configures propagation using the current user. Only one propagation is allowed between a particular source queue and destination queue.

This procedure creates DML and DDL rules automatically based on `include_dml` and `include_ddl` parameter values, respectively. Each rule has a system-generated rule name that consists of the table name with a sequence number appended to it. The sequence number is used to avoid naming conflicts. If the table name plus the sequence number is too long, then the table name is truncated. A propagation uses the rules for filtering.

See Also:

- "Operational Notes" and "Propagation Rules for LCRs" for more information about the rules created by this procedure
- "Security Model"

Examples

The following is an example of a table rule condition created for filtering DML statements:

```
(((:dml.get_object_owner() = 'HR' and :dml.get_object_name() = 'LOCATIONS')) 
and :dml.is_null_tag() = 'Y' and :dml.get_source_database_name() = 'DBS1.NET' )
```

---

### ADD\_TABLE\_RULES Procedure

This procedure adds rules to a rule set of one of the following types of Oracle Streams clients:

- When the `streams_type` parameter is set to `capture`, this procedure adds capture process rules for capturing changes to a specified table. See "Capture Process Rules for Changes in the Redo Log" for more information about these rules.
- When the `streams_type` parameter is set to `sync_capture`, this procedure adds rules for capturing changes to a specified table. See "Synchronous Capture Rules for DML Changes to Tables" for more information about these rules.
- When the `streams_type` parameter is set to `apply` and the `streams_name` parameter specifies the name of an apply process, this procedure adds apply process rules for applying logical change records (LCRs) in a queue that contain changes to a specified table. The rules can specify that the LCRs must be from a particular source database. See "Apply Process Rules for LCRs" for more information about these rules.
- When the `streams_type` parameter is set to `dequeue`, this procedure adds messaging client rules for dequeuing persistent LCRs from a queue that contain changes to a specified table. The rules can specify that the LCRs must be from a particular source database. See "Messaging Client Rules for LCRs" for more information about these rules.

This procedure creates the specified capture process, synchronous capture, apply process, or messaging client if it does not exist.

This procedure is overloaded. One version of this procedure contains two `OUT` parameters, and the other does not.

Note:

- Currently, messaging clients cannot dequeue buffered messages.
- The invoking user must be granted the `DBA` role to create a synchronous capture.

Syntax

```
DBMS_STREAMS_ADM.ADD_TABLE_RULES(
   table_name          IN   VARCHAR2,
   streams_type        IN   VARCHAR2,
   streams_name        IN   VARCHAR2 DEFAULT NULL,
   queue_name          IN   VARCHAR2 DEFAULT 'streams_queue',
   include_dml         IN   BOOLEAN  DEFAULT TRUE,
   include_ddl         IN   BOOLEAN  DEFAULT FALSE,
   include_tagged_lcr  IN   BOOLEAN  DEFAULT FALSE,
   source_database     IN   VARCHAR2 DEFAULT NULL,
   dml_rule_name       OUT  VARCHAR2,
   ddl_rule_name       OUT  VARCHAR2,
   inclusion_rule      IN   BOOLEAN   DEFAULT TRUE,
   and_condition       IN   VARCHAR2  DEFAULT NULL);

DBMS_STREAMS_ADM.ADD_TABLE_RULES(
   table_name          IN   VARCHAR2,
   streams_type        IN   VARCHAR2,
   streams_name        IN   VARCHAR2 DEFAULT NULL,
   queue_name          IN   VARCHAR2 DEFAULT 'streams_queue',
   include_dml         IN   BOOLEAN  DEFAULT TRUE,
   include_ddl         IN   BOOLEAN  DEFAULT FALSE,
   include_tagged_lcr  IN   BOOLEAN  DEFAULT FALSE,
   source_database     IN   VARCHAR2 DEFAULT NULL,
   inclusion_rule      IN   BOOLEAN   DEFAULT TRUE,
   and_condition       IN   VARCHAR2  DEFAULT NULL);
```

Parameters

Table 145-13 ADD\_TABLE\_RULES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `table_name` | The name of the table specified as `[``schema_name``.]` `object_name`. For example, `hr.employees`. If the schema is not specified, then the current user is the default.  You can specify a table that does not yet exist, because Oracle Streams does not validate the existence of the table. |
| `streams_type` | The type of Oracle Streams client:  - Specify `capture` for a capture process. - Specify `sync_capture` for a synchronous capture. - Specify `apply` for an apply process. - Specify `dequeue` for a messaging client. |
| `streams_name` | The name of the capture process, synchronous capture, apply process, or messaging client. Do not specify an owner.  If `NULL`, if `streams_type` is `capture`, `sync_capture`, or `dequeue`, and if one relevant capture process, synchronous capture, or messaging client for the queue exists, then the procedure uses the relevant Oracle Streams client. If no relevant Oracle Streams client exists for the queue, then the procedure creates an Oracle Streams client automatically with a system-generated name. If `NULL` and multiple Oracle Streams clients of the specified `streams_type` for the queue exist, then the procedure raises an error.  If `NULL`, if `streams_type` is `apply`, and if one relevant apply process exists, then the procedure uses the relevant apply process. The relevant apply process is identified in one of the following ways:  - If one existing apply process has the source database specified in `source_database` and uses the queue specified in `queue_name`, then the procedure uses this apply process. - If `source_database` is `NULL` and one existing apply process is using the queue specified in `queue_name`, then the procedure uses this apply process.  If `NULL` and no relevant apply process exists, then the procedure creates an apply process automatically with a system-generated name.  If `NULL` and multiple relevant apply processes exist, then the procedure raises an error.  Each apply process and messaging client must have a unique name. |
| `queue_name` | The name of the local queue, specified as `[``schema_name``.]` `queue_name`. The current database must contain the queue, and the queue must be `ANYDATA` type.  For example, to specify a queue named `streams_queue` in the `strmadmin` schema, enter `strmadmin.streams_queue` for this parameter. If the schema is not specified, then the current user is the default.  For capture process or synchronous capture rules, this is the queue into which a capture process or synchronous capture enqueues LCRs. For apply process rules, this is the queue from which an apply process dequeues messages. For messaging client rules, this is the queue from which a messaging client dequeues messages. |
| `include_dml` | If `TRUE`, then the procedure creates a DML rule for DML changes. If `FALSE`, then the procedure does not create a DML rule. `NULL` is not permitted. |
| `include_ddl` | If `TRUE`, then the procedure creates a DDL rule for DDL changes. If `FALSE`, then the procedure does not create a DDL rule. `NULL` is not permitted.  The generated rule evaluates to `TRUE` for any DDL change that operates on the table or on an object that is part of the table, such as an index or trigger on the table. The rule evaluates to `FALSE` for any DDL change that either does not refer to the table or refers to the table in a subordinate way. For example, the rule evaluates to `FALSE` for changes that create synonyms or views based on the table. The rule also evaluates to `FALSE` for a change to a PL/SQL subprogram that refers to the table. |
| `include_tagged_lcr` | If `TRUE`, then the procedure does not add a condition regarding Oracle Streams tags to the generated rules. Therefore, these rules can evaluate to `TRUE` regardless of whether a redo entry, session, or LCR has a non- `NULL` tag. If the rules are added to the positive rule set for the Oracle Streams client, then the Oracle Streams client performs its action regardless of the tag:  - A redo entry is always considered for capture by a capture process, regardless of whether the redo entry has a non- `NULL` tag. - A change is always considered for capture by a synchronous capture, regardless of whether the session that makes the change has a non- `NULL` tag. - An LCR is always considered for apply by an apply process or dequeue by a messaging client, regardless of whether redo entry or LCR has a non- `NULL` tag.  If the rules are added to a positive rule set, then setting this parameter to `TRUE` is appropriate for a full (for example, standby) copy of a database. If the rules are added to the negative rule set for the Oracle Streams client, then whether a database change is discarded does not depend on the tag.  If `FALSE`, then the procedure adds a condition to each generated rule that causes the rule to evaluate to `TRUE` only if a redo entry, session, or LCR has a `NULL` Oracle Streams tag. If the rules are added to the positive rule set for an Oracle Streams client, then the Oracle Streams client performs its action only when the tag is `NULL`:  - A redo entry is considered for capture by a capture process only when the redo entry contains a `NULL` tag. - A change is considered for capture by a synchronous capture only when the session that makes the change has a `NULL` tag. - An LCR is considered for apply by an apply process or dequeue by a messaging client only if the LCR contains a `NULL` tag.  If the rules are added to a positive rule set, then setting this parameter to `FALSE` might be appropriate in update-anywhere configurations to avoid sending a change back to its source database. If the rules are added to the negative rule set for the Oracle Streams client, then a database change can be discarded only if it has a `NULL` tag.  A setting of `FALSE` is often specified in update-anywhere configurations to avoid sending a change back to its source database.  Usually, specify `TRUE` for this parameter if the `inclusion_rule` parameter is set to `FALSE`.  See Also: [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/rep_tags.htm#STREP008) for more information about tags |
| `source_database` | The global name of the source database. If `NULL`, then the procedure does not add a condition regarding the source database to the generated rules.  For capture process rules, specify `NULL` or the global name of the local database if you are creating a capture process locally at the source database. If you are adding rules to a downstream capture process rule set at a downstream database, then specify the source database of the changes that will be captured.  For synchronous capture rules, specify the name of the local database.  For apply process rules, specify the source database of the changes that will be applied by the apply process. The source database is the database where the changes originated. If an apply process applies captured messages, then the apply process can apply messages from only one capture process at one source database.  For messaging client rules, specify `NULL` if you do not want the rules created by this procedure to have a condition for the source database. Specify a source database if you want the rules created by this procedure to have a condition for the source database. The source database is part of the information in an LCR, and user-constructed LCRs might or might not have this information.  If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify `DBS1` and the domain is `.NET`, then the procedure specifies `DBS1.NET` automatically. |
| `dml_rule_name` | If `include_dml` is `TRUE`, then this parameter contains the DML rule name.  If `include_dml` is `FALSE`, then this parameter contains a `NULL`. |
| `ddl_rule_name` | If `include_ddl` is `TRUE`, then this parameter contains the DDL rule name.  If `include_ddl` is `FALSE`, then this parameter contains a `NULL`. |
| `inclusion_rule` | If `inclusion_rule` is `TRUE`, then the procedure adds the rules to the positive rule set for the Oracle Streams client.  If `inclusion_rule` is `FALSE`, then the procedure adds the rules to the negative rule set for the Oracle Streams client. A synchronous capture cannot have a negative rule set. Specifying `FALSE` for a synchronous capture raises an error.  In either case, the system creates the rule set if it does not exist. |
| `and_condition` | If non- `NULL`, appends the specified condition to the system-generated rule condition using an `AND` clause in the following way:  ``` (system_condition) AND (and_condition) ```  The variable in the specified condition must be `:lcr`. For example, to specify that the table rules generated by the procedure evaluate to `TRUE` only if the Oracle Streams tag is the hexadecimal equivalent of `'02'`, specify the following condition:  ``` :lcr.get_tag() = HEXTORAW(''02'') ```  The `:lcr` in the specified condition is converted to `:dml` or `:ddl`, depending on the rule that is being generated. If you are specifying an LCR member subprogram that is dependent on the LCR type (row or DDL), then make sure this procedure only generates the appropriate rule.  Specifically, if you specify an LCR member subprogram that is valid only for row LCRs, then specify `TRUE` for the `include_dml` parameter and `FALSE` for the `include_ddl` parameter. If you specify an LCR member subprogram that is valid only for DDL LCRs, then specify `FALSE` for the `include_dml` parameter and `TRUE` for the `include_ddl` parameter.  See Also: [Chapter 249, "Logical Change Record TYPEs"](t_lcr.md) |

Usage Notes

This procedure creates DML and DDL rules automatically based on `include_dml` and `include_ddl` parameter values, respectively. Each rule has a system-generated rule name that consists of the table name with a sequence number appended to it. The sequence number is used to avoid naming conflicts. If the table name plus the sequence number is too long, then the table name is truncated. A capture process, synchronous capture, apply process, or messaging client uses the rules for filtering.

See Also:

- "Operational Notes"
- "Security Model"

Examples

The following is an example of a table rule condition created for DML changes:

```
(((:dml.get_object_owner() = 'HR' and :dml.get_object_name() = 'LOCATIONS')) 
and :dml.is_null_tag() = 'Y' and :dml.get_source_database_name() = 'DBS1.NET' )
```

---

### CLEANUP\_INSTANTIATION\_SETUP Procedure

This procedure removes an Oracle Streams replication configuration that was set up by the `PRE_INSTANTIATION_SETUP` and `POST_INSTANTIATION_SETUP` procedures in this package. This procedure either remove the configuration directly, or it can generate a script that removes the configuration.

Run this procedure at the capture database. The capture database is the database that captures changes made to the source database.

Attention:

When the `CLEANUP_INSTANTIATION_SETUP` procedure is run, the parameter values must match the parameter values specified when the corresponding `PRE_INSTANTIATION_SETUP` and `POST_INSTANTIATION_SETUP` procedures were run, except for the values of the following parameters: `perform_actions`, `script_name`, and `script_directory_object`.

See Also:

- "PRE\_INSTANTIATION\_SETUP Procedure"
- "POST\_INSTANTIATION\_SETUP Procedure"
- "Procedures That Configure an Oracle Streams Environment" for more information about this procedure

Syntax

```
DBMS_STREAMS_ADM.CLEANUP_INSTANTIATION_SETUP(
   maintain_mode           IN VARCHAR2,
   tablespace_names        IN DBMS_STREAMS_TABLESPACE_ADM.TABLESPACE_SET,
   source_database         IN VARCHAR2,
   destination_database    IN VARCHAR2,
   perform_actions         IN BOOLEAN   DEFAULT TRUE,
   script_name             IN VARCHAR2  DEFAULT NULL,
   script_directory_object IN VARCHAR2  DEFAULT NULL,
   capture_name            IN VARCHAR2  DEFAULT NULL,
   capture_queue_table     IN VARCHAR2  DEFAULT NULL,
   capture_queue_name      IN VARCHAR2  DEFAULT NULL,
   capture_queue_user      IN VARCHAR2  DEFAULT NULL,
   propagation_name        IN VARCHAR2  DEFAULT NULL,
   apply_name              IN VARCHAR2  DEFAULT NULL,
   apply_queue_table       IN VARCHAR2  DEFAULT NULL,
   apply_queue_name        IN VARCHAR2  DEFAULT NULL,
   apply_queue_user        IN VARCHAR2  DEFAULT NULL,
   bi_directional          IN BOOLEAN   DEFAULT FALSE,
   change_global_name      IN BOOLEAN   DEFAULT FALSE);
```

Parameters

Table 145-14 CLEANUP\_INSTANTIATION\_SETUP Procedure Parameters

| Parameter | Description |
| --- | --- |
| `maintain_mode` | Specify one of the following:  - `GLOBAL` to clean up the Oracle Streams configuration that maintained the entire database in both the source and destination databases - `TRANSPORTABLE` `TABLESPACES` to cleanup the Oracle Streams configuration that maintained a set of tablespaces at both the source and destination database |
| `tablespace_names` | If `maintain_mode` is set to `TRANSPORTABLE` `TABLESPACES`, then specify the local tablespace set to be cloned at the destination database and maintained by Oracle Streams.  The tablespaces in the tablespace set must exist at the source database, but these tablespaces must not exist at the destination database.  A directory object must exist for each directory that contains the datafiles for the tablespace set. The user who invokes this procedure must have `READ` privilege on these directory objects.  If `maintain_mode` is set to `GLOBAL`, then specify an empty tablespace set.  Regardless of the `maintain_mode` setting, an error is raised if the `tablespace_names` parameter is not set or is set to `NULL`.  See Also: [TABLESPACE\_SET Table Type](d_streams_tbl.md) |
| `source_database` | The global name of the source database.  If `NULL`, then the procedure uses the global name of the local database. |
| `destination_database` | The global name of the destination database. A database link from the local database to the destination database with the same name as the global name of the destination database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure raises an error. |
| `perform_actions` | If `TRUE`, then this procedure performs the necessary actions to clean up the Oracle Streams configuration directly.  If `FALSE`, then the procedure does not perform the necessary actions to clean up the Oracle Streams configuration directly.  Specify `FALSE` when this procedure is generating a script that you can edit and then run. The procedure raises an error if you specify `FALSE` and either of the following parameters is `NULL`:  - `script_name` - `script_directory_object` |
| `script_name` | If non- `NULL` and the `perform_actions` parameter is `FALSE`, then specify the name of the script generated by this procedure. The script contains all of the statements used to clean up the Oracle Streams configuration. If a file with the specified script name exists in the specified directory for the `script_directory_object` parameter, then the statements are appended to the existing file.  If non- `NULL` and the `perform_actions` parameter is `TRUE`, then this procedure generates the specified script and performs the actions to clean up the Oracle Streams configuration directly.  If `NULL` and the `perform_actions` parameter is `TRUE`, then this procedure directly performs the actions to clean up the Oracle Streams configuration without generating a script.  If `NULL` and the `perform_actions` parameter is `FALSE`, then the procedure raises an error. |
| `script_directory_object` | The directory object for the directory on the local computer system into which the generated script is placed.  If the `script_name` parameter is `NULL`, then this parameter is ignored, and this procedure does not generate a script.  If `NULL` and the `script_name` parameter is non- `NULL`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle Automatic Storage Management (ASM) disk group. |
| `capture_name` | The name of the capture processes configured to capture changes in the Oracle Streams configuration. Do not specify an owner.  If `NULL`, then the procedure automatically identifies the capture processes with system-generated names created by the `PRE_INSTANTIATION_SETUP` and `POST_INSTANTIATION_SETUP` procedures. |
| `capture_queue_table` | The name of the queue table for each queue used by a capture process, specified as `[``schema_name``.]` `queue_table_name`. For example, `strmadmin.streams_queue_table`. If the schema is not specified, then the current user is the default.  If `NULL`, then the procedure automatically identifies the capture queue tables with system-generated names created by the `PRE_INSTANTIATION_SETUP` and `POST_INSTANTIATION_SETUP` procedures. |
| `capture_queue_name` | The name of each queue used by a capture process, specified as `[``schema_name``.]` `queue_name`. For example, `strmadmin.streams_queue`.  If the schema is not specified, then the queue table owner is the default. The queue owner automatically has privileges to perform all queue operations on the queue.  If `NULL`, then the procedure automatically identifies the capture queues with system-generated names created by the `PRE_INSTANTIATION_SETUP` and `POST_INSTANTIATION_SETUP` procedures. |
| `capture_queue_user` | The name of the user who has `ENQUEUE` and `DEQUEUE` privileges for the queue at the source database. This user is a secure queue user of the queue. |
| `propagation_name` | The name of the propagations configured to propagate changes in the Oracle Streams configuration. Do not specify an owner.  If `NULL`, then the procedure automatically identifies the propagations with system-generated names created by the `PRE_INSTANTIATION_SETUP` and `POST_INSTANTIATION_SETUP` procedures. |
| `apply_name` | The name of the apply processes configured to apply changes in the Oracle Streams configuration. Do not specify an owner.  If `NULL`, then the procedure automatically identifies the apply processes with system-generated names created by the `PRE_INSTANTIATION_SETUP` and `POST_INSTANTIATION_SETUP` procedures. |
| `apply_queue_table` | The name of the queue table for each queue used by an apply process, specified as `[``schema_name``.]` `queue_table_name`. For example, `strmadmin.streams_queue_table`. If the schema is not specified, then the current user is the default.  If `NULL`, then the procedure automatically identifies the apply queue tables with system-generated names created by the `PRE_INSTANTIATION_SETUP` and `POST_INSTANTIATION_SETUP` procedures. |
| `apply_queue_name` | The name of each queue used by an apply process, specified as `[``schema_name``.]` `queue_name`. For example, `strmadmin.streams_queue`.  If the schema is not specified, then the queue table owner is the default. The queue owner automatically has privileges to perform all queue operations on the queue.  If `NULL`, then the procedure automatically identifies the apply queues with system-generated names created by the `PRE_INSTANTIATION_SETUP` and `POST_INSTANTIATION_SETUP` procedures. |
| `apply_queue_user` | The name of the user who has `ENQUEUE` and `DEQUEUE` privileges for the queue at the destination database. This user is a secure queue user of the queue. |
| `bi_directional` | Specify `TRUE` if the Oracle Streams replication configuration is bi-directional between the database specified in `source_database` and the database specified in `destination_database`.  Specify `FALSE` if the Oracle Streams replication configuration is one way replication from the current database to the database specified in `destination_database`. |
| `change_global_name` | If `TRUE`, then the procedure changes the global name of the database specified in `destination_database` to match the global name of the current database.  If `FALSE`, then the procedure does not change the global name of the database specified in `destination_database`. |

---

### DELETE\_COLUMN Procedure

This procedure either adds or removes a declarative rule-based transformation which deletes a column from a row logical change record (LCR) that satisfies the specified rule.

For the transformation to be performed when the specified rule evaluates to `TRUE`, the rule must be in the positive rule set of an Oracle Streams client. Oracle Streams clients include capture processes, synchronous captures, propagations, apply processes, and messaging clients.

Note:

- The `DELETE_COLUMN` procedure supports the same data types supported by Oracle Streams capture processes.
- The `DELETE_COLUMN` procedure is useful when you want to delete a relatively small number of columns in a row LCR. To delete most of the columns in a row LCR and keep a relatively small number of columns, consider using the `KEEP_COLUMNS` procedure in this package.
- Declarative transformations can transform row LCRs only. These row LCRs can be captured by a capture process, captured by a synchronous capture, or constructed and enqueued by an application. Therefore, a DML rule must be specified when you run this procedure. If a DDL is specified, then the procedure raises an error.

Syntax

```
DBMS_STREAMS_ADM.DELETE_COLUMN(
   rule_name     IN  VARCHAR2,
   table_name    IN  VARCHAR2,
   column_name   IN  VARCHAR2,
   value_type    IN  VARCHAR2   DEFAULT '*',
   step_number   IN  NUMBER     DEFAULT 0,
   operation     IN  VARCHAR2   DEFAULT 'ADD');
```

Parameters

Table 145-15 DELETE\_COLUMN Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_name` | The name of the rule, specified as `[``schema_name``.]` `rule_name`. If `NULL`, then the procedure raises an error.  For example, to specify a rule in the `hr` schema named `employees12`, enter `hr.employees12`. If the schema is not specified, then the current user is the default. |
| `table_name` | The name of the table from which the column is deleted in the row LCR, specified as `[``schema_name``.]` `object_name`. For example, `hr.employees`. If the schema is not specified, then the current user is the default. |
| `column_name` | The name of the column deleted from each row LCR that satisfies the rule. |
| `value_type` | Specify `'NEW'` to delete the column from the new values in the row LCR.  Specify `'OLD'` to delete the column from the old values in the row LCR.  Specify `'*'` to delete the column from both the old and new values in the row LCR. |
| `step_number` | The order of execution of the transformation.  See Also: [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_transform.htm#STRMS145) for more information about transformation ordering |
| `operation` | Specify `'ADD'` to add the transformation to the rule.  Specify `'REMOVE'` to remove the transformation from the rule.  See "Usage Notes" for more information about this parameter. |

Usage Notes

When `'REMOVE'` is specified for the `operation` parameter, all of the delete column declarative rule-based transformations for the specified rule are removed that match the specified `table_name`, `column_name`, and `step_number` parameters. Nulls specified for these parameters act as wildcards. The following table lists the behavior of the `DELETE_COLUMN` procedure when one or more of these parameters is `NULL`:

| table\_name | column\_name | step\_number | Result |
| --- | --- | --- | --- |
| `NULL` | `NULL` | `NULL` | Remove all delete column transformations for the specified rule. |
| `NULL` | `NULL` | non- `NULL` | Remove all delete column transformations with the specified `step_number` for the specified rule. |
| `NULL` | non- `NULL` | non- `NULL` | Remove all delete column transformations with the specified `column_name` and `step_number` for the specified rule. |
| non- `NULL` | `NULL` | `non-NULL` | Remove all delete column transformations with the specified `table_name` and `step_number` for the specified rule. |
| `NULL` | `non-NULL` | `NULL` | Remove all delete column transformations with the specified `column_name` for the specified rule. |
| non- `NULL` | non- `NULL` | `NULL` | Remove all delete column transformations with the specified `table_name` and `column_name` for the specified rule. |
| non- `NULL` | `NULL` | `NULL` | Remove all delete column transformations with the specified `table_name` for the specified rule. |
| non- `NULL` | non- `NULL` | non- `NULL` | Remove all delete column transformations with the specified `table_name`, `column_name`, and `step_number` for the specified rule. |

---

### GET\_MESSAGE\_TRACKING Function

Returns the tracking label for the current session.

See Also:

SET\_MESSAGE\_TRACKING Procedure

Syntax

```
DBMS_STREAMS_ADM.GET_MESSAGE_TRACKING
RETURN VARCHAR2;
```

---

### GET\_SCN\_MAPPING Procedure

This procedure gets information about the system change number (SCN) values to use for Oracle Streams capture and apply processes in an Oracle Streams replication environment. This information can be used for the following purposes:

- To recover transactions after point-in-time recovery is performed on a source database in a multiple source Oracle Streams environment
- To run flashback queries for the corresponding SCN at a source database and destination database in an Oracle Streams single source replication environment
	See Also:
	[Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/toc.htm) for information about [point-in-time recovery](https://docs.oracle.com/cd/E11882_01/server.112/e10705/man_gen_rep.htm#STREP121) and [flashback queries](https://docs.oracle.com/cd/E11882_01/server.112/e10705/man_gen_rep.htm#STREP133) in an Oracle Streams replication environment

Syntax

```
DBMS_STREAMS_ADM.GET_SCN_MAPPING(
   apply_name             IN  VARCHAR2,
   src_pit_scn            IN  NUMBER,
   dest_instantiation_scn OUT NUMBER,
   dest_start_scn         OUT NUMBER,
   dest_skip_txn_ids      OUT DBMS_UTILITY.NAME_ARRAY);
```

Parameters

Table 145-16 GET\_SCN\_MAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `apply_name` | Name of the apply process which applies logical change records (LCRs) from the source database. The procedure raises an error if the specified apply process does not exist. |
| `src_pit_scn` | The SCN at the source database.  For point-in-time recovery, specify the point-in-time recovery SCN at the source database.  If the specified SCN is greater than the source commit SCN of the last applied transaction, then `NULL` is returned for both `dest_start_scn` and `dest_instantiation_scn`. In this case, no values can be returned for these parameters because the corresponding transaction has not been applied at the destination database yet. |
| `dest_instantiation_scn` | The SCN at the destination database that corresponds to the specified `src_pit_scn` at the source database.  For point-in-time recovery, use this value for the instantiation SCNs at the source database during recovery. |
| `dest_start_scn` | For point in time recovery, the SCN to use for the `start_scn` parameter for the recovery capture process. |
| `dest_skip_txn_ids` | Transaction IDs of transactions that were skipped at the `dest_instantiation_scn` because the apply process was applying nondependent transactions out of order.  For point in time recovery, these transaction IDs should be ignored by the recovery apply process.  This parameter is relevant only if the `commit_serialization` for the apply process that applied these transactions was set to `DEPENDENT_TRANSACTIONS`, and the transactions were applied out of order. |

---

### GET\_TAG Function

This function gets the binary tag for all redo entries generated by the current session.

See Also:

- "SET\_TAG Procedure"
- [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/rep_tags.htm#STREP008) for more information about tags

Syntax

```
DBMS_STREAMS_ADM.GET_TAG
RETURN RAW;
```

Examples

The following example illustrates how to display the current logical change record (LCR) tag as output:

```
SET SERVEROUTPUT ON
DECLARE
   raw_tag RAW(2000);
BEGIN
   raw_tag := DBMS_STREAMS_ADM.GET_TAG();
   DBMS_OUTPUT.PUT_LINE('Tag Value = ' || RAWTOHEX(raw_tag));
END;
/
```

You can also display the value by querying the `DUAL` view:

```
SELECT DBMS_STREAMS_ADM.GET_TAG FROM DUAL;
```

---

### KEEP\_COLUMNS Procedure

This procedure either adds or removes a declarative rule-based transformation which keeps a list of columns in a row logical change record (LCR) that satisfies the specified rule. The transformation deletes columns that are not in the list from the row LCR.

For the transformation to be performed when the specified rule evaluates to `TRUE`, the rule must be in the positive rule set of an Oracle Streams client. Oracle Streams clients include capture processes, synchronous captures, propagations, apply processes, and messaging clients.

This procedure is overloaded. The `column_list` parameter is type `VARCHAR2` and the `column_table` parameter is type `DBMS_UTILITY.LNAME_ARRAY`. These parameters enable you to enter the list of columns in different ways and are mutually exclusive.

Note:

- The `KEEP_COLUMNS` procedure supports the same data types supported by Oracle Streams capture processes.
- The `KEEP_COLUMNS` procedure is useful when you want to keep a relatively small number of columns in a row LCR. To keep most of the columns in a row LCR and delete a relatively small number of columns, consider using the `DELETE_COLUMN` procedure in this package.
- Declarative transformations can transform row LCRs only. These row LCRs can be captured by a capture process, captured by a synchronous capture, or constructed and enqueued by an application. Therefore, a DML rule must be specified when you run this procedure. If a DDL is specified, then the procedure raises an error.

Syntax

```
DBMS_STREAMS_ADM.KEEP_COLUMNS(
   rule_name     IN  VARCHAR2,
   table_name    IN  VARCHAR2,
   column_list   IN  VARCHAR2,
   value_type    IN  VARCHAR2 DEFAULT '*',
   step_number   IN  NUMBER DEFAULT 0,
   operation     IN  VARCHAR2 DEFAULT 'ADD');

DBMS_STREAMS_ADM.KEEP_COLUMNS(
   rule_name     IN  VARCHAR2,
   table_name    IN  VARCHAR2,
   column_table  IN  DBMS_UTILITY.LNAME_ARRAY,
   value_type    IN  VARCHAR2 DEFAULT '*',
   step_number   IN  NUMBER DEFAULT 0,
   operation     IN  VARCHAR2 DEFAULT 'ADD');
```

Parameters

Table 145-17 KEEP\_COLUMNS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_name` | The name of the rule, specified as `[``schema_name``.]` `rule_name`. If `NULL`, then the procedure raises an error.  For example, to specify a rule in the `hr` schema named `employees12`, enter `hr.employees12`. If the schema is not specified, then the current user is the default. |
| `table_name` | The name of the table for which the columns are kept in the row LCR, specified as `[``schema_name``.]` `object_name`. For example, `hr.employees`. If the schema is not specified, then the current user is the default. |
| `column_list` | The names of the columns kept for each row LCR that satisfies the rule. Specify a comma-delimited list of type `VARCHAR2`. The transformation removes columns that are not in the list from the row LCR.  If this parameter is set to `NULL`, and the `column_table` parameter is also set to `NULL`, then the procedure raises an error. |
| `column_table` | The names of the columns kept for each row LCR that satisfies the rule. Specify a PL/SQL associative array of type `DBMS_UTILITY.LNAME_ARRAY`, where each element is the name of a column. The first schema should be in position 1. The last position must be `NULL`.  The transformation removes columns that are not in the table from the row LCR.  If this parameter is set to `NULL`, and the `column_list` parameter is also set to `NULL`, then the procedure raises an error. |
| `value_type` | Specify `'NEW'` to keep the columns in the new values in the row LCR.  Specify `'OLD'` to keep the columns in the old values in the row LCR.  Specify `'*'` to keep the columns in both the old and new values in the row LCR. |
| `step_number` | The order of execution of the transformation.  See Also: [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_transform.htm#STRMS145) for more information about transformation ordering |
| `operation` | Specify `'ADD'` to add the transformation to the rule.  Specify `'REMOVE'` to remove the transformation from the rule.  See "Usage Notes" for more information about this parameter. |

Usage Notes

When `'REMOVE'` is specified for the `operation` parameter, all of the keep columns declarative rule-based transformations for the specified rule are removed that match the specified `table_name`, `column_list`, `column_table`, and `step_number` parameters. Nulls specified for these parameters act as wildcards. The following table lists the behavior of the `KEEP_COLUMNS` procedure when one or more of these parameters is `NULL`:

| table\_name | column\_list/column\_table | step\_number | Result |
| --- | --- | --- | --- |
| `NULL` | `NULL` | `NULL` | Remove all keep columns transformations for the specified rule. |
| `NULL` | `NULL` | non- `NULL` | Remove all keep columns transformations with the specified `step_number` for the specified rule. |
| `NULL` | non- `NULL` | non- `NULL` | Remove all keep columns transformations with the specified `column_list` / `column_table` and `step_number` for the specified rule. |
| non- `NULL` | `NULL` | non- `NULL` | Remove all keep columns transformations with the specified `table_name` and `step_number` for the specified rule. |
| `NULL` | non- `NULL` | `NULL` | Remove all keep columns transformations with the specified `column_list` / `column_table` for the specified rule. |
| non- `NULL` | non- `NULL` | `NULL` | Remove all keep columns transformations with the specified `table_name` and `column_list` / `column_table` for the specified rule. |
| non- `NULL` | `NULL` | `NULL` | Remove all keep columns transformations with the specified `table_name` for the specified rule. |
| non- `NULL` | non- `NULL` | non- `NULL` | Remove all keep columns transformations with the specified `table_name`, `column_list` / `column_table`, and `step_number` for the specified rule. |

---

### MAINTAIN\_CHANGE\_TABLE Procedure

This procedure configures an Oracle Streams environment that uses change handlers to record in a change table the data manipulation language (DML) changes made to a source table. Optionally, this procedure can also configure one-way replication of the table from the source database to the destination database. This procedure can either configure the environment directly, or it can generate a script that configures the environment.

A change handler is a special type of statement DML handler that tracks table changes and was created by either this `MAINTAIN_CHANGE_TABLE` procedure or the `DBMS_APPLY_ADM.SET_CHANGE_HANDLER` procedure. Information about change handlers is stored in the `ALL_APPLY_CHANGE_HANDLERS` and `DBA_APPLY_CHANGE_HANDLERS` views.

The change table can reside in the same database as the source table or in a different database.

Run this procedure at the capture database. The capture database is the database that captures changes made to the source database.

Note:

The environment configured by this procedure does not record or replicate data definition language (DDL) changes made to the source table.

See Also:

"Procedures That Configure an Oracle Streams Environment" for more information about this procedure

Syntax

```
DBMS_STREAMS_ADM.MAINTAIN_CHANGE_TABLE(
   change_table_name        IN VARCHAR2,
   source_table_name        IN VARCHAR2,
   column_type_list         IN VARCHAR2,
   extra_column_list        IN VARCHAR2  DEFAULT 'command_type, value_type',
   capture_values           IN VARCHAR2,
   options_string           IN VARCHAR2  DEFAULT NULL,
   script_name              IN VARCHAR2  DEFAULT NULL,
   script_directory_object  IN VARCHAR2  DEFAULT NULL,
   perform_actions          IN BOOLEAN   DEFAULT TRUE,
   capture_name             IN VARCHAR2  DEFAULT NULL,
   propagation_name         IN VARCHAR2  DEFAULT NULL,
   apply_name               IN VARCHAR2  DEFAULT NULL,
   source_database          IN VARCHAR2  DEFAULT NULL,
   destination_database     IN VARCHAR2  DEFAULT NULL,
   keep_change_columns_only IN BOOLEAN   DEFAULT TRUE,
   execute_lcr              IN BOOLEAN   DEFAULT FALSE);
```

Parameters

Table 145-18 MAINTAIN\_CHANGE\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `change_table_name` | The table that records changes to the source table. This table is maintained by Oracle Streams after configuration.  Specify the table as `[``schema_name``.]` `table_name`. For example, `hr.jobs_change_table`. If the schema is not specified, then the current user is the default.  If `NULL`, then the procedure raises an error.  If the specified table exists at the database specified in the `destination_database` parameter, then the procedure raises an error. |
| `source_table_name` | The table at the source database for which changes are recorded.  Specify the table as `[``schema_name``.]` `table_name`. For example, `hr.jobs`. If the schema is not specified, then the current user is the default.  If `NULL`, then the procedure raises an error. |
| `column_type_list` | A list of the columns in the source table for which changes are recorded. Specify a comma-delimited list of each column and its data type.  For example, specify the following for the `hr.jobs` table:  ``` job_id VARCHAR2(10), job_title VARCHAR2(35), min_salary NUMBER(6), max_salary NUMBER(6) ```  The procedure automatically places columns with names that match the source database columns into an unconditional supplemental log group.  If `NULL`, then the procedure raises an error. |
| `extra_column_list` | A comma-delimited list of metadata attributes to include in the change table. The column name for a metadata attribute is in the format of attribute name followed by a `$` symbol. For example, the `source_database_name` attribute is stored in the `source_database_name$` column in the change table.  The following metadata attributes can be included:  - `value_type` - `source_database_name` - `command_type` - `object_owner` - `object_name` - `tag` - `transaction_id` - `scn` - `commit_scn` - `compatible` - `instance_number` - `message_number` - `row_text` - `row_id` - `serial#` - `session#` - `source_time` - `thread#` - `tx_name` - `username`  All of these metadata attributes, except for `value_type` and `message_number`, are row LCR attributes that can be stored in row LCRs. For information about LCR attributes, see [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_capture.htm#STRMS107).  The `value_type$` column in the change table contains either `OLD` or `NEW`, depending on whether the column value is the original column value or the new column value, respectively.  The `message_number$` column in the change table contains the identification number of each row LCR within a transaction. The message number increases incrementally for each row LCR within a transaction and shows the order of the row LCRs within a transaction.  The procedure automatically configures the source database to place information about extra attributes, such as `serial#`, into the redo log so that the information can be captured and recorded. |
| `capture_values` | Specify which values to capture when update operations are performed on the source table:  - `old` - To capture the original values for an updated column in the source table - `new` - To capture the new values for an updated column in the source table - `*` - To capture both the original and the new values for an updated column in the source table  If `NULL`, then the procedure raises an error.  Note: For insert operations, only new column values can be captured. For delete operations, only old column values can be captured. |
| `options_string` | String of options passed to the `CREATE` `TABLE` statement that creates the change table. The string is appended to the generated `CREATE` `TABLE` statement after the closing parenthesis that defines the columns of the table. The string must be syntactically correct. |
| `script_name` | If non- `NULL` and the `perform_actions` parameter is `FALSE`, then specify the name of the script generated by this procedure. The script contains all of the statements used to configure the environment. If a file with the specified script name exists in the specified directory for the `script_directory_object` parameter, then the procedure appends the statements to the existing file.  If non- `NULL` and the `perform_actions` parameter is `TRUE`, then the procedure generates the specified script and performs the actions to configure the replication environment directly.  If `NULL` and the `perform_actions` parameter is `TRUE`, then the procedure performs the actions to configure the replication environment directly and does not generate a script.  If `NULL` and the `perform_actions` parameter is `FALSE`, then the procedure raises an error. |
| `script_directory_object` | The directory object for the directory on the local computer system into which the generated script is placed.  If the `script_name` parameter is `NULL`, then the procedure ignores this parameter and does not generate a script.  If `NULL` and the `script_name` parameter is non- `NULL`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle Automatic Storage Management (ASM) disk group. |
| `perform_actions` | If `TRUE`, then the procedure performs the necessary actions to configure the environment directly.  If `FALSE`, then the procedure does not perform the necessary actions to configure the environment directly.  Specify `FALSE` when this procedure is generating a script that you can edit and then run. The procedure raises an error if you specify `FALSE` and either of the following parameters is `NULL`:  - `script_name` - `script_directory_object` |
| `capture_name` | The name of each capture process configured to capture changes. Do not specify an owner.  If the specified name matches the name of an existing capture process, then the procedure uses the existing capture process and adds the rules for capturing changes to the database to the positive capture process rule set.  If `NULL`, then the system generates a name for each capture process it creates.  Note: The capture process name cannot be altered after the capture process is created. |
| `propagation_name` | The name of the propagation configured to propagate changes from the source database to the destination database. Do not specify an owner.  If the specified name matches the name of an existing propagation, then the procedure uses the existing propagation and adds the rules for propagating changes to the positive propagation rule set.  If `NULL`, then the system generates a name for the propagation.  If non- `NULL` and the `source_database` and `destination_database` are set to the same value, then this procedure raises an error. When the capture process and apply process are in the same database, they can use the same queue, and a propagation is not needed.  Note: The propagation name cannot be altered after the propagation is created. |
| `apply_name` | The name of each apply process configured to apply changes. Do not specify an owner.  If the specified name matches the name of an existing apply process, then the procedure uses the existing apply process and adds the rules for applying changes to the positive apply process rule set.  The specified name must not match the name of an existing messaging client at the destination database.  If `NULL`, then the system generates a name for the apply process. When set to `NULL`, no apply process that applies changes from the source database can exist on the destination database. If an apply process that applies changes from the source database exists at the destination database, then specify a non- `NULL` value for this parameter.  Note: The apply process name cannot be altered after the apply process is created. |
| `source_database` | The global name of the source database.  If the specified global name is the same as the global name of the local database, then the procedure configures a local capture process for the source database.  If the specified global name is different from the global name of the local database, then the procedure configures a downstream capture process at the local database. In this case, a database link from the local database to the source database with the same name as the global name of the source database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure uses the global name of the local database. |
| `destination_database` | The global name of the destination database.  If the local database is not the destination database, then a database link from the local database to the destination database with the same name as the global name of the destination database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure uses the global name of the local database. |
| `keep_change_columns_only` | If `TRUE`, then this procedure adds a declarative rule-based transformation which keeps the list of columns specified in the `column_type_list` parameter. The columns that are not specified in the `column_type_list` parameter are removed from each row LCR captured by the capture process.  If `FALSE`, then this procedure does not create a declarative rule-based transformation, and all of the columns in the row LCRs are kept.  Specify `FALSE` when information about columns that are not included in the `column_type_list` parameter is needed at the destination database. For example, if the `execute_lcr` parameter is set to `TRUE` and the configuration will replicate all of the columns in a source table, but the `column_type_list` parameter includes a subset of these columns, then the `keep_change_columns_only` parameter should be set to `FALSE`.  Note: When this parameter is set to `TRUE`, a declarative rule-based transformation is always created, even if the `column_type_list` includes all of the columns in the source table. |
| `execute_lcr` | If `TRUE`, then this procedure creates a change handler that executes each row LCR at the destination database.  If `FALSE`, then the row LCRs are not executed at the destination database. |

Usage Notes

The following are usage notes for this procedure:

Types of Oracle Streams Environments Configured by the Procedure

This procedure can configure the following types of Oracle Streams environments:

- Local capture and apply on one database: Specify the same global name for the `source_database` and the `destination_database` parameter.
- Local capture and remote apply: Specify the global name of the local database for the `source_database` parameter and a remote database for the `destination_database` parameter.
- Downstream capture and local apply: Specify a remote database for the `source_database` parameter and the local database for the `destination_database` parameter.
- Downstream capture and remote apply: Specify a remote database for the `source_database` parameter and a remote database for the `destination_database` parameter.

Optional One-Way Replication With This Procedure

To configure one-way replication of the table, in addition to recording changes to the table, set the `execute_lcr` parameter to `TRUE`. The apply process executes each row LCR and applies the change in the row LCR to the replica table at the destination database. In this case, ensure that the source table is instantiated at the destination database before running the procedure. Specifically, the source table must be prepared for instantiation, the instantiation SCN must be set for the replica table at the destination database, and, usually, the source table replica table should be consistent.

See Also:

[Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/instant.htm#STREP012)

Statement DML Handlers, the Change Table, and Row LCR Execution

This procedure configures one or more statement DML handlers that perform the following actions:

- Record changes in the change table using the information in row LCRs.
- Execute row LCRs if the `execute_lcr` parameter is set to `TRUE`.

The procedure ensures that the row LCRs contain the required attributes to record the changes specified in the `capture_type_list`, `extra_column_list`, and `capture_values` parameters. The procedure adds the statement DML handlers to the apply process specified in the `apply_name` parameter.

See Also:

[Chapter 148, "DBMS\_STREAMS\_HANDLER\_ADM"](d_streams_hand.md)

---

### MAINTAIN\_GLOBAL Procedure

This procedure configures an Oracle Streams environment that replicates changes at the database level between two databases. This procedure can either configure the environment directly, or it can generate a script that configures the environment.

Run this procedure at the capture database. The capture database is the database that captures changes made to the source database.

Note:

- This procedure automatically excludes database objects that are not supported by Oracle Streams from the replication environment by adding rules to the negative rule set of each capture and apply process. Query the `DBA_STREAMS_UNSUPPORTED` data dictionary view to determine which database objects are not supported by Oracle Streams. If unsupported database objects are not excluded, then capture errors will result.
- If the `bi_directional` parameter is set to `TRUE`, then do not allow data manipulation language (DML) or data definition language (DDL) changes to the destination database while the `MAINTAIN_GLOBAL` procedure, or the script generated by the procedure, is running. This restriction does not apply to the source database.
- A capture process never captures changes in the `SYS`, `SYSTEM`, or `CTXSYS` schemas. This procedure does not configure replication for these schemas.

See Also:

"Procedures That Configure an Oracle Streams Environment" for more information about this procedure

Syntax

```
DBMS_STREAMS_ADM.MAINTAIN_GLOBAL(
   source_directory_object      IN VARCHAR2,
   destination_directory_object IN VARCHAR2,
   source_database              IN VARCHAR2,
   destination_database         IN VARCHAR2,
   perform_actions              IN BOOLEAN   DEFAULT TRUE,
   script_name                  IN VARCHAR2  DEFAULT NULL,
   script_directory_object      IN VARCHAR2  DEFAULT NULL,
   dump_file_name               IN VARCHAR2  DEFAULT NULL,
   capture_name                 IN VARCHAR2  DEFAULT NULL,
   capture_queue_table          IN VARCHAR2  DEFAULT NULL,
   capture_queue_name           IN VARCHAR2  DEFAULT NULL,
   capture_queue_user           IN VARCHAR2  DEFAULT NULL,
   propagation_name             IN VARCHAR2  DEFAULT NULL,
   apply_name                   IN VARCHAR2  DEFAULT NULL,
   apply_queue_table            IN VARCHAR2  DEFAULT NULL,
   apply_queue_name             IN VARCHAR2  DEFAULT NULL,
   apply_queue_user             IN VARCHAR2  DEFAULT NULL,
   log_file                     IN VARCHAR2  DEFAULT NULL,
   bi_directional               IN BOOLEAN   DEFAULT FALSE,
   include_ddl                  IN BOOLEAN   DEFAULT FALSE,
   instantiation                IN INTEGER   DEFAULT 
                                             DBMS_STREAMS_ADM.INSTANTIATION_FULL);
```

Parameters

See Also:

"Common Parameters for the Configuration Procedures" for descriptions of the procedure parameters

Table 145-19 MAINTAIN\_GLOBAL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `source_directory_object` | The directory object for the directory on the computer system running the source database into which the generated Data Pump export dump file is placed. This file remains in this directory after the procedure completes.  This parameter is ignored if `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_FULL_NETWORK` or `DBMS_STREAMS_ADM.INSTANTIATION_NONE`. In this case, specify `NULL` for the `source_directory_object` parameter.  If `NULL` and `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_FULL`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle Automatic Storage Management (ASM) disk group. |
| `destination_directory_object` | The directory object for the directory on the computer system running the destination database into which the generated Data Pump export dump file is transferred.  If the source database and destination database run on the same computer system, then the source and destination directories must be different.  This parameter is ignored if `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_FULL_NETWORK` or `DBMS_STREAMS_ADM.INSTANTIATION_NONE`. In these cases, specify `NULL` for the `destination_directory_object` parameter.  If `NULL` and `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_FULL`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle ASM disk group. |
| `source_database` | The global name of the source database.  If the specified global name is the same as the global name of the local database, then the procedure configures a local capture process for the source database.  If the specified global name is different from the global name of the local database, then the procedure configures a downstream capture process at the local database. In this case, a database link from the local database to the source database with the same name as the global name of the source database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure uses the global name of the local database. |
| `destination_database` | The global name of the destination database.  If the local database is not the destination database, then a database link from the local database to the destination database with the same name as the global name of the destination database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure raises an error. |
| `dump_file_name` | The name of the Data Pump export dump file. If a file with the specified file name exists in the specified directory for the `source_directory_object` or `destination_directory_object` parameter, then the procedure raises an error.  This parameter is ignored if `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_FULL_NETWORK` or `DBMS_STREAMS_ADM.INSTANTIATION_NONE`.  If `NULL` and `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_FULL`, then the export dump file name is generated by the system. In this case, the export dump file name is `expat` `nn``.dmp`, where `nn` is a sequence number. The sequence number is increased to produce an export dump file with a unique name in the source directory. |
| `log_file` | The name of the Data Pump export log file. This log file is placed in the same directory as the Data Pump export dump file.  This parameter is ignored if `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_FULL_NETWORK` or `DBMS_STREAMS_ADM.INSTANTIATION_NONE`.  If `NULL` and `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_FULL`, then the log file name is the same name as the export dump file name with an extension of `.clg`. |
| `instantiation` | Specify whether to perform instantiation and, if instantiation is performed, the type of instantiation:  `DBMS_STREAMS_ADM.INSTANTIATION_FULL` performs a full Data Pump export at the source database and a Data Pump import of the export dump file at the destination database. The instantiation SCN is set for the shared database objects during import. If the `instantiation` parameter is set to this value, then the user who runs this procedure must have `EXECUTE` privilege on the `DBMS_FILE_TRANSFER` package.  `DBMS_STREAMS_ADM.INSTANTIATION_FULL_NETWORK` performs a full network Data Pump import. A network import means that Data Pump performs the import without using an export dump file. The instantiation SCN is set for the shared database objects during import. If the `instantiation` parameter is set to this value, then a database link from the destination database to the source database with the same name as the global name of the source database must exist and must be accessible to the user who runs the procedure.  `DBMS_STREAMS_ADM.INSTANTIATION_NONE` does not perform an instantiation. This setting is valid only if the `perform_actions` parameter is set to `FALSE`, and the procedure generates a configuration script. In this case, the configuration script does not perform an instantiation and does not set the instantiation SCN for each shared database object. Instead, you must perform the instantiation and ensure that instantiation SCN values are set properly. If you use the RMAN `DUPLICATE` or `CONVERT` `DATABASE` command for database instantiation, then the destination database cannot be the capture database.  If this parameter is set to `DBMS_STREAMS_ADM.INSTANTIATION_FULL` or `DBMS_STREAMS_ADM.INSTANTIATION_FULL_NETWORK`, then the database objects being instantiated must exist at the source database.  If an instantiated database object does not exist at the destination database, then it is imported at the destination database, including its supplemental logging specifications from the source database and its supporting database objects, such as indexes and triggers. However, if the database object exists at the destination database before instantiation, then it is not imported at the destination database. Therefore, the supplemental logging specifications from the source database are not specified for the database object at the destination database, and the supporting database objects are not imported. |

---

### MAINTAIN\_SCHEMAS Procedure

This procedure configures an Oracle Streams environment that replicates changes to specified schemas between two databases. This procedure can either configure the environment directly, or it can generate a script that configures the environment.

Run this procedure at the capture database. The capture database is the database that captures changes made to the source database.

This procedure is overloaded. One `schema_names` parameter is type `VARCHAR2` and the other `schema_names` parameter is type `DBMS_UTILITY.UNCL_ARRAY`. These parameters enable you to enter the list of schemas in different ways and are mutually exclusive.

Note:

- This procedure automatically excludes database objects that are not supported by Oracle Streams in the schemas from the replication environment by adding rules to the negative rule set of each capture and apply process. Query the `DBA_STREAMS_UNSUPPORTED` data dictionary view to determine which database objects are not supported by Oracle Streams. If unsupported database objects are not excluded, then capture errors will result.
- If the `bi_directional` parameter is set to `TRUE`, then do not allow data manipulation language (DML) or data definition language (DDL) changes to the shared database objects at the destination database while the `MAINTAIN_SCHEMAS` procedure, or the script generated by the procedure, is running. This restriction does not apply to the source database.

See Also:

"Procedures That Configure an Oracle Streams Environment" for more information about this procedure

Syntax

```
DBMS_STREAMS_ADM.MAINTAIN_SCHEMAS(
   schema_names                 IN VARCHAR2,
   source_directory_object      IN VARCHAR2,
   destination_directory_object IN VARCHAR2,
   source_database              IN VARCHAR2,
   destination_database         IN VARCHAR2,
   perform_actions              IN BOOLEAN   DEFAULT TRUE,
   script_name                  IN VARCHAR2  DEFAULT NULL,
   script_directory_object      IN VARCHAR2  DEFAULT NULL,
   dump_file_name               IN VARCHAR2  DEFAULT NULL,
   capture_name                 IN VARCHAR2  DEFAULT NULL,
   capture_queue_table          IN VARCHAR2  DEFAULT NULL,
   capture_queue_name           IN VARCHAR2  DEFAULT NULL,
   capture_queue_user           IN VARCHAR2  DEFAULT NULL,
   propagation_name             IN VARCHAR2  DEFAULT NULL,
   apply_name                   IN VARCHAR2  DEFAULT NULL,
   apply_queue_table            IN VARCHAR2  DEFAULT NULL,
   apply_queue_name             IN VARCHAR2  DEFAULT NULL,
   apply_queue_user             IN VARCHAR2  DEFAULT NULL,
   log_file                     IN VARCHAR2  DEFAULT NULL,
   bi_directional               IN BOOLEAN   DEFAULT FALSE,
   include_ddl                  IN BOOLEAN   DEFAULT FALSE,
   instantiation                IN INTEGER   DEFAULT 
                                           DBMS_STREAMS_ADM.INSTANTIATION_SCHEMA);

DBMS_STREAMS_ADM.MAINTAIN_SCHEMAS(
   schema_names                 IN DBMS_UTILITY.UNCL_ARRAY,
   source_directory_object      IN VARCHAR2,
   destination_directory_object IN VARCHAR2,
   source_database              IN VARCHAR2,
   destination_database         IN VARCHAR2,
   perform_actions              IN BOOLEAN   DEFAULT TRUE,
   script_name                  IN VARCHAR2  DEFAULT NULL,
   script_directory_object      IN VARCHAR2  DEFAULT NULL,
   dump_file_name               IN VARCHAR2  DEFAULT NULL,
   capture_name                 IN VARCHAR2  DEFAULT NULL,
   capture_queue_table          IN VARCHAR2  DEFAULT NULL,
   capture_queue_name           IN VARCHAR2  DEFAULT NULL,
   capture_queue_user           IN VARCHAR2  DEFAULT NULL,
   propagation_name             IN VARCHAR2  DEFAULT NULL,
   apply_name                   IN VARCHAR2  DEFAULT NULL,
   apply_queue_table            IN VARCHAR2  DEFAULT NULL,
   apply_queue_name             IN VARCHAR2  DEFAULT NULL,
   apply_queue_user             IN VARCHAR2  DEFAULT NULL,
   log_file                     IN VARCHAR2  DEFAULT NULL,
   bi_directional               IN BOOLEAN   DEFAULT FALSE,
   include_ddl                  IN BOOLEAN   DEFAULT FALSE,
   instantiation                IN INTEGER   DEFAULT 
                                           DBMS_STREAMS_ADM.INSTANTIATION_SCHEMA);
```

Parameters

See Also:

"Common Parameters for the Configuration Procedures" for descriptions of the procedure parameters that are not in Table 145-20

Table 145-20 MAINTAIN\_SCHEMAS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_names` | The schemas to be configured for replication and maintained by Oracle Streams after configuration. The schemas can be specified in the following ways:  - Comma-delimited list of type `VARCHAR2` - A PL/SQL associative array of type `DBMS_UTILITY.UNCL_ARRAY`, where each element is the name of a schema. The first schema should be in position 1. The last position must be `NULL`.  This procedure raises an error in any of the following cases:  - When a specified schema does not exist at the source database - When the `schema_names` parameter is set to `NULL` |
| `source_directory_object` | The directory object for the directory on the computer system running the source database into which the generated Data Pump export dump file is placed. This file remains in this directory after the procedure completes.  This parameter is ignored if `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_SCHEMA_NETWORK` or `DBMS_STREAMS_ADM.INSTANTIATION_NONE`. In this case, specify `NULL` for the `source_directory_object` parameter.  If `NULL` and `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_SCHEMA`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle Automatic Storage Management (ASM) disk group. |
| `destination_directory_object` | The directory object for the directory on the computer system running the destination database into which the generated Data Pump export dump file is transferred.  If the source database and destination database run on the same computer system, then the source and destination directories must be different.  This parameter is ignored if `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_SCHEMA_NETWORK` or `DBMS_STREAMS_ADM.INSTANTIATION_NONE`. In this case, specify `NULL` for the `destination_directory_object` parameter.  If `NULL` and `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_SCHEMA`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle ASM disk group. |
| `source_database` | The global name of the source database.  If the specified global name is the same as the global name of the local database, then the procedure configures a local capture process for the source database.  If the specified global name is different from the global name of the local database, then the procedure configures a downstream capture process at the local database. In this case, a database link from the local database to the source database with the same name as the global name of the source database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure uses the global name of the local database. |
| `destination_database` | The global name of the destination database.  If the local database is not the destination database, then a database link from the local database to the destination database with the same name as the global name of the destination database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure raises an error. |
| `dump_file_name` | The name of the Data Pump export dump file. If a file with the specified file name exists in the specified directory for the `source_directory_object` or `destination_directory_object` parameter, then the procedure raises an error.  This parameter is ignored if `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_SCHEMA_NETWORK` or `DBMS_STREAMS_ADM.INSTANTIATION_NONE`.  If `NULL` and `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_SCHEMA`, then the export dump file name is generated by the system. In this case, the export dump file name is `expat` `nn``.dmp`, where `nn` is a sequence number. The sequence number is increased to produce an export dump file with a unique name in the source directory. |
| `capture_queue_user` | The name of the user who requires `ENQUEUE` and `DEQUEUE` privileges for the queue at the source database. This user also is configured as a secure queue user of the queue. The queue user cannot grant these privileges to other users because they are not granted with the `GRANT` option.  If `NULL`, then the procedure does not grant any privileges. You can also grant queue privileges to the appropriate users using the `DBMS_AQADM` package. |
| `log_file` | The name of the Data Pump export log file. This log file is placed in the same directory as the Data Pump export dump file.  This parameter is ignored if `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_SCHEMA_NETWORK` or `DBMS_STREAMS_ADM.INSTANTIATION_NONE`.  If `NULL` and `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_SCHEMA`, then the log file name is the same name as the export dump file name with an extension of `.clg`. |
| `instantiation` | Specify whether to perform instantiation and, if instantiation is performed, the type of instantiation:  `DBMS_STREAMS_ADM.INSTANTIATION_SCHEMA` performs a full Data Pump export at the source database and a Data Pump import of the export dump file at the destination database. The instantiation SCN is set for the shared database objects during import. If the `instantiation` parameter is set to this value, then the user who runs this procedure must have `EXECUTE` privilege on the `DBMS_FILE_TRANSFER` package.  `DBMS_STREAMS_ADM.INSTANTIATION_SCHEMA_NETWORK` performs a full network Data Pump import. A network import means that Data Pump performs the import without using an export dump file. The instantiation SCN is set for the shared database objects during import. If the `instantiation` parameter is set to this value, then a database link from the destination database to the source database with the same name as the global name of the source database must exist and must be accessible to the user who runs the procedure.  `DBMS_STREAMS_ADM.INSTANTIATION_NONE` does not perform an instantiation. This setting is valid only if the `perform_actions` parameter is set to `FALSE`, and the procedure generates a configuration script. In this case, the configuration script does not perform an instantiation and does not set the instantiation SCN for each shared database object. Instead, you must perform the instantiation and ensure that instantiation SCN values are set properly.  If this parameter is set to `DBMS_STREAMS_ADM.INSTANTIATION_SCHEMA` or `DBMS_STREAMS_ADM.INSTANTIATION_SCHEMA_NETWORK`, then the database objects being instantiated must exist at the source database, and the tablespaces that contain the schemas must exist at the destination database.  If an instantiated database object does not exist at the destination database, then it is imported at the destination database, including its supplemental logging specifications from the source database and its supporting database objects, such as indexes and triggers. However, if the database object exists at the destination database before instantiation, then it is not imported at the destination database. Therefore, the supplemental logging specifications from the source database are not specified for the database object at the destination database, and the supporting database objects are not imported. |

---

### MAINTAIN\_SIMPLE\_TABLESPACE Procedure

This procedure clones a simple tablespace from a source database at a destination database and uses Oracle Streams to maintain this tablespace at both databases. This procedure can either perform these actions directly, or it can generate a script that performs these actions. Run this procedure at the source database.

Note:

This procedure is deprecated. It is replaced by the `MAINTAIN_SIMPLE_TTS` procedure.

See Also:

- "Deprecated Subprograms"
- MAINTAIN\_SIMPLE\_TTS Procedure

Syntax

```
DBMS_STREAMS_ADM.MAINTAIN_SIMPLE_TABLESPACE(
   tablespace_name              IN VARCHAR2,
   source_directory_object      IN VARCHAR2,
   destination_directory_object IN VARCHAR2,
   destination_database         IN VARCHAR2,
   setup_streams                IN BOOLEAN   DEFAULT TRUE,
   script_name                  IN VARCHAR2  DEFAULT NULL,
   script_directory_object      IN VARCHAR2  DEFAULT NULL,
   bi_directional               IN BOOLEAN   DEFAULT FALSE);
```

Parameters

Table 145-21 MAINTAIN\_SIMPLE\_TABLESPACE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `tablespace_name` | The local simple tablespace to be cloned at the destination database and maintained by Oracle Streams.  The tablespace must exist at the source database, but it must not exist at the destination database.  A directory object must exist for the directory that contains the datafile for the tablespace. The user who invokes this procedure must have `READ` privilege on this directory object. The directory object cannot point to an Oracle Automatic Storage Management (ASM) disk group.  If `NULL`, then the procedure raises an error. |
| `source_directory_object` | The directory object for the directory on the computer system running the source database into which the generated Data Pump export dump file and the datafile for the cloned tablespace are placed. These files remain in this directory after the procedure completes.  If `NULL`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle ASM disk group. |
| `destination_directory_object` | The directory object for the directory on the computer system running the destination database into which the generated Data Pump export dump file and the datafile for the cloned tablespace are transferred.  If the source database and destination database run on the same computer system, then the source and destination directories must be different.  If `NULL`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle ASM disk group. |
| `destination_database` | The global name of the destination database. A database link from the source database to the destination database with the same name as the global name of the destination database must exist.  If `NULL`, then the procedure raises an error. |
| `setup_streams` | If `TRUE`, then the procedure performs the necessary actions to maintain the tablespace directly.  If `FALSE`, then the procedure does not perform the necessary actions to maintain the tablespace directly.  Specify `FALSE` when this procedure is generating a script that you can edit and then run. The procedure raises an error if you specify `FALSE` and either of the following parameters is `NULL`:  - `script_name` - `script_directory_object` |
| `script_name` | If non- `NULL` and the `setup_streams` parameter is `FALSE`, then specify the name of the script generated by this procedure. The script contains all of the statements used to maintain the specified tablespace. If a file with the specified script name exists in the specified directory for the `script_directory_object` parameter, then the procedure appends the statements to the existing file.  If non- `NULL` and the `setup_streams` parameter is `TRUE`, then this procedure generates the specified script and performs the actions to maintain the specified tablespace directly.  If `NULL` and the `setup_streams` parameter is `TRUE`, then this procedure does not generate a script and performs the actions to maintain the specified tablespace directly.  If `NULL` and the `setup_streams` parameter is `FALSE`, then the procedure raises an error. |
| `script_directory_object` | The directory object for the directory on the local computer system into which the generated script is placed.  If the `script_name` parameter is `NULL`, then the procedure ignores this parameter and does not generate a script.  If `NULL` and the `script_name` parameter is non- `NULL`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle ASM disk group. |
| `bi_directional` | Specify `TRUE` to configure bi-directional replication between the current database and the database specified in `destination_database`. Both databases are configured as source and destination databases, a capture and apply process is configured at both databases, and propagations are configured between the databases to propagate messages.  Specify `FALSE` to configure one way replication from the current database to the database specified in `destination_database`. A capture process is configured at the current database, a propagation is configured to propagate messages from the current database to the destination database, and an apply process is configured at the destination database. |

Usage Notes

The specified tablespace must be a simple tablespace. A simple tablespace is a single, self-contained tablespace that uses only one datafile. A self-contained tablespace has no references from the tablespace pointing outside of the tablespace. For example, if an index in the tablespace is for a table in a different tablespace, then the tablespace is not self-contained. This procedure cannot be used for a non simple tablespace or a set of tablespaces.

DDL Changes Not Maintained

This procedure does not configure the Oracle Streams environment to maintain DDL changes to the tablespace nor to the database objects in the tablespace. For example, the Oracle Streams environment is not configured to replicate `ALTER` `TABLESPACE` statements on the tablespace, nor is it configured to replicate `ALTER` `TABLE` statements on tables in the tablespace. You can configure the Oracle Streams environment to maintain DDL changes manually or modify generated scripts to achieve this.

Additional Documentation for this Procedure

The following documentation applies to the `MAINTAIN_SIMPLE_TABLESPACE` procedure:

- Automatic Platform Conversion
- [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/config_simple.htm#STREP020)

Requirements for Running this Procedure

Meet the following requirements when run the `MAINTAIN_SIMPLE_TABLESPACE` procedure:

- Run the procedure at the source database.
- Both databases must be open during configuration. If the procedure is generating a script only, then the database specified in the `destination_database` parameter does not need to be open when you run the procedure, but both databases must be open when you run the generated script.
- Grant the user who runs this procedure the `DBA` role. This user must have the necessary privileges to complete the following actions:
	- Create `ANYDATA` queues, capture processes, propagations, and apply processes.
		- Specify supplemental logging
		- Run subprograms in the `DBMS_STREAMS_ADM` and `DBMS_AQADM` packages.
		- Access the database specified in the `destination_database` parameter through a database link. This database link should have the same name as the global name of the destination database.
		- Run subprograms in the `DBMS_STREAMS_TABLESPACES_ADM` package
		- The necessary privileges to run the `CLONE_SIMPLE_TABLESPACE` procedure in the `DBMS_STREAMS_TABLESPACES_ADM` package at the source database. See [CLONE\_SIMPLE\_TABLESPACE Procedure](d_streams_tbl.md) for the list of required privileges.
		- The necessary privileges to run the `ATTACH_SIMPLE_TABLESPACE` procedure in the `DBMS_STREAMS_TABLESPACES_ADM` package at the destination database. See [ATTACH\_SIMPLE\_TABLESPACE Procedure](d_streams_tbl.md) for the list of required privileges.
	To ensure that the user who runs this procedure has the necessary privileges, you should configure an Oracle Streams administrator at each database, and each database link should be should be created in the Oracle Streams administrator's schema.
	Typically, the `DBA` role can be revoked from the user, if necessary, after the configuration is complete.
- If the `bi_directional` parameter is set to `TRUE`, then the corresponding user at the destination database must be able to use a database link to access the source database. This database link should have the same name as the global name of the source database.
- Each specified directory object must be created using the SQL statement `CREATE` `DIRECTORY`, and the user who invokes this procedure must have `READ` and `WRITE` privilege on each one.
- The databases configured by this procedure must be Oracle Database 10g Release 2 or later databases when this procedure is run under the following conditions:
	- The procedure is run at an Oracle Database 10g Release 2 or later database.
		- The `setup_streams` parameter is set to `TRUE` to configure the Oracle Streams replication environment directly.
- The databases configured by this procedure must be Oracle Database 10g Release 1 or later databases when this procedure is run under the following conditions:
	- The procedure is run at an Oracle Database 10g Release 2 or later database.
		- The `setup_streams` parameter is set to `FALSE` in this procedure, and the replication environment is configured with a generated script.
	If the script configures an Oracle Database 10g Release 1 database, then the script must be modified so that it does not configure features that are available only in Oracle Database 10g Release 2 or later, such as queue-to-queue propagation.
- If the procedure is run at an Oracle Database 10g Release 1 database, then the databases configured by the procedure must be Oracle Database 10g Release 1 or later databases.

See Also:

[Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/prep_rep.htm#STREP200) for information about configuring an Oracle Streams administrator

Default Values for Parameters Excluded From the MAINTAIN\_SIMPLE\_TABLESPACE Procedure

This procedure uses the default values for the parameters in the `MAINTAIN_TABLESPACES` procedure that do not exist in the `MAINTAIN_SIMPLE_TABLESPACE` procedure. For example, this procedure creates a capture process at the source database named `capture`, because that is the default value for the `capture_name` parameter in the `MAINTAIN_TABLESPACES` procedure.

See Also:

MAINTAIN\_TABLESPACES Procedure

Configuration Progress and Recoverability

When this procedure is run with the `setup_streams` parameter set to `TRUE`, metadata about its configuration actions is recorded in the following data dictionary views: `DBA_RECOVERABLE_SCRIPT`, `DBA_RECOVERABLE_SCRIPT_PARAMS`, `DBA_RECOVERABLE_SCRIPT_BLOCKS`, and `DBA_RECOVERABLE_SCRIPT_ERRORS`. If the procedure stops because it encounters an error, then you can use the `RECOVER_OPERATION` procedure to complete the configuration after you correct the conditions that caused the error.

Note:

When this procedure is run with the `setup_streams` parameter set to `FALSE`, these views are not populated. Also, the views are not populated when a script generated by this procedure is run.

See Also:

"RECOVER\_OPERATION Procedure"

---

### MAINTAIN\_SIMPLE\_TTS Procedure

This procedure clones a simple tablespace from a source database at a destination database and uses Oracle Streams to maintain this tablespace at both databases. This procedure can either perform these actions directly, or it can generate a script that performs these actions.

Run this procedure at the capture database. The capture database is the database that captures changes made to the source database.

Note:

- This procedure automatically excludes database objects that are not supported by Oracle Streams in the tablespace from the replication environment by adding rules to the negative rule set of each capture and apply process. Query the `DBA_STREAMS_UNSUPPORTED` data dictionary view to determine which database objects are not supported by Oracle Streams. If unsupported database objects are not excluded, then capture errors will result.
- This procedure replaces the deprecated `MAINTAIN_SIMPLE_TABLESPACE` procedure.

See Also:

"Procedures That Configure an Oracle Streams Environment" for more information about this procedure

Syntax

```
DBMS_STREAMS_ADM.MAINTAIN_SIMPLE_TTS(
   tablespace_name              IN VARCHAR2,
   source_directory_object      IN VARCHAR2,
   destination_directory_object IN VARCHAR2,
   source_database              IN VARCHAR2,
   destination_database         IN VARCHAR2,
   perform_actions              IN BOOLEAN   DEFAULT TRUE,
   script_name                  IN VARCHAR2  DEFAULT NULL,
   script_directory_object      IN VARCHAR2  DEFAULT NULL,
   bi_directional               IN BOOLEAN   DEFAULT FALSE);
```

Parameters

See Also:

"Common Parameters for the Configuration Procedures" for descriptions of the procedure parameters that are not in Table 145-22

Table 145-22 MAINTAIN\_SIMPLE\_TTS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `tablespace_name` | The local simple tablespace to be cloned at the destination database and maintained by Oracle Streams.  The tablespace must exist at the source database, but it must not exist at the destination database.  A directory object must exist for the directory that contains the datafile for the tablespace. The user who invokes this procedure must have `READ` privilege on this directory object. The directory object cannot point to an Oracle Automatic Storage Management (ASM) disk group.  If `NULL`, then the procedure raises an error. |
| `source_directory_object` | The directory object for the directory on the computer system running the source database into which the generated Data Pump export dump file and the datafile for the cloned tablespace are placed. These files remain in this directory after the procedure completes.  If `NULL`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle ASM disk group. |
| `destination_directory_object` | The directory object for the directory on the computer system running the destination database into which the generated Data Pump export dump file and the datafile for the cloned tablespace are transferred.  If the source database and destination database run on the same computer system, then the source and destination directories must be different.  If `NULL`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle ASM disk group. |
| `source_database` | The global name of the source database.  If the specified global name is the same as the global name of the local database, then the procedure configures a local capture process for the source database.  If the specified global name is different from the global name of the local database, then the procedure configures a downstream capture process at the local database. In this case, a database link from the local database to the source database with the same name as the global name of the source database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure uses the global name of the local database. |
| `destination_database` | The global name of the destination database.  If the local database is not the destination database, then a database link from the local database to the destination database with the same name as the global name of the destination database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure raises an error. |

Usage Notes

The specified tablespace must be a simple tablespace. A simple tablespace is a single, self-contained tablespace that uses only one datafile. A self-contained tablespace has no references from the tablespace pointing outside of the tablespace. For example, if an index in the tablespace is for a table in a different tablespace, then the tablespace is not self-contained. This procedure cannot be used for a non simple tablespace or a set of tablespaces.

DDL Changes Not Maintained

This procedure does not configure the Oracle Streams environment to maintain DDL changes to the tablespace nor to the database objects in the tablespace. For example, the Oracle Streams environment is not configured to replicate `ALTER` `TABLESPACE` statements on the tablespace, nor is it configured to replicate `ALTER` `TABLE` statements on tables in the tablespace. You can configure the Oracle Streams environment to maintain DDL changes manually or modify generated scripts to achieve this.

Additional Privileges Required by the MAINTAIN\_SIMPLE\_TTS Procedure

In addition to the required privileges described in "Requirements for Running These Procedures", the user who runs the `MAINTAIN_SIMPLE_TTS` procedure must have the necessary privileges to complete the following actions:

- Run subprograms in the `DBMS_STREAMS_TABLESPACES_ADM` package
- The necessary privileges to run the `CLONE_SIMPLE_TABLESPACE` procedure in the `DBMS_STREAMS_TABLESPACES_ADM` package at the source database. See [CLONE\_SIMPLE\_TABLESPACE Procedure](d_streams_tbl.md) for the list of required privileges.
- The necessary privileges to run the `ATTACH_SIMPLE_TABLESPACE` procedure in the `DBMS_STREAMS_TABLESPACES_ADM` package at the destination database. See [ATTACH\_SIMPLE\_TABLESPACE Procedure](d_streams_tbl.md) for the list of required privileges.

Default Values for Parameters Excluded From the MAINTAIN\_SIMPLE\_TTS Procedure

This procedure uses the default values for the parameters in the `MAINTAIN_TTS` procedure that do not exist in the `MAINTAIN_SIMPLE_TTS` procedure. For example, this procedure automatically generates the capture process name, because `NULL` is the default value for the `capture_name` parameter in the `MAINTAIN_TTS` procedure, and the procedure generates the capture process name when `NULL` is specified for `capture_name`.

See Also:

MAINTAIN\_TTS Procedure

---

### MAINTAIN\_TABLES Procedure

This procedure configures an Oracle Streams environment that replicates changes to specified tables between two databases. This procedure can either configure the environment directly, or it can generate a script that configures the environment.

Run this procedure at the capture database. The capture database is the database that captures changes made to the source database.

This procedure is overloaded. One `table_names` parameter is type `VARCHAR2` and the other `table_names` parameter is type `DBMS_UTILITY.UNCL_ARRAY`. These parameters enable you to enter the list of tables in different ways and are mutually exclusive.

Note:

If the `bi_directional` parameter is set to `TRUE`, then do not allow data manipulation language (DML) or data definition language (DDL) changes to the shared database objects at the destination database while the `MAINTAIN_TABLES` procedure, or the script generated by the procedure, is running. This restriction does not apply to the source database.

See Also:

"Procedures That Configure an Oracle Streams Environment" for more information about this procedure

Syntax

```
DBMS_STREAMS_ADM.MAINTAIN_TABLES(
   table_names                  IN VARCHAR2,
   source_directory_object      IN VARCHAR2,
   destination_directory_object IN VARCHAR2,
   source_database              IN VARCHAR2,
   destination_database         IN VARCHAR2,
   perform_actions              IN BOOLEAN   DEFAULT TRUE,
   script_name                  IN VARCHAR2  DEFAULT NULL,
   script_directory_object      IN VARCHAR2  DEFAULT NULL,
   dump_file_name               IN VARCHAR2  DEFAULT NULL,
   capture_name                 IN VARCHAR2  DEFAULT NULL,
   capture_queue_table          IN VARCHAR2  DEFAULT NULL,
   capture_queue_name           IN VARCHAR2  DEFAULT NULL,
   capture_queue_user           IN VARCHAR2  DEFAULT NULL,
   propagation_name             IN VARCHAR2  DEFAULT NULL,
   apply_name                   IN VARCHAR2  DEFAULT NULL,
   apply_queue_table            IN VARCHAR2  DEFAULT NULL,
   apply_queue_name             IN VARCHAR2  DEFAULT NULL,
   apply_queue_user             IN VARCHAR2  DEFAULT NULL,
   log_file                     IN VARCHAR2  DEFAULT NULL,
   bi_directional               IN BOOLEAN   DEFAULT FALSE,
   include_ddl                  IN BOOLEAN   DEFAULT FALSE,
   instantiation                IN INTEGER   DEFAULT 
                                           DBMS_STREAMS_ADM.INSTANTIATION_TABLE);

DBMS_STREAMS_ADM.MAINTAIN_TABLES(
   table_names                  IN DBMS_UTILITY.UNCL_ARRAY,
   source_directory_object      IN VARCHAR2,
   destination_directory_object IN VARCHAR2,
   source_database              IN VARCHAR2,
   destination_database         IN VARCHAR2,
   perform_actions              IN BOOLEAN   DEFAULT TRUE,
   script_name                  IN VARCHAR2  DEFAULT NULL,
   script_directory_object      IN VARCHAR2  DEFAULT NULL,
   dump_file_name               IN VARCHAR2  DEFAULT NULL,
   capture_name                 IN VARCHAR2  DEFAULT NULL,
   capture_queue_table          IN VARCHAR2  DEFAULT NULL,
   capture_queue_name           IN VARCHAR2  DEFAULT NULL,
   capture_queue_user           IN VARCHAR2  DEFAULT NULL,
   propagation_name             IN VARCHAR2  DEFAULT NULL,
   apply_name                   IN VARCHAR2  DEFAULT NULL,
   apply_queue_table            IN VARCHAR2  DEFAULT NULL,
   apply_queue_name             IN VARCHAR2  DEFAULT NULL,
   apply_queue_user             IN VARCHAR2  DEFAULT NULL,
   log_file                     IN VARCHAR2  DEFAULT NULL,
   bi_directional               IN BOOLEAN   DEFAULT FALSE,
   include_ddl                  IN BOOLEAN   DEFAULT FALSE,
   instantiation                IN INTEGER   DEFAULT 
                                           DBMS_STREAMS_ADM.INSTANTIATION_TABLE);
```

Parameters

See Also:

"Common Parameters for the Configuration Procedures" for descriptions of the procedure parameters that are not in Table 145-23

Table 145-23 MAINTAIN\_TABLES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `table_names` | The tables to be configured for replication and maintained by Oracle Streams after configuration. The tables can be specified in the following ways:  - Comma-delimited list of type `VARCHAR2` - A PL/SQL associative array of type `DBMS_UTILITY.UNCL_ARRAY`, where each element is the name of a table. The first table should be in position 1. The last position must be `NULL`.  Each table should be specified as `[``schema_name``.]` `table_name`. For example, `hr.employees`. If the schema is not specified, then the current user is the default.  This procedure raises an error in any of the following cases:  - When a specified table does not exist at the source database - When the `table_names` parameter is set to `NULL` |
| `source_directory_object` | The directory object for the directory on the computer system running the source database into which the generated Data Pump export dump file is placed. This file remain in this directory after the procedure completes.  This parameter is ignored if `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_TABLE_NETWORK` or `DBMS_STREAMS_ADM.INSTANTIATION_NONE`. In this case, specify `NULL` for the `source_directory_object` parameter.  If `NULL` and `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_TABLE`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle Automatic Storage Management (ASM) disk group. |
| `destination_directory_object` | The directory object for the directory on the computer system running the destination database into which the generated Data Pump export dump file is transferred.  If the source database and destination database run on the same computer system, then the source and destination directories must be different.  This parameter is ignored if `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_TABLE_NETWORK` or `DBMS_STREAMS_ADM.INSTANTIATION_NONE`. In this case, specify `NULL` for the `destination_directory_object` parameter.  If `NULL` and `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_TABLE`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle ASM disk group. |
| `source_database` | The global name of the source database.  If the specified global name is the same as the global name of the local database, then the procedure configures a local capture process for the source database.  If the specified global name is different from the global name of the local database, then the procedure configures a downstream capture process at the local database. In this case, a database link from the local database to the source database with the same name as the global name of the source database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure uses the global name of the local database. |
| `destination_database` | The global name of the destination database.  If the local database is not the destination database, then a database link from the local database to the destination database with the same name as the global name of the destination database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure raises an error. |
| `dump_file_name` | The name of the Data Pump export dump file. If a file with the specified file name exists in the specified directory for the `source_directory_object` or `destination_directory_object` parameter, then the procedure raises an error.  This parameter is ignored if `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_TABLE_NETWORK` or `DBMS_STREAMS_ADM.INSTANTIATION_NONE`.  If `NULL` and `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_TABLE`, then the export dump file name is generated by the system. In this case, the export dump file name is `expat` `nn``.dmp`, where `nn` is a sequence number. The sequence number is increased to produce an export dump file with a unique name in the source directory. |
| `capture_queue_user` | The name of the user who requires `ENQUEUE` and `DEQUEUE` privileges for the queue at the source database. This user also is configured as a secure queue user of the queue. The queue user cannot grant these privileges to other users because they are not granted with the `GRANT` option.  If `NULL`, then the procedure does not grant any privileges. You can also grant queue privileges to the appropriate users using the `DBMS_AQADM` package. |
| `log_file` | The name of the Data Pump export log file. This log file is placed in the same directory as the Data Pump export dump file.  This parameter is ignored if `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_TABLE_NETWORK` or `DBMS_STREAMS_ADM.INSTANTIATION_NONE`.  If `NULL` and `instantiation` is set to `DBMS_STREAMS_ADM.INSTANTIATION_TABLE`, then the log file name is the same name as the export dump file name with an extension of `.clg`. |
| `instantiation` | Specify whether to perform instantiation and, if instantiation is performed, the type of instantiation:  `DBMS_STREAMS_ADM.INSTANTIATION_TABLE` performs a full Data Pump export at the source database and a Data Pump import of the export dump file at the destination database. If the `instantiation` parameter is set to this value, then the user who runs this procedure must have `EXECUTE` privilege on the `DBMS_FILE_TRANSFER` package.  `DBMS_STREAMS_ADM.INSTANTIATION_TABLE_NETWORK` performs a full network Data Pump import. A network import means that Data Pump performs the import without using an export dump file. If the `instantiation` parameter is set to this value, then a database link from the destination database to the source database with the same name as the global name of the source database must exist and must be accessible to the user who runs the procedure.  `DBMS_STREAMS_ADM.INSTANTIATION_NONE` does not perform an instantiation. This setting is valid only if the `perform_actions` parameter is set to `FALSE`, and the procedure generates a configuration script. In this case, the configuration script does not perform an instantiation and does not set the instantiation SCN for each shared database object. Instead, you must perform the instantiation and ensure that instantiation SCN values are set properly.  If this parameter is set to `DBMS_STREAMS_ADM.INSTANTIATION_TABLE` or `DBMS_STREAMS_ADM.INSTANTIATION_TABLE_NETWORK`, then the tables being instantiated must exist at the source database, and the tablespaces that contain the tables must exist at the destination database.  If an instantiated database object does not exist at the destination database, then it is imported at the destination database, including its supplemental logging specifications from the source database and its supporting database objects, such as indexes and triggers. However, if the database object exists at the destination database before instantiation, then it is not imported at the destination database. Therefore, the supplemental logging specifications from the source database are not specified for the database object at the destination database, and the supporting database objects are not imported.  Also, if an instantiated table does not exist at the destination database, then this procedure sets the instantiation SCN for the table. However, if an instantiated table exist at the destination database before instantiation, then this procedure does not set the instantiation SCN for the table. In this case, you must set the instantiation SCN for the table manually after the procedure completes. |

---

### MAINTAIN\_TABLESPACES Procedure

This procedure clones a set of tablespaces from a source database at a destination database and uses Oracle Streams to maintain these tablespaces at both databases. This procedure can either perform these actions directly, or it can generate a script that performs these actions. Run this procedure at the source database.

Note:

This procedure is deprecated. It is replaced by the `MAINTAIN_TTS` procedure.

See Also:

- "Deprecated Subprograms"
- MAINTAIN\_TTS Procedure

Syntax

```
DBMS_STREAMS_ADM.MAINTAIN_TABLESPACES(
   tablespace_names             IN DBMS_STREAMS_TABLESPACE_ADM.TABLESPACE_SET,
   source_directory_object      IN VARCHAR2,
   destination_directory_object IN VARCHAR2,
   destination_database         IN VARCHAR2,
   setup_streams                IN BOOLEAN   DEFAULT TRUE,
   script_name                  IN VARCHAR2  DEFAULT NULL,
   script_directory_object      IN VARCHAR2  DEFAULT NULL,
   dump_file_name               IN VARCHAR2  DEFAULT NULL,
   source_queue_table           IN VARCHAR2  DEFAULT 'streams_queue_table',
   source_queue_name            IN VARCHAR2  DEFAULT 'streams_queue',
   source_queue_user            IN VARCHAR2  DEFAULT NULL,
   destination_queue_table      IN VARCHAR2  DEFAULT 'streams_queue_table',
   destination_queue_name       IN VARCHAR2  DEFAULT 'streams_queue',
   destination_queue_user       IN VARCHAR2  DEFAULT NULL,
   capture_name                 IN VARCHAR2  DEFAULT 'capture',
   propagation_name             IN VARCHAR2  DEFAULT NULL,
   apply_name                   IN VARCHAR2  DEFAULT NULL,
   log_file                     IN VARCHAR2  DEFAULT NULL,
   bi_directional               IN BOOLEAN   DEFAULT FALSE,
   include_ddl                  IN BOOLEAN   DEFAULT FALSE);
```

Parameters

Table 145-24 MAINTAIN\_TABLESPACES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `tablespace_names` | The local tablespace set to be cloned at the destination database and maintained by Oracle Streams.  The tablespaces in the tablespace set must exist at the source database, but these tablespaces must not exist at the destination database.  A directory object must exist for each directory that contains the datafiles for the tablespace set. The user who invokes this procedure must have `READ` privilege on these directory objects. The directory object cannot point to an Oracle Automatic Storage Management (ASM) disk group.  If `NULL`, then the procedure raises an error.  See Also: [TABLESPACE\_SET Table Type](d_streams_tbl.md) |
| `source_directory_object` | The directory object for the directory on the computer system running the source database into which the generated Data Pump export dump file and the datafiles that comprise the cloned tablespace set are placed. These files remain in this directory after the procedure completes.  If `NULL`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle ASM disk group. |
| `destination_directory_object` | The directory object for the directory on the computer system running the destination database into which the generated Data Pump export dump file and the datafiles that comprise the cloned tablespace set are transferred.  If the source database and destination database run on the same computer system, then the source and destination directories must be different.  If `NULL`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle ASM disk group. |
| `destination_database` | The global name of the destination database. A database link from the source database to the destination database with the same name as the global name of the destination database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure raises an error. |
| `setup_streams` | If `TRUE`, then the procedure performs the necessary actions to maintain the tablespaces directly.  If `FALSE`, then the procedure does not perform the necessary actions to maintain the tablespaces directly.  Specify `FALSE` when this procedure is generating a script that you can edit and then run. The procedure raises an error if you specify `FALSE` and either of the following parameters is `NULL`:  - `script_name` - `script_directory_object` |
| `script_name` | If non- `NULL` and the `setup_streams` parameter is `FALSE`, then specify the name of the script generated by this procedure. The script contains all of the statements used to maintain the specified tablespace set. If a file with the specified script name exists in the specified directory for the `script_directory_object` parameter, then the procedure appends the statements to the existing file.  If non- `NULL` and the `setup_streams` parameter is `TRUE`, then this procedure generates the specified script and performs the actions to maintain the specified tablespace directly.  If `NULL` and the `setup_streams` parameter is `TRUE`, then this procedure does not generate a script and performs the actions to maintain the specified tablespace set directly.  If `NULL` and the `setup_streams` parameter is `FALSE`, then the procedure raises an error. |
| `script_directory_object` | The directory object for the directory on the local computer system into which the generated script is placed.  If the `script_name` parameter is `NULL`, then the procedure ignores this parameter and does not generate a script.  If `NULL` and the `script_name` parameter is non- `NULL`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle ASM disk group. |
| `dump_file_name` | The name of the Data Pump export dump file that contains the specified tablespace set. If a file with the specified file name exists in the specified directory for the `source_directory_object` or `destination_directory_object` parameter, then the procedure raises an error.  If `NULL`, then the export dump file name is generated by the system. In this case, the export dump file name is `expat` `nn``.dmp`, where `nn` is a sequence number. The sequence number is increased to produce an export dump file with a unique name in the source directory. |
| `source_queue_table` | The name of the queue table for the queue at the source database, specified as `[``schema_name``.]` `queue_table_name`. For example, `strmadmin.streams_queue_table`. If the schema is not specified, then the current user is the default. |
| `source_queue_name` | The name of the queue at the source database that will function as the `ANYDATA` queue, specified as `[``schema_name``.]` `queue_name`. For example, `strmadmin.streams_queue`.  If the schema is not specified, then the queue table owner is the default. The queue owner automatically has privileges to perform all queue operations on the queue. |
| `source_queue_user` | The name of the user who requires `ENQUEUE` and `DEQUEUE` privileges for the queue at the source database. This user also is configured as a secure queue user of the queue. The queue user cannot grant these privileges to other users because they are not granted with the `GRANT` option.  If `NULL`, then the procedure does not grant any privileges. You can also grant queue privileges to the appropriate users using the `DBMS_AQADM` package. |
| `destination_queue_table` | The name of the queue table for the queue at the destination database, specified as `[``schema_name``.]` `queue_table_name`. For example, `strmadmin.streams_queue_table`. If the schema is not specified, then the current user is the default. |
| `destination_queue_name` | The name of the queue at the destination database that will function as the `ANYDATA` queue, specified as `[``schema_name``.]` `queue_name`. For example, `strmadmin.streams_queue`.  If the schema is not specified, then the queue table owner is the default. The queue owner automatically has privileges to perform all queue operations on the queue. |
| `destination_queue_user` | The name of the user who requires `ENQUEUE` and `DEQUEUE` privileges for the queue at the destination database. This user also is configured as a secure queue user of the queue. The queue user cannot grant these privileges to other users because they are not granted with the `GRANT` option.  If `NULL`, then the procedure does not grant any privileges. You can also grant queue privileges to the appropriate users using the `DBMS_AQADM` package. |
| `capture_name` | The name of each capture process configured to capture changes to the database objects in the tablespace set. Do not specify an owner.  If the specified name matches the name of an existing capture process, then the procedure uses the existing capture process and adds the rules for capturing changes to the database objects in the tablespace set to the positive capture process rule set.  Note: The capture process name cannot be altered after the capture process is created. |
| `propagation_name` | The name of each propagation configured to propagate changes to the database objects in the tablespace set. Do not specify an owner.  If the specified name matches the name of an existing propagation, then the procedure uses the existing propagation and adds the rules for propagating changes to the database objects in the tablespace set to the positive propagation rule set.  If `NULL`, then the system generates a name for each propagation it creates.  Note: The propagation name cannot be altered after the propagation is created. |
| `apply_name` | The name of each apply process configured to apply changes to the database objects in the tablespace set. Do not specify an owner.  If the specified name matches the name of an existing apply process, then the procedure uses the existing apply process and adds the rules for applying changes to the database objects in the tablespace set to the positive apply process rule set.  The specified name must not match the name of an existing messaging client at the destination database.  If `NULL`, then the system generates a name for each apply process it creates.  Note: The apply process name cannot be altered after the apply process is created. |
| `log_file` | The name of the Data Pump export log file. This log file is placed in the same directory as the Data Pump export dump file.  If `NULL`, then the log file name is the same name as the export dump file name with an extension of `.clg`. |
| `bi_directional` | Specify `TRUE` to configure bi-directional replication between the current database and the database specified in `destination_database`. Both databases are configured as source and destination databases, a capture and apply process is configured at both databases, and propagations are configured between the databases to propagate messages.  Specify `FALSE` to configure one way replication from the current database to the database specified in `destination_database`. A capture process is configured at the current database, a propagation is configured to propagate messages from the current database to the destination database, and an apply process is configured at the destination database. |
| `include_ddl` | Specify `TRUE` to configure an Oracle Streams replication environment that maintains both DML and DDL changes.  Specify `FALSE` to configure an Oracle Streams replication environment that maintains DML changes only. When this parameter is set to `FALSE`, DDL changes, such as `ALTER` `TABLE`, will not be replicated. |

Usage Notes

The specified set of tablespaces must be self-contained. In this context "self-contained" means that there are no references from inside the set of tablespaces pointing outside of the set of tablespaces. For example, if a partitioned table is partially contained in the set of tablespaces, then the set of tablespaces is not self-contained.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tspaces.htm#ADMIN011) for more information about self-contained tablespace sets

Additional Documentation for this Procedure

The following documentation applies to the `MAINTAIN_TABLESPACES` procedure:

- Automatic Platform Conversion
- [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/config_simple.htm#STREP020)

Requirements for Running this Procedure

Meet the following requirements when run the `MAINTAIN_TABLESPACES` procedure:

- Run the procedure at the source database.
- Both databases must be open during configuration. If the procedure is generating a script only, then the database specified in the `destination_database` parameter does not need to be open when you run the procedure, but both databases must be open when you run the generated script.
- The user who runs this procedure should be granted the `DBA` role. This user must have the necessary privileges to complete the following actions:
	- Create `ANYDATA` queues, capture processes, propagations, and apply processes.
		- Specify supplemental logging
		- Run subprograms in the `DBMS_STREAMS_ADM` and `DBMS_AQADM` packages.
		- Access the database specified in the `destination_database` parameter through a database link. This database link should have the same name as the global name of the destination database.
		- Run subprograms in the `DBMS_STREAMS_TABLESPACES_ADM` package
		- The necessary privileges to run the `CLONE_TABLESPACES` procedure in the `DBMS_STREAMS_TABLESPACES_ADM` package at the source database. See [CLONE\_TABLESPACES Procedure](d_streams_tbl.md) for the list of required privileges.
		- The necessary privileges to run the `ATTACH_TABLESPACES` procedure in the `DBMS_STREAMS_TABLESPACES_ADM` package at the destination database. See [ATTACH\_TABLESPACES Procedure](d_streams_tbl.md) for the list of required privileges.
	To ensure that the user who runs this procedure has the necessary privileges, you should configure an Oracle Streams administrator at each database, and each database link should be should be created in the Oracle Streams administrator's schema.
- If the `bi_directional` parameter is set to `TRUE`, then the corresponding user at the destination database must be able to use a database link to access the source database. This database link should have the same name as the global name of the source database.
- Each specified directory object must be created using the SQL statement `CREATE` `DIRECTORY`, and the user who invokes this procedure must have `READ` and `WRITE` privilege on each one.
- The databases configured by this procedure must be Oracle Database 10g Release 2 or later databases when this procedure is run under the following conditions:
	- The procedure is run at an Oracle Database 10g Release 2 or later database.
		- The `setup_streams` parameter is set to `TRUE` to configure the Oracle Streams replication environment directly.
- The databases configured by this procedure must be Oracle Database 10g Release 1 or later databases when this procedure is run under the following conditions:
	- The procedure is run at an Oracle Database 10g Release 2 or later database.
		- The `setup_streams` parameter is set to `FALSE` in this procedure, and the replication environment is configured with a generated script.
	If the script configures an Oracle Database 10g Release 1 database, then the script must be modified so that it does not configure features that are available only in Oracle Database 10g Release 2 or later, such as queue-to-queue propagation.
- If the procedure is run at an Oracle Database 10g Release 1 database, then the databases configured by the procedure must be Oracle Database 10g Release 1 or later databases.

See Also:

[Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/prep_rep.htm#STREP200) for information about configuring an Oracle Streams administrator

Configuration Progress and Recoverability

When this procedure is run with the `setup_streams` parameter set to `TRUE`, metadata about its configuration actions is recorded in the following data dictionary views: `DBA_RECOVERABLE_SCRIPT`, `DBA_RECOVERABLE_SCRIPT_PARAMS`, `DBA_RECOVERABLE_SCRIPT_BLOCKS`, and `DBA_RECOVERABLE_SCRIPT_ERRORS`. If the procedure stops because it encounters an error, then you can use the `RECOVER_OPERATION` procedure to complete the configuration after you correct the conditions that caused the error.

Note:

When this procedure is run with the `setup_streams` parameter set to `FALSE`, these views are not populated. Also, the views are not populated when a script generated by this procedure is run.

See Also:

"RECOVER\_OPERATION Procedure"

---

### MAINTAIN\_TTS Procedure

This procedure clones a set of tablespaces from a source database at a destination database and uses Oracle Streams to maintain these tablespaces at both databases. This procedure can either perform these actions directly, or it can generate a script that performs these actions.

Run this procedure at the capture database. The capture database is the database that captures changes made to the source database.

Note:

- This procedure automatically excludes database objects that are not supported by Oracle Streams in the tablespaces from the replication environment by adding rules to the negative rule set of each capture and apply process. Query the `DBA_STREAMS_UNSUPPORTED` data dictionary view to determine which database objects are not supported by Oracle Streams. If unsupported database objects are not excluded, then capture errors will result.
- This procedure replaces the deprecated `MAINTAIN_TABLESPACES` procedure.

See Also:

"Procedures That Configure an Oracle Streams Environment" for more information about this procedure

Syntax

```
DBMS_STREAMS_ADM.MAINTAIN_TTS(
   tablespace_names             IN DBMS_STREAMS_TABLESPACE_ADM.TABLESPACE_SET,
   source_directory_object      IN VARCHAR2,
   destination_directory_object IN VARCHAR2,
   source_database              IN VARCHAR2,
   destination_database         IN VARCHAR2,
   perform_actions              IN BOOLEAN   DEFAULT TRUE,
   script_name                  IN VARCHAR2  DEFAULT NULL,
   script_directory_object      IN VARCHAR2  DEFAULT NULL,
   dump_file_name               IN VARCHAR2  DEFAULT NULL,
   capture_name                 IN VARCHAR2  DEFAULT NULL,
   capture_queue_table          IN VARCHAR2  DEFAULT NULL,
   capture_queue_name           IN VARCHAR2  DEFAULT NULL,
   capture_queue_user           IN VARCHAR2  DEFAULT NULL,
   propagation_name             IN VARCHAR2  DEFAULT NULL,
   apply_name                   IN VARCHAR2  DEFAULT NULL,
   apply_queue_table            IN VARCHAR2  DEFAULT NULL,
   apply_queue_name             IN VARCHAR2  DEFAULT NULL,
   apply_queue_user             IN VARCHAR2  DEFAULT NULL,
   log_file                     IN VARCHAR2  DEFAULT NULL,
   bi_directional               IN BOOLEAN   DEFAULT FALSE,
   include_ddl                  IN BOOLEAN   DEFAULT FALSE);
```

Parameters

See Also:

"Common Parameters for the Configuration Procedures" for descriptions of the procedure parameters that are not in Table 145-25

Table 145-25 MAINTAIN\_TTS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `tablespace_names` | The local tablespace set to be cloned at the destination database and maintained by Oracle Streams.  The tablespaces in the tablespace set must exist at the source database, but these tablespaces must not exist at the destination database.  A directory object must exist for each directory that contains the datafiles for the tablespace set. The user who invokes this procedure must have `READ` privilege on these directory objects. The directory object cannot point to an Oracle Automatic Storage Management (ASM) disk group.  If `NULL`, then the procedure raises an error.  See Also: [TABLESPACE\_SET Table Type](d_streams_tbl.md) |
| `source_directory_object` | The directory object for the directory on the computer system running the source database into which the generated Data Pump export dump file and the datafiles that comprise the cloned tablespace set are placed. These files remain in this directory after the procedure completes.  If `NULL`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle ASM disk group. |
| `destination_directory_object` | The directory object for the directory on the computer system running the destination database into which the generated Data Pump export dump file and the datafiles that comprise the cloned tablespace set are transferred.  If the source database and destination database run on the same computer system, then the source and destination directories must be different.  If `NULL`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle ASM disk group. |
| `source_database` | The global name of the source database.  If the specified global name is the same as the global name of the local database, then the procedure configures a local capture process for the source database.  If the specified global name is different from the global name of the local database, then the procedure configures a downstream capture process at the local database. In this case, a database link from the local database to the source database with the same name as the global name of the source database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure uses the global name of the local database. |
| `destination_database` | The global name of the destination database.  If the local database is not the destination database, then a database link from the local database to the destination database with the same name as the global name of the destination database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure raises an error. |
| `dump_file_name` | The name of the Data Pump export dump file that contains the specified tablespace set. If a file with the specified file name exists in the specified directory for the `source_directory_object` or `destination_directory_object` parameter, then the procedure raises an error.  If `NULL`, then the export dump file name is generated by the system. In this case, the export dump file name is `expat` `nn``.dmp`, where `nn` is a sequence number. The sequence number is increased to produce an export dump file with a unique name in the source directory. |
| `log_file` | The name of the Data Pump export log file. This log file is placed in the same directory as the Data Pump export dump file.  If `NULL`, then the log file name is the same name as the export dump file name with an extension of `.clg`. |

Usage Notes

The specified set of tablespaces must be self-contained. In this context "self-contained" means that there are no references from inside the set of tablespaces pointing outside of the set of tablespaces. For example, if a partitioned table is partially contained in the set of tablespaces, then the set of tablespaces is not self-contained.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tspaces.htm#ADMIN011) for more information about self-contained tablespace sets

Additional Privileges Required by the MAINTAIN\_TTS Procedure

In addition to the required privileges described in "Requirements for Running These Procedures", the user who runs the `MAINTAIN_TTS` procedure must have the necessary privileges to complete the following actions:

- Run subprograms in the `DBMS_STREAMS_TABLESPACES_ADM` package
- The necessary privileges to run the `CLONE_TABLESPACES` procedure in the `DBMS_STREAMS_TABLESPACES_ADM` package at the source database. See [CLONE\_TABLESPACES Procedure](d_streams_tbl.md) for the list of required privileges.
- The necessary privileges to run the `ATTACH_TABLESPACES` procedure in the `DBMS_STREAMS_TABLESPACES_ADM` package at the destination database. See [ATTACH\_TABLESPACES Procedure](d_streams_tbl.md) for the list of required privileges.

---

### MERGE\_STREAMS Procedure

This procedure merges a stream that is flowing from one capture process with a stream that is flowing from another capture process.

Typically, this procedure is used to merge two streams that were split using the `SPLIT_STREAMS` procedure in this package. The `SPLIT_STREAMS` procedure clones components of the original stream when it splits the streams. Therefore, the information in this section uses the following terminology:

- The stream before it was split off has the original queue, original capture process, and original propagation.
- The stream that was split off by the `SPLIT_STREAMS` procedure has a cloned queue, cloned capture process, and cloned propagation.

This procedure is called by the `MERGE_STREAMS_JOB` procedure. The `MERGE_STREAMS_JOB` procedure determines whether the streams are within a user-specified merge threshold so that the streams can be merged safely. If the streams are not within the merge threshold, then the `MERGE_STREAMS_JOB` procedure does nothing. Typically, it is best to run the `MERGE_STREAMS_JOB` procedure instead of running the `MERGE_STREAMS` procedure directly.

However, you can choose to run the `MERGE_STREAMS` procedure directly when the following conditions are met:

- The problem at the destination of the split stream has been corrected, and the destination queue can accept changes.
- The cloned capture process used by the split stream is started and is capturing changes.
- The apply process at the destination database is applying the changes captured by the cloned capture process.
- The `CAPTURE_MESSAGE_CREATE_TIME` in the `GV$STREAMS_CAPTURE` view of the cloned capture process has caught up to, or nearly caught up to, the `CAPTURE_MESSAGE_CREATE_TIME` of the original capture process. The cloned capture process might never completely catch up to the original capture process. Therefore, you can merge the split stream when the cloned capture process has nearly caught up to the original capture process.

The `MERGE_STREAMS` procedure performs the following actions:

1. Stops the cloned capture process.
2. Stops the original capture process.
3. Copies the cloned propagation back to the original propagation. The propagation has the same name as the original propagation after it is copied back.
4. Starts the original capture process from the lower SCN value of these two SCN values:
	- The acknowledged SCN of the cloned propagation.
		- The lowest acknowledged SCN of the other propagations that propagate changes captured by the original capture process.
	When the original capture process is started, it might recapture changes that it already captured, or it might capture changes that were already captured by the cloned capture process. In either case, the relevant apply processes will discard any duplicate changes they receive.
5. Drops the cloned propagation.
6. Drops the cloned capture process.
7. Drops the cloned queue.

See Also:

- MERGE\_STREAMS\_JOB Procedure
- SPLIT\_STREAMS Procedure

Syntax

```
DBMS_STREAMS_ADM.MERGE_STREAMS(
   cloned_propagation_name  IN  VARCHAR2,
   propagation_name         IN  VARCHAR2  DEFAULT NULL,
   queue_name               IN  VARCHAR2  DEFAULT NULL,
   perform_actions          IN  BOOLEAN   DEFAULT TRUE,
   script_name              IN  VARCHAR2  DEFAULT NULL,
   script_directory_object  IN  VARCHAR2  DEFAULT NULL);
```

Parameters

Table 145-26 MERGE\_STREAMS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `cloned_propagation_name` | The name of the cloned propagation used by the stream that was split off from the original stream using the `SPLIT_STREAMS` procedure. The name of the cloned propagation also identifies the cloned queue and capture process used by the cloned propagation.  You must specify an existing propagation name. Do not specify an owner. |
| `propagation_name` | The name of the propagation that is merged back to the original stream.  If `NULL`, then the name of the original propagation in the original stream is used. Specify `NULL` only if the streams were split using the `SPLIT_STREAMS` procedure.  Specify a non- `NULL` value to use a name that is different from the original propagation name or if you are merging two streams that were not split by the `SPLIT_STREAMS` procedure. See "Usage Notes" for more information.  If a non- `NULL` value is specified, then an error is raised under either of the following conditions:  - The queue specified in the `queue_name` parameter does not exist. - The queue specified in the `queue_name` parameter exists but is not used by a capture process. |
| `queue_name` | The name of the queue that is the source queue for the propagation that is merged back.  If `NULL`, then the existing, original queue is the source queue for the propagation that is merged back. Specify `NULL` only if the streams were split using the `SPLIT_STREAMS` procedure.  Specify a non- `NULL` value if you are merging two streams that were not split by the `SPLIT_STREAMS` procedure. Specify the name of the existing queue used by the capture process that will capture changes in the merged stream. See "Usage Notes" for more information. |
| `perform_actions` | If `TRUE`, then the procedure performs the necessary actions to merge the streams directly.  If `FALSE`, then the procedure does not perform the necessary actions to merge the streams directly.  Specify `FALSE` when this procedure is generating a script that you can edit and then run. The procedure raises an error if you specify `FALSE` and either of the following parameters is `NULL`:  - `script_name` - `script_directory_object` |
| `script_name` | If non- `NULL` and the `perform_actions` parameter is `FALSE`, then specify the name of the script generated by this procedure. The script contains all of the statements used to merge the streams. If a file with the specified script name exists in the specified directory for the `script_directory_object` parameter, then the procedure appends the statements to the existing file.  If non- `NULL` and the `perform_actions` parameter is `TRUE`, then the procedure generates the specified script and performs the actions to split the stream directly.  If `NULL` and the `perform_actions` parameter is `TRUE`, then the procedure performs the actions to merge the streams directly and does not generate a script.  If `NULL` and the `perform_actions` parameter is `FALSE`, then the procedure raises an error. |
| `script_directory_object` | The directory object for the directory on the local computer system into which the generated script is placed.  If the `script_name` parameter is `NULL`, then the procedure ignores this parameter and does not generate a script.  If `NULL` and the `script_name` parameter is non- `NULL`, then the procedure raises an error.  Note: The specified directory object cannot point to an Oracle Automatic Storage Management (ASM) disk group. |

Usage Notes

You can use the `MERGE_STREAMS` procedure to merge two streams that were not split using the `SPLIT_STREAMS` procedure. Merging streams in this way can save resources and improve performance when a single database is running two or more capture processes.

The `DBA_STREAMS_SPLIT_MERGE` view contains information about split and merge operations.

---

### MERGE\_STREAMS\_JOB Procedure

This procedure determines whether the original capture process and the cloned capture process are within the specified merge threshold. If they are within the merge threshold, then this procedure runs the `MERGE_STREAMS` procedure to merge the two streams.

Typically, this procedure is used to merge two streams that were split using the `SPLIT_STREAMS` procedure in this package. The `SPLIT_STREAMS` procedure clones components of the original stream when it splits the streams. Therefore, the information in this section uses the following terminology:

- The stream before it was split off has the original queue, original capture process, and original propagation.
- The stream that was split off by the `SPLIT_STREAMS` procedure has a cloned queue, cloned capture process, and cloned propagation.

If the `auto_merge_threshold` parameter was set to a positive number in the `SPLIT_STREAMS` procedure that split the streams, then a merge job runs the `MERGE_STREAMS_JOB` procedure automatically according to its schedule. The schedule name is specified for the `schedule_name` parameter, and the merge job name is specified for the `merge_job_name` parameter when the `MERGE_STREAMS_JOB` procedure is run automatically. The merge job and its schedule were created by the `SPLIT_STREAMS` procedure.

If the `auto_merge_threshold` parameter was set to `NULL` or `0` (zero) in the `SPLIT_STREAMS` procedure that split the streams, then you can run the `MERGE_STREAMS_JOB` procedure manually. In this case, it is not run automatically.

See Also:

- MERGE\_STREAMS Procedure
- SPLIT\_STREAMS Procedure
- [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/man_gen_rep.htm#STREP144) for instructions on using the `MERGE_STREAMS_JOB` procedure

Syntax

```
DBMS_STREAMS_ADM.MERGE_STREAMS_JOB(
   cloned_propagation_name        IN VARCHAR2,
   propagation_name               IN VARCHAR2 DEFAULT NULL,
   queue_name                     IN VARCHAR2 DEFAULT NULL,
   merge_threshold                IN NUMBER,
   schedule_name                  IN VARCHAR2 DEFAULT NULL,
   merge_job_name                 IN VARCHAR2 DEFAULT NULL);
```

Parameters

Table 145-27 MERGE\_STREAMS\_JOB Procedure Parameters

| Parameter | Description |
| --- | --- |
| `cloned_propagation_name` | The name of the cloned propagation used by the stream that was split off from the original stream using the `SPLIT_STREAMS` procedure. The name of the cloned propagation also identifies the cloned queue and capture process used by the cloned propagation.  You must specify an existing propagation name. Do not specify an owner. |
| `propagation_name` | The name of the propagation that is merged back to the original stream.  If `NULL`, then the name of the original propagation in the original stream is used. Specify `NULL` only if the streams were split using the `SPLIT_STREAMS` procedure.  Specify a non- `NULL` value to use a name that is different from the original propagation name or if you are merging two streams that were not split by the `SPLIT_STREAMS` procedure. See "Usage Notes" for more information.  If a non- `NULL` value is specified, then an error is raised under either of the following conditions:  - The queue specified in the `queue_name` parameter does not exist. - The queue specified in the `queue_name` parameter exists but is not used by a capture process. |
| `queue_name` | The name of the queue that is the source queue for the propagation that is merged back.  If `NULL`, then the existing, original queue is the source queue for the propagation that is merged back. Specify `NULL` only if the streams were split using the `SPLIT_STREAMS` procedure.  Specify a non- `NULL` value if you are merging two streams that were not split by the `SPLIT_STREAMS` procedure. Specify the name of the existing queue used by the capture process that will capture changes in the merged stream. See "Usage Notes" for more information. |
| `merge_threshold` | The merge threshold in seconds.  The value of the `CAPTURE_MESSAGE_CREATE_TIME` column for each capture process in the `GV$STREAMS_CAPTURE` dynamic performance view determines whether the streams are merged.  Specifically, if the difference, in seconds, between the `CAPTURE_MESSAGE_CREATE_TIME` of the cloned capture process and the original capture process is less than or equal to the value specified for this parameter, then this procedure runs the `MERGE_STREAMS` procedure to merge the streams. If the difference is greater than the value specified by this parameter, then this procedure does nothing. |
| `schedule_name` | The name of the schedule for the merge job.  If `NULL`, then no schedule name is specified. Typically, you set this parameter to `NULL` when the `auto_merge_threshold` parameter was set to `NULL` or `0` (zero) in the `SPLIT_STREAMS` procedure that split the streams.  Specify `NULL` if you run this procedure manually. |
| `merge_job_name` | The name of the job that merges the streams.  If `NULL`, then no merge job name is specified. Typically, you set this parameter to `NULL` when the `auto_merge_threshold` parameter was set to `NULL` or `0` (zero) in the `SPLIT_STREAMS` procedure that split the streams.  Specify `NULL` if you run this procedure manually. |

Usage Notes

You can use the `MERGE_STREAMS_JOB` procedure to merge two streams that were not split using the `SPLIT_STREAMS` procedure. Merging streams in this way can save resources and improve performance when a single database is running two or more capture processes.

After the `MERGE_STREAMS_JOB` procedure completes, you can query the `DBA_CAPTURE` and `DBA_PROPAGATION` views to determine whether the streams were merged. If the streams were merged, then the cloned capture process and cloned propagation do not appear in these views.

If the streams were merged and the `schedule_name` and `merge_job_name` parameters were non- `NULL`, then the specified schedule and merge job are deleted automatically.

The `DBA_STREAMS_SPLIT_MERGE` view contains information about split and merge operations.

---

### POST\_INSTANTIATION\_SETUP Procedure

This procedure performs the actions required after instantiation to configure an Oracle Streams replication environment.

Run this procedure at the capture database. The capture database is the database that captures changes made to the source database.

To complete the Oracle Streams replication configuration, follow these steps:

1. Run the `PRE_INSTANTIATION_SETUP` procedure at the source database.
2. Perform any necessary instantiation actions.
3. Run the `POST_INSTANTIATION_SETUP` procedure at the source database.

Typically, the Oracle Streams replication environment configured using these steps serves one of the following purposes:

- Replicates changes to shared database objects to keep the database objects synchronized at different databases.
- Replicates changes to database objects during a database maintenance operation, such migrating a database to a different platform. In this case, use the `CLEANUP_INSTANTIATION_SETUP` procedure to remove the replication environment after the maintenance operation is complete.

Attention:

When the `POST_INSTANTIATION_SETUP` procedure is run, the parameter values must match the parameter values specified when the corresponding `PRE_INSTANTIATION_SETUP` procedure was run, except for the values of the following parameters: `perform_actions`, `script_name`, `script_directory_object`, and `start_processes`.

Note:

A capture process never captures changes in the `SYS`, `SYSTEM`, or `CTXSYS` schemas. This procedure does not configure replication for these schemas.

See Also:

- "PRE\_INSTANTIATION\_SETUP Procedure"
- "CLEANUP\_INSTANTIATION\_SETUP Procedure"
- "Procedures That Configure an Oracle Streams Environment" for more information about this procedure
- [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/prep_rep.htm#STREP011) for information about setting up an Oracle Streams replication environment
- [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/ap_strmnt.htm#STRMS165) for information about completing database maintenance operations

Syntax

```
DBMS_STREAMS_ADM.POST_INSTANTIATION_SETUP(
   maintain_mode           IN VARCHAR2,
   tablespace_names        IN DBMS_STREAMS_TABLESPACE_ADM.TABLESPACE_SET,
   source_database         IN VARCHAR2,
   destination_database    IN VARCHAR2,
   perform_actions         IN BOOLEAN         DEFAULT TRUE,
   script_name             IN VARCHAR2        DEFAULT NULL,
   script_directory_object IN VARCHAR2        DEFAULT NULL,
   capture_name            IN VARCHAR2        DEFAULT NULL,
   capture_queue_table     IN VARCHAR2        DEFAULT NULL,
   capture_queue_name      IN VARCHAR2        DEFAULT NULL,
   capture_queue_user      IN VARCHAR2        DEFAULT NULL,
   propagation_name        IN VARCHAR2        DEFAULT NULL,
   apply_name              IN VARCHAR2        DEFAULT NULL,
   apply_queue_table       IN VARCHAR2        DEFAULT NULL,
   apply_queue_name        IN VARCHAR2        DEFAULT NULL,
   apply_queue_user        IN VARCHAR2        DEFAULT NULL,
   bi_directional          IN BOOLEAN         DEFAULT FALSE,
   include_ddl             IN BOOLEAN         DEFAULT FALSE,
   start_processes         IN BOOLEAN         DEFAULT FALSE,
   instantiation_scn       IN NUMBER          DEFAULT NULL,
   exclude_schemas         IN VARCHAR2        DEFAULT NULL,
   exclude_flags           IN BINARY_INTEGER  DEFAULT NULL);
```

Parameters

See Also:

"Common Parameters for the Configuration Procedures" for descriptions of the procedure parameters that are not in Table 145-28

Table 145-28 POST\_INSTANTIATION\_SETUP Procedure Parameters

| Parameter | Description |
| --- | --- |
| `maintain_mode` | Specify one of the following:  - `GLOBAL` to maintain the entire database by configuring replication between the local database and the database specified in the `destination_database` parameter - `TRANSPORTABLE` `TABLESPACES` to maintain a set of tablespaces by configuring replication between the local database and the database specified in the `destination_database` parameter |
| `tablespace_names` | If `maintain_mode` is set to `TRANSPORTABLE` `TABLESPACES`, then specify the local tablespace set to be cloned at the destination database and maintained by Oracle Streams.  The tablespaces in the tablespace set must exist at the source database, but these tablespaces must not exist at the destination database.  Also, a directory object must exist for each directory that contains the datafiles for the tablespace set. The user who invokes this procedure must have `READ` privilege on these directory objects.  If `maintain_mode` is set to `GLOBAL`, then specify an empty tablespace set.  Regardless of the `maintain_mode` setting, an error is raised if the `tablespace_names` parameter is not set or is set to `NULL`.  See Also: [TABLESPACE\_SET Table Type](d_streams_tbl.md) |
| `source_database` | The global name of the source database.  If the specified global name is the same as the global name of the local database, then the procedure configures a local capture process for the source database.  If the specified global name is different from the global name of the local database, then the procedure configures a downstream capture process at the local database. In this case, a database link from the local database to the source database with the same name as the global name of the source database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure uses the global name of the local database. |
| `destination_database` | The global name of the destination database.  If the local database is not the destination database, then a database link from the local database to the destination database with the same name as the global name of the destination database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure raises an error. |
| `start_processes` | If `TRUE`, then the procedure starts each capture process and apply process. Any disabled capture or apply process created by the `PRE_INSTANTITAION_SETUP` procedure also is started.  If `FALSE`, then the procedure does not start any capture processes or apply processes. |
| `instantiation_scn` | Specify the instantiation SCN for the database objects at the destination database if the instantiation SCN was not set during instantiation. The instantiation SCN is not set automatically during RMAN instantiations, but the correct instantiation SCN value should be determined during an RMAN instantiation. See the [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/config_simple.htm#STREP138) for more information.  Specify `NULL` if the instantiation SCN was set for the database objects at the destination database during instantiation. The instantiation SCN can be set during export/import instantiations. |
| `exclude_schemas` | A comma-delimited list of schemas to exclude from the Oracle Streams configuration. Schema rules are added to the negative rule sets of each capture process to exclude these schemas.  Specify an asterisk (`*`) to exclude all of the schemas in the database.  If `NULL`, then the procedure does not exclude any schemas in the database.  This parameter is valid only if the `MAINTAIN_MODE` parameter is set to `GLOBAL`. If the `MAINTAIN_MODE` parameter is set to `TRANSPORTABLE` `TABLESPACES`, then the procedure ignores this parameter. |
| `exclude_flags` | Specify what is excluded from the replication configuration in the schemas specified by the `exclude_schemas` parameter. This parameter works the same way in the `PRE_INSTANTIATION_SETUP` and `POST_INSTANTIATION_SETUP` procedures. See "Usage Notes" for the `PRE_INSTANTIATION_SETUP` procedure for more information. |

Usage Notes

The following sections contain usage notes for this procedure.

Self-Contained Tablespace Sets

If the `maintain_mode` parameter is set to `TRANSPORTABLE` `TABLESPACES`, then the specified set of tablespaces must be self-contained. In this context "self-contained" means that there are no references from inside the set of tablespaces pointing outside of the set of tablespaces. For example, if a partitioned table is partially contained in the set of tablespaces, then the set of tablespaces is not self-contained.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tspaces.htm#ADMIN011) for more information about self-contained tablespace sets

Destination Database Renamed During RMAN Database Instantiation

If the `maintain_mode` parameter is set to `GLOBAL`, then database instantiation is required before running the `POST_INSTANTIATION_SETUP` procedure. If the RMAN `DUPLICATE` or RMAN `CONVERT` `DATABASE` command is used for database instantiation, then the global name of the destination database can be renamed to the global name of the source database during instantiation. In this case, before you run the `POST_INSTANTIATION_SETUP` procedure, complete the following steps:

1. Rename the global name of the destination database back to the name specified in the `destination_database` parameter.
2. At the destination database, drop and re-create any loopback database links that existed on the source and were cloned on the destination database. For example, suppose the source database `dbs1.net` has a database link that refers to itself. Suppose the destination database is `dbs2.net`. At the destination database, drop and re-create this database link as a loopback database link that refers to itself (`dbs2.net`).
3. At the destination database, drop any database links that were cloned from the source database and are from the source database to the destination database. For example, if the source database is `dbs1.net` and the destination database is `dbs2.net`, then drop any database links on the destination database that are from `dbs1.net` to `dbs2.net`.
4. Create a database link from the destination database to the source database with the same name as the global name of the source database. The database link must be accessible to the Oracle Streams administrator at the destination database.
	This database link is required because the `POST_INSTANTIATION_SETUP` procedure runs the `SET_GLOBAL_INSTANTIATION_SCN` procedure in the `DBMS_APPLY_ADM` package at the destination database, and the `SET_GLOBAL_INSTANTIATION_SCN` procedure requires the database link. The instantiation SCN is set to the value specified in the `instantiation_scn` parameter of the `POST_INSTANTIATION_SETUP` procedure.

Note:

When the RMAN `DUPLICATE` or `CONVERT` `DATABASE` command is used for database instantiation, the destination database cannot be the capture database.

Oracle Streams Components Removed From the Destination Database

If the `maintain_mode` parameter is set to `GLOBAL`, then database instantiation is required before running the `POST_INSTANTIATION_SETUP` procedure. During database instantiation, Oracle Streams components created by the `PRE_INSTANTIATION_SETUP` procedure, such as Oracle Streams clients and queues, can be copied from the source database to the destination database. The `POST_INSTANTIATION_SETUP` procedure removes the Stream components created by the `PRE_INSTANTIATION_SETUP` procedure from the destination database.

In some cases, rule sets and rules created by the `PRE_INSTANTIATION_SETUP` procedure might not be removed from the destination database. The `POST_INSTANTIATION_SETUP` procedure does not associate these rule sets and rules with any Stream clients in the destination database. Optionally, you can remove these rule sets and rules from the destination database after the `POST_INSTANTIATION_SETUP` procedure, or the script generated by the procedure, completes.

Note:

The `POST_INSTANTIATION_SETUP` procedure only removes Oracle Streams components that were created by the `PRE_INSTANTIATION_SETUP` procedure. It does not remove Oracle Streams components that were created in a different way.

---

### PRE\_INSTANTIATION\_SETUP Procedure

This procedure performs the actions required before instantiation to configure an Oracle Streams replication environment.

Run this procedure at the capture database. The capture database is the database that captures changes made to the source database.

To complete the Oracle Streams replication configuration, follow these steps:

1. Run the `PRE_INSTANTIATION_SETUP` procedure at the database that will be the source database in the Stream replication environment.
2. Perform any necessary instantiation actions.
3. Run the `POST_INSTANTIATION_SETUP` procedure at the source database.

Typically, the Oracle Streams replication environment configured using these steps serves one of the following purposes:

- Replicates changes to shared database objects to keep the database objects synchronized at different databases.
- Replicates changes to database objects during a database maintenance operation, such migrating a database to a different platform. In this case, use the `CLEANUP_INSTANTIATION_SETUP` procedure to remove the replication environment after the maintenance operation is complete.

Note:

- A capture process never captures changes in the `SYS`, `SYSTEM`, or `CTXSYS` schemas. This procedure does not configure replication for these schemas.
- When the RMAN `DUPLICATE` or `CONVERT` `DATABASE` command is used for database instantiation, the destination database cannot be the capture database.

See Also:

- "POST\_INSTANTIATION\_SETUP Procedure"
- "CLEANUP\_INSTANTIATION\_SETUP Procedure"
- "Procedures That Configure an Oracle Streams Environment" for more information about this procedure
- [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/prep_rep.htm#STREP011) for information about setting up an Oracle Streams replication environment
- [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/ap_strmnt.htm#STRMS165) for information about completing database maintenance operations

Syntax

```
DBMS_STREAMS_ADM.PRE_INSTANTIATION_SETUP(
   maintain_mode           IN VARCHAR2,
   tablespace_names        IN DBMS_STREAMS_TABLESPACE_ADM.TABLESPACE_SET,
   source_database         IN VARCHAR2,
   destination_database    IN VARCHAR2,
   perform_actions         IN BOOLEAN         DEFAULT TRUE,
   script_name             IN VARCHAR2        DEFAULT NULL,
   script_directory_object IN VARCHAR2        DEFAULT NULL,
   capture_name            IN VARCHAR2        DEFAULT NULL,
   capture_queue_table     IN VARCHAR2        DEFAULT NULL,
   capture_queue_name      IN VARCHAR2        DEFAULT NULL,
   capture_queue_user      IN VARCHAR2        DEFAULT NULL,
   propagation_name        IN VARCHAR2        DEFAULT NULL,
   apply_name              IN VARCHAR2        DEFAULT NULL,
   apply_queue_table       IN VARCHAR2        DEFAULT NULL,
   apply_queue_name        IN VARCHAR2        DEFAULT NULL,
   apply_queue_user        IN VARCHAR2        DEFAULT NULL,
   bi_directional          IN BOOLEAN         DEFAULT FALSE,
   include_ddl             IN BOOLEAN         DEFAULT FALSE,
   start_processes         IN BOOLEAN         DEFAULT FALSE,
   exclude_schemas         IN VARCHAR2        DEFAULT NULL,
   exclude_flags           IN BINARY_INTEGER  DEFAULT NULL);
```

Parameters

See Also:

"Common Parameters for the Configuration Procedures" for descriptions of the procedure parameters that are not in Table 145-29

Table 145-29 PRE\_INSTANTIATION\_SETUP Procedure Parameters

| Parameter | Description |
| --- | --- |
| `maintain_mode` | Specify one of the following:  - `GLOBAL` to maintain the entire database by configuring replication between the local database and the database specified in the `destination_database` parameter - `TRANSPORTABLE` `TABLESPACES` to maintain a set of tablespaces by configuring replication between the local database and the database specified in the `destination_database` parameter |
| `tablespace_names` | If `maintain_mode` is set to `TRANSPORTABLE` `TABLESPACES`, then specify the local tablespace set to be cloned at the destination database and maintained by Oracle Streams.  The tablespaces in the tablespace set must exist at the source database, but these tablespaces must not exist at the destination database.  Also, a directory object must exist for each directory that contains the datafiles for the tablespace set. The user who invokes this procedure must have `READ` privilege on these directory objects.  If `maintain_mode` is set to `GLOBAL`, then specify an empty tablespace set.  Regardless of the `maintain_mode` setting, an error is raised if the `tablespace_names` parameter is not set or is set to `NULL`.  See Also: [TABLESPACE\_SET Table Type](d_streams_tbl.md) |
| `source_database` | The global name of the source database.  If the specified global name is the same as the global name of the local database, then the procedure configures a local capture process for the source database.  If the specified global name is different from the global name of the local database, then the procedure configures a downstream capture process at the local database. In this case, a database link from the local database to the source database with the same name as the global name of the source database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure uses the global name of the local database. |
| `destination_database` | The global name of the destination database.  If the local database is not the destination database, then a database link from the local database to the destination database with the same name as the global name of the destination database must exist and must be accessible to the user who runs the procedure.  If `NULL`, then the procedure raises an error. |
| `capture_queue_table` | The name of the queue table for each queue used by a capture process, specified as `[``schema_name``.]` `queue_table_name`. For example, `strmadmin.streams_queue_table`. If the schema is not specified, then the current user is the default.  If `NULL`, then the system generates a name for the queue table of each queue used by a capture process, and the current user is the owner of each queue table. |
| `start_processes` | If `TRUE`, then the procedure starts each capture process and apply process.  If `FALSE`, then the procedure does not start any capture processes or apply processes. |
| `exclude_schemas` | A comma-delimited list of schemas to exclude from the Oracle Streams configuration. Schema rules are added to the negative rule sets of each capture process to exclude these schemas.  Specify an asterisk (`*`) to exclude all of the schemas in the database.  If `NULL`, then the procedure does not exclude any schemas in the database.  This parameter is valid only if the `MAINTAIN_MODE` parameter is set to `GLOBAL`. If the `MAINTAIN_MODE` parameter is set to `TRANSPORTABLE` `TABLESPACES`, then the procedure ignores this parameter. |
| `exclude_flags` | Specify what to exclude from the replication configuration in the schemas specified by the `exclude_schemas` parameter. See "Usage Notes" for more information. |

Usage Notes

The following sections contain usage notes for this procedure.

Self-Contained Tablespace Sets

If the `maintain_mode` parameter is set to `TRANSPORTABLE` `TABLESPACES`, then the specified set of tablespaces must be self-contained. In this context "self-contained" means that there are no references from inside the set of tablespaces pointing outside of the set of tablespaces. For example, if a partitioned table is partially contained in the set of tablespaces, then the set of tablespaces is not self-contained.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tspaces.htm#ADMIN011) for more information about self-contained tablespace sets

The exclude\_flags Parameter

Specify one of the following values:

- `DBMS_STREAMS_ADM.EXCLUDE_FLAGS_FULL` to exclude changes to the schemas and all of the database objects in the schemas
- `DBMS_STREAMS_ADM.EXCLUDE_FLAGS_UNSUPPORTED` to exclude changes to the database objects that are not supported by Oracle Streams in the schemas

If both of these values are specified, then the procedure raises an error.

In addition to `DBMS_STREAMS_ADM.EXCLUDE_FLAGS_FULL` or `DBMS_STREAMS_ADM.EXCLUDE_FLAGS_UNSUPPORTED`, specify one or both of the following values:

- `DBMS_STREAMS_ADM.EXCLUDE_FLAGS_DML` to exclude data manipulation language (DML) changes made to the excluded database objects
- `DBMS_STREAMS_ADM.EXCLUDE_FLAGS_FULL` to exclude data definition language (DDL) changes made to the excluded database objects

Use the plus sign (`+`) to specify more than one of these values. For example, to maintain DML changes to the tables in a schemas specified by the `exclude_schemas` parameter but exclude DDL changes to these schemas and the database objects in these schemas, specify the following for this parameter:

```
DBMS_STREAMS_ADM.EXCLUDE_FLAGS_FULL + 
DBMS_STREAMS_ADM.EXCLUDE_FLAGS_DDL
```

To exclude DML and DDL changes made to unsupported database objects in the schemas specified by the `exclude_schemas` parameter, specify the following for this parameter:

```
DBMS_STREAMS_ADM.EXCLUDE_FLAGS_UNSUPPORTED + 
DBMS_STREAMS_ADM.EXCLUDE_FLAGS_DML +
DBMS_STREAMS_ADM.EXCLUDE_FLAGS_DDL
```

Rules for the excluded database objects are added to the negative rule set of each capture process. Therefore, changes to the excluded database objects will not be captured and replicated.

This parameter is valid only if the `maintain_mode` parameter is set to `GLOBAL` and the `exclude_schemas` parameter is set to a non- `NULL` value. If the `maintain_mode` parameter is set to `GLOBAL` and the `exclude_schemas` parameter is set to a `NULL`, then the procedure ignores this parameter. If the `maintain_mode` parameter is set to `TRANSPORTABLE` `TABLESPACES`, then this the procedure ignores this parameter and excludes any database objects in the specified tablespace set that are not supported by Oracle Streams from the Oracle Streams configuration automatically.

Also, if schemas are specified in the `exclude_schemas` parameter, but the `exclude_flags` parameter is set to `NULL`, then the procedure does not add any rules to the negative rule set of any capture process, and the procedure includes the schemas specified in the `exclude_schemas` parameter in the replication environment.

---

### PURGE\_SOURCE\_CATALOG Procedure

This procedure removes all Oracle Streams data dictionary information at the local database for the specified object. You can use this procedure to remove Oracle Streams metadata that is not needed currently and will not be needed in the future.

Syntax

```
DBMS_STREAMS_ADM.PURGE_SOURCE_CATALOG(
   source_database     IN  VARCHAR2,
   source_object_name  IN  VARCHAR2,
   source_object_type  IN  VARCHAR2);
```

Parameters

Table 145-30 PURGE\_SOURCE\_CATALOG Procedure Parameters

| Parameter | Description |
| --- | --- |
| `source_database` | The global name of the source database containing the object.  If you do not include the domain name, then the procedure appends it to the database name automatically. For example, if you specify `DBS1` and the domain is `.NET`, then the procedure specifies `DBS1.NET` automatically. |
| `source_object_name` | The name of the object specified as `[``schema_name``.]` `object_name`. For example, `hr.employees`. If the schema is not specified, then the current user is the default. |
| `source_object_type` | Type of the object. Currently, `TABLE` is the only possible object type. |

Usage Notes

The global name of the source database containing the object must be specified for the `source_database` parameter. If the current database is not the source database for the object, then the procedure removes data dictionary information about the object from the current database, not the source database.

For example, suppose changes to the `hr.employees` table at the `dbs1.net` source database are being applied to the `hr.employees` table at the `dbs2.net` destination database. Also, suppose `hr.employees` at `dbs2.net` is not a source at all. In this case, specifying `dbs2.net` as the `source_database` for this table results in an error. However, specifying `dbs1.net` as the `source_database` for this table while running the `PURGE_SOURCE_CATALOG` procedure at the `dbs2.net` database removes data dictionary information about the table at `dbs2.net`.

Do not run this procedure at a database if either of the following conditions are true:

- Logical change records (LCRs) captured by the capture process for the object are or might be applied locally without reinstantiating the object.
- LCRs captured by the capture process for the object are or might be forwarded by the database without reinstantiating the object.
	Note:
	These conditions do not apply to LCRs that were not created by the capture process. That is, these conditions do not apply to user-created LCRs.

---

### RECOVER\_OPERATION Procedure

This procedure provides options for operations that stopped because they encountered an errors. These operations include split and merge operations, Oracle Streams replication configuration operations, and Oracle Streams change table configuration operations. This procedure either rolls forward the operation, rolls back the operation, or purges all of the metadata about the operation.

This procedure only can perform these actions for the following operations:

- Split and merge operations using:
	- The `split_threshold` and `merge_threshold` capture process parameters set to non- `NULL` values to enable automatic split and merge
		- SPLIT\_STREAMS Procedure
		- MERGE\_STREAMS\_JOB Procedure
- Change table configuration operations performed by the MAINTAIN\_CHANGE\_TABLE Procedure
- Replication configuration operations performed by the following procedures:
	- MAINTAIN\_GLOBAL Procedure
		- MAINTAIN\_SCHEMAS Procedure
		- MAINTAIN\_SIMPLE\_TABLESPACE Procedure
		- MAINTAIN\_SIMPLE\_TTS Procedure
		- MAINTAIN\_TABLES Procedure
		- MAINTAIN\_TABLESPACES Procedure
		- MAINTAIN\_TTS Procedure
		- PRE\_INSTANTIATION\_SETUP Procedure
		- POST\_INSTANTIATION\_SETUP Procedure

Information about the operation is stored in the following data dictionary views when the operation is in process:

- [`DBA_RECOVERABLE_SCRIPT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4196.htm#REFRN23545)
- [`DBA_RECOVERABLE_SCRIPT_PARAMS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4200.htm#REFRN23548)
- [`DBA_RECOVERABLE_SCRIPT_BLOCKS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4197.htm#REFRN23546)
- [`DBA_RECOVERABLE_SCRIPT_ERRORS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4198.htm#REFRN23547)

For split and merge operations, the data dictionary views are populated at the database that contains the capture process. For the configuration operations, the data dictionary views are populated at the database where the replication configuration procedure was run.

When the operation completes successfully, metadata about the operation is moved from the `DBA_RECOVERABLE_SCRIPT` view to the [`DBA_RECOVERABLE_SCRIPT_HIST`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4199.htm#REFRN23755) view. The other views, `DBA_RECOVERABLE_SCRIPT_PARAMS`, `DBA_RECOVERABLE_SCRIPT_BLOCKS`, and `DBA_RECOVERABLE_SCRIPT_ERRORS`, retain information about the operation until it is purged automatically after 30 days.

When one of these operations encounters an error and stops, metadata about the operation remains in these views. In this case, you can either roll forward, roll back, or purge the metadata about the operation using the `RECOVER_OPERATION` procedure. If you choose to roll forward the operation, then correct conditions that caused the errors reported in `DBA_RECOVERABLE_SCRIPT_ERRORS` before proceeding.

For split and merge operations, run the `RECOVER_OPERATION` procedure at the database that contains the capture process. For the configuration operations, run the `RECOVER_OPERATION` procedure at the database where the replication configuration procedure was run.

Note:

- Regarding the configuration operations, the procedure must configure the environment directly (`perform_actions` `=>` `TRUE`), not by generating a script, for information about the operation to be stored in the recoverable views and for the operation to be managed by the `RECOVER_OPERATION` procedure.
- To run the `RECOVER_OPERATION` procedure, both databases must be Oracle Database 10g Release 2 or later databases.

See Also:

[Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/man_gen_rep.htm#STREP149)

Syntax

```
DBMS_STREAMS_ADM.RECOVER_OPERATION(
   script_id       IN  RAW,
   operation_mode  IN  VARCHAR2  DEFAULT 'FORWARD');
```

Parameters

Table 145-31 RECOVER\_OPERATION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `script_id` | The operation id of the operation that is being rolled forward, rolled back, or purged. Query the `SCRIPT_ID` column of the `DBA_RECOVERABLE_SCRIPT` data dictionary view to determine the operation id. |
| `operation_mode` | If `FORWARD`, then the procedure rolls forward the operation. Specify `FORWARD` to try to complete the operation.  If `ROLLBACK`, then the procedure rolls back all of the actions performed in the operation. If the rollback is successful, then this option also moves the metadata about the operation from the `DBA_RECOVERABLE_SCRIPT` view to the `DBA_RECOVERABLE_SCRIPT_HIST` view. The other views retain information about the operation for 30 days.  If `PURGE`, then the procedure moves the metadata about the operation from the `DBA_RECOVERABLE_SCRIPT` view to the `DBA_RECOVERABLE_SCRIPT_HIST` view without rolling the operation back. The other views retain information about the operation for 30 days. |

---

### REMOVE\_QUEUE Procedure

This procedure removes the specified `ANYDATA` queue.

Specifically, this procedure performs the following actions:

1. Waits until all current enqueue and dequeue transactions commit.
2. Stops the queue, which means that no further enqueues into the queue or dequeues from the queue are allowed.
3. Drops the queue.
4. If the `drop_unused_queue_table` parameter is set to `TRUE`, then drops the queue table if it is empty and no other queues are using it.
5. If the `cascade` parameter is set to `TRUE`, then drops all of the Oracle Streams clients that are using the queue.
	Note:
	The specified queue must be a `ANYDATA` queue.

Syntax

```
DBMS_STREAMS_ADM.REMOVE_QUEUE(
   queue_name               IN  VARCHAR2,
   cascade                  IN  BOOLEAN  DEFAULT FALSE,
   drop_unused_queue_table  IN  BOOLEAN  DEFAULT TRUE);
```

Parameters

Table 145-32 REMOVE\_QUEUE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `queue_name` | The name of the queue to remove, specified as `[``schema_name``.]` `queue_name`. For example, `strmadmin.streams_queue`. If the schema is not specified, then the current user is the default. |
| `cascade` | If `TRUE`, then the procedure drops any Oracle Streams clients that use the queue.  If `FALSE`, then the procedure raises an error if there are any Oracle Streams clients that use the queue. Before you run this procedure with the `cascade` parameter set to `FALSE`, make sure no Oracle Streams clients are using the queue currently. |
| `drop_unused_queue_table` | If `TRUE` and the queue table for the queue is empty, then the procedure drops the queue table. The queue table is not dropped if it contains any messages or if it is used by another queue.  If `FALSE`, then the procedure does not drop the queue table. |

---

### REMOVE\_RULE Procedure

This procedure removes the specified rule or all rules from the rule set associated with the specified capture process, synchronous capture, apply process, propagation, or messaging client.

If this procedure results in an empty positive rule set for a messaging client, then the procedure drops the messaging client automatically.

Note:

If a rule was automatically created by the system, and you want to drop the rule, then you should use this procedure to remove the rule instead of the `DBMS_RULE_ADM.DROP_RULE` procedure. If you use the `DBMS_RULE_ADM.DROP_RULE` procedure, then some metadata about the rule might remain.

Syntax

```
DBMS_STREAMS_ADM.REMOVE_RULE(
   rule_name         IN  VARCHAR2,
   streams_type      IN  VARCHAR2,
   streams_name      IN  VARCHAR2,
   drop_unused_rule  IN  BOOLEAN  DEFAULT TRUE,
   inclusion_rule    IN  BOOLEAN  DEFAULT TRUE);
```

Parameters

Table 145-33 REMOVE\_RULE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_name` | The name of the rule to remove, specified as `[``schema_name``.]` `rule_name`. If `NULL`, then the procedure removes all rules from the specified capture process, synchronous capture, apply process, propagation, or messaging client rule set.  For example, to specify a rule in the `hr` schema named `prop_rule1`, enter `hr.prop_rule1`. If the schema is not specified, then the current user is the default. |
| `streams_type` | The type of Oracle Streams client:  - Specify `capture` for a capture process. - Specify `sync_capture` for a synchronous capture. - Specify `propagation` for a propagation. - Specify `apply` for an apply process. - Specify `dequeue` for a messaging client. |
| `streams_name` | The name of the Oracle Streams client, which can be a capture process, synchronous capture, propagation, apply process, or messaging client. Do not specify an owner.  If the specified Oracle Streams client does not exist, but there is metadata in the data dictionary that associates the rule with this client, then the procedure removes the metadata.  If the specified Oracle Streams client does not exist, and there is no metadata in the data dictionary that associates the rule with this client, then the procedure raises an error. |
| `drop_unused_rule` | If `TRUE` and the rule is not in any rule set, then the procedure drops the rule from the database.  If `TRUE` and the rule exists in any rule set, then the procedure does not drop the rule from the database.  If `FALSE`, then the procedure does not drop the rule from the database. |
| `inclusion_rule` | If `inclusion_rule` is `TRUE`, then the procedure removes the rule from the positive rule set for the Oracle Streams client.  If `inclusion_rule` is `FALSE`, then the procedure removes the rule from the negative rule set for the Oracle Streams client. |

---

### REMOVE\_STREAMS\_CONFIGURATION Procedure

This procedure removes the Oracle Streams configuration at the local database.

Syntax

```
DBMS_STREAMS_ADM.REMOVE_STREAMS_CONFIGURATION;
```

Usage Notes

Specifically, this procedure performs the following actions at the local database:

- Drops all capture processes
- If any tables have been prepared for instantiation, then aborts preparation for instantiation for the table using the `ABORT_TABLE_INSTANTIATION` procedure in the `DBMS_CAPTURE_ADM` package
- If any schemas have been prepared for instantiation, then aborts preparation for instantiation for the schema using the `ABORT_SCHEMA_INSTANTIATION` procedure in the `DBMS_CAPTURE_ADM` package
- If the database has been prepared for instantiation, then aborts preparation for instantiation for the database using the `ABORT_GLOBAL_INSTANTIATION` procedure in the `DBMS_CAPTURE_ADM` package
- Drops propagations that were created using either the `DBMS_STREAMS_ADM` package or the `DBMS_PROPAGATION_ADM` package. Before a propagation is dropped, its propagation job is disabled. Does not drop propagations that were created using the `DBMS_AQADM` package.
- Disables all propagation jobs used by propagations
- Drops all apply processes. If there are apply errors in the error queue for an apply process, then this procedure deletes these apply errors before it drops the apply process.
- Removes specifications for DDL handlers used by apply processes, but does not delete the PL/SQL procedures used by these handlers
- Removes specifications for message handlers used by apply processes, but does not delete the PL/SQL procedures used by these handlers
- Removes specifications for precommit handlers used by apply processes, but does not delete the PL/SQL procedures used by these handlers
- Removes the instantiation SCN and ignore SCN for each apply object and schema and for the entire database
- Removes messaging clients
- Unsets message notification specifications that were set using the `SET_MESSAGE_NOTIFICATION` procedure in the `DBMS_STREAMS_ADM` package
- Removes specifications for procedure DML handlers and error handlers, but does not delete the PL/SQL procedures used by these handlers
- Removes update conflict handlers
- Removes specifications for substitute key columns for apply tables
- Drops rule sets and rules that were created using the `DBMS_STREAMS_ADM` package.
- Drops unused rule sets that were used by capture processes, propagations, apply processes, and messaging clients, and removes the rules in these rule sets. These rules and rule sets are removed regardless of whether they were created using the `DBMS_STREAMS_ADM` package or the `DBMS_RULE_ADM` package.

This procedure stops capture processes and apply processes before it drops them.

This procedure does not drop rule sets or rules if they meet both of the following conditions:

- The rule sets or rules were created using the `DBMS_RULE_ADM` package.
- The rule sets or rules were not used by a capture process, propagation, apply process, or messaging client.

Attention:

Running this procedure is dangerous. You should run this procedure only if you are sure you want to remove the entire Oracle Streams configuration at a database.

Note:

- Running this procedure repeatedly does not cause errors. If the procedure fails to complete, then you can run it again.
- This procedure commits multiple times.

See Also:

- [STOP\_CAPTURE Procedure](d_cap_a.md) in the `DBMS_CAPTURE_ADM` package
- [STOP\_APPLY Procedure](d_apply.md) in the `DBMS_APPLY_ADM` package
- REMOVE\_RULE Procedure in the `DBMS_STREAMS_ADM` package

---

### RENAME\_COLUMN Procedure

This procedure either adds or removes a declarative rule-based transformation which renames a column in a row logical change record (LCR) that satisfies the specified rule.

For the transformation to be performed when the specified rule evaluates to `TRUE`, the rule must be in the positive rule set of an Oracle Streams client. Oracle Streams clients include capture processes, synchronous captures, propagations, apply processes, and messaging clients.

Note:

- The `RENAME_COLUMN` procedure supports the same data types supported by Oracle Streams capture processes.
- Declarative transformations can transform row LCRs only. These row LCRs can be captured by a capture process, captured by a synchronous capture, or constructed and enqueued by an application. Therefore, a DML rule must be specified when you run this procedure. If a DDL is specified, then the procedure raises an error.

See Also:

[Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm) for more information about [declarative rule-based transformations](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_transform.htm#STRMS151) and about [the data types supported by Oracle Streams capture processes](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_capture.htm#STRMS136)

Syntax

```
DBMS_STREAMS_ADM.RENAME_COLUMN(
   rule_name         IN  VARCHAR2,
   table_name        IN  VARCHAR2,
   from_column_name  IN  VARCHAR2,
   to_column_name    IN  VARCHAR2,
   value_type        IN  VARCHAR2  DEFAULT '*',
   step_number       IN  NUMBER    DEFAULT 0,
   operation         IN  VARCHAR2  DEFAULT 'ADD');
```

Parameters

Table 145-34 RENAME\_COLUMN Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_name` | The name of the rule, specified as `[``schema_name``.]` `rule_name`. If `NULL`, then the procedure raises an error.  For example, to specify a rule in the `hr` schema named `employees12`, enter `hr.employees12`. If the schema is not specified, then the current user is the default. |
| `table_name` | The name of the table in which the column is renamed in the row LCR, specified as `[``schema_name``.]` `object_name`. For example, `hr.employees`. If the schema is not specified, then the current user is the default. |
| `from_column_name` | The name of the column to be renamed in each row LCR that satisfies the rule. |
| `to_column_name` | The new name of the column in each row LCR that satisfies the rule. |
| `value_type` | Specify `'NEW'` to rename the column in the new values in the row LCR.  Specify `'OLD'` to rename the column in the old values in the row LCR.  Specify `'*'` to rename the column in both the old and new values in the row LCR. |
| `step_number` | The order of execution of the transformation.  See Also: [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_transform.htm#STRMS145) for more information about transformation ordering |
| `operation` | Specify `'ADD'` to add the transformation to the rule.  Specify `'REMOVE'` to remove the transformation from the rule. |

Usage Notes

When `'REMOVE'` is specified for the `operation` parameter, all of the rename column declarative rule-based transformations for the specified rule are removed that match the specified `table_name`, `column_name`, and `step_number` parameters. Nulls specified for these parameters act as wildcards. The following table lists the behavior of the `RENAME_COLUMN` procedure when one or more of these parameters is `NULL`:

| table\_name | from\_column\_name | to\_column\_name | step\_number | Result |
| --- | --- | --- | --- | --- |
| `NULL` | `NULL` | `NULL` | `NULL` | Remove all rename column transformations for the specified rule. |
| `NULL` | `NULL` | `NULL` | non- `NULL` | Remove all rename column transformations with the specified `step_number` for the specified rule. |
| `NULL` | `NULL` | non- `NULL` | non- `NULL` | Remove all rename column transformations with the specified `to_column_name` and `step_number` for the specified rule. |
| `NULL` | non- `NULL` | non- `NULL` | non- `NULL` | Remove all rename column transformations with the specified `table_name` and `step_number` for the specified rule. |
| `NULL` | `NULL` | non- `NULL` | `NULL` | Remove all rename column transformations with the specified column\_name for the specified rule. |
| non- `NULL` | `NULL` | non- `NULL` | `NULL` | Remove all rename column transformations with the specified `table_name` and column\_name for the specified rule. |
| `NULL` | non- `NULL` | `NULL` | `NULL` | Remove all rename column transformations with the specified `table_name` for the specified rule. |
| `NULL` | non- `NULL` | non- `NULL` | `NULL` | Remove all rename column transformations with the specified `table_name`, column\_name, and `step_number` for the specified rule. |
| non- `NULL` | `NULL` | non- `NULL` | `NULL` | Remove all rename column transformations with the specified `table_name`, column\_name, and `step_number` for the specified rule. |
| non- `NULL` | non- `NULL` | non- `NULL` | `NULL` | Remove all rename column transformations with the specified `table_name`, column\_name, and `step_number` for the specified rule. |
| non- `NULL` | non- `NULL` | non- `NULL` | non- `NULL` | Remove all rename column transformations with the specified `table_name`, column\_name, and `step_number` for the specified rule. |

---

### RENAME\_SCHEMA Procedure

This procedure either adds or removes a declarative rule-based transformation which renames a schema in a row logical change record (LCR) that satisfies the specified rule.

For the transformation to be performed when the specified rule evaluates to `TRUE`, the rule must be in the positive rule set of an Oracle Streams client. Oracle Streams clients include capture processes, synchronous captures, propagations, apply processes, and messaging clients.

Note:

Declarative transformations can transform row LCRs only. These row LCRs can be captured by a capture process, captured by a synchronous capture, or constructed and enqueued by an application. Therefore, a DML rule must be specified when you run this procedure. If a DDL is specified, then the procedure raises an error.

See Also:

[Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_transform.htm#STRMS151) for more information about declarative rule-based transformations

Syntax

```
DBMS_STREAMS_ADM.RENAME_SCHEMA(
   rule_name         IN  VARCHAR2,
   from_schema_name  IN  VARCHAR2,
   to_schema_name    IN  VARCHAR2,
   step_number       IN  NUMBER    DEFAULT 0,
   operation         IN  VARCHAR2  DEFAULT 'ADD');
```

Parameters

Table 145-35 RENAME\_SCHEMA Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_name` | The name of the rule, specified as `[``schema_name``.]` `rule_name`. If `NULL`, then the procedure raises an error.  For example, to specify a rule in the `hr` schema named `employees12`, enter `hr.employees12`. If the schema is not specified, then the current user is the default. |
| `from_schema_name` | The name of the schema to be renamed in each row LCR that satisfies the rule. |
| `to_schema_name` | The new name of the schema in each row LCR that satisfies the rule. |
| `step_number` | The order of execution of the transformation.  See Also: [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_transform.htm#STRMS145) for more information about transformation ordering |
| `operation` | Specify `'ADD'` to add the transformation to the rule.  Specify `'REMOVE'` to remove the transformation from the rule. |

Usage Notes

When `'REMOVE'` is specified for the `operation` parameter, all of the rename schema declarative rule-based transformations for the specified rule are removed that match the specified `from_schema_name`, `to_schema_name`, and `step_number` parameters. Nulls specified for these parameters act as wildcards. The following table lists the behavior of the `RENAME_SCHEMA` procedure when one or more of these parameters is `NULL`:

| from\_schema\_name | to\_schema\_name | step\_number | Result |
| --- | --- | --- | --- |
| `NULL` | `NULL` | `NULL` | Remove all rename schema transformations for the specified rule. |
| `NULL` | `NULL` | non- `NULL` | Remove all rename schema transformations with the specified `step_number` for the specified rule. |
| `NULL` | non- `NULL` | non- `NULL` | Remove all rename schema transformations with the specified `to_schema_name` and `step_number` for the specified rule. |
| non- `NULL` | `NULL` | non- `NULL` | Remove all rename schema transformations with the specified `from_schema_name` and `step_number` for the specified rule. |
| `NULL` | non- `NULL` | `NULL` | Remove all rename schema transformations with the specified `to_schema_name` for the specified rule. |
| non- `NULL` | non- `NULL` | `NULL` | Remove all rename schema transformations with the specified `from_schema_name` and to\_schema\_name for the specified rule. |
| non- `NULL` | `NULL` | `NULL` | Remove all rename schema transformations with the specified `from_schema_name` for the specified rule. |
| non- `NULL` | non- `NULL` | non- `NULL` | Remove all rename schema transformations with the specified `from_schema_name`, `to_schema_name`, and `step_number` for the specified rule. |

---

### RENAME\_TABLE Procedure

This procedure either adds or removes a declarative rule-based transformation which renames a table in a row logical change record (row LCR) that satisfies the specified rule.

For the transformation to be performed when the specified rule evaluates to `TRUE`, the rule must be in the positive rule set of an Oracle Streams client. Oracle Streams clients include capture processes, synchronous captures, propagations, apply processes, and messaging clients.

Note:

Declarative transformations can transform row LCRs only. These row LCRs can be captured by a capture process, captured by a synchronous capture, or constructed and enqueued by an application. Therefore, a DML rule must be specified when you run this procedure. If a DDL is specified, then the procedure raises an error.

See Also:

[Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_transform.htm#STRMS151) for more information about declarative rule-based transformations

Syntax

```
DBMS_STREAMS_ADM.RENAME_TABLE(
   rule_name        IN  VARCHAR2,
   from_table_name  IN  VARCHAR2,
   to_table_name    IN  VARCHAR2,
   step_number      IN  NUMBER    DEFAULT 0,
   operation        IN  VARCHAR2  DEFAULT 'ADD');
```

Parameters

Table 145-36 RENAME\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_name` | The name of the rule, specified as `[``schema_name``.]` `rule_name`. If `NULL`, then the procedure raises an error.  For example, to specify a rule in the `hr` schema named `employees12`, enter `hr.employees12`. If the schema is not specified, then the current user is the default. |
| `from_table_name` | The name of the table to be renamed in each row LCR that satisfies the rule, specified as `[``schema_name``.]` `object_name`. For example, `hr.employees`. If the schema is not specified, then the current user is the default. |
| `to_table_name` | The new name of the table in each row LCR that satisfies the rule, specified as `[``schema_name``.]` `object_name`. For example, `humres.staff`.  The transformation can rename the table only, the schema only, or the table and the schema. If the schema is not specified, then the current user is the default. |
| `step_number` | The order of execution of the transformation.  See Also: [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_transform.htm#STRMS145) for more information about transformation ordering |
| `operation` | Specify `'ADD'` to add the transformation to the rule.  Specify `'REMOVE'` to remove the transformation from the rule. |

Usage Notes

When `'REMOVE'` is specified for the `operation` parameter, all of the rename table declarative rule-based transformations for the specified rule are removed that match the specified `from_table_name`, `to_table_name`, and `step_number` parameters. Nulls specified for these parameters act as wildcards. The following table lists the behavior of the `RENAME_TABLE` procedure when one or more of these parameters is `NULL`:

| from\_table\_name | to\_table\_name | step\_number | Result |
| --- | --- | --- | --- |
| `NULL` | `NULL` | `NULL` | Remove all rename table transformations for the specified rule. |
| `NULL` | `NULL` | non- `NULL` | Remove all rename table transformations with the specified `step_number` for the specified rule. |
| `NULL` | non- `NULL` | non- `NULL` | Remove all rename table transformations with the specified `to_table_name` and `step_number` for the specified rule. |
| non- `NULL` | `NULL` | non- `NULL` | Remove all rename table transformations with the specified `from_table_name` and `step_number` for the specified rule. |
| `NULL` | non- `NULL` | `NULL` | Remove all rename table transformations with the specified `to_table_name` for the specified rule. |
| non- `NULL` | non- `NULL` | `NULL` | Remove all rename table transformations with the specified `from_table_name` and `to_table_name` for the specified rule. |
| non- `NULL` | `NULL` | `NULL` | Remove all rename table transformations with the specified `from_table_name` for the specified rule. |
| non- `NULL` | non- `NULL` | non- `NULL` | Remove all rename table transformations with the specified `from_table_name`, `to_table_name`, and `step_number` for the specified rule. |

---

### SET\_MESSAGE\_NOTIFICATION Procedure

This procedure sets a notification for messages that can be dequeued by a specified Oracle Streams messaging client from a specified queue. A notification is sent when a message is enqueued into the specified queue and the specified messaging client can dequeue the message because the message satisfies its rule sets.

Note:

- Currently, messaging clients cannot dequeue buffered messages.
- The `DBMS_AQ` package can also configure notifications. The `DBMS_AQ` package provides some notification features that are not available in `DBMS_STREAMS_ADM` package, such as buffered message notifications and notification grouping by time.

Syntax

```
DBMS_STREAMS_ADM.SET_MESSAGE_NOTIFICATION(
   streams_name          IN  VARCHAR2,
   notification_action   IN  VARCHAR2,
   notification_type     IN  VARCHAR2     DEFAULT 'PROCEDURE',
   notification_context  IN  ANYDATA      DEFAULT NULL,
   include_notification  IN  BOOLEAN      DEFAULT TRUE,
   queue_name            IN  VARCHAR2     DEFAULT 'streams_queue');
```

Parameters

Table 145-37 SET\_MESSAGE\_NOTIFICATION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `streams_name` | The name of the Oracle Streams messaging client. Do not specify an owner.  For example, if the user `strmadmin` is the messaging client, then specify `strmadmin.` |
| `notification_action` | The action to be performed on message notification. Specify one of the following:  - For URL notifications, specify a URL without the prefix `http://`. 	For example, to specify the URL `http://www.company.com:8080`, enter the following: 	``` 	www.company.com:8080 	``` - For email notifications, specify an email address. 	For example, to specify an the email address `xyz@company.com`, enter the following: 	``` 	xyz@company.com 	``` - For PL/SQL procedure notifications, specify an existing user-defined PL/SQL procedure in the form `[``schema_name``.]` `procedure_name`. If the `schema_name` is not specified, then the user who invokes the `SET_MESSAGE_NOTIFICATION` procedure is the default. The procedure must be a `PLSQLCALLBACK` data structure. 	For example, to specify a procedure named `notify_orders` in the `oe` schema, enter the following: 	``` 	oe.notify_orders 	```  See Also: Examples for more information about message notification procedures |
| `notification_type` | The type of notification. Specify one of the following:  - `HTTP` if you specified a URL for `notification_action` - `MAIL` if you specified an email address for `notification_action` - `PROCEDURE` if you specified a user-defined procedure for `notification_action`  The type must match the specification for the `notification_action` parameter. |
| `notification_context` | The context of the notification. The context must be specified using `RAW` data type information. For example, to specify the hexidecimal equivalent of `'FF'`, enter the following:  ``` ANYDATA.ConvertRaw(HEXTORAW('FF')) ```  The notification context is passed the PL/SQL procedure in procedure notifications and is not relevant for mail or HTTP notifications. |
| `include_notification` | If `TRUE`, then the procedure adds this notification for the specified `streams_name` and `queue_name`. That is, specifying `TRUE` turns on the notification for the `streams_name` and `queue_name`.  If `FALSE`, then the procedure removes this notification for the specified `streams_name` and `queue_name`. That is, specifying `FALSE` turns off the notification for the `streams_name` and `queue_name`. If you specify `FALSE`, then this procedure ignores any specified values for the `notification_action` or `notification_context` parameters. |
| `queue_name` | The name of a local `ANYDATA` queue, specified as `[``schema_name``.]` `queue_name`. The current database must contain the queue. The specified queue must be a `ANYDATA` queue.  For example, to specify a queue named `streams_queue` in the `strmadmin` schema, enter `strmadmin.streams_queue` for this parameter. If the schema is not specified, then the current user is the default. |

Usage Notes

You can specify one of the following types of notifications:

- An email address to which message notifications are sent. When a relevant message is enqueued into the queue, an email with the message properties is mailed to the specified email address.
- A PL/SQL procedure to be invoked on a notification. When a relevant message is enqueued into the queue, the specified PL/SQL procedure is invoked with the message properties. This PL/SQL procedure can dequeue the message.
- An HTTP URL to which the notification is posted. When a relevant message is enqueued into the queue, a notification with the message properties is posted to the specified URL specified.

A client does not need to be connected to the database to receive a notification.

If you register for email notifications, then you should use the `DBMS_AQELM` package to set the host name and port name for the SMTP server that will be used by the database to send email notifications. If required, then you should set the send-from email address, which is set by the database as the `sent` `from` field. You need a Java-enabled database to use this feature.

If you register for HTTP notifications, you might want to use the `DBMS_AQELM` package to set the host name and port number for the proxy server and a list of no-proxy domains that will be used by the database to post HTTP notifications.

Each notification is an `AQXmlNotification`, which includes of the following:

- `notification_options`, which includes the following:
	- `destination` - The destination queue from which the message was dequeued
		- `consumer_name` - The name of the messaging client that dequeued the message
- `message_set` - The set of message properties
	See Also:
	- The documentation for the `DBMS_AQELM` package for more information on email notifications and HTTP notifications
	- [Oracle Database 2 Day + Data Replication and Integration Guide](https://docs.oracle.com/cd/E11882_01/server.112/e17516/tdpii_messaging.htm#TDPII043) for an example that configures message notification to automatically dequeue of messages of interest
	- [Oracle Streams Advanced Queuing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e11013/toc.htm) and [Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm) for more information about message notifications and XML
	- [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_rules.htm#STRMS006) for more information about how rules are used in Oracle Streams

Examples

If you use a message notification procedure, then this PL/SQL procedure must have the following signature:

```
PROCEDURE procedure_name(
  context  IN  ANYDATA,
  reginfo  IN  SYS.AQ$_REG_INFO,
  descr    IN  SYS.AQ$_DESCRIPTOR);
```

Here, `procedure_name` stands for the name of the procedure. The procedure is a `PLSQLCALLBACK` data structure that specifies the user-defined PL/SQL procedure to be invoked on message notification.

The following is a simple example of a notification procedure that dequeues a message of type `oe.user_msg` using the message identifier and consumer name sent by the notification. To complete the example, first create the type:

```
CREATE TYPE oe.user_msg AS OBJECT(
  object_name    VARCHAR2(30),
  object_owner   VARCHAR2(30),
  message        VARCHAR2(50));
/
```

Next, create the procedure:

```
CREATE OR REPLACE PROCEDURE oe.notification_dequeue(
  context  ANYDATA, 
  reginfo  SYS.AQ$_REG_INFO, 
  descr    SYS.AQ$_DESCRIPTOR)
AS 
  dequeue_options     DBMS_AQ.DEQUEUE_OPTIONS_T; 
  message_properties  DBMS_AQ.MESSAGE_PROPERTIES_T; 
  message_handle      RAW(16); 
  message             ANYDATA; 
  oe_message          oe.user_msg; 
  rc                  PLS_INTEGER; 
BEGIN 
  -- Get the message identifier and consumer name from the descriptor 
  dequeue_options.msgid := descr.msg_id; 
  dequeue_options.consumer_name := descr.consumer_name; 
  -- Dequeue the message 
  DBMS_AQ.DEQUEUE( 
    queue_name         => descr.queue_name, 
    dequeue_options    => dequeue_options, 
    message_properties => message_properties, 
    payload            => message, 
    msgid              => message_handle);
  rc := message.getobject(oe_message); 
  COMMIT; 
END; 
/
```

See Also:

[Oracle Database PL/SQL Packages and Types Reference](d_aq.md) for more information about `PLSQLCALLBACK` data structures

---

### SET\_MESSAGE\_TRACKING Procedure

Sets the tracking label for logical change records (LCRs) produced by the current session. This procedure affects only the current session. Any LCRs produced by the current session are tracked, including captured LCRs and persistent LCRs.

Note:

The tracking label set by this procedure does not track non-LCR messages.

See Also:

GET\_MESSAGE\_TRACKING Function

Syntax

```
DBMS_STREAMS_ADM.SET_MESSAGE_TRACKING(
   tracking_label IN VARCHAR2  DEFAULT 'Streams_tracking',
   actions        IN NUMBER    DEFAULT DBMS_STREAMS_ADM.ACTION_MEMORY);
```

Parameters

Table 145-38 SET\_MESSAGE\_TRACKING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `tracking_label` | The label used to track the LCRs produced by the session.  Set this parameter to `NULL` to stop message tracking in the current session.  The size limit for a label is 4,000 bytes. |
| `actions` | When `DBMS_STREAMS_ADM.ACTION_MEMORY` is specified, the LCRs are tracked in memory, and the `V$STREAMS_MESSAGE_TRACKING` dynamic performance view is populated with information about the LCRs.  Currently, `DBMS_STREAMS_ADM.ACTION_MEMORY` is the only valid setting for this parameter.  The value specified for this parameter is an enumerated constant. Enumerated constants must be prefixed with the package name. |

---

### SET\_RULE\_TRANSFORM\_FUNCTION Procedure

This procedure sets or removes the transformation function name for a custom rule-based transformation.

Syntax

```
DBMS_STREAMS_ADM.SET_RULE_TRANSFORM_FUNCTION(
   rule_name           IN  VARCHAR2,
   transform_function  IN  VARCHAR2);
```

Parameters

Table 145-39 SET\_RULE\_TRANSFORM\_FUNCTION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_name` | The name of the rule whose rule-based transformation function you are setting or removing, specified as `[``schema_name``.]` `rule_name`.  For example, to specify a rule in the `hr` schema named `prop_rule1`, enter `hr.prop_rule1`. If the schema is not specified, then the current user is the default. |
| `transform_function` | Either the name of the transformation function to be used in the rule-based transformation for the rule or `NULL`.  If you specify a transformation function name, then specify an existing function in one of the following forms:  - `[``schema_name``.]` `function_name` - `[``schema_name``.]` `package_name.function_name`  If the function is in a package, then you must specify the `package_name`. For example, to specify a function in the `transform_pkg` package in the `hr` schema named `executive_to_management`, enter `hr.transform_pkg.executive_to_management`. An error is returned if the specified procedure does not exist.  If the `schema_name` is not specified, then the user who invokes the rule-based transformation function is the default.  If you specify `NULL`, then the `SET_RULE_TRANSFORM_FUNCTION` procedure removes the current custom rule-based transformation from the rule. |

Usage Notes

The following sections contain usage notes for this procedure:

- Transformation Function Signature
- Rule Action Context
- User Who Calls the Transformation Function
- Function Verification

Transformation Function Signature

A custom rule-based transformation function always operates on one message, but it can return one message or many messages. A custom rule-based transformation function that returns one message is a one-to-one transformation function. A one-to-one transformation function must have the following signature:

```
FUNCTION user_function (
   parameter_name   IN  ANYDATA)
RETURN ANYDATA;
```

Here, `user_function` stands for the name of the function and `parameter_name` stands for the name of the parameter passed to the function. The parameter passed to the function is an `ANYDATA` encapsulation of a message, and the function must return an `ANYDATA` encapsulation of a message.

A custom rule-based transformation function that can return multiple messages is a one-to-many transformation function. A one-to-many transformation function must have the following signature:

```
FUNCTION user_function (
   parameter_name  IN  ANYDATA)
RETURN STREAMS$_ANYDATA_ARRAY;
```

Here, `user_function` stands for the name of the function and `parameter_name` stands for the name of the parameter passed to the function. The parameter passed to the function is an `ANYDATA` encapsulation of a message, and the function must return an array that contains zero or more `ANYDATA` encapsulations of a message. If the array contains zero `ANYDATA` encapsulations of a message, then the original message is discarded.

The `STREAMS$_ANYDATA_ARRAY` type is an Oracle-supplied type that has the following definition:

```
CREATE OR REPLACE TYPE SYS.STREAMS$_ANYDATA_ARRAY
   AS VARRAY(2147483647) of ANYDATA
/
```

The following restrictions apply to custom rule-based transformations that use one-to-many functions:

- Rules that are associated with one-to-many functions are supported for Oracle Streams capture processes only. These rules must not be added to rule sets used by other Oracle Streams clients, including propagations, apply processes, and messaging clients.
- One-to-many functions only can operate on row logical change records (row LCRs). They cannot operate on DDL LCRs.
- Row LCRs returned by a one-to-many function cannot contain piecewise LOB, `LONG`, or `LONG` `RAW` operations.
- The one-to-many function must return row LCRs in the correct order. The order of row LCRs in the array (starting from index 1) is the order that the row LCRs will be executed in the transaction.

When an apply process dequeues row LCRs that are the result of a transformation by a one-to-many function, the apply process uses the instantiation SCN of the LCR passed to the one-to-many function for all of row LCRs.

Note:

- An error is raised if a one-to-one or one-to-many transformation function returns `NULL`.
- Only one custom rule-based transformation can be specified for a particular rule. You cannot specify both a one-to-one and a one-to-many transformation function for the same rule.
- For any LCR constructed and returned by a custom rule-based transformation, the `source_database_name`, `transaction_id`, and `scn` parameter values must match the values in the original LCR. Oracle automatically specifies the values in the original LCR for these parameters, even if an attempt is made to construct LCRs with different values.

Rule Action Context

This procedure modifies the specified rule's action context to specify the transformation. A rule's action context is optional information associated with a rule that is interpreted by the client of the rules engine after the rule evaluates to `TRUE` for a message. The client of the rules engine can be a user-created application or an internal feature of Oracle, such as Oracle Streams. The Oracle Streams clients include capture processes, synchronous captures, propagations, apply processes, and messaging clients. The information in an action context is an object of type `SYS.RE$NV_LIST`, which consists of a list of name-value pairs.

A custom rule-based transformation in Oracle Streams always consists of the following name-value pair in an action context:

- If the function is a one-to-one transformation function, then the name is `STREAMS$_TRANSFORM_FUNCTION`. If the function is a one-to-many transformation function, then the name is `STREAMS$_ARRAY_TRANS_FUNCTION`.
- The value is a `ANYDATA` instance containing a PL/SQL function name specified as a `VARCHAR2`. This function performs the transformation.

User Who Calls the Transformation Function

The user that calls the transformation function must have `EXECUTE` privilege on the function. The following list describes which user calls the transformation function:

- If a transformation is specified for a rule used by a capture process, then the user who calls the transformation function is the capture user for the capture process.
- If a transformation is specified for a rule used by a synchronous capture, then the user who calls the transformation function is the capture user for the synchronous capture.
- If a transformation is specified for a rule used by a propagation, then the user who calls the transformation function is the owner of the source queue for the propagation.
- If a transformation is specified on a rule used by an apply process, then the user who calls the transformation function is the apply user for the apply process.
- If a transformation is specified on a rule used by a messaging client, then the user who calls the transformation function is the user who invokes the messaging client.

Function Verification

This procedure does not verify that the specified transformation function exists. If the function does not exist, then an error is raised when an Oracle Streams client tries to invoke the transformation function.

---

### SET\_TAG Procedure

This procedure sets the binary tag for all redo entries subsequently generated by the current session. Each redo entry generated by DML or DDL statements in the current session will have this tag. This procedure affects only the current session.

See Also:

- "GET\_TAG Function"
- [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/rep_tags.htm#STREP008) for more information about tags

Syntax

```
DBMS_STREAMS_ADM.SET_TAG(
   tag  IN RAW  DEFAULT NULL);
```

Parameters

Table 145-40 SET\_TAG Procedure Parameters

| Parameter | Description |
| --- | --- |
| `tag` | The binary tag for all subsequent redo entries generated by the current session. A raw value is a sequence of bytes, and a byte is a sequence of bits.  By default, the tag for a session is `NULL`.  The size limit for a tag value is 2000 bytes. |

Usage Notes

To set the tag to the hexadecimal value of `'17'` in the current session, run the following procedure:

```
EXEC DBMS_STREAMS_ADM.SET_TAG(tag => HEXTORAW('17'));
```

The following are considerations for the `SET_TAG` procedure:

- This procedure is not transactional. That is, the effects of `SET_TAG` cannot be rolled back.
- If the `SET_TAG` procedure is run to set a non- `NULL` session tag before a data dictionary build has been performed on the database, then the redo entries for a transaction that started before the dictionary build might not include the specified tag value for the session. Therefore, perform a data dictionary build before using the `SET_TAG` procedure in a session. A data dictionary build happens when the `DBMS_CAPTURE_ADM.BUILD` procedure is run. The `BUILD` procedure can be run automatically when a capture process is created.

See Also:

[BUILD Procedure](d_cap_a.md)

---

### SET\_UP\_QUEUE Procedure

This procedure creates a queue table and a `ANYDATA` queue.

Syntax

```
DBMS_STREAMS_ADM.SET_UP_QUEUE(
   queue_table     IN  VARCHAR2  DEFAULT 'streams_queue_table',
   storage_clause  IN  VARCHAR2  DEFAULT NULL,
   queue_name      IN  VARCHAR2  DEFAULT 'streams_queue',
   queue_user      IN  VARCHAR2  DEFAULT NULL,
   comment         IN  VARCHAR2  DEFAULT NULL);
```

Parameters

Table 145-41 SET\_UP\_QUEUE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `queue_table` | The name of the queue table specified as `[``schema_name``.]` `queue_table_name`. For example, `strmadmin.streams_queue_table`. If the schema is not specified, then the current user is the default.  If the queue table owner is not specified, then the procedure specifies the user who runs this procedure automatically as the queue table owner.  Queue table names can be a maximum of 24 bytes. |
| `storage_clause` | The storage clause for queue table  The storage parameter is included in the `CREATE` `TABLE` statement when the queue table is created. You can specify any valid table storage clause.  If a tablespace is not specified here, then the procedure creates the queue table and all its related objects in the default user tablespace of the user who runs this procedure. If a tablespace is specified here, then the procedure creates the queue table and all its related objects in the tablespace specified in the storage clause.  If `NULL`, then the procedure uses the storage characteristics of the tablespace in which the queue table is created.  See Also: [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for more information about storage clauses |
| `queue_name` | The name of the queue that will function as the `ANYDATA` queue, specified as `[``schema_name``.]` `queue_name`. For example, `strmadmin.streams_queue`.  If the schema is not specified, then the procedure uses the queue table owner. The owner of the queue table must also be the owner of the queue. The queue owner automatically has privileges to perform all queue operations on the queue.  If the schema is not specified for this parameter, and the queue table owner is not specified in `queue_table`, then the current user is the default.  Queue names can be a maximum of 24 bytes. |
| `queue_user` | The name of the user who requires `ENQUEUE` and `DEQUEUE` privileges for the queue. This user also is configured as a secure queue user of the queue. The queue user cannot grant these privileges to other users because they are not granted with the `GRANT` option.  If `NULL`, then the procedure does not grant any privileges. You can also grant queue privileges to the appropriate users using the `DBMS_AQADM` package. |

[^1]: Creates a new queue at the database running the capture process. The new queue is called the cloned queue because it is a clone of the queue used by the original stream. The new queue will be used by the new, cloned capture process, and it will be the source queue for the new, cloned propagation.

[^2]: Queries the acknowledge SCN for the original propagation. The acknowledged SCN is the last SCN acknowledged by the apply process that applies the changes sent by the propagation.

[^undefined]: Creates a new capture process. The new capture process is called the cloned capture process because it is a clone of the capture process used by the original stream. The procedure sets the start SCN for the cloned capture process to the value of the acknowledged SCN queried in Step 4. The cloned capture process uses the same rule set as the original capture process.

[^undefined]: Drops the original propagation.

[^undefined]: Starts the original capture process with the start SCN set to the acknowledged SCN queried in Step 4.

[^undefined]: If the `auto_merge_threshold` parameter is set to a positive number, then creates an Oracle Scheduler job to run the `MERGE_STREAMS_JOB` procedure at set intervals according to its schedule. When the two streams are within the specified merge threshold, the `MERGE_STREAMS_JOB` procedure runs the `MERGE_STREAMS` procedure to merge the streams automatically.
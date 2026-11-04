---
title: DBMS_STREAMS_ADVISOR_ADM
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_streams_adv.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 146 DBMS\_STREAMS\_ADVISOR\_ADM

The `DBMS_STREAMS_ADVISOR_ADM` package, one of a set of Oracle Streams packages, provides an interface to gather information about an Oracle Streams environment and advise database administrators based on the information gathered. This package is part of the Oracle Streams Performance Advisor.

This chapter contains the following topics:

- Using DBMS\_STREAMS\_ADVISOR\_ADM
- Summary of DBMS\_STREAMS\_ADVISOR\_ADM Subprograms

See Also:

[Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_topology.htm#STRMS170) for instructions about using this package

---

## Using DBMS\_STREAMS\_ADVISOR\_ADM

This section contains topics which relate to using the `DBMS_STREAMS_ADVISOR_ADM` package.

---

### Overview

The `DBMS_STREAMS_ADVISOR_ADM` package enables you to gather and analyze information about an Oracle Streams environment. You can use this information in the following ways:

- To populate data dictionary views with an Oracle Streams topology that contains information about the Oracle Streams components at one or more databases
- To examine the Oracle Streams components at one or more databases in your environment and the ways in which information flows through streams that include these components
- To analyze the performance of the Oracle Streams components in your environment
- To detect performance problems with Oracle Streams components and correct these problems

See Also:

[Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_topology.htm#STRMS170) for instructions about using this package

---

### Security Model

Security on this package can be controlled in either of the following ways:

- Granting `EXECUTE` on this package to selected users or roles.
- Granting `EXECUTE_CATALOG_ROLE` to selected users or roles.

If subprograms in the package are run from within a stored procedure, then the user who runs the subprograms must be granted `EXECUTE` privilege on the package directly. It cannot be granted through a role.

To ensure that the user who runs the subprograms in this package has the necessary privileges, configure an Oracle Streams administrator and connect as the Oracle Streams administrator when using this package.

See Also:

[Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/prep_rep.htm#STREP200) for information about configuring an Oracle Streams administrator

---

### Constants

The `DBMS_STREAMS_ADVISOR_ADM` package defines several enumerated constants for specifying parameter values. Enumerated constants must be prefixed with the package name. For example, `DBMS_DBMS_ADVISOR_ADM.CAPTURE_TYPE`.

Table 146-1 DBMS\_STREAMS\_ADVISOR\_ADM Parameters With Enumerated Constants

| Parameter | Option | Type | Description |
| --- | --- | --- | --- |
| `component_type` | - `CAPTURE_TYPE` - `PROPAGATION_SENDER_TYPE` - `PROPAGATION_RECEIVER_TYPE` - `APPLY_TYPE` - `QUEUE_TYPE` | `NUMBER` | `CAPTURE_TYPE` indicates that the Oracle Streams component is a capture process. The constant number for this option is 1.  `PROPAGATION_SENDER_TYPE` indicates that the Oracle Streams component is a propagation sender. The constant number for this option is 2.  `PROPAGATION_RECEIVER_TYPE` indicates that the Oracle Streams component is a propagation receiver. The constant number for this option is 3.  `APPLY_TYPE` indicates that the Oracle Streams component is an apply process. The constant number for this option is 4.  `QUEUE_TYPE` indicates that the Oracle Streams component is a queue. The constant number for this option is 5. |

---

### Views

The `DBMS_STREAMS_ADVISOR_ADM` package uses the following views:

- [`DBA_STREAMS_TP_COMPONENT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5020.htm#REFRN23611) contains information about each Oracle Streams component at each database.
- [`DBA_STREAMS_TP_COMPONENT_LINK`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5021.htm#REFRN23612) contains information about how messages flow between Oracle Streams components.
- [`DBA_STREAMS_TP_COMPONENT_STAT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5022.htm#REFRN23613) contains temporary performance statistics about each Oracle Streams component.
- [`DBA_STREAMS_TP_DATABASE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5023.htm#REFRN23614) contains information about each database that contains Oracle Streams components.
- [`DBA_STREAMS_TP_PATH_BOTTLENECK`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5024.htm#REFRN23615) contains temporary information about Oracle Streams components that might be slowing down the flow of a stream.
- [`DBA_STREAMS_TP_PATH_STAT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5025.htm#REFRN23616) contains temporary performance statistics about each stream path that exists in the Oracle Streams topology.

The topology information is stored permanently in the following data dictionary views: `DBA_STREAMS_TP_DATABASE`, `DBA_STREAMS_TP_COMPONENT`, and `DBA_STREAMS_TP_COMPONENT_LINK`.

However, the following views contain temporary information: [`DBA_STREAMS_TP_COMPONENT_STAT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5022.htm#REFRN23613), [`DBA_STREAMS_TP_PATH_BOTTLENECK`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5024.htm#REFRN23615), and [`DBA_STREAMS_TP_PATH_STAT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5025.htm#REFRN23616). Some of the data in these views is retained only for the user session that runs the `ANALYZE_CURRENT_PERFORMANCE` procedure. When this user session ends, this temporary information is purged.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm)
- [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_topology.htm#STRMS170) for sample queries that use these views

---

### Operational Notes

This section contains the following operational notes for the `DBMS_STREAMS_ADVISOR_ADM` package:

- Oracle Streams Components Analyzed by the DBMS\_STREAMS\_ADVISOR\_ADM Package
- General Steps for Running the Oracle Streams Performance Advisor and Analyzing the Information

#### Oracle Streams Components Analyzed by the DBMS\_STREAMS\_ADVISOR\_ADM Package

The `DBMS_STREAMS_ADVISOR_ADM` analyzes the following Oracle Streams components at the specified databases:

- Capture processes
- Propagations
- Apply processes
- Queues

The `DBMS_STREAMS_ADVISOR_ADM` package does not analyze the following Oracle Streams components:

- Synchronous captures
- Messaging clients

#### General Steps for Running the Oracle Streams Performance Advisor and Analyzing the Information

To use the `DBMS_STREAMS_ADVISOR_ADM` package, complete the following general steps:

1. Identify the database that you will use to gather the information.
	An administrative user at this database must meet the following requirements:
	- The user must have access to a database link to each database that contains Oracle Streams components.
		- The user must have been granted privileges using the `DBMS_STREAMS_AUTH.GRANT_ADMIN_PRIVILEGE` procedure, and each database link must connect to a user at the remote database that has been granted privileges using the `DBMS_STREAMS_AUTH.GRANT_ADMIN_PRIVILEGE` procedure.
	In an Oracle Streams environment, the Oracle Streams administrator uses this package.
	If no database in your environment meets these requirements, then choose a database, configure the necessary database links, and grant the necessary privileges to the users before proceeding.
2. Connect as the administrative user to the database you identified in Step [^1], and remain connected to the session while you complete the remaining steps.
3. Run the `ANALYZE_CURRENT_PERFORMACE` procedure.
4. Optionally, allow messages to flow in the environment for some time.
5. Optionally, rerun the `ANALYZE_CURRENT_PERFORMACE` procedure one or more times.
6. Query the data dictionary views listed in "Views" to analyze the Oracle Streams environment.
7. If you want to update the information in the data dictionary views or if you add new Oracle Streams components to any database in the environment, repeat Steps [^2] -[^3].

Note:

When you exit the user session, the rate, bandwidth, event, and flow control statistics are purged from the data dictionary views.

---

## Summary of DBMS\_STREAMS\_ADVISOR\_ADM Subprograms

Table 146-2 DBMS\_STREAMS\_ADVISOR\_ADM Package Subprograms

| Subprogram | Description |
| --- | --- |
| ANALYZE\_CURRENT\_PERFORMANCE Procedure | Gathers information about the Oracle Streams components at one or more databases in your environment and analyzes Oracle Streams performance based on the information gathered |

---

### ANALYZE\_CURRENT\_PERFORMANCE Procedure

This procedure gathers information about the Oracle Streams components at one or more databases in your environment and analyzes Oracle Streams performance based on the information gathered.

The performance analyses includes:

- Calculating bottleneck components for each separate stream
- Calculating the throughput of each Oracle Streams component
- Calculating the latency of each Oracle Streams component
- Calculating the top wait event of each Oracle Streams component
- Calculating the message rate of each stream
- Calculating the transaction rate of each stream

The procedure places the gathered information in data dictionary views.

Note:

The parameters in this procedure must all be either non- `NULL` or `NULL`.

See Also:

- [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_topology.htm#STRMS170) for instructions on using this procedure
- "Views"

Syntax

```
DBMS_STREAMS_ADVISOR_ADM.ANALYZE_CURRENT_PERFORMANCE(
   component_name  IN  VARCHAR2  DEFAULT NULL,
   component_db    IN  VARCHAR2  DEFAULT NULL,
   component_type  IN  NUMBER    DEFAULT NULL);
```

Parameters

Table 146-3 ANALYZE\_CURRENT\_PERFORMANCE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `component_name` | The name of the Oracle Streams component to analyze. For example, to analyze a capture process named `capture01`, then specify `capture01`.  If `NULL`, then all of the Oracle Streams components are analyzed, and the other two parameters must also be `NULL`. |
| `component_db` | The global name of the database that contains the component specified in the `component_name` parameter. For example, if the `db.net` database contains the component, then specify `db.net`.  If `NULL`, then all of the Oracle Streams components are analyzed, and the other two parameters must also be `NULL`. |
| `component_type` | The type of the component specified in the `component_name` parameter. If the `component_name` parameter is non- `NULL`, then specify one of the following:  - `DBMS_STREAMS_ADVISOR_ADM.CAPTURE_TYPE` - `DBMS_STREAMS_ADVISOR_ADM.PROPAGATION_SENDER_TYPE` - `DBMS_STREAMS_ADVISOR_ADM.PROPAGATION_RECEIVER_TYPE` - `DBMS_STREAMS_ADVISOR_ADM.APPLY_TYPE` - `DBMS_STREAMS_ADVISOR_ADM.QUEUE_TYPE`  See "Constants" for information about these constants.  If `NULL`, then all of the Oracle Streams components are analyzed, and the other two parameters must also be `NULL`. |

[^1]: Identify the database that you will use to gather the information.

An administrative user at this database must meet the following requirements:

- The user must have access to a database link to each database that contains Oracle Streams components.
- The user must have been granted privileges using the `DBMS_STREAMS_AUTH.GRANT_ADMIN_PRIVILEGE` procedure, and each database link must connect to a user at the remote database that has been granted privileges using the `DBMS_STREAMS_AUTH.GRANT_ADMIN_PRIVILEGE` procedure.

In an Oracle Streams environment, the Oracle Streams administrator uses this package.

If no database in your environment meets these requirements, then choose a database, configure the necessary database links, and grant the necessary privileges to the users before proceeding.

[^2]: Connect as the administrative user to the database you identified in Step 1, and remain connected to the session while you complete the remaining steps.

[^3]: Query the data dictionary views listed in "Views" to analyze the Oracle Streams environment.

[^undefined]: If you want to update the information in the data dictionary views or if you add new Oracle Streams components to any database in the environment, repeat Steps 2 - 6.
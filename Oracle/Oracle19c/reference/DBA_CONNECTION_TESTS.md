---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_CONNECTION_TESTS.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.216 DBA\_CONNECTION\_TESTS

`DBA_CONNECTION_TESTS` provides information about connection tests in use for CDBs and PDBs.

This view shows SQL and non-SQL connection tests.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PREDEFINED` | `VARCHAR2(1)` |  | Indicates whether the test is predefined or custom. Possible values:  - `Y`: The test is predefined. - `N`: The test is added by the user.  Predefined tests can be disabled, but not deleted. |
| `CONNECTION_TEST_TYPE` | `VARCHAR2(15)` |  | Indicates the test type. Possible values include:  - `ENDREQUEST_TEST`: Used when request boundaries are received at the RDBMS. Oracle Connection Pools and all application servers using JDK9 send request boundaries to the RDBMS starting in Oracle Database 12c Release 2 (12.2.0.1). - `PING_TEST`: Used when you are using tests that use the ping function to test the connection, including the OCIPing, isValid, isUsable, connection.status, and PING\_DATABASE connection tests. - `SQL_TEST`: Application servers and applications use SQL tests to check the validity of a connection. Use this value for SQL based connection tests, for example (`SELECT 1 FROM DUAL`;) - `XA_START_TEST`: Applies to services with applications that are using XA transactions. Allows XA tranasactions that are underway to complete and does not allow new XA transactions to start.  The test type values are the `CONNECTION_TEST_TYPE` parameter values that can be specified for the `ENABLE_CONNECTION_TEST` and `DISABLE_CONNECTION_TEST` procedures for the `DBMS_APP_CONT_ADMIN` PL/SQL package. |
| `SQL_CONNECTION_TEST` | `VARCHAR2(64)` |  | SQL test. This column is null for non-SQL tests. |
| `SERVICE_NAME` | `VARCHAR2(128)` |  | Optional service name qualifier |
| `ENABLED` | `VARCHAR2(1)` |  | Indicates whether the SQL test is enabled. Possible values:  - `Y`: The test is enabled. - `N`: The test is not enabled. |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=ARPLS-GUID-423087D8-9844-4CF1-9C4C-4D65541CFA11) for additional information about the `ENABLE_CONNECTION_TEST` procedure for the `DBMS_APP_CONT_ADMIN` PL/SQL package
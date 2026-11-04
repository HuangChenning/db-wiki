---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_AUDIT_UTIL.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 30 DBMS\_AUDIT\_UTIL

The `DBMS_AUDIT_UTIL` package provides functions that enable you to format the output of queries to the `DBA_FGA_AUDIT_TRAIL`, `DBA_AUDIT_TRAIL`, `UNIFIED_AUDIT_TRAIL`, and `V$XML_AUDIT_TRAIL` views.

This chapter contains the following topics:

### 30.1 DBMS\_AUDIT\_UTIL Overview

The functions in the `DBMS_AUDIT_UTIL` package enable you to format the output of queries to the `RLS_INFO` column of several audit trail views so that the output appear in separate rows.

These functions use a cursor to find and format each row of the corresponding view. To use the functions in this package, include the function in a query to one of the following views:

- `DBA_FGA_AUDIT_TRAIL` data dictionary view, for the `DECODE_RLS_INFO_ATRAIL_FGA` function
- `DBA_AUDIT_TRAIL` data dictionary view, for the `DECODE_RLS_INFO_ATRAIL_STD` function
- `UNIFIED_AUDIT_TRAIL` data dictionary view, for the `DECODE_RLS_INFO_ATRAIL_UNI` function
- `V$XML_AUDIT_TRAIL` dynamic view, for the `DECODE_RLS_INFO_ATRAIL_XML` function

### 30.2 DBMS\_AUDIT\_UTIL Security Model

All `DBMS_AUDIT_UTIL` subprograms require the user to have `EXECUTE` privilege on the `DBMS_AUDIT_UTIL` package.

The `SYSDBA` administrative privilege and `AUDIT_ADMIN` and `AUDIT_VIEWER` roles have the `EXECUTE` privilege on the `DBMS_AUDIT_UTIL` package by default. An auditor can view audit data after being granted the `AUDIT_VIEWER` role.

Oracle strongly recommends that only audit administrators have the `EXECUTE` privilege on the `DBMS_AUDIT_UTIL` package and be granted the `AUDIT_VIEWER` role.

### 30.3 DBMS\_AUDIT\_UTIL Views

The views in this section display the audit information used by the `DBMS_AUDIT_UTIL` package function.

Table 30-1 displays the `DBMS_AUDIT_UTIL` views.

Table 30-1 Views Used by DBMS\_AUDIT\_UTIL

| View | Description |
| --- | --- |
| `DBA_FGA_AUDIT_TRAIL` | Displays fine-grained audit record information; used with the `DBMS_AUDIT_UTIL.DECODE_RLS_INFO_ATRAIL_FGA` function |
| `DBA_AUDIT_TRAIL` | Displays standard audit record information; used with the `DBMS_AUDIT_UTIL.DECODE_RLS_INFO_ATRAIL_STD` function |
| `UNIFIED_AUDIT_TRAIL` | Displays unified audit trail information; used with the `DBMS_AUDIT_UTIL.DECODE_RLS_INFO_ATRAIL_XML` function |
| `V$XML_AUDIT_TRAIL` | Displays XML audit record information; used with the `DBMS_AUDIT_UTIL.DECODE_RLS_INFO_ATRAIL_UNI` function |

### 30.4 Summary of DBMS\_AUDIT\_UTIL Subprograms

This table lists the `DBMS_AUDIT_UTIL` subprograms and their descriptions.

Table 30-2 DBMS\_AUDIT\_UTIL Package Subprograms

| Subprogram | Description |
| --- | --- |
| DECODE\_RLS\_INFO\_ATRAIL\_FGA Function | Reformats the output for queries to the `RLS_INFO` column of the `DBA_FGA_AUDIT_TRAIL` data dictionary view |
| DECODE\_RLS\_INFO\_ATRAIL\_STD Function | Reformats the output for queries to the `RLS_INFO` column of the `DBA_AUDIT_TRAIL` data dictionary view |
| DECODE\_RLS\_INFO\_ATRAIL\_UNI Function | Reformats the output for queries to the `RLS_INFO` column of the `UNIFIED_AUDIT_TRAIL` data dictionary view |
| DECODE\_RLS\_INFO\_ATRAIL\_XML Function | Reformats the output for queries to the `RLS_INFO` column of the `V$XML_AUDIT_TRAIL` dynamic view |

#### 30.4.1 DECODE\_RLS\_INFO\_ATRAIL\_FGA Function

This function reformats the output for queries to the `RLS_INFO` column of the `DBA_FGA_AUDIT_TRAIL` data dictionary view so that the output is easily readable. It is used for the concatenated Oracle Virtual Private Database predicates for multiple fine-grained audit policies in an environment that has not been enabled for unified auditing. It returns the output in separate rows.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DBSEG60681) regarding fine-grained auditing

Syntax

```
DECODE_RLS_INFO_ATRAIL_FGA(
  IN_CURSOR                  REF CURSOR               IN)
RETURN PIPELINED ROW;
```

Parameters

Except for the `IN_CURSOR` parameter, the parameters for the `DECODE_RLS_INFO_ATRAIL_FGA` function are the same as the columns in the `DBA_FGA_AUDIT_TRAIL` data dictionary view. See [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=REFRN23075) for more information about this view.

Usage Notes

- To use this function, include it in a query to the `DBA_FGA_AUDIT_TRAIL` data dictionary view, using a cursor similar to the example shown in the following section.
- See [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=REFRN23075) for more information about the `DBA_FGA_AUDIT_TRAIL` data dictionary view.

Example

```
SELECT DB_USER, OBJECT_NAME, SQL_TEXT  
  RLS_PREDICATE, RLS_POLICY_TYPE, RLS_POLICY_OWNER, RLS_POLICY_NAME
  FROM TABLE (DBMS_AUDIT_UTIL.DECODE_RLS_INFO_ATRAIL_FGA 
  (CURSOR (SELECT * FROM DBA_FGA_AUDIT_TRAIL)));
```

Return Values

A piped row with decoded values of `DBA_FGA_AUDIT_TRAIL.RLS_INFO` column.

#### 30.4.2 DECODE\_RLS\_INFO\_ATRAIL\_STD Function

This function reformats the output for queries to the `RLS_INFO` column of the `DBA_AUDIT_TRAIL` data dictionary view so that the output is easily readable. It is used for the concatenated Oracle Virtual Private Database predicates for multiple standard audit records in an environment that has not been enabled for unified auditing. It returns the output in separate rows.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DBSEG1023) regarding auditing

Syntax

```
DECODE_RLS_INFO_ATRAIL_STD(
  IN_CURSOR                  REF CURSOR               IN)
RETURN PIPELINED ROW;
```

Parameters

Except for the `IN_CURSOR` parameter, the parameters for the `DECODE_RLS_INFO_ATRAIL_STD` function are the same as the columns in the `DBA_AUDIT_TRAIL` data dictionary view. See [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=REFRN23023) for more information about this view.

Usage Notes

- To use this function, include it in a query to the `DBA_AUDIT_TRAIL` data dictionary view, using a cursor similar to the example shown in the following section.
- See [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=REFRN23023) for more information about the `DBA_AUDIT_TRAIL` data dictionary view.

Example

```
SELECT USERNAME, USERHOST, ACTION, OBJ_NAME, OBJ_PRIVILEGE
  RLS_PREDICATE, RLS_POLICY_TYPE, RLS_POLICY_OWNER, RLS_POLICY_NAME
  FROM TABLE (DBMS_AUDIT_UTIL.DECODE_RLS_INFO_ATRAIL_STD 
  (CURSOR (SELECT * FROM DBA_AUDIT_TRAIL)));
```

Return Values

A piped row with decoded values of `DBA_AUDIT_TRAIL.RLS_INFO` column

#### 30.4.3 DECODE\_RLS\_INFO\_ATRAIL\_UNI Function

This function reformats the output for queries to the `RLS_INFO` column of the `V$XML_AUDIT_TRAIL` dynamic view so that the output is easily readable. It is used for the concatenated Oracle Virtual Private Database predicates for multiple XML audit records in an environment that has not been enabled for unified auditing. It returns the output in separate rows.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DBSEG-GUID-A215CCAF-4AFF-448A-909C-736EBDED5A8A) regarding unified auditing

Syntax

```
DECODE_RLS_INFO_ATRAIL_UNI(
  IN_CURSOR                  REF CURSOR               IN)
RETURN PIPELINED ROW;
```

Parameters

Except for the `IN_CURSOR` parameter, the parameters for the `DECODE_RLS_INFO_ATRAIL_UNI` function are the same as the columns in the `V$XML_AUDIT_TRAIL` data dictionary view. See [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=REFRN30405) for more information about this view.

Usage Notes

- To use this function, include it in a query to the `V$XML_AUDIT_TRAIL` dynamic view, using a cursor similar to the example shown in the following section.
- See [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=REFRN30405) for more information about the `V$XML_AUDIT_TRAIL` dynamic view.

Example

```
SELECT OBJECT_NAME, SQL_TEXT 
  RLS_PREDICATE, RLS_POLICY_TYPE, RLS_POLICY_OWNER, RLS_POLICY_NAME
  FROM TABLE (DBMS_AUDIT_UTIL.DECODE_RLS_INFO_ATRAIL_UNI 
  (CURSOR (SELECT * FROM V$XML_AUDIT_TRAIL)));
```

Return Values

A piped row with decoded values of `V$XML_AUDIT_TRAIL.RLS_INFO` column

#### 30.4.4 DECODE\_RLS\_INFO\_ATRAIL\_XML Function

This function reformats the output for queries to the `RLS_INFO` column of the `UNIFIED_AUDIT_TRAIL` data dictionary view so that the output is easily readable. It is used for the concatenated Oracle Virtual Private Database predicates for multiple audit records from unified audit policies. It returns the output in separate rows.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DBSEG1023) regarding auditing

Syntax

```
DECODE_RLS_INFO_ATRAIL_XML(
  IN_CURSOR                  REF CURSOR               IN)
RETURN PIPELINED ROW;
```

Parameters

Except for the `IN_CURSOR` parameter, the parameters for the `DECODE_RLS_INFO_ATRAIL_XML` function are the same as the columns in the `UNIFIED_AUDIT_TRAIL` data dictionary view. See [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=REFRN29162) for more information about this view.

Usage Notes

- To use this function, include it in a query to the `UNIFIED_AUDIT_TRAIL` data dictionary view, using a cursor similar to the example shown in the following section.
- See [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=REFRN29162) for more information about the `UNIFIED_AUDIT_TRAIL` data dictionary view.

Example

```
SELECT DBUSERNAME, ACTION_NAME, OBJECT_NAME, SQL_TEXT, 
  RLS_PREDICATE, RLS_POLICY_TYPE, RLS_POLICY_OWNER, RLS_POLICY_NAME 
  FROM TABLE (DBMS_AUDIT_UTIL.DECODE_RLS_INFO_ATRAIL_XML 
  (CURSOR (SELECT * FROM UNIFIED_AUDIT_TRAIL)));
```

Return Values

A piped row with decoded values of `UNIFIED_AUDIT_TRAIL.RLS_INFO` column
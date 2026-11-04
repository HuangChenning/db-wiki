---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_LOCKDOWN_PROFILES.html
tags:
  - oracle
  - 12c
  - reference
---

The `PRIVATE_DBAAS`, `PUBLIC_DBAAS`, and `SAAS` lockdown profiles are empty placeholder profiles for the lockdown profiles of their corresponding deployment type. You can modify and add restrictions to these profiles based on their deployment purpose. For example, if you have a Software as a Service (SAAS) application, you can modify the `SAAS` lockdown profile and use it. You can also delete and re-create these profiles.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PROFILE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the lockdown profile |
| `RULE_TYPE` | `VARCHAR2(128)` |  | Rule type. A lockdown profile is used to restrict operations that can be performed by users connected to a given PDB. It provides the ability to add or remove different types of rules like STATEMENT, FEATURES or OPTIONS which will be restricted in the PDB. |
| `RULE` | `VARCHAR2(128)` |  | Rule to be enabled or disabled |
| `CLAUSE` | `VARCHAR2(128)` |  | Clause of the statement |
| `CLAUSE_OPTION` | `VARCHAR2(128)` |  | Option of the clause |
| `OPTION_VALUE` | `VARCHAR2(4000)` |  | Value of the option |
| `MIN_VALUE` | `VARCHAR2(4000)` |  | Minimum value allowed for the option  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `MAX_VALUE` | `VARCHAR2(4000)` |  | Maximum value allowed for the option  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `LIST` | `VARCHAR2(4000)` |  | List of allowed values for the option  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `STATUS` | `VARCHAR2(7)` |  | Status of the lockdown profile:  - `ENABLE` - `DISABLE` - `EMPTY` |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [PDB\_LOCKDOWN](PDB_LOCKDOWN.md) "
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=CNCPT-GUID-1F6D3E4F-786A-47A0-A36C-83BAB75FCDAE) for an introduction to PDB lockdown profiles
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SQLRF-GUID-1CDEC3A3-F3F1-4279-9370-36AACF416E0A) for more information about creating lockdown profiles
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SQLRF-GUID-62D428C1-5081-43CA-B45D-7FF1B81363E7) for more information about dropping lockdown profiles
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SQLRF-GUID-B4029154-54A8-4B78-97C3-9CED416F1C34) for more information about altering lockdown profiles
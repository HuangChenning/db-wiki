---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ASSEMBLIES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.81 ALL\_ASSEMBLIES

`ALL_ASSEMBLIES` provides information about assemblies accessible to the current user.

Related Views

- `DBA_ASSEMBLIES` provides information about all assemblies in the database.
- `USER_ASSEMBLIES` provides information about all assemblies owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the assembly |
| `ASSEMBLY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the assembly |
| `FILE_SPEC` | `VARCHAR2(4000)` |  | Operating system file specification of the assembly |
| `SECURITY_LEVEL` | `VARCHAR2(10)` |  | The maximum security level of the assembly |
| `IDENTITY` | `VARCHAR2(4000)` |  | The identity of the assembly |
| `STATUS` | `VARCHAR2(7)` |  | Status of the assembly |

See Also:

- " [DBA\_ASSEMBLIES](DBA_ASSEMBLIES.md) "
- " [USER\_ASSEMBLIES](USER_ASSEMBLIES.md) "
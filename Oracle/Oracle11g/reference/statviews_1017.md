---
title: ALL_ASSEMBLIES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1017.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_ASSEMBLIES` provides information about assemblies accessible to the current user.

Related Views

- `DBA_ASSEMBLIES` provides information about all assemblies in the database.
- `USER_ASSEMBLIES` provides information about all assemblies owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the assembly |
| `ASSEMBLY_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the assembly |
| `FILE_SPEC` | `VARCHAR2(4000)` |  | Operating system file specification of the assembly |
| `SECURITY_LEVEL` | `VARCHAR2(10)` |  | The maximum security level of the assembly |
| `IDENTITY` | `VARCHAR2(4000)` |  | The identity of the assembly |
| `STATUS` | `VARCHAR2(7)` |  | Status of the assembly |

See Also:

- ["DBA\_ASSEMBLIES"](statviews_3068.md)
- ["USER\_ASSEMBLIES"](statviews_5229.md)
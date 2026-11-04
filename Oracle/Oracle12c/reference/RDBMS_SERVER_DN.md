---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/RDBMS_SERVER_DN.html
tags:
  - oracle
  - 12c
  - reference
---

`RDBMS_SERVER_DN` specifies the Distinguished Name (DN) of the Oracle server. It is used for retrieving Enterprise Roles from an enterprise directory service.

| Property | Description |
| --- | --- |
| Parameter type | X.500 Distinguished Name |
| Default value | There is no default value. |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | All X.500 Distinguished Name format values |
| Basic | No |

Note:

The `RDBMS_SERVER_DN` parameter is deprecated in Oracle Database 12c Release 1 (12.1.0.2). It is replaced by the `LDAP_DIRECTORY_ACCESS` initialization parameter.

If you do not want to use a directory for enterprise user and privilege management, but prefer to use SSL authentication alone, do not set this parameter.

See Also:

- [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBIMI214) for more information on enterprise roles and the enterprise directory service
- " [LDAP\_DIRECTORY\_ACCESS](LDAP_DIRECTORY_ACCESS.md) "
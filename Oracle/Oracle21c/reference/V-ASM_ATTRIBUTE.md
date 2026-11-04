---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_ATTRIBUTE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.50 V$ASM\_ATTRIBUTE

`V$ASM_ATTRIBUTE` displays one row for each attribute defined. In addition to attributes specified by `CREATE DISKGROUP` and `ALTER DISKGROUP` statements, the view may show other attributes that are created automatically.

Note that attributes are only displayed for disk groups where `COMPATIBLE.ASM` is set to 11.1 or higher.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(256)` | Full name of the attribute |
| `VALUE` | `VARCHAR2(256)` | Value of the attribute |
| `GROUP_NUMBER` | `NUMBER` | Number of the disk group in which this attribute exists (composite primary key) |
| `ATTRIBUTE_INDEX` | `NUMBER` | Number of this attribute in the disk group (composite primary key) |
| `ATTRIBUTE_INCARNATION` | `NUMBER` | Incarnation number for this attribute (composite primary key) |
| `READ_ONLY` | `VARCHAR2(7)` | Indicates whether the attribute is read-only (`Y`) or not (`N`) |
| `SYSTEM_CREATED` | `VARCHAR2(7)` | Indicates whether this is a system-created attribute (`Y`) or not (`N`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

Note:

In an Oracle Database instance, this view returns 0 rows when queried from a PDB.

See Also:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG94106) for more information about viewing Oracle ASM disk group attributes using this view
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information
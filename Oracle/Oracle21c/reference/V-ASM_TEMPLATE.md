---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_TEMPLATE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.69 V$ASM\_TEMPLATE

In an Oracle Automatic Storage Management (Oracle ASM) instance, `V$ASM_TEMPLATE` displays one row for every template present in every disk group mounted by the Oracle ASM instance.

In a database instance, `V$ASM_TEMPLATE` displays one row for every template present in every disk group mounted by the Oracle ASM instance with which the database instance communicates.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Owning disk group number (foreign key to the `V$ASM_DISKGROUP` view) |
| `ENTRY_NUMBER` | `NUMBER` | Template number (primary key) |
| `REDUNDANCY` | `VARCHAR2(6)` | Redundancy of the template:  - `HIGH` - `MIRROR` - `PARITY` - `UNPROT` |
| `STRIPE` | `VARCHAR2(6)` | Indicates how the template is striped:  - `FINE` - `COARSE` |
| `SYSTEM` | `VARCHAR2(1)` | Indicates whether the template is a system template (`Y`) or not (`N`) |
| `NAME` | `VARCHAR2(30)` | Name of the template |
| `PRIMARY_REGION` <sup>Foot 1</sup> | `VARCHAR2(4)` | Region used for allocating primary extents:  - `HOT` - `COLD` |
| `MIRROR_REGION` <sup>Foot 1</sup> | `VARCHAR2(4)` | Region for allocating mirrored extents:  - `HOT` - `COLD` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

<sup>Footnote 1</sup> Intelligent Data Placement is desupported starting with Oracle Database 21c. As a result, the `PRIMARY_REGION` and `MIRROR_REGION` columns are no longer meaningful.

Note:

In an Oracle Database instance, this view returns 0 rows when queried from a PDB.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information
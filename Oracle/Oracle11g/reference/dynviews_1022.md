---
title: "V$ASM_ATTRIBUTE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1022.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ASM_ATTRIBUTE` displays one row for each attribute defined. In addition to attributes specified by `CREATE DISKGROUP` and `ALTER DISKGROUP` statements, the view may show other attributes that are created automatically. Note that attributes are only displayed for disk groups where `COMPATIBLE.ASM` is set to 11.1 or higher.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(256)` | Full name of the attribute |
| `VALUE` | `VARCHAR2(256)` | Value of the attribute |
| `GROUP_NUMBER` | `NUMBER` | Number of the disk group in which this attribute exists (composite primary key) |
| `ATTRIBUTE_INDEX` | `NUMBER` | Number of this attribute in the disk group (composite primary key) |
| `ATTRIBUTE_INCARNATION` | `NUMBER` | Incarnation number for this attribute (composite primary key) |
| `READ_ONLY` | `VARCHAR2(7)` | Indicates whether the attribute is read-only (`Y`) or not (`N`) |
| `SYSTEM_CREATED` | `VARCHAR2(7)` | Indicates whether this is a system-created attribute (`Y`) or not (`N`) |

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmviews.htm#OSTMG10031) for more information about viewing ASM disk group attributes using this view
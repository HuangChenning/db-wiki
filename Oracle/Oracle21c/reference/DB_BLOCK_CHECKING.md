---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_BLOCK_CHECKING.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.73 DB\_BLOCK\_CHECKING

`DB_BLOCK_CHECKING` specifies whether Oracle Database performs block checking for database blocks.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_BLOCK_CHECKING = { FALSE \| OFF \| LOW \| MEDIUM \| TRUE \| FULL }` |
| Default value | `FALSE` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes, with the following restriction:  If block checking is enabled for a CDB, then you cannot subsequently disable block checking in any of its PDBs. That is, if the value of `DB_BLOCK_CHECKING` in a CDB is `LOW`, `MEDIUM`, `TRUE`, or `FULL`, and you then attempt to set the value of `DB_BLOCK_CHECKING` in one of its PDBs to `FALSE` or `OFF`, an error will occur. |
| Basic | No |

Values

- `OFF` or `FALSE`
	No block checking is performed for blocks in user tablespaces. However, semantic block checking for `SYSTEM` tablespace blocks is always turned on.
- `LOW`
	Basic block header checks are performed after block contents change in memory (for example, after `UPDATE`, `INSERT` or `DELETE` statements, or after inter-instance block transfers in Oracle RAC).
- `MEDIUM`
	All `LOW` checks and full semantic checks are performed for all objects except indexes (whose contents can be reconstructed by a drop+rebuild on encountering a corruption).
- `FULL` or `TRUE`
	All `LOW` and `MEDIUM` checks and full semantic checks are performed for all objects.

Oracle checks a block by going through the data in the block, making sure it is logically self-consistent. Block checking can often prevent memory and data corruption. Block checking typically causes 1% to 10% overhead in most applications, depending on workload and the parameter value. Specific DML overhead may be higher. The more updates or inserts in a workload, the more expensive it is to turn on block checking. You should set `DB_BLOCK_CHECKING` to `FULL` if the performance overhead is acceptable.

For backward compatibility, the use of `FALSE` (implying `OFF`) and `TRUE` (implying `FULL`) is preserved.

Caution:

Before enabling block checking with this parameter, Oracle recommends that you detect and repair any logical corruptions in the database. Otherwise, a block that contains logical corruption will be marked as "soft corrupt" after block checking is enabled and the block is modified by a DML statement. This will result in `ORA-1578` errors and the block will be unreadable. For more information about detecting and repairing logical corruptions, see [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=BRADV-GUID-C9F93B27-D13F-465D-A32C-CF6B092CE2F0).

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11820) for more information about this parameter
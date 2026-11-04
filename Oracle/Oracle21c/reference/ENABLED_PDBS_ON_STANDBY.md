---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ENABLED_PDBS_ON_STANDBY.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.126 ENABLED\_PDBS\_ON\_STANDBY

`ENABLED_PDBS_ON_STANDBY` specifies which pluggable databases (PDBs) to replicate on an Oracle Data Guard standby database.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `ENABLED_PDBS_ON_STANDBY = PDB-list` |
| Default value | `*` if no value is specified for this parameter in the `init.ora` file |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | All instances should use the same value. |

Note:

This parameter is meaningful only on standby databases. Its settings are ignored on a primary database.

PDB-list accepts a list of PDB names represented by glob patterns such as “PDB?” or “PDB\*a”, “PDB2”. The glob pattern rules are like those of UNIX shells. The asterisk (\*) and question mark (?) wildcard characters are supported. The? wildcard character matches exactly one unknown character, and the \* wildcard character matches any number of unknown characters. Also, the minus sign (-) character can be used as the first character in a PDB name to indicate that the PDB should be excluded on the standby database.

The following characters are valid in a PDB name: alphanumeric characters, underscore (\_), number sign (#), and dollar sign ($). No other characters are valid. Oracle removes double quotation before processing the PDB name. Therefore you cannot use double quotation marks to embed other characters in the name. The PDB name is case insensitive. These are the same naming conventions as for a database name (as described in the `DB_NAME` initialization parameter description).

These rules apply for the `ENABLED_PDBS_ON_STANDBY` parameter:

- Any PDB names that match glob patterns starting with minus sign (-) will not be part of the standby database.
- If a PDB name matches several patterns in the PDB-list at the same time, the rightmost matched pattern has the highest precedence.
- If this parameter is not specified in the `init.ora` file, it is assumed that “\*” is specified by default.
- If one or more patterns are specified in this parameter, it is assumed that “-\*” is implicitly specified in the leftmost position. For example, `ENABLED_PDBS_ON_STANDBY=“PDB1”, “PDB2”` is equivalent to `ENABLED_PDBS_ON_STANDBY=“-*”, “PDB1”, “PDB2”`. It means that a PDB name that does not match any patterns is not allowed to be part of the standby.

Examples

These examples assumes that nine new PDBs named PDB1A, PDB1B, PDB1C, PDB2A, PDB2B, PDB2C, PDB3A, PDB3B, and PDB3C are being added to the primary database.

1. If STANDBY1 sets `ENABLED_PDBS_ON_STANDBY=“*”` on STANDBY1, then all nine PDBs will be created on STANDBY1.
2. If STANDBY1 sets `ENABLED_PDBS_ON_STANDBY=“PDB1*”` on STANDBY1, then PDB1A, PDB1B, and PDB1C will be created on STANDBY1.
3. If STANDBY1 sets `ENABLED_PDBS_ON_STANDBY=“PDB*A”` on STANDBY1, then PDB1A, PDB2A, and PDB3A will be created on STANDBY1.
4. If STANDBY1 sets `ENABLED_PDBS_ON_STANDBY=“PDB1*”, “-PDB*A”` on STANDBY1, then PDB1B and PDB1C will be created on STANDBY1.
5. If STANDBY1 sets `ENABLED_PDBS_ON_STANDBY=“*”, “-PDB*A”, “-PDB*B”` on STANDBY1, then PDB1C, PDB2C and PDB3C will be created on STANDBY1. All other PDBs match “\*”, and the rightmost pattern has the higher precedence, so they are excluded on the standby.
6. If STANDBY1 sets `ENABLED_PDBS_ON_STANDBY=“*”, “-PDB*A”, “PDB2A”` on STANDBY1, then PDB1A and PDB3A are excluded, but all other PDBs including PDB2A will be created.
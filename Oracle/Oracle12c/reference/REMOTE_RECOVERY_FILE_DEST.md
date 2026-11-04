---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/REMOTE_RECOVERY_FILE_DEST.html
tags:
  - oracle
  - 12c
  - reference
---

`REMOTE_RECOVERY_FILE_DEST` specifies a directory from which to read archive log files during a pluggable database (PDB) refresh operation if the source is not available.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `REMOTE_RECOVERY_FILE_DEST = string` |
| Default value | None |
| Modifiable | `ALTER SYSTEM ... SID='*'` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | The directory location where archive redo logs are accessible can be different on different instances, so this parameter can be set to different values on different instances. |

For a PDB refresh copy to be in sync with its source, redo is accessed from the source PDB over a database link. Sometimes the source PDB or the CDB to which the source PDB belongs is not accessible when the refresh copy needs to be updated. In those cases, if this parameter is set, an attempt will be made to read archive log files from the directory specified by this parameter.

Note:

This initialization parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).
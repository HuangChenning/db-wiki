---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_REGISTRY_SQLPATCH.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_REGISTRY_SQLPATCH` contains information about the SQL patches that have been installed in the database.

A SQL patch is a patch that contains SQL scripts which need to be run after OPatch completes. `DBA_REGISTRY_SQLPATCH` is updated by the datapatch utility. Each row contains information about an installation attempt (apply or roll back) for a given patch.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PATCH_ID` | `NUMBER` | `NOT NULL` | ID associated with the patch |
| `PATCH_UID` | `NUMBER` | `NOT NULL` | UPI (Universal Patch ID) associated with the patch |
| `VERSION` | `VARCHAR2(20)` | `NOT NULL` | 4 digit version on which the patch was installed (for example, 12.1.0.2) |
| `FLAGS` | `VARCHAR2(10)` |  | One or more of the following:  - `B`: Patch is a bundle patch - `J`: Patch is a JVM patch - `N`: Patch requires normal mode - `U`: Patch requires upgrade mode |
| `ACTION` | `VARCHAR2(15)` | `NOT NULL` | `APPLY` or `ROLLBACK` |
| `STATUS` | `VARCHAR2(15)` |  | Possible values:  - `SUCCESS`: Patch application has completed with no errors - `WITH ERRORS`: Patch application finished with errors |
| `INSTALL_ID` | `NUMBER` |  | Unique numeric identifier for this datapatch session. All patches installed in the same invocation of datapatch will have the same value for `INSTALL_ID`.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `ACTION_TIME` | `TIMESTAMP(6)` | `NOT NULL` | Timestamp when the install was performed |
| `DESCRIPTION` | `VARCHAR2(100)` |  | Description of this patch from OPatch metadata |
| `BUNDLE_SERIES` | `VARCHAR2(30)` |  | If a bundle patch, the series (for example, PSU or DBBP) |
| `BUNDLE_ID` | `NUMBER` |  | If a bundle patch, ID in the series |
| `BUNDLE_DATA` | `XMLTYPE` |  | If a bundle patch, the bundledata.xml associated with the patch |
| `PATCH_DESCRIPTOR` | `XMLTYPE` |  | Contents of the XML descriptor for the patch  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `PATCH_DIRECTORY` | `BLOB` |  | Contents of the patch directory under ORACLE\_HOME/sqlpatch  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `LOGFILE` | `VARCHAR2(500)` |  | Location of the logfile for this apply or rollback attempt |

See Also:

- [Oracle OPatch User's Guide for Windows and UNIX](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=OPTCH106) for more information about OPatch and related patching utilities
- My Oracle Support note 1585822.1 "Datapatch: Database 12c Post Patch SQL Automation” at the following URL for more information about datapatch:
	[https://support.oracle.com/rs?type=doc&id=1585822.1](https://support.oracle.com/rs?type=doc&id=1585822.1)
---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_REGISTRY_SQLPATCH.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.285 DBA\_REGISTRY\_SQLPATCH

`DBA_REGISTRY_SQLPATCH` contains information about the SQL patches that have been installed in the database.

A SQL patch is a patch that contains SQL scripts which need to be run after OPatch completes. `DBA_REGISTRY_SQLPATCH` is updated by the datapatch utility. Each row contains information about an installation attempt (apply or roll back) for a given patch.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INSTALL_ID` | `NUMBER` | `NOT NULL` | Unique numeric identifier for this datapatch session. All patches installed in the same invocation of datapatch will have the same value for `INSTALL_ID`. |
| `PATCH_ID` | `NUMBER` | `NOT NULL` | ID associated with the patch |
| `PATCH_UID` | `NUMBER` | `NOT NULL` | UPI (Universal Patch ID) associated with the patch |
| `PATCH_TYPE` | `VARCHAR2(10)` | `NOT NULL` | Type of the patch. Possible values:  - `INTERIM`: Interim patch - `RU`: Release Update - `RUI`: Release Update Increment - `RUR`: Release Update Revision - `CU`: Cumulative Update |
| `ACTION` | `VARCHAR2(15)` | `NOT NULL` | `APPLY` or `ROLLBACK` |
| `STATUS` | `VARCHAR2(25)` | `NOT NULL` | Possible values:  - `SUCCESS`: Patch application has completed with no errors - `WITH ERRORS`: Patch application finished with errors |
| `ACTION_TIME` | `TIMESTAMP(6)` | `NOT NULL` | Timestamp when the install was performed |
| `DESCRIPTION` | `VARCHAR2(100)` |  | Description of this patch from OPatch metadata |
| `LOGFILE` | `VARCHAR2(500)` | `NOT NULL` | Location of the logfile for this apply or rollback attempt |
| `RU_LOGFILE` | `VARCHAR2(500)` |  | Logfile location for RU specific commands |
| `FLAGS` | `VARCHAR2(10)` |  | One or more of the following:  - `J`: Patch is a JVM patch - `M`: Patch installation was merged with another patch - `N`: Patch requires normal mode - `R`: Patch installation has been retried - `U`: Patch requires upgrade mode |
| `PATCH_DESCRIPTOR` | `XMLTYPE` |  | Contents of the XML descriptor for the patch |
| `PATCH_DIRECTORY` | `BLOB` |  | Contents of the patch directory under ORACLE\_HOME/sqlpatch |
| `SOURCE_VERSION` | `VARCHAR2(15)` |  | 5 digit version (for example, 18.3.2.0.0) for the version on which the patch was applied |
| `SOURCE_BUILD_DESCRIPTION` | `VARCHAR2(80)` |  | Build description (for example, Release\_Update or Release\_Update\_Revision) for the version on which the patch was applied |
| `SOURCE_BUILD_TIMESTAMP` | `TIMESTAMP(6)` |  | Build timestamp for the version on which the patch was applied |
| `TARGET_VERSION` | `VARCHAR2(15)` |  | 5 digit version (for example, 18.4.0.0.0) for the version to be installed |
| `TARGET_BUILD_DESCRIPTION` | `VARCHAR2(80)` |  | Build description (for example, Release\_Update or Release\_Update\_Revision) for the version to be installed |
| `TARGET_BUILD_TIMESTAMP` | `TIMESTAMP(6)` |  | Build timestamp for the version to be installed |

See Also:

- [Oracle OPatch User's Guide for Windows and UNIX](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OPTCH106) for more information about OPatch and related patching utilities
- My Oracle Support note KB148594 "Datapatch: Database 12c Post Patch SQL Automation” at the following URL for more information about datapatch:
	[https://support.oracle.com/support/?documentId=KB148594](https://support.oracle.com/support/?documentId=KB148594)
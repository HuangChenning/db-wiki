---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_PROFILES.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.255 DBA\_PROFILES

`DBA_PROFILES` displays all profiles and their limits.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PROFILE` | `VARCHAR2(128)` | `NOT NULL` | Profile name |
| `RESOURCE_NAME` | `VARCHAR2(32)` | `NOT NULL` | Resource name |
| `RESOURCE_TYPE` | `VARCHAR2(8)` |  | Indicates whether the resource profile is a `KERNEL` or a `PASSWORD` parameter |
| `LIMIT` | `VARCHAR2(128)` |  | Limit placed on this resource for the profile |
| `COMMON` | `VARCHAR2(3)` |  | Indicates whether the profile is common. Possible values:  - `YES` if a profile is common - `NO` if a profile is local (not common) |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the profile definition was inherited from another container (`YES`) or not (`NO`) |
| `IMPLICIT` | `VARCHAR2(3)` |  | Indicates whether the profile was created by an implicit application (`YES`) or not (`NO`) |
| `ORACLE_MAINTAINED` <sup>Foot 1</sup> | `VARCHAR2(3)` |  | Indicates whether the profile was created by Oracle-supplied scripts (`YES`) or not (`NO`)  Note that a profile created by Oracle-supplied scripts is local to all PDBs and can be changed inside a PDB to accommodate individual application requirements. |
| `MANDATORY` <sup>Foot 1</sup> | `VARCHAR2(3)` |  | Indicates whether the profile is a mandatory user profile (`YES`) or not (`NO`)  See Also: The [MANDATORY\_USER\_PROFILE](MANDATORY_USER_PROFILE.md) initialization parameter |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.
---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_PROFILES.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_PROFILES` displays all profiles and their limits.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PROFILE` | `VARCHAR2(128)` | `NOT NULL` | Profile name |
| `RESOURCE_NAME` | `VARCHAR2(32)` | `NOT NULL` | Resource name |
| `RESOURCE_TYPE` | `VARCHAR2(8)` |  | Indicates whether the resource profile is a `KERNEL` or a `PASSWORD` parameter |
| `LIMIT` | `VARCHAR2(128)` |  | Limit placed on this resource for this profile |
| `COMMON` | `VARCHAR2(3)` |  | Indicates whether a given profile is common. Possible values:  - `YES` if a profile is common - `NO` if a profile is local (not common) |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the profile definition was inherited from another container (`YES`) or not (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `IMPLICIT` | `VARCHAR2(3)` |  | Indicates whether this profile was created by an implicit application (`YES`) or not (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
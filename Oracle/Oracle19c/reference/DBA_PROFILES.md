---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_PROFILES.html
tags:
  - oracle
  - 19c
  - reference
---

## 5.254 DBA\_PROFILES

`DBA_PROFILES` displays all profiles and their limits.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PROFILE` | `VARCHAR2(128)` | `NOT NULL` | Profile name |
| `RESOURCE_NAME` | `VARCHAR2(32)` | `NOT NULL` | Resource name |
| `RESOURCE_TYPE` | `VARCHAR2(8)` |  | Indicates whether the resource profile is a `KERNEL` or a `PASSWORD` parameter |
| `LIMIT` | `VARCHAR2(128)` |  | Limit placed on this resource for this profile |
| `COMMON` | `VARCHAR2(3)` |  | Indicates whether a given profile is common. Possible values:  - `YES` if a profile is common - `NO` if a profile is local (not common) |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the profile definition was inherited from another container (`YES`) or not (`NO`) |
| `IMPLICIT` | `VARCHAR2(3)` |  | Indicates whether this profile was created by an implicit application (`YES`) or not (`NO`) |
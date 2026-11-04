---
title: DBA_PROFILES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4187.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_PROFILES` displays all profiles and their limits.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PROFILE` | `VARCHAR2(30)` | `NOT NULL` | Profile name |
| `RESOURCE_NAME` | `VARCHAR2(32)` | `NOT NULL` | Resource name |
| `RESOURCE_TYPE` | `VARCHAR2(8)` |  | Indicates whether the resource profile is a `KERNEL` or a `PASSWORD` parameter |
| `LIMIT` | `VARCHAR2(40)` |  | Limit placed on this resource for this profile |
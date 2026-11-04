---
title: DBA_EPG_DAD_AUTHORIZATION
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3169.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_EPG_DAD_AUTHORIZATION` describes the DADs that are authorized to use different user's privileges.

Related View

`USER_EPG_DAD_AUTHORIZATION` describes the DADs that are authorized to use the user's privileges. This view does not display the `USERNAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DAD_NAME` | `VARCHAR2(64)` | NOT NULL | Name of DAD |
| `USERNAME` | `VARCHAR2(30)` | NOT NULL | Name of the user whose privileges the DAD is authorized to use |
---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SCHEDULER_EXTERNAL_DESTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.42 ALL\_SCHEDULER\_EXTERNAL\_DESTS

`ALL_SCHEDULER_EXTERNAL_DESTS` displays information about the destination objects accessible to the current user pointing to remote agents.

Related View

`DBA_SCHEDULER_EXTERNAL_DESTS` displays information about all destination objects in the database pointing to remote agents.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of this destination object |
| `DESTINATION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of this destination object |
| `HOSTNAME` | `VARCHAR2(256)` |  | Name or IP address of the host on which the agent is located |
| `PORT` | `NUMBER` |  | Port that the agent is listening on |
| `IP_ADDRESS` | `VARCHAR2(64)` |  | IP address of the host on which the agent is located |
| `ENABLED` | `VARCHAR2(5)` |  | Indicates whether this destination object is enabled (`TRUE`) or disabled (`FALSE`) |
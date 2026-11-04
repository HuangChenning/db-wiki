---
title: ALL_SCHEDULER_EXTERNAL_DESTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2036.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_EXTERNAL_DESTS` displays information about the destination objects accessible to the current user pointing to remote agents.

Related View

`DBA_SCHEDULER_EXTERNAL_DESTS` displays information about all destination objects in the database pointing to remote agents.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DESTINATION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of this destination object |
| `HOSTNAME` | `VARCHAR2(256)` |  | Name or IP address of the host on which the agent is located |
| `PORT` | `NUMBER` |  | Port that the agent is listening on |
| `IP_ADDRESS` | `VARCHAR2(64)` |  | IP address of the host on which the agent is located |
| `ENABLED` | `VARCHAR2(5)` |  | Indicates whether this destination object is enabled (`TRUE`) or disabled (`FALSE`) |
| `COMMENTS` | `VARCHAR2(240)` |  | Optional comment |

See Also:

["DBA\_SCHEDULER\_EXTERNAL\_DESTS"](statviews_4240.md)
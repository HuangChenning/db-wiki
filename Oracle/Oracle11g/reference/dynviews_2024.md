---
title: "V$LICENSE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2024.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LICENSE` displays information about license limits.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSIONS_MAX` | `NUMBER` | Maximum number of concurrent user sessions allowed for the instance |
| `SESSIONS_WARNING` | `NUMBER` | Warning limit for concurrent user sessions for the instance |
| `SESSIONS_CURRENT` | `NUMBER` | Current number of concurrent user sessions |
| `SESSIONS_HIGHWATER` | `NUMBER` | Highest number of concurrent user sessions since the instance started |
| `USERS_MAX` | `NUMBER` | Maximum number of named users allowed for the database |
| `CPU_COUNT_CURRENT` | `NUMBER` | Current number of logical CPUs or processors on the system |
| `CPU_CORE_COUNT_CURRENT` | `NUMBER` | Current number of CPU cores on the system (includes subcores of multicore CPUs, as well as single-core CPUs) |
| `CPU_SOCKET_COUNT_CURRENT` | `NUMBER` | Current number of CPU sockets on the system (represents an absolute count of CPU chips on the system, regardless of multithreading or multicore architectures) |
| `CPU_COUNT_HIGHWATER` | `NUMBER` | Highest number of logical CPUs or processors on the system since the instance started |
| `CPU_CORE_COUNT_HIGHWATER` | `NUMBER` | Highest number of CPU cores on the system since the instance started (includes subcores of multicore CPUs, as well as single-core CPUs) |
| `CPU_SOCKET_COUNT_HIGHWATER` | `NUMBER` | Highest number of CPU sockets on the system since the instance started (represents an absolute count of CPU chips on the system, regardless of multithreading or multicore architectures) |

Note:

The availability of the CPU core count and CPU socket count statistics is subject to the operating system platform on which the Oracle Database is running. If a statistic is unavailable, the view will return NULL for the statistic value.
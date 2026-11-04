---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LICENSE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.38 V$LICENSE

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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

The availability of the CPU core count and CPU socket count statistics is subject to the operating system platform on which the Oracle Database is running. If a statistic is unavailable, the view will return NULL for the statistic value.
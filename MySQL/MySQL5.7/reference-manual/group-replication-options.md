---
title: "17.7 Group Replication Variables"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/group-replication-options.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

The next two sections contain information about MySQL server system and server status variables which are specific to the Group Replication plugin.

**Table 17.4 Group Replication Variable and Option Summary**

| Name | Cmd-Line | Option File | System Var | Status Var | Var Scope | Dynamic |
| --- | --- | --- | --- | --- | --- | --- |
| [group\_replication\_allow\_local\_disjoint\_gtids\_join](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_allow\_local\_lower\_version\_join](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_auto\_increment\_increment](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_bootstrap\_group](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_components\_stop\_timeout](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_compression\_threshold](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_enforce\_update\_everywhere\_checks](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_exit\_state\_action](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_flow\_control\_applier\_threshold](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_flow\_control\_certifier\_threshold](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_flow\_control\_mode](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_force\_members](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_group\_name](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_group\_seeds](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_gtid\_assignment\_block\_size](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_ip\_whitelist](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_local\_address](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_member\_weight](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_poll\_spin\_loops](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_primary\_member](server-status-variables.md) |  |  |  | Yes | Global | No |
| [group\_replication\_recovery\_complete\_at](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_recovery\_reconnect\_interval](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_recovery\_retry\_count](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_recovery\_ssl\_ca](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_recovery\_ssl\_capath](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_recovery\_ssl\_cert](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_recovery\_ssl\_cipher](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_recovery\_ssl\_crl](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_recovery\_ssl\_crlpath](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_recovery\_ssl\_key](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_recovery\_ssl\_verify\_server\_cert](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_recovery\_use\_ssl](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_single\_primary\_mode](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_ssl\_mode](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_start\_on\_boot](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_transaction\_size\_limit](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_unreachable\_majority\_timeout](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
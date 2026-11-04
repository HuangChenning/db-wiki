---
title: "20.9 Group Replication Variables"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/group-replication-options.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

The next two sections contain information about MySQL server system and server status variables which are specific to the Group Replication plugin.

**Table 20.4 Group Replication Variable and Option Summary**

| Name | Cmd-Line | Option File | System Var | Status Var | Var Scope | Dynamic |
| --- | --- | --- | --- | --- | --- | --- |
| [Gr\_all\_consensus\_proposals\_count](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_all\_consensus\_time\_sum](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_certification\_garbage\_collector\_count](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_certification\_garbage\_collector\_time\_sum](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_consensus\_bytes\_received\_sum](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_consensus\_bytes\_sent\_sum](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_control\_messages\_sent\_bytes\_sum](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_control\_messages\_sent\_count](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_control\_messages\_sent\_roundtrip\_time\_sum](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_data\_messages\_sent\_bytes\_sum](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_data\_messages\_sent\_count](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_data\_messages\_sent\_roundtrip\_time\_sum](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_empty\_consensus\_proposals\_count](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_extended\_consensus\_count](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| Gr\_flow\_control\_throttle\_active\_count |  |  |  | Yes | Global | No |
| Gr\_flow\_control\_throttle\_count |  |  |  | Yes | Global | No |
| Gr\_flow\_control\_throttle\_last\_throttle\_timestamp |  |  |  | Yes | Global | No |
| Gr\_flow\_control\_throttle\_time\_sum |  |  |  | Yes | Global | No |
| [Gr\_last\_consensus\_end\_timestamp](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_total\_messages\_sent\_count](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_transactions\_consistency\_after\_sync\_count](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_transactions\_consistency\_after\_sync\_time\_sum](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_transactions\_consistency\_after\_termination\_count](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_transactions\_consistency\_after\_termination\_time\_sum](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_transactions\_consistency\_before\_begin\_count](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [Gr\_transactions\_consistency\_before\_begin\_time\_sum](group-replication-status-variables.md) |  |  |  | Yes | Both | No |
| [group\_replication\_advertise\_recovery\_endpoints](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_allow\_local\_lower\_version\_join](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_auto\_increment\_increment](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_autorejoin\_tries](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_bootstrap\_group](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_clone\_threshold](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_communication\_debug\_options](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_communication\_max\_message\_size](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_communication\_stack](group-replication-system-variables.md) |  |  | Yes |  | Global | Yes |
| [group\_replication\_components\_stop\_timeout](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_compression\_threshold](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_consistency](group-replication-system-variables.md) | Yes | Yes | Yes |  | Both | Yes |
| [group\_replication\_enforce\_update\_everywhere\_checks](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_exit\_state\_action](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_flow\_control\_applier\_threshold](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_flow\_control\_certifier\_threshold](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_flow\_control\_hold\_percent](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_flow\_control\_max\_quota](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_flow\_control\_member\_quota\_percent](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_flow\_control\_min\_quota](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_flow\_control\_min\_recovery\_quota](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_flow\_control\_mode](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_flow\_control\_period](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_flow\_control\_release\_percent](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_force\_members](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_group\_name](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_group\_seeds](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_gtid\_assignment\_block\_size](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_ip\_allowlist](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_local\_address](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_member\_expel\_timeout](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_member\_weight](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_message\_cache\_size](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_paxos\_single\_leader](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_poll\_spin\_loops](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_preemptive\_garbage\_collection](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_preemptive\_garbage\_collection\_rows\_threshold](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_recovery\_get\_public\_key](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_recovery\_public\_key\_path](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
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
| [group\_replication\_recovery\_tls\_ciphersuites](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_recovery\_tls\_version](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_recovery\_use\_ssl](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_single\_primary\_mode](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_ssl\_mode](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_start\_on\_boot](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_transaction\_size\_limit](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_unreachable\_majority\_timeout](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [group\_replication\_view\_change\_uuid](group-replication-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
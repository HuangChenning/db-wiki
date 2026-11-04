---
title: "17.4.1 Group Replication Server States"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/group-replication-server-states.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 17.4.1 Group Replication Server States

There are various states that a server instance can be in. If servers are communicating properly, all report the same states for all servers. However, if there is a network partition, or a server leaves the group, then different information could be reported, depending on which server is queried. If the server has left the group then it cannot report updated information about the other servers' states. If there is a partition, such that quorum is lost, servers are not able to coordinate between themselves. As a consequence, they cannot guess what the status of different servers is. Therefore, instead of guessing their state they report that some servers are unreachable.

**Table 17.1 Server State**

| Field | Description | Group Synchronized |
| --- | --- | --- |
| `ONLINE` | The member is ready to serve as a fully functional group member, meaning that the client can connect and start executing transactions. | Yes |
| `RECOVERING` | The member is in the process of becoming an active member of the group and is currently going through the recovery process, receiving state information from a donor. | No |
| `OFFLINE` | The plugin is loaded but the member does not belong to any group. | No |
| `ERROR` | The state of the member. Whenever there is an error on the recovery phase or while applying changes, the server enters this state. | No |
| `UNREACHABLE` | Whenever the local failure detector suspects that a given server is not reachable, because for example it was disconnected involuntarily, it shows that server's state as `UNREACHABLE`. | No |

Important

Once an instance enters `ERROR` state, the [`super_read_only`](server-system-variables.md) option is set to `ON`. To leave the `ERROR` state you must manually configure the instance with [`super_read_only=OFF`](server-system-variables.md).

Note that Group Replication is *not* synchronous, but eventually synchronous. More precisely, transactions are delivered to all group members in the same order, but their execution is not synchronized, meaning that after a transaction is accepted to be committed, each member commits at its own pace.
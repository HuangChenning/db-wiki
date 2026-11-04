---
title: "17.9.4 Data Definition Statements"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/group-replication-data-definition-statements.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 17.9.4 Data Definition Statements

In a Group Replication topology, care needs to be taken when executing data definition statements also commonly known as data definition language (DDL). Given that MySQL does not support atomic or transactional DDL, one cannot optimistically execute DDL statements and later roll back if needs be. Consequently, the lack of atomicity does not fit directly into the optimistic replication paradigm that Group Replication is based on.

Therefore, more care needs to be taken when replicating data definition statements. Schema changes and changes to the data that the object contains need to be handled through the same server while the schema operation has not yet completed and replicated everywhere. Failure to do so can result in data inconsistency.

Note

If the group is deployed in single-primary mode, then this is not a problem, because all changes are performed through the same server, the primary.

Warning

MySQL DDL execution is not atomic or transactional. The server executes and commits without securing group agreement first. As such, you must route DDL and DML for the same object through the same server, while the DDL is executing and has not replicated everywhere yet.
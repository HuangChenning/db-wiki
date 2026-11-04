---
title: "19.2.2 Starting MySQL Shell"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/installing-mysql-shell-starting.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 19.2.2 Starting MySQL Shell

You need an account name and password to establish a session using MySQL Shell. Replace *`user`* with your account name.

On the same system where the server instance is running, open a terminal window (command prompt on Windows) and start MySQL Shell with the following command:

```
mysqlsh --uri user@localhost
```

You are prompted to input your password and then this establishes an X Session.

For instructions to get you started using MySQL as a document store, see the following quick-start guides:
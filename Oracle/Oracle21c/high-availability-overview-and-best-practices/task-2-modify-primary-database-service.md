---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-2-modify-primary-database-service.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 2: Modify the Primary Database Service

On the primary database server, modify the existing database service that was created as part of the original Oracle GoldenGate on Oracle RAC configuration.

Set the service role to `PRIMARY`, so that the service is only be started when the database becomes the Data Guard primary database role after a role transition.

As the `oracle` user, modify the service using the following command:

```
$ srvctl modify service -db dbName -service service_name
 -role PRIMARY
```

If your database is part of a multitenant environment, remember to modify both the multitenant container database (CDB) and pluggable database (PDB) services.
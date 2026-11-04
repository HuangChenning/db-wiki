---
title: "2.11.5 Downgrade Troubleshooting"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/downgrade-troubleshooting.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 2.11.5 Downgrade Troubleshooting

If you downgrade from one release series to another, there may be incompatibilities in table storage formats. In this case, use [**mysqldump**](mysqldump.md) to dump your tables before downgrading. After downgrading, reload the dump file using [**mysql**](mysql.md) or [**mysqlimport**](mysqlimport.md) to re-create your tables. For examples, see [Section 2.10.13, “Copying MySQL Databases to Another Machine”](copying-databases.md).

A typical symptom of a downward-incompatible table format change when you downgrade is that you cannot open tables. In that case, use the following procedure:

1. Stop the older MySQL server that you are downgrading to.
2. Restart the newer MySQL server you are downgrading from.
3. Dump any tables that were inaccessible to the older server by using [**mysqldump**](mysqldump.md) to create a dump file.
4. Stop the newer MySQL server and restart the older one.
5. Reload the dump file into the older server. Your tables should be accessible.
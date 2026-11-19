---
title: "查询分区名称"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077187.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 查询分区名称

已知表的 `table_id` 时，可以通过视图 `CDB_OB_TABLE_LOCATIONS`（系统租户）或 `DBA_OB_TABLE_LOCATIONS`（用户租户）查询表中所有分区的分区名称。

- 系统租户

  系统租户下，可以通过以下语句进行查询。

  ```
  obclient> SELECT * FROM oceanbase.CDB_OB_TABLE_LOCATIONS WHERE TENANT_ID=tenant_id AND TABLE_ID=table_id;  
  ```

- 用户租户

  MySQL 模式的用户租户下，可以通过以下语句进行查询。

  ```
  obclient> SELECT * FROM oceanbase.DBA_OB_TABLE_LOCATIONS WHERE TABLE_ID=table_id; 
  ```

  Oracle 模式的用户租户下，可以通过以下语句进行查询。

  ```
  obclient> SELECT * FROM SYS.DBA_OB_TABLE_LOCATIONS WHERE TABLE_ID=table_id; 
  ```

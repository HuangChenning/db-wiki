---
title: "查找某个租户中执行全表扫描的 SQL"
book: "性能调优"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005687660.html"
tags:
  - oceanbase
  - distributed
  - ref-performance-tuning-guide
---

# 查找某个租户中执行全表扫描的 SQL

运行如下语句可以查询某个租户中执行全表扫描的 SQL：

```javascript
obclient> SELECT query_sql 
      FROM oceanbase.GV$OB_SQL_AUDIT 
      WHERE table_scan = 1 AND tenant_id = 1001 
      GROUP BY sql_id;

+-------------------------------+
| query_sql                     |
+-------------------------------+
| SHOW VARIABLES LIKE 'version' |
+-------------------------------+
```

---
title: "检查租户资源使用状态"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701789.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 检查租户资源使用状态

您可以通过 SQL 命令的方式来检查租户资源使用状态。

语句如下：

``` sql
obclient> SELECT t1.tenant_name,concat(svr_ip,":",svr_port) as "unit_server",t3.max_cpu,t3.min_cpu  FROM OCEANBASE.DBA_OB_TENANTS t1,OCEANBASE.DBA_OB_UNITS t2,OCEANBASE.DBA_OB_UNIT_CONFIGS t3,OCEANBASE.DBA_OB_RESOURCE_POOLS t4
where t1.tenant_id = t4.tenant_id
AND t4.resource_pool_id=t2.resource_pool_id 
AND t4.unit_config_id=t3.unit_config_id
ORDER BY t1.tenant_name;

+----------------+---------------------+---------+---------+
| tenant_name    | unit_server         | max_cpu | min_cpu |
+----------------+---------------------+---------+---------+
| mysql          | xxx.xx.xxx.193:2882 |       2 |       2 |
| oracle001      | xxx.xx.xxx.193:2882 |       1 |       1 |
| standby_tenant | xxx.xx.xxx.193:2882 |       1 |       1 |
| sys            | xxx.xx.xxx.193:2882 |       3 |       3 |
| test           | xxx.xx.xxx.193:2882 |       1 |       1 |
+----------------+---------------------+---------+---------+
```

字段说明如下。

| 字段        | 说明                              |
|-------------|-----------------------------------|
| tenant_name | 租户名                            |
| unit_server | 租户 Unit 所在的 OBServer         |
| max_cpu     | 租户 Unit 允许使用的最大 CPU 核数 |
| min_cpu     | 租户 Unit 至少可使用的 CPU 核数   |

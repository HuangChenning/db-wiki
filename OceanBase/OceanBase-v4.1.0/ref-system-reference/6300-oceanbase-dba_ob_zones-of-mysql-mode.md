---
title: oceanbase.DBA_OB_ZONES
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699275.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# oceanbase.DBA_OB_ZONES

oceanbase.DBA_OB_ZONES 
===========================================


功能 
--------------------

展示所有 Zone 的信息。

字段说明 
----------------------



|  字段名称  |      类型       | 是否可以为 NULL |        描述         |
|--------|---------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ZONE   | varchar(128)  | NO         | Zone 名称           |
| CREATE_TIME | timestamp(6)  | NO    | Zone 的创建时间     |
| MODIFY_TIME | timestamp(6)  | NO    | Zone 的修改时间    |
| STATUS | varchar(4096) | NO         | Zone 的状态 <li> `ACTIVE`：当前是活跃状态，正常提供服务   <li> `INACTIVE`：Zone 处于 stop 状态    |
| IDC    | varchar(4096) | NO         | Zone 所属的 IDC 信息   |
| REGION | varchar(4096) | NO         | Zone 所属的 Region 信息|
| TYPE   | varchar(4096) | NO         | Zone 的类型 <li> `ReadWrite`：读写 Zone   <li> `Encryption`：加密 Zone              |

---
title: "运维指导类 目录"
book: "运维指导类"
version: "V4.5"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
  - contents
---

# 运维指导类

按原站点顺序排列。路径相对于本目录。

- [1、 判断流复制主备角色的方法](judge_standby.md)
- [2、HGDB如何提升批量导入数据的速度](HGDB_speed.md)
- [3、HG数据库恢复表中被删除的列](recover_colum.md)
- [4、HighGo Database删除表中的重复数据](delete_repeat.md)
- [5、查看正在在运行的瀚高数据库服务的启动方式：是由systemd(systemctl)启动的，还是由pg_ctl启动的](running.md)
- [6、查询瀚高数据库的创建时间](create_time.md)
- [7、瀚高数据库修改用户密码及有效期](validity.md)
- [8、简单方便的获取所有表的条数](eazy_count.md)
- [9、禁用表的触发器以及外键约束](trigger_disabled.md)
- [10、如何处理表或索引的膨胀](expand.md)
- [11、如何创建大写的表名](big_tablename.md)
- [12、如何开关数据库告警日志及修改日志级别](alarm.md)
- [13、如何使用BenchmarkSQL工具测试HGDB](BenchmarkSQL.md)
- [14、数据库服务是否运行及运行状态的检查方法](running_check.md)
- [15、在HGDB中生成连续时间数据](continuous_data.md)
- [16、HGDB如何查询慢SQL](slow_sql.md)
- [17、pg_relation_size,pg_table_size,pg_indexes_size,pg_total_relation_size之间的关系](pg_relation.md)
- [18、pg_resetwal 使用简介](pg_resetwal.md)
- [19、Postgresql TOAST简介](Postgresql_TOAST.md)
- [20、Postgresql共享库预加载(Shared Library Preloading)](Shared_Library.md)
- [21、逻辑导入导出(pg_dumppg_restore)-导入到不同的schema或tablespace](pg_dumppg_restore.md)
- [22、密码文件的格式和使用](password_use.md)
- [23、再谈mvcc与vacuum](again_mvcc.md)
- [24、查看数据库占用磁盘空间的方法](view_disk.md)
- [25、HAC集群修改为单机](HAC_alone.md)
- [26、HAC集群更改IP（单节点更改、全部节点更改）](HAC_ip.md)
- [27、HAC集群启停步骤](HAC_stop.md)
- [28、HAC集群添加新节点](HAC_add.md)
- [29、流复制运维实践](HAC_copy.md)

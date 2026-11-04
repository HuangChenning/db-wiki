---
title: "17、pg_relation_size,pg_table_size,pg_indexes_size,pg_total_relation_size之间的关系"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/pg_relation.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## pg\_relation\_size,pg\_table\_size,pg\_indexes\_size,pg\_total\_relation\_size之间的关系

先通过一个例子来直观的展现一下他们的区别和联系。

存在一张带索引的表t，OID为16384，与该表相关联的TOAST表的OID为16387。

```
select pg_relation_size(16384) ,
pg_relation_size(16384, 'main') as main,
pg_relation_size(16384, 'fsm') as fsm,
pg_relation_size(16384, 'vm') as vm,
pg_relation_size(16384, 'init') as init,
pg_total_relation_size(16387) as toast,
pg_table_size(16384), 
pg_indexes_size(16384),
pg_total_relation_size(16384);
```

| pg\_relation\_size | main | fsm | vm | init | toast | pg\_table\_size | pg\_indexes\_size | pg\_total\_relation\_size |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 106496 | 106496 | 24576 | 8192 | 0 | 4186112 | 4325376 | 114688 | 4440064 |

pg\_relation\_size不加参数，默认就是查的表的数据文件大小，单位字节。

pg\_relation\_size加参数main，也是查的表的数据文件大小，单位字节。

pg\_relation\_size加参数fsm，查的表的fsm文件大小，单位字节。

pg\_relation\_size加参数vm，查的表的vm文件大小，单位字节。

pg\_relation\_size加参数init，查的表的init文件大小，单位字节。

pg\_table\_size，查的表的数据文件，fsm文件，vm文件，init文件，toast表的总大小，单位字节。

pg\_indexes\_size，查的表上索引文件的大小，单位字节。

pg\_total\_relation\_size查询的是表的总大小，也就是表的数据文件，fsm文件，vm文件，init文件，索引文件，toast表的总大小，单位字节。
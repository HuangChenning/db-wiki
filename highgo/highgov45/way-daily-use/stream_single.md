---
title: "9、流复制改单机的注意事项"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/stream_single.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## 流复制改单机的注意事项

## 1、确认当前流复制状态

```
select * from pg_stat_replication();
```

确认现有流复制有多少备节点及是否为同步流复制或异步流复制

## 2、确认是否使用复制槽

```
select * from  pg_replication_slots();
```

## 3、如采用的是同步流复制，更改主库流复制相关参数

```
vi  $PGDATA/postgresql.auto.conf
将synchronous_standby_names参数注释掉，如synchronous_commit参数配置的为非on值，则将起更改为on
```

## 4、如使用了复制槽，主库需手动将复制槽进行删除

```
select * from pg_drop_replication_slot('复制槽名');
```

## 5、备库更改流复制相关参数

```
vi  $PGDATA/postgresql.auto.conf
```

将primary\_conninfo及primary\_slot\_name参数注释

## 6、备库将standby.signal文件改名

```
mv  $PGDATA/standby.signal  $PGDATA/standby.signal-bak
```

## 7、重启各数据库节点

```
pg_ctl restart
```
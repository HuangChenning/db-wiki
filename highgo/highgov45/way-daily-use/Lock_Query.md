---
title: "10、锁查询及处理"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/Lock_Query.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## 锁查询及处理

## 1、查看锁等待

### 方法一

```
SELECT
lock2.pid as locking_pid,
lock1.pid as locked_pid,
stat1.usename as locked_user,
stat1.query as locked_statement,
stat1.state as state,
stat2.query as locking_statement,
stat2.state as state,
now() - stat1.query_start as locking_duration,
stat2.usename as locking_user
FROM pg_catalog.pg_locks lock1
JOIN pg_catalog.pg_stat_activity stat1 on lock1.pid = stat1.pid
JOIN pg_catalog.pg_locks lock2 on
(lock1.locktype,lock1.database,lock1.relation,
lock1.page,lock1.tuple,lock1.virtualxid,
lock1.transactionid,lock1.classid,lock1.objid,
lock1.objsubid) IS NOT DISTINCT FROM
(lock2.locktype,lock2.DATABASE,
lock2.relation,lock2.page,
lock2.tuple,lock2.virtualxid,
lock2.transactionid,lock2.classid,
lock2.objid,lock2.objsubid)
JOIN pg_catalog.pg_stat_activity stat2 on lock2.pid
= stat2.pid
WHERE NOT lock1.granted AND lock2.granted;

 locking_pid | locked_pid | locked_user |     locked_statement     | state |     locking_statement     |    state    | locking_d
uration | locking_user
-------------+------------+-------------+------------------------------------+--------+------------------------------------+---------------------+----------

--------+--------------
    2176 |    2614 | pg106    | update a set col1=666 where aid=1; | active | update a set col1=555 where aid=1; | idle in transaction | 00:52:54.
146781 | pg106
(1 row)
```

显示

locking，锁持有者相关信息

locked，被阻塞者相关信息

### 方法二

```
with
t_wait as
(
select a.mode,a.locktype,a.database,a.relation,a.page,a.tuple,a.classid,a.granted,
a.objid,a.objsubid,a.pid,a.virtualtransaction,a.virtualxid,a.transactionid,a.fastpath,
b.state,b.query,b.xact_start,b.query_start,b.usename,b.datname,b.client_addr,b.client_port,b.application_name
from pg_locks a,pg_stat_activity b where a.pid=b.pid and not a.granted
),
t_run as
(
select a.mode,a.locktype,a.database,a.relation,a.page,a.tuple,a.classid,a.granted,
a.objid,a.objsubid,a.pid,a.virtualtransaction,a.virtualxid,a.transactionid,a.fastpath,
b.state,b.query,b.xact_start,b.query_start,b.usename,b.datname,b.client_addr,b.client_port,b.application_name
from pg_locks a,pg_stat_activity b where a.pid=b.pid and a.granted
),
t_overlap as
(
select r.* from t_wait w join t_run r on
(
r.locktype is not distinct from w.locktype and
r.database is not distinct from w.database and
r.relation is not distinct from w.relation and
r.page is not distinct from w.page and
r.tuple is not distinct from w.tuple and
r.virtualxid is not distinct from w.virtualxid and
r.transactionid is not distinct from w.transactionid and
r.classid is not distinct from w.classid and
r.objid is not distinct from w.objid and
r.objsubid is not distinct from w.objsubid and
r.pid <> w.pid
)
),
t_unionall as
(
select r.* from t_overlap r
union all
select w.* from t_wait w
)

select locktype,datname,relation::regclass,page,tuple,virtualxid,transactionid::text,classid::regclass,objid,objsubid,
string_agg(
'Pid: '||case when pid is null then 'NULL' else pid::text end||chr(10)||

'Lock_Granted: '||case when granted is null then 'NULL' else granted::text end||' , Mode: '||case when mode is null then 'NULL' else mode::text end||' , FastPath: '||case when fastpath is null then 'NULL' else fastpath::text end||' , VirtualTransaction: '||case when virtualtransaction is null then 'NULL' else virtualtransaction::text end||' , Session_State: '||case when state is null then 'NULL' else state::text end||chr(10)||

'Username: '||case when usename is null then 'NULL' else usename::text end||' , Database: '||case when datname is null then 'NULL' else datname::text end||' , Client_Addr: '||case when client_addr is null then 'NULL' else client_addr::text end||' , Client_Port: '||case when client_port is null then 'NULL' else client_port::text end||' , Application_Name: '||case when application_name is null then 'NULL' else application_name::text end||chr(10)||

'Xact_Start: '||case when xact_start is null then 'NULL' else xact_start::text end||' , Query_Start: '||case when query_start is null then 'NULL' else query_start::text end||' , Xact_Elapse: '||case when (now()-xact_start) is null then 'NULL' else (now()-xact_start)::text end||' , Query_Elapse: '||case when (now()-query_start) is null then 'NULL' else (now()-query_start)::text end||chr(10)||

'SQL (Current SQL in Transaction): '||chr(10)||
case when query is null then 'NULL' else query::text end,
chr(10)||'--------'||chr(10)
order by
( case mode
when 'INVALID' then 0
when 'AccessShareLock' then 1
when 'RowShareLock' then 2
when 'RowExclusiveLock' then 3
when 'ShareUpdateExclusiveLock' then 4
when 'ShareLock' then 5
when 'ShareRowExclusiveLock' then 6
when 'ExclusiveLock' then 7
when 'AccessExclusiveLock' then 8
else 0
end ) desc,
(case when granted then 0 else 1 end)
) as lock_conflict
from t_unionall
group by
locktype,datname,relation,page,tuple,virtualxid,transactionid::text,classid,objid,objsubid;

Pid: 1980
Lock_Granted: false , Mode: AccessExclusiveLock , FastPath: false , VirtualTransaction: 9/4 , Session_State: active
Username: test , Database: postgres , Client_Addr: NULL , Client_Port: -1 , Application_Name: psql
Xact_Start: 2019-02-11 15:35:33.054468+08 , Query_Start: 2019-02-11 15:35:34.283192+08 , Xact_Elapse: 00:01:18.422846 , Query_Elapse: 00:01:17.194122
SQL (Current SQL in Transaction):
truncate table_lock;

--------
Pid: 1894
Lock_Granted: true , Mode: RowExclusiveLock , FastPath: false , VirtualTransaction: 5/128 , Session_State: idle in transaction
Username: test , Database: postgres , Client_Addr: NULL , Client_Port: -1 , Application_Name: psql
Xact_Start: 2019-02-11 15:17:48.342793+08 , Query_Start: 2019-02-11 15:17:48.344543+08 , Xact_Elapse: 00:19:03.134521 , Query_Elapse: 00:19:03.132771
SQL (Current SQL in Transaction):
insert into table_lock values (2,'b');
```
1. 前面的锁查询SQL，已经清晰的显示了每一个发生了锁等待的对象，Lock\_Granted: true阻塞了Lock\_Granted: false
2. 同时按锁的大小排序，第一行的锁最大（Mode: AccessExclusiveLock级别最高）

### 方法三

```
SELECT
  l1.*,
  l2.virtualtransaction,
  l2.pid,
  l2.mode,
  l2.granted
FROM
  pg_locks l1
JOIN
  pg_locks l2 on (
    (
      l1.locktype,
      l1.database,
      l1.relation,
      l1.page,
      l1.tuple,
      l1.virtualxid,
      l1.transactionid,
      l1.classid,
      l1.objid,
      l1.objsubid
    )
  IS NOT DISTINCT FROM
    (
      l2.locktype,
      l2.database,
      l2.relation,
      l2.page,
      l2.tuple,
      l2.virtualxid,
      l2.transactionid,
      l2.classid,
      l2.objid,
      l2.objsubid
    )
  )
WHERE
  NOT l1.granted
AND
  l2.granted;

  locktype  | database | relation | page | tuple | virtualxid | transactionid | classid | objid | objsubid | virtualtransaction | pid |  mode  | gran

ted | fastpath | virtualtransaction | pid |   mode   | granted

---------------+----------+----------+------+-------+------------+---------------+---------+-------+----------+--------------------+------+-----------+-----

----+----------+--------------------+------+---------------+---------
 transactionid |     |     |   |    |      |      614 |     |    |     | 4/49        | 2614 | ShareLock | f

  | f    | 3/14        | 2176 | ExclusiveLock | t
```

显示阻塞者相关信息

## 2、处理方法

确认会话状态为idle状态。会话的类型state in (‘idle’, ‘idle in transaction’, ‘idle in transaction (aborted)’, ‘disabled’)

```
select pid, state from pg_stat_activity where state in ('idle', 'idle in transaction', 'idle in transaction (aborted)', 'disabled');
```

找到会话信息，通知前台用户结束事务操作，或者手动杀死会话

```
SELECT pg_terminate_backend(pid);
```

注意：此处不要使用操作系统命令kill -9, 其会造成所有活动进程被终止，数据库重启。

## 3、死锁等待

```
SESSION A：
  Lock tuple 1;
SESSION B：
  Lock tuple 2;
SESSION A：
  Lock tuple 2 waiting;
SESSION B：
  Lock tuple 1 waiting;
```

A,B相互等待。

死锁检测的时间间隔配置，deadlock\_timeout默认为1秒。

锁等待超过这个配置后，触发死锁检测算法。

因为死锁检测比较耗资源，所以这个时间视情况而定。

规避死锁需要从业务逻辑的角度去规避，避免发生这种交错持锁和交错等待的情况。
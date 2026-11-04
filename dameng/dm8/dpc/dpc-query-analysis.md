---
title: "查询分析"
book: "DM8 分布计算集群"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dpc-query-analysis.html
tags:
  - dameng
  - dm8
  - dpc
---

在执行形态和执行调度上，DMDPC 和 DM MPP 相比差别很大。DMDPC 执行计划中增加了子计划的概念。为此 DMDPC 新增了 V$DPC\_STASK\_THRD 动态视图，来展示每个子任务、每个线程的执行统计信息，便于用户对性能进行分析。

## 10.1 查看子计划

子计划是使用一对 ESEND/ERECV 操作符来划分的。整个执行计划可通过 EXPLAIN 获取，子计划为整体计划中的一部分。

举例：

```
create table M1(c1 int not null, c2 char(1000)) partition by hash(c1)(
 partition p1  storage (on TS_01), 
 partition p2  storage (on TS_02),
 partition p3  storage (on TS_01), 
 partition p4  storage (on TS_02),
 partition p5  storage (on TS_01), 
 partition p6  storage (on TS_02)
) ;
insert into M1 select level, 'aaa' || mod(level, 10) || repeat('x', 20) from dual  connect by level <= 50;
commit;
```

通过 EXPLAIN 命令查看 SQL 语句的整体执行计划，其中就使用到了子计划。

```
Explain select /*+ use_hash(m1, sysobjects) parallel(#1 8) parallel(sysobjects 8) stat(m1 1M) dpc_opt_flag(0) */ count(*) from m1 where c1 in (select mod(id, 10000) from  sysobjects);

1   #NSET2: [171, 1, 4] 
2     #PRJT2: [171, 1, 4]; exp_num(1), is_atom(FALSE); INFO_BITS(0); spl_info(NULL)
3       #AAGR2: [171, 1, 4]; grp_num(0), sfun_num(1), distinct_flag[0]; slave_empty(0)
4         #ERECV: [171, 1, 4]; stask_no(-1), l_stask_no(1), n_key(0), trig(0)
5           #ESEND: [171, 1, 4]; stask_no(1), type(DIRECT), sites(3:8), sql_invoke(0), pwj_opt(0), table(-)
6             #AAGR2: [171, 1, 4]; grp_num(0), sfun_num(1), distinct_flag[0]; slave_empty(0)
7               #HASH RIGHT SEMI JOIN2: [171, 312, 4]; KEY_NUM(1), KEY(DMTEMPVIEW_889193496.colname = exp_cast(M1.C1)), KEY_NULL_EQU(0)
8                 #ERECV: [1, 1284, 4]; stask_no(1), l_stask_no(0), n_key(0), trig(0)
9                   #ESEND: [1, 1284, 4]; stask_no(0), type(N_DEST), sites(0:1), sql_invoke(0), pwj_opt(0), table(-), keys(DMTEMPVIEW_889193496.colname) 
10                    #GI: [1, 1284, 4]; policy(PART_UNIT), gi_unit[0..0], scan_type[0](FULL)
11                      #PRJT2: [1, 1284, 4]; exp_num(1), is_atom(FALSE); INFO_BITS(0); prjt_batch_exec(1); spl_info(NULL)
12                        #SSCN: [1, 1284, 4]; SYSINDEXIDSYSOBJECTS(SYSOBJECTS as SYSOBJECTS); btr_scan(1); is_global(0)
13                #ERECV: [105, 1000000, 4]; stask_no(1), l_stask_no(2), n_key(0), trig(0)
14                  #ESEND: [105, 1000000, 4]; stask_no(2), type(N_DEST), sites(2:3,1:3), sql_invoke(0), pwj_opt(0), table(-), keys(exp_cast(M1.C1)) 
15                    #GI: [105, 1000000, 4]; policy(PART_UNIT), gi_unit[0..0], scan_type[0](FULL)
16                      #CSCN2: [105, 1000000, 4]; INDEX33555523(M1); btr_scan(1); need_slct(0); prejudge_iescn(0)

Predicate Information (identified by operation id):
---------------------------------------------------
7 - access(DMTEMPVIEW_889193496.colname = exp_cast(M1.C1))
```

执行 SQL 语句，得到结果：

```
select /*+ use_hash(m1, sysobjects) xparallel(#1 8) parallel(sysobjects 8) stat(m1 1M)dpc_opt_flag(0)  */ count(*) from m1 where c1 in (select mod(id, 20)+10 from  sysobjects);
//查询结果如下：
行号 COUNT(*)
---------- --------------------
1 20
已用时间: 139.984(毫秒). 执行号:16777624.
```

## 10.2 查看物理计划生成阶段的计划

DM 提供一个展示物理计划生成阶段的计划（包含子计划拆分细节）的存储过程。

**定义：**

```
sp_set_dbg_show (
    mode_name varchar(256),
    v int
)
```

**功能说明：**

开启或者关闭物理计划生成阶段（PHD）的计划展示。

**参数说明：**

mode\_name：阶段的名称，取值 PHD。PHD 表示物理计划生成阶段；

v: 开启或者关闭。1：开启；0：关闭。

**举例说明：**

使用 sp\_set\_dbg\_show('PHD',1)开启 PHD 阶段计划展示。服务器控制台上子任务独立展示如下：

```
===> [PLAN0] 3 stasks, after PHD, info_bits[0x8];  <===
***** trunk stask execute seq: 0->1->2

>>>> #0: data_source: TAB, n_recv:0, SINGLE PARTITION, GI: UNIT, sites_source:SELF, parent stask: #1
9   #ESEND: [1, 1357, 4]; stask_no(0), type(N_DEST), sites(0:1), sql_invoke(0), pwj_opt(0), table(-), keys(DMTEMPVIEW_889193842.colname) 
10    #GI: [1, 1357, 4]; policy(PART_UNIT), gi_unit[0..0], scan_type[0](FULL)
11      #PRJT2: [1, 1357, 4]; exp_num(1), is_atom(FALSE); INFO_BITS(0)
12        #SSCN: [1, 1357, 4]; SYSINDEXIDSYSOBJECTS(SYSOBJECTS as SYSOBJECTS); btr_scan(1); is_global(0)

 MP_RAFT(id=0): workers 1, scan operator 1

>>>> #1: children[#0,#2], data_source: RECV, n_recv:2, SINGLE SITE, GI: UNIT, sites_source:SPs, ROOT task
5   #ESEND: [171, 1, 4]; stask_no(1), type(DIRECT), sites(3:8), sql_invoke(0), pwj_opt(0), table(-)
6     #AAGR2: [171, 1, 4]; grp_num(0), sfun_num(1), distinct_flag[0]; slave_empty(0)
7       #HASH RIGHT SEMI JOIN2: [171, 1413, 4]; n_keys(1) KEY(DMTEMPVIEW_889193842.colname=exp_cast(M1.C1)) KEY_NULL_EQU(0)
8         #ERECV: [1, 1357, 4]; stask_no(1), l_stask_no(0), n_key(0), trig(0)
13        #ERECV: [105, 1000000, 4]; stask_no(1), l_stask_no(2), n_key(0), trig(0)

Predicate Information (identified by operation id):
---------------------------------------------------
7 - access(DMTEMPVIEW_889193842.colname = exp_cast(M1.C1))

SP_26330_1(id=3): workers 8, scan operator 0

>>>> #2: data_source: HP_TAB, n_recv:0, MULTI SITES, GI: UNIT, sites_source:SELF, parent stask: #1
14  #ESEND: [105, 1000000, 4]; stask_no(2), type(N_DEST), sites(1:3,2:3), sql_invoke(0), pwj_opt(0), table(-), keys(exp_cast(M1.C1)) 
15    #GI: [105, 1000000, 4]; policy(PART_UNIT), gi_unit[0..0], scan_type[0](FULL)
16      #CSCN2: [105, 1000000, 4]; INDEX33555594(M1); btr_scan(1); need_slct(0)

  RAFT_1(id=1): workers 3, scan operator 1
  RAFT_2(id=2): workers 3, scan operator 1
```

这种展示方案更贴近于 SQC 实际调度，包括子任务依赖关系，调度的站点和并行度信息一目了然。

也可以通过 DEM 或者 MANAGER 工具进行图形化的计划展示。以 MANAGER 为例，图形化的计划展示如下图所示：

图10.1 通过MANAGER查看执行计划

## 10.3 查看正在执行的语句信息

使用之前需开启监控。监控开启方法是设置 INI 参数 ENABLE\_MONITOR 大于 0。

1. 查看监控是否开启。
```
select SF_GET_PARA_STRING_VALUE(1, 'INSTANCE_NAME') as ins_name,* from
v$dm_ini where para_name = 'ENABLE_MONITOR';
```

如果未开启，可以执行下列语句动态更改。例如：设置 ENABLE\_MONITOR=1。

```
alter system set 'ENABLE_MONITOR'=1 MEMORY;
```
2. 获取正在执行语句的执行号。
	1）通过 V$SESSIONS 找到执行的会话 ID 等信息；
	2）根据上一步会话 ID 信息找到对应的 QC、执行号。如果返回多个 QC 记录，可以加入 is\_over ='N'排除已完成 SQL 或者根据执行号随时间递增的特性来筛选得到正确的执行号。

例 以某个执行时间耗时较长的语句 Q1 为例。

```
//Q1
select /*+ parallel(8) */ count(*) from (select * from j2 x union all select id, pid, id, pid from sys.sysobjects x) t1 join j2 t2 on t1.d2 = t2.d2;
```

用下列查询获取 Q1 执行号。

```
with v_sql_1 as (select sess_id, sess_seq from v$sessions 
    where SQL_TEXT like 'select /*+ parallel(8) */ count(*) from %')
    select x.* from v$dpc_qc_history x,v_sql_1 y where x.sess_id = y.sess_id and x.sess_seq = y.sess_seq;
```

返回的部分结果：

```
EXEC_ID     MPP_EXEC_ID SQC_EXEC_ID    N_STASK     IDU_FLAG N_SITES     N_HTAB      N_SPL       N_DPP    IS_OVER
    12582912       13313984         1               2           -        3           0           0           0     N
```
3. 根据找到的执行号 12582912，在 V$DPC\_STASK\_THRD 视图中获取执行的动态信息，观察某个子任务发送、存储行数的变化。
```
select * from v$dpc_stask_thrd where exec_id = 12582912;
```

其中，V$DPC\_QC\_HISTORY 和 V$DPC\_STASK\_THRD 是在内存中维持特定数量的信息。某些陈旧的已完成记录或者高并发压力下尚未执行完成的记录都存在被淘汰覆盖的可能。
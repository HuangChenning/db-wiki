---
title: "DBMS_WORKLOAD_REPOSITORY 包"
book: "DM8 系统包使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dbms_workload-package.html
tags:
  - dameng
  - dm8
  - system-packages
---

数据库快照是一个只读的静态的数据库。DM 快照功能是基于数据库实现的，每个快照是基于数据库的只读镜像。通过检索快照，可以获取源数据库在快照创建时间点的相关数据信息。

为了方便管理自动工作集负载信息库 AWR（Automatic Workload Repository）的信息，系统为其所有重要统计信息和负载信息执行一次快照，并将这些快照存储在 AWR 中。

用户在使用 DBMS\_WORKLOAD\_REPOSITORY 包之前，需要提前调用系统过程 SP\_INIT\_AWR\_SYS(1)创建包。DM 数据库在创建该包时，默认创建一个名为 SYSAUX 的表空间，对应的数据文件为 SYSAWR.DBF，该表空间用于存储该包生成快照的数据，表空间大小上限为 16GB。如果该包被删除，那么 SYSAUX 表空间也对应地被删除。若包已创建成功，再次执行 SP\_INIT\_AWR\_SYS(1), 不会影响当前已创建的表和数据。

AWR 功能默认是关闭的，如果需要开启，则调用 DBMS\_WORKLOAD\_REPOSITORY.AWR\_SET\_INTERVAL 过程设置快照的间隔时间。DBMS\_WORKLOAD\_REPOSITORY 包还负责 snapshot（快照）的管理。

DM MPP 环境下不支持 DBMS\_WORKLOAD\_REPOSITORY 包。

ASH（Active Session History）数据报表记录当前活动会话的等待信息，对应 V$ACTIVE\_SESSION\_HISTORY。ASH 报表生成时依赖 DBA\_USERS 对象，该对象在数据库创建过程中，会默认随 SP\_CREATE\_SYSTEM\_VIEWS(1)自动创建，若该对象不存在时则会报错。

## 21.1 相关方法

> **注意**
> 
> DBMS\_WORKLOAD\_REPOSITORY包不支持打开ASM文件系统上的路径。  
> DBMS\_WORKLOAD\_REPOSITORY包创建、删除及其相关方法不支持在主备集群的备库模式下执行。

1. AWR\_CLEAR\_HISTORY();

清理之前的所有 SNAPSHOT 记录。

**语法如下：**

```
PROCEDURE AWR_CLEAR_HISTORY();
```
2. AWR\_SET\_INTERVAL();

设置生成 SNAPSHOT 的时间间隔。

**语法如下：**

```
PROCEDURE AWR_SET_INTERVAL(
    AWR_INTERVAL    IN        INT        DEFAULT 60
);
```

**参数详解**

- AWR\_INTERVAL
	时间间隔。单位分钟，取值范围为 10~525600，缺省值为 60。参数为 0 时，关闭快照（关闭时参数值为 57816000 分钟(110 年)，是一个无效的值）。
3. AWR\_REPORT\_HTML

**定义 1：**

将 AWR 数据报表生成 HTML 格式的报告。

```
FUNCTION AWR_REPORT_HTML(
    START_SNAP_ID    IN        INT,
    END_SNAP_ID        IN        INT
)RETURN AWRRPT_ROW_TYPE PIPELINED;
```

**参数详解**

- START\_SNAP\_ID
	起始 SNAPSHOT\_ID。
- END\_SNAP\_ID
	终止 SNAPSHOT\_ID。

**返回值**

返回包含报告的全部 HTML 脚本信息的嵌套表类型 AWRRPT\_ROW\_TYPE。

**定义 2：**

把 AWR 数据报表生成到指定路径的 HTML 文件。

```
PROCEDURE  SYS.AWR_REPORT_HTML(
    START_ID    IN        INT, 
    END_ID        IN        INT, 
    DEST_DIR    IN        VARCHAR(128), 
    DEST_FILE    IN        VARCHAR(128)
);
```

**参数详解**

- START\_ID
	起始 SNAPSHOT\_ID。
- END\_ID
	终止 SNAPSHOT\_ID。
- DEST\_DIR
	指定生成报告的目标路径。
- DEST\_FILE
	指定生成报告的目标文件名，文件名需要以.HTM 和.HTML 结尾。
4. AWR\_REPORT\_TEXT

**定义 1：**

生成 TEXT 格式的报告。

```
FUNCTION AWR_REPORT_TEXT(
    START_SNAP_ID    IN        INT,
    END_SNAP_ID        IN        INT
) RETURN AWRRPT_ROW_TYPE PIPELINED;
```

**参数详解**

- START\_SNAP\_ID
	起始 SNAPSHOT\_ID。
- END\_SNAP\_ID
	终止 SNAPSHOT\_ID。

**返回值**

返回包含报告的全部 TEXT 脚本信息的嵌套表类型 AWRRPT\_ROW\_TYPE。

**定义 2：**

把 AWR 数据报表生成到指定路径的 TEXT 文件。

```
PROCEDURE  SYS.AWR_REPORT_TEXT(
    START_ID    IN        INT, 
    END_ID        IN        INT, 
    DEST_DIR    IN        VARCHAR(128), 
    DEST_FILE    IN        VARCHAR(128)
);
```

**参数详解**

- START\_ID
	起始 SNAPSHOT\_ID。
- END\_ID
	终止 SNAPSHOT\_ID。
- DEST\_DIR
	指定生成报告的目标路径。
- DEST\_FILE
	指定生成报告的目标文件名，文件名需要以.txt 结尾。
5. CREATE\_SNAPSHOT

创建一次快照 SNAPSHOT

**语法如下：**

```
FUNCTION CREATE_SNAPSHOT(
    FLUSH_LEVEL        IN        VARCHAR2    DEFAULT 'TYPICAL'
) RETURN INT;
```

**参数详解**

- FLUSH\_LEVEL
	'TYPICAL' OR 'ALL'；如果为空，则缺省为'TYPICAL'，该值会影响快照生成数据的大小，如果是'ALL'，则将全部历史数据保存，如果是'TYPICAL'则会刷部分数据。目前该参数只形式支持，暂未支持实际功能。

**返回值**

返回创建的快照 ID 值。

6. DROP\_SNAPSHOT\_RANGE

删除指定快照 ID 范围内的快照。

**语法如下：**

```
PROCEDURE DROP_SNAPSHOT_RANGE(
    LOW_SNAP_ID        IN        INT,
    HIGH_SNAP_ID    IN        INT,
    DBID            IN        INT            DEFAULT NULL,
    FREE_TS_SIZE       IN      BOOLEAN        DEFAULT FALSE
);
```

**参数详解**

- LOW\_SNAP\_ID
	范围的起始值。
- HIGH\_SNAP\_ID
	范围的结束值。
- DBID
	表示 snapshot 所在的 DB 唯一标识，默认为 NULL，表示当前 DB，目前该参数暂时忽略不支持。
- FREE\_TS\_SIZE
	是否不等待触发器执行，直接释放被删除快照对应分区表空间。TRUE：是；FALSE：否。缺省为 FALSE，表示等待系统触发器执行时统一释放空间。目前该参数暂时忽略不支持。
7. DROP\_SNAPSHOT\_BY\_TIME

删除快照创建时间小于等于指定时间戳的所有快照。

**语法如下：**

```
PROCEDURE DROP_SNAPSHOT_BY_TIME(
    END_DT           IN     TIMESTAMP,
    FREE_TS_SIZE    IN     BOOLEAN DEFAULT FALSE
);
```

**参数详解：**

- END\_DT
	指定时间戳，若指定为 NULL，则指定时间戳为当前系统时间。
- FREE\_TS\_SIZE
	是否不等待触发器执行，直接释放被删除快照对应分区表空间。TRUE：是；FALSE：否。缺省为 FALSE，表示等待系统触发器执行时统一释放空间。目前该参数暂时忽略不支持。
8. MODIFY\_SNAPSHOT\_SETTINGS

设置 snapshot 的属性值。

**语法如下：**

```
PROCEDURE MODIFY_SNAPSHOT_SETTINGS(
    RETENTION        IN        INT        DEFAULT NULL,
    AWR_INTERVAL    IN        INT        DEFAULT NULL,
    TOPNSQL            IN        INT        DEFAULT NULL,
    DBID            IN        INT        DEFAULT NULL
);

PROCEDURE MODIFY_SNAPSHOT_SETTINGS(
    RETENTION        IN          INT        DEFAULT NULL,
    AWR_INTERVAL     IN          INT        DEFAULT NULL,
    TOPNSQL          IN          VARCHAR2,
    DBID             IN          INT        DEFAULT NULL
);
```

**参数详解**

- RETENTION
	表示 SNAPSHOT 在数据库中保留的时间，以分钟为单位，最小值为 1 天，最大值为 100 年；如果值为 0，则表示永久保留；如果值为 NULL，则表示本次设置的该值无效，保留以前的旧值。
- AWR\_INTERVAL
	表示每次生成 SNAPSHOT 的间隔时间，以分钟为单位，最小值为 10 分钟，最大值为 1 年；如果值为 0，则 SNAPSHOT 会失效。如果值为 NULL，则表示本次设置的该值无效，保留以前的旧值。
- TOPNSQL
	如果为 NULL，则保留当前设置的值。
	如果为 INT 类型，则表示按照 SQL 的衡量标准（执行时间，CPU 时间，消耗内存等）获取保存的 SQL 个数，最小值为 30，最大值为 50000。
	如果为 VARCHAR2 类型，则可以设置如下 3 个值：DEFAULT、MAXIMUM 和 N。DEFAULT 对应值为 100；MAXIMUM 对应值为 50000；值 N 是数字串，但要求转化为 INT 类型之后，值必须在 30 至 50000 之间。
	目前该参数暂时忽略不支持。
- DBID
	表示 SNAPSHOT 所在的 DB 唯一标识，缺省为 NULL，表示当前 DB。目前该参数暂时忽略不支持。
9. AWR\_CLEAR\_TMP\_TABLE

清理创建快照时产生的中间表。

创建快照时系统会创建中间表临时存储数据，预期在创建快照阶段末尾进行删除，若发生异常导致中间表未能如期删除，可以调用此接口对中间表进行手动清理。

**语法如下**

```
PROCEDURE  AWR_CLEAR_TMP_TABLE();
```
10. ASH\_REPORT\_HTML

**定义 1：**

将 ASH 数据报表生成 html 格式的报告。

```
FUNCTION ASH_REPORT_HTML(
    START_SNAP_ID    IN        INT,
    END_SNAP_ID        IN        INT
)RETURN AWRRPT_ROW_TYPE PIPELINED;
```

**参数详解**

- START\_ID
	起始 SNAPSHOT\_ID。
- END\_ID
	终止 SNAPSHOT\_ID。

**返回值**

返回包含报告的全部 html 脚本信息的嵌套表类型 AWRRPT\_ROW\_TYPE。

**定义 2：**

把 ASH 数据报表（目前支持单机、主备和 DPC）生成到指定路径的 HTML 文件。

```
PROCEDURE  SYS.ASH_REPORT_HTML(
    START_ID        IN        INT, 
    END_ID            IN        INT, 
    DEST_DIR        IN        VARCHAR(128), 
    DEST_FILE        IN        VARCHAR(128)
);
```

**参数详解**

- Start\_ID
	起始 snapshot\_id。
- End\_ID
	终止 snapshot\_id。
- DEST\_DIR
	指定生成报告的目标路径。
- DEST\_FILE
	指定生成报告的目标文件名，文件名需要以.htm 或.html 结尾。

**存在限制**

目标路径 DEST\_DIR 的长度与目标文件名 DEST\_FILE 的长度的加和小于 256。

## 21.2 系统表

DBMS\_WORKLOAD\_REPOSITORY 包相关的系统表包括快照信息管理表及快照信息表，这些系统表都只有创建了 DBMS\_WORKLOAD\_REPOSITORY 包后才能查看。

### 21.2.1 快照信息管理表

1. SYS.WRM$\_WR\_CONTROL

记录快照的相关控制信息。

| **列名** | **类型** | **说明** |
| --- | --- | --- |
| DBID | INTEGER | 数据库 id（NULL） |
| SNAP\_INTERVAL | INTERVAL DAY(5) TO SECOND(1) | 快照间隔 |
| RETENTION | INTERVAL DAY(5) TO SECOND(1) | 快照保留时间（单位:INTERVAL DAY TO SECOND 类型） |
| TOPNSQL | INTEGER | 每次快照搜集 sql 条数 |
| STATUS\_FLAG | INTEGER | AWR 状态（1：开启；0：关闭） |

2. SYS.WRM$\_SNAPSHOT

记录快照的相关信息。

| **列名** | **类型** | **说明** |
| --- | --- | --- |
| SNAP\_ID | INTEGER | 快照 ID |
| DBID | INTEGER | 数据库 ID（NULL） |
| INSTANCE\_NUMBER | INTEGER | 实例编号 |
| STARTUP\_TIME | DATETIME(6) | 数据库启动时间 |
| BEGIN\_INTERVAL\_TIME | DATETIME(6) | 开始快照时间 |
| END\_INTERVAL\_TIME | DATETIME(6) | 结束快照时间 |
| FLUSH\_ELAPSED | INTERVAL DAY(5) TO SECOND(1) | 生成快照的时间（NULL） |
| SNAP\_LEVEL | INTEGER | 快照等级，恒为 1 |
| STATUS | INTEGER | 快照是否成功生成，0：成功；1：失败（NULL） |
| ERROR\_COUNT | INTEGER | 快照生成失败时的错误数（NULL） |
| BL\_MOVED | INTEGER | 保留字段（NULL） |
| SNAP\_FLAG | INTEGER | 快照生成方式（NULL） |
| SNAP\_TIMEZONE | INTERVAL DAY(1) TO SECOND(0) | 快照生成的时区和 UTC 时区的时间差 |
| BEGIN\_INTERVAL\_TIME\_TZ | DATETIME(6) WITH TIME ZONE | 带时区的开始快照时间 |
| END\_INTERVAL\_TIME\_TZ | DATETIME(6) WITH TIME ZONE | 带时区的结束快照时间 |

### 21.2.2 快照信息表

快照信息表记录快照中数据库的一些具体信息。

1. SYS.WRH$\_RESOURCE\_LIMIT

显示所有快照中表、用户的空间限制信息。

| **列名** | **类型** | **说明** |
| --- | --- | --- |
| SNAP\_ID | INTEGER | 快照 ID |
| NAME | VARCHAR(128) | 表/用户名 |
| ID | INTEGER | 表/用户 ID |
| TYPE | VARCHAR(64) | 表/用户类型 |
| SPACE\_LIMIT | INTEGER | 空间限制大小，以页为单位 |
| SPACE\_USED | INTEGER | 空间实际使用大小，以页为单位 |

2. SYS.WRH$\_SQL\_HISTORY

当 INI 参数 ENABLE\_MONITOR=1 时，显示所有快照中执行 sql 的历史记录信息，其中不同快照的 SQL\_ID 和 START\_TIME 肯定不相同。

| **列名** | **类型** | **说明** |
| --- | --- | --- |
| SNAP\_ID | INTEGER | 快照 ID |
| SQL\_ID | INTEGER | 当前语句的 SQL ID |
| START\_TIME | DATETIME(6) | SQL 执行的起始时间 |
| TIME\_USED | BIGINT | SQL 执行所使用时间（单位：usec） |
| BYTES\_DYNAMIC\_ALLOCED | BIGINT | 动态分配字节数 |
| N\_LOGIC\_READ | INTEGER | 语句逻辑读的次数 |
| N\_PHY\_READ | INTEGER | 语句物理读的次数 |
| AFFECTED\_ROWS | INTEGER | 语句影响的行数 |
| HARD\_PARSE\_FLAG | INTEGER | 语句硬解析标记，0：软解析；1：语义解析；2：硬解析 |
| EXEC\_ID | BIGINT | SQL 执行 ID |

3. SYS.WRH$\_SQLTEXT

显示所有快照的缓冲区中的 SQL 语句信息。

| **列名** | **类型** | **说明** |
| --- | --- | --- |
| SNAP\_ID | INTEGER | 快照 ID |
| SQL\_ID | INTEGER | 语句的 SQL ID |
| N\_EXEC | INTEGER | 语句执行次数 |
| SQL\_TEXT | TEXT | SQL 语句内容，超过 7168 的串不分行显示，而是显示成一行 |
| SQL\_NTH | INTEGER | SQL 语句段号（从 0 开始） |

4. SYS.WRH$\_SQLTEXT\_TMP

SYS.WRH$\_SQLTEXT 的辅助表，显示所有快照中缓冲区中的 SQL 语句信息。

| **列名** | **类型** | **说明** |
| --- | --- | --- |
| SNAP\_ID | INTEGER | 快照 ID |
| SQL\_ID | INTEGER | 语句的 SQL ID |
| N\_EXEC | INTEGER | 语句执行次数 |
| SQL\_TEXT | TEXT | SQL 语句内容，与 v$SQLTEXT 里的一致，超过 7168 的串分行显示 |
| SQL\_NTH | INTEGER | SQL 语句段号（从 0 开始） |

5. SYS.WRH$\_SESSIONS

显示所有快照中会话的具体信息，如执行的 sql 语句、主库名、当前会话状态、用户名等。

| **列名** | **类型** | **说明** |
| --- | --- | --- |
| SNAP\_ID | INTEGER | 快照 ID |
| N\_SESSIONS | INTEGER | 会话数 |
| N\_STMTS | INTEGER | 已使用的 STMT 数量之和 |

6. SYS.WRH$\_SESSION\_WAIT\_HISTORY

显示所有快照中会话等待事件的历史信息。

| **列名** | **类型** | **说明** |
| --- | --- | --- |
| SNAP\_ID | INTEGER | 快照 ID |
| SQL\_ID | INTEGER | 语句的 SQL ID |
| EVENT# | SMALLINT | 事件编号 |
| EVENT | VARCHAR(32) | 事件名称 |
| TIME\_WAITED\_MICRO | INTEGER | 等待时间（单位：微秒） |
| WAIT\_CLASS# | SMALLINT | 等待事件类别编号 |
| SESSION# | INTEGER | 会话 ID |

7. SYS.WRH$\_ACTIVE\_SESSION\_HISTORY

显示当前活动会话的等待信息。

此表与其他快照信息表的不同之处是，向此表内插入数据的时间周期与 ASH 刷盘的时间周期保持一致，而不与创建快照的时间周期一致。这就导致执行创建快照的操作后此表内可能没有数据写入，或者未执行创建快照的操作但此表内已写入数据两种情况均属正常现象。例如：由于一个快照创建时间需要至少几秒钟，而 ASH 自身采样频率为 1s, 故快照 BEGIN\_INTERVAL\_TIME 与 END\_INTERVAL\_TIME 之间可能出现查询 WRH$\_ACTIVE\_SESSION\_HISTORY 表数据不同批次的情况。

基于上述差异，SNAP\_ID 这一列定义也存在不同。此视图中 SNAP\_ID 为插入数据时的时间戳，不是快照表 WRM$\_SNAPSHOT 中的快照 ID，所以在生成 ASH 报表时部分模块需要首先获取开始和结束快照对应的 BEGIN\_INTERVAL\_TIME，即数据插入时的系统时间。

可以通过以下语句，获取实际进行 ASH 报表模块生成的、可以映射在 WRH$\_ACTIVE\_SESSION\_HISTORY 快照信息表中的 SNAP\_ID 范围。

```
--获取指定快照id在WRH$_ACTIVE_SESSION_HISTORY中的时间戳范围
--语句中涉及的START_SNAP_ID和END_SNAP_ID分别表示生成ASH报表时指定的起始SNAP_ID和结束SNAP_ID。
DECLARE
    TMP_START       BIGINT;
    TMP_END         BIGINT;
    CURSOR CUR1 FAST IS
       SELECT SNAP_ID, TO_NUMBER(YEAR(BEGIN_INTERVAL_TIME)) TYEAR, TO_NUMBER(MONTH(BEGIN_INTERVAL_TIME)) TMONTH,
         TO_NUMBER(DAY(BEGIN_INTERVAL_TIME)) TDAY, TO_NUMBER(HOUR(BEGIN_INTERVAL_TIME)) THOUR,
         TO_NUMBER(MINUTE(BEGIN_INTERVAL_TIME)) TMINUTE, TO_NUMBER(SECOND(BEGIN_INTERVAL_TIME)) TSECOND
       FROM SYS.WRM$_SNAPSHOT WHERE SNAP_ID IN (START_SNAP_ID, END_SNAP_ID);
BEGIN
    FOR X IN CUR1 LOOP
        IF X.SNAP_ID = 1 THEN 
         TMP_START = X.TYEAR * 10000000000 + X.TMONTH * 100000000 + X.TDAY * 1000000 + X.THOUR * 10000 + X.TMINUTE * 100 + X.TSECOND;
        ELSE
         TMP_END = X.TYEAR * 10000000000 + X.TMONTH * 100000000 + X.TDAY * 1000000 + X.THOUR * 10000 + X.TMINUTE * 100 + X.TSECOND;
        END IF;
    END LOOP;
  PRINT TMP_START;
  PRINT TMP_END;
END;
/
```

该表的列说明中提到的 SESSION\_STATE 对应于 V$ACTIVE\_SESSION\_HISTORY 系统视图的 SESSION\_STATE 列。

| **列名** | **类型** | **说明** |
| --- | --- | --- |
| SNAP\_ID | BIGINT | 执行数据插入时的系统时间，格式为 YYYYMMDDHH24MISS，与其他信息表不同 |
| INSTANCE\_NUMBER | INTEGER | 实例个数，单机下为 1 |
| SAMPLE\_ID | BIGINT | 采样 ID |
| SAMPLE\_TIME | DATETIME(3) | 采样时戳 |
| SESSION\_ID | BIGINT | 会话 ID |
| SESSION\_SERIAL# | INTEGER | 会话序列号，用来唯一标识会话 |
| USER\_ID | INTEGER | 当前用户 ID |
| SQL\_ID | INTEGER | 采样时正在执行的语句 ID |
| IS\_SQLID\_CURRENT | VARCHAR(1) | SQL\_ID 列所标识的语句是否正在执行(Y/N) |
| SESSION\_TYPE | VARCHAR(10) | FOREGROUND/BACKGROUND   FOREGROUND 表示用户创建的会话；   BACKGROUND 表示系统内部创建的会话 |
| SQL\_OPCODE | INTEGER | SQL 语句类型 |
| SQL\_OPNAME | VARCHAR(64) | SQL 语句类型名 |
| EVENT | VARCHAR(64) | 如果 SESSION\_STATE=WAITING，则表示会话在采样时的等待事件。否则为 NULL |
| EVENT\_ID | SMALLINT | 采样时等待事件的 ID |
| P1TEXT | VARCHAR(64) | 等待事件对应的参数 1 说明 |
| P1 | VARCHAR(256) | 等待事件对应的参数 1 值 |
| P2TEXT | VARCHAR(64) | 等待事件对应的参数 2 说明 |
| P2 | BIGINT | 等待事件对应的参数 2 值 |
| P3TEXT | VARCHAR(64) | 等待事件对应的参数 3 说明 |
| P3 | BIGINT | 等待事件对应的参数 3 值 |
| P4TEXT | VARCHAR(64) | 等待事件对应的参数 4 说明 |
| P4 | BIGINT | 等待事件对应的参数 4 值 |
| WAIT\_CLASS | VARCHAR(64) | 等待会话在采样时等待的事件的类名 |
| WAIT\_CLASS\_ID | INTEGER | 等待会话在采样时等待的事件的类 ID |
| WAIT\_TIME | BIGINT | 如果是在 SESSION\_STATE=ON CPU 采样，则表示会话上次等待的事件的总等待时间，单位为微秒，否则为 0 |
| TIME\_WAITED | BIGINT | 如果 SESSION\_STATE=WAITING，则表示会话实际花费在等待该事件的时间，单位微秒 |
| PROGRAM | VARCHAR(128) | 程序名 |
| MODULE | VARCHAR(64) | 采样时执行模块的名称(DBMS\_APPLICATION\_INFO.SET\_MODULE) |
| ACTION | VARCHAR(64) | 采样时执行模块的动作(DBMS\_APPLICATION\_INFO.SET\_ACTION) |
| CLIENT\_ID | VARCHAR(64) | 客户端标识 |
| SQL\_EXEC\_ID | BIGINT | SQL 执行 ID |
| TOP\_LEVEL\_SQL\_ID | INTEGER | 顶层 SQL 语句 ID |
| TOP\_LEVEL\_SQL\_OPCODE | INTEGER | 顶层 SQL 语句类型 |
| MACHINE | VARCHAR(128) | 客户端的机器名 |
| PORT | INTEGER | 客户端的端口号 |

快照信息表共有 39 张表，每张快照信息表都有其对应的动态性能视图，快照信息表名以“WRH$\_”开头，相应的动态性能视图名以“V$”开头。例如快照信息表 SYS.WRH$\_ARCH\_QUEUE 对应的动态性能视图为 V$ARCH\_QUEUE。除了上述 7 张快照信息表与其对应的动态性能视图在结构上有些许不同，其余的快照信息表仅比对应的动态性能视图多一列名为 SNAP\_ID 的整型列，其余结构完全相同，如 SYS.WRH$\_ARCH\_QUEUE 仅比 V$ARCH\_QUEUE 多一列 SNAP\_ID，这里不再赘述，仅给出快照信息表的名称，具体字段介绍可以参考对应的动态性能视图，动态性能视图介绍可参考《DM8 系统管理员手册》附录 2。

剩余的快照信息表名称如下：

1. SYS.WRH$\_ARCH\_QUEUE
2. SYS.WRH$\_BUFFERPOOL
3. SYS.WRH$\_CKPT\_HISTORY
4. SYS.WRH$\_DATAFILE
5. SYS.WRH$\_DB\_CACHE
6. SYS.WRH$\_DEADLOCK\_HISTORY
7. SYS.WRH$\_DMSQL\_EXEC\_TIME
8. SYS.WRH$\_DM\_INI
9. SYS.WRH$\_HASH\_MERGE\_USED\_HISTORY
10. SYS.WRH$\_LARGE\_MEM\_SQLS
11. SYS.WRH$\_LOCK
12. SYS.WRH$\_MAL\_INFO
13. SYS.WRH$\_MEM\_POOL
14. SYS.WRH$\_MTAB\_USED\_HISTORY
15. SYS.WRH$\_PSEG\_ITEMS
16. SYS.WRH$\_RLOG
17. SYS.WRH$\_SCP\_CACHE
18. SYS.WRH$\_SESSION\_HISTORY
19. SYS.WRH$\_SORT\_HISTORY
20. SYS.WRH$\_SQL\_NODE\_HISTORY
21. SYS.WRH$\_SQL\_PLAN\_NODE
22. SYS.WRH$\_SQL\_STAT\_HISTORY
23. SYS.WRH$\_SYSSTAT
24. SYS.WRH$\_SYSTEMINFO
25. SYS.WRH$\_SYSTEM\_EVENT
26. SYS.WRH$\_TABLESPACE
27. SYS.WRH$\_TASK\_QUEUE
28. SYS.WRH$\_TRACE\_QUEUE
29. SYS.WRH$\_VIRTUAL\_MACHINE
30. SYS.WRH$\_WAIT\_HISTORY
31. SYS.WRH$\_TRX
32. SYS.WRH$\_LONG\_EXEC\_SQLS

## 21.3 创建、检测、删除语句

### 21.3.1 SP\_INIT\_AWR\_SYS

创建或删除 DBMS\_WORKLOAD\_REPOSITORY 系统包。

**语法如下：**

```
void
SP_INIT_AWR_SYS(
    CREATE_FLAG        INT
)
```

**参数详解**

- CREATE\_FLAG
	为 1 时表示创建 DBMS\_WORKLOAD\_REPOSITORY 包；为 0 表示删除该系统包。

**返回值**

无

**举例说明**

创建 DBMS\_WORKLOAD\_REPOSITORY 系统包。

```
SP_INIT_AWR_SYS(1);
```

### 21.3.2 SF\_CHECK\_AWR\_SYS

系统的 DBMS\_WORKLOAD\_REPOSITORY 系统包启用状态检测。

**语法如下：**

```
int
SF_CHECK_AWR_SYS ()
```

**返回值**

0：未启用；1：已启用

**举例说明**

获得 DBMS\_WORKLOAD\_REPOSITORY 系统包的启用状态。

```
SELECT SF_CHECK_AWR_SYS;
```

## 21.4 报表解析说明

### 21.4.1 信息表介绍

> **注意**
> 
> 下面对各报表含义的详细介绍中，由于部分项的含义是较为明显的，存在对部分内容做忽略处理的情况，实际包含内容以生成的报表为准。

自动工作集负载信息库 AWR（Automatic Workload Repository）提供了某一时间段内整个系统的报表数据，通过生成并解读该报告，用户能够对指定时间段内数据库系统的性能进行分析。后文中按照报表标题名细分出了若干小节，并依次给出了 AWR 报告中每个表格中的字段名、相应的说明和字段的计算方式。信息表的各个部分含义如下：

- HEAD INFO

AWR 报告的头部信息，包含数据库基本信息（DB INFO）、实例运行环境基本信息（HOST INFO）、快照统计基本信息（SNAP INFO）三个部分。

- Report Summary

AWR 报告的摘要，包含内存池信息报告（Memory Pool）、缓存池信息报告（Buffer Pool）、两次快照之间的数据库负载概况（Load Profile）、内存命中率及数据库实例操作的效率报告（Instance Efficiency Percentages）、系统中最严重的 5 个等待（Top 5 Timed Foreground Events）。

- Main Report

AWR 报告的主体部分，包含等待事件统计信息等待事件统计名称（Wait Events Statistics）、SQL 语句相关统计（SQL Statistics）、实例活动统计信息（Instance Activity Statistics）、IO 信息（IO Stats）、缓存区统计信息（Buffer Pool Statistics）、等待事件统计信息（Wait Statistics）、撤销的统计信息（Undo Statistics）、锁统计信息（Lock Statistics）、死锁统计信息（Dead Lock Statistics）、隔离区活动统计信息（Seg Activity Statistics ）、数据库缓存信息（Dictionary Cache Statistics）、库缓存统计信息（Library Cache Statistics）、内存池的统计信息（Memory Statistics）、分类统计信息（Sort Statistics）、空间限制信息（Resource Limit Statistics）、邮箱视图信息（Mail Statistics）、dm.ini 参数信息（dm.ini Parameters）、顶级等待事件中的高负载 SQL 语句（Top SQL with Top Events）。

除了 AWR 数据报表以外，用户也可自行生成并解读 ASH 数据报表。由于二者存在部分重叠内容，因此放在一起介绍。ASH 数据报表各方面含义如下：

- HEAD INFO

ASH 报告的头部信息，包含 DB INFO 和 SNAP INFO。其中大部分项的解释与 AWR 一致，在 AWR 的 HEAD INFO 中统一介绍。

- ASH\_REPORT

ASH 报告的主体部分，包括顶级等待事件（Top Event），负载情况（Load Profile），顶级 SQL 语句（Top SQL），顶级等待会话（Top Sessions），分析期间的活动与工作负载（Activity Over Time）。各内容将在 AWR 的 Main Report 中介绍。

#### 21.4.1.1 HEAD INFO

##### 21.4.1.1.1 DB INFO

显示数据库的基本信息，每个字段说明及值的计算参见下表。

表21.1 DB INFO说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| DB Name | 数据库名 | 初始化时指定的数据库名 |
| DB Id | 数据库唯一标识 | \\ |
| Instance | 实例名 | 生成报表时指定的起始快照 ID 对应的实例名 |
| Inst num | 实例数 | 单机环境为 1 |
| Startup Time | 起始快照服务器启动时间 | V$INSTANCE 中的 START\_TIME |
| Release | 起始快照服务器的版本 | V$INSTANCE 中的 SVR\_VERSION |
| DSC | 是否为 DSC 环境 | 单机环境为 NO, DSC 环境为 YES |

##### 21.4.1.1.2 HOST INFO

显示实例运行环境，每个字段说明及值的计算参见下表。

表21.2 HOST INFO说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Host Name | 主机名 | V$INSTANCE 中 HOST\_NAME |
| Platform | 实例运行平台 | \\ |
| Cpus | cpu 数 | V$SYSTEMINFO 中 N\_CPU |
| Cores | 核数 | CORE\_NUM\*SOCKET\_NUMBER |
| Sockets | socket 数 | SOCKET\_NUMBER |
| Memory(GB) | 内存 | 物理内存大小，单位 GB |

##### 21.4.1.1.3 SNAP INFO

显示快照统计的基本信息，每个字段说明及值的计算参见下表。

表21.3 SNAP INFO说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Snap Id | 快照 ID | 传入参数：快照的范围值\[start,end\] |
| Snap Time | 快照生成的时间 | 起始和结束快照生成的时间。AWR 对应的是起始和结束快照的结束生成时间，即 WRM\\\_SNAPSHOT中的END\_INTERVAL\_TIME，ASH对应的是及时和结束快照的开始生成时间，即WRM\_SNAPSHOT 中的 BEGIN\_INTERVAL\_TIME |
| Sessions | 生成快照时的会话数 | V$SESSIONS count(\*) |
| stmts/Session | 每个会话的语句数 | V$SESSIONS SUM(N\_USED\_STMT)/Sessions |
| Elapsed | 起始快照和结束快照持续的时间 | 起始快照和结束快照的时间差 |
| DB Time | 在起始和结束快照间的数据库时间 | V$SYSSTAT 中的 db\_time (ms), 选择起始和结束快照的差值 |
| Average Active Session | 平均活动会话 | WRH$\_ACTIVE\_SESSION\_HISTORY 信息表中获取到采样 SQLID 总数/去重后会话数 |

#### 21.4.1.2 Report Summary

##### 21.4.1.2.1 Memory Pool

记录 dm memory pool 的使用情况，每个字段说明及值的计算参见下表。每项显示 begin 和 end 的值。

表21.4 Memory Pool说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Memory Pool Size(MB) | 内存池大小 | V$SYSSTAT 中’ memory pool size in bytes’ |
| Memory Used(MB) | 内存池使用大小 | V$SYSSTAT 中’memory used bytes’ |
| Bytes Allocated From OS(MB) | 从 OS 申请内存数 | V$SYSSTAT 中’bytes allocated from os’ |
| Memory used bytes from os(MB) | 内存池使用字节数 | V$SYSSTAT 中’memory used bytes from os’ |
| Memory Usage % | memory pool 使用率 | memory used / memory pool size |
| % SQL with executions>1 | 执行次数大于 1 的 sql 比率 | V$SYSSTAT 中的 sql cache hit count / sql executed count |
| % plan with executions>1 | 执行次数大于 1 的计划比率 | V$SYSSTAT 中的 plan cache hit count / sql executed count |
| %rowset cache hit count | rowset 比率 | V$SYSSTAT 中的 rowset cache hit count / rowset total count |

##### 21.4.1.2.2 Buffer Pool

显示 buffer pool 的信息，每个字段说明及值的计算参见下表。每项显示 begin 和 end 的值。

表21.5 Buffer Pool说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Name | 缓冲池名称 | V$BUFFERPOOL 中’NAME’ |
| Page Size(Bytes) | 基缓冲池页大小 | V$BUFFERPOOL 中’PAGE\_SIZE’, 单位 Bytes |
| Total Pages | 页数 | V$BUFFERPOOL 中’ N\_PAGES’ |
| Free | 空闲页数目 | V$BUFFERPOOL 中’FREE’ |
| Logic\_Reads | READ 命中的次数 | V$BUFFERPOOL 中 ’N\_LOGIC\_READS’ |
| Discards | 淘汰的页数 | V$BUFFERPOOL 中’N\_DISCARD’ |
| Rat Hit % | 命中率 | V$BUFFERPOOL 中’RAT\_HIT’ |

##### 21.4.1.2.3 Load Profile

主要记录两次快照之间的数据库负载概况，每个字段的含义和说明，参见下表。

表21.6 Load Profile说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| DB Time(s) | 每秒/每事务的 DB TIME | 总的 db 时间、快照持续时间或总的事务数，根据 V$sysstat 计算，取两次快照的差值 |
| DB CPU(s) | 每秒/每事务的 cpu 时间 | 总的 cpu 时间、快照持续时间或总的事务数，根据 V$sysstat 计算，取两次快照的差值 |
| Redo size | 每秒/每事务 redo 日志的字节大小 | redo 日志的大小（根据 V$sysstat 的 redo log size in pages 计算）与总的 db 时间或者总的事务数的相除 |
| Logical reads | 每秒/每事务逻辑读的块数 | logic read count / db time 或者 total\_trx |
| Block changes | 每秒/每事务修改的块数 | V$SYSSTAT 里添加 block changes 事件 |
| Physical reads | 每秒/每事务物理读的块数 | physical read count / db time |
| Physical writes | 每秒/每事务物理写的块数 | physical write count / db time |
| User calls | 每秒/每事务用户 call 次数 | V$SYSSTAT 中的 command received count 总数 |
| Parses | 每秒/每事 SQL 解析的次数 | 添加 parse 解析次数，prepare\_low2 |
| Hard parses | 每秒/每事务 SQL 硬解析的次数 | V$SYSSTAT 添加硬解析次数，每走一次 phc 算一次 |
| Logons | 每秒/每事务登录的次数 | session alloc count |
| Logoff | 每秒/每事务登出的次数 | session free count |
| Executes | 每秒/每事务 SQL 执行次数 | V$SYSSTAT 中的 sql execution count / 快照持续时间 |
| Rollbacks | 每秒/每事务的回滚率 | transaction rollback count |
| Commit | 每秒/每事务的提交率 | transaction commit count |
| Deadlock | 每秒/每事务的死锁率 | transaction deadlock count |
| Transactions | 每秒事务数.每秒产生的事务数，反映数据库任务繁重与否 | transaction total count |
| %Changes changed per read | 每个逻辑读产生的数据页变更 | data page changes / logic read count |
| Rows per transaction | 每事务行数 | V$SYSSTAT 中的 optimized sort count+one-way sort count+one-way sort count |
| Rows per Sort | 每事务排序行数 | V$SORT\_HISTORY 中 SORT\_ROWS |

##### 21.4.1.2.4 Instance Efficiency Percentages (Target 100%)

本节统计内存命中率及数据库实例操作的效率，每个字段的含义和说明参见下表。

表21.7 Instance Efficiency Percentages说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Buffer Nowait % | 在内存获得数据的未等待比例，在缓冲区中获取 Buffer 的未等待比率 | V$SYSTEM\_EVENT 中的 buffer busy wait 事件 |
| Buffer Hit % | 数据块的命中率 | V$BUFFER\_POOL 中的 N\_LOGIC\_READS / N\_LOGIC\_READS + N\_PHY\_READS |
| Redo NoWait % | LOG 缓冲区获得 BUFFER 的未等待比例 | V$SYSTEM\_EVENT 中的(100-redo log system busy 的 TOTAL\_WAITS)/ TOTAL\_WAITS |
| Library Hit % | 从 Library Cache 中检索到一个解析过的 SQL 或 PL/SQL 语句的比率 | V$SYSSTAT 中的(plan cache hit count + rowset cache hit count + sql cache hit count) / (plan cache hit count + rowset cache hit count + sql cache hit count + plan total count) |
| Execute to Parse % | 语句执行与分析的比例，如果要 SQL 重用率高，则这个比例会很高. 该值越高表示一次解析后被重复执行的次数越多。该值 <0 通常说明 shared pool 设置或者语句效率存在问题，造成反复解析，reparse 可能较严重,或者是可能同 snapshot 有关，通常说明数据库性能存在问题。 | V$SYSSTAT 中的 100 \* (1 - parse count/Executions) |
| In-memory Sort % | 在内存中排序的比率 | V$SYSSTAT 中的 optimized sort count / (optimized sort count + one-way sort count + multi-way sort count) |
| Soft Parse % | 软解析的百分比(softs/(softs+hards))，近似当作 sql 在共享区的命中率 | V$SYSSTAT 中的 parse time - hard parse time(ms) / parse time |
| % Non-Parse CPU | SQL 实际运行时间/(SQL 实际运行时间 +SQL 解析时间) 值越小表示解析消耗时间过多 | V$SYSSTAT 中的(1-PARSE\_CPU)/db time(ms) |

##### 21.4.1.2.5 Top 5 Timed Foreground Events

显示系统中最严重的 5 个等待，按所占等待时间的比例倒序显示，每个字段的说明参见下表。

表21.8 Top 5 Timed Foreground Events说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| event | 等待时间的名称 | V$SYSTEM\_EVENT 中的 Event |
| Waits | 等待的次数 | V$SYSTEM\_EVENT 中的 Total\_waits |
| Times(s) | 等待的时间 | V$SYSTEM\_EVENT 中的 Time\_waited\_micro(s) |
| Avg wait (ms) | 平均等待时间 | V$SYSTEM\_EVENT 中的 Average\_wait\_micro(ms) |
| % DB time | 等待时间和 db time 的比例 | V$SYSTEM\_EVENT 中的 Time\_waited\_micro / db time |
| Wait Class | 等待类别 | Wait\_class |

#### 21.4.1.3 Main Report

##### 21.4.1.3.1 Wait Events Statistics

**21.4.1.3.1.1 Time Model Statistics**

记录各类型任务占用 CPU 时间，每个字段的含义和说明参见下表。

表21.9 Time Model Statistics说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Statistic Name | 统计名称 | 根据 V$SYSSTAT 细分的时间类型划分 |
| Time(s) | 各种类型任务所占用的 CPU 时间 | \\ |
| % of DB Time | 该任务所占用的 CPU 时间占总的 DB TIME 的时间比 | Time/DB Time |

**21.4.1.3.1.2 Operating System Statistics**

记录起始快照与结束快照之间的系统信息，每个字段的含义和说明参见下表。

表21.10 Operating System Statistics说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Statistic | 统计名称 | V$SYSTEMINFO 系统信息 |
| Value | 起始快照对应统计值 | \\ |
| End Value | 结束快照对应统计值 | 仅在与起始快照对应值不同时进行展示 |

**21.4.1.3.1.3 Foreground Wait Class**

记录等待事件类型的次数与所用时间，每个字段的含义和说明参见下表。

表21.11 Foreground Wait Class说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Wait class | 等待事件类别 | V$SYSTEM\_EVENT 中 WAIT\_CLASS |
| Waits | 各种类型事件发生次数 | V$SYSTEM\_EVENT 中 TOTAL\_WAITS |
| %Time -outs | 各种类型事件所占用的 CPU 时间占总的 DB CPU 的时间比 | V$SYSTEM\_EVENT 中的 MAX(TIME\_WAITED\_MICRO)/DB CPU |
| Total Wait Time (s) | 各种类型事件所占用的总的 CPU 时间 | V$SYSTEM\_EVENT 中的 MAX(TIME\_WAITED\_MICRO) |
| Avg Wait(ms) | 各种类型事件的平均 CPU 时间 | Total Wait Time/ Waits |
| %DB time | 各种类型事件所占用的 CPU 时间占总的 DB TIME 的时间比 | Total Wait Time/DB TIME |

**21.4.1.3.1.4 Foreground Wait Events**

记录等待事件的次数与所用时间，每个字段的含义和说明参见下表。

表21.12 Foreground Wait Events说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Event | 事件名称 | V$SYSTEM\_EVENT 中 EVENT |
| Waits | 该事件等待次数 | V$SYSTEM\_EVENT 中 TOTAL\_WAITS |
| %Time -outs | 各种类型事件所占用的 CPU 时间占总的 DB CPU 的时间比 | Total Wait Time/DB CPU |
| Total Wait Time (s) | 事件所占用的总的 CPU 时间 | V$SYSTEM\_EVENT 中 TIME\_WAITED\_MICROSS |
| Avg Wait (ms) | 事件的平均 CPU 时间 | Total Wait Time/ Waits |
| Waits /txn | 每个事务发生的等待次数总的事务个数 | Waits / transaction total count |
| %DB time | 事件所占用的 CPU 时间占总的 DB TIME 的时间比 | Total Wait Time/DB TIME |

**21.4.1.3.1.5 Wait Event Histogram**

事件的等待次数与具体等待时间占比，每个字段的含义和说明参见下表。

表21.13 Wait Event Histogram说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Event | 事件名称 | V$SESSION\_WAIT\_HISTORY 中 EVENT |
| Total waits | 等待次数 | V$SESSION\_WAIT\_HISTORY 中 EVENT, COUNT(\*) |
| % of Waits | 以 <1ms 为例，表示等待时间 <1ms 的百分比 | V$SESSION\_WAIT\_HISTORY 里每种事件的等待时间 <1ms 的等待次数/总的等待事件次数 |

##### 21.4.1.3.2 Sql Statistics

**21.4.1.3.2.1 SQL ordered by Elapsed Time**

sql、pl/sql 按执行时间降序排序。每个字段的含义和说明参见下表。

表21.14 SQL ordered by Elapsed Time说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Elapsed Time (s) | 该条语句执行时间 | V$SQL\_STAT\_HISTORY 的 exec\_time |
| Executions | 该条语句执行次数 | V$SQLTEXT 中 N\_EXEC |
| Elapsed Time per Exec (s) | 每次执行的时间 | Elapsed Time / Executions |
| %Total | 执行时间占 DB TIME 总时间的百分比 | Elapsed Time / DB TIME |
| %CPU | 每条 sqlcpu 时间占执行时间的百分比 | V$SESSION\_WAIT\_HISTORY 中 TIME\_WAITED\_MICRO/Elapsed Time |
| %IO | 每条 sqlIO 时间占执行时间的百分比 | V$SQL\_STAT\_HISTORY 中 IO\_WAIT\_TIME/Elapsed Time |
| SQL Id | 语句编号 | V$SQL\_STAT\_HISTORY 中 SQL\_ID |
| SQL Text | SQL 语句内容 | V$SQLTEXT 中 SQL\_TEXT |

**21.4.1.3.2.2 SQL ordered by CPU Time**

sql、pl/sql 按每条语句的 cpu 时间降序排序。每个字段的含义和说明参见下表。

表21.15 SQL ordered by CPU Time说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| CPU Time (s) | 该条语句 cpu 时间 | V$SESSION\_WAIT\_HISTORY 中 TIME\_WAITED\_MICRO |
| Executions | 该条语句执行次数 | V$SQLTEXT 中 N\_EXEC |
| CPU per Exec (s) | 每次执行的 cpu 时间 | CPU Time (s)/Executions |
| %Total | 该条语句 cpu 时间占总的 cpu 时间的百分比 | CPU Time (s)/V$SYSSTAT 中在指定快照范围内的总的 CPU 时间 |
| Elapsed Time (s) | 该条语句执行时间 | V$SQL\_STAT\_HISTORY 的 exec\_time |
| %CPU | 每条语句 cpu 时间占执行时间的百分比 | CPU Time (s)/Elapsed Time (s) |
| %IO | 每条语句 IO 时间占执行时间的百分比 | V$SQL\_STAT\_HISTORY 中 IO\_WAIT\_TIME/Elapsed Time (s) |
| SQL Id | 语句编号 | V$SQL\_STAT\_HISTORY 中 SQL\_ID |
| SQL Text | SQL 语句内容 | V$SQLTEXT 中 SQL\_TEXT |

**21.4.1.3.2.3 SQL ordered by User I/O Wait Time**

sql、pl/sql 按 User I/O Wait 时间降序排序。每个字段的含义和说明参见下表。

表21.16 SQL ordered by User I/O Wait Time说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| User I/O Time (s) | 该条语句 User IO wait time | V$SQL\_STAT\_HISTORY 中 IO\_WAIT\_TIME |
| Executions | 该条语句执行次数 | V$SQLTEXT 中 N\_EXEC |
| UIO per Exec (s) | 每次执行的 IO wait time | User I/O Time (s)/Executions |
| %Total | 该条语句 cpu 时间占总的 cpu 时间的百分比 | CPU Time (s)/V$SYSSTAT 中在指定快照范围内的总的 CPU 时间 |
| Elapsed Time (s) | 该条语句执行时间 | V$SQL\_STAT\_HISTORY 的 exec\_time |
| %CPU | 每条语句 cpu 时间占执行时间的百分比 | V$SESSION\_WAIT\_HISTORY 中 TIME\_WAITED\_MICRO/Elapsed Time |
| %IO | 每条语句 IO 时间占执行时间的百分比 | V$SQL\_STAT\_HISTORY 中 IO\_WAIT\_TIME/Elapsed Time (s) |
| SQL Id | 语句编号 | V$SQL\_STAT\_HISTORY 中 SQL\_ID |
| SQL Text | SQL 语句内容 | V$SQLTEXT 中 SQL\_TEXT |

**21.4.1.3.2.4 SQL ordered by Gets**

sql、pl/sql 按 buffer gets 时间降序排序。每个字段的含义和说明参见下表。

表21.17 SQL ordered by Gets说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Buffer Gets | 该条语句 Buffer Gets | V$SQL\_STAT\_HISTORY LOGIC\_READ\_CNT |
| Executions | 该条语句执行次数 | V$SQLTEXT 中 N\_EXEC |
| Gets per Exec | 每次执行的 Buffer Gets | Buffer Gets /Executions |
| %Total | 该条语句 Buffer Gets 占总的 Buffer Gets 的百分比 | Buffer Get/ V$SYSSTAT logic read count |
| Elapsed Time (s) | 该条语句执行时间 | V$SQL\_STAT\_HISTORY 的 exec\_time |
| %CPU | 每条语句 cpu 时间占执行时间的百分比 | V$SESSION\_WAIT\_HISTORY 中 TIME\_WAITED\_MICRO/Elapsed Time |
| %IO | 每条语句 IO 时间占执行时间的百分比 | V$SQL\_STAT\_HISTORY 中 IO\_WAIT\_TIME/Elapsed Time (s) |
| SQL Id | 语句编号 | V$SQL\_STAT\_HISTORY 中 SQL\_ID |
| SQL Text | SQL 语句内容 | V$SQLTEXT 中 SQL\_TEXT |

**21.4.1.3.2.5 SQL ordered by Reads**

sql、pl/sql 按 physical reads 降序排序。每个字段的含义和说明参见下表。

表21.18 SQL ordered by Reads说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Physical Reads | 该条语句 Physical Reads | V$SQL\_STAT\_HISTORY 中 PHY\_READ\_CNT |
| Executions | 该条语句执行次数 | V$SQLTEXT 中 N\_EXEC |
| Reads per Exec | 每次执行的 Buffer Gets | Physical Reads /Executions |
| %Total | 该条语句 Physical Reads 占总的 Disk Reads 的百分比 | Physical Reads/总的 Disk Reads 的次数 |
| Elapsed Time (s) | 该条语句执行时间 | V$SQL\_STAT\_HISTORY 的 exec\_time |
| %CPU | 每条语句 cpu 时间占执行时间的百分比 | V$SESSION\_WAIT\_HISTORY 中 TIME\_WAITED\_MICRO/Elapsed Time |
| %IO | 每条语句 IO 时间占执行时间的百分比 | V$SQL\_STAT\_HISTORY 中 IO\_WAIT\_TIME/Elapsed Time (s) |
| SQL Id | 语句编号 | V$SQL\_STAT\_HISTORY 中 SQL\_ID |
| SQL Text | SQL 语句内容 | V$SQLTEXT 中 SQL\_TEXT |

**21.4.1.3.2.6 SQL ordered by Executions**

sql、pl/sql 按执行次数降序排序。每个字段的含义和说明参见下表。

表21.19 SQL ordered by Executions说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Executions | 该条 SQL 执行次数 | V$SQLTEXT 中 N\_EXEC |
| Rows Processed | 该条 SQL 影响行数 | V$SQL\_HISTORY 中 AFFECTED\_ROWS |
| Rows per Exec | 每次执行影响行数 | Rows Processed/ Executions |
| Elapsed Time (s) | 该条语句执行时间 | V$SQL\_STAT\_HISTORY 的 exec\_time |
| %CPU | 每条语句 cpu 时间占执行时间的百分比 | V$SESSION\_WAIT\_HISTORY 中 TIME\_WAITED\_MICRO/Elapsed Time |
| %IO | 每条语句 IO 时间占执行时间的百分比 | V$SQL\_STAT\_HISTORY 中 IO\_WAIT\_TIME/Elapsed Time (s) |
| SQL Id | 语句编号 | V$SQL\_STAT\_HISTORY 中 SQL\_ID |
| SQL Text | SQL 语句内容 | V$SQLTEXT 中 SQL\_TEXT |

**21.4.1.3.2.7 SQL ordered by Parse Calls**

sql、pl/sql 按解析次数降序排序。每个字段的含义和说明参见下表。

表21.20 SQL ordered by Parse Calls说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Parse Calls | 该条语句解析次数 | V$SQL\_STAT\_HISTORY 中 HARD\_PARSE\_CNT |
| Executions | 该条语句执行次数 | V$SQLTEXT 中 N\_EXEC |
| %Total Parses | 该条语句分析次数占总的解析次数的百分比 | Parse Calls/V$SYSSTAT 中 pl/sql parse count |
| SQL Id | 语句编号 | V$SQL\_STAT\_HISTORY 中 SQL\_ID |
| SQL Text | SQL 语句内容 | V$SQLTEXT 中 SQL\_TEXT |

**21.4.1.3.2.8 SQL ordered by Sharable Memory**

sql、pl/sql 按共享内存大小降序排序。每个字段的含义和说明参见下表。只显示共享内存 >1048576 字节的字段。

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Sharable Mem(b) | 该条语句共享内存 | V$LARGE\_MEM\_SQLS 中 MEM\_USED\_BY\_K，单位 KB |
| Executions | 该条语句执行次数 | V$SQLTEXT 中 N\_EXEC |
| %Total | 该条语句共享内存占总的共享内存的百分比 | Sharable Mem(b)/总的共享内存 |
| SQL Id | 语句编号 | V$SQL\_STAT\_HISTORY 中 SQL\_ID |
| SQL Text | SQL 语句内容 | V$SQLTEXT 中 SQL\_TEXT |

**21.4.1.3.2.9 SQL Plan ordered by Cost**

sql、pl/sql 按代价大小降序排序。每个字段的含义和说明参见下表。

表21.22 SQL Plan ordered by Cost说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Pln\_addr(b) | 计划地址 | V$SQL\_PLAN\_NODE 中 PLN\_ADDR |
| Node\_addr | 节点地址 | V$SQL\_PLAN\_NODE 中 NODE\_ADDR |
| Operation | 操作符名称 | V$SQL\_PLAN\_NODE 中 OPERATION |
| Depth | 节点层次 | V$SQL\_PLAN\_NODE 中 DEPTH |
| SQL Id | 语句编号 | V$SQL\_PLAN\_NODE 中中 SQL\_ID |
| card | 行数 | V$SQL\_PLAN\_NODE 中 CARD |
| cost | 代价 | V$SQL\_PLAN\_NODE 中 COST |
| cpu\_cost | CPU 代价 | V$SQL\_PLAN\_NODE 中 CPU\_COST |
| io\_cost | IO 代价 | V$SQL\_PLAN\_NODE 中 IO\_COST |
| SQL Text | SQL 语句内容 | V$SQLTEXT 中 SQL\_TEXT |

**21.4.1.3.2.10 SQL Node ordered by Time**

sql、pl/sql 按节点执行耗时降序排序。每个字段的含义和说明参见下表。

表21.23 SQL Node ordered by Time说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| seq\_no | 操作符在计划中的序号 | V$SQL\_NODE\_HISTORY 中 SEQ\_NO |
| exec\_id | 执行 ID | V$SQL\_NODE\_HISTORY 中 EXEC\_ID |
| node | 节点 ID | V$SQL\_NODE\_HISTORY 中 NODE |
| time\_used(us) | 节点执行耗时 | V$SQL\_NODE\_HISTORY 中 TIME\_USED,单位微秒 |
| SQL Id | 语句编号 | V$SQLTEXT 中 SQL\_ID |
| n\_enter | 节点进入次数 | V$SQL\_NODE\_HISTORY 中 N\_ENTER |
| name | 代价 | V$SQL\_NODE\_NAME 中 NAME |
| SQL Text | SQL 语句内容 | V$SQLTEXT 中 SQL\_TEXT |

**21.4.1.3.2.11 DMSQL ordered by exec time**

sql、pl/sql 按执行时间降序排序。每个字段的含义和说明参见下表。

表21.24 DMSQL ordered by exec time说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| exec\_id | 语句执行号 | V$DMSQL\_EXEC\_TIME 中 EXEC\_ID |
| type \|语句类型 \|VDMSQL\_EXEC\_TIME 中 TYPE$ |  |  |
| seq | 相对序号 | V$DMSQL\_EXEC\_TIME 中 SEQ |
| level | 执行层次 | V$DMSQL\_EXEC\_TIME 中 LEVEL |
| caller | 调用方法名 | V$DMSQL\_EXEC\_TIME 中 CALLER |
| method | 方法名 | V$DMSQL\_EXEC\_TIME 中 METHOD |
| exec\_cnt | 执行次数 | V$DMSQL\_EXEC\_TIME 中 EXEC\_CNT |
| last\_exec\_tick | 最后一次执行时戳 | V$DMSQL\_EXEC\_TIME 中 LAST\_EXEC\_TICK，单位微秒 |
| time\_used(ms) | 执行时间 | V$DMSQL\_EXEC\_TIME 中 LAST\_EXEC\_TICK，单位毫秒 |
| SQL Text | SQL 语句内容 | V$SQLTEXT 中 SQL\_TEXT |

##### 21.4.1.3.3 Instance Activity Statistics

###### 21.4.1.3.3.1 System Statistics

记录统计对象在两快照间的统计信息。每个字段的含义和说明参见下表。

表21.25 System Statistics说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Statistic Name | 统计对象名 | V$SYSSTAT 中 NAME |
| Class Id | 统计对象所属类别 | V$SYSSTAT 中 CLASSID |
| ID | 统计对象 ID | V$SYSSTAT 中 ID |
| Max Stat Val | 最大统计值 | V$SYSSTAT 中 MAX(STAT\_VAL) |
| Min Stat Val | 最小统计值 | V$SYSSTAT 中 MIN(STAT\_VAL) |
| Avg Stat Val | 平均统计值 | V$SYSSTAT 中 AVG(STAT\_VAL) |
| Total | 指定快照范围内统计值总计 | V$SYSSTAT 中 MAX(STAT\_VAL)-MIN(STAT\_VAL) |
| Per Second | 每秒统计值 | Total/Elapsed |
| Per Trans | 每事务统计值 | Total/Transaction |

###### 21.4.1.3.3.2 VM Statistics

记录活动的虚拟机信息。每个字段的含义和说明参见下表。

表21.26 VM Statistics说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| id | 虚拟机 ID | V$VIRTUAL\_MACHINE 中 ID |
| sessid | 会话 ID | V$VIRTUAL\_MACHINE 中 SESSID |
| stmt\_id | 语句 ID | V$VIRTUAL\_MACHINE 中 STMT\_ID |
| exp\_flag | 表达式标识 | V$VIRTUAL\_MACHINE 中 EXP\_FLAG |
| vstack\_size | 栈大小 | V$VIRTUAL\_MACHINE 中 VSTACK\_SIZE |
| vtop | 栈顶离基址距离 | V$VIRTUAL\_MACHINE 中 VTOP |
| vused | 栈已用空间大小 | V$VIRTUAL\_MACHINE 中 VUSED |
| stkfrm\_depth | 栈深度 | V$VIRTUAL\_MACHINE 中 STKFRM\_DEPTH |
| vstack | 栈基址 | V$VIRTUAL\_MACHINE 中 VSTACK |
| free\_stkfrms | 已释放的栈 | V$VIRTUAL\_MACHINE 中 FREE\_STKFRM |
| curr\_frm | 当前栈 | V$VIRTUAL\_MACHINE 中 CURR\_FRM |
| ip | IP 地址 | V$VIRTUAL\_MACHINE 中 IP |
| sql\_no | SQL 语句树的信号 | V$VIRTUAL\_MACHINE 中 SQL\_NO |
| reuse\_cnt | 虚拟机重用次数 | V$VIRTUAL\_MACHINE 中 REUSE\_CNT |

###### 21.4.1.3.3.3 Session history Statistics

记录指定快照范围内会话历史的记录信息，属性列均源于动态视图 V$SESSION\_HISTORY。

##### 21.4.1.3.4 IO Stats

###### 21.4.1.3.4.1 Tablespace IO Stats

统计各表空间 IO 信息，根据读写次数降序排序。每个字段的含义和说明参见下表。

表21.27 Tablespace IO Stats说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Tablespace | 表空间名称 | V$TABLESPACE 中 NAME |
| Reads | 读页 | V$DATAFILE 中 PAGES\_READ，根据表空间 ID 进行 SUM |
| Av Reads/s | 每秒读页 | Reads/DB time |
| Writes | 写页 | V$DATAFILE 中 PAGES\_WRITE，根据表空间 ID 进行 SUM |
| Av Writes/s | 每秒写页 | Writes/DB time |

###### 21.4.1.3.4.2 File IO Stats

记录数据库文件信息，每个字段的含义和说明参见下表。

表21.28 File IO Stats说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Tablespace | 表空间名称 | V$TABLESPACE 中 NAME |
| Path | 数据库文件路径 | V$DATAFILE 中 PATH |
| Reads | 读页 | V$DATAFILE 中 PAGES\_READ |
| Av Reads/s | 每秒读页 | Reads/DB time |
| Writes | 写页 | V$DATAFILE 中 PAGES\_WRITE |
| Av Writes/s | 每秒写页 | Writes/DB time |

##### 21.4.1.3.5 Buffer Pool Statistics

###### 21.4.1.3.5.1 Buffer Pool Statistics

记录缓冲区动态性能信息，每个字段的含义和说明参见下表。

表21.29 Buffer Pool Statistics说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Name | 缓冲区名称 | V$BUFFERPOOL 中 NAME |
| Id | 缓冲区 ID | V$BUFFERPOOL 中 ID |
| Page Size | 基缓冲区页大小 | V$BUFFERPOOL 中 PAGES\_SIZE |
| Pages | 页数 | V$BUFFERPOOL 中 N\_PAGES |
| Total Pages | 页大小 | V$BUFFERPOOL 中 N\_TOTAL\_PAGES |
| Max Pages | 最多的页数 | V$BUFFERPOOL 中 N\_MAX\_PAGES |
| Fixed | 数据页被引用的次数 | V$BUFFERPOOL 中 N\_FIXED |
| Pool Hit % | READ 命中次数占比 | V$BUFFERPOOL 中 N\_LOGIC\_READS/N\_LOGIC\_READS+N\_PHY\_READS |
| Logical Reads | READ 命中次数 | V$BUFFERPOOL 中 N\_LOGIC\_READS |
| Physical Reads | READ 未命中次数 | V$BUFFERPOOL 中 N\_PHY\_READS |
| Exp Bufferpools | 扩展缓冲区个数 | V$BUFFERPOOL 中 N\_EXP\_BUFFERPOOL |

###### 21.4.1.3.5.2 Checkpoint Activity

显示检查点历史信息，每个字段的含义和说明参见下表。

表21.30 Checkpoint Activity说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Thread Id | 线程 ID | V$CKPT\_HISTORY 中 THREAD\_ID |
| Ckpt Cmd | 检查点 | V$CKPT\_HISTORY 中 CKPT\_CMD |
| Start Time | 基缓冲区页大小 | V$CKPT\_HISTORY 中 START\_TIME |
| Total Used Time(s) | 页数 | V$CKPT\_HISTORY 中 TIME\_USED |
| Total Flused Pages | 页大小 | V$CKPT\_HISTORY 中 PAGE\_FLUSHED |
| Min Ckpt Lsn | 最多的页数 | V$CKPT\_HISTORY 中 MIN(CKPT\_LSN) |
| Max Ckpt Lsn | 数据页被引用的次数 | V$CKPT\_HISTORY 中 MAX(CKPT\_LSN) |

###### 21.4.1.3.5.3 Rlog Statistics

显示日志的总体信息，每个字段的含义和说明参见下表。

表21.31 Rlog Statistics说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| ckpt\_lsn | 最近一次检查点 LSN | V$RLOG 中 CKPT\_LSN |
| file\_lsn | 已经到盘上的 LSN | V$RLOG 中 FILE\_LSN |
| flush\_lsn | 当前准备刷盘的 LSN | V$RLOG 中 FLUSH\_LSN |
| cur\_lsn | 当前的 LSN | V$RLOG 中 CUR\_LSN |
| next\_seq | 下一个日志包序号 | V$RLOG 中 NEXT\_SEQ |
| flush\_pages | Flush 链表中的总页数 | V$RLOG 中 FLUSH\_PAGES |
| flushing\_pages | 正在刷盘的总页数 | V$RLOG 中 FLUSHING\_PAGES |
| free\_space | 可用的日志空间 | V$RLOG 中 FREE\_SPACE，单位为字节 |
| total\_space | 日志总空间 | V$RLOG 中 TOTAL\_SPACE，单位为字节 |
| suspend\_time | 挂起时间戳 | V$RLOG 中 SUSPEND\_TIME |
| upd\_ctl\_lsn | 系统修改控制文件的 RLOG\_RESERVE\_THRESHOLD ->lsn | V$RLOG 中 UPD\_CTL\_LSN |
| n\_reserve\_wait | 日志空间预申请等待个数 | V$RLOG 中 N\_RESERVE\_WAIT |

##### 21.4.1.3.6 Wait Statistics

###### 21.4.1.3.6.1 Wait History

记录指定快照范围内等待事件的具体信息，属性列均源于动态视图 V$WAIT\_HISTORY。

###### 21.4.1.3.6.2 Enqueue Activity

记录当前归档任务队列信息，每个字段的含义和说明参见下表。

表21.32 Enqueue Activity说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| queue\_name | 归档类型 | V$ARCH\_QUEUE 中 ARCH\_TYPE |
| readys | 已处理任务数 | V$ARCH\_QUEUE 中 READY |
| total\_wait | 已处理任务的总等待时间 | V$ARCH\_QUEUE 中 TOTAL\_WAIT\_TIME |
| avg\_wait | 已处理任务的平均等待时间 | total\_wait/readys |

##### 21.4.1.3.7 Undo Statistics

###### 21.4.1.3.7.1 Pseg Items

记录回滚系统中回滚项信息，每个字段的含义和说明参见下表。

表21.33 Pseg Items说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Snap Id | 快照 ID | \\ |
| Total Pages | 总回滚页数 | V$PSEG\_ITEMS 中 SUM(N\_PAGES) |
| Total Extends | 总扩展回滚段次数 | V$PSEG\_ITEMS 中 SUM(N\_EXTEND) |
| Total Purge Pages | 总 purge 页数 | V$PSEG\_ITEMS 中 SUM(N\_PURGED\_PAGES) |
| Total Used Pages | 总正在使用的页数 | V$PSEG\_ITEMS 中 SUM(N\_USED\_PAGES) |
| Total Urec Used(MB) | 总生成回滚记录的总字节数 | V$PSEG\_ITEMS 中 SUM(N\_UREC\_BYTES) |
| Total Commit Trx | 总已经提交未 PURGE 的事务数 | V$PSEG\_ITEMS 中 SUM(N\_COMMIT\_TRX) |
| Max Reserve Time | 最大最长的保留时间，单位秒 | V$PSEG\_ITEMS 中 MAX(RESERVE\_TIME) |
| Free Stack Total Pages | 最小空闲回滚页堆栈空间大小，单位页数 | V$PSEG\_ITEMS 中 MIN(STACK\_SIZE) |
| Free Stack Free Pages | 最小空闲回滚页堆栈中空闲页数 | V$PSEG\_ITEMS 中 MIN(STACK\_SP) |

###### 21.4.1.3.7.2 Undo Segment Summary

记录系统中回滚项相关信息，每个字段的含义和说明参见下表。

表21.34 Undo Segment Summary说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Num Undo Blocks | 当前回滚项的回滚块数 | V$PSEG\_ITEMS 中 N\_PAGES |
| Number of Transactions | 当前回滚表空间上执行过的事务总数 | V$PSEG\_ITEMS 中 N\_TRXS |
| Max Exec Len | 持续最久的查询时间 | V$LONG\_EXEC\_SQLS 中 MAX(EXEC\_TIME) |
| Max Tx Concy | 最大事务并发量 | V$TRX 中 MAX(COUNT(ID)) |
| Min/Max TR (mins) | 最小和最大的 undo retention | V$PSEG\_ITEMS 中 MAX(TUNED\_UNDO\_RETENTION) /MIN(TUNED\_UNDO\_RETENTION) |

##### 21.4.1.3.8 Lock Statistics

记录活动的事务锁信息，每个字段的含义和说明参见下表。

表21.35 Lock Statistics说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| addr | 锁地址 | V$LOCK 中 ADDR |
| trx\_id | 所属事务 ID | V$LOCK 中 TRX\_ID |
| ltype | 锁类型 | V$LOCK 中 LTYPE |
| lmode | 锁模式 | V$LOCK 中 LMODE |
| blocked | 是否阻塞 | V$LOCK 中 BLOCKED |
| table\_id | 对于对象锁，表示表对象或字典对象的 ID；对于 TID 锁，表示封锁记录对应的表 ID | V$LOCK 中 TABLE\_ID |
| row\_idx | TID 锁封锁记录行信息 | V$LOCK 中 ROW\_IDX |

##### 21.4.1.3.9 Dead Lock Statistics

###### 21.4.1.3.9.1 Dead Lock Stats

记录死锁的历史信息，每个字段的含义和说明参见下表。

表21.36 Dead Lock Stats说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| SeqNo | 编号 | V$DEADLOCK\_HISTORY 中 SEQNO |
| trx\_id | 事务 ID | V$DEADLOCK\_HISTORY 中 TRX\_ID |
| Sess Id | 会话 ID | V$DEADLOCK\_HISTORY 中 SESS\_ID |
| Sess Seq | 会话序列号 | V$DEADLOCK\_HISTORY 中 SESS\_SEQ |
| Happen Time | 死锁发生时间 | V$DEADLOCK\_HISTORY 中 HAPPEN\_TIME |
| Sql Text | 产生死锁的 SQL 语句 | V$DEADLOCK\_HISTORY 中 SQL\_TEXT |

##### 21.4.1.3.10 Seg Activity Statistics

记录指定快照范围内统计对象 ID 在 98 至 106 区间内的具体信息，属性列均源于动态视图 V$SYSSTAT。

##### 21.4.1.3.11 Dictionary Cache Statistics

记录两快照间数据字典的实时信息，每个字段的含义和说明参见下表。

表21.37 Dictionary Cache Statistics说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Snap Id | 快照编号 | \\ |
| Total Size(MB) | 总缓存池空间，单位字节 | V$DB\_CACHE 中 SUM(TOTAL\_SIZE) |
| Used % | 总实际使用空间，单位字节 | V$DB\_CACHE 中 SUM(USED\_SIZE)/SUM(TOTAL\_SIZE) |
| Dict Num | 总缓存池中字典对象 | V$DB\_CACHE 中 SUM(DICT\_NUM) |
| Total LRU Discards Used(MB) | 总被淘汰字典对象空间的总和，单位字节 | V$DB\_CACHE 中 SUM(SIZE\_LRU\_DISCARD) |
| Total LRU Discards | 总字典对象被淘汰次数 | V$DB\_CACHE 中 SUM(LRU\_DISCARD) |
| DDL Discards | 总 DDL 操作导致字典对象被淘汰的次数 | V$DB\_CACHE 中 SUM(DDL\_DISCARD) |

##### 21.4.1.3.12 Library Cache Statistics

记录两快照间缓存池信息，每个字段的含义和说明参见下表。

表21.38 Library Cache Statistics说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Pln\_addr | 缓存池地址 | V$SCP\_CACHE 中 SCP\_ADDR |
| Pln\_num | 计划缓存总数 | V$SCP\_CACHE 中 PLN\_CNT |
| Sql\_num | SQL 缓存总数 | V$SCP\_CACHE 中 SQL\_CNT |
| RS\_num | 结果集缓存总数 | V$SCP\_CACHE 中 RS\_CNT |
| Discard\_Mem | 缓存对象淘汰大小 | V$SCP\_CACHE 中 DISCARD\_MEM |
| Discard\_cnt | 缓存对象淘汰次数 | V$SCP\_CACHE 中 DISCARD |

##### 21.4.1.3.13 Memory Statistics

记录指定快照范围内所有内存池的具体信息，属性列均源于动态视图 V$MEM\_POOL。

##### 21.4.1.3.14 Sort Statistics

###### 21.4.1.3.14.1 Hash Merge Used History

记录指定快照范围内 HASH MERGE 连接操作符使用的缓存信息，属性列均源于动态视图 V$HASH\_MERGE\_USED\_HISTORY。

###### 21.4.1.3.14.2 Memory Table Used History

显示快照范围内使用 MTAB 空间最多的操作符信息，每个字段的含义和说明参见下表。

表21.39 Memory Table Used History说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Exec Id | 语句执行 ID | V$MTAB\_USED\_HISTORY 中 EXEC\_ID |
| Op Seq No | 操作符在执行计划中序号 | V$MTAB\_USED\_HISTORY 中 OP\_SEQ\_NO |
| Op Type | 节点名字 | V$SQL\_NODE\_NAME 中 NAME |
| Mtab Used(MB) | 操作符使用的 MTAB 空间，单位 MB | V$MTAB\_USED\_HISTORY 中 MTAB\_USED\_BY\_M |
| Sql Text | SQL 文本 | V$MTAB\_USED\_HISTORY 中 SQL\_TEXT |

###### 21.4.1.3.14.3 Sort History

记录指定快照范围内当 INI 参数 ENABLE\_MONITOR=1 都打开时，显示系统自启动以来使用排序页数最多的 50 个操作符信息，属性列均源于动态视图 V$SORT\_HISTORY。

##### 21.4.1.3.15 Resource Limit Statistics

记录指定起始快照与结束快照对应的表的空间限制信息，属性列均源于动态视图 V$RESOURCE\_LIMIT。

##### 21.4.1.3.16 Mail Statistics

记录指定快照范围内 mail 邮箱视图信息，属性列均源于动态视图 V$MAL\_INFO。

##### 21.4.1.3.17 dm.ini Parameters

显示快照范围内 ini 参数和 dminit 建库参数信息，每个字段的含义和说明参见下表。

表21.40 dm.ini Parameters说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Parameter Name | 参数名称 | V$DM\_INI 中 PARA\_NAME |
| Begin value | 起始快照系统参数值 | V$DM\_INI 中 PARA\_VALUE |
| End value (if different) | 结束快照系统参数值 | V$DM\_INI 中 PARA\_VALUE，仅与 Begin value 不同时显示 |

##### 21.4.1.3.18 Top SQL with Top Events

显示采样的 SQL 语句及其对应的等待事件相关信息，来源 V$ACTIVE\_SESSION\_HISTORY。由于动态视图的采样周期与快照生成周期不一致，故此表仅分析在指定快照范围对应的采样时间的采样数据。每个字段的含义和说明参见下表。

表21.41 Top SQL with Top Events说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| SQL ID | SQL 语句 ID | V$ACTIVE\_SESSION\_HISTORY 中 SQL\_ID |
| Samples | SQL 语句的采样次数 | V$ACTIVE\_SESSION\_HISTORY 中 COUNT(SQL\_ID) |
| %Activity | SQL 执行时间对 DB Time 的占比 | V$SQL\_STAT\_HISTORY 中 SUM(EXEC\_TIME) / DB TIME |
| Event | SQL 语句对应等待事件 | V$ACTIVE\_SESSION\_HISTORY 中 EVENT |
| Waits | 事件等待次数 | V$SYSTEM\_EVENT 中 TOTAL\_WAITS，取结束快照与起始快照的差值 |
| %Event | 平均等待时间对 DB Time 的占比 | V$SYSTEM\_EVENT 中 AVERAGE\_WAIT\_MICRO / DB Time |
| Sql Text | 采样的 SQL 语句 | V$SQL\_STAT\_HISTORY 中 SQL\_TXT |

##### 21.4.1.3.19 Top Events

Top Events 分为以下几个模块：顶级用户事件（Top User Events）、（顶级后台事件）Top Background Events、（顶级等待事件参数）Top EVENT P1/P2/P3/P4 Values。

###### 21.4.1.3.19.1 Top User Events

Top User Events 显示顶级用户事件，其中有以下几项需要注意：

- %Event：类名为 User I/O, Concurrency, Commit, Transaction, Network 中所有等待事件数量 / 起始快照之间所有的等待事件数量。
- Avg Wait Time：平均等待时间。从 WRH$\_ACTIVE\_SESSION\_HISTORY 信息表中，类名 WAIT\_CLASS 在 User I/O, Concurrency, Commit, Transaction, Network 中根据事件数量排序取出前 30 条，再从 WRH$\_SYSTEM\_EVENT 表中限制 EVENT IS NOT NULL 即事件类型为等待事件，根据事件名称 EVENT 取出各事件名称在 START\_SNAP\_ID 以及 END\_SNAP\_ID 期间的对应的平均等待时间 AVERAGE\_TIME\_MICRO（单位微秒）。若查询时 SYS.WRH$\_SYSTEM\_EVENT 中不包含所查询的快照数据，查询数据失败会导致该字段全部写入’/ ’。

> **注意**
> 
> WRH$\_SYSTEM\_EVENT信息表记录的是系统启动以来所有等待事件的信息，最后的报表按照等待事件数量进行排序

###### 21.4.1.3.19.2 Top Background Events

显示顶级后台事件。在 WRH$\_ACTIVE\_SESSION\_HISTORY 信息表中，限制字段 SESSION\_TYPE = BACKGROUND 代表收集到事件都为 Background，，再从 WRH$\_SYSTEM\_EVENT 表中限制 EVENT IS NOT NULL 即事件类型为等待事件，根据事件名称 EVENT 取出各事件名称在 START\_SNAP\_ID 以及 END\_SNAP\_ID 期间的对应的平均等待时间 AVERAGE\_TIME\_MICRO（单位微秒）。

###### 21.4.1.3.19.3 Top Event P1/P2/P3/P4 Values

显示顶级等待事件的相关参数，来源于 WRH$\_ACTIVE\_SESSION\_HISTORY 表。根据起始快照 ID，取值 WRH$\_ACTIVE\_SESSION\_HISTORY 中的 P1/P1TEXT，对应 P1/Parameter1 列,分别表示等待事件的参数和参数取值。同样的还有 P2,P3,P4。

##### 21.4.1.3.20 Load Profile

该模块包括顶级 SQL 语句类型（Top SQL Command Types）。

Top SQL Command Types 显示采样的 SQL 语句类型以及相关信息，来源于 V$ACTIVE\_SESSION\_HISTORY，详见下表。

表21.42 Top SQL Command Types说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| SQL Command Type | SQL 语句类型 | V$ACTIVE\_SESSION\_HISTORY 中 SQL\_OPNAME，对应 WRH$\_ACTIVE\_SESSION\_HISTORY 信息表中的 SQL 语句类型 |
| Distinct SQLIDS | 去重后的 SQL 语句的采样次数 | V$ACTIVE\_SESSION\_HISTORY 中 COUNT(DISTINCT(SQL\_ID))，执行的语句 ID 数量,实现逻辑中进行去重 |
| %Activity | 分组 SQL 语句采样次数/去重后会话数 | V$ACTIVE\_SESSION\_HISTORY 中分组 COUINT(SQL\_ID) /COUNT(DISTINCT(SESSION\_ID) 即分组 SQL 语句采样次数/去重后会话数，报表也根据该值进行排序 |
| Avg Active Sessions | 平均活跃会话数 | V$ACTIVE\_SESSION\_HISTORY 中 COUNT(SQL\_ID)/COUNT(DISTINCT(SESSION\_ID))，即分组 SQLID 数/去重后的会话 ID 数量 |

##### 21.4.1.3.21 Top SQL

该模块包括包括对等待事件顶级占比 SQL 语句（TOP SQL WITH TOP EVENTS）。

TOP SQL WITH TOP EVENTS 显示采样的 SQL 语句及其对应的等待事件的相关信息，来源于 WRH$\_ACTIVE\_SESSION\_HISTORY 以及 WRH$\_SQL\_STAT\_HISTORT 信息表。由于动态视图的采样周期与快照生成周期不一致，故此表仅分析在指定快照范围对应的采样时间的采样数据。每个字段的含义和说明参见下表。

表21.43 Top SQL with Top Events说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| SQL ID | SQL 语句 ID | WRH$\_ACTIVE\_SESSION\_HISTORY 中 SQL\_ID |
| Samples | SQL 语句的采样次数 | WRH$\_ACTIVE\_SESSION\_HISTORY 中 COUNT(SQL\_ID)，限制 EVENT IS NOT NULL,并且是在同一个 EVENT 事件中 |
| %Activity | SQL 语句采样次数对执行总次数的占比 | WRH$\_ACTIVE\_SESSION\_HISTORY 中 COUNT(SQL\_ID) / 快照期间该 SQL\_ID 在 WRH$\_SQL\_STAT\_HISTORY 中的 COUNT(SQL\_ID) 若 WRH$\_SQL\_STAT\_HISTORY 中不存在该 SQL\_ID 则输出‘/’,且 SQL Text 也为‘/’ |
| Event | SQL 语句对应等待事件 | WRH$\_ACTIVE\_SESSION\_HISTORY 中 EVENT |
| Waits | 事件等待时间，单位为微秒 | WRH$\_ACTIVE\_SESSION\_HISTORY 中根据 SQL\_ID,EVENT,SESSION\_ID,SQL\_EXEC\_ID 分组得到 MAX(TIME\_WAITED)，除以 1000 输出，若为 0 则输出‘/’ 报表根据该值进行排序 |
| %Event | 事件等待时间对 DB Time 的占比 | Waits/DB Time 若 DB\_TIME 或 Waits 为 0，输出‘/’ |
| Sql Text | 采样的 SQL 语句 | WRH$\_SQL\_STAT\_HISTORY 中 SQL\_TXT |

##### 21.4.1.3.22 Top Sessions

包括顶级会话（Top Sessions）和顶级阻塞会话（Top Blocking Sessions）。

###### 21.4.1.3.22.1 Top Sessions

显示采样时的会话以及相关信息，数据来源于 DBA\_HIST\_ACTIVE\_SESS\_HISTORY 以及 DBA\_USER 系统视图，通过 USER\_ID 进行连接，限定 SQL\_ID 列所标识的语句为正在执行状态，并且为会话在采样时的等待事件，根据会话 ID，会话序列号，事件名称，用户名称，程序名进行分组，根据每组会话总数进行排序。每个字段说明具体见下表。

表21.44 Top Sessions说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Sid,Serial# | 会话 ID 以及序列号 | DBA\_HIST\_ACTIVE\_SESS\_HISTORY 中的 SESSION\_ID 拼接 SESSION\_SERIAL# |
| %Activity | 会话对总会话占比 | DBA\_HIST\_ACTIVE\_SESS\_HISTORY 中分组的会话数/总会话数 |
| Event | 事件名称 | DBA\_HIST\_ACTIVE\_SESS\_HISTORY 中 EVENT |
| %Event | 事件数对总事件数占比 | DBA\_HIST\_ACTIVE\_SESS\_HISTORY 中按照上述分组后的每组事件数/总事件数 |
| User | 用户名称 | DBA\_USER 中 USERNAME |
| Program | 程序名 | DBA\_HIST\_ACTIVE\_SESS\_HISTORY 中 PROGRAM |
| #Sample Active | 样本活跃度 | ELAPSED 作为起始快照的时间差，若 ELAPSED 为 0 为每组会话数 ’/’ 总会话数\|\| \[0%\] 否则最后拼接的为\[AVG(TIME\_WAITED)/1000000/ELAPSED \* 100 ’%’\] |

###### 21.4.1.3.22.2 Top Blocking Sessions

显示阻塞会话的情况，数据来源于 WRH$\_SESSION\_WAIT\_HISTORY 快照信息表,该表显示所有快照中会话等待时间的历史信息，按照会话 ID 以及事件名称分组,逻辑部分与 Top Sessions 一致，报表根据 %Activity 进行排序。下表为该信息表内容。

表21.45 WRH$\_SESSION\_WAIT\_HISTORY快照信息表说明

| **列名** | **类型** | **说明** |
| --- | --- | --- |
| SNAP\_ID | INTEGER | 快照 ID |
| SQL\_ID | INTEGER | 语句的 SQL ID |
| EVENT# | SMALLINT | 事件编号 |
| EVENT | VARCHAR(32) | 事件名称 |
| TIME\_WAITED\_MICRO | INTEGER | 等待时间（单位：微秒） |
| WAIT\_CLASS# | SMALLINT | 等待事件类别编号 |
| SESSION# | INTEGER | 会话 ID |

##### 21.4.1.3.23 Activity Over Time

显示数据库随时间推移的活动情况，提供了期间活动以及工作负载的信息。将起始快照之间的采样数据，以 2 分钟为一个窗口切割成连续的时间窗口，并且统计每个窗口的活动情况,每个窗口只统计前三项最活跃的事件，数据来源于 WRH$\_ACTIVE\_SESSION\_HISTORY 信息表，详见下表。

表21.46 Activity Over Time说明

| **字段名** | **说明** | **计算值** |
| --- | --- | --- |
| Slot Time | 当前窗口的结束时间 | 每个窗口结束时间由快照对应时间开始逐步加 2mins，若剩余时间不足两分钟，则使用剩余时间作为 slot |
| Slot Count | 窗口期间采样 ID 总数量 | WRH$\_ACTIVE\_SESSION\_HISTORY 中 COUNT(SAMPLE\_ID) |
| Event | 事件名称 | WRH$\_ACTIVE\_SESSION\_HISTORY 中 EVENT |
| Event Count | 会话在采样时的等待事件的数量 | WRH$\_ACTIVE\_SESSION\_HISTORY 中 COUNT(EVENT) WHERE EVENT IS NOT NULL 报表根据该值进行排序 |
| %Event | 在采样时等待事件数量对快照起始间分组采样 ID 总数量的占比 | Event Count / COUNT(SAMPLE\_ID) \* 100 |

### 21.4.2 快照存储说明

快照信息管理表 WRM$\_SNAPSHOT 中 SNAP\_ID 为自增列，默认值为 1，每当新建一个快照该参数就自增“1”。快照信息表为水平分区表，且为范围（Range）分区类型，初始分区为 Part0 不存储信息，分区表均存储于 SYSAUX 表空间上。

分区表均以快照 ID 进行分区，新建快照时会在每个分区表末尾新增新的分区 Parti（i 为变量，Part 为常量），其中 i 为当前快照 ID，同时向 Parti 中插入此快照对应的数据。

暂未提供接口查询指定快照的大小。可以使用系统函数 TABLE\_USED\_SPACE 获取每个水平分区表中指定快照所占用的页大小，如获取 SYS.WRH$\_SESSIONS 表中快照 8 所占用的页大小可执行以下 SQL 语句：

```
SELECT TABLE_USED_SPACE('SYS', 'WRH$_SESSIONS_PART8');
```

执行结果如下：

```
行号    TABLE_USED_SPACE('SYS','WRH$_SESSIONS_PART8')
---------- ---------------------------------------------
1     16
```

### 21.4.3 快照删除说明

目前 AWR 支持四种对快照进行删除的方式：

1. 过期快照定期删除

快照保留时间由快照信息管理表 WRM$\_WR\_CONTROL 中 RETENTION 列决定，RETENTION 列默认为 8 天，可以使用 MODIFY\_SNAPSHOT\_SETTINGS 接口进行修改。每次创建新的快照创建新的分区子表前对当前所有快照进行扫描，找到已过期的快照。

2. 指定快照范围删除

调用接口 DROP\_SNAPSHOT\_RANGE 指定待删除的 LOW\_SNAP\_ID 与 HIGH\_SNAP\_ID 对\[LOW\_SNAP\_ID, HIGH\_SNAP\_ID\]范围内的快照进行删除。

3. 指定快照创建时间删除

调用接口 DROP\_SNAPSHOT\_BY\_TIME 指定待删除的快照创建时间 END\_DT，对快照开始创建时间小于等于 END\_DT 范围内的快照进行删除。

上述删除快照的方式均会将待删除快照存入中间表 SYS.WRM\\\_SNAPSHOT\\\_D，并立即对SYS.WRM\_SNAPSHOT 表中待删除快照的数据进行 DELETE。

每间隔 11min 会对中间表 SYS.WRM\\\_SNAPSHOT\\\_D中存储的快照ID对应的快照信息表中的分区子表进行DROP，且经过系统purge时间后对应空间会真正释放。DROP操作结束后将已删除的快照从中间表SYS.WRM\_SNAPSHOT\_D 中进行 DELETE。

4. 对全部快照进行删除

调用接口 AWR\_CLEAR\_HISTORY，对全部快照信息表先进行 TRUNCATE 操作释放空间，再对表进行 DROP 操作。删除后再执行对全部信息表的重建操作，同时对中间表 SYS.WRM\\\_SNAPSHOT\\\_D与SYS.WRM\_SNAPSHOT 表进行数据清理。

## 21.5 举例说明

用户在使用 DBMS\_WORKLOAD\_REPOSITORY 包之前，需要提前调用系统过程并设置间隔时间：

```
SP_INIT_AWR_SYS(1);
```

下面语句设置间隔为 10 分钟，也可以是其他值：

```
CALL DBMS_WORKLOAD_REPOSITORY.AWR_SET_INTERVAL(10);
```

设置成功后，可以使用 CREATE\_SNAPSHOT 手动创建快照，也可以等待设置的间隔时间后系统自动创建快照，快照 id 从 1 开始递增：

手动创建快照：

```
DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT();
```

查看创建的快照信息，包括快照 id：

```
SELECT * FROM SYS.WRM$_SNAPSHOT;
```

查看 snapshot 的 id 在 1~2 范围内的 AWR 分析报告的带 html 格式的内容。然后复制到文本文件中，保存成 html 格式即可查看。

```
SELECT * FROM TABLE (DBMS_WORKLOAD_REPOSITORY.AWR_REPORT_HTML(1,2));
```

把 snapshot 的 id 在 1~2 范围内的 AWR 分析报告生成到 c 盘 awr1.html 文件。

```
SYS.AWR_REPORT_HTML(1,2,'C:\','AWR1.HTML');
```

通过 DBMS\_WORKLOAD\_REPOSITORY 包还可以对快照本身做增删改操作。

例 1 删除 id 在 22~32 之间的 snapshot，并立即释放相应分区表空间。

```
CALL DBMS_WORKLOAD_REPOSITORY.DROP_SNAPSHOT_RANGE(22,32,NULL,TRUE);
```

例 2 删除“2023-11-17 17:01:29.488000”时间点之前创建的所有 snapshot，并立即释放相应分区表空间。

```
CALL DBMS_WORKLOAD_REPOSITORY.DROP_SNAPSHOT_BY_TIME('2023-11-17 17:01:29.488000', TRUE);
```

例 3 修改 snapshot 的间隔时间为 30 分钟、保留时间为 1 天。

```
CALL DBMS_WORKLOAD_REPOSITORY.MODIFY_SNAPSHOT_SETTINGS(1440,30);
```

查询设置后快照参数。

```
SELECT * FROM SYS.WRM$_WR_CONTROL;
```

例 4 创建一次 snapshot。

```
CALL DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT();
```

例 5 清理全部 snapshot。

```
CALL DBMS_WORKLOAD_REPOSITORY.AWR_CLEAR_HISTORY();
```

例 6 设置 snapshot 的间隔为 10 分钟。

```
CALL DBMS_WORKLOAD_REPOSITORY.AWR_SET_INTERVAL(10);
```

例 7 手动清理创建快照时产生的中间表。

```
CALL DBMS_WORKLOAD_REPOSITORY.AWR_CLEAR_TMP_TABLE();
```

例 8 执行下述语句，将 SNAPSHOT 的 ID 在 1~2 范围内的 ASH 分析报告生成到/home/test 路径下的 ash\_test.html 文件中。

```
CALL SYS.ASH_REPORT_HTML(1,2, '/home/test', 'ash_test.html');
```
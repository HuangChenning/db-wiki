---
title: "DBMS_SPACE 包"
book: "DM8 系统包使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dbms_space-package.html
tags:
  - dameng
  - dm8
  - system-packages
---

为了展示所有物理对象（文件、页）和逻辑对象（表空间、簇、段）的存储空间信息。通过 DBMS\_SPACE 包来获取表空间、文件、页、簇、段的内容。DM DPC 环境下不支持 DBMS\_SPACE 包。

## 16.1 数据类型

DBMS\_SPACE 包中涉及到的变量和记录类型。如下统一说明：

| **包内变量和记录类型** | **解释** |
| --- | --- |
| TS\_T | 表空间记录类型，用于记录表空间的信息 |
| TS\_ARR\_T | 表空间记录类型数组 |
| TS\_ALL\_ARR\_T | 表空间 ID 数组 |
| FILE\_T | 文件记录类型，用于记录文件的信息 |
| FILE\_ARR\_T | 文件记录类型数组 |
| FILE\_ALL\_ARR\_T | 文件的 ID 数组 |
| SEG\_T | 段记录类型，用于记录段的信息 |
| SEG\_ARR\_T | 段记录类型数组 |
| SEG\_ID\_ARR\_T | 段 ID 数组 |
| EXTENT\_T | 簇记录类型，用于记录簇的信息 |
| EXTENT\_ARR\_T | 簇记录类型数组 |
| EXTENT\_SIZE | 簇的大小（页为单位） |
| PAGE\_ADDR\_T | 页地址记录类型，用于记录页地址的信息 |
| PAGE\_ADDR\_ARR\_T | 页地址记录类型数组 |
| PAGE\_N | 描述页能描述的页数 |

下面为 DBMS\_SPACE 包中记录类型的具体定义：

1. TS\_T

TS\_T 为表空间记录类型，用于记录表空间的信息，具体数据信息来源于 V$TABLESPACE，类型定义如下：

```
TYPE TS_T IS RECORD(
    ID             INT,
    NAME        VARCHAR(128),
    CACHE       VARCHAR(20),
    TYPE        TINYINT, 
    STATUS      TINYINT,
    MAX_SIZE    BIGINT, 
    TOTAL_SIZE  BIGINT,
    FILE_NUM    SMALLINT 
);
```

**参数详解**

- ID
	表空间 ID。
- NAME
	表空间名称。
- CACHE
	缓冲区名。
- TYPE
	表空间类型，1：DB 类型，2：临时表空间。
- STATUS
	表空间状态。0：ONLINE；1：OFFLINE；2：RES\_OFFLINE；3：CORRUPT。
- MAX\_SIZE
	表空间的最大大小，以页为单位。0 代表只受操作系统限制（暂无实际意义）。
- TOTAL\_SIZE
	表空间的总大小，以页为单位。
- FILE\_NUM
	包含的文件数。
2. TS\_ARR\_T

TS\_ARR\_T 为表空间记录类型数组，类型定义如下：

```
TYPE TS_ARR_T IS ARRAY TS_T[];
```
3. TS\_ALL\_ARR\_T

TS\_ALL\_ARR\_T 为表空间 ID 数组，类型定义如下：

```
TYPE TS_ALL_ARR_T IS ARRAY INT[];
```
4. FILE\_T

FILE\_T 为文件记录类型，用于记录文件的信息，具体数据信息来源于 V$DATAFILE，类型定义如下：

```
TYPE FILE_T IS RECORD(
    PATH                   VARCHAR(256), 
    CREATE_TIME            TIMESTAMP,
    MODIFY_TIME              TIMESTAMP, 
    TOTAL_SIZE                BIGINT, 
    FREE_SIZE               BIGINT, 
    FREE_PAGE_NO           BIGINT, 
    PAGE_SIZE                INT, 
    AUTOEXTEND             INT,
    MAX_SIZE               INT,
    NEXT_SIZE              INT 
);
```

**参数详解**

- PATH
	数据库文件路径。
- CREATE\_TIME
	数据库文件创建时间。
- MODIFY\_TIME
	文件修改的时间。
- TOTAL\_SIZE
	文件的总大小，以页为单位。
- FREE\_SIZE
	未分配的空闲大小，以页为单位。
- FREE\_PAGE\_NO
	数据文件中连续空白页的起始页号。
- PAGE\_SIZE
	页大小，单位 BYTE。
- AUTOEXTEND
	是否支持自动扩展，1：支持；0：不支持。
- MAX\_SIZE
	文件最大大小，以 MB 为单位。
- NEXT\_SIZE
	文件每次扩展大小，以 MB 为单位。创建文件时没有指定则返回 0。
5. FILE\_ARR\_T

FILE\_ARR\_T 为文件记录类型数组，类型定义如下：

```
TYPE FILE_ARR_T IS ARRAY FILE_T[];
```
6. FILE\_ALL\_ARR\_T

FILE\_ALL\_ARR\_T 为文件的 ID 数组，类型定义如下：

```
TYPE FILE_ALL_ARR_T IS ARRAY INT[];
```
7. SEG\_T

SEG\_T 为段记录类型，用于记录段的信息，类型定义如下：

```
TYPE SEG_T IS RECORD(
    SEGID                 INT,
    INODE_FILE_ID       SMALLINT,     
    INODE_PAGE_NO       INT, 
    INODE_OFFSET       SMALLINT, 
    N_FULL_EXTENT        INT, 
    N_FRAG_EXTENT       INT, 
    N_FREE_EXTENT       INT,
    N_USED_IN_FRAG     INT
);
```

**参数详解**

- SEG\_ID
	段 ID。
- INODE\_FILE\_ID
	段 INODE 项所在的文件 ID。
- INODE\_PAGE\_NO
	段 INODE 项所在的页号。
- INODE\_OFFSET
	段 INODE 项的页偏移。
- N\_FULL\_EXTENT
	全满簇的个数。
- N\_FRAG\_EXTENT
	半满簇的个数。
- N\_FREE\_EXTENT
	空闲簇的个数。
- N\_USED\_IN\_FRAG
	半满簇中使用页的总数量。
8. SEG\_ARR\_T

SEG\_ARR\_T 为段记录类型数组，类型定义如下：

```
TYPE SEG_ARR_T IS ARRAY SEG_T[];
```
9. SEG\_ID\_ARR\_T

SEG\_ID\_ARR\_T 为段 ID 数组，类型定义如下：

```
TYPE SEG_ID_ARR_T IS ARRAY INT[];
```
10. EXTENT\_T

EXTENT\_T 为簇记录类型，用于记录簇的信息，类型定义如下：

```
TYPE EXTENT_T IS RECORD(
    TSID                  SMALLINT,
    SEGID                 INT,
    STATE                   VARCHAR(5),
    BITMAP                VARCHAR(64), 
    EXTENT_FILE_ID        SMALLINT,
    EXTENT_PAGE_NO        INT,
    EXTENT_OFFSET         SMALLINT,
    FIRST_PAGE_NO         INT,
    LAST_PAGE_NO          INT, 
    NEXT_LINK_FILE_ID     SMALLINT, 
    NEXT_LINK_PAGE_NO     INT, 
    NEXT_LINK_OFFSET      SMALLINT
);
```

**参数详解**

- TS\_ID
	表空间 ID。
- SEG\_ID
	段 ID。
- STATE
	簇状态，NOUSE：未使用；FULL：全满；FRAG：半满；FREE：空闲；Unknown：未知。
- BITMAP
	簇的页标记位图。
- EXTENT\_FILE\_ID
	簇描述项的文件 ID。
- EXTENT\_PAGE\_NO
	簇描述项所在页号。
- EXTENT\_OFFSET
	簇描述项的页偏移。
- FIRST\_PAGE\_NO
	簇的起始页号。
- LAST\_PAGE\_NO
	簇的终止页号。
- NEXT\_LINK\_FILE\_ID
	下一个簇描述项的文件号 ID。
- NEXT\_LINK\_PAGE\_NO
	下一个簇描述项的页号。
- NEXT\_LINK\_OFFSET
	下一个簇描述项的页偏移。
11. EXTENT\_ARR\_T

EXTENT\_ARR\_T 为簇记录类型数组，类型定义如下：

```
TYPE EXTENT_ARR_T IS ARRAY EXTENT_T[];
```
12. PAGE\_ADDR\_T

PAGE\_ADDR\_T 为页记录类型，用于记录页的信息，类型定义如下：

```
TYPE PAGE_ADDR_T IS RECORD(
    TS_ID                  SMALLINT,
    FILE_ID                   SMALLINT, 
    PAGE_NO                INT 
);
```

**参数详解**

- TS\_ID
	页所在的表空间 ID。
- FILE\_ID
	页所在的文件 ID。
- PAGE\_NO
	页号。
13. PAGE\_ADDR\_ARR\_T

PAGE\_ADDR\_ARR\_T 为页记录类型数组，类型定义如下：

```
TYPE PAGE_ADDR_ARR_T IS ARRAY PAGE_ADDR_T[];
```

## 16.2 相关方法

DBMS\_SPACE 包中包含的过程和函数如下详细介绍：

1. TS\_LOAD/ TS\_GET

根据输入的表空间 id，获得表空间信息。过程和函数功能相同。

**语法如下：**

```
PROCEDURE TS_LOAD(
    TS_ID        IN        SMALLINT, 
    TS_ARR        OUT        TS_ARR_T
);
```

**语法如下：**

```
FUNCTION  TS_GET (
    TS_ID        IN        SMALLINT
)RETURN TS_ARR_T;
```

**参数详解**

- TS\_ID
	表空间 id。
- TS\_ARR\_T
	表空间记录类型数组。
2. TS\_N\_LOAD / TS\_N\_GET

获得数据库中表空间的个数。过程和函数功能相同。

**语法如下：**

```
PROCEDURE TS_N_LOAD(
    NUMBER        OUT        INT
);
```

**语法如下：**

```
FUNCTION TS_N_GET 
RETURN INT;
```

**参数详解**

- NUMBER
	表空间的个数。
3. TS\_ALL\_LOAD/ TS\_ALL\_GET

获得所有表空间的 ID。过程和函数功能相同。

**语法如下：**

```
PROCEDURE TS_ALL_LOAD(
    TS_ALL_ARR    OUT        TS_ALL_ARR_T,
    OFFSET        IN        INT        DEFAULT 1,
    NUM            IN        INT        DEFAULT 100
);
```

**语法如下：**

```
FUNCTION TS_ALL_GET(
    OFFSET        IN        INT        DEFAULT 1,
    NUM            IN        INT        DEFAULT 100
) RETURN TS_ALL_ARR_T;
```

**参数详解**

- OFFSET
	数组起始位置。
- NUM
	数组长度
- TS\_ALL\_ARR
	表空间 ID 数组
4. FILE\_LOAD/ FILE\_GET

根据输入的表空间 id、文件 id，获得文件信息。过程和函数功能相同。

**语法如下：**

```
PROCEDURE FILE_LOAD(
    TS_ID        IN        SMALLINT,
    FILE_ID        IN        SMALLINT, 
    FILE_ARR    OUT        FILE_ARR_T
);
```

**语法如下：**

```
FUNCTION FILE_GET(
    TS_ID        IN        SMALLINT, 
    FILE_ID        IN        SMALLINT
) RETURN FILE_ARR_T;
```

**参数详解**

- TS\_ID
	表空间 id。
- FILE\_ID
	文件号。
- FILL\_ARR
	文件记录类型数组。
5. FILE\_ALL\_LOAD/ FILE\_ALL\_GET

获得所有文件的 ID。过程和函数功能相同。

**语法如下：**

```
PROCEDURE FILE_ALL_LOAD(
    TS_ID            IN        SMALLINT, 
    FILE_ALL_ARR    OUT        FILE_ALL_ARR_T, 
    OFFSET            IN        INT        DEFAULT 1, 
    NUM                IN        INT        DEFAULT 100
);
```

**语法如下：**

```
FUNCTION FILE_ALL_GET(
    TS_ID        IN        SMALLINT, 
    OFFSET        IN        INT        DEFAULT 1,
    NUM            IN        INT        DEFAULT 100
)RETURN FILE_ALL_ARR_T;
```

**参数详解**

- TS\_ID
	表空间 id。
- FILE\_ALL\_ARR
	文件的 ID 数组。
- OFFSET
	数组起始位置。
- NUM
	数组的长度。
6. SEG\_LOAD\_BY\_ID/SEG\_GET\_BY\_ID

根据输入的表空间 id、段号获得段信息。过程和函数功能相同。

**语法如下：**

```
PROCEDURE SEG_LOAD_BY_ID(
    TS_ID        IN        SMALLINT, 
    SEG_ID        IN        INT, 
    SEG_INFO    OUT        SEG_T
);
```

**语法如下：**

```
FUNCTION SEG_GET_BY_ID(
    TS_ID        IN        SMALLINT,
    SEG_ID        IN        INT
)RETURN SEG_T;
```

**参数详解**

- TS\_ID
	表空间 id。
- SEG\_ID
	段号。
- SEG\_INFO
	段的信息。
7. SEG\_LOAD\_BY\_HEADER/ SEG\_GET\_BY\_HEADER

根据输入的表空间 id、段头的文件号、页号、页内偏移，获得段信息，其中页内偏移取值只能为 62 或 72。过程和函数功能相同。

**语法如下：**

```
PROCEDURE SEG_LOAD_BY_HEADER(
    TS_ID                IN        SMALLINT, 
    HEADER_FILE_ID        IN        SMALLINT, 
    HEADER_PAGE_NO        IN        INT,
    HEADER_OFFSET         IN         SMALLINT, 
    SEG_INFO              OUT     SEG_T
);
```

**语法如下：**

```
FUNCTION SEG_GET_BY_HEADER(
    TS_ID                 IN         SMALLINT, 
    HEADER_FILE_ID         IN         SMALLINT, 
    HEADER_PAGE_NO         IN         INT, 
    HEADER_OFFSET         IN         SMALLINT
)RETURN SEG_T;
```

**参数详解**

- TS\_ID
	表空间 id。
- HEADER\_FILE\_ID
	段头文件号。
- HEADER\_PAGE\_NO
	段头页号。
- HEADER\_OFFSET
	段头偏移量。
- SEG\_INFO
	段的信息。
8. SEG\_ALL\_LOAD/SEG\_ALL\_GET

根据表空间 id、数组相对起始位置、数组长度，获得数据库中表空间中所有段的 id 信息。过程和函数功能相同。

**语法如下：**

```
PROCEDURE SEG_ALL_LOAD(
    TS_ID             IN          SMALLINT, 
    SEG_ID_ARR         OUT         SEG_ID_ARR_T,
    OFFSET             IN         INT         DEFAULT 1,
    NUM                 IN         INT         DEFAULT 100
);
```

**语法如下：**

```
FUNCTION SEG_ALL_GET(
    TS_ID              IN          SMALLINT,
    OFFSET             IN          INT         DEFAULT 1, 
    NUM                   IN          INT         DEFAULT 100   
)RETURN SEG_ID_ARR_T;
```

**参数详解**

- TS\_ID
	表空间 ID。
- OFFSET
	数组起始位置。
- NUM
	数组长度。
- SEG\_ID\_ARR
	段 ID 信息。
9. SEG\_EXTENT\_LST\_LOAD/ SEG\_EXTENT\_LST\_GET

根据输入的表空间 id、段号、链表类型、链表方向、链表相对起始位置、指定链表长度，获得 FULL、FREE 或 FRAG 链表的信息。过程和函数功能相同。

**语法如下：**

```
PROCEDURE SEG_EXTENT_LST_LOAD(
    TS_ID              IN          SMALLINT, 
    SEG_ID             IN             INT,
    EXTENT_ARR         OUT         EXTENT_ARR_T, 
    LINKTYPE         IN          VARCHAR(5)         DEFAULT 'FULL',
    DIRECT             IN          VARCHAR(10)     DEFAULT 'FORWARD', 
    OFFSET             IN          INT             DEFAULT 1,
    NUM             IN          INT             DEFAULT 100
);
```

**语法如下：**

```
FUNCTION SEG_EXTENT_LST_GET(
    TS_ID           IN          SMALLINT, 
    SEG_ID             IN          INT, 
    LINKTYPE          IN           VARCHAR(5)         DEFAULT 'FULL',
    DIRECT             IN          VARCHAR(10)     DEFAULT 'FORWARD',
    OFFSET          IN           INT             DEFAULT 1,
    NUM             IN           INT             DEFAULT 100,
) RETURN EXTENT_ARR_T;
```

**参数详解**

- TS\_ID
	表空间 id。
- SEG\_ID
	段 id。
- LINKTYPE
	链表类型。
- DIRECT
	链表方向。
- OFFSET
	链表相对起始位置。
- NUM
	指定链表长度。
- EXTENT\_ARR
	簇信息结构体链表
10. EXTENT\_SIZE\_LOAD/ EXTENT\_SIZE\_GET

获得簇的大小（页为单位）。过程和函数功能相同。

**语法如下：**

```
PROCEDURE EXTENT_SIZE_LOAD(
    EXTENT_SIZE     OUT         INT
);
```

**语法如下：**

```
FUNCTION  EXTENT_SIZE_GET  RETURN INT;
```

**参数详解**

- EXTENT\_SIZE
	簇的大小。
11. EXTENT\_XDESC\_PAGE\_NO\_LOAD/EXTENT\_XDESC\_PAGE\_NO\_GET

根据输入的表空间 id、文件 id，获得所有簇描述页的信息。过程和函数功能相同。

**语法如下：**

```
PROCEDURE EXTENT_XDESC_PAGE_NO_LOAD(
    TS_ID                     IN   SMALLINT, 
    FILE_ID                 IN   SMALLINT, 
    XPAGE_ADDR_ARR     OUT     PAGE_ADDR_ARR_T,
    OFFSET                     IN   INT         DEFAULT 1, 
    NUM                      IN   INT         DEFAULT 100  
);
```

**语法如下：**

```
FUNCTION EXTENT_XDESC_PAGE_NO_GET(
    TS_ID           IN       SMALLINT,
    FILE_ID           IN       SMALLINT,
    OFFSET          IN       INT         DEFAULT 1,
    NUM                IN       INT         DEFAULT 100
)RETURN PAGE_ADDR_ARR_T;
```

**参数详解**

- TS\_ID
	表空间 id。
- FILE\_ID
	文件 id。
- OFFSET
	数组的起始位置。
- NUM
	指定输出的长度。
- XPAGE\_ADDR\_ARR
	页地址记录类型数组。
12. PAGE\_N\_LOAD/ PAGE\_N\_GET

获得一个描述页能描述的页数。过程和函数功能相同。

**语法如下：**

```
PROCEDURE PAGE_N_LOAD(
    PAGE_N         OUT         INT
);
```

**语法如下：**

```
FUNCTION PAGE_N_GET
RETURN INT;
```

**参数详解**

- PAGE\_N
	描述页能描述的页数。
13. IPAGE\_NO\_ALL\_LOAD/ IPAGE\_NO\_ALL\_GET

输入表空间 id、inode 页链表类型（FULL 或 FREE）、链表方向、链表相对起始位置、指定链表长度，输出所有 inode 页的页号。过程和函数功能相同。

**语法如下：**

```
PROCEDURE IPAGE_NO_ALL_LOAD(
    TS_ID              IN      SMALLINT,
    PAGE_ADDR_ARR     OUT     PAGE_ADDR_ARR_T ,
    LINKTYPE          IN         VARCHAR(5)         DEFAULT 'FULL', 
    DIRECT             IN         VARCHAR(10)     DEFAULT 'FORWARD', 
    OFFSET             IN         INT             DEFAULT 1, 
    NUM             IN         INT             DEFAULT 100 
);
```

**语法如下：**

```
FUNCTION IPAGE_NO_ALL_GET(
    TS_ID              IN      SMALLINT,
    LINKTYPE          IN        VARCHAR(5)         DEFAULT 'FULL', 
    DIRECT             IN         VARCHAR(10)     DEFAULT 'FORWARD', 
    OFFSET             IN         INT             DEFAULT 1, 
    NUM             IN         INT             DEFAULT 100
)RETURN PAGE_ADDR_ARR_T;
```

**参数详解**

- TS\_ID
	表空间 id。
- PAGE\_ADDR\_ARR
	页地址记录类型数组。
- LINKTYPE
	页链表类型：full 或 free。
- DIRECT
	链表的方向。
- OFFSET
	链表的相对起始位置。
- NUM
	指定链表长度。

## 16.3 举例说明

使用包内的过程和函数之前，如果还未创建过系统包，请先调用系统过程创建系统包。

```
SP_CREATE_SYSTEM_PACKAGES(1,'DBMS_SPACE');
SET SERVEROUTPUT ON;  //PRINT需要设置这条语句，才能打印出消息
```

例 1 获取表空间信息（表空间 ID、表空间名、表空间类型：1 DB 类型，2 临时文件组、表空间状态、表空间的最大空间、表空间的总大小（页）、包含文件的个数）。

```
DECLARE
    TS_INFO DBMS_SPACE.TS_ARR_T;
 BEGIN
    TS_INFO = DBMS_SPACE.TS_GET(4);
    IF TS_INFO IS NOT NULL
 THEN
        SELECT * FROM ARRAY TS_INFO;
 ELSE PRINT 'TABLESPACE IS NULL';
 END IF;
END;
/
```

结果如下：

```
行号 ID NAME CACHE TYPE STATUS MAX_SIZE TOTAL_SIZE FILE_NUM
---------- ---------- ---- ----- ---------- ---------- -------------------
1   4   MAIN  1   0      0               16384       1
```

例 2 获得数据库中表空间的个数

```
DECLARE
TS_NUM INT;
BEGIN
TS_NUM = DBMS_SPACE.TS_N_GET;
PRINT 'TS_NUM:';
PRINT TS_NUM;
END;
/
```

结果如下：

```
TS_NUM:
5  //个数根据实际表空间个数不同而不同
```

例 3 获得文件信息（文件路径、文件创建时间、文件修改的时间、文件的总大小（MB）、文件的空闲大小（MB）、数据文件中连续空白页的起始页号、页大小（KB）、文件可扩展标记、文件最大大小（MB）、文件每次扩展大小（MB））

```
DECLARE
    FILE_INFO DBMS_SPACE.FILE_ARR_T;
BEGIN
    FILE_INFO = DBMS_SPACE.FILE_GET(4,0);
    IF FILE_INFO IS NOT NULL
    THEN
        SELECT * FROM ARRAY FILE_INFO;
    ELSE PRINT 'FILE IS NULL';
    END IF;
END;
/
```

结果如下：

```
行号 PATH CREATE_TIME MODIFY_TIME TOTAL_SIZE FREE_SIZE FREE_PAGE_NO PAGE_SIZE
AUTOEXTEND MAX_SIZE NEXT_SIZE
--------- ------------------------------- --------------------------
1 d:\database0718\DAMENG\MAIN.DBF 2012-07-19 09:47:55.000000 2012-08-07
09:43:33.000000 16384 16348 368 8192 1 0 0
```
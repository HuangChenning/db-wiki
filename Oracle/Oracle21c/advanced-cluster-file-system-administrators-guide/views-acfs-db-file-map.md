---
title: "Administrator's Guide"
book: "Advanced Cluster File System Administrator's Guide"
doc_id: F30297-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/acfsg/views-acfs-db-file-map.html
tags:
  - oracle
  - 21c
  - advanced-cluster-file-system-administrators-guide
---

Oracle ACFS supports Oracle Database file mapping views to the Oracle ASM device level.

Note:

This feature is available starting with Oracle Database 12c Release 1 (12.1.0.2).

The following database mapping views are supported by Oracle ACFS:

- `V$MAP_FILE`
- `V$MAP_FILE_EXTENT`
- `V$MAP_ELEMENT`
- `V$MAP_FILE_IO_STACK`

These `V$MAP` views are only refreshed by executing the procedure `DBMS_STORAGE_MAP.MAP_ALL`. The Oracle ACFS file mapping interface does not utilize the external `fmputl` process or its supporting libraries.

Note:

Oracle ACFS does not provide support for the `V$MAP_SUBELEMENT` view.

Before running any queries on the `V$MAP` views, ensure that the `FILE_MAPPING` initialization is set to `TRUE`, then run the `DBMS_STORAGE_MAP.MAP_ALL` procedure to build the mapping information for the entire I/O subsystem associated with the database. For example, connect as `SYSDBA` to the database instance and run the following:

```
SQL> ALTER SYSTEM SET file_mapping=true;

SQL> EXEC DBMS_STORAGE_MAP.MAP_ALL(10000);
```

The SQL statements in Example 2-12 to Example 2-15 are run from the Oracle Database instance.

Example 2-12 Viewing Oracle ASM information with V$MAP\_ELEMENT

This example displays information from the `V$MAP_ELEMENT` view.

```
SQL> SELECT ELEM_NAME, ELEM_IDX, ELEM_TYPE, ELEM_SIZE, ELEM_DESCR 
       FROM V$MAP_ELEMENT;

ELEM_NAME      ELEM_IDX ELEM_TYPE   ELEM_SIZE ELEM_DESCR
------------ ---------- ---------- ---------- -----------------
+/dev/xvdd1           0 ASMDISK     117184512 TEST_0001
+/dev/xvdc1           1 ASMDISK     117184512 TEST_0000
```

Example 2-13 Viewing Oracle ACFS Data File Information with V$MAP\_FILE

This example displays information from the `V$MAP_FILE` view.

```
SQL> SELECT FILE_NAME, FILE_MAP_IDX, FILE_TYPE, FILE_STRUCTURE, FILE_SIZE, 
      FILE_NEXTS FROM V$MAP_FILE WHERE REGEXP_LIKE(FILE_NAME, '*users01.dbf');

FILE_NAME                 FILE_MAP_IDX FILE_TYPE FILE_STRU FILE_SIZE FILE_NEXTS
------------------------- ------------ --------- --------- --------- ----------
/dbdata1/orcl/users01.dbf            4 DATAFILE  FILE          10256         41
```

Example 2-14 Viewing Element and File Offset Information with V$MAP\_FILE\_EXTENT

This example displays the element offset versus file offset information for each extent with `V$MAP_FILE_EXTENT`, specifying `FILE_MAP_IDX` equal to `4`, which is the file map index of the `/dbdata/orcl/users01.dbf` file.

```
SQL> SELECT FILE_MAP_IDX, EXT_NUM, EXT_ELEM_OFF, EXT_SIZE, EXT_FILE_OFF, 
       EXT_TYPE, ELEM_IDX FROM V$MAP_FILE_EXTENT WHERE FILE_MAP_IDX=4; 

FILE_MAP_IDX    EXT_NUM EXT_ELEM_OFF   EXT_SIZE EXT_FILE_OFF EXT_TY   ELEM_IDX
------------ ---------- ------------ ---------- ------------ ------ ----------
           4          0     58105664        192            0 DATA            0
           4          1     58154752        256          192 DATA            1
           4          2     58089472        256          448 DATA            0
...
           4         39     58140928        256         9920 DATA            1
           4         40     58108160         88        10176 DATA            0
41 rows selected.
```

Example 2-15 Viewing Extent Information With V$MAP\_FILE\_IO\_STACK

This example displays information from `V$MAP_FILE_IO_STACK` specifying `FILE_MAP_IDX` equal to `4`. The `V$MAP_FILE_IO_STACK` view is similar to `V$MAP_FILE_EXTENT`, but the display groups contiguous extents which are on the same device or element and of the same size.

```
SQL> SELECT FILE_MAP_IDX, ELEM_IDX, CU_SIZE,STRIDE, NUM_CU,ELEM_OFFSET, 
       FILE_OFFSET FROM V$MAP_FILE_IO_STACK WHERE FILE_MAP_IDX=4;

FILE_MAP_IDX   ELEM_IDX    CU_SIZE     STRIDE     NUM_CU ELEM_OFFSET FILE_OFFSET
------------ ---------- ---------- ---------- ---------- ----------- -----------
           4          0        256       1024         10    58089472 448
           4          0        192          0          1    58105664 0
           4          0        256       1024          9    58105856 960
           4          0         88          0          1    58108160 10176
           4          1        256       1024         10    58138624 704
           4          1        256       1024         10    58154752 192

6 rows selected.
```

See Also:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-346E8F7D-2A29-44D2-A47A-BE5A8032284C) for information about file mapping to Oracle ASM files
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=ADMIN-GUID-17690011-5226-4F9A-BF59-73B2A76CF4C1) for information about the Oracle Database File Mapping Interface
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=REFRN-GUID-B200B2D6-08D4-49B0-9FD9-8AF6AED37202) for details about the `V$MAP` views
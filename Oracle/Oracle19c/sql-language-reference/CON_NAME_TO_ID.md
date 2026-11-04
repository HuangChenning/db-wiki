---
title: CON_NAME_TO_ID
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CON_NAME_TO_ID.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

![con_name_to_id](img/con_name_to_id.gif)

> ```
> CON_NAME_TO_ID(container_name)
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration con\_name\_to\_id.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/con_name_to_id.html)

## Purpose

`CON_NAME_TO_ID` takes as its argument a container name and returns the container ID. For *container\_name*, specify a string, or an expression that resolves to a string, in any data type. The function returns a `NUMBER` value.

This function is useful in a multitenant container database (CDB). If you use this function in a non-CDB, then it returns 0.

## Example

The following query displays the ID and name for all containers in a CDB. The sample output shown is for the purpose of this example.

```md
SELECT CON_ID, NAME
  FROM V$CONTAINERS;

    CON_ID NAME
---------- ----------
         1 CDB$ROOT
         2 PDB$SEED
         4 SALESPDB
```

The following statement returns the ID for the container named `SALESPDB`:

```md
SELECT CON_NAME_TO_ID('SALESPDB') "Container ID"
  FROM DUAL;

Container ID
------------
           4
```
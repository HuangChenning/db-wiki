---
title: DBMS_QOPATCH
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_QOPATCH.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `DBMS_QOPATCH` package provides an interface to view the installed database patches.

This chapter contains the following topics:

### DBMS\_QOPATCH Overview

The `DBMS_QOPATCH` package provides a PLSQL/SQL interface to view the installed database patches. The interface provides all the patch information available as part of the `OPATCH LSINVENTORY -XML` command. The package accesses the OUI patch inventory in real time to provide patch and meta-information.

### DBMS\_QOPATCH Security Model

The `DBMS_QOPATCH` package is created as part of SYS schema and SYS is the only user who can execute these subprograms.

### DBMS\_QOPATCH Operational Notes

The following operational notes apply to DBMS\_QOPATCH.

- The package will work only if the database is `OPEN`.
- In an Oracle Real Application Clusters (RAC) environment, if the subprogram requires to fetch data from other RAC nodes it spawns a job in the other node(s) to get the data. In this case `JOB_QUEUE_PROCESSES` needs to be `>0` for the package to fetch the data from other RAC nodes.
- If there is a delay in the job execution, the package returns `ORA-20008` error.

### DBMS\_QOPATCH Exceptions

This table lists the exceptions raised by the `DBMS_QOPATCH` package.

Table 1 DBMS\_QOPATCH Error Messages

| Error Code | Description |
| --- | --- |
| `ORA-20001` | Latest XML inventory is not loaded into table. |
| `ORA-20002` | Directory creation failed. |
| `ORA-20003` | Configuration of a job on a node failed. |
| `ORA-20004` | Job configuration failed as node is inactive. |
| `ORA-20005` | Job is not configured with given node, instance name. |
| `ORA-20006` | Number of RAC active instances and opatch jobs configured are not same. |
| `ORA-20007` | Job configuration failed as node or instance is not active. |
| `ORA-20008` | Timed out - job execution time is more than 120Secs. |
| `ORA-20009` | Job execution failed. |
| `ORA-20010` | Node is inactive and job cannot be executed. |
| `ORA-20011` | Job name is `NULL` and inventory cannot be loaded. |
| `ORA-20012` | `JOB_QUEUE_PROCESSES` is set to zero and the inventory cannot be loaded. |
| `ORA-20013` | `DBMS_QOPATCH` ran mostly in non-install area. |
| `ORA-20014` | Database is not opened. |
| `ORA-20015` | Database opened as read-only. |

### Summary of DBMS\_QOPATCH Subprograms

This table lists and briefly describes the `DBMS_QOPATCH` package subprograms.

Table 2 DBMS\_QOPATCH Package Subprograms

| Subprogram | Description |
| --- | --- |
| CHECK\_PATCH\_INSTALLED Function | Checks if a patch is installed. |
| GET\_OPATCH\_BUGS Function | Provides a bugs list for a patch in XML format if the patch number is given. If patch is not given then it lists all the bugs installed in all the patches in XML format. |
| GET\_OPATCH\_COUNT Function | Provides the total number of installed patches in XML format |
| GET\_OPATCH\_DATA Function | Provides top level patch information for the patch (such as Patch ID, patch creation time) in the XML element |
| GET\_OPATCH\_FILES Function | Provides the list of files modified in the given patch number in XML format |
| GET\_OPATCH\_INSTALL\_INFO Function | Returns the XML element containing the `ORACLE_HOME` details such as patch and inventory location |
| GET\_OPATCH\_LIST Function | Provides list of patches installed as an XML element from the XML inventory |
| GET\_OPATCH\_LSINVENTORY | Returns whole opatch inventory as XML instance document. |
| GET\_OPATCH\_OLAYS Function | Provides overlay patches for a given patch as XML element |
| GET\_OPATCH\_PREQS Function | Provides prerequisite patches for a given patch as XML element |
| GET\_OPATCH\_XSLT | Returns the style-sheet for the opatch XML inventory presentation |
| GET\_PATCH\_DETAILS Function | Displays the detailed patch information from `opatch lsinventory`. |
| GET\_SQLPATCH\_STATUS Procedure | Displays the SQL patch status by querying from SQL patch registry to produce complete patch level information |
| IS\_PATCH\_INSTALLED Function | Provides information (such as patchID, application date, and SQL patch information) on the installed patch as XML node by querying the XML inventory |
| OPATCH\_COMPARE\_CURRENT Function | Compares the current database with a list of bugs. |
| OPATCH\_COMPARE\_NODES Function | Compares the given RAC node(s) with the instance to the present connected node with current node. The return value indicates whether the data was refreshed or not. |
| SET\_CURRENT\_OPINST Procedure | Sets the node name and instance to get the inventory details specific to it in an Oracle Real Application Clusters (RAC) environment |

### CHECK\_PATCH\_INSTALLED Function

Checks if the patch is installed.

**Syntax**

```md
DBMS_QOPATCH.CHECK_PATCH_INSTALLED (
   bugs     IN QOPATCH_LIST);
 RETURN VARCHAR2;
```

**Parameters**

Table 3 CHECK\_PATCH\_INSTALLED Parameters

| Parameter | Description |
| --- | --- |
| `bugs` | List of patches to be checked. |

### GET\_OPATCH\_BUGS Function

This function provides a bugs list in a patch if the patch number is given. If a patch number is not given, it lists all the bugs in the specified XML format.

**Syntax**

```md
DBMS_QOPATCH.GET_OPATCH_BUGS (
   patchnum IN VARCHAR2 DEFAULT NULL);
 RETURN XMLTYPE;
```

**Parameters**

Table 4 GET\_OPATCH\_BUGS Function Parameters

| Parameter | Description |
| --- | --- |
| `patchnum` | Patch number |

### GET\_OPATCH\_COUNT Function

This function provides the total number of installed patches in XML format.

**Syntax**

```md
DBMS_QOPATCH.GET_OPATCH_COUNT (
   patchnum IN VARCHAR2);
 RETURN XMLTYPE;
```

**Parameters**

Table 5 GET\_OPATCH\_COUNT Function Parameters

| Parameter | Description |
| --- | --- |
| `patchnum` | Patch number |

### GET\_OPATCH\_DATA Function

This function provides top level patch information for the patch (such as Patch ID, patch creation time) in the XML element.

**Syntax**

```md
DBMS_QOPATCH.GET_OPATCH_DATA (
   patchnum IN VARCHAR2);
 RETURN XMLTYPE;
```

**Parameters**

Table 6 GET\_OPATCH\_DATA Function Parameters

| Parameter | Description |
| --- | --- |
| `patchnum` | Patch number |

### GET\_OPATCH\_FILES Function

This function provides the list of files modified in the given patch number in XML format.

**Syntax**

```md
DBMS_QOPATCH.GET_OPATCH_FILES (
   patchnum IN VARCHAR2);
 RETURN XMLTYPE;
```

**Parameters**

Table 7 GET\_OPATCH\_FILES Function Parameters

| Parameter | Description |
| --- | --- |
| `patchnum` | Patch number |

### GET\_OPATCH\_INSTALL\_INFO Function

This function returns the XML element containing the `ORACLE_HOME` details such as patch and inventory location.

**Syntax**

```md
DBMS_QOPATCH.GET_OPATCH_INSTALL_INFO
 RETURNS XMLTYPE;
```

### GET\_OPATCH\_LIST Function

This function provides list of patches installed as an XML element from the XML inventory.

**Syntax**

```md
DBMS_QOPATCH.GET_OPATCH_LIST
 RETURN XMLTYPE;
```

### GET\_OPATCH\_LSINVENTORY

This function returns whole opatch inventory as XML instance document.

**Syntax**

```md
DBMS_QOPATCH.GET_OPATCH_LSINVENTORY
 RETURN XMLTYPE;
```

### GET\_OPATCH\_OLAYS Function

This function provides overlay patches for a given patch as XML element.

**Syntax**

```md
DBMS_QOPATCH.GET_OPATCH_OLAYS (
   patchnum IN VARCHAR2);
 RETURN XMLTYPE;
```

**Parameters**

Table 8 GET\_OPATCH\_OLAYS Function Parameters

| Parameter | Description |
| --- | --- |
| `patchnum` | Patch number |

### GET\_OPATCH\_PREQS Function

This function provides prerequisite patches for a given patch as XML element.

**Syntax**

```md
DBMS_QOPATCH.GET_OPATCH_PREQS (
   patchnum IN VARCHAR2);
 RETURN XMLTYPE;
```

**Parameters**

Table 9 GET\_OPATCH\_PREQS Function Parameters

| Parameter | Description |
| --- | --- |
| `patchnum` | Patch number |

### GET\_OPATCH\_XSLT

This function returns the style-sheet for the opatch XML inventory presentation. You can use the return type of this subprogram to perform XMLTRANSFORM and the transformed result has the same appearance as opatch text output.

**Syntax**

```md
DBMS_QOPATCH.GET_OPATCH_XSLT
 RETURN XMLTYPE;
```

### GET\_PATCH\_DETAILS Function

Displays the detailed patch information from `opatch lsinventory`.

**Syntax**

```md
DBMS_QOPATCH.GET_PATCH_DETAILS (
   patch    IN VARCHAR2);
 RETURN XMLTYPE;
```

**Parameters**

Table 10 GET\_PATCH\_DETAILS Function Parameters

| Parameter | Description |
| --- | --- |
| `patch` | The patch number. |

### GET\_SQLPATCH\_STATUS Procedure

This procedure displays the SQL patch status by querying from SQL patch registry to produce complete patch level information. If the patch number is given, it displays the information specific to the given SQL patch, otherwise information for all SQL patches.

**Syntax**

```md
DBMS_QOPATCH.GET_SQLPATCH_STATUS (
   patchnum IN VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 11 GET\_SQLPATCH\_STATUS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `patchnum` | Patch number |

### IS\_PATCH\_INSTALLED Function

This function provides information (such as patchID, application date, and SQL patch information) on the installed patch as XML node by querying the XML inventory.

**Syntax**

```md
DBMS_QOPATCH.IS_PATCH_INSTALLED (
   patchnum IN VARCHAR2);
 RETURN XMLTYPE;
```

**Parameters**

Table 12 IS\_PATCH\_INSTALLED Function Parameters

| Parameter | Description |
| --- | --- |
| `patchnum` | Patch number |

### OPATCH\_COMPARE\_CURRENT Function

Compares the current database with a list of bugs.

**Syntax**

```md
DBMS_QOPATCH.OPATCH_COMPARE_CURRENT Function (
   bugs     IN QOPATCH_LIST);
 RETURN VARCHAR2;
```

**Parameters**

Table 13 OPATCH\_COMPARE\_CURRENT Function Parameters

| Parameter | Description |
| --- | --- |
| `bugs` | List of bugs to compare with the current database. |

### OPATCH\_COMPARE\_NODES Function

Compares the given RAC node(s) with the instance to the present connected node with current node. The return value indicates whether the data was refreshed or not.

**Syntax**

```md
DBMS_QOPATCH.OPATCH_COMPARE_NODES (
   node     IN VARCHAR2 DEFAULT NULL,
   inst     IN VARCHAR2 DEFAULT NULL);
 RETURN VARCHAR2;
```

**Parameters**

Table 14 OPATCH\_COMPARE\_NODES Function Parameters

| Parameter | Description |
| --- | --- |
| `node` | Node name |
| `inst` | Instance name |

### SET\_CURRENT\_OPINST Procedure

This procedure sets the node name and instance to get the inventory details specific to it in an Oracle Real Application Clusters (RAC) environment.

**Syntax**

```md
DBMS_QOPATCH.SET_CURRENT_OPINST (
   node_name    IN VARCHAR2 DEFAULT NULL,
   inst_name    IN VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 15 SET\_CURRENT\_OPINST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `node_name` | Name of node |
| `inst_name` | Name of instance |
---
title: "Extensibility Constants, Types, and Mappings"
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/ext_types_ref.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 19 Extensibility Constants, Types, and Mappings

This chapter describes System Defined Constants and System Defined Types, which apply generically to all supported languages. It also describes mappings that are specific to the PL/SQL, C, and Java languages.

This chapter contains these topics:

## System Defined Constants

All the constants referred to in this chapter are defined in the `ODCIConst` package installed as part of the `catodci.sql` script. There are equivalent definitions for use within C routines in `odci.h`. You should use these constants instead of hard coding their underlying values in your routines. To ensure that the database or packet state are not inadvertently corrupted, the following statement is always used with these methods to restrict reads and writes:

```
pragma restrict_references(ODCIConst, WNDS, RNDS, WNPS, RNPS);
```

The options described in this section fall into two categories:

- Bit-field values that can be combined using the `OR` operator: ODCIIndexAlter Options, ODCIIndexInfo.Flags Bits, ODCIIPartInfo.PartOp, ODCIIPredInfo.Flags Bits, ODCIFuncInfo.Flags Bits, ODCIQueryInfo.Flags Bits, ODCIStatsOptions.Flags Bits, ODCIStatsOptions.Options Bits
- Distinct values, where only one option can be specified: ODCIArgDesc.ArgType Values, ODCIEnv.CallProperty Values, ScnFlg Values; Function with Index Context, Return Status Values

Table 19-1 ODCIArgDesc.ArgType Values

| Name | Description |
| --- | --- |
| ``` ArgOther ``` | Argument is other expression |
| ``` ArgCol ``` | Argument is a column name |
| ``` ArgLit ``` | Argument is a literal value |
| ``` ArgAttr ``` | Argument is an ADT `attr` column |
| ``` ArgCursor ``` | Argument is a `CURSOR` expression |
| ``` ArgNull ``` | Argument is `NULL` |

Table 19-2 ODCIEnv.CallProperty Values

| Name | Description |
| --- | --- |
| ``` None ``` | Default option |
| ``` FirstCall ``` | First partition call |
| ``` Intermediate Call ``` | Intermediate partition call |
| ``` FinalCall ``` | Final call after last partition |
| ``` StatsGlobal ``` | Used to specify global statistics gathering |
| ``` StatsGlobalAndPartition ``` | Used to specify global and partition-level statistics gathering |
| ``` StatsPartition ``` | Used to specify partition-level statistics gathering |

Table 19-3 ODCIIndexAlter Options

| Name | Description |
| --- | --- |
| ``` AlterIndexNone ``` | Default option |
| ``` AlterIndexRename ``` | Rename Partition option |
| ``` AlterIndexRebuild ``` | Rebuild Index option |
| ``` AlterIndexUpdBlockRefs ``` | IOT update block references |
| ``` AlterIndexMigrate ``` | Migrate user-managed domain index to a system-managed domain index. |
| ``` AlterIndexRenameCol ``` | Rename the column on which the domain index is based |
| ``` AlterIndexRenameTab ``` | Rename the table on which the domain index is based |

Table 19-4 ODCIIndexInfo.Flags Bits

| Name | Description |
| --- | --- |
| ``` Local ``` | Indicates a local domain index |
| ``` RangePartn ``` | For a local domain index, indicates that the base table is range-partitioned. Is set only in conjunction with the `Local` bit |
| ``` Parallel ``` | Indicates that a parallel degree was specified for the index creation or alter operation |
| ``` Unusable ``` | Indicates that `UNUSABLE` was specified during index creation, and that the index is marked unusable |
| ``` IndexOnIOT ``` | Indicates that the domain index is defined on an index-organized table |
| ``` ListPartn ``` | For a local domain index, indicates that the base table is list-partitioned. Is set only in conjunction with the `Local` bit. |
| ``` TransTblspc ``` | Indicates that the domain index is created in a transportable tablespace session. |
| ``` FunctionIdx ``` | Indicates that the index is a function-based domain index |

Table 19-5 ODCIIPartInfo.PartOp

| Name | Description |
| --- | --- |
| ``` AddPartition ``` | The partition to be added |
| ``` DropPartition ``` | The partition to be dropped |

Table 19-6 ODCIIPredInfo.Flags Bits

| Name | Description |
| --- | --- |
| ``` PredExactMatch ``` | Equality predicate |
| ``` PredPrefixMatch ``` | `LIKE` predicate |
| ``` PredIncludeStart ``` | Include start value in index range scan |
| ``` PredIncludeStop ``` | Include stop value in index range scan |
| ``` PredObjectFunc ``` | Left hand side of predicate is a standalone function |
| ``` PredObjectPkg ``` | Left hand side of predicate is a package function |
| ``` PredObjectType ``` | Left hand site of predicate is a type method |
| ``` PredObjectTable ``` | Predicate contains columns from several tables |

Table 19-7 ODCIFuncInfo.Flags Bits

| Name | Description |
| --- | --- |
| ``` ObjectFunc ``` | Standalone function |
| ``` ObjectPkg ``` | Package function |
| ``` ObjectType ``` | Type method |

Table 19-8 ODCIQueryInfo.Flags Bits

| Name | Description |
| --- | --- |
| ``` QueryFirstRows ``` | Optimizer mode is `FIRST_ROWS` |
| ``` QueryAllRows ``` | Optimizer mode is `ALL_ROWS` |

Table 19-9 ODCIStatsOptions.Flags Bits

| Name | Description |
| --- | --- |
| ``` EstimateStats ``` | Estimate statistics option |
| ``` ComputeStats ``` | Compute exact statistics option |
| ``` Validate ``` | Validate index option |

Table 19-10 ODCIStatsOptions.Options Bits

| Name | Description |
| --- | --- |
| ``` PercentOption ``` | Compute statistics by sampling |
| ``` RowOption ``` | Compute statistics based on all rows |

Table 19-11 Return Status Values

| Name | Description |
| --- | --- |
| ``` Success ``` | Indicates a successful operation. |
| ``` Error ``` | Indicates an error. |
| ``` Warning ``` | Indicates a warning. |
| ``` ErrContinue ``` | Indicates that there is an error in an index partition, but continues to work on the next partition. |
| ``` Fatal ``` | Indicates that all dictionary entries of the index are cleaned up, and that the `CREATE INDEX` operation is rolled back |

Table 19-12 ScnFlg Values; Function with Index Context

| Name | Description |
| --- | --- |
| ``` RegularCall ``` | User defined operator regular call |
| ``` CleanupCall ``` | User defined operator cleanup call |

## System-Defined Types

Several system-defined types are defined by Oracle and must be created by running the `catodci.sql` catalog script. The C mappings for these object types are defined in `odci.h`. The `ODCIIndex` and `ODCIStats` routines described in [Chapter 20](ext_idx_ref.md) and [Chapter 21](ext_opt_ref.md) use these types as parameters.

Unless otherwise mentioned, the names parsed as type attributes are unquoted identifiers.

### ODCIArgDesc

Object type. Stores function or operator arguments.

Table 19-13 DCIArgDesc Function and Operator Argument Description - Attributes

| Name | Data Type | Description |
| --- | --- | --- |
| ``` ArgType ``` | ``` NUMBER ``` | Argument type |
| ``` TableName ``` | ``` VARCHAR2(30) ``` | Name of table |
| ``` TableSchema ``` | ``` VARCHAR2(30) ``` | Schema containing the table |
| ``` ColName ``` | ``` VARCHAR2(4000) ``` | Name of column. This could be top level column name such as "A", or a nested column "A"."B" Note that the column name are quoted identifiers. |
| ``` TablePartitionLower ``` | ``` VARCHAR2(30) ``` | Contains the name of the lowest table partition that is accessed in the query |
| ``` TablePartitionUpper ``` | ``` VARCHAR2(30) ``` | Contains the name of the highest table partition that is accessed in the query |
| ``` Cardinality ``` | ``` NUMBER ``` | Cardinality value for `CURSOR` expressions |

### ODCIArgDescList

Contains a list of argument descriptors

Data Type

```
VARRAY(32767) of ODCIArgDesc
```

### ODCIRidList

Stores list of rowids. The rowids are stored in their character format.

Data Type

`VARRAY(32767) OF VARCHAR2("M_URID_SZ")`

### ODCIColInfo

Stores column related information.

Data Type

Object type.

Table 19-14 ODCIColInfo Column Related Information - Attributes

| Name | Data Type | Purpose |
| --- | --- | --- |
| ``` TableSchema ``` | ``` VARCHAR2(30) ``` | Schema containing table |
| ``` TableName ``` | ``` VARCHAR2(30) ``` | Name of table |
| ``` ColName ``` | ``` VARCHAR2(4000) ``` | Name of column. This could be top level column name such as "A", or a nested column "A"."B" Note that the column name are quoted identifiers. |
| ``` ColTypeName ``` | ``` VARCHAR2(30) ``` | Data Type of column |
| ``` ColTypeSchema ``` | ``` VARCHAR2(30) ``` | Schema containing data type if user-defined data type |
| ``` TablePartition ``` | ``` VARCHAR2(30) ``` | For a local domain index, contains the name of the specific base table partition |
| ``` TablePartitionIden ``` | ``` NUMBER ``` | Base table partition physical identifier |
| ``` TablePartitionTotal ``` | ``` NUMBER ``` | Total number of partitions in a table |

### ODCICost

Object type. Stores cost information.

Table 19-15 ODCICost Cost Information - Attributes

| Name | Data Type | Purpose |
| --- | --- | --- |
| ``` CPUCost ``` | ``` NUMBER ``` | CPU cost |
| ``` IOCost ``` | ``` NUMBER ``` | I/O cost |
| ``` NetworkCost ``` | ``` NUMBER ``` | Communication cost |
| ``` IndexCostInfo ``` | ``` VARCHAR2(255) ``` | Optional user-supplied information about the domain index for display in the `PLAN` table (255 characters maximum) |

### ODCIEnv

Object type. Contains general information about the environment in which the extensibility routines are executing.

Table 19-16 ODCIEnv Environment Variable Descriptor Information - Attributes

| Name | Data Type | Purpose |
| --- | --- | --- |
| `EnvFlags` | `NUMBER` | - 1 = Debugging On - 2 = NoData; used in [ODCIIndexAlter()](ext_idx_ref.md) method with alter\_option = AlterIndexRebuild to indicate that there is no data in the base partition. It is set only when [ODCIIndexAlter()](ext_idx_ref.md) is used as part of `TRAUNCATE TABLE` and partition management operations. |
| `CallProperty` | `NUMBER` | - 0 = None - 1 = First Call - 2 = Intermediate Call - 3 = Final Call - 6 = Global Statistics - 7 = Global and Partition Statistics - 8 = Partition Statistics |
| `DebugLevel` | `NUMBER` | Indicates the level of debugging |

Usage Notes

`CallProperty` is used only for `CREATE INDEX`, `DROP INDEX`, `TRUNCATE TABLE`, and for some extensible optimizer-related calls. In all other cases, including DML and query routines for local domain indexes, it is set to `0`.

### ODCIFuncInfo

Object type. Stores functional information.

Table 19-17 ODCIFuncInfo Function Information - Attributes

| Name | Data Type | Purpose |
| --- | --- | --- |
| ``` ObjectSchema ``` | ``` VARCHAR2(30) ``` | Object schema name |
| ``` ObjectName ``` | ``` VARCHAR2(30) ``` | Function/package/type name |
| ``` MethodName ``` | ``` VARCHAR2(30) ``` | Method name for package/type |
| ``` Flags ``` | ``` NUMBER ``` | Function flags - see `ODCIConst` |

### ODCIIndexInfo

Object type. Stores the metadata information related to a domain index. It is passed as a parameter to all `ODCIIndex` routines.

Table 19-18 ODCIIndexInfo Index Related Information - Attributes

| Name | Data Type | Purpose |
| --- | --- | --- |
| ``` IndexSchema ``` | ``` VARCHAR2(30) ``` | Schema containing domain index |
| ``` IndexName ``` | ``` VARCHAR2(30) ``` | Name of domain index |
| ``` IndexCols ``` | ``` ODCIColInfoList ``` | List of indexed columns |
| ``` IndexPartition ``` | ``` VARCHAR2(30) ``` | For a local domain index, contains the name of the specific index partition |
| ``` IndexInfoFlags ``` | ``` NUMBER ``` | Possible flags are:  - `Local` - `RangePartn` - `Parallel` - `Unusable` - `IndexOnIOT` - `ListPartn` - `TransTblspc` - `FunctionIdx` |
| ``` IndexParaDegree ``` | ``` NUMBER ``` | The degree of parallelism, if one is specified when creating or rebuilding a domain index or local domain index partition in parallel |
| ``` IndexPartitionIden ``` | ``` NUMBER ``` | The index partition object identifier, for local domain indexes |
| ``` IndexPartitionTotal ``` | ``` NUMBER ``` | The total number of partitions in an index |

### ODCIIndexCtx

Object type. Stores the index context, including the domain index metadata and the rowid. It is passed as parameter to the functional implementation of an operator that expects index context.

Table 19-19 ODCIIndexCtx Index Context Related Information - Attributes

| Name | Data Type | Purpose |
| --- | --- | --- |
| ``` IndexInfo ``` | ``` ODCIIndexInfo ``` | Stores the metadata information about the domain index |
| ``` rid ``` | ``` VARCHAR2("M_URID_SZ") ``` | Row identifier of the current row |

### ODCIObject

Object type. Stores information about a schema object.

Table 19-20 ODCIObject Index Context Related Information - Attributes

| Name | Data Type | Purpose |
| --- | --- | --- |
| ``` ObjectSchema ``` | ``` VARCHAR2(30) ``` | Name of schema in which object is located |
| ``` ObjectName ``` | ``` VARCHAR2(30) ``` | Name of object |

### ODCIObjectList

Stores information about a list of schema objects.

Data Type

`VARRAY(32) OF ODCIObject`

### ODCIPartInfo

Object type. Contains the names of both the table partition and the index partition.

Table 19-21 ODCIPartInfo Index-Related Information - Attributes

| Name | Data Type | Purpose |
| --- | --- | --- |
| ``` TablePartition ``` | `VARCHAR2(30)` | Table partition name |
| ``` IndexPartition ``` | `VARCHAR2(30)` | Index partition name |
| ``` IndexPartitionIden ``` | NUMBER | Index partition object identifier |
| ``` PartOp ``` | NUMBRER | Partition operation that is being performed |

### ODCIPredInfo

Object type. Stores the metadata information related to a predicate containing a user-defined operator or function. It is also passed as a parameter to the [ODCIIndexStart()](ext_idx_ref.md) query routine.

Table 19-22 ODCIPredInfo Operator Related Information - Attributes

| Name | Data Type | Purpose |
| --- | --- | --- |
| ``` ObjectSchema ``` | ``` VARCHAR2(30) ``` | Schema of operator/function |
| ``` ObjectName ``` | ``` VARCHAR2(30) ``` | Name of operator/function |
| ``` MethodName ``` | ``` VARCHAR2(30) ``` | Name of method, applies only to package methods type |
| ``` Flags ``` | ``` NUMBER ``` | Possible flags are:  - `PredExactMatch` - Exact Match - `PredPrefixMatch` - Prefix Match - `PredIncludeStart` - Bounds include the start key value - `PredIncludeStop` - Bounds include the stop key value - `PredMultiTable` - Predicate involves multiple tables - `PredObjectFunc` - Object is a function - `PredObjectPlg` - Object is a package - `PredObjectType` - Object is a type |

### ODCIQueryInfo

Object type. Stores information about the context of a query. It is passed as a parameter to the [ODCIIndexStart()](ext_idx_ref.md) routine.

Table 19-23 ODCIQueryInfo Index Context Related Information - Attributes

| Name | Data Type | Purpose |
| --- | --- | --- |
| ``` Flags ``` | ``` NUMBER ``` | The following flags can be set:  - `QueryFirstRows` - Set when the optimizer hint `FIRST_ROWS` is specified in the query - `QueryAllRows` - Set when the optimizer hint `ALL_ROWS` is specified in the query |
| ``` AncOps ``` | ``` ODCIObjectList ``` | Ancillary operators referenced in the query |

### ODCIStatsOptions

Object type. Stores options information for `DBMS_STATS`.

Table 19-24 ODCIStatsOptions Cost Information - Attributes

| Name | Data Type | Purpose |
| --- | --- | --- |
| ``` Sample ``` | ``` NUMBER ``` | Sample size |
| ``` Options ``` | ``` NUMBER ``` | `DBMS_STATS` options - see "ODCICost" |
| ``` Flags ``` | ``` NUMBER ``` | `DBMS_STATS` flags - see "ODCICost" |

### ODCITabFuncStats

Object type. Stores cardinality information for a table function.

Table 19-25 ODCITabFuncStats Parameter

| Parameter | Data Type | Purpose |
| --- | --- | --- |
| `num_rows` | `NUMBER` | Contains the number of rows expected to be returned by the table function |

### ODCITabStats

Stores table statistics for a table function.

Data Type

`NUMBER`

Table 19-26 ODCITabStats - Attributes

| Name | Data Type | Purpose |
| --- | --- | --- |
| `Num_rows` | `NUMBER` | Number of rows in table |

### ODCIBFileList

Stores varrays of `BFILE` s.

Data Type

`VARRAY(32767) OF BFILE`

### ODCITabFuncInfo

Object type. Stores information on which attributes of user-defined types in a collection must be set by a table function.

Table 19-27 ODCITabFuncInfo Parameters

| Name | Data Type | Purpose |
| --- | --- | --- |
| `Attrs` | `ODCINumberList` | Indicates the attributes that must be set |
| `RetType` | `AnyType` | For `AnyDataSet` table functions, indicates the actual return type to be expected in the `AnyDataSet` collection |

### ODCIDateList

Stores varrays of `DATE` s.

Data Type

`VARRAY(32767) OF DATE`

### ODCINumberList

Stores varrays of `NUMBER` s.

Data Type

`VARRAY(32767) OF NUMBER`

### ODCIRawList

Stores varrays of `Raw` s.

Data Type

`VARRAY(32767) OF Raw(2000)`

### ODCIVarchar2List

Stores varrays of `VARCHAR2` s

Data Type

`VARRAY(32767) OF VARCHAR2(4000)`

### ODCIFuncCallInfo

Object type. Stores information about the functional implementation of an operator.

Table 19-28 ODCIFuncCallInfo - Attributes

| Name | Data Type | Purpose |
| --- | --- | --- |
| `ColInfo` | `ODCIColInfo` | Information about the column on which the operator is invoked |

Usage Notes

A functional implementation can be defined with this parameter only if the operator binding is declared `WITH COLUMN CONTEXT`. This is useful if the functional implementation requires information about the column it was invoked on, and there is no domain index defined on the column. This argument is only populated in the function invocation if the first argument of the operator invocation is a column and there is no domain index defined on that column.

## Mappings of Constants and Types

This section describes language-specific mappings.

### Mappings in PL/SQL

A variety of PL/SQL mappings are common to both Extensible Indexing and the Extensible Optimizer.

- Constants are defined in the `ODCIConst` package found in `catodci.sql`
- Types are defined as object types found in `catodci.sql`

### Mappings in C

Mappings of constants and types are defined for C in the public header file `odci.h`. Each C structure to which a type is mapped has a corresponding indicator structure called `structname_ind` and a reference definition called `structname_ref`.
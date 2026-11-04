---
title: "PSBTREE: Extensible Indexing Example"
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/psbtree_example.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 16 PSBTREE: Extensible Indexing Example

This chapter presents an extensible indexing example in which some `ODCIIndex` interface routines are implemented in C.

This chapter contains these topics:

## Introducing the PSBTREE Example

The example in this chapter illustrates how to implement the extensible indexing interface routines in C. The example's focus is on topics that are common to all implementations; it does not expose domain-specific details.

The code for the example is in the demo directory, in the file `extdemo6.sql`. It extends an earlier example (`extdemo2.sql`, also in demo directory) by adding to the indextype support for local domain indexes on range partitioned tables.

## Designing of the Indextype

The indextype implemented here, called `PSBtree,` operates like a b-tree index. It supports three user-defined operators: `eq` (equals), `lt` (less than), and `gt` (greater than). These operators operate on operands of `VARCHAR2` data type.

The index data consists of records of the form `<key, rid>` where `key` is the value of the indexed column and `rid` is the row identifier of the corresponding row. To simplify the implementation of the indextype, the index data is stored in an system-partitioned table.

When an index is a system-managed local domain index, one partition in a system-partitioned table is created for each partition to store the index data for that partition. Thus, the index manipulation routines merely translate operations on the `PSBtree` into operations on the table partition that stores the index data.

When a user creates a `PSBtree` index (a local index), `n` table partitions are created consisting of the indexed column and a `rowid` column, where `n` is the number of partitions in the base table. Inserts into the base table cause appropriate insertions into the affected index table partition. Deletes and updates are handled similarly. When the `PSBtree` is queried based on a user-defined operator (one of `gt`, `lt` and `eq`), an appropriate query is issued against the index table partitions to retrieve all the satisfying rows. Appropriate partition pruning occurs, and only the index table partitions that correspond to the relevant, or "interesting", partitions are accessed.

## Implementing Operators

The `PSBtree` indextype supports three operators. Each operator has a corresponding functional implementation. The functional implementations of the `eq`, `gt` and `lt` operators are presented in the following section.

### Create Functional Implementations

This section describes the functional implementation of comparison operators. Example 16-1 shows how to implement `eq` (equals), Example 16-2 shows how to implement `lt` (less than), and Example 16-3 shows how to implement `gt` (greater than) operators.

Example 16-1 Implementing the EQUALS Operator

The functional implementation for `eq` is provided by a function (`bt_eq`) that takes in two `VARCHAR2` parameters and returns `1` if they are equal and `0` otherwise.

```
CREATE FUNCTION bt_eq(a VARCHAR2, b VARCHAR2) RETURN NUMBER AS
BEGIN 
  IF a = b then
    RETURN 1;
  ELSE
    RETURN 0;
  END IF;
END;
```

Example 16-2 Implementing the LESS THAN Operator

The functional implementation for `lt` is provided by a function (`bt_lt`) that takes in two `VARCHAR2` parameters and returns `1` if the first parameter is less than the second, `0` otherwise.

```
CREATE FUNCTION bt_lt(a VARCHAR2, b VARCHAR2) RETURN NUMBER AS
BEGIN 
  IF a < b then
    RETURN 1;
  ELSE
    RETURN 0;
  END IF;
END;
```

Example 16-3 Implementing the GREATER THAN Operator

The functional implementation for `gt` is provided by a function (`bt_gt`) that takes in two `VARCHAR2` parameters and returns `1` if the first parameter is greater than the second, `0` otherwise.

```
CREATE FUNCTION bt_gt(a VARCHAR2, b VARCHAR2) RETURN NUMBER AS
BEGIN 
  IF a > b then
    RETURN 1;
  ELSE
    RETURN 0;
  END IF;
END;
```

### Create Operators

To create the operator, you must specify the signature of the operator along with its return type and its functional implementation. Example 16-4 shows how to create `eq` (equals), Example 16-5 shows how to create `lt` (less than), and Example 16-6 shows how to create `gt` (greater than) operators.

Example 16-4 Creating the EQUALS Operator

```
CREATE OPERATOR eq 
BINDING (VARCHAR2, VARCHAR2) RETURN NUMBER 
USING bt_eq;
```

Example 16-5 Creating the LESS THAN Operator

```
CREATE OPERATOR lt 
BINDING (VARCHAR2, VARCHAR2) RETURN NUMBER 
USING bt_lt;
```

Example 16-6 Creating the GREATER THAN Operator

```
CREATE OPERATOR gt 
BINDING (VARCHAR2, VARCHAR2) RETURN NUMBER 
USING bt_gt;
```

## Implementing the ODCIIndex Interfaces

To implement the `PSBTREE`, you must implement the `ODCIIndex` `XXX` `()` routines, as outlined in the following sections. You can implement the index routines in any language supported by Oracle. This section implements the [ODCIGetInterfaces()](ext_idx_ref.md) routine in the C programming language. Note that these require advance setup, such as creating a library object, `extdemo6l`, for your compiled C code.

### Defining an Implementation Type for PSBTREE

Define an implementation type that implements the `ODCIIndex` interface routines, as demonstrated in Example 16-7.

Example 16-7 Creating a PSBTREE Index Type

```
CREATE TYPE psbtree_im AS OBJECT
(
  scanctx RAW(4),
  STATIC FUNCTION ODCIGetInterfaces(ifclist OUT SYS.ODCIObjectList)
    RETURN NUMBER,
  STATIC FUNCTION ODCIIndexCreate (ia SYS.ODCIIndexInfo, parms VARCHAR2,
    env SYS.ODCIEnv) RETURN NUMBER,
  STATIC FUNCTION ODCIIndexAlter (ia sys.ODCIIndexInfo, 
    parms IN OUT VARCHAR2, altopt number, env sys.ODCIEnv) RETURN NUMBER, 
  STATIC FUNCTION ODCIIndexDrop(ia SYS.ODCIIndexInfo, env SYS.ODCIEnv) 
    RETURN NUMBER,
  STATIC FUNCTION ODCIIndexExchangePartition(ia SYS.ODCIIndexInfo,
    ia1 SYS.ODCIIndexInfo, env SYS.ODCIEnv) RETURN NUMBER,
  STATIC FUNCTION ODCIIndexUpdPartMetadata(ia sys.ODCIIndexInfo, 
    palist sys.ODCIPartInfoList, env sys.ODCIEnv) RETURN NUMBER,
  STATIC FUNCTION ODCIIndexExchangePartition (ia sys.ODCIIndexInfo,
    ia1 sys.ODCIIndexInfo, env sys.ODCIEnv) RETURN NUMBER,
  STATIC FUNCTION ODCIIndexInsert(ia SYS.ODCIIndexInfo, rid VARCHAR2,
    newval VARCHAR2, env SYS.ODCIEnv) RETURN NUMBER,
  STATIC FUNCTION ODCIIndexDelete(ia SYS.ODCIIndexInfo, rid VARCHAR2,
    oldval VARCHAR2, env SYS.ODCIEnv) RETURN NUMBER,
  STATIC FUNCTION ODCIIndexUpdate(ia SYS.ODCIIndexInfo, rid VARCHAR2,
    oldval VARCHAR2, newval VARCHAR2, env SYS.ODCIEnv) RETURN NUMBER,
  STATIC FUNCTION ODCIIndexStart(sctx IN OUT psbtree_im, ia SYS.ODCIIndexInfo,
    op SYS.ODCIPredInfo, qi sys.ODCIQueryInfo, strt number, stop number,
    cmpval VARCHAR2, env SYS.ODCIEnv) RETURN NUMBER,
  MEMBER FUNCTION ODCIIndexFetch(nrows NUMBER, rids OUT SYS.ODCIridlist,
    env SYS.ODCIEnv) RETURN NUMBER,
  MEMBER FUNCTION ODCIIndexClose(env SYS.ODCIEnv) RETURN NUMBER
);
/
SHOW ERRORS
```

### Creating the Implementation Type Body

Define the implementation type body, as demonstrated in Example 16-8.

Example 16-8 Creating the Implementation Body for PBSTREE

```
CREATE OR REPLACE TYPE BODY psbtree_im IS
```

### Defining PL/SQL Routines in the Implementation Body

The examples in this section demonstrate how to implement the index definition routines in PL/SQL. Example 16-9 shows how to implement [ODCIGetInterfaces()](ext_idx_ref.md), Example 16-10 shows how to implement [ODCIIndexCreate()](ext_idx_ref.md), Example 16-11 shows how to implement [ODCIIndexDrop()](ext_idx_ref.md), Example 16-12 shows how to implement [ODCIIndexAlter()](ext_idx_ref.md), Example 16-13 shows how to implement [ODCIIndexUpdPartMetadata()](ext_idx_ref.md), and Example 16-14 shows how to implement [ODCIIndexExchangePartition()](ext_idx_ref.md).

Example 16-9 Implementing ODCIGetInterfaces() for PBSTREE in PL/SQL

The [ODCIGetInterfaces()](ext_idx_ref.md) routine, demonstrated in Example 16-9, returns the expected interface name through its `OUT` parameter.

```
STATIC FUNCTION ODCIGetInterfaces(
  ifclist OUT sys.ODCIObjectList) 
RETURN NUMBER IS
BEGIN
  ifclist := sys.ODCIObjectList(sys.ODCIObject('SYS','ODCIINDEX2'));
  RETURN ODCIConst.Success;
END ODCIGetInterfaces;
```

Example 16-10 Implementing ODCIIndexCreate() for PBSTREE in PL/SQL

The [ODCIIndexCreate()](ext_idx_ref.md) routine creates a system-partitioned index storage table with two columns. The first column stores the `VARCHAR2` indexed column value. The routine makes use of the information passed in to determine the context in which it is invoked. Dynamic SQL is used to execute the dynamically constructed SQL statement.

```
STATIC FUNCTION ODCIIndexCreate (
  ia sys.ODCIIndexInfo, 
  parms VARCHAR2, 
  env sys.ODCIEnv) 
RETURN NUMBER IS
  i INTEGER;
  stmt VARCHAR2(2000);
  cursor cur1(ianame VARCHAR2) IS
    SELECT partition_name, parameters 
    FROM user_ind_partitions 
    WHERE index_name = ianame order by partition_name;
BEGIN
  stmt := '';
 
  IF (env.CallProperty is null)  THEN
    stmt := 'create table ' ||ia.IndexSchema || '.' || ia.IndexName ||
      '_sbtree(f1 VARCHAR2(1000), f2 rowid)';

  ELSEIF (env.callproperty = sys.ODCIConst.FirstCall) THEN
  stmt := '';
  i := 1;
  FOR c1 in cur1(ia.indexname) LOOP
    IF (i >1) THEN
      stmt := stmt || ',';
    END IF;
    stmt := stmt || 'partition ' || c1.partition_name;
    i := i+1;
  END LOOP;
  stmt := 'create table ' || ia.indexschema || '.' || ia.indexname ||
    '_sbtree (f1 VARCHAR2(1000), f2 rowid) partition by system ' ||
     '( ' || stmt || ')';

  ELSEIF (env.callproperty = sys.ODCIConst.FinalCall) THEN
    stmt := 'create index ' || ia.indexschema || '.' || ia.indexname ||
      '_sbti on ' || ia.indexschema || '.' || ia.indexname ||
      '_sbtree (f1) local';
  END IF;
 
  dbms_output.put_line('Create');
  dbms_output.put_line(stmt);
 
  -- execute the statement
  IF ((env.CallProperty is null) OR
      (env.CallProperty = sys.ODCIConst.FirstCall) OR
      (env.CallProperty = sys.ODCIConst.FinalCall) ) THEN
    execute immediate stmt;

  IF (env.CallProperty is null) THEN
    execute immediate 'insert into ' ||ia.IndexSchema || '.' || ia.IndexName 
      || '_sbtree select '  || ia.IndexCols(1).Colname || ', ROWID from ' ||
      ia.IndexCols(1).TableSchema || '.' || ia.IndexCols(1).TableName;
    execute immediate 'create index ' || ia.indexschema || '.' || 
      ia.indexname || '_sbti on ' || ia.indexschema || '.' || 
      ia.indexname || '_sbtree (f1)';
    END IF;
  END IF;
 
  RETURN ODCIConst.Success;
END ODCIIndexCreate;
```

Example 16-11 Implementing ODCIIndexDrop() for PBSTREE in PL/SQL

The [ODCIIndexDrop()](ext_idx_ref.md) routine drops the index storage tables.

```
STATIC FUNCTION ODCIIndexDrop(
  ia sys.ODCIIndexInfo,
  env sys.ODCIEnv) 
RETURN NUMBER IS
  stmt VARCHAR2(1000);
  cnum INTEGER;
  junk INTEGER;
BEGIN
  -- construct the sql statement
  stmt := '';

  IF (env.CallProperty is null) THEN
    stmt := 'drop table ' || ia.IndexSchema || '.' || ia.IndexName || '_sbtree';
    dbms_output.put_line('Drop');
    dbms_output.put_line(stmt);
    execute immediate stmt;
  END IF;
  RETURN ODCIConst.Success;
END ODCIIndexDrop;
```

Example 16-12 Implementing ODCIIndexAlter() for PSBTREE in PL/SQL

The [ODCIIndexAlter()](ext_idx_ref.md) routine can perform many index alteration tasks, such as rebuilding and renaming an index.

```
STATIC FUNCTION ODCIIndexAlter (
  ia sys.ODCIIndexInfo, 
  parms IN OUT VARCHAR2, 
  altopt NUMBER,
  env sys.ODCIEnv) 
RETURN NUMBER IS
  stmt    VARCHAR2(2000);
BEGIN
  stmt := '';
  IF (altopt = ODCIConst.AlterIndexRebuild) THEN
    IF (ia.IndexPartition is null) THEN
      stmt := 'insert into ' || ia.indexschema || '.' || ia.indexname ||
          '_sbtree select ' || ia.indexcols(1).colname || ', rowid from ' ||
          ia.indexcols(1).tableschema || '.' || ia.indexcols(1).tablename;
    ELSE
      stmt := 'insert into ' || ia.indexschema || '.' || ia.indexname ||
          '_sbtree partition (' || ia.indexpartition || ') select ' || 
          ia.indexcols(1).colname || ', rowid from ' ||
          ia.indexcols(1).tableschema || '.' || ia.indexcols(1).tablename ||
          ' partition (' || ia.indexcols(1).tablepartition || ')';
    END IF;
  ELSEIF (altopt = ODCIConst.AlterIndexRename) THEN
    IF (ia.IndexPartition is not null) THEN
      stmt := 'alter table ' || ia.indexschema || '.' || ia.indexname ||
          '_sbtree rename partition ' || ia.indexpartition || ' to ' || parms;
    ELSE
      stmt := 'alter table ' || ia.indexschema || '.' || ia.indexname ||
          '_sbtree rename to ' || parms || '_sbtree';
    END IF;
  END IF;

  dbms_output.put_line('Alter');
  IF ((altopt=ODCIConst.AlterIndexRebuild) or (altopt=ODCIConst.AlterIndexRename))
  THEN
    dbms_output.put_line(stmt);
    execute immediate stmt;
  END IF;
  RETURN ODCIConst.Success;
END ODCIIndexAlter;
```

Example 16-13 Implementing ODCIIndexUpdPartMetadata() for PSBTREE in PL/SQL

To handle partition maintenance operations, the kernel performs the maintenance tasks on behalf of the user. The indextype, to maintain its metadata, should have the [ODCIIndexUpdPartMetadata()](ext_idx_ref.md) routine.

```
STATIC FUNCTION ODCIIndexUpdPartMetadata(
  ia sys.ODCIIndexInfo, 
  palist sys.ODCIPartInfoList, 
  env sys.ODCIEnv) 
RETURN NUMBER IS
  col  number;
BEGIN
  dbms_output.put_line('ODCIUpdPartMetadata');
  sys.ODCIIndexInfoDump(ia);
  sys.ODCIPartInfoListDump(palist);
  sys.ODCIEnvDump(env);
  RETURN ODCIConst.Success;
END ODCIIndexUpdPartMetadata;
```

Example 16-14 Implementing ODCIIndexExchangePartition() for PSBTREE in PL/SQL

The [ODCIIndexExchangePartition()](ext_idx_ref.md) exchanges the index storage tables for the index partition being exchanged, with the index storage table for the global domain index.

```
STATIC FUNCTION ODCIIndexExchangePartition(
  ia sys.ODCIIndexInfo,
  ia1 sys.ODCIIndexInfo,
  env sys.ODCIEnv)
RETURN NUMBER IS
  stmt VARCHAR2(2000);
  cnum INTEGER;
  junk INTEGER;
BEGIN
  stmt := '';
  dbms_output.put_line('Exchange Partitions');

  -- construct the sql statement
  stmt := 'alter table ' || ia.IndexSchema || '.' || ia.IndexName ||
    '_sbtree exchange partition ' ||   ia.IndexPartition || ' with table ' ||
    ia1.IndexSchema || '.' || ia1.IndexName || '_sbtree';
 
  dbms_output.put_line(stmt);
  execute immediate stmt;
 
  RETURN ODCIConst.Success;
END ODCIIndexExchangePartition;
```

### Registering the C Implementation of the ODCIIndexXXX() Methods

After creating the `extdemo6l` library object for the compiled C methods, you must register the implementations of each of the routines. Example 16-15 demonstrates how to register the [ODCIIndexInsert()](ext_idx_ref.md) implementation, Example 16-16 registers the [ODCIIndexDelete()](ext_idx_ref.md) implementation, Example 16-17 registers the [ODCIIndexUpdate()](ext_idx_ref.md) implementation, Example 16-18 registers the [ODCIIndexStart()](ext_idx_ref.md) implementation, Example 16-19 registers the [ODCIIndexFetch()](ext_idx_ref.md) implementation, and Example 16-20 registers the [ODCIIndexClose()](ext_idx_ref.md) implementation.

Example 16-15 Registering the Implementation of ODCIIndexInsert()

Register the implementation of the [ODCIIndexInsert()](ext_idx_ref.md) routine.

```
STATIC FUNCTION ODCIIndexInsert(
  ia SYS.ODCIIndexInfo,
  rid VARCHAR2,
  newval VARCHAR2,
  env SYS.ODCIEnv)
RETURN NUMBER AS EXTERNAL
name "qxiqtbspi"
library extdemo6l
with context
parameters (
  context,
  ia,
  ia indicator struct,
  rid,
  rid indicator,
  newval,
  newval indicator,
  env,
  env indicator struct,
  return OCINumber
);
```

Example 16-16 Registering the Implementation of ODCIIndexDelete()

Register the implementation of the [ODCIIndexDelete()](ext_idx_ref.md) routine.

```
STATIC FUNCTION ODCIIndexDelete(
  ia SYS.ODCIIndexInfo, 
  rid VARCHAR2,
  oldval VARCHAR2, 
  env SYS.ODCIEnv)
RETURN NUMBER AS EXTERNAL
name "qxiqtbspd"
library extdemo6l
with context
parameters (
  context,
  ia,
  ia indicator struct,
  rid,
  rid indicator,
  oldval,
  oldval indicator,
  env,
  env indicator struct,
  return OCINumber
);
```

Example 16-17 Registering the Implementation of ODCIIndexUpdate()

Register the implementation of the [ODCIIndexUpdate()](ext_idx_ref.md) routine.

```
STATIC FUNCTION ODCIIndexUpdate(
  ia SYS.ODCIIndexInfo, 
  rid VARCHAR2,
  oldval VARCHAR2,
  newval VARCHAR2,
  env SYS.ODCIEnv)
RETURN NUMBER AS EXTERNAL
name "qxiqtbspu"
library extdemo6l
with context
parameters (
  context,
  ia,
  ia indicator struct,
  rid,
  rid indicator,
  oldval,
  oldval indicator,
  newval,
  newval indicator,
  env,
  env indicator struct,
  return OCINumber
);
```

Example 16-18 Registering the Implementation of ODCIIndexStart()

Register the implementation of the [ODCIIndexStart()](ext_idx_ref.md) routine.

```
STATIC FUNCTION ODCIIndexStart(
  sctx IN OUT psbtree_im,
  ia SYS.ODCIIndexInfo,
  op SYS.ODCIPredInfo,
  qi SYS.ODCIQueryInfo,
  strt NUMBER,
  stop NUMBER,
  cmpval VARCHAR2,
  env SYS.ODCIEnv)
RETURN NUMBER AS EXTERNAL
name "qxiqtbsps"
library extdemo6l
with context
parameters (
  context,
  sctx,
  sctx indicator struct,
  ia,
  ia indicator struct,
  op,
  op indicator struct,
  qi,
  qi indicator struct,
  strt,
  strt indicator,
  stop,
  stop indicator,
  cmpval,
  cmpval indicator,
  env,
  env indicator struct,
  return OCINumber
);
```

Example 16-19 Registering the Implementation of ODCIIndexFetch()

Register the implementation of the [ODCIIndexFetch()](ext_idx_ref.md) routine.

```
MEMBER FUNCTION ODCIIndexFetch(
  nrows NUMBER,
  rids OUT SYS.ODCIRidList,
  env SYS.ODCIEnv)
RETURN NUMBER AS EXTERNAL
name "qxiqtbspf"
library extdemo6l
with context
parameters (
  context,
  self,
  self indicator struct,
  nrows,
  nrows indicator,
  rids,
  rids indicator,
  env,
  env indicator struct,
  return OCINumber
 );
```

Example 16-20 Registering the Implementation of ODCIIndexClose()

Register the implementation of the [ODCIIndexClose()](ext_idx_ref.md) routine.

```
MEMBER FUNCTION ODCIIndexClose (
  env SYS.ODCIEnv) 
RETURN NUMBER AS EXTERNAL
name "qxiqtbspc"
library extdemo6l
with context
parameters (
  context,
  self,
  self indicator struct,
  env,
  env indicator struct,
  return OCINumber
);
```

### Defining Additional Structures in C Implementation

The `stuct` s `qxiqtim` and `qciqtin`, and the `struct` `qxiqtcx` are used for mapping the object type and its `null` value (demonstrated in Example 16-21) and for keeping state during fetching calls (demonstrated in Example 16-22). These structures are used by the methods described in section "Defining C Methods in the Implementation Body".

The C `struct` s for mapping the ODCI types are defined in the file `odci.h`. For example, the C `struct` `ODCIIndexInfo` is the mapping for the corresponding ODCI object type. The C `struct` `ODCIIndexInfo_ind` is the mapping for the `null` object.

Example 16-21 Defining Mappings for the Object Type and Its Null Value

We have defined a C `struct`, `qxiqtim`, as a mapping for the object type. There is an additional C `struct`, `qxiqtin`, for the corresponding `null` object. The C `struct` s for the object type and its `null` object can be generated from the Object Type Translator (OTT).

```
/* The index implementation type is an object type with a single RAW attribute
 * used to store the context key value. 
 * C mapping of the implementation type : */

struct qxiqtim{
  OCIRaw *sctx_qxiqtim;
}; 
typedef struct qxiqtim qxiqtim;

struct qxiqtin{
  short atomic_qxiqtin;
  short scind_qxiqtin;
}; 
typedef struct qxiqtin qxiqtin;
```

Example 16-22 Keeping the Scan State During Fetching Calls

There are a set of OCI handles that must be cached away and retrieved during fetch calls. A C `struct`, `qxiqtcx`, is defined to hold all the necessary scan state. This structure is allocated out of `OCI_DURATION_STATEMENT` memory to ensure that it persists till the end of `fetch`. After populating the structure with the required info, a pointer to the structure is saved in OCI context. The context is identified by a 4-byte key that is generated by calling an OCI routine. The 4-byte key is stashed away in the scan context - `exiting`. This object is returned back to the Oracle server and is passed in as a parameter to the next fetch call.

```
/* The index scan context - should be stored in "statement" duration memory
 * and used by start, fetch and close routines.
 */
struct qxiqtcx
{
  OCIStmt *stmthp;
  OCIDefine *defnp;
  OCIBind *bndp;
  char ridp[19];
}; 
typedef struct qxiqtcx qxiqtcx;
```

### Defining C Methods in the Implementation Body

The following methods have been implemented in the C language. Example 16-23 demonstrates how to implement an error processing routine, Example 16-24 implements [ODCIIndexInsert()](ext_idx_ref.md), Example 16-25 implements [ODCIIndexDelete()](ext_idx_ref.md), Example 16-26 implements [ODCIIndexUpdate()](ext_idx_ref.md), Example 16-27 implements [ODCIIndexStart()](ext_idx_ref.md), Example 16-28 implements [ODCIIndexFetch()](ext_idx_ref.md), and Example 16-29 implements [ODCIIndexClose()](ext_idx_ref.md).

Example 16-23 Implementing a Common Error Processing Routine in C

This function is used to check and process the return code from all `OCI` routines. It checks the status code and raises an exception in case of errors.

```
static int qxiqtce(
  OCIExtProcContext *ctx,
  OCIError *errhp,
  sword status)
{
  text errbuf[512];
  sb4 errcode = 0;
  int errnum = 29400;  /* choose some oracle error number */
  int rc = 0;

  switch (status)
  {
    case OCI_SUCCESS: 
      rc = 0;
      break;
    case OCI_ERROR:
      (void) OCIErrorGet((dvoid *)errhp, (ub4)1, (text *)NULL, &errcode,
      errbuf, (ub4)sizeof(errbuf), OCI_HTYPE_ERROR);
      /* Raise exception */
      OCIExtProcRaiseExcpWithMsg(ctx, errnum, errbuf, strlen((char *)errbuf));
      rc = 1;
      break;
    default:
      (void) sprintf((char *)errbuf, "Warning - some error\n");
      /* Raise exception */
      OCIExtProcRaiseExcpWithMsg(ctx, errnum, errbuf, strlen((char *)errbuf));
      rc = 1;
      break;
  }
  return (rc);
}
```

Example 16-24 Implementing ODCIIndexInsert() for PSBTREE in C

The insert routine, [ODCIIndexInsert()](ext_idx_ref.md), parses and executes a statement that inserts a new row into the index table. The new row consists of the new value of the indexed column and the `rowid` that have been passed in as parameters.

```
OCINumber *qxiqtbspi(
  OCIExtProcContext *ctx,
  ODCIIndexInfo     *ix,
  ODCIIndexInfo_ind *ix_ind,
  char              *rid,
  short             rid_ind,
  char              *newval,
  short             newval_ind,
  ODCIEnv           *env,
  ODCIEnv_ind       *env_ind)
{
  OCIEnv *envhp = (OCIEnv *) 0;             /* env. handle */
  OCISvcCtx *svchp = (OCISvcCtx *) 0;       /* service handle */
  OCIError *errhp = (OCIError *) 0;         /* error handle */
  OCIStmt *stmthp = (OCIStmt *) 0;          /* statement handle */
  OCIBind *bndp = (OCIBind *) 0;            /* bind handle */

  int retval = (int)ODCI_SUCCESS;           /* return from this function */
  OCINumber *rval = (OCINumber *)0;

  char insstmt[2000];                       /* sql insert statement */
  ODCIColInfo  *colinfo;                    /* column info */
  ODCIColInfo_ind  *colinfo_ind;
  boolean exists = TRUE;
  unsigned int partiden;                    /* table partition iden */ 
  unsigned int idxflag;                     /* index info flag  

  /* allocate memory for OCINumber first */
  rval = (OCINumber *)OCIExtProcAllocCallMemory(ctx, sizeof(OCINumber));

  /* Get oci handles */
  if (qxiqtce(ctx, errhp, OCIExtProcGetEnv(ctx, &envhp, &svchp, &errhp)))
    return(rval);

  /* set up return code */
  if (qxiqtce(ctx, errhp, OCINumberFromInt(errhp, (dvoid *)&retval,
      sizeof(retval), OCI_NUMBER_SIGNED, rval)))
    return(rval);

  /* Convert idxflag to integer from OCINumber */
  if (qxiqtce(ctx, errhp, OCINumberToInt(errhp, &(ix->IndexInfoFlags),
      sizeof(idxflag), OCI_NUMBER_UNSIGNED, ( void *)&idxflag)))
    return(rval);

  /*****************************
  * Construct insert Statement *
  ******************************/
  if ((idxflag & ODCI_INDEX_RANGE_PARTN) != ODCI_INDEX_RANGE_PARTN)
    (void)sprintf(insstmt, "INSERT into %s.%s_sbtree values (:newval, :mrid)",
      OCIStringPtr(envhp, ix->IndexSchema), OCIStringPtr(envhp, ix->IndexName));
  else
  {
    if (qxiqtce(ctx, errhp, OCICollGetElem(envhp, errhp, (OCIColl *)ix->IndexCols,
        (sb4)0, &exists, (void **) &colinfo, (void **) &colinfo_ind)))
      return(rval);
 
  (void)sprintf(insstmt,
      "INSERT into %s.%s_sbtree partition (SYS_OP_DOBJTOPNUM(%s, :partiden))
        VALUES (:newval, :mrid)",
      OCIStringPtr(envhp, ix->IndexSchema), OCIStringPtr(envhp, ix->IndexName),
      OCIStringPtr(envhp, colinfo->TableName));
  }

  /***************************************
  * Parse and Execute Create Statement   *
  ****************************************/

  /* allocate stmt handle */
  if (qxiqtce(ctx, errhp, OCIHandleAlloc((dvoid *)envhp, (dvoid **)&stmthp,
      (ub4)OCI_HTYPE_STMT, (size_t)0, (dvoid **)0)))
    return(rval);
 
    /* prepare the statement */
    if (qxiqtce(ctx, errhp, OCIStmtPrepare(stmthp, errhp, (text *)insstmt,
        (ub4)strlen(insstmt), OCI_NTV_SYNTAX, OCI_DEFAULT)))
      return(rval);

    if ((idxflag & ODCI_INDEX_RANGE_PARTN) == ODCI_INDEX_RANGE_PARTN)
    {
      /* Convert partiden to integer from OCINumber */
      if (qxiqtce(ctx, errhp, OCINumberToInt(errhp, 
          &(colinfo->TablePartitionIden), sizeof(partiden), OCI_NUMBER_UNSIGNED,
          ( void *)&partiden)))
        return(rval);

      /* Set up bind for partiden */
      if (qxiqtce(ctx, errhp, OCIBindByName(stmthp, &bndp, errhp, 
          text *)":partiden", sizeof(":partiden")-1, (dvoid *)&partiden,
          (sb4)(sizeof(partiden)), (ub2)SQLT_INT, (dvoid *)0, (ub2 *)0,
          (ub2 *)0, (ub4)0, (ub4 *)0, (ub4)OCI_DEFAULT)))
        return(rval);
    }

    /* Set up bind for newval */
    if (qxiqtce(ctx, errhp, OCIBindByName(stmthp, &bndp, errhp, (text *)":newval",
        sizeof(":newval")-1, (dvoid *)newval, (sb4)(strlen(newval)+1),
        (ub2)SQLT_STR, (dvoid *)0, (ub2 *)0, (ub2 *)0, (ub4)0, (ub4 *)0,
        (ub4)OCI_DEFAULT)))
      return(rval);

    /* Set up bind for rid */
    if (qxiqtce(ctx, errhp, OCIBindByName(stmthp, &bndp, errhp, (text *)":mrid",
        sizeof(":mrid")-1, (dvoid *)rid, (sb4)(strlen(rid)+1), (ub2)SQLT_STR, 
        (dvoid *)0, (ub2 *)0, (ub2 *)0, (ub4)0, (ub4 *)0, (ub4)OCI_DEFAULT)))
      return(rval);

    /* Execute statement */
    if (qxiqtce(ctx, errhp, OCIStmtExecute(svchp, stmthp, errhp, (ub4)1,
        (ub4)0, (OCISnapshot *)NULL, (OCISnapshot *)NULL, (ub4)OCI_DEFAULT)))
      return(rval);
 
    /* free stmt handle */
    if (qxiqtce(ctx, errhp, OCIHandleFree((dvoid *)stmthp, (ub4)OCI_HTYPE_STMT)))
      return(rval);

    return(rval);
}
```

Example 16-25 Implementing ODCIIndexDelete() for PSBTREE in C

The delete routine constructs a SQL statement to delete a row from the index table corresponding to the row being deleted from the base table. The row in the index table is identified by the value of `rowid` that is passed in as a parameter to this routine.

```
OCINumber *qxiqtbspd(
  OCIExtProcContext *ctx,
  ODCIIndexInfo     *ix,
  ODCIIndexInfo_ind *ix_ind,
  char              *rid,
  short             rid_ind,
  char              *oldval,
  short             oldval_ind,
  ODCIEnv           *env,
  ODCIEnv_ind       *env_ind)
{
  OCIEnv *envhp = (OCIEnv *) 0;             /* env. handle */
  OCISvcCtx *svchp = (OCISvcCtx *) 0;       /* service handle */
  OCIError *errhp = (OCIError *) 0;         /* error handle */
  OCIStmt *stmthp = (OCIStmt *) 0;          /* statement handle */
  OCIBind *bndp = (OCIBind *) 0;            /* bind handle */
 
  int retval = (int)ODCI_SUCCESS;           /* return from this function */
  OCINumber *rval = (OCINumber *)0;
 
  char delstmt[2000];                       /* sql delete statement */
  ODCIColInfo  *colinfo;                    /* column info */
  ODCIColInfo_ind  *colinfo_ind;
  boolean exists = TRUE;
  unsigned int partiden;                    /* table partition iden */ 
  unsigned int idxflag;                     /* index info flag  
 
  /* Get oci handles */
  if (qxiqtce(ctx, errhp, OCIExtProcGetEnv(ctx, &envhp, &svchp, &errhp)))
    return(rval);
 
  /* set up return code */
  rval = (OCINumber *)OCIExtProcAllocCallMemory(ctx, sizeof(OCINumber));
  if (qxiqtce(ctx, errhp, OCINumberFromInt(errhp, (dvoid *)&retval,
      sizeof(retval), OCI_NUMBER_SIGNED, rval)))
    return(rval);
 
  /* Convert idxflag to integer from OCINumber */
  if (qxiqtce(ctx, errhp, OCINumberToInt(errhp, &(ix->IndexInfoFlags),
      sizeof(idxflag), OCI_NUMBER_UNSIGNED, ( void *)&idxflag)))
    return(rval);
 
  /*****************************
  * Construct delete Statement *
  ******************************/
  if ((idxflag & ODCI_INDEX_RANGE_PARTN) != ODCI_INDEX_RANGE_PARTN)
    (void)sprintf(delstmt, "DELETE FROM %s.%s_sbtree WHERE f2 = :rr",
      OCIStringPtr(envhp, ix->IndexSchema), OCIStringPtr(envhp, ix->IndexName));
  else
  {
    if (qxiqtce(ctx, errhp, OCICollGetElem(envhp, errhp, (OCIColl *)ix->IndexCols,
        (sb4)0, &exists, (void **) &colinfo, (void **) &colinfo_ind)))
      return(rval);

    (void)sprintf(delstmt, 
        "DELETE FROM %s.%s_sbtree partition (SYS_OP_DOBJTOPNUM(%s, :partiden))
          WHERE f2 = :rr",
        OCIStringPtr(envhp, ix->IndexSchema), OCIStringPtr(envhp, ix->IndexName),
        OCIStringPtr(envhp, colinfo->TableName));
  }

  /***************************************
  * Parse and Execute delete Statement   *
  ****************************************/

/* allocate stmt handle */
  if (qxiqtce(ctx, errhp, OCIHandleAlloc((dvoid *)envhp, (dvoid **)&stmthp,
      (ub4)OCI_HTYPE_STMT, (size_t)0, (dvoid **)0)))
    return(rval);

/* prepare the statement */
  if (qxiqtce(ctx, errhp, OCIStmtPrepare(stmthp, errhp, (text *)delstmt,
      (ub4)strlen(delstmt), OCI_NTV_SYNTAX, OCI_DEFAULT)))
    return(rval);

  if ( (idxflag & ODCI_INDEX_RANGE_PARTN) == ODCI_INDEX_RANGE_PARTN)
  {
    /* Convert partiden to integer from OCINumber */
    if (qxiqtce(ctx, errhp, OCINumberToInt(errhp, &(colinfo->TablePartitionIden),
        sizeof(partiden), OCI_NUMBER_UNSIGNED, ( void *)&partiden)))
      return(rval);

    /* Set up bind for partiden */
    if (qxiqtce(ctx, errhp, OCIBindByName(stmthp, &bndp, errhp, 
        (text *)":partiden", sizeof(":partiden")-1, (dvoid *)&partiden,
        sb4)(sizeof(partiden)), (ub2)SQLT_INT, (dvoid *)0, (ub2 *)0,
        (ub2 *)0, (ub4)0, (ub4 *)0, (ub4)OCI_DEFAULT)))
      return(rval);
  }

  /* Set up bind for rid */
  if (qxiqtce(ctx, errhp, OCIBindByName(stmthp, &bndp, errhp, (text *)":rr",
      sizeof(":rr")-1, (dvoid *)rid, (sb4)(strlen(rid)+1), (ub2)SQLT_STR, 
      (dvoid *)0, (ub2 *)0, (ub2 *)0, (ub4)0, (ub4 *)0, (ub4)OCI_DEFAULT)))
    return(rval);

  /* Execute statement */
  if (qxiqtce(ctx, errhp, OCIStmtExecute(svchp, stmthp, errhp, (ub4)1, (ub4)0,
      (OCISnapshot *)NULL, (OCISnapshot *)NULL, (ub4)OCI_DEFAULT)))
    return(rval);

  /* free stmt handle */
  if (qxiqtce(ctx, errhp, OCIHandleFree((dvoid *)stmthp, (ub4)OCI_HTYPE_STMT)))
    return(rval);

  return(rval);
}
```

Example 16-26 Implementing ODCIIndexUpdate() for PSBTree in C

The update routine constructs a SQL statement to update a row in the index table corresponding to the row being updated in the base table. The row in the index table is identified by the value of `rowid` that is passed in as a parameter to this routine. The old column value (`oldval`) is replaced by the new value (`newval`).

```
OCINumber *qxiqtbspu(
  OCIExtProcContext *ctx,
  ODCIIndexInfo     *ix,
  ODCIIndexInfo_ind *ix_ind,
  char              *rid,
  short             rid_ind,
  char              *oldval,
  short             oldval_ind,
  char              *newval,
  short             newval_ind,
  ODCIEnv           *env,
  ODCIEnv_ind       *env_ind)
{
  OCIEnv *envhp = (OCIEnv *) 0;             /* env. handle */
  OCISvcCtx *svchp = (OCISvcCtx *) 0;       /* service handle */
  OCIError *errhp = (OCIError *) 0;         /* error handle */
  OCIStmt *stmthp = (OCIStmt *) 0;          /* statement handle */
  OCIBind *bndp = (OCIBind *) 0;            /* bind handle */

  int retval = (int)ODCI_SUCCESS;           /* return from this function */
  OCINumber *rval = (OCINumber *)0;

  char updstmt[2000];                       /* sql upate statement */
  ODCIColInfo  *colinfo;                    /* column info */
  ODCIColInfo_ind  *colinfo_ind;
  boolean exists = TRUE;
  unsigned int partiden;                    /* table partition iden */ 
  unsigned int idxflag;                     /* index info flag  

  /* Get oci handles */
  if (qxiqtce(ctx, errhp, OCIExtProcGetEnv(ctx, &envhp, &svchp, &errhp)))
    return(rval);

  /* set up return code */
  rval = (OCINumber *)OCIExtProcAllocCallMemory(ctx, sizeof(OCINumber));
  if (qxiqtce(ctx, errhp, OCINumberFromInt(errhp, (dvoid *)&retval,
      sizeof(retval), OCI_NUMBER_SIGNED, rval)))
    return(rval);

  /* Convert idxflag to integer from OCINumber */
  if (qxiqtce(ctx, errhp, OCINumberToInt(errhp, &(ix->IndexInfoFlags),
      sizeof(idxflag), OCI_NUMBER_UNSIGNED, ( void *)&idxflag)))
    return(rval);

  /*****************************
  * Construct update Statement *
  ******************************/
  if ( (idxflag & ODCI_INDEX_RANGE_PARTN) != ODCI_INDEX_RANGE_PARTN)
    (void)sprintf(updstmt, "UPDATE %s.%s_sbtree SET f1 = :newval WHERE f2 = :rr",
        OCIStringPtr(envhp, ix->IndexSchema), OCIStringPtr(envhp, ix->IndexName));
  else
  {
    if (qxiqtce(ctx, errhp, OCICollGetElem(envhp, errhp, OCIColl *)ix->IndexCols,
        (sb4)0, &exists, (void **) &colinfo, (void **) &colinfo_ind)))
      return(rval);

    (void)sprintf(updstmt, "UPDATE %s.%s_sbtree partition 
        (SYS_OP_DOBJTOPNUM(%s, :partiden)) SET f1 = :newval WHERE f2 = :rr",
        OCIStringPtr(envhp, ix->IndexSchema), OCIStringPtr(envhp, ix->IndexName),
        OCIStringPtr(envhp, colinfo->TableName));
  }

  /****************************************
  * Parse and Execute Create Statement   *
  ****************************************/

  /* allocate stmt handle */
  if (qxiqtce(ctx, errhp, OCIHandleAlloc((dvoid *)envhp, (dvoid **)&stmthp,
      (ub4)OCI_HTYPE_STMT, (size_t)0, (dvoid **)0)))
    return(rval);

  /* prepare the statement */
  if (qxiqtce(ctx, errhp, OCIStmtPrepare(stmthp, errhp, (text *)updstmt,
      (ub4)strlen(updstmt), OCI_NTV_SYNTAX, OCI_DEFAULT)))
    return(rval);

  if ( (idxflag & ODCI_INDEX_RANGE_PARTN) == ODCI_INDEX_RANGE_PARTN)
  {
    /* Convert partiden to integer from OCINumber */
    if (qxiqtce(ctx, errhp, OCINumberToInt(errhp, 
        &(colinfo->TablePartitionIden), sizeof(partiden), OCI_NUMBER_UNSIGNED,
        ( void *)&partiden)))
      return(rval);

    /* Set up bind for partiden */
    if (qxiqtce(ctx, errhp, OCIBindByName(stmthp, &bndp, errhp, 
        (text *)":partiden", sizeof(":partiden")-1, (dvoid *)&partiden,
        (sb4)(sizeof(partiden)), (ub2)SQLT_INT, (dvoid *)0, (ub2 *)0,
        (ub2 *)0, (ub4)0, (ub4 *)0, (ub4)OCI_DEFAULT)))
      return(rval);
  }

  /* Set up bind for newval */
  if (qxiqtce(ctx, errhp, OCIBindByName(stmthp, &bndp, errhp, (text *)":newval",
      sizeof(":newval")-1, (dvoid *)newval, (sb4)(strlen(newval)+1), 
      (ub2)SQLT_STR, (dvoid *)0, (ub2 *)0, (ub2 *)0, (ub4)0, (ub4 *)0, (
      ub4)OCI_DEFAULT)))
    return(rval);

  /* Set up bind for rid */
  if (qxiqtce(ctx, errhp, OCIBindByName(stmthp, &bndp, errhp, (text *)":rr",
      sizeof(":rr")-1, (dvoid *)rid, (sb4)(strlen(rid)+1), (ub2)SQLT_STR, 
      (dvoid *)0, (ub2 *)0, (ub2 *)0, (ub4)0, (ub4 *)0, (ub4)OCI_DEFAULT)))
    return(rval);

  /* Execute statement */
  if (qxiqtce(ctx, errhp, OCIStmtExecute(svchp, stmthp, errhp, (ub4)1,
      ub4)0, (OCISnapshot *)NULL, (OCISnapshot *)NULL, (ub4)OCI_DEFAULT)))
    return(rval);

  /* free stmt handle */
  if (qxiqtce(ctx, errhp, OCIHandleFree((dvoid *)stmthp, (ub4)OCI_HTYPE_STMT)))
    return(rval);

  return(rval);
}
```

Example 16-27 Implementing ODCIIndexStart() for PSBTREE in C

The start routine performs the setup for an `psbtree` index scan. The query information in terms of the operator predicate, its arguments, and the bounds on return values are passed in as parameters to this function. The scan context that is shared among the index scan routines is an instance of the type `psbtree_im`.

This function sets up a cursor that scans the index table. The scan retrieves the stored rowids for the rows in the index table that satisfy the specified predicate. The predicate for the index table is generated based on the operator predicate information that is passed in as parameters. For example, if the operator predicate is of the form `eq(col, 'joe') = 1`, then the predicate on the index table is set up to be `f1 = 'joe'`.

This function uses the `struct` s `qxiqtim`, `qxiqtin`, and `qxiqtcx`, which were demonstrated in Example 16-21 and Example 16-22.

```
OCINumber *qxiqtbsps(
  OCIExtProcContext *ctx,
  qxiqtim           *sctx,
  qxiqtin           *sctx_ind,
  ODCIIndexInfo     *ix,
  ODCIIndexInfo_ind *ix_ind,
  ODCIPredInfo      *pr,
  ODCIPredInfo_ind  *pr_ind,
  ODCIQueryInfo     *qy,
  ODCIQueryInfo_ind *qy_ind,
  OCINumber         *strt,
  short             strt_ind,
  OCINumber         *stop,
  short             stop_ind,
  char              *cmpval,
  short             cmpval_ind,
  ODCIEnv           *env,
  ODCIEnv_ind       *env_ind)
{
  sword status;
  OCIEnv *envhp = (OCIEnv *) 0;                               /* env. handle */
  OCISvcCtx *svchp = (OCISvcCtx *) 0;                      /* service handle */
  OCIError *errhp = (OCIError *) 0;                          /* error handle */
  OCISession *usrhp = (OCISession *) 0;                       /* user handle */
  qxiqtcx *icx = (qxiqtcx *) 0;         /* state to be saved for later calls */

  int strtval;                   /* start bound */
  int stopval;                   /* stop bound */

  int errnum = 29400;            /* choose some oracle error number */
  char errmsg[512];              /* error message buffer */
  size_t errmsglen;              /* Length of error message */

  char relop[3];                 /* relational operator used in sql stmt */
  char selstmt[2000];            /* sql select statement */

  int retval = (int)ODCI_SUCCESS;       /* return from this function */
  OCINumber *rval = (OCINumber *)0;
  ub4 key;                              /* key value set in "sctx" */

  ub1 *rkey;                            /* key to retrieve context */
  ub4 rkeylen;                          /* length of key */
  ODCIColInfo  *colinfo;                /* column info */
  ODCIColInfo_ind  *colinfo_ind;
  boolean exists = TRUE;
  unsigned int partiden;                /* table partition iden */ 
  unsigned int idxflag;                 /* index info flag  

  /* Get oci handles */
  if (qxiqtce(ctx, errhp, OCIExtProcGetEnv(ctx, &envhp, &svchp, &errhp)))
    return(rval);

  /* set up return code */
  rval = (OCINumber *)OCIExtProcAllocCallMemory(ctx, sizeof(OCINumber));
  if (qxiqtce(ctx, errhp, OCINumberFromInt(errhp, (dvoid *)&retval,
      sizeof(retval), OCI_NUMBER_SIGNED, rval)))
    return(rval);

  /* get the user handle */
  if (qxiqtce(ctx, errhp, OCIAttrGet((dvoid *)svchp, (ub4)OCI_HTYPE_SVCCTX,
      (dvoid *)&usrhp, (ub4 *)0, (ub4)OCI_ATTR_SESSION, errhp)))
    return(rval);

  /**********************************************/
  /* Allocate memory to hold index scan context */
  /**********************************************/
  if (sctx_ind ->atomic_qxiqtin == OCI_IND_NULL ||
      sctx_ind ->scind_qxiqtin == OCI_IND_NULL)
  {
    if (qxiqtce(ctx, errhp, OCIMemoryAlloc((dvoid *)usrhp, errhp, (dvoid **)&icx,
        OCI_DURATION_STATEMENT, (ub4)(sizeof(qxiqtcx)), OCI_MEMORY_CLEARED)))
    return(rval);

  icx->stmthp = (OCIStmt *)0;
  icx->defnp = (OCIDefine *)0;
  icx->bndp = (OCIBind *)0;
  }

  else
  {
    /*************************/
    /* Retrieve scan context */
    /*************************/
    rkey = OCIRawPtr(envhp, sctx->sctx_qxiqtim);
    rkeylen = OCIRawSize(envhp, sctx->sctx_qxiqtim);

    if (qxiqtce(ctx, errhp, OCIContextGetValue((dvoid *)usrhp, errhp,
        rkey, (ub1)rkeylen, (dvoid **)&(icx))))
      return(rval);
  }

  /***********************************/
  /* Check that the bounds are valid */
  /***********************************/
  /* convert from oci numbers to native numbers */
  if (qxiqtce(ctx, errhp, OCINumberToInt(errhp, strt, sizeof(strtval), 
      OCI_NUMBER_SIGNED, (dvoid *)&strtval)))
    return(rval);

  if (qxiqtce(ctx, errhp, OCINumberToInt(errhp, stop, sizeof(stopval),
      OCI_NUMBER_SIGNED, (dvoid *)&stopval)))
    return(rval);

  /* verify that strtval/stopval are both either 0 or 1 */
  if (!(((strtval == 0) && (stopval == 0)) || ((strtval == 1) && (stopval == 1))))
    {
    strcpy(errmsg, (char *)"Incorrect predicate for sbtree operator");
    errmsglen = (size_t)strlen(errmsg);
    if (OCIExtProcRaiseExcpWithMsg(ctx, errnum, (text *)errmsg, errmsglen)
        != OCIEXTPROC_SUCCESS)
      /* Use cartridge error services here */;
      return(rval);
    }

  /*********************************************/
  /* Generate the SQL statement to be executed */
  /*********************************************/
  if (memcmp((dvoid *)OCIStringPtr(envhp, pr->ObjectName), (dvoid *)"EQ", 2) == 0)
    if (strtval == 1)
      strcpy(relop, (char *)"=");
    else
      strcpy(relop, (char *)"!=");
    else if 
      (memcmp((dvoid *)OCIStringPtr(envhp, pr->ObjectName), (dvoid *)"LT",2) == 0)
      if (strtval == 1)
        strcpy(relop, (char *)"<");
      else
        strcpy(relop, (char *)">=");
      else
        if (strtval == 1)
            strcpy(relop, (char *)">");
          else
            strcpy(relop, (char *)"<=");

  /* Convert idxflag to integer from OCINumber */
  if (qxiqtce(ctx, errhp, OCINumberToInt(errhp, &(ix->IndexInfoFlags),
      sizeof(idxflag), OCI_NUMBER_UNSIGNED, ( void *)&idxflag)))
    return(rval);

  if ( (idxflag & ODCI_INDEX_RANGE_PARTN) != ODCI_INDEX_RANGE_PARTN)
    (void)sprintf(selstmt, "select f2 from %s.%s_sbtree where f1 %s :val",
      OCIStringPtr(envhp, ix->IndexSchema), OCIStringPtr(envhp, ix->IndexName),
      relop);
  else
  {
    if (qxiqtce(ctx, errhp, OCICollGetElem(envhp, errhp, OCIColl *)ix->IndexCols,
        (sb4)0, &exists, (void **) &colinfo, (void **) &colinfo_ind)))
      return(rval);

    /* Convert partiden to integer from OCINumber */
  if (qxiqtce(ctx, errhp, OCINumberToInt(errhp, &(colinfo->TablePartitionIden),
      sizeof(partiden), OCI_NUMBER_UNSIGNED, ( void *)&partiden)))
    return(rval);

  (void)sprintf(selstmt, "select f2 from %s.%s_sbtree partition        (SYS_OP_DOBJTOPNUM(%s, %d)) where f1 %s :val",
      OCIStringPtr(envhp, ix->IndexSchema), OCIStringPtr(envhp, ix->IndexName),
      OCIStringPtr(envhp, colinfo->TableName), partiden, relop);
  }
  
  /***********************************/
  /* Parse, bind, define and execute */
  /***********************************/
  if (sctx_ind ->atomic_qxiqtin == OCI_IND_NULL ||
      sctx_ind ->scind_qxiqtin == OCI_IND_NULL)
  {
    /* allocate stmt handle */
    if (qxiqtce(ctx, errhp, OCIHandleAlloc((dvoid *)envhp, 
        (dvoid **)&(icx->stmthp), (ub4)OCI_HTYPE_STMT, (size_t)0, (dvoid **)0)))  
      return(rval);
  }

  /* prepare the statement */
  if (qxiqtce(ctx, errhp, OCIStmtPrepare(icx->stmthp, errhp, (text *)selstmt,
      (ub4)strlen(selstmt), OCI_NTV_SYNTAX, OCI_DEFAULT)))
    return(rval);

  /* Set up bind for compare value */
  if (qxiqtce(ctx, errhp, OCIBindByName(icx->stmthp, &(icx->bndp), errhp, 
      (text *)":val", sizeof(":val")-1, (dvoid *)cmpval, (sb4)(strlen(cmpval)+1),
      (ub2)SQLT_STR, (dvoid *)0, (ub2 *)0, (ub2 *)0, (ub4)0, (ub4 *)0,
      (ub4)OCI_DEFAULT)))
    return(rval);

  /* Set up define */
  if (qxiqtce(ctx, errhp, OCIDefineByPos(icx->stmthp, &(icx->defnp), errhp,
      (ub4)1, (dvoid *)(icx->ridp), (sb4) sizeof(icx->ridp), (ub2)SQLT_STR, 
      (dvoid *)0, (ub2 *)0, (ub2 *)0, (ub4)OCI_DEFAULT)))
    return(rval);

  /* execute */
  if (qxiqtce(ctx, errhp, OCIStmtExecute(svchp, icx->stmthp, errhp, (ub4)0,
      (ub4)0, (OCISnapshot *)NULL, (OCISnapshot *)NULL, (ub4)OCI_DEFAULT)))
    return(rval);

  /************************************/
  /* Set index context to be returned */
  /************************************/
  if (sctx_ind ->atomic_qxiqtin == OCI_IND_NULL ||
      sctx_ind ->scind_qxiqtin == OCI_IND_NULL)
  {
    /* generate a key */
    if (qxiqtce(ctx, errhp, OCIContextGenerateKey((dvoid *)usrhp, errhp, &key)))
      return(rval);

    /* set the memory address of the struct to be saved in the context */
    if (qxiqtce(ctx, errhp, OCIContextSetValue((dvoid *)usrhp, errhp,
        OCI_DURATION_STATEMENT, (ub1 *)&key, (ub1)sizeof(key), (dvoid *)icx)))
      return(rval);

    /* statement duration memory alloc for key */ 
    if (qxiqtce(ctx, errhp, OCIMemoryAlloc(( void *)usrhp, errhp,
        ( void **)&(sctx->sctx_qxiqtim), OCI_DURATION_STATEMENT,
        (sb4)(sizeof(key)+sizeof(ub4)), OCI_MEMORY_CLEARED)))
      return(rval);

    /* set the key as the member of "sctx" */
    if (qxiqtce(ctx, errhp, OCIRawAssignBytes(envhp, errhp, (ub1 *)&key,
        ub4)sizeof(key), &(sctx->sctx_qxiqtim))))
      return(rval);

    sctx_ind->atomic_qxiqtin = OCI_IND_NOTNULL;
    sctx_ind->scind_qxiqtin = OCI_IND_NOTNULL;

    return(rval);
  }

  return(rval);
}
```

Example 16-28 Implementing ODCIIndexFetch() for PSBTREE in C

The scan context set up by the start routine is passed in as a parameter to the fetch routine. This function first retrieves the 4-byte key from the scan context. The C mapping for the scan context is `qxiqtim` (see Example 16-21). Next, key is used to look up the OCI context. This gives the memory address of the `qxiqtcx` structure (see Example 16-22) that holds the OCI handles.

This function returns the next batch of rowids that satisfy the operator predicate. It uses the value of the `nrows` parameter as the size of the batch. It repeatedly fetches rowids from the open cursor and populates the `rowid` list. When the batch is full or when there are no more rowids left, the function returns them back to the Oracle server.

```
OCINumber *qxiqtbspf(
  OCIExtProcContext *ctx,
  qxiqtim           *self,
  qxiqtin           *self_ind,
  OCINumber         *nrows,
  short             nrows_ind,
  OCIArray          **rids,
  short             *rids_ind,
  ODCIEnv           *env,
  ODCIEnv_ind       *env_ind)
{
  sword status;
  OCIEnv *envhp = (OCIEnv *) 0;                               /* env. handle */
  OCISvcCtx *svchp = (OCISvcCtx *) 0;                      /* service handle */
  OCIError *errhp = (OCIError *) 0;                          /* error handle */
  OCISession *usrhp = (OCISession *) 0;                       /* user handle */
  qxiqtcx *icx = (qxiqtcx *) 0;         /* state to be saved for later calls */

  int idx = 1;
  int nrowsval;

  OCIArray *ridarrp = *rids;                  /* rowid collection */
  OCIString *ridstr = (OCIString *)0;

  int done = 0;
  int retval = (int)ODCI_SUCCESS;
  OCINumber *rval = (OCINumber *)0;

  ub1 *key;                                   /* key to retrieve context */
  ub4 keylen;                                 /* length of key */

  /*******************/
  /* Get OCI handles */
  /*******************/
  if (qxiqtce(ctx, errhp, OCIExtProcGetEnv(ctx, &envhp, &svchp, &errhp)))
    return(rval);

  /* set up return code */
  rval = (OCINumber *)OCIExtProcAllocCallMemory(ctx, sizeof(OCINumber));
  if (qxiqtce(ctx, errhp, OCINumberFromInt(errhp, (dvoid *)&retval,
      sizeof(retval), OCI_NUMBER_SIGNED, rval)))
    return(rval);

  /* get the user handle */
  if (qxiqtce(ctx, errhp, OCIAttrGet((dvoid *)svchp, (ub4)OCI_HTYPE_SVCCTX,
      (dvoid *)&usrhp, (ub4 *)0, (ub4)OCI_ATTR_SESSION, errhp)))
    return(rval);

  /********************************/
  /* Retrieve context from key    */
  /********************************/
  key = OCIRawPtr(envhp, self->sctx_qxiqtim);
  keylen = OCIRawSize(envhp, self->sctx_qxiqtim);

  if (qxiqtce(ctx, errhp, OCIContextGetValue((dvoid *)usrhp, errhp, key,
      (ub1)keylen, (dvoid **)&(icx))))
    return(rval);

  /* get value of nrows */
  if (qxiqtce(ctx, errhp, OCINumberToInt(errhp, nrows, sizeof(nrowsval),
      OCI_NUMBER_SIGNED, (dvoid *)&nrowsval)))
    return(rval);

  /****************/
  /* Fetch rowids */
  /****************/
  while (!done)
  {
    if (idx > nrowsval)
      done = 1;
    else
    {
      status =OCIStmtFetch(icx->stmthp, errhp, (ub4)1, (ub2) 0, (ub4)OCI_DEFAULT);
      if (status == OCI_NO_DATA)
      {
        short col_ind = OCI_IND_NULL;
        /* have to create dummy oci string */
        OCIStringAssignText(envhp, errhp, (text *)"dummy", (ub2)5, &ridstr);
        /* append null element to collection */
        if (qxiqtce(ctx, errhp, OCICollAppend(envhp, errhp, (dvoid *)ridstr,
            (dvoid *)&col_ind, (OCIColl *)ridarrp)))
          return(rval);
        done = 1;
      }
      else if (status == OCI_SUCCESS)
      {
        OCIStringAssignText(envhp, errhp, (text *)icx->ridp, (ub2)18, 
            OCIString **)&ridstr);
        /* append rowid to collection */
        if (qxiqtce(ctx, errhp, OCICollAppend(envhp, errhp, (dvoid *)ridstr,
            (dvoid *)0, (OCIColl *)ridarrp)))
          return(rval);
        idx++;
      }
      else if (qxiqtce(ctx, errhp, status))
        return(rval);
    }
  }

  /* free ridstr finally */
  if (ridstr &&
      (qxiqtce(ctx, errhp, OCIStringResize(envhp, errhp, (ub4)0, &ridstr))))
    return(rval);

  *rids_ind = OCI_IND_NOTNULL;

  return(rval);
}
```

Example 16-29 Implementing ODCIIndexClose() for PSBTREE in C

The scan context set up by the start routine is passed in as a parameter to the close routine. This function first retrieves the 4-byte key from the scan context. The C mapping for the scan context is `qxiqtim` (see Example 16-21). Next, the OCI context is looked up based on the key. This gives the memory address of the structure that holds the OCI handles, the `qxiqtcx` structure (see Example 16-22).

This function closes and frees all the OCI handles. It also frees the memory that was allocated in the start routine.

```
OCINumber *qxiqtbspc(
  OCIExtProcContext *ctx,
  qxiqtim           *self,
  qxiqtin           *self_ind,
  ODCIEnv           *env,
  ODCIEnv_ind       *env_ind)
{
  sword status;
  OCIEnv *envhp = (OCIEnv *) 0;                               /* env. handle */
  OCISvcCtx *svchp = (OCISvcCtx *) 0;                      /* service handle */
  OCIError *errhp = (OCIError *) 0;                          /* error handle */
  OCISession *usrhp = (OCISession *) 0;                       /* user handle */
  qxiqtcx *icx = (qxiqtcx *) 0;         /* state to be saved for later calls */

  int retval = (int) ODCI_SUCCESS;
  OCINumber *rval = (OCINumber *)0;

  ub1 *key;                                   /* key to retrieve context */
  ub4 keylen;                                 /* length of key */

  if (qxiqtce(ctx, errhp, OCIExtProcGetEnv(ctx, &envhp, &svchp, &errhp)))
    return(rval);

  /* set up return code */
  rval = (OCINumber *)OCIExtProcAllocCallMemory(ctx, sizeof(OCINumber));
  if (qxiqtce(ctx, errhp, OCINumberFromInt(errhp, (dvoid *)&retval,
      sizeof(retval), OCI_NUMBER_SIGNED, rval)))
    return(rval);

  /* get the user handle */
  if (qxiqtce(ctx, errhp, OCIAttrGet((dvoid *)svchp, (ub4)OCI_HTYPE_SVCCTX,
      (dvoid *)&usrhp, (ub4 *)0,
      (ub4)OCI_ATTR_SESSION, errhp)))
    return(rval);
  /********************************/
  /* Retrieve context using key   */
  /********************************/
  key = OCIRawPtr(envhp, self->sctx_qxiqtim);
  keylen = OCIRawSize(envhp, self->sctx_qxiqtim);

  if (qxiqtce(ctx, errhp, OCIContextGetValue((dvoid *)usrhp, errhp, key,
      (ub1)keylen, (dvoid **)&(icx))))
    return(rval);

  /* Free handles and memory */
  if (qxiqtce(ctx, errhp, OCIHandleFree((dvoid *)icx->stmthp, 
      (ub4)OCI_HTYPE_STMT)))
    return(rval);

  if (qxiqtce(ctx, errhp, OCIMemoryFree((dvoid *)usrhp, errhp, (dvoid *)icx)))
    return(rval);

  /* free the memory allocated for the index context. */
  if (qxiqtce(ctx, errhp, OCIContextClearValue((dvoid *)usrhp, errhp, key,
      (ub1)keylen)))
    return(rval);

    return(rval);
}
```

### Implementing the Indextype

You should next create the indextype object and specify the list of operators that it supports. In addition, specify the name of the implementation type that implements the `ODCIIndex` `XXX` `()` interface routines. This step is demonstrated in Example 16-30.

Example 16-30 Implementing the Indextype for PSBTREE

```
CREATE INDEXTYPE psbtree
FOR
eq(VARCHAR2, VARCHAR2),
lt(VARCHAR2, VARCHAR2),
gt(VARCHAR2, VARCHAR2)
USING psbtree_im
WITH LOCAL RANGE PARTITION
WITH SYSTEM MANAGED STORAGE TABLES
```

## Using PSBTREE

One typical usage scenario is to create a range partitioned table and populate it, as demonstrated in Example 16-31.

Example 16-31 Creating and Populating a Partitioned Table for PSBTREE

```
CREATE TABLE t1 (f1 NUMBER, f2 VARCHAR2(200))
PARTITION BY RANGE(f1)
(
  PARTITION p1 VALUES LESS THAN (101),
  PARTITION p2 VALUES LESS THAN (201),
  PARTITION p3 VALUES LESS THAN (301),
  PARTITION p4 VALUES LESS THAN (401)
 );
INSERT INTO t1 VALUES (10, 'aaaa');
INSERT INTO t1 VALUES (200, 'bbbb');
INSERT INTO t1 VALUES (100, 'cccc');
INSERT INTO t1 VALUES (300, 'dddd');
INSERT INTO t1 VALUES (400, 'eeee');
COMMIT;
```

You can then create a `psbtree` index on column `f2`. The `CREATE INDEX` statement specifies the indextype that should be used, as demonstrated in Example 16-32.

Example 16-32 Creating a PSBTREE Index on a Column

```
CREATE INDEX it1 ON t1(f2) iINDEXTYPE IS psbtree LOCAL 
(PARTITION pe1 PARAMETERS('test1'), PARTITION pe2,
 PARTITION pe3, PARTITION pe4 PARAMETERS('test4')) 
PARAMETERS('test');
```

To execute a query that uses one of the `psbtree` operators, use the code in Example 16-33

Example 16-33 Using PSBTREE Operators in a Query

```
SELECT * FROMM t1 WHERE eq(f2, 'dddd') = 1 AND f1>101 ;
```

The explain plan output for this query should look like this:

```
OPERATION            OPTIONS                PARTITION_START       PARTITION_STOP
--------------------------------------------------------------------------------
SELECT STATEMENT
PARTITION RANGE      ITERATOR               2                     4
TABLE ACCESS         BY LOCAL INDEX ROWID   2                     4
DOMAIN INDEX
```
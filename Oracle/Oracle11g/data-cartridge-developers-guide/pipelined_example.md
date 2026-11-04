---
title: "Pipelined Table Functions: Interface Approach Example"
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/pipelined_example.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 17 Pipelined Table Functions: Interface Approach Example

This chapter supplements the discussion of table functions in [Chapter 13, "Using Pipelined and Parallel Table Functions"](pipe_paral_tbl.md). The chapter shows two complete implementations of the `StockPivot` table function using the interface approach. One implementation is done in C and one in Java.

The function `StockPivot` converts a row of the type `(Ticker, OpenPrice, ClosePrice)` into two rows of the form `(Ticker, PriceType, Price)`. For example, from an input row `("ORCL", 41, 42)`, the table function returns the two rows `("ORCL", "O", 41)` and `("ORCL", "C", 42)`.

This chapter contains these topics:

- Pipelined Table Functions Example: C Implementation
- Pipelined Table Functions Example: Java Implementation

## Pipelined Table Functions Example: C Implementation

In this example, the three `ODCITable` interface methods of the implementation type are implemented as external functions in C. These methods must first be declared in SQL.

### Making SQL Declarations for C Implementation

Example 17-1 shows how to make SQL declarations for the methods implemented in C language in section "Implementation ODCITable Methods in C".

Example 17-1 Making SQL Declarations for Implementing ODCITableXXX() in C

```
-- Create the input stock table
CREATE TABLE StockTable (
  ticker VARCHAR(4),
  openprice NUMBER,
  closeprice NUMBER
);

-- Create the types for the table function's output collection 
-- and collection elements

CREATE TYPE TickerType AS OBJECT
(
  ticker VARCHAR2(4),
  PriceType VARCHAR2(1),
   price NUMBER
);
/

CREATE TYPE TickerTypeSet AS TABLE OF TickerType;
/

-- Create the external library object
CREATE LIBRARY StockPivotLib IS '/home/bill/libstock.so';
/

-- Create the implementation type
CREATE TYPE StockPivotImpl AS OBJECT
(
  key RAW(4),

  STATIC FUNCTION ODCITableStart(
    sctx OUT StockPivotImpl, 
    cur SYS_REFCURSOR) 
  RETURN PLS_INTEGER 
  AS LANGUAGE C
  LIBRARY StockPivotLib
  NAME "ODCITableStart"
  WITH CONTEXT
  PARAMETERS (context, sctx, sctx INDICATOR STRUCT, cur, RETURN INT),
 
  MEMBER FUNCTION ODCITableFetch(
    self IN OUT StockPivotImpl, 
    nrows IN NUMBER, 
    outSet OUT TickerTypeSet) 
  RETURN PLS_INTEGER
  AS LANGUAGE C
  LIBRARY StockPivotLib
  NAME "ODCITableFetch"
  WITH CONTEXT
  PARAMETERS (context, self, self INDICATOR STRUCT, nrows, outSet, 
      outSet INDICATOR, RETURN INT),

  MEMBER FUNCTION ODCITableClose(
    self IN StockPivotImpl) 
  RETURN PLS_INTEGER
  AS LANGUAGE C
  LIBRARY StockPivotLib
  NAME "ODCITableClose"
  WITH CONTEXT
  PARAMETERS (context, self, self INDICATOR STRUCT, RETURN INT)
  );
  /

  -- Define the ref cursor type
  CREATE PACKAGE refcur_pkg IS
    TYPE refcur_t IS REF CURSOR RETURN StockTable%ROWTYPE;
  END refcur_pkg;
  /

  -- Create table function
  CREATE FUNCTION StockPivot(p refcur_pkg.refcur_t) RETURN TickerTypeSet
  PIPELINED USING StockPivotImpl;
/
```

### Implementation ODCITable Methods in C

Example 17-2 implements the three `ODCITable` methods as external functions in C.

Example 17-2 Implementing ODCTableXXX() Methods in C

```
#ifndef OCI_ORACLE
# include <oci.h>
#endif
#ifndef ODCI_ORACLE
# include <odci.h>
#endif

/*---------------------------------------------------------------------------
                     PRIVATE TYPES AND CONSTANTS
  ---------------------------------------------------------------------------*/
                
/* The struct holding the user's stored context */

struct StoredCtx
{
  OCIStmt* stmthp;
};
typedef struct StoredCtx StoredCtx;

/* OCI Handles */

struct Handles_t
{
  OCIExtProcContext* extProcCtx;
  OCIEnv* envhp;
  OCISvcCtx* svchp;
  OCIError* errhp;
  OCISession* usrhp;
};
typedef struct Handles_t Handles_t;

/********************** SQL Types C representation **********************/

/* Table function's implementation type */

struct StockPivotImpl
{
  OCIRaw* key;
};
typedef struct StockPivotImpl StockPivotImpl;

struct StockPivotImpl_ind
{
  short _atomic;
  short key;
};
typedef struct StockPivotImpl_ind StockPivotImpl_ind;

/* Table function's output collection element type */

struct TickerType
{
  OCIString* ticker;
  OCIString* PriceType;
  OCINumber price;
};
typedef struct TickerType TickerType;

struct TickerType_ind
{
  short _atomic;
  short ticker;
  short PriceType;
  short price;
};
typedef struct TickerType_ind TickerType_ind;
  
/* Table function's output collection type */

typedef OCITable TickerTypeSet;

/*--------------------------------------------------------------------------*/
/* Static Functions */
/*--------------------------------------------------------------------------*/

static int GetHandles(OCIExtProcContext* extProcCtx, Handles_t* handles);

static StoredCtx* GetStoredCtx(Handles_t* handles, StockPivotImpl* self, 
                               StockPivotImpl_ind* self_ind);

static int checkerr(Handles_t* handles, sword status);

/*--------------------------------------------------------------------------*/
/* Functions definitions */
/*--------------------------------------------------------------------------*/

/* Callout for ODCITableStart */

int ODCITableStart(OCIExtProcContext* extProcCtx, StockPivotImpl*  self, 
                   StockPivotImpl_ind* self_ind, OCIStmt** cur)
{
  Handles_t handles;                   /* OCI hanldes */
  StoredCtx* storedCtx;                /* Stored context pointer */

  ub4 key;                             /* key to retrieve stored context */

  /* Get OCI handles */
  if (GetHandles(extProcCtx, &handles))
    return ODCI_ERROR;

  /* Allocate memory to hold the stored context */
  if (checkerr(&handles, OCIMemoryAlloc((dvoid*) handles.usrhp, handles.errhp,
                                        (dvoid**) &storedCtx,
                                        OCI_DURATION_STATEMENT,
                                        (ub4) sizeof(StoredCtx),
                                        OCI_MEMORY_CLEARED)))
    return ODCI_ERROR;

  /* store the input ref cursor in the stored context */
  storedCtx->stmthp=*cur;

  /* generate a key */
  if (checkerr(&handles, OCIContextGenerateKey((dvoid*) handles.usrhp, 
                                               handles.errhp, &key)))
    return ODCI_ERROR;

  /* associate the key value with the stored context address */
  if (checkerr(&handles, OCIContextSetValue((dvoid*)handles.usrhp, 
                                            handles.errhp,
                                            OCI_DURATION_STATEMENT,
                                            (ub1*) &key, (ub1) sizeof(key),
                                            (dvoid*) storedCtx)))
    return ODCI_ERROR;

  /* stored the key in the scan context */
  if (checkerr(&handles, OCIRawAssignBytes(handles.envhp, handles.errhp, 
                                           (ub1*) &key, (ub4) sizeof(key),
                                           &(self->key))))
    return ODCI_ERROR;

  /* set indicators of the scan context */
  self_ind->_atomic = OCI_IND_NOTNULL;
  self_ind->key = OCI_IND_NOTNULL;

  return ODCI_SUCCESS;
}

/***********************************************************************/

/* Callout for ODCITableFetch */

int ODCITableFetch(OCIExtProcContext* extProcCtx, StockPivotImpl* self, 
                   StockPivotImpl_ind* self_ind, OCINumber* nrows,
                   TickerTypeSet** outSet, short* outSet_ind)
{
  Handles_t handles;                   /* OCI hanldes */
  StoredCtx* storedCtx;                /* Stored context pointer */
  int nrowsval;                        /* number of rows to return */

  /* Get OCI handles */
  if (GetHandles(extProcCtx, &handles))
    return ODCI_ERROR;

  /* Get the stored context */
  storedCtx=GetStoredCtx(&handles,self,self_ind);
  if (!storedCtx) return ODCI_ERROR;

  /* get value of nrows */
  if (checkerr(&handles, OCINumberToInt(handles.errhp, nrows, sizeof(nrowsval),
                                        OCI_NUMBER_SIGNED, (dvoid *)&nrowsval)))
    return ODCI_ERROR;

  /* return up to 10 rows at a time */
  if (nrowsval>10) nrowsval=10;

  /* Initially set the output to null */
  *outSet_ind=OCI_IND_NULL;

  while (nrowsval>0)
  {

    TickerType elem;           /* current collection element */
    TickerType_ind elem_ind;   /* current element indicator */

    OCIDefine* defnp1=(OCIDefine*)0;   /* define handle */
    OCIDefine* defnp2=(OCIDefine*)0;   /* define handle */
    OCIDefine* defnp3=(OCIDefine*)0;   /* define handle */

    sword status;    

    char ticker[5];
    float openprice;
    float closeprice;
    char PriceType[2];

    /* Define the fetch buffer for ticker symbol */
    if (checkerr(&handles, OCIDefineByPos(storedCtx->stmthp, &defnp1,  
                                          handles.errhp, (ub4) 1, 
                                          (dvoid*) &ticker, 
                                          (sb4) sizeof(ticker),
                                          SQLT_STR, (dvoid*) 0, (ub2*) 0,
                                          (ub2*) 0, (ub4) OCI_DEFAULT)))
      return ODCI_ERROR;

    /* Define the fetch buffer for open price */
    if (checkerr(&handles, OCIDefineByPos(storedCtx->stmthp, &defnp2, 
                                          handles.errhp, (ub4) 2, 
                                          (dvoid*) &openprice, 
                                          (sb4) sizeof(openprice),
                                          SQLT_FLT, (dvoid*) 0, (ub2*) 0,
                                          (ub2*) 0, (ub4) OCI_DEFAULT)))
      return ODCI_ERROR;

    /* Define the fetch buffer for closing price */
    if (checkerr(&handles, OCIDefineByPos(storedCtx->stmthp, &defnp3, 
                                          handles.errhp, (ub4) 3, 
                                          (dvoid*) &closeprice, 
                                          (sb4) sizeof(closeprice),
                                          SQLT_FLT, (dvoid*) 0, (ub2*) 0,
                                          (ub2*) 0, (ub4) OCI_DEFAULT)))
      return ODCI_ERROR;

    /* fetch a row from the input ref cursor */
    status = OCIStmtFetch(storedCtx->stmthp, handles.errhp, (ub4) 1,
                          (ub4) OCI_FETCH_NEXT, (ub4) OCI_DEFAULT);

    /* finished if no more data */
    if (status!=OCI_SUCCESS && status!=OCI_SUCCESS_WITH_INFO) break;
 
    /* Initialize the element indicator struct */

    elem_ind._atomic=OCI_IND_NOTNULL;
    elem_ind.ticker=OCI_IND_NOTNULL;
    elem_ind.PriceType=OCI_IND_NOTNULL;
    elem_ind.price=OCI_IND_NOTNULL;

    /* assign the ticker name */
    elem.ticker=NULL;
    if (checkerr(&handles, OCIStringAssignText(handles.envhp, handles.errhp, 
                                               (text*) ticker, 
                                               (ub2) strlen(ticker), 
                                               &elem.ticker)))
      return ODCI_ERROR;

    /* assign the price type */
    elem.PriceType=NULL;
    sprintf(PriceType,"O");
    if (checkerr(&handles, OCIStringAssignText(handles.envhp, handles.errhp, 
                                               (text*) PriceType,
                                               (ub2) strlen(PriceType),
                                               &elem.PriceType)))
      return ODCI_ERROR;

    /* assign the price */
    if (checkerr(&handles, OCINumberFromReal(handles.errhp, &openprice,
                                             sizeof(openprice), &elem.price)))
      return ODCI_ERROR;

    /* append element to output collection */
    if (checkerr(&handles, OCICollAppend(handles.envhp, handles.errhp,
                                         &elem, &elem_ind, *outSet)))
      return ODCI_ERROR;

    /* assign the price type */
    elem.PriceType=NULL;
    sprintf(PriceType,"C");
    if (checkerr(&handles, OCIStringAssignText(handles.envhp, handles.errhp, 
                                               (text*) PriceType,
                                               (ub2) strlen(PriceType),
                                               &elem.PriceType)))
      return ODCI_ERROR;

    /* assign the price */
    if (checkerr(&handles, OCINumberFromReal(handles.errhp, &closeprice,
                                             sizeof(closeprice), &elem.price)))
      return ODCI_ERROR;

    /* append row to output collection */
    if (checkerr(&handles, OCICollAppend(handles.envhp, handles.errhp,
                     &elem, &elem_ind, *outSet)))
      return ODCI_ERROR;

    /* set collection indicator to not null */
    *outSet_ind=OCI_IND_NOTNULL;

    nrowsval-=2;
  }

  return ODCI_SUCCESS;
}

/***********************************************************************/

/* Callout for ODCITableClose */

int ODCITableClose(OCIExtProcContext* extProcCtx, StockPivotImpl* self, 
                   StockPivotImpl_ind* self_ind)
{
  Handles_t handles;                   /* OCI hanldes */
  StoredCtx* storedCtx;                /* Stored context pointer */

  /* Get OCI handles */
  if (GetHandles(extProcCtx, &handles))
    return ODCI_ERROR;

  /* Get the stored context */
  storedCtx=GetStoredCtx(&handles,self,self_ind);
  if (!storedCtx) return ODCI_ERROR;

  /* Free the memory for the stored context */
  if (checkerr(&handles, OCIMemoryFree((dvoid*) handles.usrhp, handles.errhp, 
                                       (dvoid*) storedCtx)))
    return ODCI_ERROR;

  return ODCI_SUCCESS;
}

/***********************************************************************/

/* Get the stored context using the key in the scan context */

static StoredCtx* GetStoredCtx(Handles_t* handles, StockPivotImpl* self, 
                               StockPivotImpl_ind* self_ind)
{
  StoredCtx *storedCtx;           /* Stored context pointer */
  ub1 *key;                       /* key to retrieve context */
  ub4 keylen;                     /* length of key */
  
  /* return NULL if the PL/SQL context is NULL */
  if (self_ind->_atomic == OCI_IND_NULL) return NULL;

  /* Get the key */
  key = OCIRawPtr(handles->envhp, self->key);
  keylen = OCIRawSize(handles->envhp, self->key);
  
  /* Retrieve stored context using the key */
  if (checkerr(handles, OCIContextGetValue((dvoid*) handles->usrhp, 
                                           handles->errhp,
                                           key, (ub1) keylen, 
                                           (dvoid**) &storedCtx)))
    return NULL;

  return storedCtx;
}

/***********************************************************************/

/* Get OCI handles using the ext-proc context */

static int GetHandles(OCIExtProcContext* extProcCtx, Handles_t* handles)
{
  /* store the ext-proc context in the handles struct */
  handles->extProcCtx=extProcCtx;

  /* Get OCI handles */
  if (checkerr(handles, OCIExtProcGetEnv(extProcCtx, &handles->envhp,
                          &handles->svchp, &handles->errhp)))
    return -1;

  /* get the user handle */
  if (checkerr(handles, OCIAttrGet((dvoid*)handles->svchp,
                                   (ub4)OCI_HTYPE_SVCCTX, 
                                   (dvoid*)&handles->usrhp,
                                   (ub4*) 0, (ub4)OCI_ATTR_SESSION, 
                                   handles->errhp)))
    return -1;

  return 0;
}

/***********************************************************************/

/* Check the error status and throw exception if necessary */

static int checkerr(Handles_t* handles, sword status)
{
  text errbuf[512];     /* error message buffer */
  sb4 errcode;          /* OCI error code */

  switch (status)
  {
  case OCI_SUCCESS:
  case OCI_SUCCESS_WITH_INFO:
    return 0;
  case OCI_ERROR:
    OCIErrorGet ((dvoid*) handles->errhp, (ub4) 1, (text *) NULL, &errcode,
                 errbuf, (ub4) sizeof(errbuf), (ub4) OCI_HTYPE_ERROR);
    sprintf((char*)errbuf, "OCI ERROR code %d",errcode);
    break;
  default:
    sprintf((char*)errbuf, "Warning - error status %d",status);
    break;
  }

  OCIExtProcRaiseExcpWithMsg(handles->extProcCtx, 29400, errbuf,
    strlen((char*)errbuf));

  return -1;
}
```

## Pipelined Table Functions Example: Java Implementation

In this example, the declaration of the implementation type references Java methods instead of C functions. This is the only change from the preceding, C example: all the other objects (`TickerType`, `TickerTypeSet`, `refcur_pkg`, `StockTable`, and `StockPivot`) are the same. These methods must first be declared in SQL.

### Making SQL Declarations for Java Implementation

Example 17-3 shows how to make SQL declarations for the methods implemented in C language in section "Implementing the ODCITable Methods in Java".

Example 17-3 Making SQL Declarations for Implementing OCITableXXX() in Java

```
// create the directory object

CREATE OR REPLACE DIRECTORY JavaDir AS '/home/bill/Java';

// compile the java source

CREATE AND COMPILE JAVA SOURCE NAMED source01
USING BFILE (JavaDir,'StockPivotImpl.java');
/
show errors

-- Create the implementation type

CREATE TYPE StockPivotImpl AS OBJECT
(
  key INTEGER,

  STATIC FUNCTION ODCITableStart(sctx OUT StockPivotImpl, cur SYS_REFCURSOR)
    RETURN NUMBER
    AS LANGUAGE JAVA
    NAME 'StockPivotImpl.ODCITableStart(oracle.sql.STRUCT[], java.sql.ResultSet) return java.math.BigDecimal',

  MEMBER FUNCTION ODCITableFetch(self IN OUT StockPivotImpl, nrows IN NUMBER,
                                 outSet OUT TickerTypeSet) RETURN NUMBER
    AS LANGUAGE JAVA
    NAME 'StockPivotImpl.ODCITableFetch(java.math.BigDecimal, oracle.sql.ARRAY[]) return java.math.BigDecimal',

  MEMBER FUNCTION ODCITableClose(self IN StockPivotImpl) RETURN NUMBER
    AS LANGUAGE JAVA
    NAME 'StockPivotImpl.ODCITableClose() return java.math.BigDecimal'

);
/
show errors
```

### Implementing the ODCITable Methods in Java

Example 17-4 implements the three `ODCITable` methods as external functions in Java.

Example 17-4 Implementing ODCITableXXX() Methods in Java

```
import java.io.*;
import java.util.*;
import oracle.sql.*;
import java.sql.*;
import java.math.BigDecimal;
import oracle.CartridgeServices.*;

// stored context type

public class StoredCtx
{
  ResultSet rset;
  public StoredCtx(ResultSet rs) { rset=rs; }
}

// implementation type

public class StockPivotImpl implements SQLData 
{
  private BigDecimal key;

  final static BigDecimal SUCCESS = new BigDecimal(0);
  final static BigDecimal ERROR = new BigDecimal(1);
  
  // Implement SQLData interface.

  String sql_type;
  public String getSQLTypeName() throws SQLException 
  {
    return sql_type;
  }

  public void readSQL(SQLInput stream, String typeName) throws SQLException 
  {
    sql_type = typeName;
    key = stream.readBigDecimal();
  }

  public void writeSQL(SQLOutput stream) throws SQLException 
  {
    stream.writeBigDecimal(key);
  }
  
  // type methods implementing ODCITable interface

  static public BigDecimal ODCITableStart(STRUCT[] sctx,ResultSet rset)
    throws SQLException 
  {
    Connection conn = DriverManager.getConnection("jdbc:default:connection:");

    // create a stored context and store the result set in it
    StoredCtx ctx=new StoredCtx(rset);

    // register stored context with cartridge services
    int key;
    try {
      key = ContextManager.setContext(ctx);
    } catch (CountException ce) {
      return ERROR;
    }

    // create a StockPivotImpl instance and store the key in it
    Object[] impAttr = new Object[1];
    impAttr[0] = new BigDecimal(key); 
    StructDescriptor sd = new StructDescriptor("STOCKPIVOTIMPL",conn);
    sctx[0] = new STRUCT(sd,conn,impAttr);
      
    return SUCCESS;
  }

  public BigDecimal ODCITableFetch(BigDecimal nrows, ARRAY[] outSet)
    throws SQLException 
  {
    Connection conn = DriverManager.getConnection("jdbc:default:connection:");

    // retrieve stored context using the key
    StoredCtx ctx;
    try {
      ctx=(StoredCtx)ContextManager.getContext(key.intValue());
    } catch (InvalidKeyException ik ) {
      return ERROR;
    }

    // get the nrows parameter, but return up to 10 rows
    int nrowsval = nrows.intValue();
    if (nrowsval>10) nrowsval=10;

    // create a vector for the fetched rows
    Vector v = new Vector(nrowsval);
    int i=0;

    StructDescriptor outDesc = 
      StructDescriptor.createDescriptor("TICKERTYPE", conn);
    Object[] out_attr = new Object[3];

    while(nrowsval>0 && ctx.rset.next()){
      out_attr[0] = (Object)ctx.rset.getString(1);
      out_attr[1] = (Object)new String("O");
      out_attr[2] = (Object)new BigDecimal(ctx.rset.getFloat(2));
      v.add((Object)new STRUCT(outDesc, conn, out_attr));

      out_attr[1] = (Object)new String("C");
      out_attr[2] = (Object)new BigDecimal(ctx.rset.getFloat(3));
      v.add((Object)new STRUCT(outDesc, conn, out_attr));

      i+=2;
      nrowsval-=2;
    }

    // return if no rows found
    if(i==0) return SUCCESS;

    // create the output ARRAY using the vector
    Object out_arr[] = v.toArray();
    ArrayDescriptor ad = new ArrayDescriptor("TICKERTYPESET",conn);
    outSet[0] = new ARRAY(ad,conn,out_arr);
   
    return SUCCESS;
  }

  public BigDecimal ODCITableClose() throws SQLException {
    
    // retrieve stored context using the key, and remove from ContextManager
    StoredCtx ctx;
    try {
      ctx=(StoredCtx)ContextManager.clearContext(key.intValue());
    } catch (InvalidKeyException ik ) {
      return ERROR;
    }

    // close the result set
    Statement stmt = ctx.rset.getStatement();
    ctx.rset.close();
    if(stmt!=null) stmt.close();

    return SUCCESS;
  }

}
```
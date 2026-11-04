---
title: User-Defined Aggregate Functions Interface
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/ext_agg_ref.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 22 User-Defined Aggregate Functions Interface

This chapter describes the routines that must be implemented to define a user-defined aggregate function. The routines are implemented as methods in an object type. Then the `CREATE FUNCTION` statement is used to actually create the aggregate function.

This chapter contains the following topics:

- User-Defined Aggregate Functions

See Also:

[Chapter 11, "Using User-Defined Aggregate Functions"](aggr_functions.md)

## User-Defined Aggregate Functions

The methods in this section are implemented as methods in an object type. The `CREATE FUNCTION` statement is used to actually create the aggregate function. Table 22-1 summarizes these functions.

Table 22-1 Summary of User-Defined Aggregate Functions

| Function | Description |
| --- | --- |
| ODCIAggregateDelete() | Removes an input value from the current group. |
| ODCIAggregateInitialize() | Initializes the aggregation context and instance of the implementation object type, and returns it as an `OUT` parameter. |
| ODCIAggregateIterate() | Iterates through input rows by processing the input values, updating and then returning the aggregation context. |
| ODCIAggregateMerge() | Merges two aggregation contexts into a single object instance during either serial or parallel evaluation of the user-defined aggregate. |
| ODCIAggregateTerminate() | Calculates the result of the aggregate computation and performs all necessary cleanup, such as freeing memory. |
| ODCIAggregateWrapContext() | Integrates all external pieces of the current aggregation context to make the context self-contained. |

### ODCIAggregateDelete()

Removes an input value from the current group. The routine is invoked by Oracle by passing in the aggregation context and the value of the input to be removed during It processes the input value, updates the aggregation context, and returns the context. This is an optional routine and is implemented as a member method.

Syntax

```
MEMBER FUNCTION ODCIAggregateDelete(
   self IN OUT <impltype>, 
   val <inputdatatype>) 
RETURN NUMBER
```

| Parameter | IN/OUT | Description |
| --- | --- | --- |
| ``` self ``` | ``` IN OUT ``` | As input, the value of the current aggregation context; as output, the updated value. |
| ``` val ``` | ``` IN ``` | The input value that is being removed from the current group. |

Returns

`ODCIConst.Success` on success, or `ODCIConst.Error` on error.

### ODCIAggregateInitialize()

Initializes the aggregation context and instance of the implementation object type, and returns it as an `OUT` parameter. Implement this routine as a static method.

Syntax

```
STATIC FUNCTION ODCIAggregateInitialize(
   actx IN OUT <impltype>) 
RETURN NUMBER
```

| Parameter | In/Out | Description |
| --- | --- | --- |
| ``` actx ``` | ``` IN OUT ``` | The aggregation context that is initialized by the routine. This value is `NULL` for regular aggregation cases. In aggregation over windows, `actx` is the context of the previous window. This object instance is passed in as a parameter to the next aggregation routine. |

Returns

`ODCIConst.Success` on success, or `ODCIConst.Error` on error.

### ODCIAggregateIterate()

Iterates through input rows by processing the input values, updating and then returning the aggregation context. Invoked for each value, including `NULL` s. This is a mandatory routine and is implemented as a member method.

Syntax

```
MEMBER FUNCTION ODCIAggregateIterate(
   self IN OUT <impltype>, 
   val <inputdatatype>) 
RETURN NUMBER
```

| Parameter | IN/OUT | Description |
| --- | --- | --- |
| ``` self ``` | ``` IN OUT ``` | As input, the value of the current aggregation context; as output, the updated value. |
| ``` val ``` | ``` IN ``` | The input value that is being aggregated. |

Returns

`ODCIConst.Success` on success, or `ODCIConst.Error` on error.

### ODCIAggregateMerge()

Merges two aggregation contexts into a single object instance during either serial or parallel evaluation of the user-defined aggregate. This is a mandatory routine and is implemented as a member method.

Syntax

```
MEMBER FUNCTION ODCIAggregateMerge(
   self IN OUT <impltype>, 
   ctx2 IN <impltype>)
RETURN NUMBER
```

| Parameter | IN/OUT | Description |
| --- | --- | --- |
| ``` self ``` | ``` IN OUT ``` | On input, the value of the first aggregation context; on output, the resulting value of the two merged aggregation contexts. |
| ``` ctx2 ``` | ``` IN ``` | The value of the second aggregation context. |

Returns

`ODCIConst.Success` on success, or `ODCIConst.Error` on error.

### ODCIAggregateTerminate()

Calculates the result of the aggregate computation and performs all necessary cleanup, such as freeing memory. Invoked by Oracle as the last step of aggregate computation. This is a mandatory routine and is implemented as a member method.

Syntax

```
MEMBER FUNCTION ODCIAggregateTerminate(
   self IN <impltype>, 
   ReturnValue OUT <return_type>, 
   flags IN number) 
RETURN NUMBER
```

| Parameter | IN/OUT | Description |
| --- | --- | --- |
| ``` self ``` | ``` IN ``` | The value of the aggregation context. |
| ``` ctx2 ``` | ``` OUT ``` | The resultant aggregation value. |
| ``` flags ``` | ``` IN ``` | A bit vector that indicates various options. A set bit of `ODCI_AGGREGATE_REUSE_CTX` indicates that the context is reused and any external context should not be freed. |

Returns

`ODCIConst.Success` on success, or `ODCIConst.Error` on error.

See Also:

["Reusing the Aggregation Context for Analytic Functions"](aggr_functions.md) for details on setting the `ODCI_AGGREGATE_REUSE_CTX` flag bit.

### ODCIAggregateWrapContext()

Integrates all external pieces of the current aggregation context to make the context self-contained. Invoked by Oracle if the user-defined aggregate has been declared to have external context and is transmitting partial aggregates from slave processes. This is an optional routine and is implemented as a member method.

Syntax

```
MEMBER FUNCTION ODCIAggregateWrapContext(
   self IN OUT <impltype>) 
RETURN NUMBER
```

| Parameter | IN/OUT | Description |
| --- | --- | --- |
| ``` self ``` | ``` IN ``` | On input, the value of the current aggregation context; on output, the self-contained combined aggregation context. |

Returns

`ODCIConst.Success` on success, or `ODCIConst.Error` on error.

See Also:

["Handling Large Aggregation Contexts"](aggr_functions.md) for more information on using this function
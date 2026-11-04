---
title: Designing Data Cartridges
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/cart_design.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 14 Designing Data Cartridges

This chapter discusses various design considerations related to data cartridges.

This chapter includes these topics:

## Choosing the Programming Language

You can implement methods for object types in PL/SQL, C/C++, or Java. PL/SQL and Java methods run in the address space of the server. C/C++ methods are dispatched as external procedures and run outside the address space of the server.

The best implementation choice depends on the situation. Here are some guidelines:

- A callout involving C or C++ is generally fastest if the processing is substantially CPU-bound. However, callouts incur the cost of dispatch, which might be important for small amounts of processing in C/C++.
- PL/SQL is most efficient for methods that are not computation-intensive. The other implementation options are typically favored over PL/SQL if you have a large body of code implemented in another language, and it can be used by the data cartridge, or if you must perform extensive computations.
- Java is a relatively open implementation choice. Although Java is usually interpreted, high-performance applications might benefit from pre-compilation of methods or just-in-time compilers.

## Invoker's Rights

The invoker's rights mechanism lets a function execute with the privileges of the invoker. Thus, a cartridge can live within a schema dedicated to it, which can be used by other schemas without privileges for operating on objects in the schema where the cartridge resides.

## Callouts and LOBs

When using `LOB` s with callouts, consider the following:

- It can be to your advantage to code your callout so that it is independent of `LOB` types (`BFILE` / `BLOB`).
- The PL/SQL layer of your cartridge can open your `BFILE` so that no `BFILE` -specific logic is required in your callout (other than error recovery from `OCILob` calls that do not operate on `BFILE` s).
- With the advent of temporary `LOB` s, you must be aware of the deep copy that can occur when assignments and calls are done with temporary `LOB` s. Use `NOCOPY` (`BY REFERENCE`) on `BLOB` parameters as appropriate.

## Saving and Passing State

Traditionally, external procedures have a state-less model. All statement handles opened during the invocation of an external procedure are closed implicitly at the end of the call.

Oracle Database allows state information, such as OCI statement handles and associated state in the database, to be saved and used across invocations of external procedures in a session. By default, cartridges are stateless; however, you can use `OCIMemory` services and `OCIContext` services with `OCI_DURATION_SESSION` or other appropriate duration to save state. Statement handles created in one external procedure invocation can be re-used in another. As the data cartridge developer, you must explicitly free these handles. Oracle recommends that you do this as soon as the statement handle is no longer needed. All state maintained for the statement in the OCI handles and in the database is freed as a result. This helps to improve the scalability of your data cartridge.

See Also:

Oracle Database PL/SQL Language Reference

## Designing Indexes

This section discusses some factors you should consider when designing indexes for your data cartridge.

### Domain Index Performance

Creating a domain index is not always the best course. If you decide to create a domain index, keep the following factors in mind:

- For complex domain indexes, the functional implementation works better with small data size and when results are a large percentage of the total data size.
- Judicious use of the extensible optimizer can improve performance.

### Domain Index Component Names

Naming internal components for a domain index implementation can be an issue. Names of internal data objects are typically based on names you provide for table and indexes. The problem is that the derived names for the internal objects must not conflict with any other user-defined object or system object. To avoid this problem, develop some policy that restricts names, or implement some metadata management scheme to avoid errors during `DROP`, `CREATE`, and so on.

### When to Use Index-Organized Tables

You can create secondary indexes on IOT because using them is more efficient than storing data in a table and a separate index, particularly if most of your data is in the index. This offers a big advantage if you are accessing the data in multiple ways. Note that before the Oracle9i release, you could create only one index on IOTs.

### Storing Index Structures in LOBs

Index structures can be stored in `LOB` s, but take care to tune the `LOB` for best performance. If you are accessing a particular `LOB` frequently, create your table with the `CACHE` option and place the `LOB` index in a separate tablespace. If you are updating a `LOB` frequently, `TURN` `OFF` `LOGGING` and read/write in multiples of `CHUNK` size. If you are accessing a particular portion of a `LOB` frequently, buffer your reads/writes using `LOB` buffering or your own buffering scheme.

### External Index Structures

With the extensible indexing framework, the meaning and representation of a user-defined index is left to the cartridge developer. Oracle provides basic index implementations such as IOTs. In certain cases, binary or character `LOB` s can also be used to store complex index structures. IOTs, `BLOB` s and `CLOB` s all live within the database. In addition to them, you may also store a user-defined index as a structure external to the database, for example in a `BFILE`.

The external index structure gives you the most flexibility in representing your index. An external index structure is particularly useful if you have invested in the development of in-memory indexing structures. For example, an operating system file may store index data, which is read into a memory mapped file at run time. Such a case can be handled as a `BFILE` in the external index routines.

External index structures may also provide superior performance, although this gain comes at some cost. Index structures external to the database do not participate in the transaction semantics of the database, which, in the case of index structures inside the database, make data and concomitant index updates atomic. This means that if an update to the data causes an update for the external index to be invoked through the extensible indexing interface, failures can cause the data updates to be rolled back but not the index updates. The database can only roll back what is internal to it: external index structures cannot be rolled back in synchronization with a database rollback. External index structures are perhaps most useful for read-only access. Their semantics become complex if updates to data are involved.

### Multi-Row Fetch

When the [ODCIIndexFetch()](ext_idx_ref.md) routine is called, the rowids of all the rows that satisfy the operator predicate are returned. The maximum number of rows that can be returned by the [ODCIIndexFetch()](ext_idx_ref.md) routine is `nrows` (`nrows` being an argument to the [ODCIIndexFetch()](ext_idx_ref.md) routine). The value of `nrows` is decided by Oracle based on some internal factors. If you have a better idea of the number of rows that ought to be returned to achieve optimal query performance, you can determine that this number of rows is returned in the `ODCIRidList` `VARRAY` instead of `nrows`. Note that the number of values in the `ODCIRidList` must be less than or equal to `nrows`.

As the cartridge designer, you are in the best position to make a judgement regarding the number of rows to be returned. For example, if in the index `1500` rowids are stored together, and `nrows = 2000`, then it may be optimal to return `1500` rows instead of `2000` rows. Otherwise, the user would have to retrieve `3000` rowids, return `2000` of them, and note which `1000` rowids were not returned.

If you do not have any specific optimization in mind, you can use the value of `nrows` to determine the number of rows to be returned. Currently the value of `nrows` has been set to `2000`.

If you implement indexes that use callouts, use multirow fetch to fetch the largest number of rows back to the server. This offsets the cost of making the callout.

## Designing Operators

All domain indexes should contain both indexed and functional implementations of operators, in case the optimizer chooses not to use the indexed implementation. You can, however, use the indexing structures to produce the functional result.

## Designing for the Extensible Optimizer

Data cartridges can be more efficient if they are designed with the extensible optimizer in mind. This section discusses topics that help you create such a design.

### Weighing Cost and Selectivity

When estimating cost, Oracle considers the costs associated with CPU, I/O, and Network.

### Cost for functions

You can determine the cost of executing a C function using common profilers or tools. For SQL queries, an explain plan of the query gives a rough estimate of the cost of the query. In addition, the `tkprof` utility helps you gather information about the CPU and the I/O cost involved in the operation. You can also determine the cost of executing a callout by using it in a SQL query which "selects from dual" and then estimating its cost using `tkprof`.

#### Selectivity for Functions

The selectivity of a predicate is the number of rows returned by the predicate divided by the total number of rows in the tables. Selectivity refers to the fraction of rows of the table returned by the predicate.

The selectivity function should use the statistics collected for the table to determine what percentage of rows of the table the predicate returns with the given list of arguments. For example, to compute the selectivity of a predicate `IMAGE_GREATER_THAN` (`Image` `SelectedImage`) which determines the images that are greater than the `Image` `SelectedImage`, you might use a histogram of the sizes of the images in the database to compute the selectivity.

Statistics can affect the calculation of selectivity for predicates and the cost of domain indexes.

#### Statistics for Tables

The statistics collected for a table can affect the computation of selectivity of a predicate. Thus, statistics that help the user make a better judgement about the selectivity of a predicate should be collected for tables and columns. Knowing the predicates that can operate on the data is helpful in determining what statistics to collect.

For example, in a spatial domain the average, minimum, and maximum number of elements in a `VARRAY` that contains the nodes of the spatial objects is a useful statistic to collect.

#### Statistics for Indexes

When a domain index is analyzed, statistics for the underlying objects that constitute the domain index should be analyzed. For example, if the domain index is composed of tables, the statistics collection function should analyze the tables when the domain index is analyzed. The cost of accessing the domain index can be influenced by the statistics that have been collected for the index. For instance, the cost of accessing a domain index could be approximated as the selectivity times the total number of data blocks in the various tables being accessed when the domain index is accessed.

To define cost, selectivity and statistics functions accurately requires a good understanding of the domain. The preceding guidelines are meant to help you understand some issues you must take into account while working on the cost, selectivity and statistics functions. In general it may be a good idea to start by using the default cost and selectivity, and observing how queries of interest behave.

## Designing for Maintenance

When you design a data cartridge, keep in mind the issues regarding maintenance.

In particular, if your cartridge maintains a large number of objects, views, tables, and so on, consider making a metadata table to maintain the relationships among the objects for the user. This reduces the complexity of developing and maintaining the cartridge when it is in use.

## Enabling Cartridge Installation

- Include a `README` with your cartridge to tell users how to install the cartridge.
- Make the cartridge installable in one step in the database, if possible, such as in `sqlplus @imginst`.
- Tell users how to start the `listener` if you are using callouts.
- Tell users how to setup `extproc`. Most users have never heard of `extproc` and many users have never set up a listener. This is the primary problem when deploying cartridges.
- With the Oracle Software Packager, you can easily create custom SQL install scripts using the `instantiate_file` action. This feature lets you substitute variables in your files when they are installed and it leaves your user with scripts and files that are customized for their installation.

See Also:

[Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_externproc.htm#ADFNS010) for information on setting up the `listener` and `extproc`

## Designing for Portability

To make your data cartridge more portable, consider the following:

- Use the data types in `oratypes.h`.
- Use OCI calls where ever possible.
- Use the switches that enforce ANSI C conformance when possible.
- Use ANSI C function prototypes.
- Build and test on your target platforms as early in your development cycle as possible. This helps you locate platform-specific code and provides the maximum amount of time to redesign.

Portability is reduced by:

- Storing endian (big/little) specific data
- Storing floating point data (IEEE/VAX/other)
- Operating system-specific calls (if you must use them, isolate them in a layer specific to the operating system; however, if the calls you require are not in the OCI, and also are not in POSIX, then you are likely to encounter intractable problems)
- Implicitly casting `int` as `size_t` on a 64-bit platform
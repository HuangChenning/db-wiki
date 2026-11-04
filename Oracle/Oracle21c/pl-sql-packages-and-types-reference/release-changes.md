---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/release-changes.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## Changes in This Release for Oracle Database PL/SQL Packages and Types Reference

This preface contains:

- Changes in Oracle Database Release 21c, Version 21.1

### Changes in Oracle Database Release 21c, Version 21.1

The following are changes in Oracle Database PL/SQL Packages and Types Reference for Oracle Database release 21c, version 21.1.

#### New Features

This section lists the major new features in Oracle Database release 21c PL/SQL Packages and Types Reference.

The following features are new in this release:

- The `DBMS_OPTIM_BUNDLE` package is used to manage the installed but disabled module bug fixes which cause an execution plan change.
	[DBMS\_OPTIM\_BUNDLE](dbms_optim_bundle.md)
- The `DBMS_AUTO_MV` package provides the following new `PL/SQL` procedures functions and procedures for automatic materialized views. This performs analysis and recommendation, verification, and maintenance of automatic materialized views.
	See, [DBMS\_AUTO\_MV](DBMS_AUTO_MV.md).
- The `DBMS_ACTIVITY` package provides the following new `PL/SQL` procedures functions and procedures for Object Activity Tracking System (OATS). This is a generic RDBMS based tracking service that provides information about various types of activities associated with different database objects.
	See, [DBMS\_ACTIVITY](DBMS_ACTIVITY.md).
- The `DBMS_FLASHBACK_ARCHIVE_MIGRATE` package provides new `PL/SQL` functions and procedures for exporting and importing the Flashback Archive base tables along with their history to another database using the Transportable Tablespaces.
	See, [DBMS\_FLASHBACK\_ARCHIVE\_MIGRATE](dbms_flashback_archive_migrate.md).
- The `DBMS_MLE` package provides new `PL/SQL` functions and procedures that allows users to execute JavaScript code inside the Oracle Database and exchange data seamlessly between `PL/SQL` and JavaScript. The JavaScript code itself can execute `PL/SQL` and `SQL` through built-in JavaScript modules. JavaScript data types are automatically mapped to Oracle Database data types and vice versa.
	See, [DBMS\_MLE](dbms_mle.md).
- The `DBMS_AVTUNE` package provides new `PL/SQL` functions and procedures to analyze query access levels and aggregation workloads for each auto-cache enabled analytic view (AV) and creates or drops AV auto-caches to improve the overall performance of the SQL queries on that AV.
- The following new subprograms were introduced in the `DBMS_HIERARCHY` package:
	- `CREATE_VIEW_FOR_FACT_ROWS Procedure`
		- `CREATE_VIEW_FOR_STAR_ROWS Procedure`
		- `GET_MV_SQL_FOR_AV_CACHE Function`
		- `GET_MV_SQL_FOR_STAR_CACHE Function`
- Blockchain tables are append-only tables in which only insert operations are allowed. Deleting rows is either prohibited or restricted based on time. Rows in a blockchain table are made tamper-resistant by special sequencing & chaining algorithms. Users can verify that rows have not been tampered. A hash value that is part of the row metadata is used to chain and validate rows.
	Blockchain tables enable you to implement a centralized ledger model where all participants in the blockchain network have access to the same tamper-resistant ledger. The following new packages are available in this release:
	- `DBMS_BLOCKCHAIN_TABLE`
	- `DBMS_USER_CERTS`
- `DBMS_PLSQL_CODE_COVERAGE`
	A new function `GET_BLOCK_MAP` has been added to the `DBMS_PLSQL_CODE_COVERAGE` package to help you calculate the total coverage number for a schema.
	See " [GET\_BLOCK\_MAP Function](DBMS_PLSQL_CODE_COVERAGE.md) "
- `DBMS_JSON`
	JSON data guide supports extended JSON scalar types like double, float, timestamp, and so on.
- Oracle Database Advanced Queuing Support for JSON data type
	AQ now supports `JSON` payload type. A dedicated `JSON` data type allows the user to store `JSON` data in a post-parse binary format, which allows much faster access to nested `JSON` values.
	See " [DBMS\_AQ Data Types](DBMS_AQ.md) "
- Enhanced Result Cache
	The `DBMS_RESULT_CACHE` package provides the following new `PL/SQL` procedures that allows users to block an object from the result cache.
	- `OBJECT_BLACK_LIST Function`
	- `OBJECT_BLACK_LIST_ADD Procedure`
	- `OBJECT_BLACK_LIST_CLEAR Procedure`
	- `OBJECT_BLACK_LIST_REMOVE Procedure`
	See [DBMS\_RESULT\_CACHE](DBMS_RESULT_CACHE.md).
- Support for `DBMS_CRYPTO` Asymmetric Key Operations
	Starting with this release, the `DBMS_CRYPTO` PL/SQL package supports asymmetric key operations, in addition to the existing support for symmetric key operations. To implement the support for asymmetric key operations, the following procedures have been added to the `DBMS_CRYPTO` package:
	- `PKENCRYPT`
		- `PKDECRYPT`
		- `SIGN`
		- `VERIFY`
	See [DBMS\_CRYPTO](DBMS_CRYPTO.md).
- The following two new procedures are introduced in the DBMS\_APP\_CONT\_ADMIN package to enhance the application continuity protection check:
	- ACCHK\_REPORT Procedure
		- ACCHK\_SET Procedure
- New parameter, `AUTO_INDEX_TABLE` is added in `CONFIGURE` procedure in the `DBMS_AUTO_INDEX` package. You can use the `AUTO_INDEX_TABLE` configuration setting to specify tables that can use auto indexes.
- `DBMS_JSON`:
	- The following 3 parameters are added to the `ADD_VIRTUAL_COLUMNS` Procedure in the `DBMS_JSON` package to enhance view creation and adding of virtual columns: `resolvenameconflicts`, `colnameprefix`, and `mixedcasecolumns`.
		- The following parameters are added to the `CREATE_VIEW` procedure in the DBMS\_JSON package to enhance view creation and adding of virtual columns: `resourcepath`, `materialize`, `mvrefreshmode`, `path`, `resolvenameconflicts` `colnameprefix`, and `mixedcasecolumns`.

#### Deprecated Features

List of deprecated features in Oracle Database release 21c version 21.1 PL/SQL Packages and Types Reference.

Oracle recommends that you do not use deprecated features/values in new applications. Support for deprecated features is for backward compatibility only.

- `Oracle Wallet Manager (OWM)` is deprecated with Oracle Database 21c.
	Please ensure your wallets are using the strongest protections available. Instead of using Oracle Wallet Manager, Oracle recommends that you use the command line tools `orapki` and `mkstore`.
- The use of `SHA-1` for `SQLNET` and `DBMS_CRYPTO` is deprecated.
- The use of `MD5` and `MD4` algorithms are deprecated.
- Oracle Enterprise Manager Database Express (EM Express) is deprecated.

#### Desupported Features

This section lists the desupported features in Oracle Database release 21c version 21.1 PL/SQL Packages and Types Reference.

The following features are desupported in this release:

- Multitenant-Only Architecture
	A multitenant container database is the only supported architecture in Oracle Database 21c. While the documentation is being revised, legacy terminology may persist. In most cases, "database" and "non-CDB" refer to a CDB or PDB, depending on context. In some contexts, such as upgrades, "non-CDB" refers to a non-CDB from a previous release.
- The `DBMS_XMLSAVE` package is desupported in Oracle Database 21c.
- The `DBMS_XMLQUERY` package is desupported in Oracle Database 21c.
- `DBMS_CRYPTO`: Desupported algorithms include MD4, MD5 and RC4-related algorithms. Removing older, less secure cryptography algorithms prevents accidental use of these APIs. To meet your security requirements, Oracle recommends that you use more modern cryptography algorithms.
- Starting with Oracle Database 21c, several XML Database features are desupported.
	- Package `DBMS_XDBT`. There is no replacement.
	- PL/SQL procedure `DBMS_XSLPROCESSOR.CLOB2FILE`. Use `DBMS_LOB.CLOB2FILE` instead.
	- PL/SQL function `DBMS_XSLPROCESSOR.READ2CLOB`. Use `DBMS_LOB.LOADCLOBFROMFILE` instead.
- Starting in Oracle Database 21c, the Large Object (LOB) features `DBMS_LOB.LOADFROMFILE` is desupported. Use `DBMS_LOB.LoadClobFromFile` or `DBMS_LOB.LoadBlobFromFile` instead.
	LOB buffering is also desupported. Hence, the `BUFFERING_ENABLED` exception is no longer supported.
- `DBMS_OBFUSCATION_TOOLKIT`
	The `DBMS_OBFUSCATION_TOOLKIT` package was desupported in Oracle Database 10g Release 2. It is now removed in Oracle Database 21c. `DBMS_CRYPTO` replaces the functionality that `DBMS_OBFUSCATION_TOOLKIT` provided previously. `DBMS_CRYPTO` includes more modern and secure encryption technologies for your security requirements.
- The ability to create flat file dictionary dumps of pluggable databases (PDBs) is desupported in Oracle Database 21c.
	In previous releases, using a flat file dictionary was one means of mining the redo logs for the changes associated with a specific PDB whose data dictionary was contained within the flat file. This feature is now desupported. Starting with Oracle Database 21c, Oracle recommends that you call `DBMS_LOGMNR.START_LOGMNR`, and supply the system change number (SCN) or time range that you want to mine. The SCN or time range options of `START_LOGMNR` are enhanced to support mining of individual PDBs.
- The `OPTIMIZE_PROGRESS_TABLE` parameter from the `DBMS_APPLY_ADM.SET_PARAMETER` procedure is desupported in Oracle Database 21c.
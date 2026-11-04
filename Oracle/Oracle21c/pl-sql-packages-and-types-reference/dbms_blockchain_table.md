---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/dbms_blockchain_table.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 39 DBMS\_BLOCKCHAIN\_TABLE

A blockchain table is an append-only table designed for centralized blockchain applications. The `DBMS_BLOCKCHAIN_TABLE` package allows you do the following: delete rows in a blockchain table that are beyond the row retention defined for the blockchain table; get the bytes that are input to the cryptographic hash for a row so you can verify the hash in the row; sign a row you inserted into a blockchain table after the row is added to a chain in the blockchain table; and have the database verify the hashes on some or all rows in a blockchain table. Blockchain tables support only `DER` encoding for `X.509` certificates, not `PEM` encoding.

This chapter contains the following topics:

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-707B02F5-E589-4C20-8E2E-5ED4F7888702)
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=CNCPT1132)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SQLRF54484)
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=REFRN)
- For information on hidden columns in blockchain tables, see [Hidden Columns in Blockchain Tables](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-02BD6C35-E1E9-41B7-BD56-68C7A667B51F)

### 39.1 DBMS\_BLOCKCHAIN\_TABLE Overview

In Oracle Blockchain Table, peers are database users who trust the database to maintain a tamper-resistant ledger.

The ledger is implemented as a blockchain table, which is defined and managed by the application. Existing applications can protect against fraud without requiring a new infrastructure or programming model. Although transaction throughput is lower than for a standard table, performance for a blockchain table is better than for a decentralized blockchain.

The `DBMS_BLOCKCHAIN_TABLE` package lets you do the following:
- delete rows in a blockchain table that are beyond the row retention defined for the blockchain table
- get the bytes that are input to the signature algorithm so you can sign a row you inserted into the blockchain table
- get the bytes that are input to the cryptographic hash for a row so you can verify the hash in the row
- sign a row you inserted into a blockchain table after the row is added to a chain in the blockchain table
- have the database verify the hashes and signatures on some or all rows in a blockchain table.

### 39.2 DBMS\_BLOCKCHAIN\_TABLE Security Model

The `DBMS_BLOCKCHAIN_TABLE` package is owned by `SYS` and is installed as part of database installation. The routines in the package are run with invokers' rights (run with the privileges of the current user). Thus any user with select privileges on the blockchain table should be able to validate the row contents of that table.

Any user with delete privileges on the blockchain table can delete rows beyond the retention period defined for the blockchain table.

A user that inserted a row into the blockchain table can add a digital signature to the row after the row is added to a chain in the blockchain table.

### 39.3 Summary of DBMS\_BLOCKCHAIN\_TABLE Subprograms

The `DBMS_BLOCKCHAIN_TABLE` package uses `DELETE_EXPIRED_ROWS`, `GET_BYTES_FOR_ROW_HASH`, `GET_BYTES_FOR_ROW_SIGNATURE`, `SIGN_ROW`, and `VERIFY_ROWS` subprograms to perform various functions.

Table 39-1 DBMS\_BLOCKCHAIN\_TABLE Package Subprograms

| Subprogram | Description |
| --- | --- |
| DELETE\_EXPIRED\_ROWS Procedure | Deletes rows outside the retention window created before `before_timestamp` if the time stamp is specified; otherwise, deletes all rows outside the retention window. |
| GET\_BYTES\_FOR\_ROW\_HASH Procedure | Returns in `row_data` the bytes (series of {meta-data-value} {column-data-value} in column position order} for the particular row identified, followed by the hash (in data format) for previous row in the chain, in the data format supported. |
| GET\_BYTES\_FOR\_ROW\_SIGNATURE Procedure | The bytes returned are the bytes in the row hash. No metadata is included. |
| GET\_SIGNED\_BLOCKCHAIN\_DIGEST Function | This function generates and returns the signed digest on specified blockchain table using schema user's certificate. The `signed_bytes`, `signed_row_indexes`, and `schema_certificate_guid` are also returned. |
| SIGN\_ROW Procedure | This procedure can be used by the current user to provide a signature on row content of a previously inserted row. The user who inserted a row into a blockchain table is the only user that can sign the row. |
| VERIFY\_ROWS Procedure | Verifies all rows on all applicable chains for integrity of `HASH` column value for rows created in the range of `LOW_TIMESTAMP` to `HIGH_TIMESTAMP`. Row signatures can be verified as an option. |
| VERIFY\_TABLE\_BLOCKCHAIN Procedure | This procedure verifies all rows whose creation-time fall between the minimum value for the row-creation time from signed\_buffer\_previous and the maximum value for row-creation time from signed\_buffer\_latest and returns the number of successfully verified rows. |

#### 39.3.1 DELETE\_EXPIRED\_ROWS Procedure

This procedure deletes rows outside the retention window created `before_timestamp` if the time stamp is specified; otherwise, deletes all rows outside the retention window. The number of rows deleted is returned in `number_of_rows_deleted` parameter.

Syntax

```
DBMS_BLOCKCHAIN_TABLE.DELETE_EXPIRED_ROWS(
   schema_name          IN VARCHAR2,
   table_name              IN VARCHAR2, 
   before_timestamp        IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   number_of_rows_deleted     OUT NUMBER);
```

Parameters

Table 39-2 DELETE\_EXPIRED\_ROWS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the schema. |
| `table_name` | The name of the blockchain table. |
| `before_timestamp` | The end time for the range of rows deleted by the procedure, subject to the row retention time currently associated with the blockchain table.  This is an optional parameter. The default value is `NULL`. |
| `number_of_rows_deleted` | The count of the number of rows deleted. |

#### 39.3.2 GET\_BYTES\_FOR\_ROW\_HASH Procedure

This procedure returns the bytes in `column_data` that the database hashed to get the hash value for the row identified by parameters `instance_id`, `chain_id`, and `sequence_id`. These bytes are a concatenation of metadata and data bytes for each column of the table in column position order, followed by the hash value for the previous row in the chain.

Syntax

```
DBMS_BLOCKCHAIN_TABLE.GET_BYTES_FOR_ROW_HASH(
   schema_name          IN VARCHAR2,
   table_name              IN VARCHAR2, 
   instance_id          IN NUMBER, 
   chain_id                  IN NUMBER,
   sequence_id             IN NUMBER,
   data_format             IN NUMBER, 
   row_data                IN OUT BLOB);
```

Parameters

Table 39-3 GET\_BYTES\_FOR\_ROW\_HASH Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the schema. |
| `table_name` | The name of the blockchain table. |
| `instance_id` | The instance that inserted the row.  Valid values are `1`, `2`, and so on. |
| `chain_id` | The chain containing the row. There are 32 chains in each instance, and they are numbered from 0 to 31. |
| `sequence_id` | The position of the row on the specified chain. |
| `data_format` | The version of the data layout for the hash in the specified row. Must be `1` in this release. |
| `row_data` | The bytes for the specified row in the specified data format that can be input to the cryptographic hash function to verify the value of the hash in the row. Any bytes in the `BLOB` are overwritten. |

Usage Notes

All parameters are required input parameters.

The metadata bytes for a column are 20 bytes that encode the blockchain algorithm version used to hash the row, the column position, the column data type, whether the column value is `NULL`, and the actual length of the column value in bytes.

The column data bytes are the actual bytes representing the column value on disk for non-character columns. For character columns, the values are normalized to specific character sets. For `CHAR` and `NCHAR` columns, blank trimming is also done.

Before computing the row hash, the database normalizes the character and character LOB columns to specific character sets. The number of spaces in CHAR and NCHAR values is also normalized.

Few metadata bytes are reserved for future use.

See Also:

For more information on normalizations, see [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-707B02F5-E589-4C20-8E2E-5ED4F7888702)

#### 39.3.3 GET\_BYTES\_FOR\_ROW\_SIGNATURE Procedure

The routine returns in `row_data` the bytes in the hash in the row without any metadata. No other columns are involved either in the row or in the previous row.

Syntax

```
DBMS_BLOCKCHAIN_TABLE.GET_BYTES_FOR_ROW_SIGNATURE(
   schema_name          IN VARCHAR2,
   table_name              IN VARCHAR2, 
   instance_id          IN NUMBER, 
   chain_id             IN NUMBER,
   sequence_id             IN NUMBER,
   data_format             IN NUMBER, 
   row_data                   IN OUT BLOB);
```

Parameters

Table 39-4 GET\_BYTES\_FOR\_ROW\_SIGNATURE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the schema. |
| `table_name` | The name of the blockchain table. |
| `instance_id` | The instance on which the row was inserted.  Valid values are `1`, `2`, and so on. |
| `chain_id` | The chain on which the row was inserted. There are 32 chains in each instance, and they are numbered from 0 to 31. |
| `sequence_id` | The position of the row on the chain. |
| `data_format` | The format of the data in `row_data`. The value must be `1` in the DB20c release. |
| `row_data` | A sequence of bytes that must be signed. |

Usage Notes

All parameters are required input parameters.

#### 39.3.4 GET\_SIGNED\_BLOCKCHAIN\_DIGEST Function

This function generates and returns the signed digest on specified blockchain table using schema user's certificate. The `signed_bytes`, `signed_row_indexes`, and `schema_certificate_guid` are also returned.

Syntax

```
DBMS_BLOCKCHAIN_TABLE.GET_SIGNED_BLOCKCHAIN_DIGEST(
   schema_name            IN      VARCHAR2,
   table_name                IN      VARCHAR2, 
   signed_bytes               IN OUT  BLOB,
   signed_rows_indexes        OUT     ORABCTAB_ROW_ARRAY_T,
   schema_certificate_guid    OUT     RAW,
   signature_algo             IN      NUMBER default SIGN_ALGO_DEFAULT)
  RETURN RAW;
```

Parameters

Table 39-5 GET\_SIGNED\_BLOCKCHAIN\_DIGEST Function Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the schema. |
| `table_name` | The name of the blockchain table. |
| `signed_bytes` | The BLOB value that contains a header followed by an array of row-info. The caller must pass an empty BLOB for this parameter. |
| `signed_rows_indexes` | This parameter specifies the rows in the blockchain that were digitally signed. |
| `schema_certificate_guid` | The PKI certificate of the owner of the blockchain table that was used to produce the digital signature. |
| `signature_algo` | The digital signature the algorithm must use. The parameter must be one of the following package constants: `SIGN_ALGO_RSA_SHA2_256`, `SIGN_ALGO_RSA_SHA2_384`, or `SIGN_ALGO_RSA_SHA2_512`. |

Usage Notes

- Database computes the signature on `signed_bytes` using PKI private key of blockchain table owner.
- The certificate of blockchain table owner must be added to database using `DBMS_USER_CERTS.ADD_CERTIFICATE()`.
- The PKI private key and certificate of blockchain table owner must exist in a wallet located under `<WALLET_ROOT>/bctable/` directory for a non-container database.
- The PKI private key and certificate of blockchain table owner must exist in a wallet located under `<WALLET_ROOT>/pdb_guid/bctable/` directory for a container database.
- A blockchain table digest created by the `GET_SIGNED_BLOCKCHAIN_DIGEST` function has table information specific to a pluggable database. Such a digest can be used only in the pluggable database in which the digest was created and only for the table that was used to create the digest. For `DBMS_BLOCKCHAIN_TABLE.VERIFY_TABLE_BLOCKCHAIN`, these requirements mean that both blockchain table digests must have been generated in the current pluggable database for the same blockchain table.
	For example, suppose you create a digest for a blockchain table in pluggable database A, use Data Pump to export the blockchain table, and use Data Pump to import the blockchain table into pluggable database B. The blockchain table digest created in pluggable database A cannot be used in pluggable database B. You need to create a new blockchain table digest in pluggable database B.

Note:

The `bctable` subdirectory is the name of a database component that uses wallets. It is not the name of a blockchain table.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-707B02F5-E589-4C20-8E2E-5ED4F7888702)

#### 39.3.5 SIGN\_ROW Procedure

This procedure can be used by the current user to provide a signature on row content of a previously inserted row. The transaction that inserted the row into the blockchain table must have committed before the `SIGN_ROW` procedure is called.

Syntax

```
DBMS_BLOCKCHAIN_TABLE.SIGN_ROW(
   schema_name               IN VARCHAR2,
   table_name                IN VARCHAR2,
   instance_id               IN NUMBER, 
   chain_id            IN NUMBER,
   sequence_id               IN NUMBER,
   hash                      IN RAW DEFAULT NULL,
   signature                 IN RAW,
   certificate_guid          IN RAW,
   signature_algo            IN NUMBER);
```

Parameters

Table 39-6 SIGN\_ROW Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the schema. |
| `table_name` | The name of the blockchain table. |
| `instance_id` | The instance on which the row was inserted. |
| `chain_id` | The chain containing the row to be signed. There are 32 chains in each instance, and they are numbered from 0 to 31. |
| `sequence_id` | The position of the row on the chain.  Valid values are `1`, `2`, and so on. |
| `hash` | If `non-NULL`, the expected value of the hash in the row to be signed. If `NULL`, the hash in the row to be signed is not checked. |
| `signature` | The user's digital signature on the hash value stored in the row. |
| `certificate_guid` | A unique identifier for the certificate stored in the database that may be used to verify the digital signature. |
| `signature_algo` | The algorithm used to create the digital signature. The algorithm must be one of the following constants defined in the `DBMS_BLOCKCHAIN_TABLE` package: - `SIGN_ALGO_RSA_SHA2_256` - `SIGN_ALGO_RSA_SHA2_384` - `SIGN_ALGO_RSA_SHA2_512` |

Note:

For information on hidden columns in blockchain tables, see [Hidden Columns in Blockchain Tables](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-02BD6C35-E1E9-41B7-BD56-68C7A667B51F)

Usage Notes

- All parameters are required input parameters except for `hash`.
- The database will verify that:
	- the current user’s `obj#` matches the `user#` hidden column value (ensures that the user owns the row)
		- the user has insert privileges for the blockchain table `‘schema_name’.’table_name’`
		- the hash (if provided) matches the hash column content for the row
		- the `signature` column value for the specific row identified by `‘instance_id’`, `‘chain_id’`, and `‘sequence_id’` is `NULL`
		- if the verification succeeds, the signature value is stored for the row.

#### 39.3.6 VERIFY\_ROWS Procedure

Verifies all rows on all applicable chains for integrity of `HASH` column value and optionally the `SIGNATURE` column value for rows created in the range of `low_timestamp` to `high_timestamp`. An appropriate exception is thrown if the integrity of chains is compromised.

Syntax

```
DBMS_BLOCKCHAIN_TABLE.VERIFY_ROWS(
   schema_name                  IN VARCHAR2,
   table_name                   IN VARCHAR2, 
   low_timestamp                IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   high_timestamp               IN TIMESTAMP WITH TIME ZONE DEFAULT NULL, 
   instance_id                  IN NUMBER DEFAULT NULL, 
   chain_id                     IN NUMBER DEFAULT NULL,
   number_of_rows_verified      OUT NUMBER,
   verify_signature             IN BOOLEAN DEFAULT TRUE);
```

Parameters

Table 39-7 VERIFY\_ROWS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the schema. |
| `table_name` | The name of the blockchain table. |
| `low_timestamp` | If specified, the low end of the time range for verifying rows.  The default value is `NULL`. |
| `high_timestamp` | If specified, the high end of the time range for verifying rows.  The default value is `NULL`. |
| `instance_id` | If specified, restricts row verification to rows inserted on the specified instance. |
| `chain_id` | If specified, restricts row verification to rows on the specified chain. There are 32 chains in each instance, and they are numbered from 0 to 31. |
| `number_of_rows_verified` | The number of rows verified. |
| `verify_signature` | If `verify_signature` is `TRUE`, both the hash on each row and any signature on the row are verified. If `verify_signature` is `FALSE`, only the hash on each row is verified.  The default value is `TRUE`. |

Usage Notes

- The hash on the first element in the time range for verifying rows in a chain is verified only if its sequence number is `1`.
- `schema_name` and `table_name` are required input parameters
- All others input parameters are optional, with the following exceptions:
	- If `chain_id` is specified, `instance_id` must be specified
		- Valid values for `instance_id` are 1, 2, … etc.
		- If neither `instance_id`, nor `chain_id` is specified, then it implies `*all*` chains. If only `instance_id` is specified, then it implies `*all*` chains on that instance. If both are specified, it implies the specific chain provided by the combination.
		- If both `low_timestamp` and `high_timestamp` are specified, then `high_timestamp` must be later than `low_timestamp`.
		If `low_timestamp` is not specified, then the range is the oldest row in the blockchain to `high_timestamp`.
		If `high_timestamp` is not specified then the range is `low_timestamp` to the timestamp of the last row inserted in the table.

#### 39.3.7 VERIFY\_TABLE\_BLOCKCHAIN Procedure

This procedure verifies all rows whose creation-time fall between the minimum value for the row-creation time from `signed_bytes_previous` and the maximum value for row-creation time from `signed_bytes_latest` and returns the number of successfully verified rows.

Syntax

```
DBMS_BLOCKCHAIN_TABLE.VERIFY_TABLE_BLOCKCHAIN(
   signed_bytes_latest        IN    BLOB,
   signed_bytes_previous      IN    BLOB,
   number_of_rows_verified    OUT   NUMBER);
```

Parameters

Table 39-8 VERIFY\_TABLE\_BLOCKCHAIN Procedure Parameters

| Parameter | Description |
| --- | --- |
| `signed_bytes_latest` | A BLOB created by a call to `get_signed_blockchain_digest`. |
| `signed_bytes_previous` | A BLOB created by a call to `get_signed_blockchain_digest` before the `signed_bytes_latest` BLOB was created. |
| `number_of_rows_verified` | The count of the rows in the blockchain table that was verified. |

Usage Notes

The BLOBs in `signed_bytes_latest` and `signed_bytes_previous` must be associated with the same blockchain table.
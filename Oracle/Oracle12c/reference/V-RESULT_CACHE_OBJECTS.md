---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-RESULT_CACHE_OBJECTS.html
tags:
  - oracle
  - 12c
  - reference
---

`V$RESULT_CACHE_OBJECTS` displays all the objects (both cached results and dependencies) and their attributes.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Identifier for the cache object (also the ID of the first block) |
| `TYPE` | `VARCHAR2(10)` | Type of the cache object:  - `Result` - `Dependency` |
| `STATUS` | `VARCHAR2(9)` | Status of the object:  - `New` - Result is still under construction - `Published` - Result is available for use - `Bypass` - Result will be bypassed from use - `Expired` - Result has exceeded expiration time - `Invalid` - Result is no longer available for use |
| `BUCKET_NO` | `NUMBER` | Internal hash bucket for the object |
| `HASH` | `NUMBER` | Hash value for the object |
| `NAME` | `VARCHAR2(128)` | Name (for example, SQL prefix or PL/SQL function name) |
| `NAMESPACE` | `VARCHAR2(5)` | Namespace:  - `SQL` - `PLSQL` - `KEY VECTOR` |
| `CREATION_TIMESTAMP` | `DATE` | Time when the object was created |
| `CREATOR_UID` | `NUMBER` | UID that created the object |
| `DEPEND_COUNT` | `NUMBER` | Number of dependencies (`TYPE` = `Result`) or dependents (`TYPE` = `Dependency`) |
| `BLOCK_COUNT` | `NUMBER` | Total number of blocks in the cached object |
| `SCN` | `NUMBER` | Build SCN (`TYPE` = `Result`) or invalidation SCN (`TYPE` = `Dependency`) |
| `COLUMN_COUNT` | `NUMBER` | Number of columns in the cached result  This column is only valid for `TYPE` = `Result`; otherwise, it is NULL. |
| `PIN_COUNT` | `NUMBER` | Number of active scans on this result  This column is only valid for `TYPE` = `Result`; otherwise, it is NULL. |
| `SCAN_COUNT` | `NUMBER` | Total number of scans initiated on the cached result  This column is only valid for `TYPE` = `Result`; otherwise, it is NULL. |
| `ROW_COUNT` | `NUMBER` | Total number of rows in the cached result  This column is only valid for `TYPE` = `Result`; otherwise, it is NULL. |
| `ROW_SIZE_MAX` | `NUMBER` | Size of the largest row (in bytes)  This column is only valid for `TYPE` = `Result`; otherwise, it is NULL. |
| `ROW_SIZE_MIN` | `NUMBER` | Size of the smallest row (in bytes)  This column is only valid for `TYPE` = `Result`; otherwise, it is NULL. |
| `ROW_SIZE_AVG` | `NUMBER` | Average size of a row (in bytes)  This column is only valid for `TYPE` = `Result`; otherwise, it is NULL. |
| `BUILD_TIME` | `NUMBER` | Amount of time (in hundredths of a second) it took to build the cached result  This column is only valid for `TYPE` = `Result`; otherwise, it is NULL. |
| `LRU_NUMBER` | `NUMBER` | LRU list position (the larger the value, the more recent the usage)  This column is only valid for `TYPE` = `Result`; otherwise, it is NULL. |
| `OBJECT_NO` | `NUMBER` | Dictionary object number of the dependency object  This column is only valid for `TYPE` = `Dependency`; otherwise, it is NULL. |
| `INVALIDATIONS` | `NUMBER` | Number of times the object has invalidated its dependents  This column is only valid for `TYPE` = `Dependency`; otherwise, it is NULL. |
| `SPACE_OVERHEAD` | `NUMBER` | Overhead (in bytes) for the result  This column is only valid for `TYPE` = `Result`; otherwise, it is NULL. |
| `SPACE_UNUSED` | `NUMBER` | Unused space (in bytes) for the result  This column is only valid for `TYPE` = `Result`; otherwise, it is NULL. |
| `CACHE_ID` | `VARCHAR2(93)` | `CacheId` for the result (object name if it's a dependency) |
| `CACHE_KEY` | `VARCHAR2(93)` | `CacheKey` for the result (object name if it's a dependency) |
| `CHECKSUM` | `NUMBER` | Checksum for the result object. The checksum is computed over all the blocks in the result cache object minus the object header. |
| `EDITION_ID` | `NUMBER` | Shows the edition's object ID that was in use when the result was calculated |
| `DB_LINK` | `VARCHAR2(3)` | Possible values:  - `YES`: If the result cache object references a remote database object - `NO`: If the result cache object does not reference a remote database object |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
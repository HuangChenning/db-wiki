---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RESULT_CACHE_OBJECTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.172 V$RESULT\_CACHE\_OBJECTS

`V$RESULT_CACHE_OBJECTS` displays all the objects (both cached results and dependencies) and their attributes.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Identifier for the cache object (also the ID of the first block) |
| `TYPE` | `VARCHAR2(10)` | Type of the cache object:  - `Dependency` - `Result` - `Temp` |
| `STATUS` | `VARCHAR2(9)` | Status of the object:  - `New` - Result is still under construction - `Published` - Result is available for use - `Bypass` - Result will be bypassed from use - `Expired` - Result has exceeded expiration time - `Invalid` - Result is no longer available for use |
| `BUCKET_NO` | `NUMBER` | Internal hash bucket for the object |
| `HASH` | `NUMBER` | Hash value for the object |
| `NAME` | `VARCHAR2(387)` | Name (for example, SQL prefix or PL/SQL function name) |
| `NAMESPACE` | `VARCHAR2(10)` | Namespace:  - `SQL` - `PLSQL` - `KEY VECTOR` |
| `CREATION_TIMESTAMP` | `DATE` | Time when the object was created |
| `CREATOR_UID` | `NUMBER` | UID that created the object |
| `DEPEND_COUNT` | `NUMBER` | Number of dependencies (`TYPE` = `Result`) or dependents (`TYPE` = `Dependency`) |
| `BLOCK_COUNT` | `NUMBER` | Total number of blocks in the cached object |
| `SCN` | `NUMBER` | Build SCN (`TYPE` = `Result`) or invalidation SCN (`TYPE` = `Dependency`) |
| `COLUMN_COUNT` <sup>Foot 1</sup> | `NUMBER` | Number of columns in the cached result |
| `PIN_COUNT` <sup>Foot 1</sup> | `NUMBER` | Number of active scans on this result |
| `SCAN_COUNT` <sup>Foot 1</sup> | `NUMBER` | Total number of scans initiated on the cached result |
| `ROW_COUNT` <sup>Foot 1</sup> | `NUMBER` | Total number of rows in the cached result |
| `ROW_SIZE_MAX` <sup>Foot 1</sup> | `NUMBER` | Size of the largest row (in bytes) |
| `ROW_SIZE_MIN` <sup>Foot 1</sup> | `NUMBER` | Size of the smallest row (in bytes) |
| `ROW_SIZE_AVG` <sup>Foot 1</sup> | `NUMBER` | Average size of a row (in bytes) |
| `BUILD_TIME` <sup>Foot 1</sup> | `NUMBER` | Amount of time (in hundredths of a second) it took to build the cached result |
| `LRU_NUMBER` <sup>Foot 1</sup> | `NUMBER` | LRU list position (the larger the value, the more recent the usage) |
| `OBJECT_NO` <sup>Foot 2</sup> | `NUMBER` | Dictionary object number of the dependency object |
| `INVALIDATIONS` <sup>Foot 2</sup> | `NUMBER` | Number of times the object has invalidated its dependents |
| `SPACE_OVERHEAD` <sup>Foot 1</sup> | `NUMBER` | Overhead (in bytes) for the result |
| `SPACE_UNUSED` <sup>Foot 1</sup> | `NUMBER` | Unused space (in bytes) for the result |
| `CACHE_ID` | `VARCHAR2(387)` | `CacheId` for the result (object name if it's a dependency) |
| `CACHE_KEY` | `VARCHAR2(387)` | `CacheKey` for the result (object name if it's a dependency) |
| `CHECKSUM` | `NUMBER` | Checksum for the result object. The checksum is computed over all the blocks in the result cache object minus the object header. |
| `EDITION_ID` | `NUMBER` | Shows the edition's object ID that was in use when the result was calculated |
| `DB_LINK` | `VARCHAR2(3)` | Possible values:  - `YES`: The result cache object references a remote database object - `NO`: The result cache object does not reference a remote database object |
| `GLOBAL` <sup>Foot 3</sup> | `VARCHAR2(3)` | Possible values:  - `YES`: The object was fetched from the result cache of a remote database instance - `NO`: The object was recomputed on this instance, either because it was not available on a remote database instance or because the system deemed it was inefficient to fetch the object from a remote database instance |
| `SUBCACHE_ID` <sup>Foot 3</sup> | `NUMBER` | Subcache ID |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

<sup>Footnote 1</sup>

This column is valid only for `TYPE` = `Result`; otherwise, its value is 0.

<sup>Footnote 2</sup>

This column is valid only for `TYPE` = `Dependency`; otherwise, its value is 0.

<sup>Footnote 3</sup> This column is available starting with Oracle Database 21c.
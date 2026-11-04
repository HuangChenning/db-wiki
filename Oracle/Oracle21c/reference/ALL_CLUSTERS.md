---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CLUSTERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.130 ALL\_CLUSTERS

`ALL_CLUSTERS` describes all clusters accessible to the current user.

Related Views

- `DBA_CLUSTERS` describes all clusters in the database.
- `USER_CLUSTERS` describes all clusters owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL ` | Owner of the cluster |
| `CLUSTER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the cluster |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace containing the cluster |
| `PCT_FREE` | `NUMBER` |  | Minimum percentage of free space in a block |
| `PCT_USED` | `NUMBER` |  | Minimum percentage of used space in a block |
| `KEY_SIZE` | `NUMBER` |  | Estimated size of cluster key plus associated rows |
| `INI_TRANS` | `NUMBER` | `NOT NULL` | Initial number of transactions |
| `MAX_TRANS` | `NUMBER` | `NOT NULL` | Maximum number of transactions |
| `INITIAL_EXTENT` | `NUMBER` |  | Size of the initial extent in bytes |
| `NEXT_EXTENT` | `NUMBER` |  | Size of secondary extents in bytes |
| `MIN_EXTENTS` | `NUMBER` | `NOT NULL ` | Minimum number of extents allowed in the segment |
| `MAX_EXTENTS` | `NUMBER` | `NOT NULL ` | Maximum number of extents allowed in the segment |
| `PCT_INCREASE` | `NUMBER` |  | Percentage increase in extent size |
| `FREELISTS` | `NUMBER` |  | Number of process freelists allocated to this segment |
| `FREELIST_GROUPS ` | `NUMBER` |  | Number of freelist groups allocated to this segment |
| `AVG_BLOCKS_PER_KEY ` | `NUMBER` |  | Number of blocks in the table divided by number of cluster keys |
| `CLUSTER_TYPE` | `VARCHAR2(5)` |  | Type of the cluster:  - `INDEX` - B\*-Tree index - `HASH` - Hash |
| `FUNCTION` | `VARCHAR2(15)` |  | If the cluster is a hash cluster, the hash function |
| `HASHKEYS` | `NUMBER` |  | If the cluster is a hash cluster, the number of hash keys (hash buckets) |
| `DEGREE` | `VARCHAR2(10)` |  | Number of threads per instance for scanning the cluster, or `DEFAULT` |
| `INSTANCES` | `VARCHAR2(10)` |  | Number of instances across which the cluster is to be scanned, or `DEFAULT` |
| `CACHE` | `VARCHAR2(5)` |  | Indicates whether the cluster is to be cached in the buffer cache (`Y`) or not (`N`) |
| `BUFFER_POOL` | `VARCHAR2(7)` |  | Buffer pool to be used for cluster blocks:  - `DEFAULT` - `KEEP` - `RECYCLE` - NULL |
| `FLASH_CACHE` | `VARCHAR2(7)` |  | Database Smart Flash Cache hint to be used for cluster blocks:  - `DEFAULT` - `KEEP` - `NONE`  Solaris and Oracle Linux functionality only. |
| `CELL_FLASH_CACHE` | `VARCHAR2(7)` |  | Cell flash cache hint to be used for cluster blocks:  - `DEFAULT` - `KEEP` - `NONE`  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `SINGLE_TABLE` | `VARCHAR2(5)` |  | Indicates whether this is a single-table cluster (`Y`) or not (`N`) |
| `DEPENDENCIES` | `VARCHAR2(8)` |  | Indicates whether row-level dependency tracking is enabled (`ENABLED`) or disabled (`DISABLED`) |

See Also:

- " [DBA\_CLUSTERS](DBA_CLUSTERS.md) "
- " [USER\_CLUSTERS](USER_CLUSTERS.md) "
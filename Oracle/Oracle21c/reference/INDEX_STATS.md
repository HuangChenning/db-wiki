---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INDEX_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.208 INDEX\_STATS

`INDEX_STATS` stores information from the last `ANALYZE INDEX ... VALIDATE STRUCTURE` statement.

Note:

The `ANALYZE INDEX ... VALIDATE STRUCTURE OFFLINE` statement must be used in order to collect statistics

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `HEIGHT` | `NUMBER` |  | Height of the B-Tree |
| `BLOCKS` | `NUMBER` | `NOT NULL` | Blocks allocated to the segment |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the index |
| `PARTITION_NAME` | `VARCHAR2(128)` |  | Name of the partition of the index which was analyzed. If the index is not partitioned, NULL is returned. |
| `LF_ROWS` | `NUMBER` |  | Number of leaf rows (values in the index) |
| `LF_BLKS` | `NUMBER` |  | Number of leaf blocks in the B-Tree |
| `LF_ROWS_LEN` | `NUMBER` |  | Sum of the lengths of all the leaf rows |
| `LF_BLK_LEN` | `NUMBER` |  | Usable space in a leaf block |
| `BR_ROWS` | `NUMBER` |  | Number of branch rows in the B-Tree |
| `BR_BLKS` | `NUMBER` |  | Number of branch blocks in the B-Tree |
| `BR_ROWS_LEN` | `NUMBER` |  | Sum of the lengths of all the branch blocks in the B-Tree |
| `BR_BLK_LEN` | `NUMBER` |  | Usable space in a branch block |
| `DEL_LF_ROWS` | `NUMBER` |  | Number of deleted leaf rows in the index |
| `DEL_LF_ROWS_LEN` | `NUMBER` |  | Total length of all deleted rows in the index |
| `DISTINCT_KEYS` | `NUMBER` |  | Number of distinct keys in the index (may include rows that have been deleted) |
| `MOST_REPEATED_KEY` | `NUMBER` |  | How many times the most repeated key is repeated (may include rows that have been deleted) |
| `BTREE_SPACE` | `NUMBER` |  | Total space currently allocated in the B-Tree |
| `USED_SPACE` | `NUMBER` |  | Total space that is currently being used in the B-Tree |
| `PCT_USED` | `NUMBER` |  | Percent of space allocated in the B-Tree that is being used |
| `ROWS_PER_KEY` | `NUMBER` |  | Average number of rows per distinct key (this figure is calculated without consideration of deleted rows) |
| `BLKS_GETS_PER_ACCESS` | `NUMBER` |  | Expected number of consistent mode block reads per row, assuming that a randomly chosen row is accessed using the index. Used to calculate the number of consistent reads that will occur during an index scan. |
| `PRE_ROWS` | `NUMBER` |  | Number of prefix rows (values in the index) |
| `PRE_ROWS_LEN` | `NUMBER` |  | Sum of lengths of all prefix rows |
| `OPT_CMPR_COUNT` | `NUMBER` |  | Optimal index compression length |
| `OPT_CMPR_PCTSAVE` | `NUMBER` |  | Corresponding space savings after an `ANALYZE` |
| `DEL_LF_CMP_ROWS` | `NUMBER` |  | Number of deleted rows that are within a compression unit (CU) |
| `PRG_LF_CMP_ROWS` | `NUMBER` |  | Number of purged rows that are within a CU |
| `LF_CMP_ROWS` | `NUMBER` |  | Number of rows that are in a CU or prefix compressed |
| `LF_CMP_ROWS_LEN` | `NUMBER` |  | Sum of lengths of all prefix rows and CUs |
| `LF_UNCMP_ROWS` | `NUMBER` |  | Number of rows that are neither in a CU nor prefix compressed |
| `LF_UNCMP_ROWS_LEN` | `NUMBER` |  | Sum of lengths of rows that are neither in a CU nor prefix compressed |
| `LF_SUF_ROWS_LEN` | `NUMBER` |  | Sum of lengths of suffix rows |
| `LF_CMP_ROWS_UNCMP_LEN` | `NUMBER` |  | Sum of the uncompressed lengths of rows that are in a CU or prefix compressed |
| `LF_CMP_RECMP_COUNT` | `NUMBER` |  | Sum of CU recompression counts |
| `LF_CMP_LOCK_VEC_LEN` | `NUMBER` |  | Sum of CU lock vector lengths |
| `LF_CMP_BLKS` | `NUMBER` |  | Number of blocks that have a CU or nonzero prefix column count |
| `LF_UNCMP_BLKS` | `NUMBER` |  | Number of blocks that do not have a CU and have a zero prefix column count |
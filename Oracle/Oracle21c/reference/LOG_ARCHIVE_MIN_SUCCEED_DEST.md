---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/LOG_ARCHIVE_MIN_SUCCEED_DEST.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.190 LOG\_ARCHIVE\_MIN\_SUCCEED\_DEST

`LOG_ARCHIVE_MIN_SUCCEED_DEST` defines the minimum number of destinations that must succeed in order for the online logfile to be available for reuse.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `1` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | 1 to 10 if you are using `LOG_ARCHIVE_DEST_` `n`  1 or 2 if you are using `LOG_ARCHIVE_DEST` and `LOG_ARCHIVE_DUPLEX_DEST` |
| Basic | No |

If you are using the `LOG_ARCHIVE_DEST_` `n` parameters and automatic archiving is enabled, then the value of this parameter cannot exceed the number of enabled, valid destinations specified as `MANDATORY` plus the number of enabled, valid destinations that are configured with the `OPTIONAL` and `LOCATION` attributes.

If you are using `LOG_ARCHIVE_DEST` and `LOG_ARCHIVE_DUPLEX_DEST` and automatic archiving is enabled, a value of `1` specifies that the destination specified in `LOG_ARCHIVE_DEST` must succeed. A value of `2` specifies that the destinations specified in both parameters must succeed.

If the value of this parameter is less than the number of enabled, valid `MANDATORY` destinations, this parameter is ignored in favor of the `MANDATORY` destination count. If the value is more than the number of enabled, valid `MANDATORY` destinations, then some of the enabled, valid destinations configured with the `OPTIONAL` and `LOCATION` attributes are treated as `MANDATORY`.

You can switch dynamically from using the older parameters to the `LOG_ARCHIVE_DEST_` `n` parameter using `ALTER SYSTEM`, as follows:

1. Set `LOG_ARCHIVE_MIN_SUCCEED_DEST` to `1`.
2. Set the value of `LOG_ARCHIVE_DEST` and `LOG_ARCHIVE_DUPLEX_DEST` to the null string.
3. Set the desired number of destinations for the `LOG_ARCHIVE_DEST_` `n` parameters.
4. Reset `LOG_ARCHIVE_MIN_SUCCEED_DEST` to the desired value.
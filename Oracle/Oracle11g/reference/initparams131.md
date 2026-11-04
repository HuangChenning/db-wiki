---
title: LOG_ARCHIVE_MIN_SUCCEED_DEST
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams131.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `1` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Range of values | 1 to 10 if you are using `LOG_ARCHIVE_DEST_` `n`  1 or 2 if you are using `LOG_ARCHIVE_DEST` and `LOG_ARCHIVE_DUPLEX_DEST` |
| Basic | No |

`LOG_ARCHIVE_MIN_SUCCEED_DEST` defines the minimum number of destinations that must succeed in order for the online logfile to be available for reuse.

- If you are using the `LOG_ARCHIVE_DEST_` `n` parameters and automatic archiving is enabled, then the value of this parameter cannot exceed the number of enabled, valid destinations specified as `MANDATORY` plus the number of enabled, valid destinations that are configured with the `OPTIONAL` and `LOCATION` attributes.
- If you are using `LOG_ARCHIVE_DEST` and `LOG_ARCHIVE_DUPLEX_DEST` and automatic archiving is enabled, a value of `1` specifies that the destination specified in `LOG_ARCHIVE_DEST` must succeed. A value of `2` specifies that the destinations specified in both parameters must succeed.

If the value of this parameter is less than the number of enabled, valid `MANDATORY` destinations, this parameter is ignored in favor of the `MANDATORY` destination count. If the value is more than the number of enabled, valid `MANDATORY` destinations, then some of the enabled, valid destinations configured with the `OPTIONAL` and `LOCATION` attributes are treated as `MANDATORY`.

You can switch dynamically from using the older parameters to the `LOG_ARCHIVE_DEST_` `n` parameter using `ALTER SYSTEM`, as follows:

1. Set `LOG_ARCHIVE_MIN_SUCCEED_DEST` to `1`.
2. Set the value of `LOG_ARCHIVE_DEST` and `LOG_ARCHIVE_DUPLEX_DEST` to the null string.
3. Set the desired number of destinations for the `LOG_ARCHIVE_DEST_` `n` parameters.
4. Reset `LOG_ARCHIVE_MIN_SUCCEED_DEST` to the desired value.
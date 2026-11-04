---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_CACHE_ADVICE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.76 DB\_CACHE\_ADVICE

`DB_CACHE_ADVICE` enables or disables statistics gathering used for predicting behavior with different cache sizes through the `V$DB_CACHE_ADVICE` performance view.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_CACHE_ADVICE = { ON \| READY \| OFF }` |
| Default value | If `STATISTICS_LEVEL` is set to `TYPICAL` or `ALL`, then `ON`  If `STATISTICS_LEVEL` is set to `BASIC`, then `OFF` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |

Values

- `OFF`
	Advisory is turned off and the memory for the advisory is not allocated.
- `READY`
	Advisory is turned off but the memory for the advisory remains allocated. Allocating the memory before the advisory is actually turned on avoids the risk of an error when you switch the parameter to `ON`.
	If the parameter is switched to this state from `ON`, the contents of the view are preserved and the memory for the advisory is retained.
	If the parameter is switched to this state from `OFF`, you may get an error.
- `ON`
	Advisory is turned on. CPU and memory overheads are incurred. Attempting to set the parameter to this state when it is already in the `OFF` state may result in an error. Otherwise, the view (`V$DB_CACHE_ADVICE`) is reset and statistics are gathered to the newly refreshed view.
	If the parameter is in the `READY` state, you can set it to `ON` without any errors because the memory is already allocated. The view is reset and statistics are displayed in the newly refreshed view.

See Also:

" [V$DB\_CACHE\_ADVICE](V-DB_CACHE_ADVICE.md) "
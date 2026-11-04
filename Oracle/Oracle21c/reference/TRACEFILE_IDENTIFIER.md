---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/TRACEFILE_IDENTIFIER.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.368 TRACEFILE\_IDENTIFIER

`TRACEFILE_IDENTIFIER` specifies a custom identifier that becomes part of the Oracle Trace file name. Such a custom identifier is used to identify a trace file simply from its name and without having to open it or view its contents.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `TRACEFILE_IDENTIFIER = "` `traceid` `"` |
| Default value | There is no default value. |
| Modifiable | `ALTER SESSION` |
| Modifiable in a PDB | No |
| Range of values | Any characters that can occur as part of a file name on the customer platform |
| Basic | No |

Each time this parameter is dynamically modified, the next trace dump will be written to a trace file which has the new parameter value embedded in its name. Trace file continuity information is automatically added to both the old and new trace files to indicate that these trace files belong to the same process.

This parameter can only be used to change the name of the foreground process' trace file; the background processes continue to have their trace files named in the regular format. For foreground processes, the `TRACEID` column of the `V$PROCESS` view contains the current value of the `TRACEFILE_IDENTIFIER` parameter. When this parameter value is set, the trace file name has the following format:

```
sid_ora_pid_traceid.trc
```

In this example, `sid` is the Oracle instance ID, `pid` is the process ID, and `traceid` is the value of the `TRACEFILE_IDENTIFIER` parameter.

See Also:

- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL811) for more information about this parameter
- This parameter is not supported on all operating systems. See your operating system-specific Oracle documentation for more information.
---
title: DIAGNOSTIC_DEST
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams078.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DIAGNOSTIC_DEST = { pathname \| directory }` |
| Default value | Derived from the value of the `$ORACLE_BASE` environment variable. If `$ORACLE_BASE` is not set, then derived from `ORACLE_BASE` as set by the Oracle Universal Installer. If `ORACLE_BASE` is not set, then `$ORACLE_HOME/rdbms/log` is used. |
| Modifiable | `ALTER SYSTEM` |
| Basic | No |
| Oracle RAC | This parameter can be set on each instance. Oracle recommends that each instance in a cluster specify a `DIAGNOSTIC_DEST` directory location that is located on shared disk and that the same value for `DIAGNOSTIC_DEST` be specified for each instance. |

As of Oracle Database 11g Release 1 (11.1), the diagnostics for each database instance are located in a dedicated directory, which can be specified through the `DIAGNOSTIC_DEST` initialization parameter. The structure of the directory specified by `DIAGNOSTIC_DEST` is as follows:

```
<diagnostic_dest>/diag/rdbms/<dbname>/<instname>
```

This location is known as the Automatic Diagnostic Repository (ADR) Home. For example, if the database name is `proddb` and the instance name is `proddb1`, the ADR home directory would be `<diagnostic_dest>/diag/rdbms/proddb/proddb1`.

The following files are located under the ADR home directory:

- Trace files - located in subdirectory `<adr-home>/trace`
- Alert logs - located in subdirectory `<adr-home>/alert`. In addition, the `alert.log` file is now in XML format, which conforms to the Oracle ARB logging standard.
- Core files - located in the subdirectory `<adr-home>/cdump`
- Incident files - the occurrence of each serious error (for example, ORA-600, ORA-1578, ORA-7445) causes an incident to be created. Each incident is assigned an ID and dumping for each incident (error stack, call stack, block dumps, and so on) is stored in its own file, separated from process trace files. Incident dump files are located in `<adr-home>/incident/<incdir#>`. You can find the incident dump file location inside the process trace file.
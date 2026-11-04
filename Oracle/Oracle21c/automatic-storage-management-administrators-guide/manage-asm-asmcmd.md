---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/manage-asm-asmcmd.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

Oracle Automatic Storage Management (Oracle ASM) Command-Line Utility (ASMCMD) provides commands for managing Oracle ASM.

This chapter describes the Oracle Automatic Storage Management (Oracle ASM) Command-Line Utility (ASMCMD). This chapter contains the following topics:

- [About ASMCMD](about-asmcmd.md)
- [ASMCMD Instance Management Commands](asmcmd-instance-commands.md)
- [ASMCMD Client Cluster Management Commands](asmcmd-cluster-commands.md)
- [ASMCMD Oracle ASM Filter Driver Management Commands](asmcmd-filterdriver-commands.md)
- ASMCMD Audit Files Management Commands
- [ASMCMD File Management Commands](asmcmd-file-commands.md)
- [ASMCMD Disk Group Management Commands](asmcmd-diskgroup-commands.md)
- [ASMCMD File Group Management Commands](asmcmd-filegroup-commands.md)
- [ASMCMD Template Management Commands](asmcmd-template-commands.md)
- [ASMCMD File Access Control Commands](asmcmd-accesscontrol-commands.md)

See Also:

[Oracle Automatic Storage Management Cluster File System Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ACFSG-GUID-07E90E70-406A-4273-B27F-9F2ED7C1C4BF) for information about ASMCMD commands to manage Oracle ADVM volumes

### ASMCMD Audit Files Management Commands

This document describes the ASMCMD Oracle ASM audit files management commands.

The following table provides a summary of ASMCMD audit files management commands.

Table 10-1 Summary of ASMCMD audit files management commands

| Command | Description |
| --- | --- |
| audcleanaudittrail | Deletes the audit files of the specified audit trail type. |
| audclearproperty | Clears the value for the specified audit property. |
| audcleartimestamp | Clears the last archive timestamp set by “ `audsettimestamp` ” command. |
| audcreatejob | Creates a purge job for specified audit trail type. |
| auddropjob | Drops the specified audit purge job. |
| audsetdebug | Sets the tracing to the specified debug level. |
| audsetjobinterval | Sets the job interval for the specified audit purge job. |
| audsetjobstatus | Sets the status of the specified purge job to either “ `enable` ” or “ `disable` ” state. |
| audsetproperty | Sets the value of specified audit property for given audit trail type. |
| audsettimestamp | Sets the last archive timestamp for specified audit trail type. |
| audshowtimestamp | Displays the last archive timestamps set by " `audsettimestamp` " command. |
| lsaudcleanupjobs | Displays the configured audit trail purge jobs. |
| lsaudconfigparams | Displays the configured audit trail properties for the given audit trail type. |

#### audcleanaudittrail

Purpose

Deletes the audit files of the specified audit trail type. The command will delete the files based on Last Archive Timestamp set using “ `audsettimestamp` " command, if `--useTimestamp` option is specified. Else, it will delete all the files that are not being actively written to.

Syntax and Description

```
audcleanaudittrail {--os|--uni} [--useTimestamp]
```

Options for the `audcleanaudittrail` command

Table 10-2 Options for the audcleanaudittrail command

| Option | Description |
| --- | --- |
| `--os` | Cleans up audit files of OS audit trail type. |
| `--uni` | Cleans up audit files of Unified audit trail type. |
| `--useTimestamp` | If specified, uses last archive timestamp in cleaning up the audit records. |

Examples

The following are examples of `audcleanaudittrail` command.

In the example below, the audit files of OS audit trail type that are older than the timestamp specified by " `audsettimestamp` " command will be deleted.

Example 10-1 Using the ASMCMD audcleanaudittrail command

```
ASMCMD> audcleanaudittrail --os --useTimestamp
```

In the example below, the audit files of Unified audit trail type that are older than the timestamp specified by " `audsettimestamp` " command will be deleted

Example 10-2 Using the ASMCMD audcleanaudittrail command

```
ASMCMD> audcleanaudittrail --uni --useTimestamp
```

#### audclearproperty

Purpose

Clears the value for the specified audit property. When `--use_def` argument is used, the value of the property is set to its respective default value.

Syntax and Description

```
audclearproperty {--file_max_size|--file_max_age} [--use_def] {--os|--uni}
```

Options for the `audclearproperty` command

Table 10-3 Options for the audclearproperty command

| Option | Description |
| --- | --- |
| `--file_max_size` | Maximum audit file size  Note:  For more details, see [Administering Oracle ASM audit trail](admin-oracle-asm-audit-trail.md) |
| `--file_max_age` | Maximum audit file age  Note:  For more details, see [Administering Oracle ASM audit trail](admin-oracle-asm-audit-trail.md) |
| `--use_def` | Resets or sets the value back to default value. |
| `--os` | Clears property of OS audit trail type. |
| `--uni` | Clears property of Unified audit trail type. |

Note:

The default value for the age of an audit file is 5 Days and the default value for the size of an audit file is 10 MB.

Examples

The following are examples of `audclearproperty` command.

The example below sets the `file_max_size` property for the audit files of OS audit trail type to its default value.

Example 10-3 Using the ASMCMD audclearproperty command

```
ASMCMD> audclearproperty --file_max_size --use_def --os
```

The example below specifies to clear the `file_max_age` property for the audit files of Unified audit trail type. In other words, it sets `file_max_age` property to zero.

Example 10-4 Using the ASMCMD audclearproperty command

```
ASMCMD> audclearproperty --file_max_age --uni
```

#### audcleartimestamp

Purpose

Clears the last archive timestamp set by audsettimestamp.

Syntax and Description

```
audcleartimestamp {--os  --inst <instancenumber> |--uni}
```

Options for the `audcleartimestamp` command

Table 10-4 Options for the audcleartimestamp command

| Option | Description |
| --- | --- |
| `--os` | Clears the last archive timestamp set for OS audit trail type. |
| `--uni` | Clears the last archive timestamp set for Unified audit trail type. |
| `--inst` `<instancenumber>` | Instance number |

Examples

The following are examples of `audcleartimestamp` command.

The example below clears the last archive timestamp set for instance number 1 of OS audit trail type.

Example 10-5 Using the ASMCMD audcleartimestamp command

```
ASMCMD> audcleartimestamp --os --inst 1
```

The example below clears the last archive timestamp set for Unified audit trail type.

Example 10-6 Using the ASMCMD audcleartimestamp command

```
ASMCMD> audcleartimestamp --uni
```

#### audcreatejob

Purpose

Creates a purge job for specified audit trail type. The purge job runs at a frequency specified by ` --int` and purges the audit files.

Syntax and Description

```
audcreatejob --name <job_name> --int <purge_int> {--os | --uni} [--use_ts]
```

Options for the `audcreatejob` command.

Table 10-5 Options for the audcreatejob command

| Option | Description |
| --- | --- |
| `--name` `<job_name>` | Name of the purge job |
| `--int` `<purge_int>` | Purge interval in hours |
| `--os` | Purge job for OS audit trail type |
| `--uni` | Purge job for Unified audit trail type |
| `--use_ts` | When specified, the purge will be based on the last archive timestamp set by audsettimestamp command. |

Examples

The following are examples for `audcreatejob` command.

The example below creates a job called `OSAUD_PURGE` with purge interval 10 hours for OS audit trail type and the job will use the timestamp, set earlier using `audsettimestamp`, while purging audit files (since `--use_ts` is specified).

Example 10-7 Using the ASMCMD audcreatejob command

```
ASMCMD> audcreatejob --name OSAUD_PURGE --int 10 --os --use_ts
```

The example below creates a job called `OSAUD_NOTS` with purge interval 10 hours for OS audit trail type and the job will NOT use the timestamp, set earlier using `audsettimestamp`, while purging audit files (since `--use_ts` is NOT specified).

Example 10-8 Using the ASMCMD audcreatejob command

```
ASMCMD> audcreatejob --name OSAUD_NOTS --int 10 –os
```

#### auddropjob

Purpose

Drops the specified audit purge job. This command does not require any audit trail type information.

Syntax and Description

```
auddropjob --name <job_name>
```

Options for the `auddropjob` command.

Table 10-6 Options for the auddropjob command

| Option | Description |
| --- | --- |
| `--name` `<job_name>` | Name of the purge job |

Examples

The following drops the audit purge job `OSAUD_PURGE`.

Example 10-9 Using the ASMCMD auddropjob command

```
ASMCMD> auddropjob --name OSAUD_PURGE
```

#### audsetdebug

Purpose

Sets the tracing to the specified debug level.

Syntax and Description

```
audsetdebug {--debug | --error}
```

Options for the `audsetdebug` command.

Table 10-7 Options for the audsetdebug command

| Option | Description |
| --- | --- |
| `--debug` | Dumps all debug information into the traces. |
| `--error` | Dumps only error information into the traces. |

Note:

The default debug level is "error".

Examples

The following example sets the debug level to " `debug` ".

Example 10-10 Using the ASMCMD audsetdebug command

```
ASMCMD> audsetdebug --debug
```

#### audsetjobinterval

Purpose

Sets the job interval for the specified audit purge job.

Syntax and Description

```
audsetjobinterval --name <job_name>  --int <interval>
```

Options for the `audsetjobinterval` command.

Table 10-8 Options for the audsetjobinterval command

| Option | Description |
| --- | --- |
| `--name` `<job_name>` | Name of audit purge job |
| `--int` `<interval>` | Interval in hours |

Examples

The following example sets the interval of audit cleanup job `OSAUD_PURGE` to 10 hours.

Example 10-11 Using the ASMCMD audsetjobinterval command

```
ASMCMD> audsetjobinterval --name OSAUD_PURGE --int 10
```

#### audsetjobstatus

Purpose

Sets the status of the specified purge job to enabled or disabled state.

Syntax and Description

```
audsetjobstatus --name <job_name>  {--disable | --enable}
```

Options for the `audsetjobstatus` command.

Table 10-9 Options for the audsetjobstatus command

| Option | Description |
| --- | --- |
| `--name` `<job_name>` | Audit purge job name |
| `--enable/--disable` | Enables or disables the given job. |

Note:

Audit purge job, when disabled, will not purge audit files periodically.

Examples

The following example disables the audit job `OSAUD_PURGE`.

Example 10-12 Using the ASMCMD audsetjobstatus command

```
ASMCMD> audsetjobstatus --name OSAUD_PURGE --disable
```

#### audsetproperty

Purpose

Sets the value of specified audit property for given audit trail type.

Syntax and Description

```
audsetproperty {--file_max_size | --file_max_age } --val <value> {--os | --uni}
```

Options for the `audsetproperty` command.

Table 10-10 Options for the audsetproperty command

| Option | Description |
| --- | --- |
| `--file_max_size` | Maximum size of the audit file  Note:  The value for `file_max_size` property must be in range \[1,2000000\] KB. |
| `--file_max_age` | Maximum age of the audit file  Note:  The value for `file_max_age` property must be in range \[1, 497\] days. |
| `--val` `<value>` | Value of the property |
| `--os` | Sets property for OS audit trail type. |
| `--uni` | Sets property for Unified audit trail type. |

Examples

The following are examples of the `audsetproperty` command.

The example below sets the `file_max_size` property for the audit files of OS audit trail type audit file to 10 KB.

Example 10-13 Using the ASMCMD audsetproperty command

```
ASMCMD> audsetproperty --file_max_size --val 10 --os
```

The example below sets the `file_max_age` property for the audit files of Unified audit trail type to 10 Days.

Example 10-14 Using the ASMCMD audsetproperty command

```
ASMCMD> audsetproperty --file_max_age --val 10 --uni
```

#### audsettimestamp

Purpose

Sets the last archive timestamp for specified audit trail type. This timestamp will be used by the audit purge job and `audcleanaudittrail` command, if they are configured with `--useTimestamp` option. In case of OS audit trail type, instance number is required.

Syntax and Description

```
audsettimestamp {--os|--uni} [--inst <id>] <timestamp>
```

Options for the `audsettimestamp` command.

Table 10-11 Options for the audsettimestamp command

| Option | Description |
| --- | --- |
| `--os` | Last archive timestamp for OS audit trail type |
| `--uni` | Last archive timestamp for Unified audit trail type |
| `--inst` `<id>` | Instance number |
| `<timestamp>` | Timestamp |

Examples

The following example sets the last archive timestamp of OS audit trail type in instance number 1.

Example 10-15 Using the ASMCMD audsettimestamp command

```
ASMCMD> audsettimestamp --os --inst 1 22-AUG-2012 07:48:53
```

#### audshowtimestamp

Purpose

Displays the last archive timestamp set using " `audsettimestamp` " command.

Syntax and Description

```
audshowtimestamp [{--os|--uni}] [-g]
```

Options for the `audshowtimestamp` command.

Table 10-12 Options for audshowtimestamp command

| Option | Description |
| --- | --- |
| `--os` | Displays last archive timestamp set for OS audit trail type. |
| `--uni` | Displays last archive timestamp set for Unified audit trail type. |
| `-g` | Displays clusterwide timestamp information. |

Examples

The following are examples of the `audshowtimestamp` command.

The example below displays the last archive timestamp set for OS audit trail type.

Example 10-16 Using the ASMCMD audshowtimestamp command

```
ASMCMD> audshowtimestamp --os
```

The example below displays the clusterwide timestamp information for OS audit trail type.

Example 10-17 Using the ASMCMD audshowtimestamp command

```
ASMCMD> audshowtimestamp --os -g
```

See Also:

- [Database Reference](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_AUDIT_LAST_ARCH_TS.html#GUID-92CBF38B-DF4E-4070-8873-CC0FB803CCD3) for `V$ASM_AUDIT_LAST_ARCH_TS`

#### lsaudcleanupjobs

Purpose

Displays the configured audit trail purge jobs.

Syntax and Description

```
lsaudcleanupjobs [--os |--uni]
```

Options for the `lsaudcleanupjobs` command.

Table 10-13 Options for lsaudcleanupjobs command

| Option | Description |
| --- | --- |
| `--os` | Displays only the purge job configured for OS audit trail type. |
| `--uni` | Displays only the purge job configured for Unified audit trail type. |

Note:

`lsaudcleanupjobs` displays the purge jobs configured for both OS and Unified audit trail types, when no audit trail option is provided.

Examples

The following example queries audit cleanup jobs configured for OS audit trail type.

Example 10-18 Using the ASMCMD lsaudcleanupjobs command

```
ASMCMD> lsaudcleanupjobs --os
```

See Also:

- [Database Reference](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_AUDIT_CLEANUP_JOBS.html#GUID-9356CDB7-4760-4FC3-B2AD-0E62E5ED6061) for `V$ASM_AUDIT_CLEANUP_JOBS`

#### lsaudconfigparams

Purpose

Displays the configured audit trail properties for the given audit trail type.

Syntax and Description

```
lsaudconfigparams [{--os|--uni}]
```

Options for the `lsaudconfigparams` command.

Table 10-14 Options for lsaudconfigparams command

| Option | Description |
| --- | --- |
| `--os` | Displays only the audit trail properties of OS audit trail type. |
| `--uni` | Displays only the audit trail properties of unified audit trail type. |

Note:

`lsaudconfigparams` displays the audit configuration properties for both OS and Unified audit trail type, when no audit trail type option is provided.

Examples

The following example queries audit configuration parameters for OS audit trail type.

Example 10-19 Using the ASMCMD lsaudconfigparams command

```
ASMCMD> lsaudconfigparams --os
```

See Also:

- [Database Reference](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_AUDIT_CONFIG_PARAMS.html#GUID-D8B813F8-B689-4467-AA84-D0DDD4223870) for `V$ASM_AUDIT_CONFIG_PARAMS`
---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/asmcmd-filterdriver-commands.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

This topic provides a summary of the ASMCMD Oracle ASM filter driver (Oracle ASMFD) management commands.

See Also:

[Oracle Grid Infrastructure Installation Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWGEN) for your operating system for information about installing and configuring Oracle Grid Infrastructure

Table 10-43 lists the Oracle ASM Filter Driver management commands with brief descriptions.

Table 10-43 Summary of ASMCMD Oracle ASM Filter Driver management commands

| Command | Description |
| --- | --- |
| afd\_configure | Configures Oracle ASM Filter Driver. |
| afd\_deconfigure | Deconfigures Oracle ASM Filter Driver. |
| afd\_di | Manipulates the data integrity state in the Oracle ASM Filter Driver. |
| afd\_dsget | Retrieves the Oracle ASM Filter Driver diskstring value. |
| afd\_dsset | Sets the Oracle ASM Filter Driver diskstring value. |
| afd\_filter | Sets the Oracle ASM Filter Driver mode on a given disk path. |
| afd\_label | Sets an Oracle ASM Filter Driver label to a disk. |
| afd\_loglevelget | Retrieves the `oracleafd` logging level. |
| afd\_loglevelset | Sets the `oracleafd` logging level. |
| afd\_lsdsk | Lists Oracle ASM Filter Driver disks. |
| afd\_lslbl | Lists the disks that contain Oracle ASM Filter Driver labels. |
| afd\_refresh | Refreshes Oracle ASM Filter Driver disks using the AFD discovery string. |
| afd\_scan | Scans for Oracle ASM Filter Driver disks. |
| afd\_state | Returns the state of Oracle ASM Filter Driver. |
| afd\_unlabel | Clears an existing Oracle ASM Filter Driver label. |

### afd\_configure

Purpose

Configures Oracle ASM Filter Driver.

Syntax and Description

```
# asmcmd afd_configure  [-d | -e] [-f]
```

The following table lists the options for the `afd_configure` command.

Table 10-44 Options for the afd\_configure command

| Option | Description |
| --- | --- |
| `-d` | Disables Oracle ASMFD filtering mode. |
| `-e` | Enables Oracle ASMFD filtering mode. |
| `-f` | Force Oracle ASMFD configuration. |

The `afd_configure` command must be run noninteractively as a `root` user. Before running the command on a node, the Oracle Clusterware stack must be shut down on that node. After the `afd_configure` command has been run, restart Oracle Clusterware on each node. After running `afd_configure`, the default filtering state is enabled.

Example

The following example configures Oracle ASM Filter Driver on the node on which the command was run. `$ORACLE_HOME` in the example refers to the Oracle Grid Infrastructure home.

Example 10-52 Using the afd\_configure command

```
# $ORACLE_HOME/bin/asmcmd afd_configure
```

See Also:

- [Administering Oracle ASM Filter Driver](administer-filter-driver.md) for information about Oracle ASM Filter Driver
- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWGEN) for your operating system for information about installing and configuring Oracle Grid Infrastructure

### afd\_deconfigure

Purpose

Deconfigures Oracle ASM Filter Driver.

Syntax and Description

```
# asmcmd afd_deconfigure [-f]
```

The following table lists the options for the `afd_deconfigure` command.

Table 10-45 Options for the afd\_deconfigure command

| Option | Description |
| --- | --- |
| `-f` | Force Oracle ASMFD deconfiguration. |

The `afd_deconfigure` command must be run noninteractively as a `root` user. Before running the command on a node, the Oracle Clusterware stack must be shut down on that node. After the `afd_deconfigure` command has been run, restart Oracle Clusterware on each node.

Example

The following example deconfigures Oracle ASM Filter Driver on the node on which the command was run. `$ORACLE_HOME` in the example refers to the Oracle Grid Infrastructure home.

Example 10-53 Using the afd\_deconfigure command

```
# $ORACLE_HOME/bin/asmcmd afd_deconfigure
```

See Also:

- [Administering Oracle ASM Filter Driver](administer-filter-driver.md) for information about Oracle ASM Filter Driver
- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWGEN) for your operating system for information about installing and configuring Oracle Grid Infrastructure

### afd\_di

Purpose

Manipulates the data integrity state in the Oracle ASM Filter Driver (Oracle ASMFD).

Syntax and Description

```
afd_di {-e | -d | -q}
```

The following table lists the options for the `afd_di` command.

Table 10-46 Options for the afd\_di command

| Option | Description |
| --- | --- |
| `-e` | Enables data integrity in Oracle ASMFD. |
| `-d` | Disables data integrity in Oracle ASMFD. |
| `-q` | Queries data integrity in Oracle ASMFD. |

For information about Oracle ASM Filter Driver, refer to " [Administering Oracle ASM Filter Driver](administer-filter-driver.md) ".

Example

The following example shows the use of the `afd_di` command to enable data integrity in the Oracle ASMFD driver

Example 10-54 Using the ASMCMD afd\_di command

```
ASMCMD [+] > afd_di -e
```

### afd\_dsget

Purpose

Retrieves the Oracle ASM Filter Driver discovery diskstring value.

Syntax and Description

```
afd_dsget
```

For information about Oracle ASM Filter Driver, refer to [Administering Oracle ASM Filter Driver](administer-filter-driver.md).

Example

The following example returns the current Oracle ASM Filter Driver discovery diskstring value.

Example 10-55 Using the afd\_dsget command

```
ASMCMD [+] > afd_dsget
AFD discovery string: /dev/rdsk/mydisks/*
```

### afd\_dsset

Purpose

Sets the Oracle ASM Filter Driver discovery diskstring value.

Syntax and Description

```
afd_dsset afd_diskstring
```

The syntax options for the `afd_dsset` command are described in Table 10-47.

Table 10-47 Options for the afd\_dsset command

| Option | Description |
| --- | --- |
| `afd_diskstring` | Specifies the value for the Oracle ASM Filter Driver discovery diskstring. |

For information about Oracle ASM Filter Driver, refer to [Administering Oracle ASM Filter Driver](administer-filter-driver.md).

Example

The following example sets the current Oracle ASM Filter Driver discovery diskstring value.

Example 10-56 Using the afd\_dsset command

```
ASMCMD [+] > afd_dsset /dev/rdsk/mydisks/*
```

### afd\_filter

Purpose

Sets the Oracle ASM Filter Driver filtering mode on a given disk path.

Syntax and Description

```
afd_filter {-e | -d } [disk_path]
```

The syntax options for the `afd_filter` command are described in the following table.

Table 10-48 Options for the afd\_filter command

| Option | Description |
| --- | --- |
| `-e` | Enables Oracle ASM Filter Driver mode. |
| `-d` | Disables Oracle ASM Filter Driver mode. |
| `disk_path` | Specifies the path to the disks. |

If the command is executed without specifying a disk path, then filtering is set at the node level.

Example

The following example uses `afd_filter` to enable Oracle ASM Filter Driver filtering on a specified disk path.

Example 10-57 Using the afd\_filter command

```
ASMCMD [+] > afd_filter -e /dev/sdq
```

### afd\_label

Purpose

Sets an Oracle ASM Filter Driver (Oracle ASMFD) label to the specified disk.

Syntax and Description

```
afd_label afd_label disk_path [--migrate | --rename] [--init] [--force]
```

The syntax options for the `afd_label` command are described in Table 10-49.

Table 10-49 Options for the afd\_label command

| Option | Description |
| --- | --- |
| `afd_label` | Specifies an Oracle ASM Filter Driver label. |
| `disk_path` | Specifies the path to the disks to which the label is applied. |
| `--migrate` | Specifies to migrate Oracle ASM Filter Driver disk labels to all disks in the `disk_path`.. |
| `--rename` | Specifies to label a disk that was previously labeled. |
| `--init` | Specifies to set an Oracle ASMFD label during the initialize stage. This option is not allowed if Oracle ASMFD is already loaded. |
| `--force` | Causes the `afd_label` command to execute all steps. |

For information about Oracle ASM Filter Driver, refer to " [Administering Oracle ASM Filter Driver](administer-filter-driver.md) ".

Example

The following example sets an Oracle ASM Filter Driver label to a specified disk.

Example 10-58 Using the afd\_label command

```
ASMCMD [+] > afd_label 'disk0' '/dev/rdsk/mydisks/disk0'
```

### afd\_loglevelget

Purpose

Retrieves the `oracleafd` logging level.

Syntax and Description

```
afd_loglevelget
```

The command must be executed by a privileged user.

Examples

The following example shows the use of `afd_loglevelget` to retrieve the current `oracleafd` logging level.

Example 10-59 Using the afd\_loglevelget command

```
ASMCMD [+] > afd_loglevelget 
medium
```

### afd\_loglevelset

Purpose

Sets the `oracleafd` logging level.

Syntax and Description

```
afd_loglevelset {high | medium | low | disabled}
```

The following table lists the options for the `afd_loglevelset` command.

Table 10-50 Options for the afd\_loglevelset command

| Option | Description |
| --- | --- |
| `high \| medium \| low \| disabled` | Specifies the `oracleafd` logging level. |

The command must be executed by a privileged user.

Examples

The following examples show the use of `afd_loglevelset` to set the `oracleafd` logging level.

Example 10-60 Using the afd\_loglevelset command

```
ASMCMD [+] > afd_loglevelset medium

ASMCMD [+] > afd_loglevelset disabled
```

### afd\_lsdsk

Purpose

Lists Oracle ASM Filter Driver disks.

Syntax and Description

```
afd_lsdsk [--all]
```

The following table lists the options for the `afd_lsdsk` command.

Table 10-51 Options for the afd\_lsdsk command

| Option | Description |
| --- | --- |
| `--all` | Lists all Oracle ASMFD disks clusterwide. |

Example

The following example lists Oracle ASM Filter Driver disks.

Example 10-61 Using the afd\_lsdsk commmand

```
ASMCMD [+] > afd_lsdsk
--------------------------------------------------------------------------------
Label                     Filtering   Path
================================================================================
DISK0                       ENABLED   /dev/sdd
DISK1                      DISABLED   /dev/sdm
DISK2                       ENABLED   /dev/sdq
```

### afd\_lslbl

Purpose

Scans operating system disks using the specified discovery string and lists the disks that contain Oracle ASM Filter Driver labels.

Syntax and Description

```
afd_lslbl [disk_string]
```

The following table lists the options for the `afd_lslbl` command.

Table 10-52 Options for the afd\_lslbl command

| Option | Description |
| --- | --- |
| `disk_string` | Specifies an optional disk path string for filtering. |

For information about Oracle ASM Filter Driver, refer to " [Administering Oracle ASM Filter Driver](administer-filter-driver.md) ".

Example

The following example shows the use of the `afd_lslbl` command to list disks that contain Oracle ASMFD labels.

Example 10-62 Using the ASMCMD afd\_lslbl command

```
ASMCMD [+]> afd_lslbl '/dev/sd*' 

Label                 Duplicate  Path 
======================================= 
DISK0                 /dev/sdd 
DISK1                 /dev/sdm
```

### afd\_refresh

Purpose

Refreshes Oracle ASM Filter Driver disks using the AFD discovery string.

Syntax and Description

```
afd_refresh [--all]
```

The following table lists the options for the `afd_refresh` command.

Table 10-53 Options for the afd\_refresh command

| Option | Description |
| --- | --- |
| `–-all` | Specifies a clusterwide refresh. |

If the Oracle ASM Filter Driver disks are owned by the `root` user, then you must run `afd_refresh` `--all` as `root` to ensure that accurate disk sizes are displayed in the `V$ASM_DISK` view.

For information about Oracle ASM Filter Driver, refer to [Administering Oracle ASM Filter Driver](administer-filter-driver.md).

Example

The following example uses `afd_refresh` to refresh Oracle ASMFD disks

Example 10-63 Using the ASMCMD afd\_refresh command

```
ASMCMD [+]> afd_refresh
```

### afd\_scan

Purpose

Scans for Oracle ASM Filter Driver disks.

Syntax and Description

```
afd_scan [afd_diskstring] [--all]
```

The syntax options for the `afd_scan` command are described in Table 10-54.

Table 10-54 Options for the afd\_scan command

| Option | Description |
| --- | --- |
| `afd_diskstring` | Specifies the value for the Oracle ASM Filter Driver discovery diskstring. |
| `--all` | Specifies a clusterwide scan for Oracle ASMFD disks. |

`afd_scan` scans for Oracle ASM Filter Driver disks using the specified discovery string. If the command is executed without specifying a disk string, then `afd_scan` uses the Oracle ASM Filter Driver discovery diskstring value in the `afd.conf` file.

For information about Oracle ASM Filter Driver, refer to [Administering Oracle ASM Filter Driver](administer-filter-driver.md).

Example

The following example scans for Oracle ASM Filter Driver disks with a specified diskstring.

Example 10-64 Using the afd\_scan command

```
ASMCMD [+] > afd_scan /dev/sd*
```

### afd\_state

Purpose

Returns the state of Oracle ASM Filter Driver.

Syntax and Description

```
afd_state [--all]
```

Table 10-55 lists the options for the `afd_state` command.

Table 10-55 Options for the afd\_state command

| Option | Description |
| --- | --- |
| `--all` | The `--all` option runs a clusterwide check. |

For information about Oracle ASM Filter Driver, refer to [Administering Oracle ASM Filter Driver](administer-filter-driver.md).

Example

The following example returns the current state of Oracle ASM Filter Driver.

Example 10-65 Using the afd\_state command

```
ASMCMD [+] > afd_state
ASMCMD-9526: The AFD state is 'LOADED' and filtering is 'DEFAULT' on host 'myhost'
```

### afd\_unlabel

Purpose

Clears a specified Oracle ASM filter driver (Oracle ASMFD) label.

Syntax and Description

```
afd_unlabel afd_label {afd_label | 'disk_path'} [-f] [--init]
```

The syntax options for the `afd_unlabel` command are described in Table 10-56.

Table 10-56 Options for the afd\_unlabel command

| Option | Description |
| --- | --- |
| `afd_unlabel` | Specifies an existing Oracle ASM Filter Driver label to clear. |
| `’disk_path’` | Specifies to clear a label determined by an existing disk path. If a disk needs to be unlabeled during the initialization stage, then it can be done only by using its disk path. |
| `—f` | Forces the clearing of the label if the disk is an Oracle ASM member disk and there are no pending opens of the disk. |
| `--init` | Specifies to clear an Oracle ASMFD label during the initialize stage. This option is not allowed if Oracle ASMFD is already loaded. |

For information about Oracle ASM Filter Driver, refer to " [Administering Oracle ASM Filter Driver](administer-filter-driver.md) ".

Example

The following example clears an existing Oracle ASM Filter Driver label.

Example 10-66 Using the afd\_unlabel command

```
ASMCMD [+] > afd_unlabel 'disk0'
```
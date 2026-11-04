---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/asmcmd-template-commands.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

This topic provides a summary of the ASMCMD template management commands.

Table 10-104 lists the ASMCMD template management commands with brief descriptions.

Table 10-104 Summary of ASMCMD template management commands

| Command | Description |
| --- | --- |
| chtmpl | Changes the attributes of a template. |
| lstmpl | Lists disk group templates. |
| mktmpl | Adds a template to a disk group. |
| rmtmpl | Removes a template from a disk group. |

### chtmpl

Purpose

Changes the attributes of a template.

Syntax and Description

```
chtmpl -G diskgroup { [--striping {coarse|fine}]
     [--redundancy {high|mirror|unprotected} ] } template
```

Table 10-105 lists the syntax options for the `chtmpl` command.

Table 10-105 Options for the chtmpl command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the disk group. |
| `template` | Name of the template to change. |
| `--striping` { `coarse` \| `fine` } | Striping specification, either `coarse` or `fine`. |
| `--redundancy` { `high` \| `mirror` \| `unprotected` } | Redundancy specification, either `high`, `mirror`, or `unprotected`. |

At least one of the following options is required: `--striping` or `--redundancy`.

For information about updating templates, see " [Modifying a Disk Group Template](asm-files-directories-templates.md) ".

Example

The following is an example of the `chtmpl` command that updates the `mytemplate` template of the `data` disk group. The redundancy attribute is set to high and the striping attribute is set to fine.

Example 10-115 Using the ASMCMD chtmpl command

```
ASMCMD [+] > chtmpl -G data --redundancy high --striping fine mytemplate
```

### lstmpl

Purpose

Lists all templates for all disk groups or the templates for a specified disk group.

Syntax and Description

```
lstmpl [--suppressheader] [-l] [-G diskgroup] [pattern]
```

Table 10-106 lists the syntax options for the `lstmpl` command.

Table 10-106 Options for the lstmpl command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Specifies disk group name. |
| `--suppressheader` | Suppresses column headings. |
| `-l` | Displays all details. |
| `pattern` | Displays the templates that match pattern expression. |

For information about template attributes, see " [Template Attributes](asm-files-directories-templates.md) ".

Example

The following is an example of the `lstmpl` command. The example lists all details of the templates in the `data` disk group.

Example 10-116 Using the ASMCMD lstmpl command

```
ASMCMD [+] > lstmpl -l -G data

Group_Name  Group_Num  Name                       Stripe  Sys  Redund  PriReg  MirrReg  
DATA        1          ARCHIVELOG                 COARSE  Y    MIRROR  COLD    COLD
DATA        1          ASMPARAMETERFILE           COARSE  Y    MIRROR  COLD    COLD
DATA        1          AUDIT_SPILLFILES           COARSE  Y    MIRROR  COLD    COLD
DATA        1          AUTOBACKUP                 COARSE  Y    MIRROR  COLD    COLD
DATA        1          AUTOLOGIN_KEY_STORE        COARSE  Y    MIRROR  COLD    COLD
DATA        1          BACKUPSET                  COARSE  Y    MIRROR  COLD    COLD
DATA        1          CHANGETRACKING             COARSE  Y    MIRROR  COLD    COLD
DATA        1          CONTROLFILE                FINE    Y    HIGH    COLD    COLD
DATA        1          DATAFILE                   COARSE  Y    MIRROR  COLD    COLD
DATA        1          DATAGUARDCONFIG            COARSE  Y    MIRROR  COLD    COLD
DATA        1          DUMPSET                    COARSE  Y    MIRROR  COLD    COLD
DATA        1          FLASHBACK                  COARSE  Y    MIRROR  COLD    COLD
DATA        1          FLASHFILE                  COARSE  Y    MIRROR  COLD    COLD
DATA        1          INCR XTRANSPORT BACKUPSET  COARSE  Y    MIRROR  COLD    COLD
DATA        1          KEY_STORE                  COARSE  Y    MIRROR  COLD    COLD
DATA        1          OCRFILE                    COARSE  Y    MIRROR  COLD    COLD
DATA        1          ONLINELOG                  COARSE  Y    MIRROR  COLD    COLD
DATA        1          PARAMETERFILE              COARSE  Y    MIRROR  COLD    COLD
DATA        1          TEMPFILE                   COARSE  Y    MIRROR  COLD    COLD
DATA        1          VOTINGFILE                 COARSE  Y    MIRROR  COLD    COLD
DATA        1          XTRANSPORT                 COARSE  Y    MIRROR  COLD    COLD
DATA        1          XTRANSPORT BACKUPSET       COARSE  Y    MIRROR  COLD    COLD
```

### mktmpl

Purpose

Adds a template to a disk group.

Syntax and Description

```
mktmpl -G diskgroup [--striping {coarse|fine}]
     [--redundancy {high|mirror|unprotected}] template
```

Table 10-107 lists the syntax options for the `mktmpl` command.

Table 10-107 Options for the mktmpl command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the disk group. |
| `template` | Name of the template to create. |
| `--striping` { `coarse` \| `fine` } | Striping specification, either `coarse` or `fine`. |
| `--redundancy` { `high` \| `mirror` \| `unprotected` } | Redundancy specification, either `high`, `mirror`, or `unprotected`. |

For information about adding templates, see [Adding Templates to a Disk Group](asm-files-directories-templates.md).

Example

The following is an example of the `mktmpl` command that adds the `mytemplate` template to the `data` disk group. The new template has the redundancy set to mirror and the striping set to coarse.

Example 10-117 Using the ASMCMD mktmpl command

```
ASMCMD [+] > mktmpl -G data --redundancy mirror --striping coarse mytemplate
```

### rmtmpl

Purpose

Removes a template from a disk group.

Syntax and Description

```
rmtmpl -G diskgroup template
```

Table 10-108 lists the syntax options for the `rmtmpl` command.

Table 10-108 Options for the rmtmpl command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the disk group. |
| `template` | Name of the template to delete. |

For information about template attributes, see " [Template Attributes](asm-files-directories-templates.md) ".

Example

The following is an example of the `rmtmpl` command that removes the `mytemplate` template from the `data` disk group.

Example 10-118 Using the ASMCMD rmtmpl command

```
ASMCMD [+] > rmtmpl -G data mytemplate
```
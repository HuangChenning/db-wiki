---
title: ASMCMD Template Management Commands
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asm_util005.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

This section describes the ASMCMD template management commands.

Table 12-48 provides a summary of the template management commands.

Table 12-48 Summary of ASMCMD template management commands

| Command | Description |
| --- | --- |
| chtmpl | Changes the attributes of a template. |
| lstmpl | Lists disk group templates. |
| mktmpl | Adds a template to a disk group. |
| rmtmpl | Removes a template from a disk group. |

## chtmpl

Purpose

Changes the attributes of a template.

Syntax and Description

  
`chtmpl` `-G` `diskgroup` { \[`--striping` { `coarse` | `fine` }\]  
 \[`--redundancy` { `high` | `mirror` | `unprotected` } \] \[`--primary` { `hot` | `cold` }\]  
 \[`--secondary` { `hot` | `cold` }\]} `template`  

Table 12-49 lists the syntax options for the `chtmpl` command.

Table 12-49 Options for the chtmpl command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the disk group. |
| `template` | Name of the template to change. |
| `--striping` { `coarse` \| `fine` } | Striping specification, either `coarse` or `fine`. |
| `--redundancy` { `high` \| `mirror` \| `unprotected` } | Redundancy specification, either `high`, `mirror`, or `unprotected`. |
| `--primary` { `hot` \| `cold` } | Intelligent Data Placement specification for primary extents, either `hot` or `cold` region. |
| `--secondary` { `hot` \| `cold` } | Intelligent Data Placement specification for secondary extents, either `hot` or `cold` region. |

At least one of these options is required: `--striping`, `--redundancy`, `--primary`, or `--secondary`.

For information about updating templates, see ["Modifying a Disk Group Template"](asmfiles.md).

Example

The following is an example of the `chtmpl` command that updates the `mytemplate` template of the `data` disk group. The redundancy attribute is set to high and the striping attribute is set to fine.

Example 12-52 Using the ASMCMD chtmpl command

```
ASMCMD [+] > chtmpl -G data --redundancy high --striping fine mytemplate
```

## lstmpl

Purpose

Lists all templates for all disk groups or the templates for a specified disk group.

Syntax and Description

  
`lstmpl` \[`--suppressheader`\] \[`-l`\] \[`-G` `diskgroup`\] \[`pattern`\]  

Table 12-50 lists the syntax options for the `lstmpl` command.

Table 12-50 Options for the lstmpl command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Specifies disk group name. |
| `--suppressheader` | Suppresses column headings. |
| `-l` | Displays all details. |
| `pattern` | Displays the templates that match pattern expression. |

For information about template attributes, see ["Template Attributes"](asmfiles.md).

Example

The following is an example of the `lstmpl` command. The example lists all details of the templates in the `data` disk group.

Example 12-53 Using the ASMCMD lstmpl command

```
ASMCMD [+] > lstmpl -l -G data

Group_Name  Group_Num  Name                 Stripe  Sys  Redund  PriReg  MirrReg  
DATA        1          ARCHIVELOG           COARSE  Y    MIRROR  COLD    COLD     
DATA        1          ASMPARAMETERFILE     COARSE  Y    MIRROR  COLD    COLD     
DATA        1          AUTOBACKUP           COARSE  Y    MIRROR  COLD    COLD     
DATA        1          BACKUPSET            COARSE  Y    MIRROR  COLD    COLD     
DATA        1          CHANGETRACKING       COARSE  Y    MIRROR  COLD    COLD     
DATA        1          CONTROLFILE          FINE    Y    HIGH    COLD    COLD     
DATA        1          DATAFILE             COARSE  Y    MIRROR  COLD    COLD     
DATA        1          DATAGUARDCONFIG      COARSE  Y    MIRROR  COLD    COLD     
DATA        1          DUMPSET              COARSE  Y    MIRROR  COLD    COLD     
DATA        1          FLASHBACK            COARSE  Y    MIRROR  COLD    COLD     
DATA        1          FLASHFILE            COARSE  Y    MIRROR  COLD    COLD     
DATA        1          MYTEMPLATE           FINE    N    HIGH    COLD    COLD     
DATA        1          OCRFILE              COARSE  Y    MIRROR  COLD    COLD     
DATA        1          ONLINELOG            COARSE  Y    MIRROR  COLD    COLD     
DATA        1          PARAMETERFILE        COARSE  Y    MIRROR  COLD    COLD     
DATA        1          TEMPFILE             COARSE  Y    MIRROR  COLD    COLD
DATA        1          XTRANSPORT           COARSE  Y    MIRROR  COLD    COLD
```

## mktmpl

Purpose

Adds a template to a disk group.

Syntax and Description

  
`mktmpl` `-G` `diskgroup` \[`--striping` { `coarse` | `fine` }\]  
 \[`--redundancy` { `high` | `mirror` | `unprotected` } \] \[`--primary` { `hot` | `cold` }\]  
 \[`--secondary` { `hot` | `cold` }\] `template`  

Table 12-51 lists the syntax options for the `mktmpl` command.

Table 12-51 Options for the mktmpl command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the disk group. |
| `template` | Name of the template to create. |
| `--striping` { `coarse` \| `fine` } | Striping specification, either `coarse` or `fine`. |
| `--redundancy` { `high` \| `mirror` \| `unprotected` } | Redundancy specification, either `high`, `mirror`, or `unprotected`. |
| `--primary` { `hot` \| `cold` } | Intelligent Data Placement specification for primary extents, either `hot` or `cold` region. |
| `--secondary` { `hot` \| `cold` } | Intelligent Data Placement specification for secondary extents, either `hot` or `cold` region. |

For information about adding templates, see ["Adding Templates to a Disk Group"](asmfiles.md).

Example

The following is an example of the `mktmpl` command that adds the `mytemplate` template to the `data` disk group. The new template has the redundancy set to mirror and the striping set to coarse.

Example 12-54 Using the ASMCMD mktmpl command

```
ASMCMD [+] > mktmpl -G data --redundancy mirror --striping coarse mytemplate
```

## rmtmpl

Purpose

Removes a template from a disk group.

Syntax and Description

  
`rmtmpl` `-G` `diskgroup` `template`  

Table 12-52 lists the syntax options for the `rmtmpl` command.

Table 12-52 Options for the rmtmpl command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the disk group. |
| `template` | Name of the template to delete. |

For information about template attributes, see ["Template Attributes"](asmfiles.md).

Example

The following is an example of the `rmtmpl` command that removes the `mytemplate` template from the `data` disk group.

Example 12-55 Using the ASMCMD rmtmpl command

```
ASMCMD [+] > rmtmpl -G data mytemplate
```
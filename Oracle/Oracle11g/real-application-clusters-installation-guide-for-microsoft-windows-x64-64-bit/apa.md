---
title: Directory Structure for Oracle Real Application Clusters Environments
book: Real Application Clusters Installation Guide for Microsoft Windows x64 (64-Bit)
doc_id: E48195-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e48195/apa.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-microsoft-windows-x64-64-bit
---

## D Directory Structure for Oracle Real Application Clusters Environments

This appendix describes the directory structures for Oracle Real Application Clusters (Oracle RAC) software environments. This appendix contains the following topics:

- Understanding the Oracle RAC Directory Structure
- Directory Structures for Oracle RAC

## D.1 Understanding the Oracle RAC Directory Structure

When you install Oracle Database 11g release 2 (11.2) with Oracle RAC, all subdirectories except for the Oracle Inventory directory, the Oracle Automatic Storage Management (Oracle ASM) home (if applicable), and the Oracle Clusterware home, are under a top-level Oracle base directory. The Oracle home and `admin` directories are also located under the Oracle base directory.

See Also:

[Oracle Database Installation Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/install.112/e47798/ofa.htm#NTDBI008) for more information about the Oracle home and `admin` directories

## D.2 Directory Structures for Oracle RAC

Table D-1 shows the hierarchical directory tree of a sample Optimal Flexible Architecture (OFA)-compliant database for Oracle RAC:

Table D-1 Directory Structure for a Sample OFA-Compliant Environment

| Root | Second-Level | Third-Level | Fourth-Level | Description |
| --- | --- | --- | --- | --- |
| `%ORACLE_BASE%` |  |  |  | `C:\app\oracle`  The default `ORACLE_BASE` directory, where the software was installed by the user `oracle`. |
|  | installation type |  |  | `C:\app\oracle\product\11.2.0\db`  The type of installation under the Oracle base directory. For example, when installing Oracle Database 11g release 2, the value for installation type is `product\11.2.0\db`. |
|  |  | `%ORACLE_HOME%` |  | The location in which the Oracle Database software is installed. You can also choose to add a counter, if you have multiple installations of the software. For example, if you are creating a second Oracle home for the Oracle Database 11g release 2 software, then the path is as follows:  ``` C:\app\oracle\product\11.2.0\dbhome_2 ```  Note that the Oracle database home is under the Oracle base directory path. An Oracle Clusterware directory must not be under the Oracle base directory path where the database executable files are located. |
|  |  |  | `database` | The directory in which the local initialization parameter file is stored for the database. |
|  | `admin` |  |  | The administrative directory. Note that with Oracle Database 11g and later releases, `bdump`, `cdump`, and `udump` files are relocated to the directory associated with `%ADR_BASE%`. |
|  |  | `db_unique_name` |  | The database unique name; this is the same as `dbname` when the database name is 8 or fewer characters in length. For example, if your database name is `sales`, the directory path is:  ``` C:\app\oracle\admin\sales ``` |
|  |  |  | `/hdump`  `/pfile` | The dump destinations for the database server. |
|  | `%ADR_BASE%` |  | `/bdump`  `/cdump`  `/udump` | Automatic Diagnostic Repository dump destination trace files. Note that this directory path is set by the initialization parameter `DIAGNOSTIC_DEST`, and that the path for the Automatic Diagnostic Repository must be located on a shared storage location available to all the nodes.  By default, this path is a subset of the Oracle base directory, in the following path:  `%ORACLE_BASE%\diag\` |
| Oracle Grid Infrastructure for a cluster home (Grid home) |  |  |  | An OFA-compliant path for the Oracle Clusterware home. The default value is:  `C:\app\11.2.0\grid`  During the Oracle Grid Infrastructure for a cluster installation, Oracle Clusterware and Oracle Automatic Storage Management (Oracle ASM) software is installed. |
|  | ``` bin ``` |  |  | The subtree for Oracle Clusterware and Oracle ASM executable files. |
|  | ``` network ``` |  |  | The subtree for Oracle Net Services configuration files and utilities. |

See Also:

[Oracle Database Installation Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/install.112/e47798/ofa.htm#NTDBI008) for more information about the Optimal Flexible Architecture standard used on Microsoft Windows platforms
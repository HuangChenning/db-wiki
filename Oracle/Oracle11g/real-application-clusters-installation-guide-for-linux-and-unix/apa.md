---
title: Directory Structure for Oracle Real Application Clusters Environments
book: Real Application Clusters Installation Guide for Linux and UNIX
doc_id: E41962-05
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41962/apa.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-linux-and-unix
---

## D Directory Structure for Oracle Real Application Clusters Environments

This appendix describes the directory structures for Oracle Real Application Clusters (Oracle RAC) software environments. This appendix contains the following topics:

- Understanding the Oracle RAC Directory Structure
- Directory Structures for Oracle RAC

## D.1 Understanding the Oracle RAC Directory Structure

When you install Oracle Database 11g release 2 (11.2) with Oracle RAC, all subdirectories except for `oraInventory`, the Oracle Automatic Storage Management home (if applicable), and the Oracle Clusterware home, are under a top-level `ORACLE_BASE` directory. The `ORACLE_HOME` and `ADMIN` directories are also located under `ORACLE_BASE`.

See Also:

The [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for further information about the `$ORACLE_HOME` and `/ADMIN` directories

## D.2 Directory Structures for Oracle RAC

Table D-1 shows the hierarchical directory tree of a sample optimal flexible architecture (OFA)-compliant database for Oracle RAC:

Table D-1 Directory Structure for A Sample OFA-Compliant Environment

| Root | Second-level | Third-level | Fourth-level | Description |
| --- | --- | --- | --- | --- |
| `$ORACLE_BASE` |  |  |  | `/u01/app/oracle`  The default `ORACLE_BASE` directory, where the software owner is the `oracle` user. |
|  | `ORACLE_HOME` |  |  | `/u01/app/oracle/11.2.0/`  The default name of the Oracle home. Note that the Oracle database home is under the Oracle base directory path. An Oracle Clusterware directory must not be under the Oracle base directory path where the database binaries are located. |
|  |  | `installation_type` |  | Type of installation under the Oracle base directory. You can also choose to add a counter, if you intend to have more than one installation of the software. For example, with an Oracle database installation, where the database is the second database, the path is as follows:  ``` /u01/app/oracle/11.2.0/dbhome_2 ``` |
|  | `/ADMIN` |  |  | The administrative directory. Note that with Oracle Database 11g, `bdump`, `cdump`, and `udump` files are relocated to the directory `$ADR_BASE`. |
|  |  | `/db_unique_name` |  | The database unique name; this is the same as `dbname` when the database name is 8 or fewer characters in length. |
|  |  |  | `/hdump`  `/pfile` | The dump destinations for database server. |
| `$ADR_BASE` |  |  | `/bdump`  `/cdump`  `/udump` | Automatic Diagnostic Repository dump destination trace files. Note that this directory path is set by the initialization parameter `DIAGNOSTIC_DEST`, and that the path for the Automatic Data Repository must be located on a shared storage location available to all the nodes.  By default, this path is a subset of the Oracle base directory, in the following path:  `$ORACLE_BASE/diag/` |
| ``` Oracle Grid Infrastructure for a cluster home (Grid home) ``` |  |  |  | `/u01/app/grid/11.2.0/`  An OFA-compliant path for the Oracle Clusterware home.  During the Oracle Grid Infrastructure for a cluster installation, Oracle Clusterware and Oracle Automatic Storage Management (Oracle ASM) software is installed. The `root.sh` script changes permissions of all of the parent directories of the Oracle Clusterware home directory to grant write access only to the root user. Because of this, the Oracle Clusterware home directory must not be a subdirectory of the Oracle base directory. |
|  |  | ``` /bin ``` |  | The subtree for Oracle binaries. |
|  |  | ``` /network ``` |  | The subtree for Oracle Net. |

See Also:

[Oracle Database Administrator's Reference for Linux and UNIX-Based Operating Systems](https://docs.oracle.com/cd/E11882_01/server.112/e10839/toc.htm) for further information about the `$ORACLE_HOME` and `/admin` directories
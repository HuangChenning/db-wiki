---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_VOLUME.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.73 V$ASM\_VOLUME

In an Oracle Automatic Storage Management (Oracle ASM) instance, `V$ASM_VOLUME` displays information about each Oracle ADVM volume.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Cluster-wide number assigned to the disk group (composite primary key) |
| `VOLUME_NAME` | `VARCHAR2(30)` | Name of the volume |
| `COMPOUND_INDEX` | `NUMBER` | A 32-bit number consisting of a disk group number in the high-order 8 bits and a volume number in the low-order 24 bits (for efficient access to the view) |
| `SIZE_MB` | `NUMBER` | Size of the volume (in megabytes) |
| `VOLUME_NUMBER` | `NUMBER` | Number of the Volume within the disk group (composite primary key) |
| `REDUNDANCY` | `VARCHAR2(6)` | Redundancy type for the volume:  - `UNPROT` - `HIGH` - `MIRROR` |
| `STRIPE_COLUMNS` | `NUMBER` | Number of columns in a stripe set |
| `STRIPE_WIDTH_K` | `NUMBER` | Stripe width of the volume (in kilobytes) |
| `STATE` | `VARCHAR2(8)` | Indicates whether the volume is enabled (`ENABLED`), disabled (`DISABLED`), or remote (`REMOTE`) |
| `FILE_NUMBER` | `NUMBER` | Volume file number |
| `INCARNATION` | `NUMBER` | Volume file incarnation number |
| `DRL_FILE_NUMBER` | `NUMBER` | Volume Dirty Region Logging (DRL) file used for mirrored volumes |
| `RESIZE_UNIT_MB` | `NUMBER` | Volume allocation unit (in megabytes) that a volume can be created |
| `USAGE` | `VARCHAR2(30)` | Optional usage string for the volume |
| `VOLUME_DEVICE` | `VARCHAR2(256)` | OSD path for the volume device |
| `MOUNTPATH` | `VARCHAR2(1024)` | Optional mount path string for the volume |
| `PRIMARY_REGION` <sup>Foot 1</sup> | `VARCHAR2(4)` | Region used for allocating primary extents:  - `HOT` - `COLD` |
| `MIRROR_REGION` <sup>Foot 1</sup> | `VARCHAR2(4)` | Region used for allocating mirrored extents:  - `HOT` - `COLD` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

<sup>Footnote 1</sup> Intelligent Data Placement is desupported starting with Oracle Database 21c. As a result, the `PRIMARY_REGION` and `MIRROR_REGION` columns are no longer meaningful.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information
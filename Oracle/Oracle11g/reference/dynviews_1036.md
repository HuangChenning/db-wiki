---
title: "V$ASM_VOLUME"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1036.htm
tags:
  - oracle
  - 11g
  - reference
---

In an Oracle Automatic Storage Management (Oracle ASM) instance, `V$ASM_VOLUME` displays information about each Oracle ADVM volume.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Cluster-wide number assigned to the disk group (composite primary key) |
| `VOLUME_NAME` | `VARCHAR2(30)` | Name of the volume |
| `COMPOUND_INDEX` | `NUMBER` | A 32-bit number consisting of a disk group number in the high-order 8 bits and a volume number in the low-order 24 bits (for efficient access to the view) |
| `SIZE_MB` | `NUMBER` | Size of the volume (in megabytes) |
| `VOLUME_NUMBER` | `NUMBER` | Number of the Volume within the disk group (composite primary key) |
| `REDUNDANCY` | `VARCHAR2(6)` | Redundancy type for the volume: - `UNPROT` - `HIGH` - `MIRROR` |
| `STRIPE_COLUMNS` | `NUMBER` | Number of columns in a stripe set |
| `STRIPE_WIDTH_K` | `NUMBER` | Stripe width of the volume (in kilobytes) |
| `STATE` | `VARCHAR2(8)` | Indicates whether the volume is enabled (`ENABLED`) or disabled (`DISABLED`) |
| `FILE_NUMBER` | `NUMBER` | Volume file number |
| `INCARNATION` | `NUMBER` | Volume file incarnation number |
| `DRL_FILE_NUMBER` | `NUMBER` | volume Dirty Region Logging (DRL) file used for mirrored volumes |
| `RESIZE_UNIT_MB` | `NUMBER` | Volume allocation unit (in megabytes) that a volume can be created |
| `USAGE` | `VARCHAR2(30)` | Optional usage string for the volume |
| `VOLUME_DEVICE` | `VARCHAR2(256)` | OSD path for the volume device |
| `MOUNTPATH` | `VARCHAR2(1024)` | Optional mount path string for the volume |
---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: E85760-09
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/admin/administering-cdbs-and-pdbs-with-cloud-control.html
tags:
  - oracle
  - 12c
  - administrators-guide
---

- Administering CDB Storage and Schema Objects with Cloud Control  
	You can administer CDB storage and schema objects with Oracle Enterprise Manager Cloud Control.
- Administering PDBs with Cloud Control  
	You can use Oracle Enterprise Manager Cloud Control to switch between PDBs and alter the open mode of a PDB.

See Also:

" [About Administering a CDB](administering-a-cdb-with-sql-plus.md) "

**Parent topic:** [Managing a Multitenant Environment](managing-a-multitenant-environment.md)

### 42.1 Administering CDB Storage and Schema Objects with Cloud Control

You can administer CDB storage and schema objects with Oracle Enterprise Manager Cloud Control.

**Parent topic:** Administering CDBs and PDBs with Cloud Control

#### 42.1.1 About Managing and Monitoring CDB Storage and Schema Objects

You can use Enterprise Manager to manage and monitor CDB storage and schema objects.

With Enterprise Manager you can:

- View database storage objects, such as tablespaces, and schema objects, such as tables, across the CDB. You can also view objects belonging to the `CDB$ROOT` container.
- View and manage database storage and schema objects at the container level.
- Use storage metrics to gather data across the CDB and generate Enterprise Manager incidents (alerts) at the container level.
- Run Storage and Undo Advisors for the CDB and view related storage advice.
- Support configuration metric collection for CDB/PDB.

The Database Object Search pages are displayed when you select certain menu items from either the Schema or Administration menus. These pages conduct searches for database objects based on criteria you enter, such as schema name, object name, or container name, which is only available if you are viewing from the CDB level. The Database Object Search page features are supported at both the CDB level and PDB level. The Container column displays on the Search page at both the CDB level and container level.

Undo tablespaces can only be managed from the `CDB$ROOT` container.

**Parent topic:** Administering CDB Storage and Schema Objects with Cloud Control

#### 42.1.2 Managing CDB Storage and Schema Objects

You can manage CDB storage and schema objects with Oracle Enterprise Manager Cloud Control.

To manage CDB storage and schema objects, follow these steps:

1. Navigate to the CDB database home page.
2. From the CDB menu, access a feature supporting the CDB level view, such as accessing the Tablespaces Search page.
3. Log in as a common user. The Tablespaces Search page displays in the CDB context.
4. Perform a search. In the above example, the Tablespace page displays all tablespaces within the CDB including those belonging to the `CDB$ROOT` container. An additional column displays the container name.
5. Perform any management feature if you have the proper privilege associated with that operation.

**Parent topic:** Administering CDB Storage and Schema Objects with Cloud Control

#### 42.1.3 Managing Per-Container Storage and Schema Objects

You can manager per-container storage and schema objects with Oracle Enterprise Manager Cloud Control.

To manage per-container storage and schema objects, follow these steps:

1. Navigate to a CDB target.
2. From the Administration menu, select Storage, then, select Tablespaces.
3. Log in as a common user. The Tablespaces Search page is displayed using CDB as its context.
4. Switch to a specific container. Once context switcher is used to switch containers, the pages automatically refresh and show container-only data.
5. Perform a search. The Tablespace page displays all tablespaces within the selected container.
6. You can perform any management feature for which you have the proper privilege associated with that operation.

**Parent topic:** Administering CDB Storage and Schema Objects with Cloud Control

#### 42.1.4 Monitoring Storage and Schema Alerts

You can monitor storage and schema alerts with Oracle Enterprise Manager Cloud Control.

To monitor storage and schema alerts, follow these steps:

1. Navigate to a Pluggable Database target.
2. From the Oracle Database menu, select Monitoring, then select Incident Manager.
	Open incidents for Storage and Schema area metrics are displayed. The container name is part of the incident message.

**Parent topic:** Administering CDB Storage and Schema Objects with Cloud Control

### 42.2 Administering PDBs with Cloud Control

You can use Oracle Enterprise Manager Cloud Control to switch between PDBs and alter the open mode of a PDB.

- Switching Between PDBs  
	If you are performing a task such as granting user privileges or performance reporting, and you need to perform the same task on another PDB, then you can use Oracle Enterprise Manager Cloud Control to switch to another PDB.
- Altering the Open Mode of a PDB  
	You can change the open mode of a PDB with Oracle Enterprise Manager Cloud Control.

**Parent topic:** Administering CDBs and PDBs with Cloud Control

#### 42.2.1 Switching Between PDBs

If you are performing a task such as granting user privileges or performance reporting, and you need to perform the same task on another PDB, then you can use Oracle Enterprise Manager Cloud Control to switch to another PDB.

To switch between PDBs while staying on the same feature page:

1. From the current PDB, select any PDB scope page (such as, Manage Advanced Queues).
	In the upper-left corner of the window, the name of the PDB will update to display a context switcher as a drop-down menu.
2. Click the context switcher to display the drop-down menu. This menu shows the PDBs most recently used.
	Select a PDB from this list.
3. The page will update to show the System Queues.
4. Click the context switcher to display the drop-down menu. If the menu does not show the PDBs you want, then select All Containers.
5. A Switch Container window will pop up to display all available PDBs for the monitored target.
	Select a PDB from this list and click OK.
6. The page will update to show data for the selected PDB.

**Parent topic:** Administering PDBs with Cloud Control

#### 42.2.2 Altering the Open Mode of a PDB

You can change the open mode of a PDB with Oracle Enterprise Manager Cloud Control.

To change the open mode of a single-instance PDB to Open or Close:

1. From the Oracle Database menu, select Control, then select Open/Close Pluggable Database.
2. From the Open/Close Pluggable Database page, select a PDB from the list.
3. Click on Open, Open Read Only, or Close.
4. In the Confirmation dialog window, click Yes to complete the change. A Processing dialog window appears to show you the progress of your choice.
5. Once the open mode change completes, the Open/Close PDB page will update to show the new open mode of the PDB.

To change the open mode of a PDB in a Cluster/RAC to Open or Close:

1. From the Oracle Database menu, select Control, then Open/Close Pluggable Database.
2. From the Open/Close Pluggable Database page, select a PDB from the list. The RAC instances are shown along with the PDB's current open mode on those instances.
3. Once you select a PDB, a panel appears below the list to show the open mode of the PDBs on the different RAC instances. The open and close options apply to the PDBs on the RAC instance's panel. You can open or close a PDB on any number of available RAC instances.
4. In the Confirmation dialog window, click Yes to complete the change. A Processing dialog window appears to show you the progress of your choice.
5. Once the open mode change completes, the Open/Close Pluggable Database page will update to show the new open mode of the PDB.

**Parent topic:** Administering PDBs with Cloud Control
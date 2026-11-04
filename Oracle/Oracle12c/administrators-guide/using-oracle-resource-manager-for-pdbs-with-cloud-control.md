---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: E85760-09
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/admin/using-oracle-resource-manager-for-pdbs-with-cloud-control.html
tags:
  - oracle
  - 12c
  - administrators-guide
---

You can use Oracle Resource Manage for a multitenant environment with Oracle Enterprise Manager Cloud Control.

See Also:

- " [About Using Oracle Resource Manager with CDBs and PDBs](using-oracle-resource-manager-for-pdbs-with-sql-plus.md) "
- " [Prerequisites for Using Resource Manager with a CDB](using-oracle-resource-manager-for-pdbs-with-sql-plus.md) "

**Parent topic:** [Managing a Multitenant Environment](managing-a-multitenant-environment.md)

### 47.1 About CDB Resource Manager and Cloud Control

You can use Enterprise Manager to manage multitenant container database (CDB) resource plans. Resource Manager provides CDB and pluggable database (PDB) resource management. At the CDB level, Enterprise Manager provides new resource plan creation and resource plan monitoring functionality.

The CDB Resource Plans page lists all CDB plans available in the system. Each row displays information about the specific CDB plan while the PDB Resource Plans page displays the PDB plans, one row for each PDB plan. Each plan is selectable and you can click on the plan name to drill down for more detailed information. You can edit or view a selected plan or you can create a new plan.

**Parent topic:** Using Oracle Resource Manager for PDBs with Cloud Control

### 47.2 Creating a CDB Resource Plan with Cloud Control

You can create a CDB resource plan with Oracle Enterprise Manager Cloud Control that allocates shares of system resources to all PDBs within a CDB.

To create a CDB resource plan, follow these steps:

1. From the Administration menu, choose Resource Manager.
	Enterprise Manager displays the Resource Manager home page.
2. On the Resource Manager home page, click the Resource Plan link.
	If the current target is a CDB, then a CDB top level Resource Plans page displays. The page lists CDB plans that are available in the system, one row per CDB plan. Each row displays information about the CDB plan, such as Plan Name and whether it is active. You can drill-down for more information about each plan.
3. Click Create to create a new resource plan.
	Enterprise Manager displays the CDB Resource Plan detail page. The page contains CDB Resource plan settings on the top, such as the Plan Name. You can add or remove PDBs to this plan by clicking the Add/Remove button. A select PDB page appears that allows you to choose PDBs. When you add a PDB, each PDB displays the Share Allocation and Utilization Limit.
4. Fill in the required information and click Apply.
	A new resource plan is created and all fields are updated.

**Parent topic:** Using Oracle Resource Manager for PDBs with Cloud Control

### 47.3 Creating a PDB Resource Plan with Cloud Control

You can create a PDB resource plan with Oracle Enterprise Manager Cloud Control.

To create a PDB resource plan, follow these steps:

1. From the Administration menu, choose Resource Manager.
	Enterprise Manager displays the Resource Manager home page.
2. Click on the Plans link under the Pluggable Database section.
	If you are currently connected to a PDB or Single Instance database target, you see the PDB Resource Plan page. This page displays a list of resource plans that are available in the database. Each row displays information about the plan, such as plan name and whether the plan is active. You can drill down for more information about each plan.
	The Advanced radio button is only shown when an existing advanced plan is displayed. When creating or editing a new plan, Advanced mode is not supported.
3. Click Create to create a new resource plan.
	Enterprise Manager displays the PDB Resource Plan detail page. The page contains PDB Resource plan settings. The page lists consumer groups that do not have default settings. Click the Add/Remove button to add or remove consumer groups and set the value.
4. Enter the required information in all fields and click Apply.

**Parent topic:** Using Oracle Resource Manager for PDBs with Cloud Control
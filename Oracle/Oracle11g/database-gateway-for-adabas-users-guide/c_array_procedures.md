---
title: Setting the Array Handling Policy
book: "Database Gateway for Adabas User's Guide"
doc_id: E12074-01
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/gateways.112/e12074/c_array_procedures.htm
tags:
  - oracle
  - 11g
  - database-gateway-for-adabas-users-guide
---

## 4 Setting the Array Handling Policy

This chapter contains the following sections:

- Setting the Default Behavior for Array Handling
- Modifying the Array Handling Policy for a Specific Table

## Setting the Default Behavior for Array Handling

You can define the default behavior for array handling at the data source level when configuring the data source properties.

See [Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/gateways.112/e12077/toc.htm) or [Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12076/toc.htm) for details on configuring data source properties.

Perform the following steps in Oracle Studio for IMS, VSAM, and Adabas Gateways to set the default array handling behavior:

1. In the Design Perspective Configuration Viewexpand the Machine folder and then expand the machine with the data source where you want to set the array handling behavior.
2. Expand the binding with the data source you are working with.
3. Expand the Data Sources folder and then right-click the data source and select Edit Data Source.
	The Configuration Properties screen opens.
4. On the Advanced tab, in the Virtual View Policy section, configure how arrays will be handled by selecting the relevant check boxes. The following options are available:
	- Generate sequential view: Select this option if you want to map a non-relation file to a single table.
		- Generate virtual views: Select this option if you want to have an individual table created for every array in the non-relational file.
		- Include row number column: Select this option if you want to include a column that specifies the row number in the virtual or sequential view.
		- Inherit all parent columns: Select this option if you want the virtual views to include all the columns of the parent record.
	Figure 4-1 Setting the Default Behavior for Handling Arrays
	![Default behavior for handling arrays](https://docs.oracle.com/cd/E11882_01/gateways.112/e12074/img/datasource_editor.gif "Default behavior for handling arrays")  
	[Description of "Figure 4-1 Setting the Default Behavior for Handling Arrays"](https://docs.oracle.com/cd/E11882_01/gateways.112/e12074/img_text/datasource_editor.htm)
5. Save your settings.

## Modifying the Array Handling Policy for a Specific Table

You can also change the array handling policy on the table level. Perform the following steps to modify the policy for a specific table:

1. In the Design Perspective Configuration Viewexpand the Machine folder and then expand the machine with the data source where you want to set the array handling behavior.
2. Expand the binding with the data source you are working with.
3. Expand the data sources folder, then right-click the data source and select Edit metadata.
	The Metadata view opens on the node of the respective data source.
4. Expand the data source node, and then expand the Tables node.
5. Double-click the table whose array handling settings you want to modify.
	The table editor opens.
6. On the Modeling tab, configure how arrays will be handled by selecting the relevant check boxes. The following options are available:
	- Generate sequential view: Select this option if you want to map a non-relation file to a single table.
		- Generate virtual views: Select this option if you want to have an individual table created for every array in the non-relational file.
		- Include row number column: Select this option if you want to include a column that specifies the row number in the virtual or sequential view.
		- Inherit all parent columns: Select this option if you want the virtual views to include all the columns of the parent record.
	Figure 4-2 Modifying the Array Handling Policy on the Table Level
	![Modifying array handling on table level](https://docs.oracle.com/cd/E11882_01/gateways.112/e12074/img/table_editor.gif "Modifying array handling on table level")  
	[Description of "Figure 4-2 Modifying the Array Handling Policy on the Table Level"](https://docs.oracle.com/cd/E11882_01/gateways.112/e12074/img_text/table_editor.htm)
7. Save your settings.
	Oracle Studio for IMS, VSAM, and Adabas Gateways creates new virtual views.
---
title: Preparing to Upgrade Oracle Database
book: Upgrade Guide
doc_id: E23633-11
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23633/preup.htm
tags:
  - oracle
  - 11g
  - upgrade-guide
---

## 2 Preparing to Upgrade Oracle Database

The process of upgrading Oracle Database includes understanding system considerations and requirements and troubleshooting various issues before actually performing the upgrade steps. Before you upgrade Oracle Database, you must become familiar with the new features and behavior changes. In preparation for upgrading you install the new Oracle software. The new Oracle software for this release provides the latest Pre-Upgrade Information Tool to help you understand requirements and complete pre-upgrade tasks.

This chapter contains the following topics:

## The Main Steps for Preparing to Upgrade Oracle Database

In preparation for upgrading Oracle Database, you review the new features, determine the best upgrade path and method. Oracle recommends that you test the upgrade process and prepare a backup strategy.

Complete the following tasks to prepare to upgrade:

- Become Familiar with New Oracle Database Features for Upgrading
- Determine the Upgrade Path for Upgrading Oracle Database
- Choose an Upgrade Method for Upgrading Oracle Database
- Choose a Location for the New Oracle Home for Upgrading Oracle Database
- Develop a Testing Plan to Upgrade Oracle Database
- Prepare a Backup Strategy for Upgrading Oracle Database

### Become Familiar with New Oracle Database Features for Upgrading

Before you plan the upgrade process, become familiar with the features of the new Oracle Database 11g release. [Oracle Database New Features Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41360/toc.htm) is a good starting point for learning the differences between Oracle Database releases. Also, check specific guides in the Oracle Database 11g documentation library to find information about new features for a certain component. For example, see [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for changes in Oracle Real Application Clusters.

Note:

- Oracle Database training classes are an excellent way to learn how to take full advantage of the features and functions available with Oracle Database. More information can be found at `http://education.oracle.com/`
- My Oracle Support provides detailed notes on how to obtain the latest patches, plus tools for lifecycle management and automated patching. For information about getting started with My Oracle Support, go to `http://www.oracle.com/us/support/software/premier/my-oracle-support-068523.html`

See Also:

My Oracle Support Note ID 854428.1, "Patch Set Updates for Oracle Products" at `https://support.oracle.com`

### Determine the Upgrade Path for Upgrading Oracle Database

The path that you must take to upgrade to the new Oracle Database 11g release depends on the release number of your current database. It might not be possible to directly upgrade from your current release of Oracle Database to the latest release. Depending on your current release, you might be required to upgrade through one or more intermediate releases to upgrade to the new Oracle Database 11g release.

For example, if the current database is running release 9i, then follow these steps:

1. Upgrade release 9.0.1.4 to release 10.2.0.4 using the instructions in Oracle Database Upgrade Guide Release 2 (10.2).
2. Upgrade release 10.2.0.4 to the new Oracle Database 11g release using the instructions in this guide.

Table 2-1 contains the required upgrade path for each release of Oracle Database. Use the upgrade path and the specified documentation to upgrade your database.

Table 2-1 Supported Upgrade Paths for Upgrading Oracle Database

| Current Release | Upgrade Path |
| --- | --- |
| 9.0.1.3 (or earlier) | Direct upgrade is not supported. Upgrade to an intermediate Oracle Database release before you can upgrade to the new Oracle Database 11g release, as follows:  - 9.0.1.3 (or earlier) -> 9.0.1.4 -> 10.2.0.4 -> 11.2  When upgrading to an intermediate Oracle Database release, follow the instructions in the intermediate release's documentation. Then, upgrade the intermediate release database to the new Oracle Database 11g release using the instructions in [Chapter 3, "Upgrading to the New Release of Oracle Database"](upgrade.md). |
| 9.2.0.8  10.1.0.5  10.2.0.2  11.1.0.6 | Direct upgrade to the new Oracle Database 11g release is supported from 9.2.0.8 or higher, 10.1.0.5 or higher, 10.2.0.2 or higher, and 11.1.0.6 or higher. Note that Oracle Clusterware release 10.2.0.n must be at release 10.2.0.3 (or higher), before you attempt to upgrade it to Oracle Clusterware 11g. See ["About Upgrading an Oracle Real Application Clusters (Oracle RAC) Database"](upgrade.md).  For release 9.2.0.3, you must first upgrade to an intermediate Oracle Database release, as follows:  9.2.0.3 (or earlier) -> 9.2.0.8 -> 11.2  To upgrade to the new Oracle Database 11g release, follow the instructions in [Chapter 3, "Upgrading to the New Release of Oracle Database"](upgrade.md). |

### Choose an Upgrade Method for Upgrading Oracle Database

The upgrade methods you can use to upgrade your database to the new Oracle Database 11g release are:

- Database Upgrade Assistant (DBUA)
- Manual Upgrade
- Oracle Data Pump Export and Import and Oracle Database Upgrade

#### Database Upgrade Assistant (DBUA)

Database Upgrade Assistant (DBUA) interactively steps you through the upgrade process and configures the database for the new Oracle Database 11g release. DBUA automates the upgrade process by performing all of the tasks normally performed manually. DBUA makes appropriate recommendations for configuration options such as tablespaces and redo logs. You can then act on these recommendations.

DBUA provides support for Oracle Real Application Clusters (Oracle RAC). In an Oracle RAC environment, DBUA upgrades all the database and configuration files on all nodes in the cluster.

#### Manual Upgrade

A manual upgrade consists of running SQL scripts and utilities from a command line to upgrade a database to the new Oracle Database 11g release.

While a manual upgrade gives you finer control over the upgrade process, it is more susceptible to error if any of the upgrade or pre-upgrade steps are either not followed or are performed out of order.

##### Before the Upgrade

The following list provides a high-level summary of the manual upgrade steps:

- Analyze the database using the Pre-Upgrade Information Tool. The Pre-Upgrade Information Tool is a SQL script that is supplied with the new Oracle Database 11g release, and DBUA uses this script as part of its upgrade process. Run the script on the database you are upgrading.
	The Pre-Upgrade Information Tool displays warnings about possible upgrade issues with the database. It also displays information about required initialization parameters for the new Oracle Database 11g release.
- Prepare the new Oracle home.
	See Also:
	"Choose a Location for the New Oracle Home for Upgrading Oracle Database" for more information
- Perform a backup of the database.

Depending on the release of the database being upgraded, you might be required to perform additional pre-upgrade steps:

- Adjust the parameter file for the upgrade.
- Remove obsolete initialization parameters.
- Adjust initialization parameters that might cause upgrade problems.
- Set the `COMPATIBLE` parameter if not already explicitly set.
	See Also:
	["Setting the COMPATIBLE Initialization Parameter"](afterup.md) for information about setting the `COMPATIBLE` initialization parameter

##### After the Upgrade

Review the upgrade spool log file and use the Post-Upgrade Status Tool. The Post-Upgrade Status Tool is a SQL script that ships with the new Oracle Database 11g release. You run the Post-Upgrade Status Tool in the environment of the new release. The Post-Upgrade Status Tool can be run any time after upgrading the database.

See Also:

["Upgrading Oracle Database Manually"](upgrade.md)

#### Oracle Data Pump Export and Import and Oracle Database Upgrade

Unlike DBUA or a manual upgrade, the Oracle Data Pump Export and Import utilities physically copy data from your current database to a new database. When upgrading from Oracle Database 10g Release 1 (10.1) or higher, Data Pump Export and Import are recommended for higher performance and to ensure support for new datatypes.

The Export utility of the current database copies specified parts of the database into an export dump file. Then, the Import utility of the new Oracle Database 11g release loads the exported data into a new database. However, the new Oracle Database 11g database must currently exist before it can be loaded from the export dump file.

When importing data from an earlier release, the Import utility of the new Oracle Database 11g release makes appropriate changes to data definitions as it reads export dump files from earlier releases.

The following sections highlight aspects of Export/Import that might help you to decide whether to use Export/Import to upgrade your database.

Note:

- If your database is earlier than Oracle Database release 10.1, then you can use the original Export and Import utilities to perform a full or partial export from your database, followed by a full or partial import into a new Oracle Database 11g database. Export/Import can copy a subset of the data in a database, leaving the original database unchanged.
- The original Export utility is no longer being updated to support new datatypes.

##### Export/Import Effects on Upgraded Databases

The Export/Import upgrade method does not change the current database, which enables the database to remain available throughout the upgrade process. However, if a consistent snapshot of the database is required (for data integrity or other purposes), then the database must run in restricted mode or must otherwise be protected from changes during the export procedure. Because the current database can remain available, you can, for example, keep an existing production database running while the new Oracle Database 11g database is being built at the same time by Export/Import. During the upgrade, to maintain complete database consistency, changes to the data in the database cannot be permitted without the same changes to the data in the new Oracle Database 11g database.

Most importantly, the Export/Import operation results in a completely new database. Although the current database ultimately contains a copy of the specified data, the upgraded database might perform differently from the original database. For example, although Export/Import creates an identical copy of the database, other factors, such as disk placement of data and unset tuning parameters, might cause unexpected performance problems.

##### Export/Import Benefits

Upgrading using Data Pump Export/Import:

- Defragments the data. You can compress the imported data to improve performance.
- Restructures the database. You can create new tablespaces or modify existing tables, tablespaces, or partitions to be populated by imported data.
- Facilitates side-by-side testing of the old and new versions of Oracle Database because an entirely new database is created.
- Enables the copying of specified database objects or users. Importing only the objects, users, and other items you need is useful for establishing a test environment for the new software on only a subset of the production data. Data Pump Export / Import provides flexible data subsetting capabilities.
- Serves as a backup archive - you can use a full database export as an archive of the current database.
- Enables the upgraded database to be established on an operating system or hardware platform that is different from that which is supporting the database being upgraded.Network-based Data Pump Import allows the new Oracle database to be directly loaded across the network from the old database being upgraded. Thus, no intervening dump files are required.

##### Time Requirements for Export/Import

Upgrading an entire database by using Export/Import can take a long time, especially compared to using DBUA or performing a manual upgrade. Therefore, you might be required to schedule the upgrade during non-peak hours or make provisions for propagating to the new database any changes that are made to the current database during the upgrade.

See Also:

[Chapter 7, "Moving Data Using Oracle Data Pump"](expimp.md)

### Choose a Location for the New Oracle Home for Upgrading Oracle Database

You must choose a location for Oracle home on the new Oracle Database 11g release that is separate from the Oracle home of your current release. You cannot install the new software into the same location for Oracle home as your current release, unless you are installing an Oracle Database 11g patchset release. For a patchset release, you can use the same Oracle Database 11g Oracle home.

Using separate installation directories enables you to keep your existing software installed along with the new software. This method enables you to test the upgrade process on a test database before replacing your production environment entirely.

### Develop a Testing Plan to Upgrade Oracle Database

You need a series of carefully designed tests to validate all stages of the upgrade process. Executed rigorously and completed successfully, these tests ensure that the process of upgrading the production database is well understood, predictable, and successful. Perform as much testing as possible before upgrading the production database. Do not underestimate the importance of a complete and repeatable testing process.

The types of tests to perform are the same whether you use Real Application Testing features like Database Replay or SQL Performance Analyzer, or perform testing manually.

Your test plan must include these types of tests:

- Oracle Database Upgrade Testing
- Minimal Testing for Upgrading Oracle Database
- Functional Testing for Upgrading Oracle Database
- High Availability Testing for Upgrading Oracle Database
- Integration Testing for Upgrading Oracle Database
- Performance Testing for Upgrading Oracle Database
- Volume and Load Stress Testing for Upgrading Oracle Database

#### Oracle Database Upgrade Testing

Upgrade testing entails planning and testing the upgrade path from your current software to the new Oracle Database 11g release, whether you use DBUA, perform a manual upgrade, or use Export/Import or other data-copying methods. Regardless of the upgrade method you choose, you must establish, test, and validate an upgrade plan.

#### Minimal Testing for Upgrading Oracle Database

Minimal testing entails moving all or part of an application from the current database to the new database and running the application without enabling any new database features. Minimal testing might not reveal problems that would appear in an actual production environment. However, minimal testing immediately reveals any application startup or invocation problems.

#### Functional Testing for Upgrading Oracle Database

Functional testing is a set of tests in which new and existing features and functions of the system are tested after the upgrade. Functional testing includes all database, networking, and application components. The objective of functional testing is to verify that each component of the system functions as it did before upgrading and to verify that new functions are working properly.

#### High Availability Testing for Upgrading Oracle Database

High availability testing entails:

- Ensuring that Recovery Time Objective (RTO) and Recovery Point Objective (RPO) business requirements are still met by the upgraded system. For example, in an Oracle RAC environment, injecting node or instance failures during stress testing help evaluate if the Oracle RAC recovery capability has changed.
- Testing your fallback plans and procedures.
- Checking the database performance and stability, and resolving performance problems.

See Also:

The [Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/hadesign.htm#HAOVW002) and "The Upgrade Companion" Web site available in Note 785351.1 on My Oracle Support at `http://support.oracle.com/`.

#### Integration Testing for Upgrading Oracle Database

Integration testing examines the interactions among components of the system. Consider the following factors when you plan your integration testing:

- Pro\*C/C++ applications running against a new Oracle Database 11g instance should be tested to ensure that there are no problems with the new software.
- Graphical user interfaces should be tested with other components.
- Subtle changes in the new Oracle Database 11g release, such as data types, data in the data dictionary (additional rows in the data dictionary, object type changes, and so on) can have an effect all the way up to the front-end application, even if the application is not directly connected to a new Oracle Database 11g instance.
- If the connection between two components involves Oracle Net or Oracle Net Services, then those connections should also be tested and stress tested.

#### Performance Testing for Upgrading Oracle Database

Performance testing of the new database compares the performance of various SQL statements in the new database with the performance of those same statements in the current database. Before upgrading, you should understand the performance profile of the application under the current database. Specifically, you should understand the calls the application makes to the database server.

This section describes the following types of performance testing:

- Database Replay
- SQL Performance Analyzer
- SQL Plan Management

##### Database Replay

Starting with Oracle Database 11g Release 1 (11.1), you can use the new Database Replay feature to perform real-world testing of a database upgrade on your site's production workload before actually upgrading the production database. This feature captures the actual database workload on the production system and replays it on the test system. It also provides analysis and reporting to highlight potential problems—for example, errors encountered, divergence in performance, and so forth. In addition, all the regular Enterprise Manager performance monitoring and reporting tools such as Automatic Database Diagnostic Monitor, Automatic Workload Repository (AWR), and Activity Session History are available to address any problems.

Note:

You can change the stored procedure logic in the database but the stored PL/SQL procedures that implement the application logic must maintain the same interfaces as before the upgrade. If an upgrade affects the stored procedures of an application, then the workload might not be replayable. By using the Database Replay tool in this way, you have good diagnostics to see if the new application logic in the server is performing as expected after the upgrade.

See Also:

[Oracle Database Real Application Testing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41481/dbr_intro.htm#RATUG104) for complete information about how to capture and replay workloads

##### SQL Performance Analyzer

Starting with Oracle Database 11g Release 1 (11.1), you can use the SQL Performance Analyzer to forecast the impact of system changes on a SQL workload. SQL Performance Analyzer enables evaluating the impact of a change such as database upgrade by identifying the SQL statements impacted by the upgrade and measuring their performance divergence. The analysis enables you to assess the overall effect of the upgrade on SQL performance and makes it possible to avoid any negative outcome before users can be impacted.

See Also:

[Oracle Database Real Application Testing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41481/spa_intro.htm#RATUG166) for complete information and examples using the SQL Performance Analyzer to perform what-if analysis on potential database changes

##### SQL Plan Management

SQL plan management prevents performance regressions resulting from sudden changes to the execution plan of a SQL statement by providing components for capturing, selecting, and evolving SQL plan information. SQL plan management is a preventative mechanism that records and evaluates the execution plans of SQL statements over time, and builds SQL plan baselines composed of a set of existing plans known to be efficient. The SQL plan baselines are then used to preserve performance of corresponding SQL statements, regardless of changes occurring in the system.

A database upgrade that installs a new optimizer version usually results in plan changes for a small percentage of SQL statements, with most of the plan changes resulting in either no performance change or improvement. However, certain plan changes may cause performance regressions.

SQL plan management prevents performance regressions resulting from sudden changes to the execution plan of a SQL statement by providing components for capturing, selecting, and evolving SQL plan information. If you are performing a database upgrade that installs a new optimizer version, then it can result in plan changes for a small percentage of SQL statements, with most of the plan changes resulting in either no performance change or improvement. However, certain plan changes may cause performance regressions.

With SQL plan management, the optimizer automatically manages execution plans and ensures that only known or verified plans are used. When a new plan is found for a SQL statement, the plan is not used until it has been verified by the database to have comparable or better performance than the current plan. Therefore, if you seed SQL plan management with your current (pre-Oracle Database 11g) execution plan, which is to become the SQL plan baseline for each statement, then the optimizer uses these plans after the upgrade. If the Oracle Database 11g optimizer determines that a different plan is necessary, then the new plan is queued for verification and is not used until it has been confirmed to have comparable or better performance than the current plan.

There are two ways to seed or populate a SQL Management Base (SMB) with execution plans:

- Automatic capture of execution plans (available starting with Oracle Database 11g)
- Bulk load execution plans or preexisting SQL plan baselines

Bulk loading of execution plans or SQL plan baselines is especially useful when upgrading a database from a previous release to Oracle Database 11g. SQL plans that are bulk loaded are automatically accepted and added to existing or new plan histories as SQL plan baselines.

To bulk load the SQL Management Base as part of an upgrade:

- Populate the execution plans for a given SQL Tuning Set (STS), as described in "Bulk Loading a SQL Management Base with a SQL Tuning Set (STS)".
	Or
- Unpack existing SQL plan baselines from a staging table, as described in "Unpacking Existing Oracle Database SQL Plan Baselines from a Staging Table".

Bulk Loading a SQL Management Base with a SQL Tuning Set (STS)

To bulk load the SQL Management Base with an execution plan from an STS

1. In Oracle Database 10g Release 2 (10.2), create an STS that includes the execution plan for each of the SQL statements.
2. Load the STS into a staging table and export the staging table into a dump file.
3. Import the staging table from a dump file into Oracle Database 11g and unload the STS.
4. Use Oracle Enterprise Manager or `DBMS_SPM.LOAD_PLANS_FROM_SQLSET` to load the execution plans into the SQL Management Base.

Unpacking Existing Oracle Database SQL Plan Baselines from a Staging Table

Perform the steps in this procedure to test and tune all of your critical SQL queries on an Oracle Database 11g test environment and then move those exact SQL execution plans to your Oracle Database 11g production environment.

To test and tune your critical SQL queries on an Oracle Database 11g test environment

1. On the Oracle Database 11g test system, after completing all testing and tuning, use the `DBMS_SPM.LOAD_PLAN_FROM_CURSOR_CACHE` procedure or Enterprise Manager to load all of the execution plans in the cursor cache into the SQL Management Base.
2. Create a staging table using the `DBMS_SPM.CREATE_STGTAB_BASELINE` procedure.
3. Pack the SQL plan baselines you created in step 1 into the staging table using the `DBMS_SPM.PACK_STGTAB_BASELINE` function.
4. Export the staging table into a flat file using the Export command or Data Pump.
5. Transfer this flat file to the target system.
6. Import the staging table from the flat file using the Import command or Data Pump.
7. Unpack the SQL plan baselines from the staging table into the SQL Management Base on the target system using the `DBMS_SPM.UNPACK_STGTAB_BASELINE` function.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/optplanmgmt.htm#PFGRF007) for more information about using SQL Plan Management

#### Volume and Load Stress Testing for Upgrading Oracle Database

Volume and load stress testing tests the entire upgraded database under high volume and loads. Volume describes the amount of data being manipulated. Load describes the level of concurrent demand on the system. The objective of volume and load testing is to emulate how a production system might behave under various volumes and loads.

Volume and load stress testing is crucial, but is commonly overlooked. Oracle has found that customers often do not conduct any kind of volume or load stress testing. Instead, customers often rely on benchmarks that do not characterize business applications. Benchmarks of the application should be conducted to uncover problems relating to functions, performance, and integration, but they cannot replace volume and load stress testing.

Load testing involves running an application load against the new release of the database to ensure that the application does not encounter problems such as new errors or performance issues under load conditions likely to be encountered in production. Many times, problems manifest under certain load conditions and are normally not seen in functional testing. The Database Replay feature is ideal for such load testing as it enables capturing the system workload from a production environment and replay it in identical fashion on the test system.

### Prepare a Backup Strategy for Upgrading Oracle Database

The ultimate success of your upgrade depends heavily on the design and execution of an appropriate backup strategy.

To develop a backup strategy, consider the following questions:

- How long can the production database remain inoperable before business consequences become intolerable?
- What backup strategy is necessary to meet your availability requirements?
- Are backups archived in a safe, offsite location?
- How quickly can backups be restored (including backups in offsite storage)?
- Have recovery procedures been tested successfully?

Your backup strategy should answer all of these questions and include procedures for successfully backing up and recovering your database.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) for information on database backups

## Testing the Upgrade Process for Oracle Database

Create a test environment that does not interfere with the current production database.

Your test environment depends on the upgrade method you have chosen:

- If you plan to use DBUA or perform a manual upgrade, then create a test version (typically a subset) of the current production database to test the upgrade.
- If you plan to use Export/Import, then export and import small test pieces of the current production database.

Practice upgrading the database using the test environment. The best upgrade test, if possible for you to create, is performed on an exact copy of the database to be upgraded, rather than on a downsized copy or test data. If for some reason an exact copy is impractical, then carefully chose a representative subset of your data to move over to your test environment and test the upgrade on that data.

Ensure that you upgrade any OCI and precompiler applications that you plan to use with your new Oracle database. Then, you can test these applications on a sample database before upgrading your current production database.

See Also:

["Upgrading Precompiler and OCI Applications"](app.md) for more information

## Testing the Upgraded Test Oracle Database

Perform the planned tests on the current database and on the test database that you upgraded to the new Oracle Database 11g release. Compare the results, noting anomalies. Repeat the test upgrade as many times as necessary.

Test the newly upgraded test database with existing applications to verify that they operate properly with a new Oracle database. You also might test enhanced functions by adding available Oracle Database features. However, first ensure that the applications operate in the same manner as they did in the current database.

See Also:

[Chapter 5, "Upgrading Applications After Upgrading Oracle Database"](app.md) for more information on using applications with Oracle Database
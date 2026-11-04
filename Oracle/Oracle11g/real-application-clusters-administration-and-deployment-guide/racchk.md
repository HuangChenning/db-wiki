---
title: Oracle RAC Configuration Audit Tool
book: Real Application Clusters Administration and Deployment Guide
doc_id: E41960-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41960/racchk.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-administration-and-deployment-guide
---

## D Oracle RAC Configuration Audit Tool

This appendix includes the information required to run and maintain the Oracle Real Application Clusters (Oracle RAC) Configuration Audit Tool (RACcheck). The tool is designed to audit various important configuration settings within an Oracle RAC system.

Note:

if you have not upgraded to Oracle Database 11g release 2 (11.2.0.4), which includes RACcheck, or to get the latest version of RACcheck (to which Oracle adds checks every three months), then you can download RACcheck from the following URL:

`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1268927.1`

This appendix includes the following topics:

## RACcheck Features

Use RACcheck to audit configuration settings within the following categories:

- Operating system kernel parameters
- Operating system packages and other operating system configuration settings important to Oracle RAC
- Oracle Grid Infrastructure
- Oracle Automatic Storage Management (Oracle ASM)
- Oracle Database
- Database parameters and other database configuration settings important to Oracle RAC
- Upgrade readiness assessment to Oracle Database 11g release 2 (11.2)

You can use RACcheck with Oracle RAC database servers, Oracle RAC databases (10g release 2 (10.2), 11g release 1 (11.1), and 11g release 2 (11.2)), Oracle Grid Infrastructure, hardware, and operating system and Oracle RAC software. You can also use RACcheck with nonclustered Oracle Databases (10g release 2 (10.2), 11g release 1 (11.1), and 11g release 2 (11.2)), Oracle Restart systems, and Oracle Real Application Clusters One Node configurations.

You can use RACcheck on the following platforms:

- Intel Linux <sup>Foot 1</sup> (Enterprise Linux, RedHat and SuSE 9,10, 11)
- Oracle Solaris SPARC (Solaris 10 and 11)
- Oracle Solaris x86-64 (Solaris 10 and 11)
- IBM AIX <sup>Foot 2</sup>
- HP-UX <sup>Footref 2</sup>

Other RACcheck features include:

- RACcheck is nonintrusive and does not change anything in the environment, except as follows:
	- SSH user equivalence for the Oracle Database software owner is assumed to be configured among all the database servers being audited so that RACcheck can run commands on remote database server nodes. If RACcheck determines that SSH user equivalence is not configured, then the tool gives you the option to set up user equivalence either temporarily or permanently. If you choose to set up SSH user equivalence temporarily, then, at the end of the session, RACcheck removes the keys to restore the system to its original SSH user equivalence state. If you want to configure SSH user equivalence outside of RACcheck (if it is not already configured), then consult My Oracle Support note 372795.1 at the following URL:
		`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=372795.1`
		Note:
		SSH user equivalence is always required for the Oracle Database software installation owner, but is not required for Oracle Grid Infrastructure configurations.
		- RACcheck creates a number of small output files into which the data necessary to perform the assessment is collected.
		- RACcheck creates and executes some scripts dynamically in order to accomplish some of the data collection.
		- RACcheck deletes any temporary files that are created and not needed as part of the collection.
- RACcheck interrogates the system to determine the status of the Oracle stack components (specifically, Oracle Grid Infrastructure, Oracle Database, Oracle RAC, and so on) and whether they are installed and whether they are running. Depending upon the status of each component, RACcheck runs the appropriate collections and audit checks.
	See Also:
	Troubleshooting if, because of local environmental configuration, RACcheck is unable to properly determine the necessary environmental information
- RACcheck automatically runs a process in the background to monitor command execution progress. If, for any reason, one of the commands run by RACcheck should hang or take longer to run than anticipated, then this monitor process stops the command after a configurable amount of time, so that RACcheck can continue to run. If that happens, then RACcheck skips the collection or command that was hung and a notation is made in the log.
	See Also:
	"Runtime Command Timeouts" to adjust the `RAT_TIMEOUT` and `RAT_ROOT_TIMEOUT` parameters if the default timeout duration is too short
- If the RACcheck driver files are older than 90 days, then the driver files are considered to be stale and you will be notified of a stale driver file.
- When RACcheck completes the collection and analysis, it produces a detailed HTML formatted report that contains benefit, impact, risk, and action and repair information. The report may also reference publicly available documents with additional information about the problem and its resolution. RACcheck also produces a compressed output file. This output file can be provided to My Oracle Support for further analysis, if necessary.
- The results of the audit checks can be optionally uploaded into database tables for reporting purposes.
- In some cases, you may want to stage RACcheck on a shared file system, so that various systems can access it, while still being maintained in a single location, rather than copying to each cluster on which it may be used. The default behavior of RACcheck is to create a subdirectory and its output files in the location where the it is staged. If that staging area is a read-only file system or if you would like the output to be created elsewhere, then there is an environment variable that you can use for that purpose. You can configure the `RAT_OUTPUT` parameter to any valid writable location.

## RACcheck Usage

When using RACcheck, consider the following:

- Run RACcheck on Oracle Database servers as the Oracle Database software owner (`oracle`).
- RACcheck includes a daemon that enables RACcheck to run noninteractively (in batch or silent mode) at regular intervals.
	See Also:
	"Running RACcheck Using the RACcheck Daemon"
- Oracle recommends that you install and run RACcheck from a local file system on a single database server to provide the best performance.
- To maximize its usefulness, run RACcheck when Oracle Grid Infrastructure and at least one database are up and running.
- Oracle recommends that you run RACcheck during times of least load on the system.
- To avoid possible problems running RACcheck from terminal sessions on a network attached workstation or laptop, consider running the tool using VNC so that, if there is a network interruption, then the tool will continue to run until it is finished.
- If RACcheck fails for some reason, then you can run it again from the beginning. RACcheck does not resume from the point of failure.
- You can run RACcheck on all nodes, simultaneously. To take advantage of the `root` -specific checks while still running the tool in parallel, use the `EXPECT` utility installed on the system or configure `sudo` for RACcheck to use.
	To configure `sudo`, use the `visudo` command to add the following line to the `sudoers` file on each of the cluster nodes, replacing `owner` with the user that installed the database software:
	```
	owner ALL=(root)  NOPASSWD:/tmp/root_raccheck.sh
	```
- Ensure that permissions for RACcheck are `755` (`-rwxr-xr-x`). If the permissions are not set appropriately, then run the following command:
	```
	$ chmod 755 raccheck
	```

This section includes the following topics:

- When to Use RACcheck
- Options to Use with RACcheck
- Guidelines for Using RACcheck
- How RACcheck Handles Passwords

When to Use RACcheck

You can use RACcheck at any time but Oracle recommends that you use RACcheck:

- After initially deploying Oracle RAC
- Before and after any planned system maintenance
- At least once every 90 days

Options to Use with RACcheck

Table D-1 lists and describes options you can use with RACcheck.

Table D-1 RACcheck Options

| Option | Description |
| --- | --- |
| ``` -a ``` | Specify this option to perform both best practice and recommended patch checks. This is the default method in which RACcheck runs. |
| ``` -b ``` | Specify this option to run a best practice check, only. |
| ``` -p ``` | Specify this option to run a recommended patch check, only. |
| ``` -v ``` | Specify this option to display the version of RACcheck currently in use. |
| ``` -m ``` | Specify this option to exclude checks for maximum availability architecture (MAA) scorecard.  The MAA scorecard is the findings related to a set of maximum availability architecture best practices and shows how prepared your system is for various types of failures that can occur in an Oracle RAC environment.  RACcheck shows the MAA scorecard, because Oracle considers MAA to be an important concept and set of features. However, it is most helpful when you have implemented Oracle Data Guard standby databases. |
| ``` -u ``` | Use this option to run RACcheck to check pre-upgrade or post-upgrade best practices. You must use `-o pre` or `-o post` with the `-u` option. For example:  ``` $ raccheck -u -o pre ``` |
| ``` -o ``` | Use this option to add an argument to an option. Arguments include:  - `verbose`: If you specify this argument, then RACcheck prints checks that pass. The default behavior is that RACcheck only prints checks that fail, issue warnings, or contain other information. - `pre`: Specify this argument when you want RACcheck to check pre-upgrade best practices (to be used with the `-u` option). - `post`: Specify this argument when you want RACcheck to check post-upgrade best practices (to be used with the `-u` option). |
| ``` -f ``` | Use this option to perform checks offline on data already collected from the system. |
| ``` -clusternodes ``` | Use this option to enter a comma-delimited list of node names on which to run RACcheck.  RACcheck requires this option only when you want to run the tool on subset of cluster nodes, or when RACcheck fails to retrieve cluster node information from the environment using `olsnodes`. |
| ``` -localonly ``` | Use this option to run RACcheck only on the local node. |
| ``` -nopass ``` | Use this option to omit checks from the HTML report that have passed. |
| ``` -diff report_1 report_2  [-outfile output_HTML] ``` | Use this option along with two RACcheck reports, in the form of a directory name, a zip file, or an HTML report, to compare them to each other. Optionally, you can use the `-outfile` option to direct the output of the comparison to HTML.  Note: To limit security vulnerabilities, Oracle recommends that you set the permissions of the output directory as restrictive as possible. The output directory can contain sensitive configuration information and, when no other mechanism is available, temporary data collection files.  See Also: "Comparing Reports with RACcheck" for more information |
| ``` -daemon ``` | Use this option to run RACcheck commands only if the RACcheck daemon is running. |
| ``` -nodaemon ``` | Use this option if you do not want to use the RACcheck daemon to run the command. |
| ``` -d command ``` | Use this option with commands to control the RACcheck daemon. Commands include:  - `start`: Starts the RACcheck daemon - `stop`: Stops the RACcheck daemon - `status`: Obtains the current status of the RACcheck daemon - `nextautorun`: When the RACcheck daemon is running, use this command to obtain the time of the next scheduled run of RACcheck, according to the value of the `AUTORUN_INTERVAL` configuration parameter, as described in "Running RACcheck Using the RACcheck Daemon". |
| ``` -set "parameter_1=value_1 ;parameter_2=value_2..." ``` | Use this option to set the RACcheck configuration parameters listed in "Running RACcheck Using the RACcheck Daemon". |
| ``` -get parameter \| all ``` | Specify this option to obtain the value of a specific RACcheck configuration parameter, or the value of all RACcheck configuration parameters. |
| ``` -profile profile_name ``` | Use this option to configure RACcheck to run a specific profile. Supported profiles include:  - `asm`: This profile checks Oracle ASM configuration - `clusterware`: This profile checks Oracle Clusterware (part of Oracle Grid Infrastructure) configuration - `dba`: This profile checks the database administrator configuration - `sysadmin`: This profile checks the system administrator configuration |
| ``` -h ``` | Use this option to display RACcheck usage |

Guidelines for Using RACcheck

If the `oracle` user exists on the system and all the Oracle components are installed or running (including Oracle Clusterware, Oracle Database, and Oracle ASM), then Oracle recommends that you run RACcheck as the `oracle` (or Oracle Database software installation owner) user. RACcheck does perform some audit checks that require root privileges, in which case, if `sudo` is not configured or the `root` password is not available, then you can configure RACcheck to skip these audit checks by selecting option `3` on the `root` password menu.

RACcheck can run as `root` only if you specify the `sysadmin` profile using the `raccheck -profile sysadmin` command. In this case, RACcheck skips all database-related best practices but you must set up SSH user equivalence for the `root` user among cluster nodes, so RACcheck will not prompt you for the `root` password.

Note:

Typically, when you run RACcheck as `oracle`, operating system authentication is already set up for the Oracle Database software owner and RACcheck will not require the database login credentials.

See Also:

- For instructions about configuring SSH user equivalence, go to the following URL:
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=372795.1`
- "Database Login Problems" if you want to run RACcheck as another user, and additional information on how to verify database authentication before running the tool

How RACcheck Handles Passwords

RACcheck does not store or save any passwords. The handling of `root` passwords depends on whether the `expect` utility is installed.

If the `expect` utility is not installed (which is the default for all platforms, except Oracle Enterprise Linux 5), then the `root` password prompts are deferred and you must closely monitor RACcheck as it runs and enter the passwords, as prompted, once for each node of the cluster. Otherwise, RACcheck uses the `expect` utility for interactive password automation. You can install the `expect` utility on other Linux distributions in order to automate interactive password handling.

When RACcheck finds the `expect` utility, the tool gathers the `root` passwords at the beginning of the process, and the `expect` utility will supply them, when needed, at the `root` password prompts for each node, so that RACcheck can continue without further input from you.

RACcheck inquires if the `root` password is the same for all database servers of the cluster. If you respond affirmatively (which is the default), then you will be prompted for the `root` password once and it will be validated and subsequently used for all nodes in the cluster. If you respond negatively (that the `root` password is not the same for all nodes in the cluster), then RACcheck will prompt for and validate the `root` password for each individual node in the cluster.

Additionally, when RACcheck finds the `expect` utility, when validating the `root` passwords, you have three opportunities to type the correct password. If you fail to enter the correct password after three attempts, then RACcheck proceeds to the next node and displays a message stating that the password is still incorrect and that the checks dependent upon data collected from that node will be skipped. At this point, you can either cancel running RACcheck and obtain the correct `root` password, or continue with the understanding that important data may be missing from the report.

When RACcheck uses the `expect` utility, it is possible that, between the time that the `root` passwords are entered and validated and nodes for those passwords are reached, that the passwords could have been changed. In that case, RACcheck displays a message stating that the password must have been changed and that the collections for that node will be skipped, which means the checks for that node will also be skipped. You can either allow RACcheck to continue to completion knowing that data and checks will be skipped or cancel running RACcheck and resolve the problem.

If RACcheck skips any checks for any reason, then the tool reports in the log any checks that were skipped and on which nodes, when it finishes running.

## Using RACcheck

You can run RACcheck interactively or silently, or you can run RACcheck automatically at specified intervals. To run RACcheck interactively, run the following command:

```
$ raccheck
```

RACcheck prompts you through the auditing process.

Note:

The time it takes RACcheck to run varies based on factors such as the number of nodes in a cluster, CPU load, and network latency. Typically, the entire process should only take five minutes, or so, for each node. This is just a general guideline but if it takes substantially more time than that, then there may be some other problem that should be investigated.

This section includes the following topics:

- Running RACcheck in Silent Mode without the RACcheck Daemon
- Running RACcheck Using the RACcheck Daemon
- Comparing Reports with RACcheck
- Running RACcheck to Determine Upgrade Readiness
- Maintaining the Output File
- Multiple Database Support
- Uploading RACcheck Results and Patches to a Database for Reporting
- Excluding Audit Checks

Running RACcheck in Silent Mode without the RACcheck Daemon

To run RACcheck in silent mode:

1. You must first configure SSH user equivalence. For instructions about configuring SSH user equivalence, go to the following URL:
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=372795.1`
	Note:
	SSH user equivalence is only necessary if your system is running Oracle Grid Infrastructure to support a cluster. This is not required for nonclustered databases or Oracle Restart configurations.
2. RACcheck requires `root` access to run the `root` -specific checks. To facilitate these checks in silent mode, you must configure passwordless `sudo` and use the `-s` option to run RACcheck.
	Note:
	If `sudo` is not allowed within your environment, you can skip this step. In this case, you can still run RACcheck silently without the root-specific checks using the `-S` option. Eliminating the root-specific checks limits the capabilities of RACcheck and Oracle does not recommend this method of running RACcheck.
3. To run RACcheck silently, you must specify one of the following arguments, depending on your configuration:
	- `-s`: Use this option to run RACcheck unattended when the `oracle` user can `sudo` to `root` without a password
		- `-S`: Use this option to run RACcheck unattended without the `root` password and make no `root` -privileged collections or audits
	Note:
	Oracle recommends that you implement passwordless `sudo` to `root` for `/tmp/root_raccheck.sh` for full functionality of RACcheck, as described in "RACcheck Usage".
	RACcheck runs in silent mode using the information it gathers from Oracle Clusterware. When RACcheck runs in silent mode, it performs data collection and audit checks on all databases running on the local node that are defined as Oracle Clusterware resources.

Running RACcheck Using the RACcheck Daemon

To use the RACcheck daemon, you must first configure the daemon parameters by running the `raccheck -set` `parameter` `=` `value` command. You can set the following configuration parameters:

- `AUTORUN_INTERVAL`: This parameter defines the time interval at which RACcheck runs, specified in days or hours (`d | h`). For example:
	```
	$ raccheck -set AUTORUN_INTERVAL=1d
	```
	The preceding command configures the RACcheck daemon to run every day. If you set this parameter to 0, then the RACcheck daemon will not run automatically. This is the default setting for this parameter.
- `AUTORUN_FLAGS`: This parameter defines how RACcheck runs, using the flags listed in Table D-1. For example:
	```
	$ raccheck -set "AUTORUN_INTERVAL=12h;AUTORUN_FLAGS=-profile sysadmin"
	```
	The preceding command configures RACcheck to run the `sysadmin` profile every 12 hours.
- `PASSWORD_CHECK_INTERVAL`: This parameter defines the frequency (specified in hours) with which the running daemon validates the passwords entered when the daemon starts. If the daemon encounters an invalid password (due to a password change), then the daemon stops running and enters a notification in the daemon log (`raccheck_daemon.log`), and also sends an email, if configured to do so. For example:
	```
	$ raccheck -set PASSWORD_CHECK_INTERVAL=1
	```
	The preceding command validates passwords every hour.
- `NOTIFICATION_EMAIL`: This parameter configures the RACcheck daemon to email notifications to a specific person. For example:
	```
	$ raccheck -set NOTIFICATION_EMAIL=firstname.lastname@company.com
	```

Note:

You can configure more than one parameter in a single command by providing each parameter in a semi-colon delimited list enclosed in double quotation marks (`""`). For example, the following command configures the RACcheck daemon to run every day in verbose mode, specifies an email address for daemon notices, and checks for changed passwords hourly:
```
$ raccheck -set "AUTORUN_INTERVAL=1d;AUTORUN_FLAGS= -o verbose;
NOTIFICATION_EMAIL=firstname.lastname@company.com;PASSWORD_CHECK_INTERVAL=1"
```

To obtain the current configuration of all of the parameters of the RACcheck daemon, run the following command:

```
$ raccheck -get all
```

The preceding command returns output similar to the following:

```
AUTORUN_INTERVAL = 1d
AUTORUN_FLAGS = -o verbose
NOTIFICATION_EMAIL = firstname.lastname@company.com
PASSWORD_CHECK_INTERVAL = 1
```

You can set or modify RACcheck parameters after the RACcheck daemon has started.

Note:

Oracle recommends that, at a minimum, you configure the `NOTIFICATION_EMAIL` and `PASSWORD_CHECK_INTERVAL` parameters.

To start the RACcheck daemon, run the following command:

```
$ raccheck –d start
```

RACcheck launches an interactive graphical user interface to collect the required information and start the daemon process.

You can run RACcheck on demand while the RACcheck daemon is running by entering `raccheck` on the command line without any arguments as the user that started the daemon process from the same directory from which you launched the RACcheck daemon. Running RACcheck this way is non-interactive, because the daemon passes parameters at all the prompts, and produces output on the screen similar to that which RACcheck produces when running interactively.

Note:

If the RACcheck daemon is running and want to run RACcheck interactively, then run the following command:
```
$ raccheck -nodaemon
```

RACcheck Daemon Usage Notes

- If you start the RACcheck daemon, then no other user can use the RACcheck daemon to run RACcheck in non-interactive mode. To use the RACcheck daemon, you must be the same user you must run RACcheck on demand from the same directory where you started daemon.
- Once you start the RACcheck daemon, it continues to run in the background until either you explicitly stop the daemon (using the `raccheck –d stop` command) or one of the following conditions is met:
	- The server on which the daemon is running is rebooted or stops.
		- If a password is changed on any node, then the daemon stops and an entry is placed in `raccheck_daemon.log`. Additionally, RACcheck sends an email to address entered in the `NOTIFICATION_EMAIL` configuration parameter. Configure the `PASSWORD_CHECK_INTERVAL` configuration parameter to ensure validity of the required passwords.
		- If the RACcheck script has changed or has been replaced with a new script since you started daemon, then any further attempts to run RACcheck on demand, as well as auto run will not succeed. You will have to restart daemon with new script for future run.
- If the system configuration has changed (such as nodes or instances being added or deleted), then you must restart the RACcheck daemon for the configuration changes to be recognized.

Comparing Reports with RACcheck

You can use RACcheck to compare results from two RACcheck reports. You can use the results of comparisons to monitor trends and best practice changes over time or after planned maintenance presented in a user-friendly HTML report. Ensure that the RACcheck reports in the RACcheck output directories, `.zip` output files, or HTML reports are accessible.

To compare two RACcheck reports, run the following command:

```
$ raccheck -diff report_1 report_2
```

Specify the names of the two report files you want to compare. When RACcheck finishes comparing the two files, the utility prints a summary and provides a location of the comparison report for viewing.

Running RACcheck to Determine Upgrade Readiness

You can use RACcheck to obtain an automated upgrade readiness assessment to help facilitate upgrade planning for Oracle RAC and Oracle Clusterware. Use RACcheck to automate many of the manual pre- and post-upgrade checks detailed in the following upgrade-related documents:

- Oracle Database Upgrade Guide
- Oracle Grid Infrastructure Installation Guide for your platform
- The following My Oracle Support notes:
	- `https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=785351.1`
		- `https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=837570.1`
		- `https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1363369.1`
		- `https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=810394.1`

You can run RACcheck before and after upgrading your software. Run the pre-upgrade check during the planning phase of the upgrade process to ensure that enough time is available to resolve any potential issues prior to the actual upgrade process. Run the post-upgrade check to ensure the health of Oracle Grid Infrastructure and Oracle Database. Following is a summary of what you can expect from RACcheck upgrade checks:

- When performing pre-upgrade checks, RACcheck detects all databases registered with Oracle Clusterware and produces a list of databases on which it will perform pre-upgrade checks. If any databases of the most current version are detected, then RACcheck skips them and will not perform any checks.
- When performing post-upgrade checks, RACcheck detects all databases registered with Oracle Clusterware and produces a list of databases on which it will perform post-upgrade checks. If RACcheck detects any databases versions preceding Oracle Database 11g release 2 (11.2.0.3), then RACcheck skips them and will not perform any checks.
- When performing either pre- or post-upgrade checks, RACcheck checks both Oracle Clusterware and the operating system.
- When RACcheck finishes its checks, the tool produces a report in HTML format that contains the findings and links to additional details and information.

Use the following syntax to run RACcheck upgrade checks:

```
$ raccheck -u -o pre | post
```

Maintaining the Output File

When you run RACcheck, the tool creates a subdirectory using a naming convention that begins with "raccheck" and includes a date and time (such as, `raccheck_SIEBXL_072613_141001`), and a zip file that contains the contents of the subdirectory (such as, `raccheck_SIEBXL_072611_141001.zip`) at the same level on the file system as RACcheck, itself. The total size of the subdirectory and zip file should be less than 5 MB on the file system. The exact varies depending upon how many nodes and how many databases there are in the system. While Oracle recommends that you run RACcheck when there is the least load on the system, over time, the number of files will build up and you must maintain and clean out older files, subdirectories, or both.

Multiple Database Support

Oracle designed RACcheck to support multiple databases. The tool presents a list of running databases, which are registered in the Oracle Grid Infrastructure. You can choose one, all, or enter a comma-delimited list of numbers that designate the listed databases. You do not have to install the tool on multiple nodes to check database instances running on other nodes in the cluster.

RACcheck logs into all databases by using local bequeath connections and assumes the existence of operating system authentication in the database for the user running the tool. In some configurations, there could be multiple database homes all owned by the same operating system user (such as `oracle`), while in other configurations, there could be any number of database homes all owned by different operating system users.

In the former case, run RACcheck as `oracle`. In the latter case, you may want to deploy RACcheck on the home with the greatest number of databases to obtain the most information possible, in which case install RACcheck as the owner of that home. To scan the other databases, RACcheck must be installed and run under each database home user account.

Uploading RACcheck Results and Patches to a Database for Reporting

Oracle supports uploading the results of audit checks done by RACcheck or the list of installed patches into database tables for use as a source of data for reporting.

To take advantage of this optional feature, you must set a number of environment variables in the runtime environment, and you must create two tables to receive the data: one for the audit check results and another for the patches installed on the systems.

To create a results table called `auditcheck_result`, run the following DDL command:

```
create table
  auditcheck_result
    (
    COLLECTION_DATE TIMESTAMP,
     CHECK_NAME VARCHAR2(256),
     PARAM_NAME VARCHAR2(256),
     STATUS VARCHAR2(256),
     STATUS_MESSAGE VARCHAR2(256),
     ACTUAL_VALUE VARCHAR2(256),
     RECOMMENDED_VALUE VARCHAR2(256),
     COMPARISON_OPERATOR VARCHAR2(256),
     HOSTNAME VARCHAR2(256),
     INSTANCE_NAME VARCHAR2(256),
     CHECK_TYPE VARCHAR2(256),
     DB_PLATFORM VARCHAR2(256),
     OS_DISTRO VARCHAR2(256),
     OS_KERNEL VARCHAR2(256),
     OS_VERSION NUMBER,
     DB_VERSION VARCHAR2(256),
     CLUSTER_NAME VARCHAR2(256),
     DB_NAME VARCHAR2(256),
     ERROR_TEXT VARCHAR2(256)
     CHECK_ID VARCHAR2(40),
     NEEDS_RUNNING VARCHAR2(100),
     MODULES VARCHAR2(4000),
     DATABASE_ROLE VARCHAR2(100),
     CLUSTERWARE_VERSION VARCHAR2(100),
     GLOBAL_NAME VARCHAR2(256)
);
```

To create a table for patches called `auditcheck_patch_result`, run the following DDL command:

```
create table
  auditcheck_patch_result
       ( COLLECTION_DATE     TIMESTAMP(6),
          HOSTNAME            VARCHAR2(256),
          ORACLE_HOME_TYPE    VARCHAR2(256),
          ORACLE_HOME_PATH    VARCHAR2(256),
          ORACLE_HOME_VERSION VARCHAR2(256),
          PATCH_NUMBER NUMBER,
         CLUSTER_NAME VARCHAR2(256),
         DESCRIPTION         VARCHAR2(256),
         PATCH_TYPE VARCHAR2(128),
         APPLIED NUMBER,
         RECOMMENDED NUMBER
         );
```

Set the following environment variables (shown with example values):

```
$ export RAT_UPLOAD_CONNECT_STRING="(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)
(HOST = bonanza)(PORT = 1521)) (LOAD_BALANCE = yes) (CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = orcl)))"
$ export RAT_UPLOAD_TABLE=auditcheck_result (name must match that of the table created for the purpose)
$ export RAT_PATCH_UPLOAD_TABLE=auditcheck_patch_result (name must match the name of the table created for the purpose)
$ export RAT_UPLOAD_USER=auditcheck (schema owner of the table created for the purpose)
$ export RAT_UPLOAD_PASSWORD=auditcheck (password for the schema owner)
$ export RAT_UPLOAD_ORACLE_HOME=path_of_database_home (optional, alternate home
containing sqlplus that you want to use for connecting in case it is not the
current $ORACLE_HOME as derived by RACcheck from the environment)
```

Note:

Use the fully-qualified address (as shown in the preceding example) for the connect string rather than an alias from the `tnsnames.ora` file, so that it is not necessary to rely on `tnsnames.ora` file name resolution on all the servers where RACcheck might run. You must use double quotation marks (`""`).

When you set the first four environment variables (shown in the preceding example) in the runtime environment, RACcheck assumes that the intent is to upload the data into the tables at the end of the process, and it attempts to upload the data. This process requires that you properly set the environment, that is, that the connect string is reachable, the user name and password are correct, and the table name is correct. If RACcheck cannot connect to the database, then a message to that effect will be written to the log. If the `RAT_UPLOAD_ORACLE_HOME` variable is set, then RACcheck invokes SQL\*Plus from that home rather than attempting to invoke SQL\*Plus from the current Oracle home derived by RACcheck. If you do not set any of the first four environment variables, then RACcheck will not attempt to upload the data.

Excluding Audit Checks

Optionally, you can exclude one or more audit checks after the first run of RACcheck, as follows:

1. Create a text file named `excluded_check_ids.txt` in the same directory as the RACcheck script and driver files.
2. Open the `raccheck.log` file, which is located in the output directory of the previous run of the tool.
3. Search for the audit checks that you want to exclude in subsequent runs.
4. Note the `CHECK_ID` of the audit checks you want to exclude. The `CHECK ID` is an alphanumeric string similar to `CHECK_ID = 65E4DC8B76BC4DA6E040E50A1EC03704`. If the audit check block does not contain a `CHECK_ID` line, then you cannot exclude that audit check.
5. Enter the `CHECK_ID` s for the audit checks that you want to exclude in the `excluded_check_ids.txt` file, one `CHECK_ID` per line.
6. Subsequently, when you run RACcheck, before the tool runs an audit check, it checks the `excluded_check_ids.txt` file for any excluded checks and skips them.

## Troubleshooting RACcheck

This section discusses various problems you may encounter when running RACcheck and how to solve them, included in the following sections:

- Runtime Command Timeouts
- The raccheck\_error.log File Contains Errors
- Remote root Login Problems
- Local Environmental Issues
- Database Login Problems
- User Profiles

Runtime Command Timeouts

If any non- `root` -privileged individual commands timeout before they finish running, then RACcheck stops that process and does not collect the desired data. If this happens, then you can lengthen the timeout by setting the following environment variable in the script execution environment:

```
$ export RAT_TIMEOUT=120
```

The default value for this environment variable is 90 seconds.

RACcheck runs a set of `root` -privileged data collections, once for each node in the cluster. If collections timeout before the data can be collected, then RACcheck stops that process and does not collect the desired data. If this happens, then you can lengthen the timeout by setting the following environment variable in the script execution environment:

```
$ export RAT_ROOT_TIMEOUT=600
```

The default value for this environment variable is 300 seconds.

Note:

If you encounter either of these timeouts, then Oracle recommends that you determine the cause of the delay and correct it, and that you run RACcheck during times of least load on the system.

The raccheck\_error.log File Contains Errors

You can ignore the following errors that do appear in the `raccheck_error.log` file:

- `/bin/sh: /u01/app/11.2.0/grid/OPatch/opatch: Permission denied`
- `chmod: changing permissions of '/u01/app/oracle_ebs/product/11.2.0.2/VIS_RAC/.patch_storage': Operation not permitted`
- `OPatch could not open log file, logging will not be possible`
- `Inventory load failed... OPatch cannot load inventory for the given Oracle Home.`

The preceding errors occur in role-separated environments when RACcheck, which is run as the database software owner, attempts to list the patch inventories of homes owned by other users (`grid`, for example, or other database home owners) using OPatch. When you run OPatch to list the patch inventories for those other users it causes errors because the current user does not have permissions on the other homes. In these cases the OPatch errors are ignored and the patch inventories for those homes are gathered by other means.

Additionally, you can ignore errors similar to the following:

`./raccheck: line [N]: [: : integer expression expected`

The line number may change over time but this error occurs when RACcheck expects an integer return value but no value was found. RACcheck returns that error when trying to make the comparison. You could see this error repeated many times for the same command, once for each node.

Remote root Login Problems

If remote `root` login is not permitted over SSH, then the `root` -privileged commands will fail. To verify the Oracle software owner (`oracle`), run the following command manually from whichever node is not working and ensure you get similar output, as follows:

```
$ ssh root@remotehostname "id"
root@remotehostname's password:
uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel)
```

If remote `root` login is not working, then RACcheck cannot check the remote nodes. Contact a system administrator to correct this, if only temporarily, for running RACcheck.

If you can configure the remote `root` login, then edit the `/etc/ssh/sshd_config` file, as follows:

```
PermitRootLogin to yes
```

Run the following command as `root` on all nodes of the cluster:

```
# /etc/init.d/sshd restart
```

Local Environmental Issues

RACcheck attempts to derive all the data it requires from the environment (operating system and Oracle Cluster Registry) but the tool may not work as expected because of local system differences, and it is difficult to anticipate and test every possible scenario. Therefore, support for a number of environment variables has been included so that you can override the default behavior of the tool or provide the required information. Following is a list of environment variables and descriptions for each:

- `RAT_INV_LOC`: If the `oraInst.loc` file is not located where expected (`/u01/app/oraInventory`), then you can specify the correct location of the `oraInventory` directory in this environment variable.
- `RAT_CRS_HOME`: You can set this environment variable if RACcheck cannot determine the correct `Grid_home` path, and displays information stating that the software is not installed, even though you know that Oracle Clusterware is installed.
- `RAT_ORACLE_HOME`: You can set this environment variable if RACcheck cannot determine the correct `ORACLE_HOME` paths for the databases registered with Oracle Clusterware, and displays information stating that the software is not installed, even though you know that the database software is installed. RACcheck performs best practice and recommended patch checks for all the databases running from the home specified in this environment variable.
- `RAT_ASM_HOME`: You can set this environment variable if RACcheck cannot determine the correct Oracle ASM home path (which is the same as the `Grid_home` path) from Oracle Clusterware, and displays information stating that the software is not installed, even though you know that the Oracle ASM software is installed.
- `RAT_OS`: You can set this environment variable if RACcheck fails to determine the correct platform, and the tool informs you that the data necessary for the determined platform could not be found.
- `RAT_DB`: You can set this environment variable if RACcheck determines an incorrect database version.
- `RAT_DBNAMES`: You can set this environment variable if RACcheck fails to determine valid database names from Oracle Clusterware. You can specify a space-delimited list of database names, and RACcheck will use that list instead of what it derives from Oracle Clusterware. For example:
	```
	$ export RAT_DBNAMES="ORCL ORADB PROD"
	```
	Use double quotation marks (`""`) if specifying more than one database name.
	Note:
	If you configure `RAT_DBNAMES` as a subset of databases registered with Oracle Clusterware, and you want the patch inventories of all databases found registered with Oracle Clusterware to have their patch inventories checked for recommended patches, then Oracle recommends that you also configure `RAT_DBHOMES`.
- `RAT_DBHOMES`: If you set the `RAT_DBNAMES` environment variable, then, by default, the recommended patch analysis will be limited to the homes for the database names you listed. If you want to perform the recommended patch analysis for additional database homes than those specified in `RAT_DBNAMES`, then specify a space-delimited list of databases whose homes you want checked for recommended patches. For example, assume that you run the `export RAT_DBNAMES="ORCL ORADB"` command but that you also want to check the `PROD` database home, even if the `PROD` database is down. Run the `export RAT_DBHOMES="ORCL ORADB PROD"` command so that best practices will be checked for the `ORCL` and `ORADB` databases but the recommended patches will be checked for the `ORCL`, `ORADB`, and `PROD` database homes. Use double quotation marks (`""`) if specifying more than one database name.
- `RAT_SSHELL`: Set this environment variable to specify a secure shell location that overrides the default location (typically, `/usr/bin/ssh`), in case `ssh` is not where it is expected, and `ssh` commands return the following error:
	```
	-bash: /usr/bin/ssh -q: No such file or directory
	```
- `RAT_SCOPY`: Set this environment variable to specify a secure copy location that overrides the default secure copy location (typically, `/usr/bin/scp`), in case `scp` is not where it is expected, and `scp` commands return the following error:
	```
	/usr/bin/scp -q: No such file or directory
	```

Database Login Problems

If you intend to run RACcheck as a user other than the database software installation owner (such as `root` or `grid`), and if you experience problems connecting to the database, then do the following:

1. Log in to the system as `grid`.
2. Run the following commands:
	```
	$ export ORACLE_HOME=path_to_Oracle_Database_home
	$ export ORACLE_SID=database_SID
	$ export PATH=$ORACLE_HOME/bin:$ORACLE_HOME/lib:$PATH
	```
3. Add an alias in the `$ORACLE_HOME/network/admin/tnsnames.ora` file for the `database_SID`.
4. Connect to the database as follows, including the password:
	```
	$ORACLE_HOME/bin/sqlplus sys@SID as sysdba
	```
5. Ensure that you have successful connection.

If this method of connecting to the database fails, then RACcheck will be unable to connect, as well. Consider running the tool as the Oracle database software installation owner.

User Profiles

The presence of prompts or traps in the user profile can lead to RACcheck hanging while it is running, because it sources the profile at runtime. For this reason, RACcheck checks the profile in the environment for these statements and presents a message advising you to temporarily comment out those statements on all nodes.

---

Footnote Legend

Footnote 1: Oracle does not plan to support Linux Itanium  
Footnote 2: Requires BASH Shell 3.2 or higher to be installed on the systems
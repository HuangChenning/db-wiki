---
title: Diagnosability in JDBC
book: "JDBC Developer's Guide"
doc_id: E16548-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/java.112/e16548/diagnose.htm
tags:
  - oracle
  - 11g
  - jdbc-developers-guide
---

## 31 Diagnosability in JDBC

In Oracle Database 11g, the JDBC drivers have been enhanced by including new diagnosabilty features and improving existing diagnosabilty features. These features enable users to diagnose problems in the applications that use Oracle JDBC drivers and the problems in the drivers themselves. They also reduce the effort required to develop and maintain Java applications that access an Oracle Database instance using Oracle JDBC drivers.

Oracle JDBC drivers provide the following diagnosabilty features that enable users to identify and fix problems in their JDBC applications:

- Logging
- Diagnosability Management

Note:

The diagnosability features of the JDBC drivers are based on the standard `java.util.logging` framework and the `javax.management` MBean framework. Information about these standard frameworks is not covered in this document. For more information about these standard frameworks refer to
```
http://www.oracle.com/technetwork/java/index.html
```

## Logging

This feature logs information about events that occur when JDBC driver code runs. Events can include user-visible events, such as SQL exceptions, running of SQL statements, and detailed JDBC internal events, such as entry to and exit from internal JDBC methods. Users can enable this feature to log specific events or all the events.

Prior to Oracle Database 11g, JDBC drivers supported J2SE 2.0 and 3.0. These versions of J2SE did not include `java.util.logging`. Therefore, the logging feature provided by JDBC driver releases prior to Oracle Database 11g, differs from the `java.util.logging` framework.

In Oracle Database 11g, the JDBC drivers no longer support J2SE 2.0 and 3.0. Therefore, the logging feature of JDBC drivers makes full use of the standard `java.util.logging` package. The enhanced logging system makes effective use of log levels to enable users to restrict log output to things of interest. It logs specific classes of information more consistently, making it easier for the user to understand the log file.

This feature does not introduce new APIs or configuration files. Only new parameters are added to the existing standard `java.util.logging` configuration file. These parameters are identical in use to the existing parameters and are intrinsic to using `java.util.logging`.

Note:

Oracle does not guarantee the exact content of the generated logs. To a large extent the log content is dependent on the details of the implementation. The details of the implementation change with every release, and therefore, the exact content of the logs are likely to change from release to release.

### Enabling and Using JDBC Logging

Before you can start debugging your Java application, you must enable and configure JDBC logging. This section covers the steps you must perform to enable and use JDBC logging. It describes the following:

#### Configuring the CLASSPATH

Oracle ships several JAR files for each version of the JDBC drivers. The optimized JAR files do not contain any logging code and, therefore, do not generate any log output when used. To get log output, you must use the debug JAR files, which are indicated with a "\_g" in the file name, like `ojdbc5_g.jar` or `ojdbc6_g.jar`. The debug JAR file must be included in the `CLASSPATH`.

Note:

Ensure that the debug JAR file, say `ojdbc5_g.jar` or `ojdbc6_g.jar`, is the only Oracle JDBC JAR file in the `CLASSPATH`.

#### Enabling Logging

You can enable logging in the following ways:

- Setting a Java system property
	You can enable logging by setting the `oracle.jdbc.Trace` system property.
	```
	java -Doracle.jdbc.Trace=true ...
	```
	Setting the system property enables global logging, which means that logging is enabled for the entire application. You can use global logging if you want to debug the entire application, or if you cannot or do not want to change the source code of the application.
- Programmatically
	You can programmatically enable or disable logging in the following way:
	First, get the `ObjectName` of the Diagnosability MBean. The `ObjectName` is
	```
	com.oracle.jdbc:type=diagnosability,name=<loader>
	```
	Here, `loader` is a unique name based on the class loader instance that loaded the Oracle JDBC drivers.
	Note:
	The drivers can be loaded multiple times in a single VM. So, there can be multiple MBeans, each with a unique name.
	Now, write the following lines of code:
	```
	ClassLoader l = oracle.jdbc.OracleDriver.getClassLoader();
	String loader = l.getName() + "@" + l.hashCode();
	// compute the ObjectName
	javax.management.ObjectName name = new javax.management.ObjectName("com.oracle.jdbc:type=diagnosability,
	name="+loader);
	// get the MBean server
	javax.management.MBeanServer mbs = java.lang.management.ManagementFactory.getPlatformMBeanServer();
	// find out if logging is enabled or not
	System.out.println("LoggingEnabled = " + mbs.getAttribute(name, "LoggingEnabled"));
	// enable logging
	mbs.setAttribute(name, new javax.management.Attribute("LoggingEnabled", true));
	// disable logging
	mbs.setAttribute(name, new javax.management.Attribute("LoggingEnabled", false));
	```
	Note:
	- If the same class loader loads the JDBC drivers multiple times, then each subsequent MBean increments the value of the `l.hashCode()` method, so as to create a unique name. It may be problematic to identify which MBean is associated with which JDBC driver instance.
	- If there is only one instance of the JDBC drivers loaded, then set the name to "\*".

Programmatic enabling and disabling of logging helps you to control what parts of your application need to generate log output.

Note:

Enabling logging using either of the methods would only generate a minimal log of serious errors. Usually this is not of much use. To generate a more useful and detailed log, you must configure `java.util.logging`.

#### Configuring Logging

To generate a useful and detailed log, you must configure `java.util.logging`. This can be done either through a configuration file or programmatically.

A sample configuration file, `OracleLog.properties`, is provided as part of the JDBC installation in the `demo` directory. It contains basic information about how to configure `java.util.logging` and provides some initial settings that you can start with. You may use this sample file as is, edit the file and use it, rename the file and edit it, or create an entirely new file of any name.

To use a configuration file, you must identify it to the Java run-time. This can be done by setting a system property. For example:

```
java -Djava.util.logging.config.file=/jdbc/demo/OracleLog.properties.
```

It is read by the `java.util.logging` system. This file can reside anywhere.

You can use both `java.util.logging.config.file` and `oracle.jdbc.Trace` at the same time.

```
java -Djava.util.logging.config.file=/jdbc/demo/OracleLog.properties -Doracle.jdbc.Trace=true
```

You can use the default `OracleLog.properties` file. It may or may not get you the desired output. You can also create and use your own configuration file by following these steps:

1. Create a file named `myConfig.properties`. You can use any name you choose.
2. Insert the following lines of text in the file:
	```
	.level=SEVERE
	oracle.jdbc.level=INFO
	oracle.jdbc.handlers=java.util.logging.ConsoleHandler
	java.util.logging.ConsoleHandler.level=INFO
	java.util.logging.ConsoleHandler.formatter=java.util.logging.SimpleFormatter
	```
3. Save the file.
4. Set the system property to use this configuration file.
	```
	java -Djava.util.logging.config.file=<filepath>/myConfig.properties ...
	```
	`filepath` is the path of the folder where you have saved the `myConfig.properties` file.

You can also configure `java.util.logging` to dump the log output into a file. To do so, modify the configuration file as follows:

```
.level=SEVERE
oracle.jdbc.level=INFO
oracle.jdbc.handlers=java.util.logging.FileHandler
java.util.logging.FileHandler.level=INFO
java.util.logging.FileHandler.pattern=jdbc.log
java.util.logging.FileHandler.count=1
java.util.logging.FileHandler.formatter=java.util.logging.SimpleFormatter
```

This will generate exactly the same log output and save it in a file named `jdbc.log` in the current directory.

You can control the amount of detail by changing the level settings. The defined levels from the least detailed to the most detailed are the following:

- `OFF`
	Turns off logging.
- `SEVERE`
	Logs SQLExceptions and internal errors.
- `WARNING`
	Logs SQLWarnings and bad but not fatal internal conditions.
- `INFO`
	Logs infrequent but significant events and errors. It produces a relatively low volume of log messages.
- `CONFIG`
	Logs SQL strings that are executed.
- `FINE`
	Logs the entry and exit to every public method providing a detailed trace of JDBC operations. It produces a fairly high volume of log messages.
- `FINER`
	Logs calls to internal methods.
- `FINEST`
	Logs calls to high volume internal methods.
- `ALL`
	Logs all the details. This is the most detailed level of logging.

Note:

Levels more detailed than `FINE` generate huge log volumes.

In the example provided earlier, to reduce the amount of detail, change the `java.util.logging.FileHandler.level` setting from `ALL` to `INFO`:

```
java.util.logging.FileHandler.level=INFO
```

Although you can, it is not necessary to change the level of the `oracle.jdbc` logger. Setting the `FileHandler` level will control what log messages are dumped into the log file.

#### Using Loggers

Setting the level reduces all the logging output from JDBC. However, sometimes you need a lot of output from one part of the code and very little from other parts. To do that you must understand more about loggers.

Loggers exist in a tree structure defined by their names. The root logger is named "", the empty string. If you look at the first line of the configuration file you see `.level=SEVERE`. This is setting the level of the root logger. The next line is `oracle.jdbc.level=INFO`. This sets the level of the logger named `oracle.jdbc`. The `oracle.jdbc` logger is a member of the logger tree. Its parent is named `oracle`. The parent of the `oracle` logger is the root logger (the empty string).

Logging messages are sent to a particular logger, for example, `oracle.jdbc`. If the message passes the level check at that level, then the message is passed to the handler at that level, if any, and to the parent logger. So a log message sent to `oracle.log` is compared against that logger's level, `INFO` if you are following along. If the level is the same or less (less detailed) then it is sent to the FileHandler and to the parent logger, 'oracle'. Again it is checked against the level. If as in this case, the level is not set then it uses the parent level, `SEVERE`. If the message level is the same or less it is passed to the handler, which there is not one, and sent to the parent. In this case the parent in the root logger.All this tree structure did not help you reduce the amount of output. What will help is that the JDBC drivers use several subloggers. If you restrict the log messages to one of the subloggers you will get substantially less output. The loggers used by Oracle JDBC drivers include the following:

- `oracle.jdbc`
- `oracle.jdbc.driver`
- `oracle.jdbc.pool`
- `oracle.jdbc.rowset`
- `oracle.jdbc.xa`
- `oracle.sql`

Note:

The loggers used by the drivers may vary from release to release.

#### An Example

Suppose you want to trace what is happening in the `oracle.sql` component and also want to capture some basic information about the rest of the driver. This is a more complex use of logging. The following are the entries in the `config` file:

```
# 
     # set levels 
     # 
.level=SEVERE
oracle.level=INFO
oracle.jdbc.driver.level=INFO
oracle.jdbc.pool.level=OFF
oracle.jdbc.util.level=OFF
oracle.sql.level=INFO
     # 
     # configure handlers
     # 
oracle.handlers=java.util.logging.ConsoleHandler
java.util.logging.ConsoleHandler.level=INFO
java.util.logging.ConsoleHandler.formatter=java.util.logging.SimpleFormatter
```

Let us consider what each line in the configuration file is doing.

```
.level=SEVERE
```

Sets the logging level of the root logger to `SEVERE`. We do not want to see any logging from other, non-Oracle components unless something fails badly. Therefore, we set the default level for all loggers to `SEVERE`. Each logger inherits its level from its parent unless set explicitly. By setting the level of the root logger to `SEVERE` we ensure that all other loggers inherit that level except for the ones we set otherwise.

```
oracle.level=INFO
```

We want log output from both the `oracle.sql` and `oracle.jdbc.driver` loggers. Their common ancestor is `oracle`. Therefore, we set the level of the `oracle` logger to `INFO`. We will control the detail more explicitly at lower levels.

```
oracle.jdbc.driver.level=INFO
```

We only want to see the SQL execution from `oracle.jdbc.driver`. Therefore, we set the level to `INFO`. This is a fairly low volume level, but will help us to keep track of what our test is doing.

```
oracle.jdbc.pool.level=OFF
```

We are using a `DataSource` in our test and do not want to see all of that logging. Therefore, we turn it `OFF`.

```
oracle.jdbc.util.level=OFF
```

We do not want to see the logging from the `oracle.jdbc.util` package. If we were using XA or row sets we would turn them off as well.

```
oracle.sql.level=INFO
```

We want to see what is happening in `oracle.sql`. Therefore, we set the level to `INFO`. This provides a lot of information about the public method calls without overwhelming detail.

```
oracle.handlers=java.util.logging.ConsoleHandler
```

We are going to dump everything to `stderr`. When we run the test we will redirect `stderr` to a file.

```
java.util.logging.ConsoleHandler.level=INFO
```

We want to dump everything to the console which is `System.err`. In this case, we are doing the filtering with the loggers rather than the handler.

```
java.util.logging.ConsoleHandler.formatter=java.util.logging.SimpleFormatter
```

We will use a simple, more or less human readable format.

When you run your test with this configuration file, you will get moderately detailed information from the `oracle.sql` package, a little bit of information from the core driver code, and nothing from any other code.

You can also use `XMLFormatter` for sending logs to Oracle Support.

You can implement and use a custom `java.util.logging.Filter` to obtain finer control of the data captured in the logs. This is a standard `java.util.logging` feature and is documented in the JSE JavaDoc. A custom Filter enables you to:

- Capture only one thread in multithreaded applications
- Capture intermittent errors in long running applications

### Performance, Scalability, and Security Issues

Although the logging feature enables you to trace or debug your application and generate detail log output, it has certain performance, scalability, and security issues.

Performance and Scalability Issues

Logging has substantial impact on performance. However, JDBC logging is generally not enabled in production systems. When logging is disabled, it will have no impact on performance.

It also has a negative impact on scalability. Logging involves protected access to a number of shared resources resulting in severely reduced scalability. This is intrinsic to the `java.util.logging` framework. However, in a typical production system, JDBC logging is not enabled and, therefore, will not have an impact on scalability.

Security Concerns

When full logging is enabled, it is almost guaranteed that all sensitive information will be exposed in the log files. This is intrinsic to the logging feature. However, only certain JDBC JAR files include the JDBC logging feature. The following JAR files include full logging and should not be used in a sensitive environment:

- `ojdbc5_g.jar`
- `ojdbc5dms_g.jar`
- `ojdbc6_g.jar`
- `ojdbc6dms_g.jar`

The following JAR files include a limited logging capability:

- `ojdbc5dms.jar`
- `ojdbc6dms.jar`

Note:

Database user names and passwords do not appear in log files created by these JAR files. However, sensitive user data that is part of a SQL statement, a defined value, or a bind value can appear in a log created using one of these JAR files.

## Diagnosability Management

The JDBC diagnosability management feature introduces an MBean, `oracle.jdbc.driver.OracleDiagnosabilityMBean`. This MBean provides means to enable and disable JDBC logging.

See Also:

For information about the `OracleDiagnosabilityMBean` API, refer to the Oracle Javadoc at
```
http://download.oracle.com/otn/utilities_drivers/jdbc/111060/doc/javadoc/index.html
```

In future releases, the MBean will be enhanced to provide additional statistics about JDBC internals.

Security Concerns

This feature can enable JDBC logging. Enabling JDBC logging does not require any special permission. However, once logging is enabled, generating any log output requires the standard Java permission `LoggingPermission`. Without this permission, any JDBC operation that would generate log output will throw a security exception. This is a standard Java mechanism.
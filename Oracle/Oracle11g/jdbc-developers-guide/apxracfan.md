---
title: Oracle RAC Fast Application Notification
book: "JDBC Developer's Guide"
doc_id: E16548-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/java.112/e16548/apxracfan.htm
tags:
  - oracle
  - 11g
  - jdbc-developers-guide
---

## B Oracle RAC Fast Application Notification

Oracle Database 11g Release 2 (11.2) introduces a new set of APIs for Oracle RAC Fast Application Notification (FAN) events. These APIs provide an alternative for taking advantage of the high-availability (HA) features of Oracle Database, if you do not use Universal Connection Pool or Oracle JDBC connection caching. These APIs are not a part of Oracle JDBC APIs.

This appendix covers the following topics:

This feature depends on the Oracle Notification System (ONS) message transport mechanism. This feature requires configuring your system, servers, and clients to use ONS.

For using Oracle RAC Fast Application Notification, the `simplefan.jar` file must be present in the classpath, and either the `ons.jar` file must be present in the classpath or an Oracle Notification Services (ONS) client must be installed and running in the client system.

## Overview of Oracle RAC Fast Application Notification

The Oracle RAC Fast Application Notification (FAN) feature provides a simplified API for accessing FAN events through a callback mechanism. This mechanism enables application code to receive a callback when a FAN event occurs. These APIs are referred to as Oracle RAC FAN APIs in this appendix.

The Oracle RAC FAN APIs provide FAN event notification for developing more responsive applications that can take full advantage of Oracle Database HA features. If you do not want to use Universal Connection Pool, but want to work with FAN events implementing your own connection cache, then you should use Oracle RAC Fast Application Notification.

Note:

- If you do not want to implement your own connection cache, then you should use Universal Connection Pooling to get all the advantages of Oracle RAC Fast Application Notification, along with many additional benefits. For more information on Universal Connection Pooling, refer to Oracle Universal Connection Pool for JDBC Developer's Guide.
- Starting from Oracle Database 11g Release 2 (11.2), implicit connection cache has been deprecated, and replaced with Universal Connection Pool (UCP) for JDBC. Oracle recommends that you take advantage of the new architecture, which is more powerful and offers better performance. Refer to the following link for more information
	```
	http://www.oracle.com/technology/tech/java/sqlj_jdbc/index.html
	```

The Oracle RAC FAN APIs enable application code to receive and respond to FAN event notifications sent by Oracle RAC. This is achieved by enabling the code to respond to FAN events in the following way:

- Listening for Oracle RAC service down, service up, and node down events
- Listening for load balancing advisory events and responding to them

This feature exposes a subset of FAN events, which are the notifications sent by a cluster running Oracle RAC, to inform the subscribers about the configuration changes within the cluster. The supported FAN events are the following:

- Service up
	The service up events notify that the managed resources are up and available. The cluster sends service up events when a cluster managed Database service becomes active, that is, available to accept work on an instance within the cluster.
- Service down
	The service down events notify that the managed resources are down and currently not available for access. There are two kinds of service down events:
	- Events indicating that a particular instance of a service is down and the instance is no longer able to accept work.
		- Events indicating that all instances of a service are down and the service is no longer able to accept work.
	When the last instance of a service goes down, then the subscriber receives both events. The events may or may not arrive together.
- Node down
	The node down events notify that the Oracle RAC node identified by the host identifier is down and not reachable. The cluster sends node down events when a node is no longer able to accept work.
- Load balancing advisory
	The load balancing advisory events provide metrics for load balancing algorithms. Load balancing advisories are sent regularly to inform subscribers of the recommended distribution of work among the available nodes.

Note:

If you want to implement your own connection cache, only then you should use Oracle RAC Fast Application Notification. Otherwise, you should use Universal Connection Pooling to get all the advantages of Oracle RAC Fast Application Notification, along with many additional benefits. For more information on Universal Connection Pooling, refer to Oracle Universal Connection Pool for JDBC Developer's Guide.

## Installing and Configuring Oracle RAC Fast Application Notification

You can install the Oracle RAC FAN APIs by performing the following steps:

1. Download the `simplefan.jar` file from the following link
	```
	http://www.oracle.com/technology/tech/java/sqlj_jdbc/index.html
	```
2. Add the `simplefan.jar` file to the classpath.
3. Perform the following in your Java code:
	1. Get an instance of the `FanManager` class by using the `getInstance` method.
		2. Configure the event daemon using the `configure` method of the `FanManager` class. The `configure` method sets the following properties:
		`onsNodes`: A comma separated list of `host:port` pairs of ONS daemons that the ONS runtime in this Java VM should communicate with. The `host` in a `host:port` pair is the host name of a system running the ONS daemon. The `port` is the local port configuration parameter for that daemon.
		`onsWalletFile`: The path name of the ONS wallet file. The wallet file is the path to a local wallet file used by SSL to store SSL certificates. Same as wallet file configuration parameter to ONS daemon.
		`onsWalletPassword`: The password for accessing the ONS wallet file.

For a detailed description of the Oracle RAC FAN APIs, refer to [Oracle Database RAC FAN Events Java API Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e13993/toc.htm).

### Configuration of ONS

The Java API for Oracle RAC FAN Events depends on the Oracle Notification System (ONS) service. This section describes how to configure ONS. It covers the following topics:

- Overview of ONS Configuration File
- Configuring Client-Side ONS

#### Overview of ONS Configuration File

ONS configuration is controlled by the ONS configuration file, `ORACLE_HOME` `/opmn/conf/ons.config`. This file tells the ONS daemon how it should behave. Configuration information within `ons.config` is defined in simple name and value pairs.

Some parameters in the `ons.config` file are required and some are optional. Table B-1 lists the required ONS configuration parameters and Table B-2 lists the optional ONS configuration parameters.

Table B-1 Required ONS Configuration Parameters

| Parameter | Explanation |
| --- | --- |
| `localport` | The port that ONS binds to on the local host interface to talk to local clients.  For example, `localport=4100` |
| `remoteport` | The port that ONS binds to on all interfaces for talking to other ONS daemons.  For example, `remoteport=4200` |
| `nodes` | A list of other ONS daemons to talk to. Node values are given as a comma-delimited list of either host names or IP addresses plus ports. The port value that is given is the remote port that each ONS instance is listening on. In order to maintain an identical file on all nodes, the `host:port` of the current ONS node can also be listed in the nodes list. It will be ignored when reading the list.  For example, `nodes=myhost.example.com:4200,123.123.123.123:4200`  The nodes listed in the nodes line correspond to the individual nodes in the Oracle RAC instance. Listing the nodes ensures that the middle-tier node can communicate with the Oracle RAC nodes. At least one middle-tier node and one node in the Oracle RAC instance must be configured to see one another. As long as one node on each side is aware of the other, all nodes are visible. You need not list every single cluster and middle-tier node in the ONS configuration file of each Oracle RAC node. In particular, if one ONS configuration file cluster node is aware of the middle tier, then all nodes in the cluster are aware of it. |

Table B-2 Optional ONS Configuration Parameters

| Parameter | Description |
| --- | --- |
| `loglevel` | The level of messages that should be logged by ONS. This value is an integer that ranges from 1, which indicates least messages logged, to 9, which indicates most messages logged. The default value is 3.  For example, `loglevel=3` |
| `logfile` | A log file that ONS should use for logging messages. The default value for log file is `$ORACLE_HOME/opmn/logs/ons.log`.  For example, `logfile=/private/oraclehome/opmn/logs/myons.log` |
| `walletfile` | The wallet file used by the Oracle Secure Sockets Layer (SSL) to store SSL certificates. If a wallet file is specified to ONS, then it uses SSL when communicating with other ONS instances and require SSL certificate authentication from all ONS instances that try to connect to it. This means that if you want to turn on SSL for one ONS instance, then you must turn it on for all instances that are connected. This value should point to the directory where your `ewallet.p12` file is located.  For example, `walletfile=/private/oraclehome/opmn/conf/ssl.wlt/default` |
| `useocr` | The value, reserved for use on the server-side, to indicate ONS whether it should store all Oracle RAC nodes and port numbers in Oracle Cluster Registry (OCR) instead of the ONS configuration file or not. A value of `useocr=on` is used to store all Oracle RAC nodes and port numbers in Oracle Cluster Registry (OCR).  Do not use this option on the client-side. |

The `ons.config` file allows blank lines and comments on lines that begin with the number sign (`#`).

#### Configuring Client-Side ONS

You can access the client-side ONS through `ORACLE_HOME` `/opmn`. On the client-side, there are two ways to set up ONS:

- Remote ONS configuration
	See Also:
	["Remote ONS Subscription"](fstconfo.md)
- ONS daemon on the client-side

Example B-1 illustrates how a sample configuration file may look.

Example B-1 Example of a Sample ons.config File

```
# This is an example ons.config file
#
# The first three values are required
localport=4100
remoteport=4200
nodes=racnode1.example.com:4200,racnode2.example.com:4200
```

After configuring ONS, you start the ONS daemon with the `onsctl` command. It is the user's responsibility to make sure that an ONS daemon is running at all times.

Using the onsctl Command

After configuring, use `ORACLE_HOME` `/opmn/bin/onsctl` to start, stop, reconfigure, and monitor the ONS daemon. Table B-3 is a summary of the commands that `onsctl` supports.

Table B-3 onsctl Commands

| Command | Effect | Output |
| --- | --- | --- |
| `start` | Starts the ONS daemon | `onsctl: ons started` |
| `stop` | Stops the ONS daemon | `onsctl: shutting down ons daemon...` |
| `ping` | Verifies whether or not the ONS daemon is running | `ons is running ...` |
| `reconfig` | Triggers a reload of the ONS configuration without shutting down the ONS daemon |  |
| `help` | Prints a help summary message for onsctl |  |
| `detailed` | Prints a detailed help message for onsctl |  |

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/adddelunix.htm#RACAD0067)

## Using Oracle RAC Fast Application Notification

Example B-2 provides an example to use Oracle RAC Fast Application Notification in your code. This example code prints the event data to the standard output device.

This example code demonstrates sample usages of Oracle RAC FAN APIs by overloading the `handleFanEvent` method to accept different FAN event notifications as arguments. The example code also displays event data such as

- Name of the system sending the FAN event notification
- Timestamp of the FAN event notification
- Load status of the FAN event notification

Example B-2 Example of Sample Code Using Oracle RAC FAN API

```
...
...Properties props = new Properties();
props.putProperty(“serviceName”, “gl”);
FanSubscription sub = FanManager.getInstance().subscribe(props);
sub.addListener(new FanEventListener()) {
  public void handleFanEvent(ServiceDownEvent event) {
    try {
      System.out.println(event.getTimestamp());
      System.out.println(event.getServiceName());
      System.out.println(event.getDatabaseUniqueName());
      System.out.println(event.getReason());
      ServiceMemberEvent me = se.getServiceMemberEvent();
      if (me != null) {
        System.out.println(me.getInstanceName());
        System.out.println(me.getNodeName());
        System.out.println(me.getServiceMemberStatus());
      }
      ServiceCompositeEvent ce = se.getServiceCompositeEvent();
      if (ce != null) {
        System.out.println(ce.getServiceCompositeStatus());
      }
    }
    catch (Throwable t) {
      // handle all exceptions and errors
      t.printStackTrace(System.err);
    }
  }
  public void handleFanEvent(NodeDownEvent event) {
    try {
      System.out.println(event.getTimestamp());
      System.out.println(ne.getNodeName());
      System.out.println(ne.getIncarnation());
    }
    catch (Throwable t) {
      // handle all exceptions and errors
      t.printStackTrace(System.err);
    }
  }
  public void handleFanEvent(LoadAdvisoryEvent event) {
    try {
      System.out.println(event.getTimestamp());
      System.out.println(le.getServiceName());
      System.out.println(le.getDatabaseUniqueName());
      System.out.println(le.getInstanceName());
      System.out.println(le.getPercent());
      System.out.println(le.getServiceQuality());
      System.out.println(le.getLoadStatus());
    }
    catch (Throwable t) {
      // handle all exceptions and errors
      t.printStackTrace(System.err);
    }
  }
});
```

## Implementing a Connection Cache

You must implement your own connection cache for using Oracle RAC FAN APIs. Consider the following points before you implement a connection cache using the Oracle RAC FAN APIs:

- Oracle RAC FAN APIs provide a minimal subset of FAN events.
- Oracle RAC FAN APIs support only ONS events. If you want your application to support corresponding supercluster events, then you may require additions to the subscription properties.
- Oracle RAC FAN APIs do not enable application code to send FAN events.
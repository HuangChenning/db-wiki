---
title: "第4章 DM JDBC编程指南"
book: "DM7程序员手册"
version: "DM7"
source: "temp/doc/DM7³ÌÐòÔ±ÊÖ²á.pdf#page=133"
tags:
  - dameng
  - dm7
  - programmer
---

## 第4 章 DM JDBC 编程指南

## 4.1 JDBC 介绍

JDBC（Java Database Connectivity）是Java 应用程序与数据库的接口规范，旨在让各数据库开发商为Java 程序员提供标准的数据库应用程序编程接口（API）。JDBC 定义了一个跨数据库、跨平台的通用SQL 数据库API。

DM JDBC 驱动程序是DM 数据库的JDBC 驱动程序，它是一个能够支持基本SQL 功能的通用应用程序编程接口，支持一般的SQL 数据库访问。

通过JDBC 驱动程序，用户可以在应用程序中实现对DM 数据库的连接与访问，JDBC驱动程序的主要功能包括：

1. 建立与DM 数据库的连接；
2. 转接发送SQL 语句到数据库；
3. 处理并返回语句执行结果。

## 4.2 JDBC 基本示例

利用JDBC 驱动程序进行编程的一般步骤为：

1. 获得java.sql.Connection 对象。

利用DriverManager 或者数据源来建立同数据库的连接。

2. 创建java.sql.Statement 对象。这里也包含了java.sql.PreparedStatement 和

java.sql.CallableStatement 对象。

利用连接对象的创建语句对象的方法来创建。在创建的过程中，根据需要来设置结果集的属性。

3. 数据操作。

数据操作主要分为两个方面，一个是更新操作，例如更新数据库、删除一行、创建一个新表等；另一个就是查询操作，执行完查询之后，会得到一个java.sql.ResultSet对象，可以操作该对象来获得指定列的信息、读取指定行的某一列的值。

4. 释放资源。

在操作完成之后，用户需要释放系统资源，主要是关闭结果集、关闭语句对象，释放连接。当然，这些动作也可以由JDBC 驱动程序自动执行，但由于Java 语言的特点，这个过程会比较慢(需要等到Java 进行垃圾回收时进行)，容易出现意想不到的问题。

下面用一个具体的编程实例来展示利用JDBC 驱动程序进行数据库操作的基本步骤：

/*该例程实现插入数据，修改数据，删除数据，数据查询等基本操作。*/import java.awt.Color;

import java.awt.Font;

import java.awt.Graphics2D;

import java.awt.font.FontRenderContext;

import java.awt.geom.Rectangle2D;

## 第4 章 DM JDBC 编程指南

import java.awt.image.BufferedImage;

import java.io.BufferedInputStream;

import java.io.File;

import java.io.FileInputStream;

import java.io.FileNotFoundException;

import java.io.FileOutputStream;

import java.io.IOException;

import java.io.InputStream;

import java.math.BigDecimal;

import java.sql.CallableStatement;

import java.sql.Connection;

import java.sql.Date;

import java.sql.DriverManager;

import java.sql.PreparedStatement;

import java.sql.ResultSet;

import java.sql.ResultSetMetaData;

import java.sql.SQLException;

import java.sql.Statement;

import javax.imageio.ImageIO;

public class BasicApp {// 定义DM JDBC 驱动串String jdbcString = "dm.jdbc.driver.DmDriver";

// 定义DM URL 连接串String urlString = "jdbc:dm://localhost:5236";

// 定义连接用户名String userName = "SYSDBA";

// 定义连接用户口令String password = "SYSDBA";

// 定义连接对象Connection conn = null;

/* 加载JDBC 驱动程序* @throws SQLException 异常 */public void loadJdbcDriver() throws SQLException {try {System.out.println("Loading JDBC Driver...");

// 加载JDBC 驱动程序Class.forName(jdbcString);

} catch (ClassNotFoundException e) {throw new SQLException("Load JDBC Driver Error : " + e.getMessage());

} catch (Exception ex) {throw new SQLException("Load JDBC Driver Error : "+ ex.getMessage());

}}

## 第4 章 DM JDBC 编程指南

/* 连接DM 数据库* @throws SQLException 异常 */public void connect() throws SQLException {try {System.out.println("Connecting to DM Server...");

// 连接DM 数据库conn = DriverManager.getConnection(urlString, userName, password);

} catch (SQLException e) {throw new SQLException("Connect to DM Server Error : "+ e.getMessage());

}}/* 关闭连接* @throws SQLException 异常 */public void disConnect() throws SQLException {try {// 关闭连接conn.close();

} catch (SQLException e) {throw new SQLException("close connection error : " + e.getMessage());

}}/* 往产品信息表插入数据* @throws SQLException 异常 */public void insertTable() throws SQLException {// 插入数据语句String sql = "INSERT INTO production.product(name,author,publisher,publishtime,"+ "product_subcategoryid,productno,satetystocklevel,originalprice,nowprice,discount,"+ "description,photo,type,papertotal,wordtotal,sellstarttime,sellendtime) "+ "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);";

// 创建语句对象PreparedStatement pstmt = conn.prepareStatement(sql);

// 为参数赋值pstmt.setString(1, "三国演义");

pstmt.setString(2, "罗贯中");

pstmt.setString(3, "中华书局");

pstmt.setDate(4, Date.valueOf("2005-04-01"));

pstmt.setInt(5, 4);

pstmt.setString(6, "9787101046121");

pstmt.setInt(7, 10);

pstmt.setBigDecimal(8, new BigDecimal(19.0000));

pstmt.setBigDecimal(9, new BigDecimal(15.2000));

pstmt.setBigDecimal(10, new BigDecimal(8.0));

pstmt.setString(11, "《三国演义》是中国第一部长篇章回体小说，中国小说由短篇发展至长篇的

## 第4 章 DM JDBC 编程指南

原因与说书有关。");

// 设置大字段参数try {// 创建一个图片用于插入大字段String filePath = "c:\\三国演义.jpg";

CreateImage(filePath);

File file = new File(filePath);

InputStream in = new BufferedInputStream(new FileInputStream(file));

pstmt.setBinaryStream(12, in, (int) file.length());

} catch (FileNotFoundException e) {System.out.println(e.getMessage());

// 如果没有图片设置为NULL pstmt.setNull(12, java.sql.Types.BINARY);

} catch (IOException e) {System.out.println(e.getMessage());

}pstmt.setString(13, "25");

pstmt.setInt(14, 943);

pstmt.setInt(15, 93000);

pstmt.setDate(16, Date.valueOf("2006-03-20"));

pstmt.setDate(17, Date.valueOf("1900-01-01"));

// 执行语句pstmt.executeUpdate();

// 关闭语句pstmt.close();

}/* 查询产品信息表* @throws SQLException 异常 */public void queryProduct() throws SQLException {// 查询语句String sql = "SELECT productid,name,author,description,photo FROM production.product WHERE productid=11";

// 创建语句对象Statement stmt = conn.createStatement();

// 执行查询ResultSet rs = stmt.executeQuery(sql);

// 显示结果集displayResultSet(rs);

// 关闭结果集rs.close();

// 关闭语句stmt.close();

}/* 修改产品信息表数据

## 第4 章 DM JDBC 编程指南

* @throws SQLException 异常 */public void updateTable() throws SQLException {// 更新数据语句String sql = "UPDATE production.product SET name = ?"+ "WHERE productid = 11;";

// 创建语句对象PreparedStatement pstmt = conn.prepareStatement(sql);

// 为参数赋值pstmt.setString(1, "三国演义（上）");

// 执行语句pstmt.executeUpdate();

// 关闭语句pstmt.close();

}/* 删除产品信息表数据* @throws SQLException 异常 */public void deleteTable() throws SQLException {// 删除数据语句String sql = "DELETE FROM production.product WHERE productid = 11;";

// 创建语句对象Statement stmt = conn.createStatement();

// 执行语句stmt.executeUpdate(sql);

// 关闭语句stmt.close();

}/* 查询产品信息表* @throws SQLException 异常 */public void queryTable() throws SQLException {// 查询语句String sql = "SELECT productid,name,author,publisher FROM production.product";

// 创建语句对象Statement stmt = conn.createStatement();

// 执行查询ResultSet rs = stmt.executeQuery(sql);

// 显示结果集displayResultSet(rs);

// 关闭结果集rs.close();

// 关闭语句stmt.close();

}/* 调用存储过程修改产品信息表数据* @throws SQLException 异常 */

## 第4 章 DM JDBC 编程指南

public void updateProduct() throws SQLException {// 更新数据语句String sql = "{ CALL production.updateProduct(?,?) }";

// 创建语句对象CallableStatement cstmt = conn.prepareCall(sql);

// 为参数赋值cstmt.setInt(1, 1);

cstmt.setString(2, "红楼梦（上）");

// 执行语句cstmt.execute();

// 关闭语句cstmt.close();

}/* 显示结果集* @param rs 结果集对象* @throws SQLException 异常 */private void displayResultSet(ResultSet rs) throws SQLException {// 取得结果集元数据ResultSetMetaData rsmd = rs.getMetaData();

// 取得结果集所包含的列数int numCols = rsmd.getColumnCount();

// 显示列标头for (int i = 1; i <= numCols; i++) {if (i > 1) {System.out.print(",");

}System.out.print(rsmd.getColumnLabel(i));

}System.out.println("");

// 显示结果集中所有数据while (rs.next()) {for (int i = 1; i <= numCols; i++) {if (i > 1) {System.out.print(",");

}// 处理大字段if ("IMAGE".equals(rsmd.getColumnTypeName(i))) {byte[] data = rs.getBytes(i);

if (data != null && data.length > 0) {FileOutputStream fos;

try {fos = new FileOutputStream("c:\\三国演义1.jpg");

fos.write(data);

fos.close();

## 第4 章 DM JDBC 编程指南

} catch (FileNotFoundException e) {System.out.println(e.getMessage());

} catch (IOException e) {System.out.println(e.getMessage());

}}System.out.print("字段内容已写入文件c:\\三国演义1.jpg，长度" + data.length);

} else {// 普通字段System.out.print(rs.getString(i));

}}System.out.println("");

}}/* 创建一个图片用于插入大字段* @throws IOException 异常 */private void CreateImage(String path) throws IOException {int width = 100;

int height = 100;

String s = "三国演义";

File file = new File(path);

Font font = new Font("Serif", Font.BOLD, 10);

BufferedImage bi = new BufferedImage(width, height,BufferedImage.TYPE_INT_RGB);

Graphics2D g2 = (Graphics2D) bi.getGraphics();

g2.setBackground(Color.WHITE);

g2.clearRect(0, 0, width, height);

g2.setPaint(Color.RED);

FontRenderContext context = g2.getFontRenderContext();

Rectangle2D bounds = font.getStringBounds(s, context);

double x = (width - bounds.getWidth()) / 2;

double y = (height - bounds.getHeight()) / 2;

double ascent = -bounds.getY();

double baseY = y + ascent;

g2.drawString(s, (int) x, (int) baseY);

ImageIO.write(bi, "jpg", file);

}/** 类主方法 @param args 参数*/public static void main(String args[]) {try {// 定义类对象

## 第4 章 DM JDBC 编程指南

BasicApp basicApp = new BasicApp();

// 加载驱动程序basicApp.loadJdbcDriver();

// 连接DM 数据库basicApp.connect();

// 插入数据System.out.println("--- 插入产品信息 ---");

basicApp.insertTable();

// 查询含有大字段的产品信息System.out.println("--- 显示插入结果 ---");

basicApp.queryProduct();

// 在修改前查询产品信息表System.out.println("--- 在修改前查询产品信息 ---");

basicApp.queryTable();

// 修改产品信息表System.out.println("--- 修改产品信息 ---");

basicApp.updateTable();

// 在修改后查询产品信息表System.out.println("--- 在修改后查询产品信息 ---");

basicApp.queryTable();

// 删除产品信息表System.out.println("--- 删除产品信息 ---");

basicApp.deleteTable();

// 在删除后查询产品信息表System.out.println("--- 在删除后查询产品信息 ---");

basicApp.queryTable();

// 调用存储过程修改产品信息表System.out.println("--- 调用存储过程修改产品信息 ---");

basicApp.updateProduct();

// 在存储过程更新后查询产品信息表System.out.println("--- 调用存储过程后查询产品信息 ---");

basicApp.queryTable();

// 关闭连接basicApp.disConnect();

} catch (SQLException e) {System.out.println(e.getMessage());

}}}

运行程序，启动达梦数据库服务器并创建用于修改产品信息的存储过程。存储过程代码如下：

-- 创建修改产品信息的存储过程create or replace procedure "PRODUCTION"."updateProduct"

## 第4 章 DM JDBC 编程指南

(v_id int,v_name varchar(50))as begin UPDATE production.product SET name = v_name WHERE productid = v_id;

end;

将以上Java 程序保存为C:\BasicApp.java 文件，打开命令行窗口进入C盘根目录，输入javac BasicApp.java 编译该类文件，编译完成后在命令行窗口输入java -classpath D:\dmdbms\jdbc\Dm7JdbcDriver.jar; BasicApp 运行该文件。其中，Dm7JdbcDriver.jar 有三个版本： Dm7JdbcDriver.jar15、Dm7JdbcDriver.jar16 和Dm7JdbcDriver.jar17，分别对应JDK版本1.5、1.6 和1.7，用户根据需要自行选择。

注意这里还需要将达梦数据库驱动程序Dm7JdbcDriver.jar（根据JDK 版本选择上述三个驱动之一）文件加入到classpath 中，达梦数据库驱动程序Dm7JdbcDriver.jar 文件存在于达梦数据库安装路径下的jdbc 目录下，这里假设达梦数据库安装在 D:\dmdbms7 目录，那么达梦数据库驱动程序Dm7JdbcDriver.jar 文件就在D:\dmdbms7\ jdbc 目录下。

## 4.3 DM JDBC 特性

DM JDBC 驱动程序有JDBC3.0 和JDBC4.0 两种类型。

DM JDBC 3.0 驱动程序符合SUN JDBC3.0 标准，实现了JDBC3.0 规范所要求的下列接口：

java.sql.Driver java.sql.Connection java.sql.Statement java.sql.PreparedStatement java.sql.CallableStatement java.sql.ResultSet java.sql.ResultSetMetaData java.sql.DatabaseMetaData java.sql.Blob java.sql.Clob java.sql.PrameterMetaData java.sql.Savepoint javax.sql.DataSource javax.sql.ConnectionEvent javax.sql.ConnectionEventListener javax.sql.ConnectionPoolDataSource javax.sql.PooledConnection DM JDBC 4.0 驱动程序符合SUN JDBC4.0 标准，实现了下列新特性：

1. JDBC 驱动类的自动加载；
2. 连接管理的增强；
3. 对RowId SQL 类型的支持；

## 第4 章 DM JDBC 编程指南

4. SQL 的DataSet 实现使用了Annotations；
5. SQL 异常处理的增强；
6. 对SQL XML 的支持；
7. 对BLOB/CLOB 的改进支持以及对国际字符集的支持。

## 4.4 DM JDBC 扩展

DM JDBC 驱动程序为了支持DM 特有的数据类型，采用了自定义扩展包的方式来进行解决。DM.sql 这个包中包含了DM 特有数据类型所对应的类。时间间隔类型是DM 具有的数据类型，JDBC 标准中没有相对应的类型。故令dm.sql.DmdbIntervalYM 和dm.sql.DmdbIntervalDT 分别对应于年-月间隔类型和日-时间隔类型。JDBC 标准中的java.sql.Types.Time 类型不允许带有纳秒，为了表示DM 中带纳秒的时间类型，设立了dm.sql.DmdbTime 类型。这些类型的主要方法为：

1. Dm.sql.DmdbIntervalDT

方法名功能说明DmdbIntervalDT(byte[]) 利用字节数组作为参数的构造函数。

DmdbIntervalDT(byte[],int,int) 利用字节数组，指定引导精度、纳秒精度构造函数。

DmdbIntervalDT(String) 利用字符串作为参数的构造函数。

DmdbIntervalDT(String,int,int) 设置字符串，指定引导精度、纳秒精度构造函数。

getByteArrayValue() 获取字节数组。

getDTString() 把DmdbIntervalDT 的值以字符串的形式返回。

getDTType() 获取DmdbIntervalDT 值类型。

getDay() 获取DmdbIntervalDT 值中日值。

getHour() 获取DmdbIntervalDT 值中时值。

getMinute() 获取DmdbIntervalDT 值中分值。

getSecond() 获取DmdbIntervalDT 值中秒值。

getNano() 获取DmdbIntervalDT 值中纳秒值。

getLoadPrec() 获取DmdbIntervalDT 值中引导精度数。

getSecPrec() 获取DmdbIntervalDT 值中纳秒精度数。

clear() 清除DmdbIntervalDT 值。

2. Dm.sql.DmdbIntervalYM

方法名功能说明DmdbInterval (byte[]) 利用字节数组作为参数的构造函数。

DmdbInterval (byte[],int) 利用字节数组、精度作为参数构造函数，精度默认为0。

DmdbInterval (String) 利用字符串作为参数的构造函数。

DmdbInterval (String,int) 利用字符串、精度作为参数的构造函数，精度默认为0。

getByteArrayValue() 把DmdbIntervalYM 的值以字节数组的形式返回。

getYMString() 把DmdbIntervalYM 的值以字符串的形式返回。

getYMType() 获取DmdbIntervalYM 值类型。

getYear() 返回DmdbIntervalYM 值中的年值。

getMonth() 返回DmdbIntervalYM 值中的月值。

getLoadPrec() 获取DmdbIntervalYM 的引导精度。

## 第4 章 DM JDBC 编程指南

toString() 把DmdbIntervalYM 的值转化为字符串的形式。

clear() 清除DmdbIntervalYM 值信息。

3. Dm.sql.DmdbTime

方法名功能说明DmdbTime(bytes[],int) 利用字节数组、引导精度作为参数构造函数。

DmdbTime(String,int) 利用字符串、引导精度作为参数的构造函数。

getBytesArray() 把DmdbTime 的值以字节数组的形式返回。

getHour() 获取DmdbTime 值中的时值。

getMinute() 获取DmdbTime 值中的分值。

getSecond() 获取DmdbTime 值中的秒值。

getNano() 获取DmdbTime 值中的纳秒值。

getTime() 以java.sql.Time 的形式返回DmdbTime 的值。只是去掉纳秒而已。

getTimestamp() 以java.sql.Timestamp 的形式返回DmdbTime 的值。

getTimeWithNano() 以字符串的形式返回DmdbTime 的值，并包括纳秒信息。

getTimeWithoutNano() 以字符串的形式返回DmdbTime 的值，并且不包括纳秒信息。

toString() 把DmdbTime 的值转化为字符串的形式。

4. 访问方式

为了能够在DM JDBC 驱动程序中访问这些特有的数据类型，我们在DmdbPreparedStatement、DmdbCallableStatement 和DmdbResultSet 类中增加了许多方法。客户如果想使用这些方法，必须把对象强制转化为DmdbXXX 类型：

PreparedStatement pstmt = connection.prepareStatement("insert into testInterval “ + “values(?)");

(DmdbPreparedStatement)pstmt.setIntervalYM(1, "Interval '0015-08' year to month");

int updateCount = pstmt.executeUpdate();

其它方法的使用方式与此类同。而且，时间间隔类型可以利用setString 和getString 方法进行存取，带纳秒的时间类型也可以当作普通的时间类型(不带纳秒)来进行操作。

## 4.5 建立JDBC 连接

通常有两种途径来获得JDBC 的连接对象，一种是通过驱动管理器DriverManager 的getConnection(String url, String user, String password)方法来建立，另外一种就是通过数据源的方式来建立。JDBC 3.0 支持这两种建立连接的方式。

### 4.5.1 通过DriverManager 建立连接

这种建立连接的途径是最常用的，也称作编程式连接。利用这种方式来建立连接通常需要以下几个步骤：

注册数据库驱动程序(driver)。可以通过调用java.sql.DriverManager 类的registerDriver方法显式注册驱动程序，也可以通过加载数据库驱动程序类隐式注册驱动程序。

//显示注册DriverManager.registerDriver(new dm.jdbc.driver.dmDriver());

//隐式注册Class.forName("dm.jdbc.driver.DmDriver");

## 第4 章 DM JDBC 编程指南

隐式注册过程中加载实现了java.sql.Driver 的类，该类中有一静态执行的代码段，在类加载的过程中向驱动管理器DriverManager 注册该类。而这段静态执行的代码段其实就是上述显式注册的代码。

建立连接。注册驱动程序之后，就可以调用驱动管理器的getConnection 方法来建立连接。建立数据库连接需要指定连接数据库的url、登录数据库所用的用户名user 和密码password。

通过DriverManager 建立连接的具体过程如下：

1. 加载DM JDBC 驱动程序

dm.jdbc.driver.DmDriver 类包含一静态部分，它创建该类的实例。当加载驱动程序时，驱动程序会自动调用DriverManager.registerDriver 方法向DriverManager 注册自己。通过调用方法Class.forName(String str)，将显式地加载驱动程序。以下代码加载DM 的JDBC 驱动程序：

Class.forName("dm.jdbc.driver.DmDriver");

2. 建立连接

加载DM JDBC 驱动程序并在DriverManager 类中注册后，即可用来与数据库建立连接。

DriverManager 对象提供三种建立数据库连接的方法。每种方法都返回一个Connection 对象实例，区别是参数不同。

Connection DriverManager.getConnection(String url, java.util.Properties info);

Connection DriverManager.getConnection(String url);

Connection DriverManager.getConnection(String url, String user, String password);

通常采用第三种方式进行数据库连接，该方法通过指定数据库url、用户名、口令来连接数据库。

以下代码建立与数据库的连接：

Class.forName("dm.jdbc.driver.DmDriver"); // 加载驱动程序String url = "jdbc:dm://223.254.254.19"; // 主库IP = 223.254.254.19 String userID = "SYSDBA";

String passwd = "SYSDBA";

Connection con = DriverManager.getConnection(url, userID, passwd);

利用这种方式来建立数据库连接，连接数据库所需要的参数信息都被硬编码到程序中，这样每次更换不同的数据库或登录用户信息都要对应用进行重新改写、编译，不够灵活。而且，当用户同时需要多个连接时，就不得不同时建立多个连接，造成资源浪费和性能低下。

为了解决这些问题，SUN 公司在JDBC 2.0 的扩展包中定义了数据源接口，提供了一种建立连接的新途径。

### 4.5.2 创建JDBC 数据源

数据源是在JDBC 2.0 中引入的一个概念。在JDBC 2.0 扩展包中定义了javax.sql.DataSource 接口来描述这个概念。如果用户希望建立一个数据库连接，通过查询在JNDITM 服务中的数据源，可以从数据源中获取相应的数据库连接。这样用户就只需要提供一个逻辑名称（Logic Name），而不是数据库登录的具体细节。

JNDITM 的全称是Java Naming and Directory Interface， 可以理解为Java 名称和目录服务接口。JNDI 向应用程序提供了一个查询和使用远程服务的机制。这些远程服务可以是任何企业服务。对于JDBC 应用程序来说，JNDI 提供的是数据库连接服务。JNDI 使应用程序

## 第4 章 DM JDBC 编程指南

通过使用逻辑名称获取对象和对象提供的服务，从而使程序员可以避免使用与提供对象的机构有关联的代码。

一个DataSource 对象代表一个实际的数据源。在数据源中存储了所有建立数据库连接的信息。系统管理员用一个逻辑名字对应DataSource 对象，这个名字可以是任意的。在下面的例子中DataSource 对象的名字是NativeDB。依照传统习惯, DataSource 对象的名字包含在jdbc/下，所以这个数据源对象的完整名字是：jdbc/NativeDB。

数据源的逻辑名字确定之后，就需要向JNDI 服务注册该数据源。下面的代码展示了向JNDI 服务注册数据源的过程。

// 初始化名称-目录服务环境Context ctx = null;

try{Hashtable env = new Hashtable (5);

env.put (Context.INITIAL_CONTEXT_FACTORY,"com.sun.jndi.fscontext.RefFSContextFactory");

env.put (Context.PROVIDER_URL, "file:JNDI");

ctx = new InitialContext(env);

}catch (NamingException ne){ne.printStackTrace();

}bind(ctx, "jdbc/NativeDB");

程序首先生成了一个Context 实例。javax.naming.Context 接口定义了名称服务环境(Naming Context)及该环境支持的操作。名称服务环境实际上是由名称和对象间的相互映射组成的。程序中初始化名称服务环境的环境工厂(Context Factory) 是com.sun.jndi.fscontext.RefFSContextFactory(该类在fscontext.jar 中可以找到，由于fscontext.jar中包含的不是标准的API，用户需要从www.javasoft.com 中的JNDI 专区下载fscontext.jar)类，环境工厂的作用是生成名称服务环境的实例。javax.naming.spi.InitialContextFactory 接口定义了环境工厂应该如何初始化名称服务环境(该接口在providerutil.jar 中实现，由于providerutil.jar 中包含的不是标准的API，用户需要从www.javasoft.com 中的JNDI 专区下载providerutil.jar)。在初始化名称服务环境时还需要定义环境的URL。程序中使用的是"file:JNDI"，也就是把环境保存在本地硬盘的JNDI 目录下。目前很多J2EETM 应用服务器都实现了自己的JNDI 服务，用户可以选用这些服务包。

初始化了名称服务环境后，就可以把数据源实例注册到名称服务环境中。注册时调用javax.naming.Context.bind()方法，参数为注册名称和注册对象。注册成功后，在JNDI 目录下会生成一个.binding 文件，该文件记录了当前名称-服务环境拥有的名称及对象。具体实现如下例所示：

void bind (Context ctx, String ln)throws NamingException, SQLException{// 创建一个DmdbDataSource 实例DmdbDataSource dmds = new DmdbDataSource ();

// 把DmdbDataSource 实例注册到JNDI 中ctx.bind (ln, dmds);

}

## 第4 章 DM JDBC 编程指南

当需要在名称服务环境中查询一个对象时，需要调用javax.naming.Context.lookup（）方法，并把查询到的对象显式转化为数据源对象。然后通过该数据源对象进行数据库操作。

DataSource ds = (DataSource) lookup (ctx, "jdbc/NativeDB");

Connection conn = ds.getConnection();

DataSource 对象中获得的Connection 对象和用DriverManager.getConnection 方法获得的对象是等同的。由于DataSource 方法具有很多优点，该方法成为获得连接的推荐方法。

### 4.5.3 数据源与连接池

利用数据源可以增强代码的可移植性，方便代码的维护。而且还可以利用连接池的功能来提高系统的性能。连接缓冲池的工作原理是：当一个应用程序关闭一个连接时，这个连接并不真正释放而是被循环利用。因为建立连接是消耗较大的操作，循环利用连接可以减少新连接的建立，能够显著地提高性能。

JDBC 规范为连接池定义了两个接口，一个客户端接口和一个服务器端接口。客户端接口就是javax.sql.DataSource，这样客户先前采用数据源来获得连接的代码就不需要任何的修改。通过数据源所获得的连接是否是缓冲的，这取决于具体实现的JDBC 驱动程序是否实现了连接池的服务器端接口javax.sql.ConnectionPoolDataSource。DM JDBC实现了连接缓冲池，在实现连接缓冲池的过程中采用了新水平的高速缓存。一般说来，连接高速缓存是一种在一个池中保持数目较小的物理数据库连接的方式，这个连接池由大量的并行用户共享和重新使用，从而避免在每次需要时建立一个新的物理数据库连接，以及当其被释放时关闭该连接的昂贵的操作。连接池的实现对用户来说是透明的，用户不需为其修改任何代码。

### 4.5.4 DM 扩展连接属性的使用

除了标准JDBC 接口功能，DM 扩展了一些具有自身特点的功能处理特性，这些特性可以通过在连接串上设置连接属性进行控制。

连接串的书写格式有以下两种：

1. host、port 不作为连接属性，此时只需输入值即可：

格式：

jdbc:dm [: //host][:port][?propName1=propValue1][& propName2=propValue2]….

注：

1） 若host 不设置，则默认为‘localhost’2） 若port 不设置，则默认为‘5236’3） 若host 不设置，则port 一定不能设4） 若user、password 没有单独作为参数传入，则必须在连接属性中传入5） 若host 为ipv6 地址，则应包含在[]中

例：

jdbc:dm://192.168.0.96:5236?LobMode=1

2. host、port 作为连接属性，此时必须按照上述列表中说明进行设置，且属性名称大小写

敏感格式：

jdbc:dm[?propName1=propValue1] [ & HOST=localhost][&…]…注：

## 第4 章 DM JDBC 编程指南

1） host、port 设置与否，以及在属性串中的位置没有限制2） 若user、password 没有单独作为参数传入，则必须在连接属性中传入

例：

jdbc:dm://HOST=192.168.0.96&PORT=5236

连接串中可以设置的属性及其说明见下表。

表4.1 JDBC 连接串属性是否必须设属性名称说明置主库地址，包括IP 地址、localhost 或者配置文件中主库地址“host” 是列表对应的变量名，如dm_svc.conf 中的’o2000’“port” 端口号，服务器登录端口号否“user” 登录用户是“password” 登录密码是“socketTimeout” 套接字超时时间，默认0 否是否进行语法转义处理，默认true，若确定使用环境中SQL语句不会存在需要转义处理的情况，可以将该属性设为“escapeProcess” 否false，在一定程度上提交操作效率；取值（true/True，false/False）“autoCommit” 是否自动提交，默认true；取值（true/True，false/False） 否“maxRows” 批量操作最大行数，默认0 否“rowPrefetch” 预取行数，默认10 否Lob 模式，默认1；取值（1 分批缓存到本地,2 一次将大字“LobMode” 否段数据缓存到本地）“StmtPoolSize” 语句句柄池大小，默认0 否“comOra” 是否与oracle 兼容，默认false；取值（true/True，false/False）否“ignoreCase” 是否忽略大小写，默认true，取值（true/True，false/False）否“alwayseAllowCommit” 在自动提交开关打开时，是否允许手动提交回滚否批处理类型，默认1，取值（1 进行批量绑定 2 不进行批“batchType” 否量绑定）“maxCachedPstmtSize” 缓存准备执行语句句柄的数量，默认0 否追踪级别，默认0（0 不记录、1 记录错误、 2 记录debug、“traceLevel” 否3 记录trace、 4 所有）“appName” 客户端应用程序名称否“sessionTimeout” 会话超时时间，默认0 否“isCompress” 是否压缩消息，默认false，取值（true/True，false/False） 否“sslFilesPath” 指定ssl 加密文件的路径否“sslKeystorePass” 指定ssl 加密文件的指令否指定默认创建结果集类型，1003—readonly，“resultSetType” 否1004—unsensitive，1005—insensitive，默认1003“kerberosLoginConfPath” Kerberors 认证登录配置文件路径否“mppLocal” 是否MPP 本地连接，默认false；取值（true/True，false/False） 否“rwSeparate” 是否使用读写分离系统，默认0；取值（0 不使用，1 使用）否

## 第4 章 DM JDBC 编程指南

分发到主库的事务占主备库总事务的百分比，有效值0~100，“rwPercent” 否默认25编目函数是否进行权限检测，默认false；取值（true/True，“dbmdChkPrv” 否false/False）是否使用列模式结果集，默认true；取值（true/True，“isBdtaRS” 否false/False）配置的连接服务名包含多个服务器时，连接是否均匀分布，“wellDistributed” 否默认false；取值（true/True，false/False）“uKeyName” Ukey 的用户名否“uKeyPin” Ukey 的口令否若使用服务名方式登录，且服务名配置了多个ip，当连接发“doSwitch” 生异常时是否自动切换；默认false；取值（true/True，否false/False）clob 类型列调用resultSetMetaData 的getColumnType()映射为“clobAsString” Types.VARCHAR 类型；默认false；取值（true/True，否false/False）批量执行出错时是否继续执行；默认false；取值（true/True，“continueBatchOnError” 否false/False）“connectTimeout” 连接数据库超时时间，单位ms， 默认0 否“columnNameUpperCase” 列名转换为大写字母，默认false；取值（true/True，false/False）否

## 4.6 Statement/Prepare Statement/Callable Statement

### 4.6.1 Statement

1. 概述

Statement 对象用于将SQL 语句发送到数据库服务器。DM JDBC 提供三种类型的语句对象：Statement，PreparedStatement，CallableStatement。其中PreparedStatement 是Statement的子类，CallableStatement 是PreparedStatement 的子类。每一种语句对象用来运行特定类型的SQL 语句。

Statement 对象用来运行简单类型的SQL 语句，语句中无需指定参数。

PreparedStatement 对象用来运行包含（或不包含）IN 类型参数的预编译SQL 语句。

CallableStatement 对象用来调用数据库存储过程。

2. 创建Statement 对象

建立连接后，Statement 对象用Connection 对象的createStatement 方法创建，以下代码创建Statement 对象：

Connection con = DriverManager.getConnection(url, "SYSDBA", "SYSDBA");

Statement stmt = con.createStatement();

3. 使用Statement 对象执行语句

Statement接口提供了三种执行SQL语句的方法：executeQuery、executeUpdate和execute。

方法 executeQuery 用于产生单个结果集的语句，例如 SELECT 语句。

## 第4 章 DM JDBC 编程指南

方法 executeUpdate 用于执行 INSERT、UPDATE 或 DELETE 语句以及 SQL DDL 语句，如 CREATE TABLE 和 DROP TABLE。INSERT、UPDATE 或 DELETE 语句的效果是修改表中零行或多行中的一列或多列。executeUpdate 的返回值是一个整数，表示受影响的行数。对于CREATE TABLE 或DROP TABLE 等DDL 语句，executeUpdate 的返回值总为零。

方法 execute 用于执行返回多个结果集、多个更新元组数或二者组合的语句。

执行语句的三种方法都将关闭所调用的Statement 对象的当前打开结果集（如果存在）。

这意味着在重新执行Statement 对象之前，需要完成对当前ResultSet 对象的处理。

4. 关闭 Statement 对象

Statement 对象可由Java 垃圾收集程序自动关闭。但作为一种良好的编程风格，应在不需要Statement 对象时显式地关闭它们。这将立即释放数据库服务器资源，有助于避免潜在的内存问题。

5. 性能优化调整

1) 批处理更新DM JDBC 驱动程序提供批处理更新的功能，通过批处理更新可以一次执行一个语句集合。JDBC 提供了三个方法来支持批处理更新：通过addBatch 方法，向批处理语句集中增加一个语句；通过executeBatch 执行批处理更新；通过clearBatch 来清除批处理语句集。

批处理更新过程中，如果出现执行异常，DM 将立即退出批处理的执行，同时返回已经被执行语句的更新元组数(在自动提交模式下)。

推荐批处理更新在事务的非自动提交模式下执行。同时，批处理更新成功后，需要主动提交以保证事务的永久性。

2) 性能优化参数设置DM JDBC 驱动程序提供了setFetchDirection、setFetchSize 来向驱动程序暗示用户操作语句结果集的缺省获取方向和一次获取的缺省元组数。这些值的设定可以为驱动程序优化提供参考。

6. 语句对象

JDBC 在创建语句对象时，可以指定语句对象的缺省属性：结果集类型和结果集并发类型。DM JDBC 驱动程序支持TYPE_FORWARD_ONLY 和TYPE_SCROLL_INSENSITIVE两种结果集类型，不支持 TYPE_SCROLL_SENSITIVE 结果集类型；支持CONCUR_READ_ONLY、CONCUR_UPDATABLE 两种结果集并发类型。

语句对象的缺省属性用来指定执行语句产生的结果集的缺省类型，其具体含义和用法参见5.7 节中“结果集增强特性部分”。

DM JDBC 驱动程序中当执行的查询语句涉及多个基表时，结果集不能更新，结果集的类型可能被自动转换为CONCUR_READ_ONLY 类型。

## 第4 章 DM JDBC 编程指南

### 4.6.2 PreparedStatement

1. 概述

PreparedStatement 继承 Statement，并与之在两方面有所不同：

1) PreparedStatement 对象包含已编译的 SQL 语句，语句已经“准备好”；

2) 包含于PreparedStatement 对象中的 SQL 语句可具有一个或多个 IN 参数。IN 参数的值在SQL 语句创建时未被指定。相反，该语句为每个 IN 参数保留一个问号（“?”）作为占位符。每个问号所对应的值必须在该语句执行之前，通过适当的setXXX 方法来提供。

由于 PreparedStatement 对象已预编译过，所以其执行速度要快于 Statement 对象。因此，需要多次重复执行的SQL 语句经常创建为PreparedStatement 对象，以提高效率。

作为 Statement 的子类，PreparedStatement 继承了Statement 的所有功能。另外它还添加了一整套方法，用于设置发送给数据库以取代IN参数占位符的值。同时，三种方法execute、executeQuery 和executeUpdate 能执行设置好参数的语句对象。

2. 创建 PreparedStatement 对象

以下的代码段（其中con 是 Connection 对象）创建一个PreparedStatement 对象：

PreparedStatement pstmt = con.prepareStatement("UPDATE person.person SET name = ? WHERE personid = ?");

对象pstmt 包含语句 "UPDATE person.person SET name = ? WHERE personid = ?"，该语句带两个IN 参数占位符，它已发送给数据库，并由服务器为其执行作好了准备。

3. 传递 IN 参数

在执行 PreparedStatement 对象之前，必须设置占位符（“?”）的值。这可通过调用setXXX方法来完成，其中XXX 是与该参数相应的类型。例如，如果参数具有Java 类型String，则使用的方法就是setString。setXXX 方法的第一个参数是要设置的参数的序号（从1 算起），第二个参数是设置给该参数的值。譬如，以下代码将第一个参数设为“张三”，第二个参数设为“18”：

pstmt.setString(1, "张三");

pstmt.setInt(2, 18);

每当设置了给定语句的参数值，就可执行该语句。设置一组新的参数值之前，应先调用clearParameters 方法清除原先设置的参数值。

4. 使用 setObject

setObject 方法可显式地将输入参数转换为特定的JDBC 类型。该方法可以接受三个参数，其中第三个参数用来指定目标JDBC 类型。将Java Object 发送给数据库之前，驱动程序将把它转换为指定的JDBC 类型。例如，上面的setXXX 语句就可以改写为：

pstmt.setObject(1, "张三", java.sql.Types.VARCHAR);

pstmt.setObject(2, 18, java.sql.Types.INTEGER);

如果没有指定JDBC 类型，驱动程序就会将Java Object 映射到其缺省的JDBC 类型，然后将它发送到数据库，这与常规的 setXXX 方法类似。在这两种情况下，驱动程序在将值发送到数据库之前，会将该值的Java 类型映射为适当的JDBC 类型。二者的差别在于setXXX 方法使用从Java 类型到JDBC 类型的标准映射，而setObject 方法使用从Java Object类型到JDBC 类型的映射。

## 第4 章 DM JDBC 编程指南

方法setObject 允许接受所有Java 对象，这使应用程序更为通用，并可在运行时接受参数的输入。这样，如果用户在编辑应用程序时不能确定输入类型，可以通过使用setObject，对应用程序赋予可接受的Java 对象，然后由JDBC 驱动程序自动将其转换成数据库所需的JDBC 类型。但如果用户已经清楚输入类型，使用相应的setXXX 方法是值得推荐的，可以提高效率。

5. 将 JDBC NULL 作为 IN 参数发送

setNull 方法允许程序员将JDBC NULL 值作为IN 参数发送给数据库。在这种情况下，可以把参数的目标JDBC 类型指定为任意值，同时参数的目标精度也不再起作用。

6. 发送大的 IN 参数

setBytes 和setString 方法能够发送无限量的数据。但是，内存要足够容纳相关数据。有时程序员更喜欢用较小的块传递大型的数据，这可通过将IN 参数设置为Java 输入流来完成。

当语句执行时，JDBC 驱动程序将重复调用该输入流，读取其内容并将它们当作实际参数数据传输。

JDBC 提供了四种将IN 参数设置为输入流的方法：setBinaryStream 用于字节流，setAsciiStream 用于ASCII 字符流，setUnicodeStream 用于Unicode 字符流，从JDK1.2 起，输入字符流的新方法为setCharacterStream，而setAsciiStream 和setUnicodeStream 已经很少用。

7. 获得参数元数据

DM JDBC 实现了getParameterMetaData()方法，通过这个方法可以获得有关IN 参数的各种属性信息，比如类型、精度、刻度等信息，类似于结果集元数据的内容。通过这些信息，用户可以更准确地设置IN 参数的值。

在下面的代码中涉及到了这种方法：

PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM person.person " + "WHERE personid= ?");

...

//获得参数元数据对象ParameterMetaData pmd = pstmt.getParameterMetaData();

//获得参数的个数int paramCount = pmd.getParameterCount();

//获得第一参数的类型int colType = pmd.getParameterType(1);

…

8. 自定义方法列表

为了实现对达梦数据库所提供的时间间隔类型和带纳秒的时间类型的支持，在实现PreparedStatement 接口的过程中，增加了一些自定义的扩展方法。用户将获得的PreparedStatement 对象反溯成DmdbPreparedStatment 类型就可以访问这些方法。这些方法所涉及到的扩展类请参看4.4 节。

表4.2 自定义方法列表方法名功能说明setINTERVALYM 设置参数为年-月时间间隔类型值setINTERVALDT 设置参数为日-时时间间隔类型值setTIME 设置参数为时间类型(带纳秒)

## 第4 章 DM JDBC 编程指南

例如，想要插入一个年月时间间隔类型，代码如下（pstmt 为PreparedStatement 类型）：

DmdbPreparedStatement dmps = (DmdbPreparedStatement)pstmt;

DmdbIntervalYM dmivm = new DmdbIntervalYM("20-10");

dmps.setINTERVALYM(1, dmiym);

另外，DM 中不支持JDBC 规范中所要求的标准方法setURL 和setRef。

### 4.6.3 CallableStatement

1. 概述

CallableStatement 用来运行SQL 存储过程。存储过程是数据库中已经存在的SQL 语句，它通过名字调用。

CallableStatement 是PreparedStatement 的子类。CallableStatement 中定义的方法用于处理 OUT 参数或 INOUT 参数的输出部分：注册OUT 参数的 JDBC 类型（一般SQL 类型）、从这些参数中检索结果，或者检查所返回的值是否为 JDBC NULL。

2. 创建 CallableStatement 对象

CallableStatement 对象是用 Connection.prepareCall 创建的。以下代码创建CallableStatement 对象，其中含有对存储过程p1 的调用，con 为连接对象：

CallableStatement cstmt = con.prepareCall("call p1(?, ?)");

其中"?"占位符为 IN、OUT 还是INOUT 参数，取决于存储过程p1。

3. IN 和 OUT 参数

将 IN 参数传给 CallableStatement 对象是通过 setXXX 方法完成的。该方法继承自PreparedStatement。所传入参数的类型决定了所用的setXXX 方法（例如，用 setString 来传入String 值等）。

如果存储过程返回OUT参数，则在执行CallableStatement对象之前必须先注册每个OUT参数的JDBC 类型，有的参数还要同时提供刻度。注册JDBC 类型是用registerOutParameter方法来完成的。语句执行完后，CallableStatement 的getXXX 方法将取回参数值。其中XXX是为各参数所注册的JDBC 类型所对应的Java 类型。换言之， registerOutParameter 使用的是JDBC 类型（因此它与数据库返回的JDBC 类型匹配），而getXXX 将之转换为Java 类型。

设存储过程p1 的定义如下：

CREATE OR REPLACE PROCEDURE p1( a1 IN VARCHAR(10), a2 OUT VARCHAR(50)) AS DECLARE CURSOR CUR1 FOR SELECT name FROM person.person WHERE personid = a1;

BEGIN OPEN CUR1;

FETCH CUR1 INTO a2;

END;

以下代码先注册OUT 参数，执行由cstmt 所调用的存储过程，然后检索通过OUT 参数返回的值。方法getString 从OUT 参数中取出字符串：

CallableStatement cstmt = con.prepareCall("call p1(?, ?)");

cstmt.setString(1, "1");

cstmt.registerOutParameter(2, java.sql.Types.VARCHAR);

cstmt.executeUpdate();

## 第4 章 DM JDBC 编程指南

String x = cstmt.getString(2);

4. INOUT 参数

如果参数为既接受输入又接受输出的参数类型（INOUT 参数），那么除了调用registerOutParameter 方法外，还要调用对应的setXXX 方法（继承自PreparedStatement）。

setXXX 方法将参数值设置为输入参数，而registerOutParameter 方法将它的JDBC 类型注册为输出参数。setXXX 方法提供一个Java 值，驱动程序先把这个值转换为JDBC 值，然后将它送到数据库服务器。

该IN 值的JDBC 类型和提供给registerOutParameter 方法的JDBC 类型应该相同。如果要检索输出值，就要用对应的getXXX 方法。

设有一个存储过程 p2 的定义如下：

CREATE OR REPLACE PROCEDURE p2(a1 IN OUT VARCHAR(10)) AS DECLARE CURSOR CUR1 FOR SELECT name FROM person.person WHERE personid = a1;

BEGIN OPEN CUR1;

FETCH CUR1 INTO a1;

END;

以下代码中，方法setString 把参数设为“1”。然后，registerOutParameter 将该参数注册为JDBC VARCHAR。执行完该存储过程后，将返回一个新的JDBC VARCHAR 值。方法getString 将把这个新值作为Java 的String 类型返回。

CallableStatement cstmt = con.prepareCall("call p2(?)");

cstmt.setString(1, "1");

cstmt.registerOutParameter(1, java.sql.Types.VARCHAR);

cstmt.executeUpdate();

String x = cstmt.getString(1);

5. 利用参数名进行操作

在通常的情况下一般采用参数索引来进行赋值。JDBC3.0 规范要求可以利用参数名来对参数进行赋值，DM JDBC 驱动程序实现了这一点。如果某个存储过程的一些参数有默认值，这时候采用参数名进行赋值就非常有用，用户可以只对那些没有默认值的参数进行赋值。参数名可以通过调用DatabaseMetaData.getProcedureColumns()来获得。

下面的代码中，存储过程p2 为上面那个存储过程p2。利用参数名进行操作：

CallableStatement cstmt = con.prepareCall("CALL p2 (?)");

cstmt.setString("a1", "1");

cstmt.registerOutParameter("a1", java.sql.Types.VARCHAR);

cstmt.executeUpdate();

String x = cstmt.getString("a1");

而且，在读取参数的值和进行参数注册的时候，setXXX、getXXX、registerOutParameter也都可以采用参数名来进行操作。通过调用DatabaseMetaData.supportsNamedParameters()方法就可以确定JDBC 驱动程序是否支持利用参数名来进行操作。

## 第4 章 DM JDBC 编程指南

在执行同一条语句的过程中，不允许交叉使用参数索引和参数名来进行操作，否则会抛出异常。

6. 自定义方法列表

为了实现对达梦数据库所提供的时间间隔类型和带纳秒的时间类型的支持，在实现CallableStatement 接口的过程中，增加了一些自定义的扩展方法。用户将获得的CallableStatement 对象反溯成DmdbCallableStatment 类型就可以访问这些方法。这些方法所涉及到的扩展类请参看4.4 DM JDBC 扩展这一节。

表4.3 自定义方法列表方法名功能说明

getINTERVALYM(int) 获得参数的值getINTERVALYM(String) 获得参数的值getINTERVALDT(int) 获得参数的值getINTERVALDT(String) 获得参数的值getTIME(int) 获得参数的值getTIME(String) 获得参数的值

setTIME(String,String) 根据参数名来设置DmdbTime 类型值。

setINTERVALDT(String,String) 根据参数名来设置DmdbIntervalDT 类型值。

setINTERVALYM(String,String) 设置参数为年-月时间间隔类型值

另外，DM 中不支持JDBC 规范中所要求的标准方法setURL、getURL 和getRef。由于CallableStatement 是PreparedStatement 的子类，因此，它将继承PreparedStatement 的所有的方法。

## 4.7 ResultSet

1. 概述

ResultSet 提供执行SQL 语句后从数据库返回结果中获取数据的方法。执行SQL 语句后数据库返回结果被JDBC 处理成结果集对象，可以用ResultSet 对象的next 方法以行为单位进行浏览，用getXXX 方法取出当前行的某一列的值。

通过Statement，PreparedStatement，CallableStatement 三种不同类型的语句进行查询都可以返回ResultSet 类型的对象。

2. 行和光标

ResultSet 维护指向其当前数据行的逻辑光标。每调用一次next 方法，光标向下移动一行。最初它位于第一行之前，因此第一次调用next 将把光标置于第一行上，使它成为当前行。随着每次调用next 导致光标向下移动一行，按照从上至下的次序获取 ResultSet 行。

在ResultSet 对象或对应的Statement 对象关闭之前，光标一直保持有效。

3. 列

## 第4 章 DM JDBC 编程指南

方法getXXX 提供了获取当前行中某列值的途径。在每一行内，可按任何次序获取列值。

列名或列号可用于标识要从中获取数据的列。例如，如果ResultSet 对象rs 的第二列名为“title”，则下列两种方法都可以获取存储在该列中的值：

String s = rs.getString("title");

String s = rs.getString(2);

注意列是从左至右编号的，并且从1 开始。

在DM JDBC 驱动程序中，如果列的全名为“表名.列名”的形式。在不引起混淆的情况下（结果集中有两个表具有相同的列名），可以省略表名，直接使用列名来获取列值。

关于ResultSet 中列的信息，可通过调用方法ResultSet.getMetaData 得到。返回的ResultSetMetaData 对象将给出其ResultSet 对象各列的名称、类型和其他属性。

4. NULL 结果值

要确定给定结果值是否是JDBC NULL，必须先读取该列，然后使用ResultSet 对象的wasNull 方法检查该次读取是否返回JDBC NULL，如下：

String sql="select * from person.person";

ResultSet rs;

rs = stmt.executeQuery(sql);

while (rs.next()){if(rs.wasNull())System.out.println("Get A Null Value");

}

当使用ResultSet 对象的getXXX 方法读取JDBC NULL 时，将返回下列值之一：

1) Java null 值：对于返回Java 对象的getXXX 方法（如getString、getBigDecimal、getBytes、getDate、getTime、getTimestamp、getAsciiStream、getUnicodeStream、getBinaryStream、getObject 等）；

2) 零值：对于getByte、getShort、getInt、getLong、getFloat 和 getDouble；

3) false 值：对于getBoolean。

5. 结果集增强特性

在DM JDBC 驱动程序中提供了符合JDBC 2.0 标准的结果集增强特性：可滚动、可更新结果集，及JDBC3.0 标准的可持有性。

1) 结果集的可滚动性通过执行语句而创建的结果集不仅支持向前（从第一行到最后一行）浏览内容，而且还支持向后（从最后一行到第一行）浏览内容的能力。支持这种能力的结果集被称为可滚动的结果集。可滚动的结果集同时也支持相对定位和绝对定位。绝对定位指的是通过指定在结果集中的绝对位置而直接移动到某行的能力，而相对定位则指的是通过指定相对于当前行的位置来移动到某行的能力。DM 支持可滚动的结果集。

DM JDBC 驱动程序中支持只向前滚结果集(ResultSet.TYPE_FORWARD_ONLY)和滚动不敏感结果集(ResultSet.TYPE_SCROLL_INSENSITIVE)两种结果集类型，不支持滚动敏感结果集(ResultSet.TYPE_SCROLL_SENSITIVE)。当结果集为滚动不敏感结果集时，它提供所含基本数据的静态视图，即结果集中各行的成员顺序、列值通常都是固定的。

2) 结果集的可更新性DM JDBC 驱动程序中提供了两种结果集并发类型：只读结果集(ResultSet.CONCUR_READ_ONLY)和可更新结果集(ResultSet.CONCUR_UPDATABLE)。采用只读并发类型的结果集不允许对其内容进行更新。可更新的结果集支持结果集的更新操

## 第4 章 DM JDBC 编程指南

作。

3) 结果集的可持有性JDBC 3.0 提供了两种结果集可持有类型：

提交关闭结果集(ResultSet.CLOSE_CURSORS_AT_COMMIT) 和跨结果集提交(ResultSet.HOLD_CURSORS_OVER_COMMIT)。采用提交关闭结果集类型的结果集在事务提交之后被关闭，而跨结果集提交类型的结果集在事务提交之后仍能保持打开状态。

通过DatabaseMetaData.supportsHoldability()方法可以确定驱动程序是否支持结果集的可持有性。目前DM 支持这两种类型。

4) 性能优化DM JDBC 驱动程序的结果集对象中提供了方法setFetchDirection和setFetchSize来设置缺省检索结果集的方向和缺省一次从数据库获取的记录条数。它们的含义与用法和语句对象中的同名函数是相同的。

6. 更新大对象数据

从DM JDBC 2.0 驱动程序就支持可更新的结果集，但是对LOB 对象只能读取，而不能更新，这也是JDBC 2.0 标准所规定的。而JDBC 3.0 规范规定用户可以对LOB 对象进行更新，DM JDBC 3.0 驱动程序中实现了这一点：

假设数据库中存在BOOKLIST 表，且含有id、comment 两个字段，建表语句如下：

CREATE TABLE BOOKLIST ("ID" INTEGER,"COMMENT" TEXT);

INSERT INTO SYSDBA.BOOKLIST VALUES (1, '测试数据');

Statement stmt = conn.createStatement(ResultSet.TYPE_FORWARD_ONLY,ResultSet.CONCUR_UPDATABLE);

ResultSet rs = stmt.executeQuery("select comment from booklist " +"where id = 1");

rs.next();

Clob commentClob = new Clob(...)；

rs.updateClob("author", commentClob); // commentClob is a Clob Object rs.updateRow();

7. 自定义方法列表

为了实现对达梦数据库所提供的时间间隔类型和带纳秒的时间类型的支持，在实现ResultSet 接口的过程中，增加了一些自定义的扩展方法。用户将获得的ResultSet 对象反溯成DmdbResultSet 类型就可以访问这些方法。这些方法所涉及到的扩展类请参看4.4 节。

表4.4 自定义方法列表方法名功能说明

getTime(int) 根据列号(1 开始)获取时间信息，以java.sql.Time 类型返回。

根据列号(1 开始)、Calendar 对象获取时间信息，getTime(int, Calendar)以java.sql.Time 类型返回。

getTime(String) 根据列名获取时间信息，以java.sql.Time 类型返回。

根据列名、Calendar 对象获取时间信息，getTime(String, Calendar)以java.sql.Time 类型返回。

getTimestamp(int) 根据列号(1 开始)获取时间信息，以java.sql.Timestamp 类型返回。

根据列号(1 开始)、Calendar 对象获取时间信息，getTimestamp(int, Calendar)以java.sql.Timestamp 类型返回。

getTimestamp(String) 根据列名获取时间信息，以java.sql.Timestamp 类型返回。

## 第4 章 DM JDBC 编程指南

根据列名、Calendar 对象获取时间信息，getTimestamp(String, Calendar)以java.sql.Timestamp 类型返回。

updateINTERVALYM(int,设置列为年-月时间间隔类型值DmdbIntervalYM )updateINTERVALYM(String,设置列为年-月时间间隔类型值DmdbIntervalYM)updateINTERVALDT(int,设置列为日-时时间间隔类型值DmdbIntervalDT)updateINTERVALDT(String,设置列为日-时时间间隔类型值DmdbIntervalDT)

另外，DM 中不支持getURL 和getRef 方法。

## 4.8 流与大对象

### 4.8.1 Stream 使用

为了获取大数据量的列，DM JDBC 驱动程序提供了四个获取流的方法：

1. getBinaryStream 返回只提供数据库原字节而不进行任何转换的流；
2. getAsciiStream 返回提供单字节 ASCII 字符的流；
3. getUnicodeStream 返回提供双字节 Unicode 字符的流；
4. getCharacterStream 返回提供双字节 Unicode 字符的java.io.Reader 流。

在这四个函数中，JDBC 规范不推荐使用getUnicodeStream 方法，其功能可以用getCharacterStream 代替。以下是采用其它三种方法获取流的示例代码：

1. 采用getBinaryStream 获取流

// 查询语句String sql = "SELECT description FROM production.product WHERE productid=1";

// 创建语句对象Statement stmt = conn.createStatement();

// 执行查询ResultSet rs = stmt.executeQuery(sql);

// 显示结果集while (rs.next()) {try {InputStream stream = rs.getBinaryStream("description");

ByteArrayOutputStream baos = new ByteArrayOutputStream();

int num = -1;

while ((num = stream.read()) != -1) {baos.write(num);

}System.out.println(baos.toString());

} catch (IOException e) {e.printStackTrace();

## 第4 章 DM JDBC 编程指南

}}// 关闭结果集rs.close();

// 关闭语句stmt.close();

2. 采用getAsciiStream 获取流

// 查询语句String sql = "SELECT description FROM production.product WHERE productid=1";

// 创建语句对象Statement stmt = conn.createStatement();

// 执行查询ResultSet rs = stmt.executeQuery(sql);

// 显示结果集while (rs.next()) {try {InputStream stream = rs.getAsciiStream("description");

StringBuffer desc = new StringBuffer();

byte[] b = new byte[1024];

for (int n; (n = stream.read(b)) != -1;) {desc.append(new String(b, 0, n));

}System.out.println(desc.toString());

} catch (IOException e) {e.printStackTrace();

}}// 关闭结果集rs.close();

// 关闭语句stmt.close();

3. 采用getCharacterStream 获取流

// 查询语句String sql = "SELECT description FROM production.product WHERE productid=1";

// 创建语句对象Statement stmt = conn.createStatement();

// 执行查询ResultSet rs = stmt.executeQuery(sql);

// 显示结果集while (rs.next()) {try {Reader reader = rs.getCharacterStream("description");

BufferedReader br = new BufferedReader(reader);

## 第4 章 DM JDBC 编程指南

String thisLine;

while ((thisLine = br.readLine()) != null) {System.out.println(thisLine);

}} catch (IOException e) {e.printStackTrace();

}}// 关闭结果集rs.close();

// 关闭语句stmt.close();

### 4.8.2 LOB 对象使用

1. 概述

JDBC 标准为了增强对大数据对象的操作，在JDBC 3.0 标准中增加了java.sql.Blob 和java.sql.Clob 这两个接口。这两个接口定义了许多操作大对象的方法，通过这些方法就可以对大对象的内容进行操作。

2. 产生Lob 对象

在ResultSet 和CallableStatement 对象中调用getBlob()和getClob()方法就可以获得Blob对象和Clob 对象：

Blob blob = rs.getBlob(1);

Clob clob = rs.getClob(2);

3. 设置Lob 对象

Lob 对象可以像普通数据类型一样作为参数来进行参数赋值，在操作PreparedStatement、CallableStatement、ResultSet 对象时使用：

PreparedStatement pstmt = conn.prepareStatement("INSERT INTO bio (image, text) " + "VALUES (?, ?)");

//authorImage is a Blob Object pstmt.setBlob(1, authorImage);

//authorBio is a Clob Object pstmt.setClob(2, authorBio);

在一个可更新的结果集中，也可以利用updateBlob(int,Blob)、updateBlob(String,Blob)和updateClob(int,Clob)、updateClob(String,Clob)来更新当前行。

4. 改变Lob 对象的内容

Lob 接口提供了方法让用户可以对Lob 对象的内容进行任意修改：

byte[] val = {0,1,2,3,4};

## 第4 章 DM JDBC 编程指南

Blob data = rs.getBlob("DATA");

int numWritten = data.setBytes(1, val); // 在指定的位置插入数据PreparedStatement ps = conn.prepareStatement("UPDATE datatab SET data = ?");

ps.setBlob("DATA", data);

ps.executeUpdate();

目前LOB 内容的更新和其当前所处的事务之间没有直接的联系。更新LOB 时，会直接写入到数据库中，即便当前事务最终回滚也不能恢复。

## 4.9 元数据

### 4.9.1 ResultSetMetaData

1. 概述

ResultSetMetaData 提供许多方法，用于读取ResultSet 对象返回数据的元信息。包括：

列名、列数据类型、列所属的表、以及列是否允许为NULL 值等，通过这些方法可以确定结果集中列的一些信息。

2. 创建结果集元数据对象

结果集元数据是用来描述结果集的特征，所以，需要首先执行查询获得结果集，才能创建结果集元数据对象。

3. 创建ResultSetMetaData 对象如下例所示：

假如有一个表TESTTABLE(no int,name varchar(10))，利用下面的代码就可以知道这个表的各个列的类型：

ResultSet rs = stmt.executeQuery("SELECT * FROM TESTTABLE");

ResultSetMetaData rsmd = rs.getMetaData();

for(int i = 1; i <= rsmd.getColumnCount(); i ++){String typeName = rsmd.getColumnTypeName(i);

System.out.println("第" + i + "列的类型为：" + typeName);

}

### 4.9.2 DatabaseMetaData

1. 概述

## 第4 章 DM JDBC 编程指南

DatabaseMetaData 提供了许多方法，用于获取数据库的元数据信息。包括：描述数据库特征的信息(如是否支持多个结果集)、目录信息、模式信息、表信息、表权限信息、表列信息、存储过程信息等。DatabaseMetaData 有部分方法以ResultSet 对象的形式返回结果，可以用ResultSet 对象的getXXX()方法获取所需的数据。

2. 创建数据库元数据对象

数据库元数据对象由连接对象创建。以下代码创建DatabaseMetaData 对象（其中con为连接对象）：

DatabaseMetaData dbmd = con.getMetaData();

利用该数据库元数据对象就可以获得一些有关数据库和JDBC 驱动程序的信息：

String databaseName = dbmd.getDatabaseProductName(); // 数据库产品的名称int majorVersion = dbmd.getJDBCMajorVersion(); // JDBC 驱动程序的主版本号String []types ={"TABLE"};

ResultSet tablesInfor = dbmd.getTables(null, null, "*TE%", types);

### 4.9.3 ParameterMetaData

1. 概述

参数元数据是JDBC 3.0 标准新引入的接口，它主要是对PreparedStatement、CallableStatement 对象中的占位符（“?”）参数进行描述，例如参数的个数、参数的类型、参数的精度等信息，类似于ResultSetMetaData 接口。通过引入这个接口，就可以对参数进行较为详细、准确的操作。

2. 创建参数元数据对象

通过调用PreparedStatement 或CallableStatement 对象的getParameterMetaData()方法就可以获得该预编译对象的ParameterMetaData 对象：

ParameterMetaData pmd = pstmt.getParameterMetaData();

然后就可以利用这个对象来获得一些有关参数描述的信息：

// 获取参数个数int paraCount = pmd.getParameterCount();

for(int i = 1; i <= paraCount; i ++) {// 获取参数类型System.out.println("The Type of Parameter("+i+") is " + ptmt.getParameterType(i));

// 获取参数类型名System.out.println("The Type Name of Parameter("+i+") is "+ ptmt.getParameterTypeName(i));

// 获取参数精度System.out.println("The Precision of Parameter("+i+") is " + ptmt.getPrecision(i));

// 获取参数是否为空System.out.println("Parameter("+i+") is nullable? " + ptmt.isNullable (i));

}

## 第4 章 DM JDBC 编程指南

## 4.10 RowSet

RowSet 接口扩展了标准java.sql.ResultSet 接口。RowSetMetaData 接口扩展了java.sql.ResultSetMetaData 接口。JDK 5.0 定义了5 个标准的 JDBCRowSet 接口，DM 实现了其中的CachedRowSet 和JdbcRowSet。

RowSet 对象可以建立一个与数据源的连接并在其整个生命周期中维持该连接，在此情况下，该对象被称为连接的Rowset。Rowset 还可以建立一个与数据源的连接，从其获取数据，然后关闭它。这种 Rowset 被称为非连接Rowset。非连接 Rowset 可以在断开时更改其数据，然后将这些更改发送回原始数据源，不过它必须重新建立连接才能完成此操作。相比较java.sql.ResultSet 而言，RowSet 的离线操作能够有效的利用计算机越来越充足的内存，减轻数据库服务器的负担，由于数据操作都是在内存中进行然后批量提交到数据源，灵活性和性能都有了很大的提高。RowSet 默认是一个可滚动，可更新，可序列化的结果集，而且它作为JavaBeans，可以方便地在网络间传输，用于两端的数据同步。

### 4.10.1 CachedRowSet

CachedRowSet 是非连接的RowSet，数据行均被缓冲至本地内存，但并未保持与数据库服务器的连接。Dm7JdbcDriver15.jar 和Dm7Jdbc16.jar 中dm.jdbc.rowset.DmdbCachedRowSet类是达梦对于接口javax.sql.rowset.CachedRowSet 的实现。

1．使用URL、用户名、密码和一个查询SQL 语句作为设置属性，创建一个DmdbCachedRowSet 对象。RowSet 使用execute 方法完成CachedRowSet 对象的填充。完成execute 方法执行后，可以像使用java.sql.ResultSet 对象方法一样，使用RowSet 对象返回、滚动、插入、删除或更新数据。

/* 创建DmdbCachedRowSet 对象示例 */String sql = "SELECT productid,name,author FROM production.product";

CachedRowSet crs = new DmdbCachedRowSet();

crs.setUrl("jdbc:dm://localhost:5236");

crs.setUsername("SYSDBA");

crs.setPassword("SYSDBA");

crs.setCommand(sql);

crs.execute();

while (crs.next()){System.out.println("productid: " + crs.getInt(1));

System.out.println("name: " + crs.getString(2));

System.out.println("author: " + crs.getString(3));

}

2、CachedRowSet 对象也可以通过调用populate 方法，使用一个已经存在的ResultSet对象填充。完成填充后，便可以像操作ResultSet 对象一样，返回、滚动、插入、删除或更新数据。

/* 使用populate 方法填充代码片段 */// 执行查询，获取ResultSet 对象

## 第4 章 DM JDBC 编程指南

String sql = "SELECT productid,name,author FROM production.product";

ResultSet rs = stmt.executeQuery(sql);

// 填充CachedRowSet CachedRowSet crs = new DmdbCachedRowSet();

crs.populate(rs);

3、其他功能特点创建一个CachedRowSet 的拷贝：

CachedRowSet copy = crs.createCopy();

创建一个CachedRowSet 的共享：

CachedRowSet shard = crs.createShared();

4、CachedRowSet 限制

- 仅支持单表查询，且无连接操作；
- 因数据缓存在内存，故不支持大数据块；
- 连接属性，如事务隔离级等，不能在填充（执行execute 或populate）后设置，因

为此时已经断开了与数据库服务器的连接，不能将这些属性设置到返回数据的同一个连接上。

### 4.10.2 JdbcRowSet

JdbcRowSet 是对ResultSet 对象的封装，是连接的RowSet。达梦关于JdbcRowSet 的实现是dm.jdbc.rowset.DmdbJdbcRowSet 类。DmdbJdbcRowSet 在Dm7JdbcDriver15.jar 和Dm7JdbcDriver16.jar 中实现标准接口javax.sql.rowset.JdbcRowSet。

JdbcRowSet 在其生命期中始终保持着与数据库服务器的连接。其所有调用操作，均渗透进对JDBC Connection、statement 和ResultSet 调用。而CachedRowSet 则不存在于打开数据库服务器的任何连接。

CachedRowSet 在其操作过程中不需要JDBC 驱动的存在，而JdbcRowSet 需要。但两者在填充RowSet 和提交数据修改的过程中，均需JDBC 驱动的存在。

/* 使用JdbcRowSet 接口示例 */String sql = "SELECT name,author,publisher FROM production.product";

JdbcRowSet jrs = new DmdbJdbcRowSet();

jrs.setUrl("jdbc:dm://localhost:5236");

jrs.setUsername("SYSDBA");

jrs.setPassword("SYSDBA");

jrs.setCommand(sql);

jrs.execute();

int numcolsSum = jrs.getMetaData().getColumnCount();

while (jrs.next()) {for (int i = 1; i <= numcolsSum; i++) {System.out.print(jrs.getString(i) + "\t");

}

## 第4 章 DM JDBC 编程指南

System.out.println();

}jrs.close();

## 4.11 分布式事务支持

DM 对分布式事务的支持是依据X/OPEN 分布式事务处理模型XA 规范实现的。

DM 数据库系统实现了X/OPEN DTP 模型中的RM 组件，通过JDBC 接口与第三方TM工具配合完成分布式事务处理。JDBC 标准中，对XA 协议进行了部分剪裁，仅支持TM 对RM 的单向调用，不允许RM 向TM 的动态注册。因此DM 系统对XA 协议的支持也仅为单向调用。

一个会话同时只能处理一个分支事务，一个分支事务同时也只能被一个会话绑定处理。

DM JDBC 接口提供了dm.jdbc.xa 包，其中的类实现JDBC 的XA 标准接口，包括：

javax.sql.XADataSource javax.sql.XAConnection javax.transaction.xa. XAResource javax.transaction.xa.Xid

### 4.11.1 XADataSource

1. 概述

XADataSource 是分布式连接的数据源，通过其可以获取分布式连接。

2. 获取分布式连接

XADataSource 提供了两个方法用于获取分布式连接：

public XAConnection getXAConnection() throws SQLException public XAConnection getXAConnection(String user, String password) throws SQLException

第一个方法取给数据源设置的用户名和口令进行连接并返回得到的分布式连接，第二个方法则可以给定用户名和口令。

### 4.11.2 XAConnection

1. 概述

XAConnection 是对分布式事务进行支持的对象。XAConnection 对象通常是以XAResource 对象的方式被纳入到分布式事务的管理中。

2. 获取XAResource 对象

XAConneciton 提供了 javax.transaction.xa.XAResource getXAResource() throws SQLException 方法用于获取该分布式连接对应的XAResource 对象，这个XAResource 对象将代表XAConnection 对象参加分布式事务的管理。

## 第4 章 DM JDBC 编程指南

### 4.11.3 XAResource

1. 概述

XAResource 对象是代表XAConnection 对象参与分布式事务管理的，真正对分布式事务进行操控的方法都在这个接口中实现。

2. 主要方法介绍

1) public void start(Xid xid, int flags) throws XAException该方法用于开始一个事务分支。第一个参数xid用于指定事务分支的id，第二个参数flags用于指明开始这个事务分支的方式，其合法值及意义如下：

TMJOIN：这个标志指名该事务分支将被合并到之前的具有相同xid 的事务分支上，如果资源管理器发现之前没有这个xid 的事务分支，则抛出异常。

TMRESUME：这个标志指明该事务分支将重新开始之前用TMSUSPEND 标志结束的一个事务分支。

TMNOFLAGS：当没有特殊操作而只是开始一个普通的事务分支时，将flags 置为TMNOFLAGS。

2) public void end(Xid xid, int flags) throws XAException该方法用于结束一个事务分支。第一个参数xid用于指定事务分支的id，第二个参数flags用于指明结束这个事务分支的方式，其合法值及意义如下：

TMSUSPEND：这个标志指明暂时终止该事务分支，之后该事务分支应该被用TMRESUME 重新开始或者用RMSUCCESS 或TMFAIL 正式结束。

TMSUCCESS：这个标志指明该事务分支成功结束。

TMFAIL：这个标志指明这个事务已经失败，则这个事务分支被资源管理器标记为只能回滚。

3) public int prepare(Xid xid) throws XAException该方法用来预提交一个事务分支。参数xid 用于指定事务分支的id。

可能的返回值有：

XA_OK：该标志表明预提交成功。

XA_RDONLY：该标志表明事务分支具有只读属性并已被提交。

错误码：预提交失败并返回具体的错误码对应不同的失败信息。

4) public void commit(Xid xid, boolean onePhase) throws XAException该方法用来提交一个事务分支。第一个参数xid 用于指定事务分支的id。第二个参数onePhase 用来指定是否进行一阶段提交。

5) public void rollback(Xid xid) throws XAException该方法用来回滚一个事务分支。参数xid 用户指定事务分支的id。

6) public boolean isSameRM(XAResource xares) throws XAException该方法用来判断指定的xares 与当前XAResource 对象是否是指向同一数据源的两个实例。

7) public Xid[] recover(int flag) throws XAException该方法用于返回资源管理器中所有已被预提交的事务分支的id。

flags 的合法值及意义为：

TMSTARTRSCAN | TMENDRSCAN：一次获取到所有的已预提交的事务分支的id。

TMSTARTRSCAN：开始扫描并返回已预提交的事务分支的id，如果资源管理器中

## 第4 章 DM JDBC 编程指南

的已预提交事务分支过多，可能返回的不是全部。

TMNOFLAGS：用于继续扫描已预提交的事务分支的id。使用这一标志时，之前应该已经用TMSTARTRSCAN 开始了扫描。

TMENDRSCAN：这个标志表明在此次扫描并返回对应的已预提交的事务分支的id后，结束此次扫描。

8) public void forget(Xid xid) throws XAException该方法用来“遗忘”一个自主完成的事务分支，这里的“遗忘”表示真正释放事务分支，之前即使一个事务分支已经自主完成，其事务分支对象仍然保留。对于非自主完成的事务分支使用此方法时将返回异常。

3. DM 扩展方法介绍

DmdbXAResource 在实现了标准接口定义的方法的基础上，还扩展实现了heurCommit()和heurRollback()方法。

1) public void heurCommit(Xid xid) throws XAException该方法用于自主提交一个事务分支。参数xid 用于指定事务分支的id。

2) public void heurRollback(Xid xid) throws XAException该方法用于自主回滚一个事务分支。参数xid 用于指定事务分支的id。

### 4.11.4 Xid

1. 概述

Xid 接口是X/Open 事务标识符XID 结构的Java 映射，由全局事务格式 ID、全局事务 ID和分支限定符构成。

2. 使用介绍

DmdbXid 提供了构造函数public DmdbXid(int fmtId, byte[] gTranId, byte[] bQual)throws XAException 供用户生成一个Xid 实例。

同时DmdbXid 也实现了Xid 标准接口中的三个用于获取XID 的格式标识符部分、XID的全局事务标识符部分作为字节数组和XID 的事务分支标识符部分作为字节数组的三个方法。

### 4.11.5 实例解析

以下是一个使用JDBC 的XA 接口用两阶段提交协议来提交一个事务分支的例子。

DmdbXADataSource xaDS;

XAConnection xaCon;

XAResource xaRes;

Xid xid;

Connection con;

Statement stmt;

int ret;

DmdbXADataSource xaDS = new DmdbXADataSource();

## 第4 章 DM JDBC 编程指南

/* 获取分布式连接 */xaCon = xaDS.getXAConnection("jdbc_user", "jdbc_password");

/* 获取代表分布式连接的XAResource 实例 */xaRes = xaCon.getXAResource();

con = xaCon.getConnection();

stmt = con.createStatement();

xid = new MyXid(100, new byte[]{0x01}, new byte[]{0x02});

try {/* 开始一个事务分支 */xaRes.start(xid, XAResource.TMNOFLAGS);

stmt.executeUpdate("insert into test_table values (100)");

/* 结束一个事务分支 */xaRes.end(xid, XAResource.TMSUCCESS);

/* 预提交该事务分支 */ret = xaRes.prepare(xid);

if (ret == XAResource.XA_OK) {/* 提交事务分支 */xaRes.commit(xid, false);

}}catch (XAException e) {e.printStackTrace();

}finally {stmt.close();

con.close();

xaCon.close();

}

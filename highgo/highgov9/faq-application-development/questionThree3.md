---
title: "数据库(V9)常见问题（应用开发类-Java）"
book: "应用开发类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionThree3.html"
tags:
  - highgo
  - highgo-v9
  - faq-application-development
---

## 数据库(V9)常见问题（应用开发类-Java）

测试环境：IntelliJ IDEA

## 2.1 准备 JDBC 驱动

V9 数据库安装后，驱动路径：

```bash
/home/highgo/hgdb-v9.0/interfaces/jdbc/hgdb-jdbc-v9.0.jar
```

## 2.2 导入驱动到 IDEA

1. 右击项目 → Open Modules Settings
2. 进入 Dependencies 标签页
3. 点击 + → 选择 hgdb-jdbc-v9.0.jar
4. 勾选驱动 → 点击 Apply → OK

## 2.3 连接测试代码

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class Test {
    public static void main(String args[]) {
        Connection c = null;
        Statement stmt = null;
        try {
            // 加载驱动
            Class.forName("org.postgresql.Driver");
            
            // 建立连接
            c = DriverManager.getConnection(
                "jdbc:postgresql://192.168.1.7:5866/highgo",
                "highgo",
                "Hello@123"
            );
            c.setAutoCommit(false);
            System.out.println("连接v9数据库成功!");
            
            // 执行查询
            stmt = c.createStatement();
            ResultSet rs = stmt.executeQuery("select * from test");
            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                int age = rs.getInt("age");
                String address = rs.getString("address");
                float salary = rs.getFloat("salary");
                System.out.printf("%d,%s,%d,%s,%.1f%n", id, name, age, address, salary);
            }
            rs.close();
            stmt.close();
            c.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## 运行结果

```
连接v9数据库成功!
1,test_1,25,北京,12.0
2,test_2,22,西宁,22.0
3,test_3,26,济南,33.0
查询数据成功!
```
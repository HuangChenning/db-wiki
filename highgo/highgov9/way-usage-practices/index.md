---
title: "列级透明加密配置方案"
book: "使用类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/way/index.html"
tags:
  - highgo
  - highgo-v9
  - way-usage-practices
---

## 瀚高数据库 V9.0.5 列级透明加密配置方案

---

## 文档信息

| 项目 | 内容 |
| --- | --- |
| **文档标题** | 瀚高数据库 V9.0.5 列级透明加密配置方案 |
| **适用版本** | V9.0.5 及以上版本 |
| **文档类型** | 技术配置方案 |
| **编写日期** | 2026年3月26日 |
| **关键字** | 列级加密、透明加密、数据安全、column\_encrypt、TDE |

---

## 一、出现背景

### 1.1 数据安全合规需求

随着《数据安全法》《个人信息保护法》等法规的实施，企业对敏感数据保护的要求日益严格。在实际业务场景中，经常遇到以下数据安全挑战：

- **敏感数据泄露风险** ：数据库中存储的身份证号、银行卡号、手机号等敏感信息需要加密保护
- **合规审计要求** ：等保2.0、GDPR等法规要求对敏感数据进行加密存储
- **内部人员风险** ：防止DBA或开发人员直接查看敏感数据
- **数据脱敏需求** ：生产环境数据需要加密后才能同步到测试环境

### 1.2 传统加密方案的局限性

| 方案 | 优点 | 缺点 |
| --- | --- | --- |
| **应用层加密** | 灵活性高 | 需要修改应用代码，工作量大 |
| **磁盘加密** | 对应用透明 | 数据库运行时数据在内存中仍是明文 |
| **数据库TDE** | 透明加密 | 粒度粗，整个表空间加密，性能影响大 |
| **列级加密（手动）** | 粒度细 | 需要修改SQL，维护复杂 |

### 1.3 解决方案概述

瀚高数据库 V9.0.5 基于 PostgreSQL 扩展机制，提供了 **透明列级加密（Transparent Column-Level Encryption）** 功能：

- **透明性** ：应用无需修改SQL，加密解密自动完成
- **列级粒度** ：可针对特定敏感列加密，不影响其他列
- **双层密钥** ：KEK（密钥加密密钥）+ DEK（数据加密密钥）架构
- **安全可靠** ：AES-256加密，支持密钥轮换

---

## 二、相关参数与组件

### 2.1 核心组件

| 组件 | 说明 |
| --- | --- |
| **column\_encrypt** | 列级加密扩展 |
| **pgcrypto** | 加密函数扩展（依赖） |
| **ENCRYPTED\_TEXT** | 加密文本数据类型 |
| **ENCRYPTED\_BYTEA** | 加密二进制数据类型 |

### 2.2 GUC 配置参数

| 参数名 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `encrypt.enable` | bool | on | 全局启用/禁用列加密 |
| `encrypt.mask_key_log` | bool | on | 在日志中掩码密钥材料 |
| `encrypt.key_version` | int | 1 | 密钥版本号（1-32767） |

### 2.3 核心函数

| 函数名 | 功能 |
| --- | --- |
| `register_cipher_key()` | 注册数据加密密钥 |
| `load_key()` | 加载密钥到会话 |
| `cipher_key_disable_log()` | 禁用密钥日志 |
| `cipher_key_enable_log()` | 启用密钥日志 |
| `cipher_key_reencrypt_data()` | 密钥轮换重新加密 |

---

## 三、配置步骤

### 3.1 环境准备

#### 3.1.1 确认数据库版本

```sql
-- 检查瀚高数据库版本
SELECT build_version();

-- 预期输出包含：HG Database Server x86_64 V9 05-0-0-4462-20251219-590-852b855-cf04a5c
```

#### 3.1.2 安装依赖

```bash
# 确保已安装 pgcrypto 扩展
# 瀚高 V9.0.5 默认已包含 pgcrypto
```

### 3.2 安装 column\_encrypt 扩展

#### 步骤1：获取扩展文件

```bash
# 从 GitHub 获取 column_encrypt 源码包
# 源码编译安装

# 解压到扩展目录
cd /home/highgo下
# 确认文件存在
ls -la column_encrypt*
# 应有：column_encrypt.control, column_encrypt--1.0.sql 等
# 编译安装
make
make install
```

#### 步骤2：配置 shared\_preload\_libraries

```bash
# 编辑 postgresql.conf
vi $PGDATA/postgresql.conf

# 添加或修改
shared_preload_libraries = 'gb18030_2022, liboracle_parser, ivorysql_ora, pg_object, ora_synonym, restricted_dba, pg_audit, sqlite_fdw, credcheck, hg_sysmac, pg_stat_statements, column_encrypt'
```

#### 步骤3：重启数据库

```bash
# 使用 highgo 用户执行
pg_ctl restart -D $PGDATA

# 或使用系统服务
systemctl restart hgdb-9.0.5
```

#### 步骤4：创建扩展

```sql
-- 连接到目标数据库
\c your_database

-- 创建扩展（需要超级用户权限）
CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE EXTENSION column_encrypt;

-- 验证安装
\dx

-- 应显示 column_encrypt 和 pgcrypto
```

### 3.3 密钥注册与配置

#### 步骤1：禁用日志（安全操作）

```sql
-- 先禁用查询日志，防止密钥出现在日志中
SELECT cipher_key_disable_log();
```

#### 步骤2：注册加密密钥

```sql
-- 注册数据加密密钥（DEK）
-- 参数说明：数据密钥, 算法, 主口令（KEK）
SELECT register_cipher_key(
    'my-secret-data-encryption-key-32bytes',  -- DEK：32字节随机字符串
    'aes',                                     -- 算法：AES
    'my-master-passphrase-for-kek'            -- KEK：主口令
);

-- 返回 1 表示成功
```

#### 步骤3：启用日志

```sql
SELECT cipher_key_enable_log();
```

### 3.4 创建加密表

#### 步骤1：加载密钥到会话

```sql
-- 每个新会话都需要加载密钥
SELECT cipher_key_disable_log();
SELECT load_key('my-master-passphrase-for-kek');
```

#### 步骤2：创建带加密列的表

```sql
-- 创建包含加密列的表
CREATE TABLE customer_info (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),                           -- 普通列，不加密
    phone VARCHAR(20),                           -- 普通列，不加密
    id_card ENCRYPTED_TEXT,                      -- 身份证号：加密存储
    bank_card ENCRYPTED_TEXT,                    -- 银行卡号：加密存储
    address TEXT,                                -- 普通列，不加密
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 创建索引（支持哈希索引）
CREATE INDEX idx_customer_id_card ON customer_info USING HASH (id_card);
```

#### 步骤3：插入数据（透明加密）

```sql
-- 插入数据，加密自动进行
INSERT INTO customer_info (name, phone, id_card, bank_card, address)
VALUES 
    ('张三', '13800138000', '110101199001011234', '6222021234567890123', '北京市朝阳区'),
    ('李四', '13900139000', '310101199002022345', '6222029876543210987', '上海市浦东新区');

-- 查询数据，解密自动进行
SELECT * FROM customer_info;

-- 输出：
-- id | name | phone       | id_card            | bank_card           | address     | create_time
-- ----+------+-------------+--------------------+---------------------+-------------+---------------
-- 1  | 张三 | 13800138000 | 110101199001011234 | 6222021234567890123 | 北京市朝阳区 | 2026-03-26...
-- 2  | 李四 | 13900139000 | 310101199002022345 | 6222029876543210987 | 上海市浦东新区 | 2026-03-26...
```

### 3.5 验证加密效果

#### 测试1：未加载密钥时查询

```sql
-- 新开一个会话，不加载密钥
\c your_database

-- 尝试查询
SELECT * FROM customer_info;

-- 预期结果：
-- ERROR: cannot decrypt data, because key was not set

-- 查看非加密列
SELECT id,name,phone,address,create_time FROM customer_info;
-- 预期结果：
-- id | name |    phone    |    address     |        create_time         
-- ----+------+-------------+----------------+----------------------------
--   1 | 张三 | 13800138000 | 北京市朝阳区   | 2026-03-30 17:25:04.806558
--   2 | 李四 | 13900139000 | 上海市浦东新区 | 2026-03-30 17:25:04.806558
```

#### 测试2：查看物理存储（加密状态）

```sql
-- 启用会话密钥解密
SELECT cipher_key_disable_log();
SELECT load_key('my-master-passphrase-for-kek');

-- 输出：加密列正常显示
SELECT * FROM customer_info;
-- 输出：
-- id | name | phone       | id_card            | bank_card           | address     | create_time
-- ----+------+-------------+--------------------+---------------------+-------------+---------------
-- 1  | 张三 | 13800138000 | 110101199001011234 | 6222021234567890123 | 北京市朝阳区 | 2026-03-26...
-- 2  | 李四 | 13900139000 | 310101199002022345 | 6222029876543210987 | 上海市浦东新区 | 2026-03-26...
```

---

## 四、影响范围控制

### 4.1 对应用程序的影响

| 影响项 | 说明 | 控制措施 |
| --- | --- | --- |
| **SQL兼容性** | 应用SQL无需修改 | 完全透明，无感知 |
| **数据类型** | 使用 ENCRYPTED\_TEXT 类型 | 建表时指定列类型 |
| **索引支持** | 仅支持哈希索引 | 等值查询走索引，范围查询需全表扫描 |
| **性能影响** | 加密/解密有CPU开销 | 建议仅加密敏感列，非敏感列保持明文 |

### 4.2 性能优化建议

#### 4.2.1 选择性加密

```sql
-- 推荐：仅加密敏感列
CREATE TABLE user_info (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),              -- 不加密：常用于查询条件
    email VARCHAR(100),                -- 不加密：常用于查询条件
    password_hash ENCRYPTED_TEXT,      -- 加密：敏感数据
    id_card ENCRYPTED_TEXT,            -- 加密：敏感数据
    phone ENCRYPTED_TEXT               -- 加密：敏感数据
);
```

#### 4.2.2 索引策略

```sql
-- 加密列支持哈希索引（等值查询）
CREATE INDEX idx_enc_hash ON table_name USING HASH (encrypted_column);

-- 不支持B-tree索引（范围查询会全表扫描）
-- 如果需要范围查询，考虑：
-- 1. 增加一个脱敏列用于查询
-- 2. 使用应用层加密
```

#### 4.2.3 连接池配置

```sql
-- 连接池初始化时加载密钥
-- 在连接池配置中添加初始化SQL

-- 例如 HikariCP：
-- connectionInitSql=SELECT cipher_key_disable_log(); SELECT load_key('passphrase');
```

### 4.3 备份恢复注意事项

| 场景 | 说明 |
| --- | --- |
| **物理备份** | 备份文件中是加密数据，安全 |
| **逻辑备份** | pg\_dump 导出的是密文 |
| **恢复后** | 需要重新加载密钥才能解密 |
| **跨库恢复** | 目标库需要相同的密钥配置 |

```bash
# 逻辑备份（备份的是密文）
pg_dump -U hgdbadmin -d your_db -t customer_info > backup.sql

# 恢复
psql -U hgdbadmin -d new_db < backup.sql

# 恢复后需要在新库注册密钥
```

---

## 五、局限性

### 5.1 功能限制

| 限制项 | 说明 |
| --- | --- |
| **索引类型** | 仅支持哈希索引，不支持B-tree/GiST/GIN |
| **查询类型** | 加密列不支持范围查询（> < BETWEEN） |
| **函数索引** | 不支持在加密列上创建函数索引 |
| **外键约束** | 加密列不支持作为外键引用 |
| **唯一约束** | 加密列不支持唯一约束 |

### 5.2 性能限制

| 场景 | 影响 | 建议 |
| --- | --- | --- |
| **大批量插入** | 加密CPU开销 | 批量插入时临时禁用加密（encrypt.enable=off） |
| **聚合查询** | 无法使用索引 | 避免对加密列做COUNT/DISTINCT等聚合 |
| **排序** | 无法使用索引 | 避免对加密列做ORDER BY |

### 5.3 使用场景建议

#### ✅ 适用场景

- 敏感字段存储（身份证号、银行卡号、密码等）
- 等值查询为主的场景（根据身份证号查用户）
- 数据脱敏需求（生产数据加密后同步到测试环境）

#### ❌ 不适用场景

- 需要范围查询的字段（日期范围、金额范围）
- 需要排序的字段
- 需要聚合统计的字段
- 外键关联字段

---

## 六、密钥轮换

### 6.1 密钥轮换场景

- 定期轮换（如每季度）
- 密钥泄露 suspected
- 人员离职
- 合规要求

### 6.2 密钥轮换步骤

```sql
-- 步骤1：禁用日志
SELECT cipher_key_disable_log();

-- 步骤2：存储旧密钥（用于解密）
SELECT enc_store_prv_key('old-data-key', 'aes');

-- 步骤3：存储新密钥（用于加密）
SELECT enc_store_key('new-data-key', 'aes');

-- 步骤4：重新加密所有数据
SELECT cipher_key_reencrypt_data('public', 'customer_info', 'id_card');
SELECT cipher_key_reencrypt_data('public', 'customer_info', 'bank_card');

-- 步骤5：更新存储的包装密钥
DELETE FROM cipher_key_table;
SELECT register_cipher_key('new-data-key', 'aes', 'new-master-passphrase');

-- 步骤6：清理会话内存
SELECT enc_rm_prv_key();
SELECT enc_rm_key();
SELECT cipher_key_enable_log();
```

### 6.3 轮换后验证

```sql
-- 加载新密钥
SELECT load_key('new-master-passphrase');

-- 验证数据可读
SELECT COUNT(*) FROM customer_info;

-- 验证密钥版本
SELECT encrypt.key_version;
```

---

## 七、最佳实践

### 7.1 安全规范

| 规范项 | 要求 |
| --- | --- |
| **密钥管理** | DEK和KEK分开管理，KEK由安全团队保管 |
| **密钥复杂度** | DEK至少32字节随机字符串 |
| **密钥存储** | 不要将密钥硬编码在应用代码中 |
| **日志保护** | 操作密钥前先执行 cipher\_key\_disable\_log() |
| **访问控制** | 限制 cipher\_key\_table 的访问权限 |

### 7.2 密钥管理方案

```bash
# 方案1：环境变量（推荐）
export DB_ENCRYPTION_KEY=$(cat /secure/path/to/key.txt)

# 应用启动时加载
# connectionInitSql=SELECT load_key(current_setting('app.encryption_key'));

# 方案2：密钥管理系统（KMS）
# 从KMS获取密钥，动态加载到会话
```

### 7.3 监控告警

```sql
-- 监控加密列访问情况
SELECT 
    schemaname,
    tablename,
    attname as column_name,
    n_tup_read,
    n_tup_fetch
FROM pg_statio_user_tables
JOIN pg_attribute ON pg_statio_user_tables.relid = pg_attribute.attrelid
WHERE atttypid = 'encrypted_text'::regtype;

-- 监控密钥加载情况
-- 可通过日志审计跟踪 load_key() 调用
```

### 7.4 故障排查

| 问题 | 原因 | 解决方案 |
| --- | --- | --- |
| cannot decrypt data | 未加载密钥 | 执行 load\_key() |
| cipher key is not correct | 密钥错误 | 检查KEK是否正确 |
| 查询性能慢 | 加密列无索引 | 创建哈希索引 |
| 备份无法恢复 | 密钥不匹配 | 确保目标库有相同密钥 |

---

## 八、参考信息

### 8.1 相关文档

- 瀚高数据库 V9.0.5 管理员指南
- PostgreSQL pgcrypto 扩展文档
- column\_encrypt 官方文档

### 8.2 相关参数速查

| 参数名 | 默认值 | 说明 |
| --- | --- | --- |
| encrypt.enable | on | 启用列加密 |
| encrypt.mask\_key\_log | on | 日志掩码 |
| encrypt.key\_version | 1 | 密钥版本 |

---

**文档版本**: V1.0  
**最后更新**: 2026年3月26日
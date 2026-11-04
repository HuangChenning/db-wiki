# db-wiki

**中文** · [English](README.md)

Oracle 与达梦数据库文档的 Markdown 阅读库，按版本和手册组织，方便查阅、全文检索与离线阅读。

从 [Oracle 19c](Oracle/Oracle19c/catalog.md) 或 [达梦 DM8](dameng/dm8/catalog.md) 开始，也可以直接按下方任务选择手册。

## 概述

面向数据库管理员与开发者，收录数据库概念、SQL、日常管理、性能调优、备份恢复及高可用等主题。章节保留来源信息，便于回到原文核对；Oracle 正文主要为英文，达梦正文主要为中文。

## 收录示例与版本入口

| 数据库版本 | 手册目录数 | 阅读入口 |
| --- | ---: | --- |
| Oracle 11g | 45 | [版本总目录](Oracle/Oracle11g/catalog.md) · [数据库概念](Oracle/Oracle11g/concepts/contents.md) |
| Oracle 12c | 12 | [版本总目录](Oracle/Oracle12c/catalog.md) · [数据库概念](Oracle/Oracle12c/concepts/contents.md) |
| Oracle 19c | 17 | [版本总目录](Oracle/Oracle19c/catalog.md) · [数据库概念](Oracle/Oracle19c/concepts/contents.md) |
| Oracle 21c | 23 | [版本总目录](Oracle/Oracle21c/catalog.md) · [数据库概念](Oracle/Oracle21c/concepts/contents.md) |
| 达梦 DM7 | 21 | [版本总目录](dameng/dm7/catalog.md) · [系统管理员手册](dameng/dm7/administrator/contents.md) |
| 达梦 DM8 | 56 | [版本总目录](dameng/dm8/catalog.md) · [系统管理](dameng/dm8/administrator/contents.md) |

例如，阅读 [Oracle 19c 数据库概念目录](Oracle/Oracle19c/concepts/contents.md)，再进入 [Introduction to Oracle Database](Oracle/Oracle19c/concepts/introduction-to-oracle-database.md)，即可查看完整章节；章节开头的 `source` 字段记录官方原文地址。

### 按任务查阅

以下 Oracle 链接以 **19c** 为例，其他版本请从对应总目录进入。

| 要解决的问题 | Oracle 19c | 达梦 DM8 |
| --- | --- | --- |
| 管理实例与数据库对象 | [管理员指南](Oracle/Oracle19c/administrators-guide/contents.md) | [系统管理员手册](dameng/dm8/administrator/contents.md) |
| 查询 SQL 语法与函数 | [SQL 语言参考](Oracle/Oracle19c/sql-language-reference/contents.md) | [SQL 语言手册](dameng/dm8/sql-language/contents.md) |
| 编写存储过程与程序块 | [PL/SQL 语言参考](Oracle/Oracle19c/pl-sql-language-reference/contents.md) | [SQL 程序设计](dameng/dm8/sql-programming/contents.md) |
| 分析性能与优化 SQL | [SQL 调优指南](Oracle/Oracle19c/sql-tuning-guide/contents.md) | [SQL 调优](dameng/dm8/administrator/sql-tuning.md) |
| 备份、还原与恢复 | [备份与恢复用户指南](Oracle/Oracle19c/backup-and-recovery-users-guide/contents.md) | [备份与还原](dameng/dm8/backup-restore/contents.md) |
| 查找参数与系统视图 | [数据库参考](Oracle/Oracle19c/reference/contents.md) | [动态视图](dameng/dm8/administrator/dynamic-management.md) |

## 查阅流程

1. **选版本**：从上方入口打开该版本的 `catalog.md`，按主题选手册。
2. **选章节**：打开手册目录中的 `contents.md`，按原书顺序定位内容。总目录中以反引号标注的路径，相对于该总目录所在文件夹。
3. **核对原文**：在章节开头查看 `version`、`doc_id`（如有）和 `source`，确认适用版本及来源。

## 快速开始

在 GitHub 上点击链接即可阅读，无需安装数据库。离线阅读时，先克隆仓库，再用支持 Markdown 的编辑器打开：

```bash
git clone https://github.com/HuangChenning/db-wiki.git
cd db-wiki
```

打开 `Oracle/Oracle19c/concepts/contents.md`，点击第一章即可开始阅读。

### 本地全文检索

安装了 [ripgrep](https://github.com/BurntSushi/ripgrep) 后，可在仓库根目录执行以下命令。用 `-g '*.md'` 限定正文文件，避免搜索图片等资源：

```bash
# 在 Oracle 19c 概念手册中查找事务相关章节
rg -l -i -g '*.md' 'transaction' Oracle/Oracle19c/concepts

# 在达梦备份手册中查找 DMRMAN，显示匹配行及行号
rg -n -g '*.md' 'DMRMAN' dameng/dm8/backup-restore
```

## 注意事项与收录限制

- **按版本使用**：不同版本的参数、语法与功能可能不同，不要直接将其他版本的示例用于当前环境。
- **收录范围有限**：这里是已整理手册的阅读入口，不代表厂商全部文档，也不保证与官网同步更新。在线手册与本地 PDF 的文档号差异，在部分版本总目录中已有注明。
- **保留正文语言**：中英文 README 提供同一套导航，并不表示所有章节均有双语译文。
- **转换格式可能有差异**：Markdown 由在线文档整理而来，复杂表格、图片和交叉链接可能存在格式或解析偏差；关键操作请核对章节中的官方来源。
- **来源与版权**：原始文档的版权归相应权利人所有。本仓库目前未提供 `LICENSE` 文件，请勿将文档收录理解为额外的授权声明。

## 贡献

提交问题时，请注明数据库版本、手册名、章节路径及具体问题；如涉及内容差异，请附上章节的 `source` 地址。补充或修订文档时，保持现有的版本目录、`catalog.md`、`contents.md` 和来源元数据，新增图片放在对应手册的 `img/` 下。

新增、删除或移动手册后，请同步更新总目录以及这两份 README 中的入口和手册目录数。

---
title: "DM PHP 编程指南"
book: "DM8 程序员手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/php-rogramming-guide.html
tags:
  - dameng
  - dm8
  - programmer
---

## 6.1 DM PHP 介绍

本章主要介绍 DM PHP 扩展的基本概念以及使用方法，以便于用户更好地使用 DM PHP 扩展库编写 PHP 应用程序。

在使用 PHP 语言的 Web 应用中，为了可以和 DM 数据库的服务器端进行通信，并且获得更快的速度以及对系统更强的控制，我们可以通过一个用 C 语言函数实现的瘦中间层来实现这个目标。该瘦中间层就是 PHP 扩展，它实现了一组 C 语言 API，成为 PHP 语言级别的函数调用。

DM PHP 是在 PHP 开放源码的基础上开发的一个动态扩展库，命名统一采用 dm 开头的小写英文字母方式，各个单词之间以下划线分割。PHP 应用程序可通过 DM PHP 扩展接口库访问 DM 数据库服务器。

### 6.1.1 PHP 5.x 扩展函数

下面列出 DM 提供的 PHP 5.x 扩展函数，并简要说明每个函数的功能。

<table><tbody><tr><td><b>序号</b></td><td><b>函数类型</b></td><td><b>扩展库接口函数</b></td><td><b>作用描述</b></td><td><b>PHP 7.x</b></td></tr><tr><td>1</td><td rowspan="6">连接相关</td><td>dm_connect</td><td>打开一个到DM服务器的连接</td><td>支持，但参数略有不同</td></tr><tr><td>2</td><td>dm_pconnect</td><td>打开一个到DM服务器的持久连接</td><td>支持，但参数略有不同</td></tr><tr><td>3</td><td>dm_close</td><td>关闭DM连接</td><td>支持（PHP 5.x返回dmbool，PHP 7.x返回void）</td></tr><tr><td>4</td><td>dm_set_connect</td><td>设置连接</td><td>PHP 7.x用 dm_setoption代替</td></tr><tr><td>5</td><td>dm_get_server_info</td><td>取得DM服务器信息</td><td>支持</td></tr><tr><td>6</td><td>dm_select_db</td><td>选择用于数据库查询的默认模式</td><td>支持，但参数略有不同</td></tr><tr><td>7</td><td>绑定参数</td><td>dm_prepare</td><td>准备一条语句</td><td>支持，但参数略有不同</td></tr><tr><td>8</td><td rowspan="3">执行</td><td>dm_execute</td><td>执行一条语句</td><td>支持，但功能和参数略有不同</td></tr><tr><td>9</td><td>dm_execute_ex</td><td>执行一条dm_prepare准备后的语句</td><td>PHP 7.x用dm_execute代替</td></tr><tr><td>10</td><td>dm_bind_array_by_name</td><td>将php的array变量绑定到指定变量名的位置上</td><td>支持</td><td>11</td><td rowspan="4">查询</td><td>dm_query</td><td>发送一条DM查询，并可执行</td><td>PHP 7.x用dm_exec代替（本扩展函数自PHP 5.5.0起已废弃）</td></tr><tr><td>12</td><td>dm_unbuffered_query</td><td>向DM发送一条SQL查询，并不获取和缓存结果的行</td><td>PHP 7.x用dm_exec代替</td></tr><tr><td>13</td><td>dm_more_query_no_result</td><td>执行一条无结果集的语句</td><td>PHP 7.x用dm_exec代替</td></tr><tr><td>14</td><td>dm_db_query</td><td>发送一条库的DM查询，并可执行，但库参数不起作用</td><td>PHP 7.x用dm_exec代替</td></tr><tr><td>15</td><td rowspan="7">结果集</td><td>dm_result</td><td>取得一行结果数据</td><td>支持，但功能和参数略有不同</td></tr><tr><td>16</td><td>dm_more_result</td><td>确定句柄上是否包含有多个结果集。如果有，则处理这些结果集</td><td>PHP 7.x用dm_next_result代替</td></tr><tr><td>17</td><td>dm_free_result</td><td>释放结果内存</td><td>支持</td></tr><tr><td>18</td><td>dm_num_rows</td><td>取得结果集中行的数目</td><td>支持</td></tr><tr><td>19</td><td>dm_num_fields</td><td>取得结果集中字段的数目</td><td>支持</td></tr><tr><td>20</td><td>dm_affected_rows</td><td>取得前一次DM操作所影响的记录行数</td><td>支持</td></tr><tr><td>21</td><td>dm_data_seek</td><td>移动内部结果的游标</td><td>PHP 7.x用 dm_fetch_row代替</td></tr><tr><td>22</td><td rowspan="6">Fetch结果集</td><td>dm_fetch_array</td><td>从结果集中取得一行作为关联数组，或数字数组，或二者兼有</td><td>支持，但功能和参数略有不同</td></tr><tr><td>23</td><td>dm_fetch_object</td><td>从结果集中取得一行作为对象</td><td>支持，但参数略有不同</td></tr><tr><td>24</td><td>dm_fetch_row</td><td>从结果集中取得一行作为枚举数组</td><td>支持，但功能和参数略有不同</td></tr><tr><td>25</td><td>dm_fetch_assoc</td><td>从结果集中取得一行作为关联数组</td><td>支持，但功能和参数略有不同</td></tr><tr><td>26</td><td>dm_fetch_field</td><td>从结果集中取得列信息并作为对象返回</td><td>支持</td></tr><tr><td>27</td><td>dm_fetch_length</td><td>取得结果集中每个输出的长度</td><td>PHP 7.x用dm_fetch_array代替</td></tr><tr><td>28</td><td rowspan="3">表元数据</td><td>dm_list_fields</td><td>列出DM结果中的字段</td><td>支持</td></tr><tr><td>29</td><td>dm_list_tables</td><td>列出DM数据库中的表</td><td>PHP 7.x用dm_tables代替</td></tr><tr><td>30</td><td>dm_tablename</td><td>取得表名</td><td>支持</td></tr><tr><td>31</td><td rowspan="7">列元数据</td><td>dm_field_flags</td><td>从结果中取得和指定字段关联的标志</td><td>支持</td></tr><tr><td>32</td><td>dm_field_len</td><td>返回指定字段的长度</td><td>支持</td></tr><tr><td>33</td><td>dm_field_name</td><td>取得结果中指定字段的字段名</td><td>支持</td></tr><tr><td>34</td><td>dm_field_seek</td><td>将结果集中的指针设定为制定的字段偏移量</td><td>PHP 7.x用 dm_fetch_field代替</td></tr><tr><td>35</td><td>dm_field_table</td><td>取得指定字段所在的表名</td><td>支持</td></tr><tr><td>36</td><td>dm_field_type</td><td>取得结果集中指定字段的类型</td><td>支持</td></tr><tr><td>37</td><td>dm_insert_id</td><td>取得上一步INSERT操作产生的ID</td><td>支持</td></tr><tr><td>38</td><td rowspan="2">错误</td><td>dm_error</td><td>返回上一个DM操作产生的文本错误信息</td><td>PHP 7.x用dm_errormsg代替</td></tr><tr><td>39</td><td>dm_errno</td><td>返回上一个DM操作中的错误信息的数字编码</td><td>PHP 7.x用dm_error代替</td></tr><tr><td>40</td><td rowspan="4">事务</td><td>dm_abort</td><td>回滚一个事务</td><td>PHP 7.x用dm_rollback代替</td></tr><tr><td>41</td><td>dm_commit</td><td>提交一个事务</td><td>支持</td></tr><tr><td>42</td><td>dm_autocommit</td><td>设置自动提交功能</td><td>支持</td></tr><tr><td>43</td><td>dm_begin_trans</td><td>开始一个事务</td><td>PHP 7.x用dm_autocommit代替</td></tr><tr><td>44</td><td rowspan="5">其他</td><td>dm_set_object_name_case</td><td>设置比较时的大小写方式</td><td>支持</td></tr><tr><td>45</td><td>dm_escape_string</td><td>转义一个字符串</td><td>支持</td></tr><tr><td>46</td><td>dm_ping</td><td>Ping一个服务器连接，如果参数缺省则重新连接</td><td>支持</td></tr><tr><td>47</td><td>dm_php_debug</td><td>开启后将保存后续执行的sql语句到指定文件中</td><td>不支持</td></tr><tr><td>48</td><td>dm_longreadlen</td><td>设置变长类型读取的最大长度，为0时表示读取全部</td><td>支持</td></tr></tbody></table>

### 6.1.2 PHP 7.x 扩展函数

下面列出 DM 提供的 PHP 7.x 扩展函数，并简要说明每个函数的功能。

<table><tbody><tr><td><b>序号</b></td><td><b>函数类型</b></td><td><b>扩展库接口函数</b></td><td><b>作用描述</b></td><td><b>PHP 5.x</b></td></tr><tr><td>1</td><td rowspan="12">兼容PHP 5.x的函数</td><td>dm_num_fields</td><td>取得结果集中字段的数目</td><td>支持</td></tr><tr><td>2</td><td>dm_free_result</td><td>释放结果内存</td><td>支持</td></tr><tr><td>3</td><td>dm_num_rows</td><td>取得结果集中行的数目</td><td>支持</td></tr><tr><td>4</td><td>dm_commit</td><td>提交一个事务</td><td>支持</td></tr><tr><td>5</td><td>dm_fetch_field</td><td>从结果集中取得列信息并作为对象返回</td><td>支持</td></tr><tr><td>6</td><td>dm_tablename</td><td>取得表名</td><td>支持</td></tr><tr><td>7</td><td>dm_field_table</td><td>取得指定字段所在的表名</td><td>支持</td></tr><tr><td>8</td><td>dm_field_flags</td><td>从结果中取得和指定字段关联的标志</td><td>支持</td></tr><tr><td>9</td><td>dm_escape_string</td><td>转义一个字符串</td><td>支持</td></tr><tr><td>10</td><td>dm_set_object_name_case</td><td>设置比较时的大小写方式</td><td>支持</td></tr><tr><td>11</td><td>dm_longreadlen</td><td>设置变长类型读取的最大长度，为0时表示读取全部</td><td>支持</td></tr><tr><td>12</td><td>dm_bind_array_by_name</td><td>将php的array变量绑定到指定变量名的位置上</td><td>支持</td></tr><tr><td>13</td><td rowspan="20">与PHP 5.x同名，但功能或参数略有不同</td><td>dm_get_server_info</td><td>取得DM服务器信息</td><td>支持，参数略有不同</td><td>14</td><td>dm_prepare</td><td>准备一条语句</td><td>支持，参数略有不同</td></tr><tr><td>15</td><td>dm_execute</td><td>执行一条准备过的语句</td><td>支持，功能和参数略有不同</td></tr><tr><td>16</td><td>dm_field_len/别名dm_field_precision</td><td>返回指定字段的长度</td><td>支持，参数略有不同</td></tr><tr><td>17</td><td>dm_field_name</td><td>取得结果中指定字段的字段名</td><td>支持，参数略有不同</td></tr><tr><td>18</td><td>dm_field_type</td><td>取得结果集中指定字段的类型</td><td>支持，参数略有不同</td></tr><tr><td>19</td><td>dm_fetch_array</td><td>指定行号从结果集中取得一行作为关联数组</td><td>支持，功能和参数略有不同</td></tr><tr><td>20</td><td>dm_fetch_row</td><td>从结果集中取得一行数据</td><td>支持，功能和参数略有不同</td></tr><tr><td>21</td><td>dm_fetch_object</td><td>从结果集中取得一行作为对象</td><td>支持，参数略有不同</td></tr><tr><td>22</td><td>dm_result</td><td>取得结果数据</td><td>支持，功能和参数略有不同</td></tr><tr><td>23</td><td>dm_connect</td><td>打开一个到DM服务器的连接</td><td>支持，功能和参数略有不同</td></tr><tr><td>24</td><td>dm_pconnect</td><td>打开一个到DM服务器的持久连接</td><td>支持，功能和参数略有不同</td></tr><tr><td>25</td><td>dm_error</td><td>返回上一个DM操作中的错误信息的数字编码</td><td>功能等价于dm_errno(PHP 5.x)</td></tr><tr><td>26</td><td>dm_close</td><td>关闭DM连接</td><td>支持，参数略有不同</td></tr><tr><td>27</td><td>dm_affected_rows</td><td>取得前一次DM操作所影响的记录行数</td><td>支持，参数略有不同</td></tr><tr><td>28</td><td>dm_insert_id</td><td>取得上一步INSERT操作产生的ID</td><td>支持，参数略有不同</td></tr><tr><td>29</td><td>dm_list_fields</td><td>列出DM结果中的字段</td><td>支持，参数略有不同</td></tr><tr><td>30</td><td>dm_fetch_assoc</td><td>从结果集中取得一行作为关联数组，可指定行号</td><td>支持，功能和参数略有不同</td></tr><tr><td>31</td><td>dm_select_db</td><td>选择用于数据库查询的默认模式</td><td>支持，功能和参数略有不同</td></tr><tr><td>32</td><td>dm_ping</td><td>Ping一个服务器连接</td><td>支持，参数略有不同</td></tr><tr><td>33</td><td rowspan="24">新增函数</td><td>dm_binmode</td><td>是否读取二进制类型</td><td></td></tr><tr><td>34</td><td>dm_close_all</td><td>关闭所有DM连接</td><td></td></tr><tr><td>35</td><td>dm_columns</td><td>获取指定表的所有列信息</td><td></td></tr><tr><td>36</td><td>dm_autocommit</td><td>设置自动提交功能</td><td></td></tr><tr><td>37</td><td>dm_cursor</td><td>获取游标信息</td><td></td></tr><tr><td>38</td><td>dm_errormsg</td><td>返回上一个DM操作产生的文本错误信息</td><td>功能等价于dm_error(PHP 5.x)</td></tr><tr><td>39</td><td>dm_exec/别名dm_do</td><td>准备并执行sql语句</td><td>功能等价于dm_execute(PHP 5.x)</td></tr><tr><td>40</td><td>dm_fetch_into</td><td>从结果集中取得一行作为一个数组</td><td></td></tr><tr><td>41</td><td>dm_field_scale</td><td>取得结果中指定字段的标度</td><td></td></tr><tr><td>42</td><td>dm_field_num</td><td>取得结果中字段的编号</td><td></td></tr><tr><td>43</td><td>dm_next_result</td><td>确定句柄上是否包含有多个结果集。如果有，则处理这些结果集</td><td></td></tr><tr><td>44</td><td>dm_result_all</td><td>获取全部结果集，并打印成html格式</td><td></td></tr><tr><td>45</td><td>dm_rollback</td><td>回滚</td><td>功能等价于dm_abort (PHP 5.x)</td></tr><tr><td>46</td><td>dm_setoption</td><td>调整语句和连接的属性配置</td><td>功能等价于dm_set_connect(PHP 5.x)</td></tr><tr><td>47</td><td>dm_specialcolumns</td><td>获取特殊列</td><td></td></tr><tr><td>48</td><td>dm_statistics</td><td>获取表及其索引的信息</td><td></td></tr><tr><td>49</td><td>dm_tables</td><td>获取指定模式所有表信息</td><td>功能等价于dm_list_tables(PHP 5.x)</td></tr><tr><td>50</td><td>dm_primarykeys</td><td>获取表的主键</td><td></td></tr><tr><td>51</td><td>dm_columnprivileges</td><td>列的权限</td><td></td></tr><tr><td>52</td><td>dm_tableprivileges</td><td>表的权限</td><td></td></tr><tr><td>53</td><td>dm_foreignkeys</td><td>获取表的外键</td><td></td></tr><tr><td>54</td><td>dm_procedures</td><td>获取所有过程名</td><td></td></tr><tr><td>55</td><td>dm_procedurecolumns</td><td>获取所有过程的参数名</td><td></td></tr></tbody></table>

### 6.1.3 PHP 8.x 扩展函数

下面列出 DM 提供的 PHP 7.x 扩展函数，并简要说明每个函数的功能。

<table><tbody><tr><td><b>序号</b></td><td><b>函数类型</b></td><td><b>扩展库接口函数</b></td><td><b>作用描述</b></td><td><b>PHP 7.x</b></td></tr><tr><td>1</td><td rowspan="43">兼容PHP 7.x的函数</td><td>dm_close</td><td>关闭DM连接</td><td>支持</td></tr><tr><td>2</td><td>dm_num_fields</td><td>取得结果集中字段的数目</td><td>支持</td></tr><tr><td>3</td><td>dm_field_len/别名dm_field_precision</td><td>返回指定字段的长度</td><td>支持</td></tr><tr><td>4</td><td>dm_field_name</td><td>取得结果中指定字段的字段名</td><td>支持</td></tr><tr><td>5</td><td>dm_field_type</td><td>取得结果集中指定字段的类型</td><td>支持</td></tr><tr><td>6</td><td>dm_free_result</td><td>释放结果内存</td><td>支持</td></tr><tr><td>7</td><td>dm_num_rows</td><td>取得结果集中行的数目</td><td>支持</td></tr><tr><td>8</td><td>dm_commit</td><td>提交一个事务</td><td>支持</td></tr><tr><td>9</td><td>dm_fetch_field</td><td>从结果集中取得列信息并作为对象返回</td><td>支持</td></tr><tr><td>10</td><td>dm_affected_rows</td><td>取得前一次DM操作所影响的记录行数</td><td>支持</td></tr><tr><td>11</td><td>dm_insert_id</td><td>取得上一步INSERT操作产生的ID</td><td>支持</td></tr><tr><td>12</td><td>dm_list_fields</td><td>列出DM结果中的字段</td><td>支持</td></tr><tr><td>13</td><td>dm_tablename</td><td>取得表名</td><td>支持</td></tr><tr><td>14</td><td>dm_field_table</td><td>取得指定字段所在的表名</td><td>支持</td></tr><tr><td>15</td><td>dm_field_flags</td><td>从结果中取得和指定字段关联的标志</td><td>支持</td></tr><tr><td>16</td><td>dm_get_server_info</td><td>取得DM服务器信息</td><td>支持</td></tr><tr><td>17</td><td>dm_escape_string</td><td>转义一个字符串</td><td>支持</td></tr><tr><td>18</td><td>dm_ping</td><td>Ping一个服务器连接</td><td>支持</td></tr><tr><td>19</td><td>dm_set_object_name_case</td><td>设置比较时的大小写方式</td><td>支持</td></tr><tr><td>20</td><td>dm_prepare</td><td>准备一条语句</td><td>支持</td></tr><tr><td>21</td><td>dm_execute</td><td>执行一条准备过的语句</td><td>支持</td></tr><tr><td>22</td><td>dm_fetch_array</td><td>指定行号从结果集中取得一行作为关联数组。在PHP 8.X中，从结果集中获取INT/BIGINT/TINYINT类型返回INT、获取浮点类型返回DOUBLE、获取其他类型返回STRING</td><td>支持</td></tr><tr><td>23</td><td>dm_fetch_row</td><td>从结果集中取得一行数据</td><td>支持</td></tr><tr><td>24</td><td>dm_fetch_object</td><td>从结果集中取得一行作为对象</td><td>支持</td></tr><tr><td>25</td><td>dm_result</td><td>取得结果数据</td><td>支持</td></tr><tr><td>26</td><td>dm_pconnect</td><td>打开一个到DM服务器的持久连接</td><td>支持</td></tr><tr><td>27</td><td>dm_error</td><td>返回上一个DM操作中的错误信息的数字编码</td><td>支持</td></tr><tr><td>28</td><td>dm_binmode</td><td>是否读取二进制类型</td><td>支持</td></tr><tr><td>29</td><td>dm_close_all</td><td>关闭所有DM连接</td><td>支持</td></tr><tr><td>30</td><td>dm_cursor</td><td>获取游标信息</td><td>支持</td></tr><tr><td>31</td><td>dm_errormsg</td><td>返回上一个DM操作产生的文本错误信息</td><td>支持</td></tr><tr><td>32</td><td>dm_exec/别名dm_do</td><td>准备并执行sql语句</td><td>支持</td></tr><tr><td>33</td><td>dm_fetch_into</td><td>从结果集中取得一行作为一个数组</td><td>支持</td></tr><tr><td>34</td><td>dm_field_scale</td><td>取得结果中指定字段的标度</td><td>支持</td></tr><tr><td>35</td><td>dm_field_num</td><td>取得结果中字段的编号</td><td>支持</td></tr><tr><td>36</td><td>dm_longreadlen</td><td>设置变长类型读取的最大长度，为0时表示读取全部</td><td>支持</td></tr><tr><td>37</td><td>dm_next_result</td><td>确定句柄上是否包含有多个结果集。如果有，则处理这些结果集</td><td>支持</td></tr><tr><td>38</td><td>dm_result_all</td><td>获取全部结果集，并打印成html格式</td><td>支持</td></tr><tr><td>39</td><td>dm_rollback</td><td>回滚</td><td>支持</td></tr><tr><td>40</td><td>dm_setoption</td><td>调整语句和连接的属性配置</td><td>支持</td></tr><tr><td>41</td><td>dm_specialcolumns</td><td>获取特殊列</td><td>支持</td></tr><tr><td>42</td><td>dm_select_db</td><td>选择用于数据库查询的默认模式</td><td>支持</td></tr><tr><td>43</td><td>dm_bind_array_by_name</td><td>将php的array变量绑定到指定变量名的位置上</td><td>支持</td></tr><tr><td>44</td><td rowspan="12">与PHP 7.x同名，但功能或参数略有不同</td><td>dm_connect</td><td>打开一个到DM服务器的连接</td><td>支持，但功能略有不同</td></tr><tr><td>45</td><td>dm_columns</td><td>获取指定表的所有列信息</td><td>支持，但参数取值略有不同</td></tr><tr><td>46</td><td>dm_statistics</td><td>获取表及其索引的信息</td><td>支持，但参数取值略有不同</td></tr><tr><td>47</td><td>dm_tables</td><td>获取指定模式所有表信息</td><td>支持，但参数取值略有不同</td></tr><tr><td>48</td><td>dm_primarykeys</td><td>获取表的主键</td><td>支持，但参数取值略有不同</td></tr><tr><td>49</td><td>dm_autocommit</td><td>设置自动提交功能</td><td>支持，但参数取值略有不同</td></tr><tr><td>50</td><td>dm_columnprivileges</td><td>列的权限</td><td>支持，但参数取值略有不同</td></tr><tr><td>51</td><td>dm_tableprivileges</td><td>表的权限</td><td>支持，但参数取值略有不同</td></tr><tr><td>52</td><td>dm_foreignkeys</td><td>获取表的外键</td><td>支持，但参数取值略有不同</td></tr><tr><td>53</td><td>dm_procedures</td><td>获取所有过程名</td><td>支持，但参数取值略有不同</td></tr><tr><td>54</td><td>dm_procedurecolumns</td><td>获取所有过程的参数名</td><td>支持，但参数取值略有不同</td></tr></tbody></table>

## 6.2 DM PHP 模块加载

目前 DM 支持的 PHP 版本为 PHP 5.2、5.3 、5.4 、5.5 、5.6，PHP 7.0、7.1、7.2、7.3、7.4 和 PHP 8.0、8.1、8.2、8.3、8.4、8.5，凝思操作系统只支持到 PHP 7.2，用户可根据自己安装的 PHP 版本选择对应的接口库。

PHP 从 PHP 5.1 版本开始附带了 PHP 数据对象（PHP Data Object，简称 PDO），PDO 扩展为 PHP 访问数据库定义了一个轻量级的一致性接口。利用 PDO 扩展，用户可使用相同的方法来查询获取不同数据库的数据。需要注意的是，PDO 扩展必须配合数据库的 PDO 驱动一起使用，才能成功访问相应的数据库。

下面的示例均以 PHP5.3 版本为例，如果版本不同，将 53 改为对应值即可。

### 6.2.1 linux 系统下 PHP 加载

linux 系统下的 PHP 加载分为两种方式：普通源码安装方式和 yum 安装方式。

普通源码安装下载的是源码包，编译安装过程可以设定参数，按照需求进行安装，并且安装的版本可以选择，灵活性比较大。

yum 安装下载的是 rpm 软件包，安装 rpm 包。这个 rpm 包是别人编译安装好的二进制包，安装方便快捷，但是安装过程无法干预，不能按需安装。因此，安装之后，要根据实际情况再进行局部功能调整。

Linux 系统下 PDO 接口依赖的动态链接库为 libdmdpi.so。上述动态链接库在 DM 安装目录的/bin 目录下，使用时须配置 dmdbms/bin 目录为动态依赖库。该动态链接库也存放在发版 drivers 目录的/dpi 目录下，使用时须配置 drivers/dpi 目录为动态依赖库。

#### 6.2.1.1 普通源码安装

**步骤：**

1. 下载并安装 apache

从网络中下载 apache-2.0.48.tar.gz。存至/home/tmp。

```
cd /home/tmp
tar -xvzf apache-2.0.48.tar.gz  -C/usr/local
cd /usr/local/apache-2.0.48
./configure --prefix=/usr/local/apache  --enable-module=so
make
make install
cd /usr/local/apache/conf
vi httpd.conf
ServerName localhost
port 80
DirectoryIndex default.php default.phtml default.php3 default.html default.htm 
AddType application/x-httpd-php .php .phtml .php3 .inc 
AddType application/x-httpd-php-source .phps
```
2. 下载并安装 PHP

从网络中下载最新 php-5.3.tar.gz 。存至/home/tmp。

```
cd /home/tmp
tar -xvzf php-x.x.x.tar.gz  /usr/local
cd /usr/local/php-x.x.x
./buildconf --force
./configure --with-apache2=/usr/local/apache/bin/apxs
make 
make install
cp php.ini-dist /usr/local/lib/php.ini
```
3. 安装 DM DBMS

假定安装到/usr/local/DMDBMS 目录。

4. 配置 DM PHP

修改 php.ini，添加 extension\_dir=drivers/php\_pdo，extension=libphp53\_dm.so，添加 php.ini 中有关连接的配置。设置环境变量 export  
LD\_LIBRARY\_PATH=/usr/local/DMDBMS/bin，或者设置为依赖文件 libdmdpi.so 存放的路径。

#### 6.2.1.2 yum 方式安装

**步骤：**

1. 安装 epel
```
yum install epel-release
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
```
2. 安装 PHP
```
yum install php72w
```
3. 安装必需扩展和 pdo 扩展
```
yum install php72w-cli
yum install php72w-pdo
```
4. 查看版本
```
php -v
PHP 7.2.27 (cli) (built: Jan 26 2020 15:49:49) ( NTS )
Copyright (c) 1997-2018 The PHP Group
Zend Engine v3.2.0, Copyright (c) 1998-2018 Zend Technologies
```
5. 修改配置文件/etc/php.ini

配置 PDO 的数据库扩展，需要 PDO 的支持。

因为 PDO 必须在具体的数据库扩展被载入前初始化，而 congifuge/make&makestall 配置编译安装会默认启用自带的 PDO 模块，yum 共享模块安装不会启用，所以要在配置具体的 dm 数据库 pdo 扩展前配置 pdo.so。

```
extension=pdo.so
extension=php72_pdo_dm.so
extension=libphp53_dm.so
```
6. 拷贝驱动至目录 /usr/lib64/php/modules
7. 设置 LD\_LIBRARY\_PATH
```
export LD_LIBRARY_PATH=/home/ATS/smoke_47570/dm7dev2/build/linux/linux_build/debug
```
8. 查看是否成功加载了 DM PHP
```
php –m
[PHP Modules]
Core
ctype
date
DM
dom
fileinfo
filter
hash
iconv
json
libxml
pcre
PDO
PDO_DM
Phar
posix
Reflection
session
SimpleXML
SPL
sqlite3
standard
tokenizer
xml
xmlreader
xmlwriter
```

### 6.2.2 Windows 系统下加载 PHP 模块

**步骤：**

1. 下载 apache 的 windows 版本并安装，同时修改 httpd.conf。
2. 下载 PHP 并安装。
3. 安装 DM DBMS。
4. 配 DM PHP。拷贝 drivers\\php\_pdo 目录下 php53\_dm.dll 到 php 目录下的 ext 目录中，修改 php.ini，添加 extension=php53\_dm.dll，添加 php.ini 中有关连接的配置；在环境变量 PATH 中添加 dmdbms\\bin 所在的目录。php53\_dm.dll 中 PDO 类和 PDOStatement 类支持的接口和 libphp53\_dm.so 一样。
5. 重启 apache 服务器，在浏览器中输入 http:\\\\localhost\\php\_info.php 查看是否有 dm 模块项，如有说明加载 DM PHP 成功。

Windows 系统下 PDO 接口依赖的动态链接库如下：dmdpi.dll、dmclientlex.dll、dmutl.dll、dmstrt.dll、dmshm.dll、dmos.dll、dmmsg.dll、dmmout.dll、dmmem.dll、dmelog.dll、dmdta.dll、dmdcr.dll、dmcyt.dll、dmcvt.dll、dmcpr.dll、dmcomm.dll、dmcfg.dll、dmcalc.dll。上述动态链接库在 DM 安装目录的\\bin 目录下。

### 6.2.3 PHP INI 文件和 PDO 相关类介绍

php.ini 中可以配置的参数如下表所示：

| **参数** | **说明** | **配置示例** |
| --- | --- | --- |
| dm.default\_host | DM 连接默认 ip、port 和模式名 | dm.default\_host =192.168.0.25:6237:PHPTEST |
| dm.default\_user | DM 连接默认用户名 | dm.default\_user =SYSDBA |
| dm.default\_pw | DM 连接默认密码 | dm.default\_pw =sysDBA\*00 |
| extension\_dir | DM 依赖库路径 | extension\_dir=D:\\php-7.1.32-nts-Win32-VC14-x64\\ext |
| extension | DM 依赖库名称 | extension=php71nts\_dm.dll |
| dm.defaultlrl | Clob 类型读取的默认长度，单位为 BYTE，取值范围 1~2147483648，即 1~2GB；0：读取全部内容。缺省为 0 | dm.defaultlrl = 32767 |
| dm.defaultbinmode | 二进制数据处理方式，0：省略；1：按照实际返回；2：转换到字符。缺省为 1 | dm.defaultbinmode = 1 |
| dm.connect\_timeout | 数据库驱动与服务器建立 TCP 连接的超时时间，单位 s。缺省为 0 | dm.connect\_timeout = 10 |
| dm.max\_links | 最大连接数，缺省为-1，即最大连接数无限制 | dm.max\_links = 3 |
| dm.max\_persistent | 持久连接的最大数，缺省为-1，即最大持久连接数无限制 | dm.max\_persistent = 3 |
| dm.allow\_persistent | 允许或禁止持久连接，1：允许持久连接；0：禁止持久连接。缺省为 1 | dm.allow\_persistent = 1 |
| dm.check\_persistent | 在重用前检查连接是否还可用，1：检查；0：不检查。缺省为 1 | dm.check\_persistent = 1 |
| dm.fetch\_number | 设置 dmphp7 和 dmphp8 中 dm\_fetch\_array 获取 NUMBER 类型数据的返回类型，0：返回 DOUBLE；1：返回 STRING。缺省为 0 | dm.fetch\_number = 1 |
| dm.quote\_replace | 是否将 SQL 语句中的双引号改成单引号；0：否；1：是。 缺省为 0 | dm.quote\_replace = 1 |
| dm.ukey\_login | 设置 dmphp 连接时是否使用 ukey 的形式登录。0：不适用 ukey。1：使用 ukey。缺省为 0 | dm.ukey\_login = 1 |
| dm.extra\_decimal | 设置 dmphp7 和 dmphp8 中 dm\_fetch\_array 获取 NUMBER 类型数据的返回值是否展示小数点末尾的零。该参数仅在 dm.fetch\_number = 1 时生效。 0：省略末尾的 0；1：展示末尾的 0。缺省为 0 | dm.fetch\_number = 1 dm.extra\_decimal = 1 |
| dm.ssl\_login | 设置 dmphp 连接时是否使用 SSL 协议连接。0：不使用 SSL。1：使用 SSL。缺省为 0 | dm.ssl\_login = 1 |

PDO 类和 PDOStatement 类共支持 34 个接口：

<table><colgroup><col width="72"> <col width="556"> <col width="612"></colgroup><tbody><tr height="20"><td height="20" width="72"><b>类名</b></td><td width="72"><b>序号</b></td><td width="556"><b>接口名</b></td><td width="612"><b>释义</b></td></tr><tr height="20"><td rowspan="15" height="300">PDO <font>类</font></td><td>1</td><td>PDO::beginTransaction</td><td>启动一个事务</td></tr><tr height="20"><td height="20">2</td><td>PDO::commit</td><td>提交一个事务</td></tr><tr height="20"><td height="20">3</td><td>PDO::__construct</td><td>创建一个表示数据库连接的 PDO 实例。如果使用SSL协议连接，则可以通过连接属性PDO::SSL_PATH和PDO::SSL_PWD来设置SSL证书路径和密码。如果要展示NUMBER类型返回值小数点末尾的0，需要设置PDO::ATTR_STRINGIFY_FETCHES=>true，PDO::EXTRA_DECIMAL=>1。<br>在PDO 8.5中，以下DM属性需通过PDO\Dm::方式调用：PDO\Dm::SSL_PATH、PDO\Dm::SSL_PWD、PDO\Dm::EXTRA_DECIMAL、PDO\Dm::CHARSET</td></tr><tr height="20"><td height="20">4</td><td>PDO::errorCode</td><td>获取跟数据库句柄上一次操作相关的 <font>SQLSTATE</font></td></tr><tr height="20"><td height="20">5</td><td>PDO::errorInfo</td><td>获取最后一次操作数据库句柄的扩展错误信息</td></tr><tr height="20"><td height="20">6</td><td>PDO::exec</td><td>执行一条 <font>SQL</font> <font>语句，并返回受影响的行数</font></td></tr><tr height="20"><td height="20">7</td><td>PDO::getAttribute</td><td>取回一个数据库连接的属性</td></tr><tr height="20"><td height="20">8</td><td>PDO::getAvailableDrivers</td><td>返回一个可用驱动的数组</td></tr><tr height="20"><td height="20">9</td><td>PDO::inTransaction</td><td>检查是否在一个事务内</td></tr><tr height="20"><td height="20">10</td><td>PDO::lastInsertId</td><td>返回最后插入行的 <font>ID</font></td></tr><tr height="20"><td height="20">11</td><td>PDO::prepare</td><td>准备要执行的语句，并返回语句对象</td></tr><tr height="20"><td height="20">12</td><td>PDO::query</td><td>执行 <font>SQL</font> <font>语句，以</font> <font>PDOStatement</font> <font>对象形式返回结果集</font></td></tr><tr height="20"><td height="20">13</td><td>PDO::quote</td><td>为 <font>SQL</font> <font>查询里的字符串添加引号</font></td></tr><tr height="20"><td height="20">14</td><td>PDO::rollBack</td><td>回滚一个事务</td></tr><tr height="20"><td height="20">15</td><td>PDO::setAttribute</td><td>设置属性</td></tr><tr height="20"><td rowspan="19" height="380">PDOStatement <font>类</font></td><td>16</td><td>PDOStatement::bindColumn</td><td>绑定一列到一个 <font>PHP</font> <font>变量</font></td></tr><tr height="20"><td height="20">17</td><td>PDOStatement::bindParam</td><td>绑定一个参数到指定的变量名</td></tr><tr height="20"><td height="20">18</td><td>PDOStatement::bindValue</td><td>把一个值绑定到一个参数</td></tr><tr height="20"><td height="20">19</td><td>PDOStatement::closeCursor</td><td>关闭游标，使语句能再次被执行。</td></tr><tr height="20"><td height="20">20</td><td>PDOStatement::columnCount</td><td>返回结果集中的列数</td></tr><tr height="20"><td height="20">21</td><td>PDOStatement::debugDumpParams</td><td>打印一条 <font>SQL</font> <font>预处理命令</font></td></tr><tr height="20"><td height="20">22</td><td>PDOStatement::errorCode</td><td>获取跟上一次语句句柄操作相关的 <font>SQLSTATE</font></td></tr><tr height="20"><td height="20">23</td><td>PDOStatement::errorInfo</td><td>获取跟上一次语句句柄操作相关的扩展错误信息</td></tr><tr height="20"><td height="20">24</td><td>PDOStatement::execute</td><td>执行一条预处理语句</td></tr><tr height="20"><td height="20">25</td><td>PDOStatement::fetch</td><td>从结果集中获取下一行</td></tr><tr height="20"><td height="20">26</td><td>PDOStatement::fetchAll</td><td>返回一个包含结果集中所有行的数组</td></tr><tr height="20"><td height="20">27</td><td>PDOStatement::fetchColumn</td><td>从结果集中的下一行返回单独的一列。</td></tr><tr height="20"><td height="20">28</td><td>PDOStatement::fetchObject</td><td>获取下一行并作为一个对象返回。</td></tr><tr height="20"><td height="20">29</td><td>PDOStatement::getAttribute</td><td>检索一个语句属性</td></tr><tr height="20"><td height="20">30</td><td>PDOStatement::getColumnMeta</td><td>返回结果集中一列的元数据</td></tr><tr height="20"><td height="20">31</td><td>PDOStatement::nextRowset</td><td>在一个多行集语句句柄中推进到下一个行集</td></tr><tr height="20"><td height="20">32</td><td>PDOStatement::rowCount</td><td>返回受上一个 <font>SQL</font> <font>语句影响的行数</font></td></tr><tr height="20"><td height="20">33</td><td>PDOStatement::setAttribute</td><td>设置一个语句属性</td></tr><tr height="20"><td height="20">34</td><td>PDOStatement::setFetchMode</td><td>为语句设置默认的获取模式</td></tr></tbody></table>

## 6.3 编程接口

### 6.3.1 PHP 5.X 接口

1. **dm\_connect**

**描述**

建立一个到 DM 服务器的连接。

在 dm.ukey\_login=0 且 dm.ssl\_login=0 时，最多设置 5 个参数，分别是：server、username、password、new\_link 和 client\_flags。

在 dm.ukey\_login=0 且 dm.ssl\_login=1 时，最多设置 7 个参数，分别是:server、username、password、ssl\_path、ssl\_pwd、new\_link 和 client\_flags。

在 dm.ukey\_login=1 且 dm.ssl\_login=0 时，最多设置 7 个参数，分别是:server、username、password、ukey\_name、ukey\_pin、new\_link 和 client\_flags。

在 dm.ukey\_login=1 且 dm.ssl\_login=1 时，最多设置 9 个参数，分别是:server、username、password、ukey\_name、ukey\_pin、ssl\_path、ssl\_pwd、new\_link 和 client\_flags。

**格式**

```
resource dm_connect ([string $server [, string $username [, string $password [, string $ukey_name [, string $ukey_pin [, string $ssl_path [, string $ssl_pwd[, bool $new_link[, bool $client_flags]]]]]]]]])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| server | \[IN\]服务器地址，格式为 IP:PORT:模式名，PORT 缺省为 5236，模式名缺省为用户名称。server 缺省使用 php.ini 中的配置 |
| username | \[IN\]用户名称，缺省使用 php.ini 中的配置 |
| password | \[IN\]用户密码，缺省使用 php.ini 中的配置 |
| ukey\_name | \[IN\]ukey 名，仅在 dm.ukey\_login=1 时可以设置该参数 |
| ukey\_pin | \[IN\]ukey 密码，仅在 dm.ukey\_login=1 时可以设置该参数 |
| ssl\_path | \[IN\]SSL 证书路径，仅在 dm.ssl\_login=1 时可以设置该参数 |
| ssl\_pwd | \[IN\]SSL 证书密码，仅在 dm.ssl\_login=1 时可以设置该参数 |
| new\_link | \[IN\]设为 0 或不设时，用同样的参数第二次调用 dm\_connect 将不会建立新连接，而将返回已经打开的连接标识；设为 1 时总是返回新的连接标识 |
| client\_flags | 保留参数，不起作用 |

**返回值**

如果成功则返回一个连接标识，失败则返回 FALSE。用同样的参数第二次调用 dm\_connect 不会建立新连接，而将复用已经打开的连接。

**举例说明**

例

```
dm_connect("192.168.0.25:5236:PHPTEST", "SYSDBA", "Dmdba_123", 1);
或
dm_connect("192.168.0.25:5236:PHPTEST", "SYSDBA", "Dmdba_123", "dmukey1", "123456", 1);
或
dm_connect("192.168.0.25:5236:PHPTEST", "SYSDBA", "Dmdba_123", "/home/dmdbms/bin/client_ssl/SYSDBA", "123456", 1);
```
2. **dm\_pconnect**

**描述**

打开一个到 DM 服务器的持久连接。

在 dm.ukey\_login=0 且 dm.ssl\_login=0 时，最多设置 5 个参数，分别是：server、username、password、client\_flag1 和 client\_flag2。

在 dm.ukey\_login=0 且 dm.ssl\_login=1 时，最多设置 7 个参数，分别是:server、username、password、ssl\_path、ssl\_pwd、client\_flag1 和 client\_flag2。

在 dm.ukey\_login=1 且 dm.ssl\_login=0 时，最多设置 7 个参数，分别是:server、username、password、ukey\_name、ukey\_pin、client\_flag1 和 client\_flag2。

在 dm.ukey\_login=1 且 dm.ssl\_login=1 时，最多设置 9 个参数，分别是:server、username、password、ukey\_name、ukey\_pin、ssl\_path、ssl\_pwd、client\_flag1 和 client\_flag2。

**格式**

```
resource dm_pconnect ([string $server [, string $username [, string $password [, string $ukey_name [, string $ukey_pin [, string $ssl_path [, string $ssl_pwd[, bool $client_flag1[, bool $client_flag2]]]]]]]]])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| server | \[IN\]服务器地址，格式为 IP:PORT:模式名，PORT 缺省为 5236，模式名缺省为用户名称。server 缺省使用 php.ini 中的配置 |
| username | \[IN\]用户名称，缺省使用 php.ini 中的配置 |
| password | \[IN\]用户密码，缺省使用 php.ini 中的配置 |
| ukey\_name | \[IN\]ukey 名，仅在 dm.ukey\_login=1 时可以设置该参数 |
| ukey\_pin | \[IN\]ukey 密码，仅在 dm.ukey\_login=1 时可以设置该参数 |
| ssl\_path | \[IN\]SSL 证书路径，仅在 dm.ssl\_login=1 时可以设置该参数 |
| ssl\_pwd | \[IN\]SSL 证书密码，仅在 dm.ssl\_login=1 时可以设置该参数 |
| client\_flag1 | 保留参数，不起作用 |
| client\_flag2 | 保留参数，不起作用 |

**返回值**

如果成功则返回一个正的持久连接标识符，出错则返回 FALSE。

**举例说明**

例

```
dm_pconnect("192.168.0.25:5236:PHPTEST", "SYSDBA", "Dmdba_123");
或
dm_pconnect("192.168.0.25:5236:PHPTEST", "SYSDBA", "Dmdba_123", "dmukey1", "123456");
或
dm_pconnect("192.168.0.25:5236:PHPTEST","SYSDBA", "Dmdba_123", "/home/dmdbms/bin/client_ssl/SYSDBA", "123456", 1);
```
3. **dm\_close**

**描述**

关闭指定的连接标识所关联的 DM 服务器的连接。如果没有指定 link\_identifier，则关闭上一个打开的连接

**格式**

```
bool dm_close ( [resource $link_identifier])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |

**返回值**

如果成功则返回 TRUE，失败则返回 FALSE。

4. **dm\_set\_connect**

**描述**

设置连接。

**格式**

```
int dm_set_connect (int $attr, int $value, resource $link_identifier)
```

**参数**

| **参数** | **描述** | **属性值** |
| --- | --- | --- |
| attr | 设置的属性，同 dpi | DSQL\_ATTR\_ACCESS\_MODE 101   DSQL\_ATTR\_AUTOCOMMIT 102   DSQL\_ATTR\_CONNECTION\_TIMEOUT 113   DSQL\_ATTR\_LOGIN\_TIMEOUT 103   DSQL\_ATTR\_TXN\_ISOLATION 108   DSQL\_ATTR\_LOCAL\_CODE 12345 |
| value | 设置的值 | 属性值。各属性 ID 对应的属性值请参考 2.2.2 节中对应属性的介绍 |
| link\_identifier | \[IN\]连接标识符 |  |

**返回值**

如果成功则返回 TRUE，失败则返回 FALSE。

5. **dm\_error**

**描述**

返回上一个 DM 操作产生的文本错误信息。

**格式**

```
string dm_error ( [resource link_identifier])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |

**返回值**

返回上一个 DM 函数的错误文本，如果没有出错则返回''（空字符串）。如果没有指定连接资源号，则使用上一个成功打开的连接从 DM 服务器提取错误信息。

6. **dm\_errno**

**描述**

返回上一个 DM 操作中的错误信息的数字编码。

**格式**

```
resource dm_db_query (string $database, string $query [, resource $link_identifier])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |

**返回值**

返回上一个 DM 函数的错误号码，如果没有出错则返回 0（零）。

7. **dm\_query**

**描述**

发送一条 DM 查询。

**格式**

```
resource dm_query ( string query [, resource link_identifier])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| query | \[IN\]查询字符串 |
| link\_identifier | \[IN\]连接标识符 |

**返回值**

仅对 SELECT、EXPLAIN 语句返回一个资源标识符，如果查询执行不正确则返回 FALSE。对于其它类型的 SQL 语句，dm\_query()在执行成功时返回 TRUE，出错时返回 FALSE。非 FALSE 的返回值意味着查询是合法的并能够被服务器执行。这并不说明任何有关影响到的或返回的行数。

8. **dm\_unbuffered\_query**

**描述**

向 DM 发送一条 SQL 查询，并不获取和缓存结果的行。

**格式**

```
resource dm_unbuffered_query ( string query [, resource link_identifier])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| query | \[IN\]查询字符串 |
| link\_identifier | \[IN\]连接标识符 |

**返回值**

向 DM 发送一条 SQL 查询 query，但不像 dm\_query()那样自动获取并缓存结果集。一方面，这在处理很大的结果集时会节省可观的内存；另一方面，可以在获取第一行后立即对结果集进行操作，而不用等到整个 SQL 语句都执行完毕。当使用多个数据库连接时，必须指定可选参数 link\_identifier。

9. **dm\_more\_query\_no\_result**

**描述**

执行多条无结果集的语句。

**格式**

```
int dm_more_query_no_result (string sql, resource link_identifier, int flag)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| sql | 要执行的语句 |
| link\_identifier | \[IN\]连接标识符 |
| flagdm | 出错是否返回 |

**返回值**

如果成功则返回 TRUE，失败则返回 FALSE。

10. **dm\_db\_query**

**描述**

发送一条 DM 查询。

**格式**

```
resource dm_db_query ( string database, string query [, resource link_identifier])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| database | \[IN\]指定的数据库名称 |
| query | \[IN\]查询字符串 |
| link\_identifier | \[IN\]连接标识符 |

**返回值**

根据查询结果返回一个正的 DM 结果资源号，出错时返回 FALSE。

11. **dm\_affected\_rows**

**描述**

取得前一次数据库操作 INSERT、UPDATE 或 DELETE 所影响的记录行数。如果连接句柄没有指定，则默认使用最近一次由 dm\_connect()函数打开的连接句柄。

**格式**

```
int dm_affected_rows ( [resource $link_identifier])
```

**参数**

| 参数 | 描述 |
| --- | --- |
| link\_identifier | \[IN\]连接句柄 |

**返回值**

对于非 dml 语句（ddl 语句），返回-1。

**举例说明**

例 1 当前一次数据库操作为 INSERT、UPDATE 或 DELETE 时返回该操作所影响的记录行数。

```
$ret = dm_query("delete from t1;");
$ret = dm_affected_rows($link); //返回delete操作实际影响的记录行数
```

例 2 dm\_more\_query\_no\_result 和 dm\_unbuffered\_query 都不缓存影响行数，因此返回值为-1。

```
dm_more_query_no_result("insert into t1 values(1); insert into t1 values(1);insert into t1 values(1);");
$ret = dm_affected_rows($link); //返回-1
```

例 3 当结果集无法获取时返回值为-1。

```
$ret = dm_query("begin SELECT * from t;sELECT * from t; end;"); 
$ret1=dm_more_result($ret);      //结果集无法获取
$ret2 = dm_affected_rows($link); //返回-1
```

例 4 begin end 均返回 1。

```
$ret = dm_query("begin delete from t; delete from t; end;");
$ret1=dm_more_result($ret); 
$ret2 = dm_affected_rows($link); //返回1
```
12. **dm\_escape\_string**

**描述**

转义一个字符串。转义单引号为’和\`。

**格式**

```
string dm_escape_string ( string $unescaped_string)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| unescaped\_string | \[IN\]被转义字符串 |

**返回值**

返回转义以后的字符串。

13.**dm\_fetch\_array**

**描述**

从结果集中取得一行作为关联数组，或数字数组，或二者兼有。

从结果集中获取的数据返回值类型为 STRING。

**格式**

```
array dm_fetch_array (resource $result [, int $result_type])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |
| result\_type | \[IN\]是一个常量，可以接受以下值：1(DM\_ASSOC)，2(DM\_NUM)和 0(DM\_BOTH)，如果设为 0，即 DM\_BOTH，将得到一个同时包含关联和数字索引的数组。如果设为 1，即 DM\_ASSOC 只得到关联索引, 如果设为 2，即 DM\_NUM 只得到数字索引，数字索引从 0 开始 |

**返回值**

返回从结果集取得的行生成的数组，默认双索引。如果没有更多行则返回 FALSE。

**举例说明**

例

```
$ret = dm_query("SELECT * from t;");

$result1 = dm_fetch_array($ret,1);

if($result1){

echo $result1["C1"];

echo $result1["C2"];

echo 'success'; 

}

//或者

$ret = dm_query("SELECT * from t;");

$result1 = dm_fetch_array($ret,2);

if($result1){

echo $result1[0];

echo $result1[1];

echo 'success'; 

}
```

14.**dm\_fetch\_assoc**

**描述**

从结果集中取得一行作为关联数组。

**格式**

```
array dm_fetch_assoc ( resource $result)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |

**返回值**

返回根据从结果集取得的行生成的关联数组，列名为索引。如果没有更多行则返回 FALSE，可以获取全部结果集。

**举例说明**

例

```
$ret = dm_query("SELECT * from t;");

$result1 = dm_fetch_assoc($ret);

if($result1){

echo $result1["C1"];

echo $result1["C2"];

echo 'success'; 

}
```

15.**dm\_fetch\_field**

**描述**

从结果集中取得列信息并作为对象返回。

**格式**

```
object dm_fetch_field (resource $result [, int $field_offset])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |
| field\_offset | \[IN\]字段偏移，从 0 开始 |

**返回值**

返回一个包含字段信息的对象。

**举例说明**

例

```
$ret = dm_query("SELECT 1 as c1, 2 as c2, 3 as c3");
$col = dm_fetch_field($ret);
if($col){
    if($col->name != "1" || $col->table != "" || $col->auto_uniq != "-1"
        || $col->max_length != "10" || $col->numeric != "1" || $col->blob != "-1"
        || $col->type != "INTEGER" || $col->unsigned != "-1"){
    …
    }
}
```

16.**dm\_num\_fields**

**描述**

取得结果集中字段的数目。

**格式**

```
int dm_num_fields ( resource $result)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |

**返回值**

返回结果集中字段的数目。

17.**dm\_fetch\_lengths**

**描述**

取得结果集中每个输出的长度。

**格式**

```
array dm_fetch_lengths ( resource $result)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |

**返回值**

以数组返回取得的行中每个字段的长度，如果出错返回 FALSE。

18.**dm\_fetch\_object**

**描述**

从结果集中取得一行作为对象。

**格式**

```
object dm_fetch_object ( resource $result)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |

**返回值**

返回根据所取得的行生成的对象，列名为索引。如果没有更多行则返回 FALSE。

**举例说明**

例

```
$result1 = dm_fetch_object($ret);
if($result1){
  echo $result1->C1;
  echo $result1->C2;
}
```

19.**dm\_fetch\_row**

**描述**

从结果集中取得一行作为枚举数组。

**格式**

```
array dm_fetch_row ( resource $result)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |

**返回值**

返回根据所取得的行生成的数组，列序号为索引，从 0 开始。如果没有更多行则返回 FALSE。

**举例说明**

例

```
$ret = dm_query( "SELECT 1 as c1, 2 as c2, 3 as c3");

$result1 = dm_fetch_row($ret);

if($result1[0] != "1" || $result1[1] != "2" || $result1[2] != "3"){…}
```

20.**dm\_field\_flags**

**描述**

从结果中取得和指定字段关联的标志。

**格式**

```
string dm_field_flags (resource $result, int $field_offset)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |
| field\_offset | \[IN\]字段偏移，从 0 开始 |

**返回值**

返回指定字段的字段标志。每个标志都用一个单词表示，之间用一个空格分开。

**举例说明**

例

```
$ret = dm_exec($link,"SELECT * from t1;");
$col = dm_field_flags($ret, 0);
```

21.**dm\_field\_len**

**描述**

返回指定字段的固定长度（精度）。

**格式**

```
int dm_field_len (resource $result, int $field_offset)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |
| field\_offset | 结果集中列的偏移，从 0 开始 |

**返回值**

返回指定字段的固定长度。

22.**dm\_field\_name**

**描述**

取得结果中指定字段的字段名。

**格式**

```
string dm_field_name (resource $result, int $field_index)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |
| field\_index | \[IN\]字段索引号，从 0 开始 |

**返回值**

返回指定字段索引的字段名。result 必须是一个合法的结果标识符，field\_index 是该字段的数字偏移量。

23.**dm\_field\_seek**

**描述**

将结果集中的指针设定为指定的字段偏移量。

**格式**

```
int dm_field_seek (resource $result, int $field_offset)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |
| field\_offset | \[IN\]字段偏移，从 0 开始 |

**返回值**

返回指定字段的上一个字段偏移量。

**举例说明**

例

```
$ret = dm_query("SELECT 1 c1, 2 as c2, 3 as c3");
dm_field_seek($ret, 0)  ;
{
    $col = dm_fetch_field($ret);
    if($col->name == "C1"){
    $result="success"; 
}
```

24.**dm\_field\_table**

**描述**

取得指定字段所在的表名。

**格式**

```
ststring dm_field_table (resource $result, int $field_offset)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| field\_offset | \[IN\]字段偏移 |
| result | \[IN\]结果集资源 |

**返回值**

返回指定字段所在的表名。

25.**dm\_field\_type**

**描述**

取得结果集中指定字段的类型。

**格式**

```
string dm_field_type (resource $result, int $field_offset)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| field\_offset | \[IN\]字段偏移 |
| result | \[IN\]结果集资源 |

**返回值**

返回字段类型有“int”，“real”，“char”，“blob”等。

26.**dm\_free\_result**

**描述**

释放结果内存。

**格式**

```
bool dm_free_result (resource $result)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |

**返回值**

如果成功则返回 TRUE，失败则返回 FALSE。

27.**dm\_get\_server\_info**

**描述**

取得 DM 服务器信息。

**格式**

```
string dm_get_server_info ([resource $link_identifier])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |

**返回值**

返回 link\_identifier 所使用的服务器版本。如果省略 link\_identifier，则使用上一个打开的连接。

28.**dm\_list\_fields**

**描述**

列出 DM 结果中的字段。

**格式**

```
resource dm_list_fields ( string $database_name, string $table_name [, resource $link_identifier[,string $owner_name r[,string $field_name]]])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| database\_name | \[IN\]数据库名 |
| table\_name | \[IN\]表名 |
| link\_identifier | \[IN\]连接标识符 |
| owner\_name | 模式名 |
| field\_name | 指定列名 |

**返回值**

返回一个结果指针。

**举例说明**

例

```
$ret = dm_list_fields("SYSTEM", "T1"); 
$col = dm_fetch_field($ret);
    while($col)
    {
      if($col->name == "CT1"){ 
      $flag= TRUE;
      break;
    }
    else{  
      $result="fail"; 
        }
        $col = dm_fetch_field($ret);
    }
```

29.**dm\_list\_tables**

**描述**

列出 DM 数据库中的表。

**格式**

```
resource dm_list_tables (string $database_name [, resource $link_identifier[, string $owner [, string $name ]]])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| database\_name | \[IN\]数据库名，忽略 |
| link\_identifier | \[IN\]连接标识符 |
| owner | 模式名 |
| name | 表名 |

**返回值**

返回一个结果指针。

30.**dm\_num\_rows**

**描述**

取得结果集中行的数目。

**格式**

```
int dm_num_rows ( resource $result)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集 |

**返回值**

返回结果集中行的数目。此命令仅对 SELECT 语句有效。

31.**dm\_ping**

**描述**

Ping 一个服务器连接，如果参数缺省则重新连接。

**格式**

```
bool dm_ping ( [resource $link_identifier])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |

**返回值**

如果到服务器的连接可用则 dm\_ping()返回 TRUE，否则返回 FALSE。

32.**dm\_more\_result**

**描述**

取得下一个结果集。释放当前结果集。

**格式**

```
bool dm_more_result (resource $result )
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集 |

**返回值**

如果含有至少两个结果集，返回 TRUE，否则返回 FALSE。

**举例说明**

例

```
//错误用法：
$ret = dm_query("begin SELECT * from t;delete * from t; end;");  
$ret1=dm_more_result($ret);
//正确用法：
$ret = dm_query("begin SELECT * from t; SELECT * from t;end;");  
$ret1=dm_more_result($ret);
```

33.**dm\_result**

**描述**

取得一行结果数据。

**格式**

```
mixed dm_result (resource $result, int $row [, mixed $field])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集 |
| row | \[IN\]指定行序号(从 0 开始) |
| field | \[IN\]指定列索引(从 0 开始)或列名称 |

**返回值**

返回 DM 结果集中一个单元（第 row +1 行 第 field+1 列）的内容。Row 为也可以为字符串（单引号或双引号的数字），若为无效字符串时，默认是第一行。列名称大小写不区分。第三个参数为可选参数，默认第一列。

**举例说明**

例

```
SQL> select * from member;
//查询结果如下：
行号       member_name C0
---------- ----------- -----------
1          小明        NULL
2          小红        NULL
3          小日        100
$ret = dm_query("SELECT  * from member");
$result = dm_result($ret,  '2', 'C0');
```

34.**dm\_insert\_id**

**描述**

取得上一步 INSERT 操作产生的 ID。

**格式**

```
int dm_insert_id ( [resource $link_identifier])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |

**返回值**

返回给定的 link\_identifier 中上一步 INSERT 查询中产生的 AUTO\_INCREMENT 的 ID 号。如果没有指定 link\_identifier，则使用上一个打开的连接。如果上一查询没有产生 AUTO\_INCREMENT 的值，则 dm\_insert\_id()返回 0。

35.**dm\_tablename**

**描述**

取得表名。

**格式**

```
string dm_tablename (resource $result, int $i)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]表结果集 |
| i | \[IN\]表索引序号，从 0 开始 |

**返回值**

接受 dm\_list\_tables()返回的结果指针以及一个整数索引作为参数并返回表名。

**举例说明**

例

```
$ret = dm_list_tables("SYSTEM", $link, "%", "T1");
$row = 0;
$name = dm_tablename($ret, $row);
while($name){
    if($name == "T1"){
                    …….
                }
    $row = $row + 1;
    $name = dm_tablename($ret, $row);
    }
```

36.**dm\_data\_seek**

**描述**

移动内部结果的指针。

**格式**

```
bool dm_data_seek (resource $result_identifier, int $row_number)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result\_identifier | \[IN\]结果集 |
| row\_number | \[IN\]表索引序号，从 0 开始 |

**返回值**

指定的结果标识所关联的 DM 结果内部的行指针移动到指定的行号。

37.**dm\_set\_object\_name\_case**

**描述**

设置使用列名称时的大小写方式。

**格式**

```
bool dm_set_object_name_case(resource $link_identifier, int $case_sensitive)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| case\_sensitive | 大小写方式。1：小写； 2：大写； 0：保持大小写 |

**返回值**

设置成功，返回 TRUE；否则返回 FALSE。

38.**dm\_prepare**

**描述**

准备一条语句

**格式**

```
resource dm_prepare (string $query [, resource $link_identifier])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| query | \[IN\]查询字符串 |
| link\_identifier | \[IN\]连接标识符 |

**返回值**

在准备成功时返回一个资源标识符，出错时返回 FALSE。

39.**dm\_commit**

**描述**

提交一个事务。

**格式**

```
bool dm_commit (resource $link_identifier)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |

**返回值**

成功返回 TRUE，失败返回 FALSE。

40.**dm\_execute**

**描述**

执行一条语句。（包括准备和执行，可以带绑定参数）

**格式**

```
resource  dm_execute (resource $link_identifier, string $query[, array $parameters_array])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| query | \[IN\]查询字符串 |
| parameters\_array | 参数组成的数组 |

**返回值**

在执行成功时返回一个资源标识符，出错时返回 FALSE。

**举例说明**

例

```
$a = 1;
$query = "INSERT INTO t2(c0)  VALUES(?)";  
$result = dm_execute($link, $query, array($a)); 
$query = "INSERT INTO t2(c0)  VALUES(10)"; 
$result = dm_execute($link, $query ) or die("Query failed : " . dm_error());
```

41.**dm\_execute\_ex**

**描述**

执行一条准备过的语句（可以带有绑定参数）。

**格式**

```
resource  dm_execute_ex (resource $result [, array $parameters_array])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]准备过的资源标识符 |
| parameters\_array | 参数组成的数组 |

**返回值**

在执行成功时返回一个资源标识符，出错时返回 FALSE。

**举例说明**

例

```
$a = 1;
$b = 2;
$c = 3;
$stmt = dm_prepare($link, 'insert into t values(?,?,?)');
$result = dm_execute_ex($stmt, array($a,$b,$c));
```

42.**dm\_abort**

**描述**

回滚一个事务。

**格式**

```
bool dm_abort (resource $link_identifier)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |

**返回值**

成功返回 TRUE，失败返回 FALSE。

43.**dm\_begin\_trans**

**描述**

设置事务为不自动提交。

**格式**

```
bool dm_begin_trans (resource $link_identifier)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |

**返回值**

成功返回 TRUE，失败返回 FALSE。

44.**dm\_get\_version**

**描述**

获得服务器版本号。

**格式**

```
char*  dm_get_version (resource $link_identifier)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |

**返回值**

返回 dmversion 字符串。

45.**dm\_select\_db**

**描述**

选择用于数据库查询的默认模式，如果连接标识符没有指定，则默认使用最近一次由 dm\_connect()函数打开的连接句柄。

**格式**

```
bool  dm_select_db (string $schema[,resource $link_identifier]))
```

**参数**

| **参数** | **描述** |
| --- | --- |
| schema | \[IN\]连接模式名 |
| link\_identifier | \[IN\]连接标识符 |

**返回值**

成功返回 TRUE，失败返回 FALSE。

**举例说明**

例

```
$ret = dm_select_db("SYS", $link);
或
$ret = dm_select_db("SYS");
```

46.**dm\_php\_debug**

**描述**

开启 debug 模式，开启后会保存后续执行的 sql 语句到指定的文件中。如果没有指定 $path 参数，则用于关闭 debug 模式。

**格式**

```
bool dm_php_debug ([string $path])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| path | 开启 debug 模式后，保存 sql 语句的文件路径 |

**返回值**

开启成功或关闭成功返回 TRUE，如果保存的文件路径不存在返回 FALSE。

**举例说明**

例

```
$a = 1;
$query = "select *,id_code from v\$version where rownum = (?)";
dm_php_debug("D:/debug_php.txt");
$result = dm_execute($conn, $query, array($a));
```

47.**dm\_longreadlen**

**描述**

设置变长类型读取的最大长度，为 0 时表示读取全部。

**格式**

```
bool dm_longreadlen (resource $link_identifier, int $length)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| length | 读取的最大长度 |

**返回值**

在获取成功时返回 TRUE，出错时返回 FALSE。

48.**dm\_bind\_array\_by\_name**

**描述**

将 php 的 array 变量绑定到指定变量名的位置上。

**格式**

```
bool dm_bind_array_by_name (resource $statement, string $param, array $var, int $max_array_length, int $maxlength, int $type)
```

**参数**

statement（输入）：准备过的资源标识符。

param: 需要绑定的变量名。

var: 参数组成的数组。

max\_array\_length: 设置输入或输出数组的最大长度

maxlength: 数组中单项的最大长度。若设置为-1，则将使用数组中元素最长的值作为最大长度。如果设置过小，数据会被破坏

type: 要绑定的数据库类型，支持的类型如下：DSQL\_BIT、DSQL\_TINYINT、DSQL\_SMALLINT、DSQL\_INTEGER、DSQL\_BIGINT、DSQL\_FLOAT、DSQL\_DOUBLE、DSQL\_DECIMAL、DSQL\_CHAR、DSQL\_VARCHAR、DSQL\_DATE、DSQL\_TIME、DSQL\_TIMESTAMP、DSQL\_CLOB、DSQL\_BLOB、DSQL\_BINARY、DSQL\_VARBINARY。

**返回值**

在执行成功时返回 TRUE，出错时返回 FALSE。

**举例说明**

```
$create = "CREATE table bind_test(name FLOAT)";
$statement = dm_prepare($c, $create);
dm_execute_ex($statement);

$create_pkg = "
CREATE OR REPLACE PACKAGE ARRAY_BIND_FLOAT_PKG AS
 TYPE ARRTYPE IS TABLE OF FLOAT;
 PROCEDURE iobind(c1 IN OUT ARRTYPE);
END ARRAY_BIND_FLOAT_PKG;";
$statement = dm_prepare($c, $create_pkg);
dm_execute_ex($statement);

$create_pkg_body = "
CREATE OR REPLACE PACKAGE BODY ARRAY_BIND_FLOAT_PKG AS
 CURSOR CUR IS SELECT name FROM bind_test;
 PROCEDURE iobind(c1 IN OUT ARRTYPE) IS
  BEGIN
  FOR i IN 1..5 LOOP
   INSERT INTO bind_test VALUES (c1(i));
  END LOOP;
  IF NOT CUR%ISOPEN THEN
   OPEN CUR;
  END IF;
  FOR i IN REVERSE 1..5 LOOP
   FETCH CUR INTO c1(i);
   IF CUR%NOTFOUND THEN
    CLOSE CUR;
    EXIT;
   END IF;
  END LOOP;
 END iobind;
END ARRAY_BIND_FLOAT_PKG;";

$statement = dm_prepare($c, $create_pkg_body);
dm_execute_ex($statement);
 
$array = Array(1.243,2.5658,3.4234,4.2123,5.9999);
$statement = dm_prepare($c, "BEGIN array_bind_float_pkg.iobind(?); END;");
dm_bind_array_by_name($statement, ":c1", $array, 5, 5, DSQL_DOUBLE);
```

### 6.3.2 PHP 7.X 接口

#### 6.3.2.1 和 PHP 5.X 同名接口

下面是 PHP 7.X 中和 PHP 5.X 同名的接口，但是功能和参数等和 PHP 5.X 略有不同。

1. **dm\_prepare**

**描述**

准备一条语句。PHP 7.x dm\_prepare 不支持默认连接，除此之外其他用法同 dm\_errno(PHP 5.x)。

**格式**

```
resource dm_prepare (resource $link_identifier, string $query)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| query | \[IN\]查询字符串 |
| link\_identifier | \[IN\]连接标识符\[IN\]连接标识符，不支持缺省默认连接，不可缺省 |

**返回值**

在准备成功时返回一个资源标识符，出错时返回 FALSE。

2.**dm\_execute**

**描述**

执行一条准备过的语句（可以带有绑定参数）。

**格式**

```
resource dm_execute (resource $result , array $parameters_array )
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | 准备过的资源标识符 |
| parameters\_array | \[IN\]参数数组 |

**返回值**

成功时返回 TRUE， 或者在失败时返回 FALSE。

**举例说明**

例

```
$a = 1;
$b = 2;
$c = 3;
$stmt = dm_prepare($link, 'insert into t values(?,?,?)');
$result = dm_execute($stmt, array($a,$b,$c));
```

3.**dm\_field\_len**

**描述**

返回指定字段的固定长度（精度）。

**格式**

```
int dm_field_len (resource $result, int $field_offset)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |
| field\_offset | 结果集中列的偏移，从 1 开始 |

**返回值**

返回指定字段的固定长度。

4.**dm\_field\_name**

**描述**

取得结果中指定字段的字段名。

**格式**

```
string dm_field_name (resource $result, int $field_index)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |
| field\_index | \[IN\]字段索引号，从 1 开始 |

**返回值**

返回指定字段索引的字段名。result 必须是一个合法的结果标识符，field\_index 是该字段的数字偏移量。

5.**dm\_field\_type**

**描述**

取得结果集中指定字段的类型。

**格式**

```
string dm_field_type (resource $result, int $field_offset)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| field\_offset | \[IN\]字段偏移，从 1 开始 |
| result | \[IN\]结果集资源 |

**返回值**

返回字段类型有“int”，“real”，“char”，“blob”等。

6.**dm\_fetch\_array**

**描述**

指定行号从结果集中取得一行作为关联数组。

从结果集中获取 INT/BIGINT/TINYINT 类型返回 INT、获取浮点类型返回 DOUBLE、获取 NUMBER 类型的返回 DOUBLE 或 STRING、获取其他类型返回 STRING。NUMBER 类型的返回类型由 PHP.INI 参数 DM.FETCH\_NUMBER 控制。0：返回 DOUBLE；1：返回 STRING。缺省为 0。

**格式**

```
array dm_fetch_array (resource $result [,int $rownum])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |
| rownum | \[IN\]取得的行号。可选参数，缺省从 1 开始 |

**返回值**

返回根据指定行号从结果集取得生成的数组，列名为索引。如果没有更多行则返回 FALSE。如果 rownum=0 或缺省，则获取游标的下一行。可代替 PHP 5.x 中的 dm\_fetch\_array 以及 dm\_fetch\_length。

**举例说明**

例

```
//PHP 5.x中利用dm_fetch_lengths获取结果集中所有列长度数组
$ret = dm_exec($link,"SELECT * from T1");
$collens = dm_fetch_lengths($ret);
 
//PHP 7.x中利用dm_fetch_array获取结果集中的列长度
$ret = dm_exec($link,"SELECT * from T1");
$colval= dm_fetch_array($ret);
//建议直接查看$colval["列名"]对象的实际长度以获取该列长度
```

7.**dm\_fetch\_row**

**描述**

从结果集中取得一行数据。

**格式**

```
bool dm_fetch_row (resource $result [,int $rownum])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |
| rownum | \[IN\]取得的行号。可选参数，缺省从 1 开始。 |

**返回值**

成功获取到数据返回 TRUE，如果没有更多行则返回 FALSE。可代替 PHP 5.x 中的 dm\_fetch\_row 和 dm\_data\_seek。

**举例说明**

例

```
//PHP 5.x中利用dm_data_seek取得第三行结果集

$ret = dm_query("SELECT * from t1");

dm_data_seek($ret, 2);   

$result = dm_fetch_object($ret);

//PHP 7.x中利用dm_fetch_row取得第三行结果集

dm_fetch_row($ret, 3);

//PHP 7.x访问结果集的第一列

$val = dm_result($ret, 1);
```

8.**dm\_fetch\_object**

**描述**

从结果集中取得一行作为对象。

**格式**

```
object dm_fetch_object (resource $result  [, int $rownumber])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |
| rownumber | 行号。可选参数，缺省从 1 开始 |

**返回值**

返回根据所取得的行生成的对象，列名为索引，借助 dm\_result 函数可以以列序号为索引进行查找。如果没有更多行则返回 FALSE。

**举例说明**

例

```
$result1 = dm_fetch_object($ret, 2);
if($result1){ 
    echo $result1->C1;
    echo $result1->C2;
    $val1 = dm_result($ret,1);
    echo $val1;
}
```

9.**dm\_result**

**描述**

取得结果数据。

**格式**

```
mixed dm_result (resource $result, mixed $field)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集 |
| field | \[IN\]指定列索引(从 1 开始)或列名称(单引号或双引号) |

**返回值**

返回 DM 结果集中指定列的第一行的内容。

**举例说明**

例

```
SQL> SELECT * from t2; 
//查询结果如下：
行号       member_name c0
---------- ----------- -----------
1          小明         1
2          小红         2
$ret = dm_exec($link, "SELECT * from t2");
$result = dm_result($ret,  1);--第1列
$result = dm_result($ret,  "c0");--c0列 

//可以按下面方式遍历所有行
while(dm_fetch_row($ret)){
    $result1 = dm_result($ret, "c0");
}
```

10.**dm\_connect**

**描述**

建立一个到 DM 服务器的连接。

在 dm.ukey\_login=0 且 dm.ssl\_login=0 时，最多设置 4 个参数，分别是：server、username、password 和 client\_flags。

在 dm.ukey\_login=0 且 dm.ssl\_login=1 时，最多设置 6 个参数，分别是:server、username、password、ssl\_path、ssl\_pwd 和 client\_flags。

在 dm.ukey\_login=1 且 dm.ssl\_login=0 时，最多设置 6 个参数，分别是:server、username、password、ukey\_name、ukey\_pin 和 client\_flags。

在 dm.ukey\_login=1 且 dm.ssl\_login=1 时，最多设置 8 个参数，分别是:server、username、password、ukey\_name、ukey\_pin、ssl\_path、ssl\_pwd 和 client\_flags。

**格式**

```
resource dm_connect ([string $server [, string $username [, string $password [, string $ukey_name [, string $ukey_pin[, string $ssl_path [, string $ssl_pwd [,bool $client_flags]]]]]]]])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| server | \[IN\]服务器地址，格式为 IP:PORT:模式名，PORT 缺省为 5236，模式名缺省为用户名称。server 缺省使用 php.ini 中的配置 |
| username | \[IN\]用户名称，缺省使用 php.ini 中的配置 |
| password | \[IN\]用户密码，缺省使用 php.ini 中的配置 |
| ukey\_name | \[IN\]ukey 名，仅在 dm.ukey\_login=1 时可以设置该参数 |
| ukey\_pin | \[IN\]ukey 密码，仅在 dm.ukey\_login=1 时可以设置该参数 |
| ssl\_path | \[IN\]SSL 证书路径，仅在 dm.ssl\_login=1 时可以设置该参数 |
| ssl\_pwd | \[IN\]SSL 证书密码，仅在 dm.ssl\_login=1 时可以设置该参数 |
| client\_flags | 保留参数，不起作用 |

**返回值**

如果成功则返回一个连接标识，失败则返回 FALSE。

**举例说明**

例

```
dm_connect("192.168.0.25:5236:PHPTEST", "SYSDBA", "Dmdba_123", 1);
或
dm_connect("192.168.0.25:5236:PHPTEST", "SYSDBA", "Dmdba_123", "dmukey1", "123456", 1);
或
dm_connect("192.168.0.25:5236:PHPTEST", "SYSDBA", "Dmdba_123", "/home/dmdbms/bin/client_ssl/SYSDBA", "123456", 1);
```

11.**dm\_pconnect**

**描述**

打开一个到 DM 服务器的持久连接。

在 dm.ukey\_login=0 且 dm.ssl\_login=0 时，最多设置 4 个参数，分别是：server、username、password 和 client\_flags。

在 dm.ukey\_login=0 且 dm.ssl\_login=1 时，最多设置 6 个参数，分别是:server、username、password、ssl\_path、ssl\_pwd 和 client\_flags。

在 dm.ukey\_login=1 且 dm.ssl\_login=0 时，最多设置 6 个参数，分别是:server、username、password、ukey\_name、ukey\_pin 和 client\_flags。

在 dm.ukey\_login=1 且 dm.ssl\_login=1 时，最多设置 8 个参数，分别是:server、username、password、ukey\_name、ukey\_pin、ssl\_path、ssl\_pwd 和 client\_flags。

**格式**

```
resource dm_pconnect ([string $server [, string $username [, string $password [, string $ukey_name [, string $ukey_pin[, string $ssl_path [, string $ssl_pwd [,bool $client_flags]]]]]]]])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| server | \[IN\]服务器地址，格式为 IP:PORT:模式名，PORT 缺省为 5236，模式名缺省为用户名称。server 缺省使用 php.ini 中的配置 |
| username | \[IN\]用户名称，缺省使用 php.ini 中的配置 |
| password | \[IN\]用户密码，缺省使用 php.ini 中的配置 |
| ukey\_name | \[IN\]ukey 名，仅在 dm.ukey\_login=1 时可以设置该参数 |
| ukey\_pin | \[IN\]ukey 密码，仅在 dm.ukey\_login=1 时可以设置该参数 |
| ssl\_path | \[IN\]SSL 证书路径，仅在 dm.ssl\_login=1 时可以设置该参数 |
| ssl\_pwd | \[IN\]SSL 证书密码，仅在 dm.ssl\_login=1 时可以设置该参数 |
| client\_flags | 保留参数，不起作用 |

**返回值**

如果成功则返回一个正的持久连接标识符，出错则返回 FALSE。用同样的参数第二次调用 dm\_pconnect 不会建立新连接，而将复用已经打开的连接。

12.**dm\_error**

**描述**

返回上一个 DM 操作中的错误信息的数字编码。PHP 7.x dm\_error 返回值为 string，除此之外其他用法同 dm\_errno(PHP 5.x)。

**格式**

```
string dm_error ([resource $link_identifier])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符，可缺省 |

**返回值**

返回上一个 DM 函数的错误号码，如果没有出错则返回空字符串。

13.**dm\_get\_server\_info**

**描述**

取得 DM 服务器信息。PHP 7.x dm\_get\_server\_info 不支持默认连接，除此之外其他用法同 PHP 5.x。

**格式**

```
string dm_get_server_info (resource $link_identifier)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符，不支持缺省默认连接，不可缺省 |

**返回值**

返回 link\_identifier 所使用的服务器版本。

14.**dm\_close**

**描述**

关闭指定的连接标识所关联的 DM 服务器的连接。PHP 7.x dm\_close 不支持默认连接，除此之外其他用法同 PHP 5.x。

**格式**

```
bool dm_close (resource $link_identifier)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符，不支持缺省默认连接，不可缺省 |

**返回值**

如果成功则返回 TRUE，失败则返回 FALSE。

15.**dm\_affected\_rows**

**描述**

取得前一次数据库操作 INSERT、UPDATE 或 DELETE 所影响的记录行数。如果连接句柄没有指定，则默认使用最近一次由 dm\_connect()函数打开的连接句柄。PHP 7.x dm\_affected\_rows 不支持默认连接，除此之外其他用法同 PHP 5.x。

**格式**

```
int dm_affected_rows (resource $link_identifier)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符，不支持缺省默认连接，不可缺省 |

**返回值**

对于非 dml 语句（ddl 语句），返回-1。

16.**dm\_list\_fields**

**描述**

列出 DM 结果中的字段。PHP 7.x dm\_list\_fields 不支持默认连接，除此之外其他用法同 PHP 5.x。

**格式**

```
resource dm_list_fields (string $database_name, string $table_name , resource  $link_identifier[,string $owner_name r[,string $field_name]])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| database\_name | \[IN\]数据库名 |
| table\_name | \[IN\]表名 |
| link\_identifier | \[IN\]连接标识符，不支持缺省默认连接，不可缺省 |
| owner\_name | 模式名 |
| field\_name | 指定列名 |

**返回值**

返回一个结果指针。

17.**dm\_insert\_id**

**描述**

取得上一步 INSERT 操作产生的 ID。PHP 7.x dm\_insert\_id 不支持默认连接，除此之外其他用法同 PHP 5.x。

**格式**

```
int dm_insert_id (resource $link_identifier)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符，不支持缺省默认连接，不可缺省 |

**返回值**

返回给定的 link\_identifier 中上一步 INSERT 查询中产生的 AUTO\_INCREMENT 的 ID 号。如果没有指定 link\_identifier，则使用上一个打开的连接。如果上一查询没有产生 AUTO\_INCREMENT 的值，则 dm\_insert\_id()返回 0。

18.**dm\_fetch\_assoc**

**描述**

指定行号从结果集中取得一行作为关联数组。

**格式**

```
array dm_fetch_assoc (resource $result [,int $rownum])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |
| rownum | \[IN\]取得的行号。可选参数，缺省从 1 开始 |

**返回值**

返回根据指定行号从结果集取得生成的数组，列名为索引。如果没有更多行则返回 FALSE。如果 rownum=0 或缺省，则获取游标的下一行；如果 rownum 缺省，可代替 PHP 5.x 中的 dm\_fetch\_assoc。

**举例说明**

例

```
//PHP 5.x中利用dm_fetch_assoc从结果集取得的行生成的关联数组
$ret = dm_query("SELECT * from t;");
$result1 = dm_fetch_assoc($ret);
if($result1){
echo $result1["C1"];
echo $result1["C2"];
echo 'success'; 
}
//PHP 7.x中利用dm_fetch_array从结果集取得的行生成的关联数组
$ret = dm_exec($link,"SELECT * from t");
$result1 = dm_fetch_assoc($ret);
if($result1){
echo $result1["C1"];
echo $result1["C2"];
echo 'success'; 
}
```

19.**dm\_select\_db**

**描述**

选择用于数据库查询的默认模式，连接标识符不可缺省。

**格式**

```
bool  dm_select_db (resource $link_identifier, string $schema)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符，不支持缺省默认连接，不可缺省 |
| schema | \[IN\]连接模式名 |

**返回值**

成功返回 TRUE，失败返回 FALSE。

**举例说明**

例

```
$ret = dm_select_db( $link, "SYS");
```

20. **dm\_ping**

**描述**

Ping 一个服务器连接。

**格式**

```
bool dm_ping (resource $link_identifier)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |

**返回值**

如果到服务器的连接可用则 dm\_ping()返回 TRUE，否则返回 FALSE 或者抛出异常。

#### 6.3.2.2 PHP 7.X 新增接口

1. **dm\_exec**

**描述**

执行一条语句或查询。

**格式**

```
resource dm_exec(resource $link_identifier [,string $query])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| query | \[IN\]语句字符串 |

**返回值**

作用同 dm\_query(PHP 5.x)，可代替 PHP 5.x 中的 dm\_query、dm\_unbuffered\_query、dm\_more\_query\_no\_result 以及 dm\_db\_query。

**举例说明**

例

```
$result = dm_exec($link, $query);
$result = dm_exec($link, “ddl语句”);
```

2.**dm\_tables**

**描述**

列出 DM 数据库中的表。

**格式**

```
$result = dm_exec($link, $query);
$result = dm_exec($link, "ddl语句");
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link | \[IN\]连接句柄，不支持缺省默认连接，不可缺省 |
| qualifier | 库名，忽略该参数 |
| owner | 模式名 |
| name | 表名 |
| types | 表 or 视图。值：SYSTEM TABLE，TABLE，VIEW |

**返回值**

在获取成功时返回一个资源标识符，出错时返回 FALSE。可代替 PHP 5.x 中的 dm\_list\_tables。

3.**dm\_columns**

**描述**

列出 DM 数据库中的列。

**格式**

```
resource dm_columns (resource $link[, string $qualifier [, string $schema [, string $table_name [, string $column_name ]]]])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link | \[IN\]连接句柄 |
| qualifier | 库名 |
| schema | 模式名 |
| table\_name | 表名 |
| column\_name | 列名过滤格式，如 % |

**返回值**

在获取成功时返回一个资源标识符，出错时返回 FALSE。

4.**dm\_result\_all**

**描述**

取得全部结果数据，并打印成 html 格式。

**格式**

```
int dm_result_all ( resource $result,  [, string $format])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集 |
| format | html 格式中\<table 标签追加属性> ' id="c1",age="c2"' |

**返回值**

返回的是结果集行数，错误时返回 FALSE。

**举例说明**

例

```
dm_result_all($ret, 'id="c1", age="c2"');
```

执行结果如下：

```
<table id="c1", age="c2" >
<tr><th>C1</th><th>C2</th></tr>
<tr><td>10</td><td>20</td></tr>
```

5.**dm\_binmode**

**描述**

二进制类型数据的处理方式。该函数用来对输入的二进制类型列数据进行转换处理。二进制类型有：BINARY、VARBINARY 及 BLOB 三种。

当二进制 SQL 数据转换为字符串时，源数据的每个字节（8 位）表示为两个 ASCII 字符，这些字符是由十六进制数字的 ASCII 字符表示。例如：BINARY 类型的  
00000001 被转为十六进制的“01”，BINARY 类型的 11111111 被转为十六进制的“FF”。

**格式**

```
bool dm_binmode (resource $link_identifier, int $mode)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| mode | 模式取值：   DM\_BINMODE\_PASSTHRU 不处理   DM\_BINMODE\_RETURN 转成 16 进制   DM\_BINMODE\_CONVERT 转成字符串 |

**返回值**

在获取成功时返回 TRUE，出错时返回 FALSE。

6.**dm\_close\_all**

**描述**

关闭所有连接

**格式**

```
void dm_close_all ( void )
```

**参数**

无。

**返回值**

无。

7.**dm\_autocommit**

**描述**

设置事务是否为自动提交。

**格式**

```
bool dm_autocommit (resource $link_identifier, bool $flag)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| flag | 取值： 1 是 0 否 |

**返回值**

成功返回 TRUE，失败返回 FALSE。可代替 PHP 5.x 中的 dm\_begin\_trans，只需将 flag 设为 0，即可设置事务为不自动提交。

8.**dm\_cursor**

**描述**

获取游标名。

**格式**

```
string dm_cursor (resource  $result_id )
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]结果集资源 |

**返回值**

游标名。

9.**dm\_errormsg**

用法同 dm\_error(PHP 5.x)。

10.**dm\_fetch\_into**

**描述**

获取一行结果集到数组中。

**格式**

```
int dm_fetch_into(resource $result, array $parameters_array [, int $rownumber])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |
| parameters\_array | Array 数组 |
| rownumber | 行号 |

**返回值**

返回结果集的列数，失败返回 FALSE。

11.**dm\_field\_scale**

**描述**

获取结果集中指定字段的标度。

**格式**

```
int dm_field_scale ( resource $result, int $field_offset)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result | \[IN\]结果集资源 |
| field\_offset | 字段序号，起始值为 1 |

**返回值**

指定字段的标度。

12.**dm\_field\_num**

**描述**

获取结果集中指定字段的序号。

**格式**

```
int dm_field_num (resource $result_id, string $field_name)
```

| **参数** | **描述** |
| --- | --- |
| result\_id | \[IN\]结果集资源 |
| field\_name | 字段名 |

**返回值**

指定字段的序号，起始值为 1。

13.**dm\_next\_result**

**描述**

切换结果集。单条 sql 不能切换，必须是一个过程中产生了多个结果集。

**格式**

```
bool  dm_next_result ( resource $result_id )
```

**参数**

| **参数** | **描述** |
| --- | --- |
| result\_id | \[IN\]结果集资源 |

**返回值**

有下一个结果集返回 TRUE，无结果集返回 FALSE。可代替 PHP 5.x 中的 dm\_more\_result。

14.**dm\_rollback**

用法同 dm\_abort(PHP 5.x)。

15.**dm\_setoption**

**描述**

设置 dm 连接和语句的相关属性。

**格式**

```
bool  dm_setoption (resource $id, int $function, int $option, int $param)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| id | 连接标识符或者结果集资源 |
| function | 取值：   1：conn   2：stmt |
| option | 属性 ID。 当 function 为 1 时，不同属性对应的属性 ID 为： DSQL\_ATTR\_ACCESS\_MODE 101   DSQL\_ATTR\_AUTOCOMMIT 102   DSQL\_ATTR\_CONNECTION\_TIMEOUT 113   DSQL\_ATTR\_LOGIN\_TIMEOUT 103   DSQL\_ATTR\_TXN\_ISOLATION 108   DSQL\_ATTR\_LOCAL\_CODE 12345   当 function 为 2 时，不同属性对应的属性 ID 为：   DSQL\_ATTR\_ENABLE\_AUTO\_IPD 15   DSQL\_ATTR\_FETCH\_BOOKMARK\_PTR 16   DSQL\_ATTR\_MAX\_LENGTH 3   DSQL\_ATTR\_MAX\_ROWS 1   DSQL\_ATTR\_NOSCAN 2   DSQL\_ATTR\_PARAM\_BIND\_OFFSET\_PTR 17   DSQL\_ATTR\_PARAM\_BIND\_TYPE 18   DSQL\_ATTR\_PARAM\_OPERATION\_PTR 19   DSQL\_ATTR\_PARAM\_STATUS\_PTR 20   DSQL\_ATTR\_PARAMS\_PROCESSED\_PTR 21   DSQL\_ATTR\_PARAMSET\_SIZE 22   DSQL\_ATTR\_QUERY\_TIMEOUT 0   DSQL\_ATTR\_RETRIEVE\_DATA 11   DSQL\_ATTR\_ROW\_BIND\_OFFSET\_PTR 23   DSQL\_ATTR\_ROW\_BIND\_TYPE 5   DSQL\_ATTR\_ROW\_NUMBER 14   DSQL\_ATTR\_ROW\_OPERATION\_PTR 24   DSQL\_ATTR\_ROW\_STATUS\_PTR 25   DSQL\_ATTR\_ROWS\_FETCHED\_PTR 26   DSQL\_ATTR\_ROW\_ARRAY\_SIZE 27   DSQL\_ATTR\_SIMULATE\_CURSOR 10   DSQL\_ATTR\_USE\_BOOKMARKS 12   DSQL\_ATTR\_ROWSET\_SIZE 9 |
| param | 属性值。各属性 ID 对应的属性值请参考 2.2.2 节中对应属性的介绍 |

**返回值**

在设置成功时返回 TRUE，出错时返回 FALSE。可代替 PHP 5.x 中的 dm\_set\_connect。

16.**dm\_specialcolumns**

**描述**

返回可唯一标识表中任意行的最佳列或列集，或者返回事务更新表时被自动更新的列或列集。

**格式**

```
resource dm_specialcolumns(resource $link_identifier, int $type, char* $catalog_name, char* $schema_name, char* $table_name, int $scope, int $nullable);
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| type | 取值范围：   1：返回可唯一标识表中任意行的最佳列或列集；   2：返回事务更新表时被自动更新的列或列集 |
| catalog\_name | 目录限定符，仅支持取值为 NULL 或空串 |
| schema\_name | 模式名 |
| table\_name | 表名 |
| scope | 仅支持取值为 0，否则返回结果集为空 |
| nullable | 是否为空，0：否；1：是 |

**返回值**

返回一个资源 id。

17.**dm\_statistics**

**描述**

获取表及其索引的信息

**格式**

```
resource dm_statistics (resource $link_identifier, string $qualifier, string $owner, string $table_name, int $unique, int $accuracy)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| qualifier | 库名 |
| owner | 模式名 |
| table\_name | 表名 |
| unique | unique 属性。取值： SQL\_INDEX\_UNIQUE 表示只返回 unique 索引 SQL\_INDEX\_ALL 表示返回所有索引 |
| accuracy | 忽略 |

**返回值**

返回一个结果集或失败返回 FALSE。

18.**dm\_primarykeys**

**描述**

获取表的主键。

**格式**

```
resource dm_primarykeys ( resource $ link_identifier , string $qualifier , string $owner , string $ table )
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| Qualifier | 库名 |
| owner | 模式名 |
| table | 表名 |

**返回值**

返回一个结果集或失败返回 FALSE。

19.**dm\_columnprivileges**

**描述**

列出列的权限。

**格式**

```
resource dm_primarykeys (resource $link_identifier, string $qualifier, string $owner, string $table )
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| qualifier | 库名 |
| owner | 模式名 |
| name | 表名 |
| column\_name | 列名 |

**返回值**

返回一个结果集或失败返回 FALSE。

20.**dm\_tableprivileges**

**描述**

列出表的权限。

**格式**

```
resource dm_tableprivileges (resource $link_identifier, string $qualifier, string $owner, string $name)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| qualifier | 库名 |
| owner | 模式名 |
| name | 表名 |

**返回值**

返回一个结果集或失败返回 FALSE。

21.**dm\_foreignkeys**

**描述**

获取表的外键。

**格式**

```
resource dm_foreignkeys (resource $link_identifier, string $pk_qualifier, string $pk_owner, string $pk_table, string $fk_qualifier, string $fk_owner, string $fk_table)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| pk\_qualifier | 主键库名 |
| pk\_owner | 主键模式名 |
| pk\_table | 主键表名 |
| fk\_qualifier | 外键库名 |
| fk\_owner | 外键模式名 |
| fk\_table | 外键表名 |

**返回值**

返回一个结果集或失败返回 FALSE。

22.**dm\_procedures**

**描述**

列出 DM 数据库中的全部过程或指定的过程。

**格式**

```
resource dm_procedures (resource $link_identifier )
```

或

```
resource dm_procedures (resource $link_identifier, string $qualifier, string $owner, string $name )
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| qualifier | 库名 |
| owner | 模式名，支持使用通配符匹配方式："%" 来匹配零到多个字符，"\_" 来匹配单个字符 |
| name | 过程名，支持使用通配符匹配方式："%" 来匹配零到多个字符，"\_" 来匹配单个字符 |

**返回值**

在获取成功时返回一个资源标识符，出错时返回 FALSE。

23.**dm\_procedurecolumns**

**描述**

列出 DM 数据库中过程的列。

**格式**

```
resource  dm_procedurecolumns ( resource $link_identifier )
```

或

```
resource dm_procedurecolumns (resource $link_identifier, string $qualifier, string $owner, string $proc, string $column)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| qualifier | 库名 |
| owner | 模式名 |
| proc | 过程名 |
| column | 列名 |

**返回值**

在获取成功时返回一个资源标识符，出错时返回 FALSE。

### 6.3.3 PHP 8.X 接口

下面是 PHP 8.X 中和 PHP 7.X 同名的接口，但是功能或参数等和 PHP 7.X 略有不同。

1. **dm\_tables**

**描述**

列出 DM 数据库中的表。

**格式**

```
resource dm_tables (resource $link [, string $qualifier [, string $owner [, string $name [, string $types]]]] )
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link | \[IN\]连接句柄 |
| qualifier | 库名，仅支持取值为 NULL 或空串 |
| owner | 模式名 |
| name | 表名 |
| types | 表 or 视图。值：SYSTEM TABLE，TABLE，VIEW |

**返回值**

在获取成功时返回一个资源标识符，出错时返回 FALSE。可代替 PHP 5.x 中的 dm\_list\_tables。

2. **dm\_columns**

**描述**

列出 DM 数据库中的列。

**格式**

```
resource dm_columns (resource $link[, string $qualifier [, string $schema [, string $table_name [, string $column_name]]]])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link | \[IN\]连接句柄 |
| qualifier | 库名，仅支持取值为 NULL 或空串 |
| schema | 模式名 |
| table\_name | 表名 |
| column\_name | 列名过滤格式，如 % |

**返回值**

在获取成功时返回一个资源标识符，出错时返回 FALSE。

3. **dm\_statistics**

**描述**

获取表及其索引的信息。

**格式**

```
resource dm_statistics (resource $link_identifier, string $qualifier, string $owner, string $table_name, int $unique, int $accuracy)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| qualifier | 库名，仅支持取值为 NULL 或空串 |
| owner | 模式名 |
| table\_name | 表名 |
| unique | unique 属性。取值：   DSQL\_INDEX\_UNIQUE 表示只返回 unique 索引   DSQL\_INDEX\_ALL 表示返回所有索引 |
| accuracy | 忽略 |

**返回值**

返回一个结果集或失败返回 FALSE。

4. **dm\_primarykeys**

**描述**

获取表的主键。

**格式**

```
resource dm_primarykeys (resource $link_identifier, string $qualifier, string $owner, string $table)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| qualifier | 库名，仅支持取值为 NULL 或空串 |
| owner | 模式名 |
| table | 表名 |

**返回值**

返回一个结果集或失败返回 FALSE。

5. **dm\_autocommit**

**描述**

设置事务是否为自动提交。

**格式**

```
int dm_autocommit (resource $link_identifier, bool $flag)
或
bool dm_autocommit (resource $link_identifier, bool $flag)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| flag | 处理标识，设置事务是否为自动提交，取值范围：   1：是   0：否   null：返回自动提交状态 |

**返回值**

成功返回 TRUE，失败返回 FALSE。flag 可以设置为 null，此时会返回自动提交状态，自动提交会返回 1，否则会返回 0。

6. **dm\_columnprivileges**

**描述**

列出列的权限。

**格式**

```
resource dm_columnprivileges (resource $link_identifier, string $qualifier, string $owner, string $name, string $column_name)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| qualifier | 库名，仅支持取值为 NULL 或空串 |
| owner | 模式名 |
| table | 表名 |
| column\_name | 列名 |

**返回值**

返回一个结果集或失败返回 FALSE。

7. **dm\_tableprivileges**

**描述**

列出表的权限。

**格式**

```
resource dm_tableprivileges (resource $link_identifier, string $qualifier, string $owner, string $name)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| qualifier | 库名，仅支持取值为 NULL 或空串 |
| owner | 模式名 |
| name | 表名 |

**返回值**

返回一个结果集或失败返回 FALSE。

8. **dm\_foreignkeys**

**描述**

获取表的外键。

**格式**

```
resource dm_foreignkeys (resource $link_identifier, string $pk_qualifier, string $pk_owner, string $pk_table, string $fk_qualifier, string $fk_owner, string $fk_table)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| pk\_qualifier | 主键库名，仅支持取值为 NULL 或空串 |
| pk\_owner | 主键模式名，可以为 NULL 或空串 |
| pk\_table | 主键表名，可以为 NULL 或空串 |
| fk\_qualifier | 外键库名，仅支持取值为 NULL 或空串 |
| fk\_owner | 外键模式名，可以为 NULL 或空串 |
| fk\_table | 外键表名，可以为空串或 NULL |

**返回值**

返回一个结果集或失败返回 FALSE。

9. **dm\_procedures**

**描述**

列出 DM 数据库中的全部过程或指定的过程。

**格式**

```
resource dm_procedures (resource $link_identifier)
```

或

```
resource dm_procedures (resource $link_identifier, string $qualifier, string $owner, string $name)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| qualifier | 库名，仅支持取值为 NULL 或空串 |
| owner | 模式名，支持使用通配符匹配方式："%" 来匹配零到多个字符，"\_" 来匹配单个字符，可以设置为 NULL，但不可以设置为空串 |
| name | 过程名，支持使用通配符匹配方式："%" 来匹配零到多个字符，"\_" 来匹配单个字符，可以设置为 NULL，但不可以设置为空串 |

**返回值**

在获取成功时返回一个资源标识符，出错时返回 FALSE。

10. **dm\_procedurecolumns**

**描述**

列出 DM 数据库中过程的列。

**格式**

```
resource dm_procedurecolumns (resource $link_identifier)
```

或

```
resource dm_procedurecolumns (resource $link_identifier, string $qualifier, string $owner, string $proc, string $column)
```

**参数**

| **参数** | **描述** |
| --- | --- |
| link\_identifier | \[IN\]连接标识符 |
| qualifier | 库名，仅支持取值为 NULL 或空串 |
| owner | 模式名，可以设置为 NULL，但不可以设置为空串 |
| proc | 过程名，可以设置为 NULL，但不可以设置为空串 |
| column | 列名，可以设置为 NULL，但不可以设置为空串 |

**返回值**

在获取成功时返回一个资源标识符，出错时返回 FALSE。

11. **dm\_connect**

**描述**

建立一个到 DM 服务器的连接。

在 dm.ukey\_login=0 且 dm.ssl\_login=0 时，最多设置 4 个参数，分别是：server、username、password 和 client\_flags。

在 dm.ukey\_login=0 且 dm.ssl\_login=1 时，最多设置 6 个参数，分别是:server、username、password、ssl\_path、ssl\_pwd 和 client\_flags。

在 dm.ukey\_login=1 且 dm.ssl\_login=0 时，最多设置 6 个参数，分别是:server、username、password、ukey\_name、ukey\_pin 和 client\_flags。

在 dm.ukey\_login=1 且 dm.ssl\_login=1 时，最多设置 8 个参数，分别是:server、username、password、ukey\_name、ukey\_pin、ssl\_path、ssl\_pwd 和 client\_flags。

**格式**

```
resource dm_connect ([string $server [, string $username [, string $password [, string $ukey_name [, string $ukey_pin[, string $ssl_path [, string $ssl_pwd [,bool $client_flags]]]]]]]])
```

**参数**

| **参数** | **描述** |
| --- | --- |
| server | \[IN\]服务器地址，格式为 IP:PORT:模式名，PORT 缺省为 5236，模式名缺省为用户名称。server 缺省使用 php.ini 中的配置 |
| username | \[IN\]用户名称，缺省使用 php.ini 中的配置 |
| password | \[IN\]用户密码，缺省使用 php.ini 中的配置 |
| ukey\_name | \[IN\]ukey 名，仅在 dm.ukey\_login=1 时可以设置该参数 |
| ukey\_pin | \[IN\]ukey 密码，仅在 dm.ukey\_login=1 时可以设置该参数 |
| ssl\_path | \[IN\]SSL 证书路径，仅在 dm.ssl\_login=1 时可以设置该参数 |
| ssl\_pwd | \[IN\]SSL 证书密码，仅在 dm.ssl\_login=1 时可以设置该参数 |
| client\_flags | 保留参数，不起作用 |

**返回值**

如果成功则返回一个连接标识，失败则返回 FALSE。用同样的参数第二次调用 dm\_connect 会建立新连接。

例 使用 dm\_connect 建立连接。

```
dm_connect("192.168.0.25:5236:PHPTEST", "SYSDBA", "Dmdba_123", 1);
或
dm_connect("192.168.0.25:5236:PHPTEST", "SYSDBA", "Dmdba_123", "dmukey1", "123456", 1);
或
dm_connect("192.168.0.25:5236:PHPTEST", "SYSDBA", "Dmdba_123", "/home/dmdbms/bin/client_ssl/SYSDBA", "123456", 1);
```

## 6.4 基本示例

利用 DM PHP 驱动程序进行编程的一般步骤为：

1. 利用 dm\_connect()建立同数据库的连接。
2. DM PHP 数据操作。数据操作主要分为两个方面，一个是更新操作，例如更新数据库、删除一行、创建一个新表等；另一个就是查询操作。dm\_query()执行完查询之后，会得到一个记录集。可以操作该对象来获得指定列的信息、读取指定行的某一列的值。
3. 释放资源。在操作完成之后，用户需要释放系统资源，主要是关闭结果集、关闭语句对象，释放连接。

下面用具体的编程实例来展示利用 DM PHP 对示例数据库 BOOKSHOP，以产品信息表 product 的增加、删除、修改、查询为例子进行数据库操作的基本步骤。

1. **增加记录**
```
<?php
    //连接选择数据库 
    $link = dm_connect("localhost", "SYSDBA", "sysDBA*00")
        or die("Could not connect : " . dm_error()); 
    print "Connected successfully";
    //执行 SQL 查询 
    $query = " INSERT INTO production.product(name,author,publisher,publishtime,
product_subcategoryid,productno,safetystocklevel,originalprice,nowprice,
discount,description,photo,sellstarttime) 
VALUES('三国演义','罗贯中','中华书局','2005-04-01','4','9787101046121','10',
'19.0000','15.2000','8.0','《三国演义》是中国第一部长篇章回体小说!',null,'2006-03-20')";
    $result = dm_query($query) or die("Query failed : " . dm_error()); 
    //释放资源
    dm_free_result($result);
    //断开连接
    dm_close($link);
?>
```
2. **修改数据**
```
<?php
    //连接选择数据库
    $link = dm_connect("localhost", "SYSDBA", "sysDBA*00")
        or die("Could not connect : " . dm_error()); 
    print "Connected successfully";
    //执行 SQL 查询
    $query = " UPDATE production.product SET TYPE =1000 WHERE productid = 10";
    $result = dm_query($query) or die("Query failed : " . dm_error()); 
    //释放资源
    dm_free_result($result);
    //断开连接
    dm_close($link);
?>
```
3. **删除记录**
```
<?php
    //连接选择数据库
    $link = dm_connect("localhost", "SYSDBA", "sysDBA*00")
        or die("Could not connect : " . dm_error()); 
    print "Connected successfully";
    //执行 SQL 查询 
    $query = " DELETE FROM production.product WHERE productid = 10";
    $result = dm_query($query) or die("Query failed : " . dm_error()); 
    //释放资源
    dm_free_result($result);
    //断开连接
    dm_close($link);
?>
```
4. **查询记录**
```
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
 <style type="text/css">
<!--
body,td,th {
    font-size: 12px;
}
-->
</style></head>
<body><?php
    //连接选择数据库 
    $link = dm_connect("localhost", "SYSDBA", "sysDBA*00")
        or die("Could not connect : " . dm_error()); 
    print "Connected successfully";
    //执行 SQL 查询 
    $query = " select * from production.product";
    $result = dm_query($query) or die("Query failed : " . dm_error()); 
    //在 HTML 中打印结果
    print "<table border=\"1\" cellspacing=\"1\" cellpadding=\"1\">\n";
    while ($line = dm_fetch_array($result, DM_ASSOC)) {
        print "\t<tr>\n";
        foreach ($line as $col_value) {
            print "\t\t<td>$col_value</td>\n";
        }
        print "\t</tr>\n";
    }
    print "</table>\n";
    //释放资源
    dm_free_result($result);
    //断开连接
    dm_close($link);
?>
 </body>
</html>
```

**5\. 存储过程**

运行程序，启动达梦数据库服务器并创建用于修改产品信息的存储过程。存储过程代码如下：

```
create or replace procedure "PRODUCTION"."updateProduct"
(
  v_id int,
  v_name varchar(50)
)
as
begin
  UPDATE production.product SET name = v_name WHERE productid = v_id;
end;
```

在 PHP 里得到返回的结果集。

```
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
 <style type="text/css">
<!--
body,td,th {
    font-size: 12px;
}
-->
</style></head>
<body><?php
    //连接选择数据库
    $link = dm_connect("localhost", "SYSDBA", "sysDBA*00")
        or die("Could not connect : " . dm_error()); 
    print "Connected successfully";
    dm_select_db("system") or die("Could not select database");
    // 执行 SQL 查询
    $query = " CALL production.updateProduct(1,'红楼梦')";
    $result = dm_query($query) or die("Query failed : " . dm_error()); 
     //释放资源
    dm_free_result($result);
    //断开连接
    dm_close($link);
?>
</body>
</html>
```
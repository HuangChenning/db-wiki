---
title: "附录"
book: "DM8 数据共享集群"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dsc-appendix.html
tags:
  - dameng
  - dm8
  - dsc
---

## 19.1 DMASMAPI 接口

DMASMAPI 是连接 DMASMSVR 执行操作的接口，所有使用 DMASM 文件系统的程序都使用 DMASMAPI 接口连接 DMASMSVR。

返回值分为三种类型：正数，0 和负数。0 表示正常；正数为警告信息；负数为错误信息，对应的错误码请参考 19.1.3 错误码汇编 。

### 19.1.1 DMASMAPI 接口说明

DMASMAPI 提供的接口如下：

#### 1\. dmasm\_sys\_init

**函数原型：**

```
ASMRETURN
dmasm_sys_init(
    sdbyte*            err_desc,
    udint4*            err_len,
    udint4            char_code,
    udint4            lang_id
)
```

**功能说明：**

环境初始化接口。使用 ASMAPI 接口，必须第一个调用 dmasm\_sys\_init 接口。

**参数说明：**

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

char\_code：输入参数，编码。0：PG\_INVALID\_CODE；1：PG\_UTF8；2：PG\_GBK；3：PG\_BIG5；4：PG\_ISO\_8859\_9；5：PG\_EUC\_JP；6：PG\_EUC\_KR；7：PG\_KOI8R；8:PG\_ISO\_8859\_1；9：PG\_SQL\_ASCII；10：PG\_GB18030；11：PG\_ISO\_8859\_11；12：PG\_UTF16。-1 表示使用默认编码。

lang\_id ：输入参数，语言。0：中文；1：英文；2：繁体中文。-1 表示使用默认语言。

#### 2\. dmasm\_sys\_deinit

**函数原型：**

```
void
dmasm_sys_deinit()
```

**功能说明：**

环境销毁接口。使用 ASMAPI 接口结束时，调用 dmasm\_sys\_deinit 销毁资源。

#### 3\. dmasm\_alloc\_con

**函数原型：**

```
ASMRETURN
dmasm_alloc_con(
    asmcon_handle*    con,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

申请并初始化连接句柄。返回申请的连接句柄。

**参数说明：**

con：输入参数，连接句柄。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 4\. dmasm\_free\_con

**函数原型：**

```
void
dmasm_free_con(
    asmcon_handle    con_in
)
```

**功能说明：**

释放连接句柄。

**参数说明：**

con\_in：输入参数，连接句柄。

#### 5\. dmasm\_connect

**函数原型：**

```
ASMRETURN
dmasm_connect(
    asmcon_handle    con_in,
    sdbyte*            username,
    sdbyte*            password,
    sdbyte*            hostname,
    udint2            portnum,
    asmbool*        con_is_local,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

登录接口。ASMSVR 允许本地连接和远程连接，但是 dmserver 仅允许本地连接，依据 con\_is\_local 判断是否远程连接。

**参数说明：**

con\_in：输入参数，连接句柄。

username：输入参数，用户名。

password：输入参数，密码。

hostname：输入参数，主机 ip 或主机名。

portnum：输入参数，主机监听端口号。

con\_is\_local：输出参数，标识远程或本地登录。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 6\. dmasm\_close\_con

**函数原型：**

```
void
dmasm_close_con(
    asmcon_handle    con_in
)
```

**功能说明：**

关闭连接。关闭连接句柄，释放资源。

**参数说明：**

conn\_in：输入参数，连接句柄。

#### 7\. dmasm\_get\_n\_group

**函数原型：**

```
ASMRETURN
dmasm_get_n_group(
    asmcon_handle    conn_in,
    udint2*            num,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

获取 ASM Disk Group 个数。获取有多少个磁盘组。

**参数说明：**

conn\_in：输入参数，连接句柄。

num：输出参数，磁盘组个数。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 8\. dmasm\_get\_group\_id\_arr

**函数原型：**

```
ASMRETURN
dmasm_get_group_id_arr(
    asmcon_handle   con_in,
    udint2*         id_arr,    
    udint4*         au_size_arr,
    udint4*         ex_size_arr,    
    udint2          arr_size,
    udint2*         num,        
    sdbyte*         err_desc,
    udint4*         err_len
)
```

**功能说明：**

获取 ASM Disk Group ID 数组。配合 dmasm\_get\_n\_group 使用，获取所有 Disk Group ID。

**参数说明：**

conn\_in：输入参数，连接句柄。

id\_arr：输出参数，磁盘 ID 数组。

au\_size\_arr：输出参数，无实际意义。

ex\_size\_arr：输出参数，无实际意义。

arr\_size：输入参数，数组最大长度。

num：输出参数，返回数组长度。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 9\. dmasm\_get\_disk\_id\_arr\_by\_group

**函数原型：**

```
ASMRETURN
dmasm_get_disk_id_arr_by_group(
    asmcon_handle    con_in,
    udint2            group_id,
    udint2*            id_arr,
    udint2            arr_size,
    udint2*            n_disk,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

获取磁盘组内磁盘 ID 数组。根据磁盘组 ID 获取磁盘组内包含的所有磁盘 ID。

**参数说明：**

conn\_in：输入参数，连接句柄。

group\_id：输入参数，磁盘组 ID。

id\_arr：输出参数，磁盘 ID 数组。

arr\_size：输入参数，数组最大长度。

n\_disk：输出参数，返回数组长度。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 10\. dmasm\_get\_disk\_info

**函数原型：**

```
ASMRETURN
dmasm_get_disk_info(
    asmcon_handle      conn_in,
    udint2              group_id,
    udint4              disk_id,
    sdbyte*             path,    
    udint2              path_buflen,
    sdbyte*             name,
    udint2              name_buflen,
    sdbyte*             frp_name,   
    udint2              frp_buflen,   
    sdbyte*             status,   
    udint2              status_buflen, 
    udint4*             size,    
    udint4*             free_auno,
    sdbyte*             create_time,
    sdbyte*             modify_time,
    sdbyte*             uuid_str,
    sdbyte*             err_desc,
    udint4*             err_len
)
```

**功能说明：**

获取 ASM 磁盘详细信息。根据磁盘组 ID 和磁盘 ID 获取 ASM 磁盘详细信息。

**参数说明：**

conn\_in：输入参数，连接句柄。

group\_id：输入参数，磁盘组 ID。

disk\_id：输入参数，磁盘 ID。

path：输出参数，磁盘路径。

path\_buflen：输入参数，path 缓冲区长度。

name：输出参数，磁盘名称。

name\_buflen：输入参数，name 缓冲区长度。

frp\_name：输出参数，无实际意义。

frp\_buflen：输入参数，无实际作用。

status：输出参数，无实际意义。

status\_buflen：输入参数，无实际作用。

size：输出参数，磁盘大小，单位 MB。

free\_auno：输出参数，最大 au 号。

create\_time：输出参数，磁盘创建时间。

modify\_time：输出参数，磁盘最近一次修改时间。

uuid\_str：输出参数，磁盘唯一标识。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 11\. dmasm\_create\_diskgroup

**函数原型：**

```
ASMRETURN
dmasm_create_diskgroup(
    asmcon_handle    conn_in,
    sdbyte*            group_name,
    sdbyte*            disk_path_in,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

创建 ASM Disk Group。使用 disk\_path 所指的 ASM 磁盘创建 ASM 磁盘组。

**参数说明：**

conn\_in：输入参数，连接句柄。

group\_name：输入参数，磁盘组名。

disk\_path\_in：输入参数，磁盘路径。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 12\. dmasm\_add\_disk\_to\_diskgroup

**函数原型：**

```
ASMRETURN
dmasm_add_disk_to_diskgroup(
    asmcon_handle    conn_in,
    sdbyte*            group_name,
    sdbyte*            disk_path_in,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

磁盘组增加磁盘。往磁盘组增加 ASM 磁盘。

**参数说明：**

conn\_in：输入参数，连接句柄。

group\_name：输入参数，磁盘组名。

disk\_path\_in：输入参数，磁盘路径。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 13\. dmasm\_drop\_diskgroup\_by\_name

**函数原型：**

```
ASMRETURN
dmasm_drop_diskgroup_by_name(
    asmcon_handle    conn_in,
    sdbyte*            group_name,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

删除磁盘组。ASM 文件系统不支持单独删除 ASM 磁盘，只能删除整个 ASM 磁盘组

**参数说明：**

conn\_in：输入参数，连接句柄。

group\_name：输入参数，磁盘组名。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 14\. dmasm\_file\_create

**函数原型：**

```
ASMRETURN
dmasm_file_create(
    asmcon_handle       conn_in,
    asmbool    p_flag,
    sdbyte*             filepath_in, 
    udint8    filesize,
    asm_fhandle_t*      fil_handle,
    asmbool              need_init,  
    udint2              striping_size, 
    udbyte              redundancy_type,
    sdbyte*             err_desc,
    udint4*             err_len
)
```

**功能说明：**

创建 ASM 文件。在 ASM 文件系统中创建 ASM 文件，如果文件父亲目录不存在，并且 p\_flag 为 TRUE 的情况，会自动创建父目录，否则会报错。

**参数说明：**

conn\_in：输入参数，连接句柄。

p\_flag：输入参数，创建父目录标记。

filepath\_in：输入参数，文件路径。

filesize：输入参数，文件大小，单位 Byte。

fil\_handle：输出参数，文件句柄。

need\_init：输入参数，是否需要初始化。

striping\_size：输入参数，无实际作用。

redundancy\_type：输入参数，无实际作用。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 15\. dmasm\_file\_open

**函数原型：**

```
ASMRETURN
dmasm_file_open(
    asmcon_handle    conn_in,
    sdbyte*            filepath_in,
    asm_fhandle_t*    fhandle,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

打开 ASM 文件，获取 ASM 文件句柄。已经打开的文件，不能被删除。

**参数说明：**

conn\_in：输入参数，连接句柄。

filepath\_in：输入参数，文件路径。

fhandle：输入参数，文件句柄。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 16\. dmasm\_file\_trunc

**函数原型：**

```
ASMRETURN
dmasm_file_trunc(
    asmcon_handle    conn_in,
    asm_fhandle_t    fhandle,
    udint8            truncate_size,
    udint8*            real_size,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

截断 ASM 文件。将 ASM 文件截断到 truncate\_size，如果 truncate\_size 小于文件大小，文件会被截断到 truncate\_size；如果 truncate\_size 大于文件大小，文件大小不变，接口返回 EC\_SUCCESS。

**参数说明：**

conn\_in：输入参数，连接句柄。

fhandle：输入参数，文件句柄。

truncate\_size：输入参数，截断后的大小，单位 Byte。

real\_size：输出参数，执行后实际大小，单位 Byte。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 17\. dmasm\_file\_extend

**函数原型：**

```
ASMRETURN
dmasm_file_extend(
    asmcon_handle    conn_in,
    asm_fhandle_t    fhandle,
    udint8            offset,
    udint8            extend_size,
    udint4          need_init,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

扩展 ASM 文件。将文件从 offset 偏移处，扩展 extent\_size 大小，最终实际大小为 offset+extent\_size。如果 offset+extend\_size 大于文件大小，文件会被扩展到 offset+extend\_size 大小；如果 offset+extend\_size 小于文件大小，直接返回成功。

**参数说明：**

conn\_in：输入参数，连接句柄。

fhandle：输入参数，文件句柄。

offset：输入参数，起始偏移。

extend\_size：输入参数，扩展大小。

need\_init：输入参数，是否需要初始化。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 18\. dmasm\_file\_close

**函数原型：**

```
void
dmasm_file_close(
    asmcon_handle    conn_in,
    asm_fhandle_t    fhandle
)
```

**功能说明：**

关闭 ASM 文件。关闭打开的 ASM 文件

**参数说明：**

conn\_in：输入参数，连接句柄。

fhandle：输入参数，文件句柄。

#### 19\. dmasm\_file\_delete

**函数原型：**

```
ASMRETURN
dmasm_file_delete(
    asmcon_handle    conn_in,
    sdbyte*            filepath_in,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

删除 ASM 文件。删除 ASM 文件，正在被使用的 ASM 文件不能被删除。

**参数说明：**

conn\_in：输入参数，连接句柄。

filepath\_in：输入参数，文件路径。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 20\. dmasm\_file\_read\_by\_offset

**函数原型：**

```
ASMRETURN
dmasm_file_read_by_offset(
    asmcon_handle    conn_in,
    asm_fhandle_t    fhandle,
    udint8            offset,
    sdbyte*            buffer,
    udint4            bytes_to_read,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

从 ASM 文件读取数据。从 ASM 文件 offset 偏移读取 bytes\_to\_read 大小的内容到缓冲区 buffer，调用者保证缓冲区够用。因为裸设备读写限制，offset, buffer, bytes\_to\_read 都必须能被 512 整除，否则会报错。

**参数说明：**

conn\_in：输入参数，连接句柄。

fhandle：输入参数，文件句柄。

offset：输入参数，起始偏移。

buffer：输入参数，缓冲区。

bytes\_to\_read：输入参数，读取数据大小，单位 Byte。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 21\. dmasm\_file\_read\_by\_offset\_normal

**函数原型：**

```
ASMRETURN
dmasm_file_read_by_offset_normal(
    asmcon_handle    conn_in,
    asm_fhandle_t    fhandle,
    udint8            offset,
    sdbyte*            buffer,
    udint4            bytes_to_read,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

从 ASM 文件读取数据。从 ASM 文件 offset 偏移读取 bytes\_to\_read 大小的内容到缓冲区 buffer，调用者保证缓冲区够用。该接口支持 offset,buffer,bytes\_to\_read 不是 512 整数倍，但是性能比 dmasm\_file\_read\_by\_offset 慢。

**参数说明：**

conn\_in：输入参数，连接句柄。

fhandle：输入参数，文件句柄。

offset：输入参数，起始偏移。

buffer：输入参数，缓冲区。

bytes\_to\_read：输入参数，写取数据大小，单位 Byte。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 22\. dmasm\_file\_write\_by\_offset

**函数原型：**

```
ASMRETURN
dmasm_file_write_by_offset(
    asmcon_handle    conn_in,
    asm_fhandle_t    fhandle,
    udint8            offset,
    sdbyte*            buffer,
    udint4            bytes_to_write,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

将数据写入 ASM 文件。将缓冲区中的内容写入 ASM 文件，从 offset 偏移开始。因为裸设备读写限制，offset，buffer 地址，bytes\_to\_write 都必须能被 512 整除。

**参数说明：**

conn\_in：输入参数，连接句柄。

fhandle：输入参数，文件句柄。

offset：输入参数，起始偏移。

buffer：输入参数，缓冲区。

bytes\_to\_write：输入参数，写数据大小，单位 Byte。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 23\. dmasm\_file\_write\_by\_offset\_normal

**函数原型：**

```
ASMRETURN
dmasm_file_write_by_offset_normal(
    asmcon_handle    conn_in,
    asm_fhandle_t    fhandle,
    udint8            offset,
    sdbyte*            buffer,
    udint4            bytes_to_write,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

将数据写入 ASM 文件。将缓冲区中的内容写入 ASM 文件，从 offset 偏移开始。该接口支持 offset,buffer,bytes\_to\_write 不是 512 倍数，但是性能比 dmasm\_file\_write\_by\_offset 慢。

**参数说明：**

conn\_in：输入参数，连接句柄。

fhandle：输入参数，文件句柄。

offset：输入参数，起始偏移。

buffer：输入参数，缓冲区。

bytes\_to\_write：输入参数，写数据大小，单位 Byte。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 24\. dmasm\_file\_copy

**函数原型：**

```
ASMRETURN
dmasm_file_copy(
    asmcon_handle    conn_in,
    sdbyte*            source_in,
    sdbyte*            dest_in,
    asmbool            bOverwriteIfExists,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

文件拷贝操作。支持 ASM 文件拷贝到 ASM 文件；ASM 文件拷贝到普通文件系统文件；普通文件系统文件拷贝到 ASM 文件系统；不支持普通文件拷贝到普通文件。bOverwriteIfExists：0 或者 NULL 表示不覆盖，其他非 0 值表示覆盖。

**参数说明：**

conn\_in：输入参数，连接句柄。

source\_in：输入参数，源文件路径。必须是全路径，不能是相对路径。

dest\_in：输入参数，目标文件路径。必须是全路径，不能是相对路径。

bOverwriteIfExists：输入参数，如果目标存在是否删除。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 25\. dmasm\_dir\_create

**函数原型：**

```
ASMRETURN
dmasm_dir_create(
    asmcon_handle    conn_in,
    asmbool            p_flag,
    sdbyte*            fdir_in,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

创建目录。ASM 文件系统创建目录，当 p\_flag=TRUE 时会级联创建父目录，否则父目录不存在会报错。

**参数说明：**

conn\_in：输入参数，连接句柄。

p\_flag：输入参数，是否级联创建父目录。

fdir\_in：输入参数，目录路径。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 26\. dmasm\_dir\_delete

**函数原型** ：

```
ASMRETURN
dmasm_dir_delete(
    asmcon_handle    conn_in,
    sdbyte*            fdir_in,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

删除目录，以及目录下面所有的文件。

**参数说明：**

conn\_in：输入参数，连接句柄。

fdir\_in：输入参数，目录路径。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 27\. dmasm\_get\_file\_num\_by\_group

**函数原型：**

```
ASMRETURN
dmasm_get_file_num_by_group(
    asmcon_handle    conn_in,
    udint2            group_id,
    udint4*            num,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

获取磁盘组内总的文件个数。根据磁盘组 ID 获取总的文件个数，包括文件和目录。

**参数说明：**

conn\_in：输入参数，连接句柄。

group\_id：输入参数，磁盘组的 ID 。

num ：输出参数，文件的个数。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 28\. dmasm\_get\_file\_info

**函数原型：**

```
ASMRETURN
dmasm_get_file_info(
    asmcon_handle    conn_in,
    asm_fhandle_t    file_id,
    ASM_FILE_ATTR*    fattr_out,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

获取 ASM 文件详细信息。

ASM\_FILE\_ATTR 包括：

type：目录标记，整型。1 表示文件，2 表示目录。

name：文件名称，字符型。

full\_path：完整路径，字符型。

size：文件大小，整型，单位 Byte。目录忽略此字段。

c\_time：创建时间，time\_t 类型。

m\_time：修改时间，time\_t 类型。

group\_id：所在磁盘组编号，整型。

disk\_id：inode 项所在磁盘 ID，整型。

disk\_auno：inode 项所在磁盘 AU 编号，整型。

offset：inode 项 AU 偏移，整型。

**参数说明：**

conn\_in：输入参数，连接句柄。

file\_id：输入参数，打开的文件句柄。

fattr\_out：输出参数，文件属性结构。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 29\. dmasm\_get\_group\_info\_by\_name

**函数原型：**

```
ASMRETURN
dmasm_get_group_info_by_name(
    asmcon_handle    con_in,
    sdbyte*            group_name,
    udint2*            group_id,
    udint2*            status,
    udint2*            n_disk,
    udint4*            total_size,
    udint4*            free_size,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

通过磁盘组名获取磁盘组详细信息。

**参数说明：**

con\_in：输入参数，连接句柄。

group\_name：输入参数，磁盘组名字。

group\_id：输出参数，磁盘组 ID。

status：输出参数，磁盘组状态(1:正在创建中 2：正常的 3：正在删除中)。

n\_disk：输出参数，磁盘数。

total\_size：输出参数，磁盘组大小，单位 AU。

free\_size：输出参数，磁盘组空闲大小，单位 AU。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 30\. dmasm\_get\_group\_info\_by\_id

**函数原型：**

```
ASMRETURN
dmasm_get_group_info_by_id(
    asmcon_handle    con_in,
    udint2            group_id,
    sdbyte*            group_name,
    udint2            name_buflen,
    udint2*            status,
    udint2*            n_disk,
    udint4*            total_size,
    udint4*            free_size,
    udint4*            au_size,   
    byte*           n_copy,     
    udint4*         redo_size,   
    udint2*         rbl_stat,
    udint2*         rbl_pwr,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

通过磁盘组 ID 获取磁盘组详细信息。

**参数说明：**

con\_in：输入参数，连接句柄。

group\_id：输入参数，磁盘组 ID。

group\_name：输出参数，磁盘组名字。

name\_buflen：输入参数，磁盘组的 buf 长度

status：输出参数，磁盘组状态(1:正在创建中 2：正常的 3：正在删除中)。

n\_disk：输出参数，磁盘数。

total\_size：输出参数，磁盘组大小，单位 AU。

free\_size：输出参数，磁盘组空闲大小，单位 AU。

au\_size：输出参数，无实际意义。

n\_copy：输出参数，无实际意义。

redo\_size：输出参数，无实际意义。

rbl\_stat：输出参数，无实际意义。

rbl\_pwr：输出参数，无实际意义。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 31\. dmasm\_dir\_get\_first

**函数原型** ：

```
ASMRETURN
dmasm_dir_get_first(
    asmcon_handle    conn_in,
    sdbyte*            path_in,
    sdbyte*            suffix,
    asm_dhandle_t*    dir_handle_out,
    ASM_FILE_ATTR*    fattr_out,
    asmbool*        exist_flag,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

获取目录下第一个文件信息。

**参数说明：**

conn\_in：输入参数，连接句柄。

path\_in：输入参数，目录路径。

suffix：输入参数，指定扩展名关键字，如：”.log”。用于取出以指定关键字作为扩展名的文件。

dir\_handle\_out：输出参数，打开的目录句柄。

fattr\_out：输出参数，文件属性结构。

exist\_flag：输出参数，是否存在。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 32\. dmasm\_dir\_get\_next

**函数原型：**

```
ASMRETURN
dmasm_dir_get_next(
    asmcon_handle    conn_in,
    asm_dhandle_t    dir_handle,
    sdbyte*            path_in,
    sdbyte*            suffix,
    ASM_FILE_ATTR*    fattr_out,
    asmbool*        exist_flag,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

获取目录下下一个文件信息，须配合函数 dmasm\_dir\_get\_first 使用。

**参数说明：**

conn\_in：输入参数，连接句柄。

dir\_handle：输入参数，打开的目录句柄。

path\_in：输入参数，目录路径，须与目录句柄 dir\_handle 中打开的 path\_in 保持一致。

suffix：输入参数，指定扩展名关键字，如：”.log”。用于取出以指定关键字作为扩展名的文件。

fattr\_out：输出参数，文件属性结构。

exist\_flag：输出参数，是否存在。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 33\. dmasm\_dir\_close

**函数原型：**

```
ASMRETURN
dmasm_dir_close(
    asmcon_handle    conn_in,
    asm_dhandle_t    dir_handle,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

关闭目录。

**参数说明：**

con\_in：输入参数，连接句柄。

dir\_handle：输入参数，打开的目录句柄。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 34\. dmasm\_file\_attributes\_get

**函数原型：**

```
ASMRETURN
dmasm_file_attributes_get(
    asmcon_handle    conn_in,
    sdbyte*            path,
    ASM_FILE_ATTR*    fattr_out,
    sdbyte*            err_desc,
    udint4*            err_len
)
```

**功能说明：**

根据文件路径获取文件详细信息。

**参数说明：**

conn\_in：输入参数，连接句柄。

path：输入参数，路径。

fattr\_out：输出参数，文件属性结构。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 35\. dmasm\_file\_is\_exist

**函数原型：**

```
ASMRETURN
dmasm_file_is_exist(
    asmcon_handle   conn_in,
    sdbyte*         path,
    sdbyte*         err_desc,
    udint4*         err_len
)
```

**功能说明：**

判断在 ASM 文件系统中，以 path 为文件路径的文件是否存在。

**参数说明：**

conn\_in：输入参数，连接句柄。

path：输入参数，文件路径。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

### 19.1.2 返回值说明

返回值分为三种类型：正数，0 和负数。0 表示正常；正数为警告信息；负数为错误信息，对应的错误码请参考 19.1.3 错误码汇编 。

### 19.1.3 错误码汇编

DMASMAPI 的错误码值域从-11000 开始。具体可参考 V$ERR\_INFO。

### 19.1.4 编程示例

下面举一个简单的例子，展示 DMASMAPI 的使用方法。若本示例在编译过程中出现实参过多或者变量未声明等问题，可查询相应版本的 DMASMAPI 接口使用手册，适当增减参数或者将变量改为实际值。

```
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "asmapi2.h"

#define TRUE        1
#define FALSE       0

#define IS_SUCCESS(code)    ((sdint4)code >= 0)
#define RET_IF_ERR_EX(c, act) \
    { if (!IS_SUCCESS(c)) { {act;} return (c); }}

/*运行前修改file_name username passwd ip port
  镜像不支持远程写，示例程序需要和服务端在同一台机器
  LINUX下编译
  gcc -DLINUX -I/home/test/include test.c -L. -ldmasmapi -o demo
  -I:指定头文件目录，本例中需要指定asmapi2.h头文件所在目录
  -L(大写L):指定库搜索路径
  -l(小写L):指定库名
  -D:定义预处理宏*/
int
main(
    int             argc,
    char*           argv[]
)
{
    int             code = 0;
    char            err_desc[1024];
    int             err_len;
    asm_fhandle_t   fil_handle;
    void*           conn;
    char*           wbuf        = "hello asm";
    char            rbuf[10];
    int             len;
    int             file_size = 20;       //单位字节
int             offset = 0;
    int             strip_size  = 0;        //条带大小
    int             redundancy_type = 1;    //镜像类型
    char*           username = "ASMSYS";
    char*           passwd = "DCRpsd_123";
char*           file_name = "+DATA/test1.dta";
    char*           ip = "192.168.100.118";
int             port = 10060;

#ifdef WIN32
    /*windows环境需要添加附加依赖项ws2_32.lib*/
    WSADATA WsaData;
    if (SOCKET_ERROR == WSAStartup(0x0101, &WsaData))
    {
        fprintf(stderr, "WSAStartup Failed\n");
        exit(-1);
    }
#endif

    err_len         = sizeof(err_desc);
    len             = (int)strlen(wbuf);

    code = dmasm_sys_init(err_desc, &err_len, -1, 1);
    if (!IS_SUCCESS(code))
    {
        fprintf(stderr, "dmasm_sys_init error:[%s]\n", err_desc);
        return -1;
    }

    /* 分配连接句柄 */
    code = dmasm_alloc_con(&conn, err_desc, &err_len);
    if (!IS_SUCCESS(code))
    {
        fprintf(stderr, "dmasm_alloc_con error:[%s]\n", err_desc);
        return -1;
    }

    /* 登录asmsvr，本地登录不校验密码，可以输入任意字符串，远程登录会校验用户名密码*/
    code = dmasm_connect(conn, username, passwd, ip, port, NULL, err_desc, &err_len);
    if (!IS_SUCCESS(code))
    {
        fprintf(stderr, "dmasm_connect error:[%s]\n", err_desc);
        return -1;
    }

    /* 文件存在直接打开 */
    if (dmasm_file_is_exist(conn, file_name, err_desc, &err_len) == TRUE)
    {
        code = dmasm_file_open(conn, file_name, &fil_handle, err_desc, &err_len);
        RET_IF_ERR_EX(code, goto fun_end);
    }
    else
    {
        /* 在已有的磁盘组内创建asm文件， */
        code = dmasm_file_create(conn, 1, file_name, file_size, &fil_handle, FALSE, strip_size, redundancy_type, err_desc, &err_len);
        if (!IS_SUCCESS(code))
        {
            fprintf(stderr, "dmasm_file_create error code:%d [%s]\n", code, err_desc);
            goto fun_end;
        }
    }

    /* 写文件 */
    code = dmasm_file_write_by_offset_normal(conn, fil_handle, offset, wbuf, len, err_desc, &err_len);
    if (!IS_SUCCESS(code))
    {
        fprintf(stderr, "dmasm_file_write_by_offset_normal error code:%d [%s]\n", code, err_desc);
        goto fun_end;
    }

    /* 读文件 */
    code = dmasm_file_read_by_offset_normal(conn, fil_handle, offset, rbuf, len, err_desc, &err_len);
    if (!IS_SUCCESS(code))
    {
        fprintf(stderr, "dmasm_file_write_by_offset_normal error code:%d [%s]\n", code, err_desc);
        goto fun_end;
    }
    else
    {
        rbuf[len] = '\0';
        fprintf(stderr, "dmasm_file_write_by_offset_normal succ buf:%s\n", rbuf);
    }

fun_end:
    // 文件存在就关闭删除
    if (dmasm_file_is_exist(conn, file_name, err_desc, &err_len) == TRUE)
    {
        /* 关闭打开的文件句柄，否则删除会报错 */
        dmasm_file_close(conn, fil_handle);

        /* 删除文件 */
        code = dmasm_file_delete(conn, file_name, err_desc, &err_len);
        if (!IS_SUCCESS(code))
        {
            fprintf(stderr, "dmasm_file_delete error:[%s]\n", err_desc);
        }
    }

    dmasm_close_con(conn);
    dmasm_free_con(conn);
    dmasm_sys_deinit();
    return 0;
}
```

## 19.2 DMCSSM 接口

### 19.2.1 DLL 依赖库

监视器的 DLL 名称为 dmcssmon.dll（windows）和 libdmcssm.so（linux），使用监视器接口时必须加载，另外监视器 DLL 还依赖了其他的一些动态链接库，编程时需要将达梦 bin 目录的以下库拷贝到和 dmcssmon.dll 或 libdmcssm.so 相同目录下，也可以在加载动态链接库时直接指定 bin 目录，就不需要再拷贝库文件：

| **序号** | **WINDOWS** | **非 WINDOWS（LINUX 等）** |
| --- | --- | --- |
| 1 | dmcalc.dll | libdmcalc.so |
| 2 | dmcfg.dll | libdmcfg.so |
| 3 | dmcomm.dll | libdmcomm.so |
| 4 | dmcvt.dll | libdmcvt.so |
| 5 | dmcyt.dll | libdmcyt.so |
| 6 | dmdcr.dll | libdmdcr.so |
| 7 | dmelog.dll | libdmelog.so |
| 8 | dmmem.dll | libdmmem.so |
| 9 | dmmout.dll | libdmmout.so |
| 10 | dmos.dll | libdmos.so |
| 11 | dmsys.dll | libdmsys.so |
| 12 | dmutl.dll | libdmutl.so |

### 19.2.2 返回值说明

监视器接口总体的返回值策略为：小于 0 表示执行失败，其他值表示执行成功。

相关的错误码说明请参考 19.2.3 错误码汇编 ，也可借助 cssm\_get\_error\_msg\_by\_code 接口获取错误码对应的错误描述信息。

### 19.2.3 错误码汇编

| **错误码** | **解释** |
| --- | --- |
| \-1 | 普通错误 |
| \-2 | 无效的句柄 |
| \-3 | 初始化日志信息失败 |
| \-4 | 初始化系统信息失败 |
| \-5 | 读取 DMCSSM.INI 文件失败（路径错误或配置错误或没有权限） |
| \-6 | 无效的日志文件路径 |
| \-7 | 建立到所有 CSS 的连接失败，可能 CSS 都未启动，由用户决定是否忽略此错误码继续往下执行，如果不忽略此错误，认定初始化失败，则需要先销毁监视器环境，再释放操作句柄。 |
| \-8 | 非法的参数，参数为空或长度超长或值非法 |
| \-9 | 没有找到 code 对应的错误信息 |
| \-10 | 内存不足 |
| \-11 | 监视器已达到最大个数（同一套 DSC 集群最多允许同时启动 10 个监视器） |
| \-1001 | 用户自定义异常或者未知错误 |
| \-1003 | 根据 ep\_seqno 获取发送端口失败 |
| \-1004 | 到 dmcss 的连接断开 |
| \-1005 | 有消息正在发送中,您的命令当前不能执行 |
| \-1007 | 设置 CSS 的 MID 命令执行失败 |
| \-1009 | 监视器操作冲突 |
| \-1012 | CSS 执行失败 |
| \-1017 | 通知 CSS 执行命令失败 |
| \-1018 | 获取有效的 CSS 通信端口失败，CSS 尚未启动或监视器配置错误 |
| \-1019 | 无效的组名或尚未收到消息 |
| \-1020 | 接收 CSS 消息超时 |
| \-1022 | 非法的 DCR 类型 |
| \-1023 | 只有主 CSS 能执行该操作 |
| \-1024 | CSS 中没有找到指定类型的组信息 |
| \-1025 | 执行 OPEN FORCE 的组当前不是 SLAVE STARTUP 状态 |
| \-1026 | 无效的 EP 名称或尚未收到消息 |
| \-1027 | 未找到指定类型的组信息 |
| \-1028 | 检测到主 CSS 发生变化 |
| \-1029 | 当前不存在活动的 CSS |
| \-1031 | 通知 CSS 打开监控失败 |
| \-1033 | 通知 CSS 关闭监控失败 |
| \-1035 | 命令执行失败 |
| \-1036 | 组当前没有活动 EP |
| \-1037 | 当前存在有活动的 DB 节点，需要先退出对应的 DB 组，才允许退出 ASM 组 |
| \-1038 | 组中的 EP 已处于 ACTIVE 状态（只收集活动 CSS 对应的 EP），或者 CSS 配置有自动重启，请等待 CSS 自动检测重启 |
| \-1039 | 当前活动的 CSS 监控都已处于打开状态 |
| \-1040 | 当前活动的 CSS 监控都已处于关闭状态 |
| \-1041 | 获取 CSS 的通信端口失败 |
| \-1042 | 通知 CSS 执行 EP STARTUP 失败 |
| \-1045 | CSS 中没有找到指定组的信息 |
| \-1046 | CSS 对指定的组配置了自动重启，请等待 CSS 自动检测重启对应的 EP |
| \-1047 | EP 已经处于 ACTIVE 状态 |
| \-1048 | ASM 实例未处于 ACTIVE 状态 |
| \-1049 | ASM 组未处于 OPEN 状态 |
| \-1050 | 指定组中没有活动 EP |
| \-1051 | 当前存在有活动的 DB 节点，需要先退出对应的 DB 组 |
| \-1052 | CSS 监控处于关闭状态，不允许执行此命令 |
| \-1053 | CSS 类型的组不允许执行此命令 |
| \-1057 | 获取主 CSS 通信端口失败，主 CSS 尚未选出或 CSS 未启动或者监视器配置错误 |
| \-1058 | ASM 组没有活动节点或者活动节点不是 OPEN 状态，或者 ASM 组不是 OPEN 状态，不允许启动 DB 组 |
| \-1059 | 检测到主 CSS 发生变化，命令中断执行 |
| \-1065 | 关闭 CSS 监控失败 |
| \-1067 | 打开 CSS 监控失败 |
| \-1069 | 指定组不是 SLAVE STARTUP 状态，不允许执行 OPEN FORCE |
| \-1070 | CSS 监控处于打开状态，不允许手动执行此命令，请等待 CSS 自动处理 |
| \-1071 | CSS 当前正在做故障处理或故障恢复 |
| \-1072 | CSS 监控处于打开状态，不允许执行此命令 |
| \-1073 | 没有找到满足故障恢复条件的节点 |
| \-1074 | CSS 当前正在做故障处理或故障恢复 |
| \-1075 | 没有找到满足故障处理条件的节点 |
| \-1076 | 需要先对 ASM 组做故障处理 |
| \-1077 | CSS 对指定的组没有配置自动重启参数 |
| \-1078 | 监视器超时仍未等到组中的所有 EP 执行成功，命令执行失败 |
| \-1079 | 监视器超时仍未等到当前 EP 执行成功，命令执行失败 |
| \-1080 | 控制节点尚未选出，获取信息失败 |
| \-1081 | 无效的节点名或尚未收到消息 |
| \-1082 | 指定节点的组内序号非法 |
| \-1083 | 组中的 EP 不是活动状态 |
| \-1085 | 对应的 ASM 组中没有活动节点，无法执行故障处理 |
| \-1086 | 指定组中没有活动节点，无法执行故障处理 |
| \-1087 | 没有找到满足故障恢复条件的节点 |
| \-1088 | 需要先对 ASM 组做故障处理 |
| \-1089 | 监视器正在执行命令，请稍候重试 |
| \-1090 | CSS 没有对组配置重启参数 |
| \-1091 | 非法的 EP 序号 |
| \-1092 | 对 EP 写入 HALT 命令成功，请等待处理结果 |
| \-1094 | ASM 组中没有活动 EP，不允许执行故障处理 |
| \-1095 | 指定组中没有活动 EP，不允许执行故障处理 |
| \-1096 | 打开 CSS 对节点的自动拉起成功 |
| \-1097 | 关闭 CSS 对节点的自动拉起成功 |
| \-1098 | 组中没有非活动 EP |
| \-1105 | 扩展节点失败，请查看日志获取详细信息 |
| \-1521 | DSC 环境同一机器上的节点不允许配置相同的归档路径 |

### 19.2.4 C 接口说明

#### 1\. cssm\_alloc\_handle

**函数原型：**

```
CSSM_RETURN
cssm_alloc_handle(
    mhandle*        mhdle
);
```

**功能说明：**

分配监视器操作句柄，监视器的接口都通过此句柄调用执行。

**参数说明：**

mhdle: 输出参数，分配到的监视器句柄。

**返回值：**

0：执行成功。

<0：执行失败。

#### 2\. cssm\_get\_error\_msg\_by\_code

**函数原型：**

```
CSSM_RETURN
cssm_get_error_msg_by_code(
    mhandle            mhdle,
    mint4            code,
    mschar*            buf_msg,
    muint4            buf_len,
    muint4*            msg_len_out
);
```

**功能说明：**

获取输入 code 对应的错误描述信息，code 必须是小于 0 的值。

**参数说明：**

mhdle: 输入参数，分配到的监视器句柄，注意如果是分配句柄或初始化环境时失败，允许 mhdle 是无效的，否则要求 mhdle 必须是有效句柄。

code：输入参数，需要获取错误信息的错误码 code，注意 code 必须是小于 0 的值。

buf\_msg：输出参数，输出错误描述信息，注意 buf\_msg 缓存长度建议大于 4096，避免输出信息被截断。

buf\_len:输入参数，指定 buf\_msg 可写入的最大长度。

msg\_len\_out：输出参数，buf\_msg 缓存实际写入长度。

**返回值：**

0：执行成功。

<0：执行失败，-10 表示没有找到 code 对应的错误信息。

#### 3\. cssm\_init

**函数原型：**

```
CSSM_RETURN
cssm_init(
    mhandle            mhdle,
    mschar*            ini_path,
    mschar*            log_path
);
```

**功能说明：**

初始化监视器环境。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

ini\_path: 输入参数，指定 dmcssm.ini 的绝对路径。

log\_path: 输入参数，指定日志文件的存放路径，如果为 NULL 或空串，则将 dmcssm.ini 中配置的 CSSM\_LOG\_PATH 作为日志文件路径，如果 dmcssm.ini 中没有配置 CSSM\_LOG\_PATH，则将 dmcssm.ini 的同级目录作为日志文件路径。

**返回值：**

0：执行成功。

<0：执行失败，-7 表示监视器尝试建立到所有 CSS 的连接失败，可能 CSS 都未启动，允许忽略此错误继续执行其他操作，如果不忽略此错误，认定初始化失败，则需要先正常销毁监视器环境（调用 cssm\_deinit 接口），再释放操作句柄（调用 cssm\_free\_handle 接口）。

#### 4\. cssm\_msg\_event\_wait

**函数原型：**

```
void
cssm_msg_event_wait(
    mhandle            mhdle
);
```

**功能说明：**

等待消息事件。监视器接口命令执行过程中产生的中间输出消息，以及收到 CSS 自动处理的消息时都会将消息写入到缓存并通知消息事件，调用者只需要调用此接口等待即可，等待事件发生后，可通过接口 cssm\_get\_exec\_msg 去读取输出消息。

这种方式需要单独起一个线程来处理消息，以免消息被阻塞。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

无

#### 5\. cssm\_get\_exec\_msg

**函数原型：**

```
CSSM_RETURN
cssm_get_exec_msg(
    mhandle            mhdle,
    mschar*            buf_msg,
    muint4            buf_len,
    muint4*            msg_len_out,
    muint4*            get_flag
);
```

**功能说明：**

获取输出信息，和 cssm\_msg\_event\_wait 配合使用。

**参数说明：**

mhdle:输入参数，监视器操作句柄。

buf\_msg：输出参数，保存获取到的输出消息，注意 buf\_msg 缓存长度需要大于 4096，以免长度不够导致消息被截断。

buf\_len:输入参数，指定 buf\_msg 可写入的最大长度，建议 buf\_msg 缓存长度及 buf\_len 输入值大于 4096，避免消息被截断。

msg\_len\_out:输出参数，写消息成功后，输出实际写入的消息长度。

get\_flag:输出参数，是否继续读取消息，TRUE 表示还有消息可读，FALSE 表示已全部读完。

**返回值：**

0：执行成功。

<0：执行失败。

#### 6\. cssm\_get\_msg\_exit\_flag

**函数原型：**

```
CSSM_RETURN
cssm_get_msg_exit_flag(
    mhandle            mhdle,
    mbool*            exit_flag
);
```

**功能说明：**

如果上层应用程序中有单独的消息线程，可通过调用此接口获取退出标记，在标记为 TRUE 时可正常退出线程。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

exit\_flag：输出参数，输出退出标记，1 表示可以正常退出，0 表示不能退出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 7\. cssm\_set\_msg\_exit\_event

**函数原型：**

```
void
cssm_set_msg_exit_event(
    mhandle            mhdle
);
```

**功能说明：**

设置消息退出事件。如果上层应用程序中有单独的消息线程，在 cssm\_get\_msg\_exit\_flag 接口获取到退出标记为 TRUE 时，需要调用此接口设置退出事件。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

无

#### 8\. cssm\_msg\_event\_deinit

**函数原型：**

```
void
cssm_msg_event_deinit(
    mhandle            mhdle
);
```

**功能说明：**

通知并等待消息退出。使用等待事件方式获取监视器消息时，需要单独起一个线程，在程序结束，退出线程时，需要调用此接口通知并等待消息线程退出。

消息线程相关的接口有 cssm\_msg\_event\_wait、cssm\_get\_exec\_msg、cssm\_get\_msg\_exit\_flag、cssm\_set\_msg\_exit\_event 和 cssm\_msg\_event\_deinit，这几个接口需要配合使用。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

无

#### 9\. cssm\_get\_master\_css\_info

**函数原型：**

```
CSSM_RETURN
cssm_get_master_css_info(
    mhandle            mhdle,
    mbyte*            ep_seqno,
    mschar*            ep_name
);
```

**功能说明：**

获取主 CSS 节点的组内序号和节点名称。

> **注意**
> 
> **CSS需要5s的选举时间来确定主CSS，在CSS的选举时间内，此接口会执行失败，获取不到主CSS信息。**

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

ep\_seqno：输出参数，输出主 CSS 节点的组内序号。

ep\_name：输出参数，输出主 CSS 节点的名称，注意缓存长度不能小于 65，避免长度溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 10\. cssm\_get\_master\_asm\_info

**函数原型：**

```
CSSM_RETURN
cssm_get_master_asm_info(
    mhandle            mhdle,
    mbyte*            ep_seqno,
    mschar*            ep_name
);
```

**功能说明：**

获取主 ASM 节点的组内序号和节点名称。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

ep\_seqno：输出参数，输出主 ASM 节点的组内序号。

ep\_name：输出参数，输出主 ASM 节点的名称，注意缓存长度不能小于 65，避免长度溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 11\. cssm\_get\_master\_db\_info

**函数原型：**

```
CSSM_RETURN
cssm_get_master_db_info(
    mhandle            mhdle,
    mschar*            group_name,
    mbyte*            ep_seqno,
    mschar*            ep_name
);
```

**功能说明：**

获取主 DB 节点的组内序号和节点名称。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，需要获取主 DB 信息的组名，允许配置有多个 DB 组。

ep\_seqno：输出参数，输出主 DB 节点的组内序号。

ep\_name：输出参数，输出主 DB 节点的名称，注意缓存长度不能小于 65，避免长度溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 12\. cssm\_get\_css\_auto\_flag

**函数原型：**

```
CSSM_RETURN
cssm_get_css_auto_flag(
    mhandle            mhdle,
    mschar*            css_name,
    mbool*            auto_flag
);
```

**功能说明：**

获取指定 CSS 的监控状态。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

css\_name：输入参数，需要获取监控状态的 CSS 名称。

auto\_flag：输出参数，为 1 表示 CSS 监控处于打开状态，为 0 表示 CSS 监控处于关闭状态。

**返回值：**

0：执行成功。

<0：执行失败。

#### 13\. cssm\_get\_css\_auto\_info

**函数原型：**

```
CSSM_RETURN
cssm_get_css_auto_info(
    mhandle            mhdle,
    mschar*            css_name,
    mbyte*            auto_flag,
    mschar*            asm_name,
    mbyte*            asm_auto_restart,
    mschar*            db_name,
    mbyte*            db_auto_restart
);
```

**功能说明：**

获取指定 CSS 上的自动监控、自动拉起信息。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

css\_name：输入参数，需要获取信息的 CSS 名称。

auto\_flag：输出参数，为 1 表示 CSS 监控处于打开状态，为 0 表示 CSS 监控处于关闭状态。

asm\_name：输出参数，当前 css 可以控制自动拉起的 asm 节点名称。

asm\_auto\_restart：输出参数，asm\_name 当前的自动拉起状态，为 1 表示自动拉起打开，为 0 表示自动拉起关闭，0xFE 表示 dmdcr.ini 中配置有自动拉起命令串，但自动拉起检测间隔为 0，为 0xFF 则表示 dmdcr.ini 中自动拉起参数配置错误。

db\_name：输出参数，当前 css 可以控制自动拉起的 db 节点名称。

db\_auto\_restart：输出参数，db\_name 当前的自动拉起状态，为 1 表示自动拉起打开，为 0 表示自动拉起关闭，0xFE 表示 dmdcr.ini 中配置有自动拉起命令串，但自动拉起检测间隔为 0，为 0xFF 则表示 dmdcr.ini 中自动拉起参数配置错误。

**返回值：**

0：执行成功。

<0：执行失败。

#### 14\. cssm\_set\_group\_auto\_restart

**函数原型：**

```
CSSM_RETURN
cssm_set_group_auto_restart(
    mhandle            mhdle,
    mschar*            group_name,
    mbyte            auto_restart_flag
);
```

**功能说明：**

设置指定组的自动拉起标记。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，输入需要修改自动拉起标记的组名。

auto\_restart\_flag：输入参数，输入需要修改的值，只能是 0 或 1，为 0 表示关闭指定组自动拉起功能，为 1 表示打开指定组自动拉起功能。

**返回值：**

0：执行成功。

<0：执行失败。

#### 15\. cssm\_get\_n\_group

**函数原型：**

```
CSSM_RETURN
cssm_get_n_group(
    mhandle            mhdle,
    muint4*            n_group,
    mbyte*            group_seqno,
    mschar**        group_name,
    mschar**        group_type
);
```

**功能说明：**

获取 DSC 集群所有的组信息。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

n\_group：输入输出参数，输入参数指定要获取的最多组个数，建议不小于 16，避免取不到完整信息，输出参数为实际获取的组个数。

group\_seqno：输出参数，输出各组的序号，参数为 mbyte 数组类型，数组长度为 n\_group 的输入值。

group\_name：输出参数，输出各组的名称，参数为字符串指针数组类型，数组长度是 n\_group 的输入值，每个指针元素指向的缓存长度不能小于 65，避免长度溢出。

group\_type：输出参数，输出各组的类型，参数为字符串指针数组类型，数组长度是 n\_group 的输入值，每个指针元素指向的缓存长度不能小于 65，避免长度溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 16\. cssm\_get\_n\_ep

**函数原型：**

```
CSSM_RETURN
cssm_get_n_ep(
    mhandle            mhdle,
    mschar*            group_name,
    muint4*            n_ep,
    mbyte*            ep_seqno,
    mschar**        ep_name
);
```

**功能说明：**

获取指定组中的节点信息。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定要获取节点信息的组名。

n\_ep：输入输出参数，输入参数指定要获取的最多节点个数，建议不小于 16，避免取不到完整信息，输出参数为实际获取的节点个数。

ep\_seqno：输出参数，输出各节点的组内序号，参数为 mbyte 数组类型，数组长度为 n\_ep 的输入值。

ep\_name：输出参数，输出各节点的名称，参数为字符串指针数组类型，数组长度是 n\_ep 的输入值，每个指针元素指向的缓存长度不能小于 65，避免长度溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 17\. cssm\_get\_group\_info\_by\_name

**函数原型：**

```
CSSM_RETURN
cssm_get_group_info_by_name(
    mhandle            mhdle,
    mschar*            group_name,
    mbyte*            group_seqno,
    mschar*            group_type,
    mbyte*            n_ep,
    mbyte*            ep_seqno_arr,
    mschar**        ep_name_arr,
    mbyte*            n_ok_ep,
    mbyte*            ok_ep_arr,
    mbyte*            master_ep,
    mschar*            master_ep_name,
    mschar*            sta,
    mschar*            sub_sta,
    mbyte*            n_break_ep,
    mbyte*            break_ep_arr,
    mbyte*            recover_ep,
    mbyte*            crash_over
);
```

**功能说明：**

获取指定名称的组信息。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定要获取信息的组名。

group\_seqno：输出参数，输出组的序号。

group\_type：输出参数，输出组的类型，注意缓存长度不能小于 65，避免长度溢出。

n\_ep：输入输出参数，输入参数指定最多要获取的节点个数，建议输入值不小于 16，避免取不到完整信息，输出参数为实际获取的节点个数。

ep\_seqno\_arr：输出参数，输出各节点的组内序号，是 mbyte 数组类型，数组长度为 n\_ep 的输入值。

ep\_name\_arr：输出参数，输出各节点的名称，是字符串指针数组类型，数组长度为 n\_ep 的输入值，每个指针元素指向的缓存长度不能小于 65，避免长度溢出。

n\_ok\_ep：输入输出参数，输入参数指定最多要获取的正常节点个数，建议输入值不小于 16，避免取不到完整信息，输出参数为实际获取的正常节点个数，该字段只对 ASM/DB 类型的组有效，CSS 类型的组输出为 0。

ok\_ep\_arr：输出参数，输出组中正常节点的组内序号，是 mbyte 数组类型，数组长度是 n\_ok\_ep 的输入值，该字段只对 ASM/DB 类型的组有效。

master\_ep：输出参数，输出组中控制节点的组内序号。

master\_ep\_name：输出参数，输出组中控制节点的名称，注意缓存长度不能小于 65，避免长度溢出。

sta：输出参数，输出组的状态，该字段只对 ASM/DB 类型的组有效，CSS 类型的组输出为空串。

sub\_sta：输出参数，输出组的子状态，该字段只对 ASM/DB 类型的组有效，CSS 类型的组输出为空串。

n\_break\_ep：输出参数，输出组中正在执行故障处理的节点个数。

break\_ep\_arr：输出参数，输出组中正在执行故障处理的节点序号，该字段只对 ASM/DB 类型的组有效，CSS 类型的组输出为 0xFF。

recover\_ep：输出参数，输出组中正在执行故障恢复的节点序号，该字段只对 ASM/DB 类型的组有效，CSS 类型的组输出为 0xFF。

crash\_over：输出参数，表示故障处理是否结束。0 表示未结束，1 表示结束。

**返回值：**

0：执行成功。

<0：执行失败。

#### 18\. cssm\_get\_ep\_info\_by\_name

**函数原型：**

```
CSSM_RETURN
cssm_get_ep_info_by_name(
    mhandle            mhdle,
    mschar*            group_name,
    mschar*            ep_name,
    mbyte*            css_seqno,
    mschar*            css_name,
    mschar*            css_time,
    mbyte*            ep_seqno,
    mschar*            work_mode,
    mschar*            inst_stat,
    mschar*            vtd_stat,
    mschar*            ok_stat,
    mschar*            is_active,
    mschar*            ep_guid,
    mschar*            ep_ts
);
```

**功能说明：**

获取指定名称的组信息。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定要获取信息的组名。

ep\_name：输入参数，指定要获取信息的节点名称。

css\_seqno：输出参数，输出取得节点信息的 CSS 序号。

css\_name：输出参数，输出取得节点信息的 CSS 名称，注意缓存长度不能小于 65，避免长度溢出。

css\_time：输出参数，输出取得节点信息的 CSS 当前时间，注意缓存长度不能小于 65，避免长度溢出。

ep\_seqno：输出参数，输出节点的组内序号。

work\_mode：输出参数，输出节点的工作模式，注意缓存长度不能小于 65，避免长度溢出。

inst\_stat：输出参数，输出节点的工作状态，注意缓存长度不能小于 65，避免长度溢出。

vtd\_stat：输出参数，输出节点在 Voting Disk 中的状态，注意缓存长度不能小于 65，避免长度溢出。

ok\_stat：输出参数，输出节点状态是否正常（OK/ERROR），注意缓存长度不能小于 6，避免长度溢出。

is\_active：输出参数，输出节点是否处于活动状态（TRUE/FALSE），注意缓存长度不能小于 6，避免长度溢出。

ep\_guid：输出参数，输出节点的 guid 值。

ep\_ts：输出参数，输出节点的时间戳值。

**返回值：**

0：执行成功。

<0：执行失败。

#### 19\. cssm\_get\_header\_config\_info

**函数原型：**

```
CSSM_RETURN
cssm_get_header_config_info(
    mhandle            mhdle,
    muint4*            dcr_n_group,
    mschar*            dcr_vtd_path,
    muint8*            dcr_oguid,
);
```

**功能说明：**

输出 dmdcr\_cfg.ini 中配置的全局信息。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

dcr\_n\_group：输出参数，输出配置的组个数。

dcr\_vtd\_path：输出参数，输出 Voting Disk 路径，注意缓存长度不能小于 257，避免长度溢出。

dcr\_oguid：输出参数，输出配置的 OGUID 标识。

**返回值：**

0：执行成功。

<0：执行失败。

#### 20\. cssm\_get\_group\_config\_info

**函数原型：**

```
CSSM_RETURN
cssm_get_group_config_info(
    mhandle            mhdle,
    mschar*            dcr_grp_name,
    mschar*            dcr_grp_type,
    mbyte*            dcr_grp_n_ep,
    muint4*            dcr_grp_dskchk_cnt,
);
```

**功能说明：**

输出 dmdcr\_cfg.ini 中配置的组信息。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

dcr\_grp\_name：输入参数，输入要获取信息的组名。

dcr\_grp\_type：输出参数，输出配置的组类型，注意缓存长度不能小于 65，避免长度溢出。

dcr\_grp\_n\_ep：输出参数，输出组中配置的节点个数。

dcr\_grp\_dskchk\_cnt：输出参数，输出指定组配置的磁盘心跳容错时间。

**返回值：**

0：执行成功。

<0：执行失败。

#### 21\. cssm\_get\_ep\_config\_info

**函数原型：**

```
CSSM_RETURN
cssm_get_ep_config_info(
    mhandle            mhdle,
    mschar*            dcr_group_name,
    mschar*            dcr_ep_name,
    mbyte*            dcr_ep_seqno,
    mschar*            dcr_ep_host,
    muint4*            dcr_ep_port,
    muint4*            dcr_ep_shm_key,
    muint4*            dcr_ep_shm_size,
    mschar*            dcr_ep_asm_load_path
);
```

**功能说明：**

输出 dmdcr\_cfg.ini 中配置的节点信息。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

dcr\_group\_name：输入参数，输入节点所在的组名。

dcr\_ep\_name：输入参数，输入节点名称。

dcr\_ep\_seqno：输出参数，输出节点的组内序号，CSS/ASM 类型的节点为自动分配的值，DB 类型的节点如果没有显式配置 DCR\_EP\_SEQNO，也是自动分配的值，否则为手动配置的值。

dcr\_ep\_host：输出参数，输出节点的 IP 地址，对 CSS/ASM 类型的节点有效，表示登录 CSS/ASM 节点的 IP 地址，注意缓存长度不能小于 65，避免长度溢出。

dcr\_ep\_port：输出参数，输出节点的 TCP 监听端口，对 CSS/ASM 类型的节点有效，对应登录 CSS/ASM 的端口号。

dcr\_ep\_shm\_key：输出参数，输出节点的共享内存标识，对 ASM 类型的节点有效。

dcr\_ep\_shm\_size：输出参数，输出节点的共享内存大小，单位 M，对 ASM 类型的节点有效。

dcr\_ep\_asm\_load\_path：输出参数，输出节点的 ASM 磁盘扫描路径，对 ASM 类型的节点有效，注意缓存长度不能小于 257，避免长度溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 22\. cssm\_get\_monitor\_info

**函数原型：**

```
CSSM_RETURN
cssm_get_monitor_info(
    mhandle            mhdle,
    mbyte*            css_seqno,
    mschar*            css_name,
    muint4*            n_mon,
    mschar**        conn_time_arr,
    muint8*            mid_arr,
    mschar**        mon_ip_arr
);
```

**功能说明：**

输出连接到主 CSS 上的所有监视器信息，如果主 CSS 故障或尚未选出，则任选一个 CSS 输出所有的连接信息。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

css\_seqno：输出参数，输出取得监视器连接信息的 CSS 序号。

css\_name：输出参数，输出取得监视器连接信息的 CSS 名称，注意缓存长度不能小于 65，避免长度溢出。

n\_mon：输入输出参数，输入值指定可获取的最多的监视器个数，建议不小于 10，避免取不到完整信息，输出值为实际获取到的监视器个数。

conn\_time\_arr：输出参数，参数类型为字符串指针数组类型，数组长度为 n\_mon 的输入值，输出各监视器连接到 css\_name 的时间，注意每个数组元素指向的缓存长度不能小于 65，避免长度溢出。

mid\_arr：输出参数，参数类型为 muint8 数组类型，数组长度为 n\_mon 的输入值，输出各监视器的 mid 值。

mon\_ip\_arr：参数类型为字符串指针数组类型，数组长度为 n\_mon 的输入值，输出各监视器的 IP 地址，注意每个数组元素指向的缓存长度不能小于 65，避免长度溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 23\. cssm\_css\_startup

**函数原型：**

```
CSSM_RETURN
cssm_css_startup(
  mhandle     mhdle
);
```

**功能说明：**

打开当前所有活动 CSS 的监控功能。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

0：执行成功。

<0：执行失败。

#### 24\. cssm\_css\_stop

**函数原型：**

```
CSSM_RETURN
cssm_css_stop(
  mhandle     mhdle
);
```

**功能说明：**

关闭当前所有活动 CSS 的监控功能。

CSS 监控被关闭后，只负责调整各组节点的 active 状态，除此之外不会做任何自动处理，也不会自动拉起对应的节点，如果在监控关闭后，通过手动方式（非 cssm\_ep\_startup 接口方式）启动 ASM 或 DB 组，各节点也无法正常启动到 OPEN 状态。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

0：执行成功。

<0：执行失败。

#### 25\. cssm\_open\_force

**函数原型：**

```
CSSM_RETURN
cssm_open_force(
    mhandle            mhdle,
    mschar*            group_name
);
```

**功能说明：**

强制 OPEN 指定的组。

使用场景：

在启动 ASM 或 DB 组时，如果某个节点故障一直无法启动，可借助此接口将 ASM 或 DB 组强制 OPEN。

接口会发送消息到主 CSS 执行，并且主 CSS 的监控需要处于打开状态，如果主 CSS 故障或尚未选出，则接口执行失败。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定要强制 OPEN 的组名。

**返回值：**

0：执行成功。

<0：执行失败。

#### 26\. cssm\_ep\_startup

**函数原型：**

```
CSSM_RETURN
cssm_ep_startup(
    mhandle            mhdle,
    mschar*            group_name
);
```

**功能说明：**

启动指定 ASM 或 DB 组的所有节点。

如果 CSS 已经配置了自动重启，并且 CSS 的监控处于打开状态，则接口不允许执行，需要等待 CSS 自动检测故障并执行重启操作。

每个 CSS 只负责重启和自己的 dmdcr.ini 中配置的 DMDCR\_SEQNO 相同的 ASM 或 DB 节点，因此需要所有 CSS 都处于活动状态，否则只通知当前活动的 CSS 重启相对应的节点。

> **注意**
> 
> **只有在ASM组正常启动到OPEN状态，并且所有活动的ASM节点都处于OPEN状态时，才允许启动DB组，否则执行DB组的启动操作会报错。**
> 
> **另外在接口执行时，如果CSS监控处于关闭状态，则会直接打开CSS监控，否则ASM或DB组无法正常启动到OPEN状态。**

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定要启动的组名。

**返回值：**

0：执行成功。

<0：执行失败。

#### 27\. cssm\_ep\_stop

**函数原型：**

```
CSSM_RETURN
cssm_ep_stop(
    mhandle            mhdle,
    mschar*            group_name
);
```

**功能说明：**

退出指定的 ASM 或 DB 组，如果主 CSS 故障或尚未选出，则接口执行失败。

> **注意**
> 
> **在退出ASM组时，需要保证DB组已经退出，否则会报错处理。**
> 
> **另外如果退出时，CSS监控没有关闭，在退出完成后，达到CSS设置的重启间隔之后，CSS仍然会执行自动拉起，如果要正常退出集群，不需要自动拉起，则退出之前需要调用cssm\_css\_stop接口停止CSS的监控功能。**

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定要退出的组名。

**返回值：**

0：执行成功。

<0：执行失败。

#### 28\. cssm\_ep\_break

**函数原型：**

```
CSSM_RETURN
cssm_ep_break(
    mhandle            mhdle,
    mschar*            group_name
);
```

**功能说明：**

此接口只允许在主 CSS 监控关闭的情况下使用。

ASM 组或 DB 组在正常运行时，如果某个节点出现故障，则需要调用此接口执行故障处理，将故障节点从组的 OK 节点数组中摘除。

> **注意**
> 
> **在主CSS监控关闭的情况下，如果ASM组的某个节点故障，和故障节点有相同DCR\_SEQNO的DB节点需要使用cssm\_ep\_halt接口执行强制退出，否则DB节点访问对应的ASM文件系统失败，也会自动HALT。**
> 
> **在ASM和DB节点都出现故障的情况下，需要先对ASM组执行故障处理，再对DB组执行故障处理，否则会报错不允许执行。**

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定要执行故障处理的组名。

**返回值：**

0：执行成功。

<0：执行失败。

#### 29\. cssm\_ep\_recover

**函数原型：**

```
CSSM_RETURN
cssm_ep_recover(
    mhandle            mhdle,
    mschar*            group_name
);
```

**功能说明：**

此接口只允许在主 CSS 监控关闭的情况下使用。

执行过故障处理的节点重启成功后，可通过调用此接口将故障节点重加入指定的 ASM 或 DB 组，重新恢复组到 OPEN 状态。

> **注意**
> 
> **如果主CSS故障或尚未选出，则接口执行失败。另外只有在ASM组的故障节点重加入成功后，才允许重启对应的DB节点，并执行DB组的故障重加入。**

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定要执行故障恢复的组名。

**返回值：**

0：执行成功。

<0：执行失败。

#### 30\. cssm\_ep\_halt

**函数原型：**

```
CSSM_RETURN
cssm_ep_halt(
    mhandle            mhdle,
    mschar*            group_name,
    mschar*            ep_name
);
```

**功能说明：**

强制退出指定组的指定 EP。

此接口在 CSS 监控打开或关闭的情况下都允许使用，适用于下述场景：

a. 某个 ASM 或 DB 节点故障，CSS DCR\_GRP\_DSKCHK\_CNT 配置值很大，在容错时间内，CSS 不会调整故障节点的 active 标记，一直是 TRUE，CSS 认为故障 EP 仍然处于活动状态，不会自动执行故障处理，并且不允许手动执行故障处理。

另外执行 cssm\_ep\_startup 或 cssm\_ep\_stop 接口时，会误认为故障 EP 仍然处于活动状态，导致执行结果与预期不符。

此时可以通过执行此接口，通知 CSS 再次 HALT 故障 EP，确认 EP 已经被 HALT 后，CSS 会及时调整 active 标记为 FALSE，在此之后，对自动/手动故障处理，启动/退出 EP 节点等操作都可以正常执行。

b. 需要强制 HALT 某个正在运行的 ASM 或 DB 节点，也可以通过此接口完成。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定要强制退出的节点所在的组名。

ep\_name：输入参数，指定要强制退出的节点名称。

**返回值：**

0：执行成功。

<0：执行失败。

#### 31\. cssm\_deinit

**函数原型：**

```
CSSM_RETURN
cssm_deinit(
    mhandle            mhdle
);
```

**功能说明：**

销毁监视器执行环境。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

0：执行成功。

<0：执行失败。

#### 32\. cssm\_free\_handle

**函数原型：**

```
CSSM_RETURN
cssm_free_handle(
    mhandle            mhdle
);
```

**功能说明：**

释放分配到的监视器句柄。

**参数说明：**

mhdle: 输入参数，分配到的句柄。

**返回值：**

0：执行成功。

<0：执行失败。

### 19.2.5 JAVA 接口说明

#### 1\. cssm\_init\_handle

**函数原型：**

```
boolean
cssm_init_handle();
```

**功能说明：**

分配监视器操作句柄，监视器的接口都通过此句柄调用执行。

**参数说明：**

无

**返回值：**

true：分配成功，返回值为监视器操作句柄。

false：分配失败。

#### 2\. cssm\_get\_error\_msg\_by\_code

**函数原型：**

```
CssMonMsg
cssm_get_error_msg_by_code(
    int                code
);
```

**功能说明：**

获取输入 code 对应的错误描述信息，code 必须是小于 0 的值。

**参数说明：**

code：输入参数，需要获取错误信息的错误码 code，注意 code 必须是小于 0 的值。

**返回值：**

返回 CssMonMsg 对象，可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 CssMonMsg 的其他对象成员获取输出消息。

<0：执行失败。

#### 3\. cssm\_init\_env

**函数原型：**

```
int
cssm_init_env(
    String            ini_path,
    String            log_path
);
```

**功能说明：**

初始化监视器环境。

**参数说明：**

ini\_path: 输入参数，指定 dmcssm.ini 的绝对路径。

log\_path: 输入参数，指定日志文件的存放路径，如果为 NULL 或空串，则将 dmcssm.ini 中配置的 CSSM\_LOG\_PATH 作为日志文件路径，如果 dmcssm.ini 中没有配置 CSSM\_LOG\_PATH，则将 dmcssm.ini 的同级目录作为日志文件路径。

**返回值：**

0：执行成功。

<0：执行失败，-7 表示监视器尝试建立到所有 CSS 的连接失败，可能 CSS 都未启动，允许忽略此错误继续执行其他操作，如果不忽略此错误，认定初始化失败，则需要先正常销毁监视器环境（调用 cssm\_deinit 接口），再释放操作句柄（调用 cssm\_free\_handle 接口）。

#### 4\. cssm\_msg\_event\_wait

**函数原型：**

```
void
cssm_msg_event_wait();
```

**功能说明：**

等待消息事件。监视器接口命令执行过程中产生的中间输出消息，以及收到 CSS 自动处理的消息时都会将消息写入到缓存并通知消息事件，调用者只需要调用此接口等待即可，等待事件发生后，可通过接口 cssm\_get\_exec\_msg 去读取输出消息。

这种方式需要单独起一个线程来处理消息，以免消息被阻塞。

**参数说明：**

无

**返回值：**

无

#### 5\. cssm\_get\_exec\_msg

**函数原型：**

```
CssMonMsg
cssm_get_exec_msg();
```

**功能说明：**

获取输出信息，和 cssm\_msg\_event\_wait 配合使用。

**参数说明：**

无

**返回值：**

返回 CssMonMsg 对象，可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 CssMonMsg 的其他对象成员获取输出消息。

<0：执行失败。

#### 6\. cssm\_get\_msg\_exit\_flag

**函数原型：**

```
boolean
cssm_get_msg_exit_flag();
```

**功能说明：**

如果上层应用程序中有单独的消息线程，可通过调用此接口获取退出标记，在标记为 true 时可正常退出线程。

**参数说明：**

无

**返回值：**

true：允许线程退出。

false：不允许线程退出，需要继续等待获取输出消息。

#### 7\. cssm\_set\_msg\_exit\_event

**函数原型：**

```
void
cssm_set_msg_exit_event();
```

**功能说明：**

设置消息退出事件。如果上层应用程序中有单独的消息线程，在 cssm\_get\_msg\_exit\_flag 接口获取到退出标记为 true 时，需要调用此接口设置退出事件。

**参数说明：**

无

**返回值：**

无

#### 8\. cssm\_msg\_event\_deinit

**函数原型：**

```
void
cssm_msg_event_deinit();
```

**功能说明：**

通知并等待消息退出。使用等待事件方式获取监视器消息时，需要单独起一个线程，在程序结束，退出线程时，需要调用此接口通知并等待消息线程退出。

消息线程相关的接口有 cssm\_msg\_event\_wait、cssm\_get\_exec\_msg、cssm\_get\_msg\_exit\_flag、cssm\_set\_msg\_exit\_event 和 cssm\_msg\_event\_deinit，这几个接口需要配合使用。

**参数说明：**

无

**返回值：**

无

#### 9\. cssm\_get\_master\_css\_info

**函数原型：**

```
CssMonMasterEpInfo
cssm_get_master_css_info();
```

**功能说明：**

获取主 CSS 节点的组内序号和节点名称。

> **注意**
> 
> **CSS需要5s的选举时间来确定主CSS，在CSS的选举时间内，此接口会执行失败，获取不到主CSS信息。**

**参数说明：**

无

**返回值：**

返回 CssMonMasterEpInfo 对象，可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 CssMonMasterEpInfo 的其他对象成员获取主 CSS 信息。

<0：执行失败。

#### 10\. cssm\_get\_master\_asm\_info

**函数原型：**

```
CssMonMasterEpInfo
cssm_get_master_asm_info();
```

**功能说明：**

获取主 ASM 节点的组内序号和节点名称。

**参数说明：**

无

**返回值：**

返回 CssMonMasterEpInfo 对象，可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 CssMonMasterEpInfo 的其他对象成员获取主 ASM 信息。

<0：执行失败。

#### 11\. cssm\_get\_master\_db\_info

**函数原型：**

```
CssMonMasterEpInfo
cssm_get_master_db_info(
    String            group_name
);
```

**功能说明：**

获取主 DB 节点的组内序号和节点名称。

**参数说明：**

group\_name：输入参数，需要获取主 DB 信息的组名，允许配置有多个 DB 组。

**返回值：**

返回 CssMonMasterEpInfo 对象，可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 CssMonMasterEpInfo 的其他对象成员获取主 DB 信息。

<0：执行失败。

#### 12\. cssm\_get\_css\_auto\_flag

**函数原型：**

```
boolean
cssm_get_css_auto_flag(
    String            css_name
);
```

**功能说明：**

获取指定 CSS 的监控状态。

**参数说明：**

css\_name：输入参数，需要获取监控状态的 CSS 名称。

**返回值：**

true：表示 CSS 监控处于打开状态。

false：表示 CSS 监控处于关闭状态。

#### 13\. cssm\_get\_css\_auto\_info

**函数原型：**

```
CssMonAutoInfo
cssm_get_css_auto_info(
    String            css_name
);
```

**功能说明：**

获取指定 CSS 上的自动监控、自动拉起信息。

**参数说明：**

css\_name：输入参数，需要获取信息的 CSS 名称。

**返回值：**

返回 CssMonAutoInfo 对象，可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 CssMonAutoInfo 的其他对象成员获取相关信息。

<0：执行失败。

#### 14\. cssm\_set\_group\_auto\_restart

**函数原型：**

```
int
cssm_set_group_auto_restart(
    String            group_name,
    byte            auto_restart_flag
);
```

**功能说明：**

设置指定组的自动拉起标记。

**参数说明：**

group\_name：输入参数，输入需要修改自动拉起标记的组名。

auto\_restart\_flag：输入参数，输入需要修改的值，只能是 0 或 1，为 0 表示关闭指定组自动拉起功能，为 1 表示打开指定组自动拉起功能。

**返回值：**

0：执行成功。

<0：执行失败。

#### 15\. cssm\_get\_n\_group

**函数原型：**

```
CssMonGrpNameArray
cssm_get_n_group();
```

**功能说明：**

获取 DSC 集群所有的组信息。

**参数说明：**

无

**返回值：**

返回 CssMonGrpNameArray 对象，可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 CssMonGrpNameArray 的其他对象成员获取组信息。

<0：执行失败。

#### 16\. cssm\_get\_n\_ep

**函数原型：**

```
CssMonEpNameArray
cssm_get_n_ep(
    String            group_name
);
```

**功能说明：**

获取指定组中的节点信息。

**参数说明：**

group\_name：输入参数，指定要获取节点信息的组名。

**返回值：**

返回 CssMonEpNameArray 对象，可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 CssMonEpNameArray 的其他对象成员获取节点信息。

<0：执行失败。

#### 17\. cssm\_get\_group\_info\_by\_name

**函数原型：**

```
CssMonGrpInfo
cssm_get_group_info_by_name(
    String            group_name
);
```

**功能说明：**

获取指定名称的组信息。

**参数说明：**

group\_name：输入参数，指定要获取信息的组名。

**返回值：**

返回 CssMonGrpInfo 对象，可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 CssMonGrpInfo 的其他对象成员获取节点信息。

<0：执行失败。

#### 18\. cssm\_get\_ep\_info\_by\_name

**函数原型：**

```
CssMonEpInfo
cssm_get_ep_info_by_name(
    String            group_name,
    String            ep_name
);
```

**功能说明：**

获取指定名称的组信息。

**参数说明：**

group\_name：输入参数，指定要获取信息的组名。

ep\_name：输入参数，指定要获取信息的节点名称。

**返回值：**

返回 CssMonEpInfo 对象，可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 CssMonEpInfo 的其他对象成员获取节点信息。

<0：执行失败。

#### 19\. cssm\_get\_header\_config\_info

**函数原型：**

```
CssMonHeaderConfigInfo
cssm_get_header_config_info();
```

**功能说明：**

输出 dmdcr\_cfg.ini 中配置的全局信息。

**参数说明：**

无

**返回值：**

返回 CssMonHeaderConfigInfo 对象，可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 CssMonHeaderConfigInfo 的其他对象成员获取配置信息。

<0：执行失败。

#### 20\. cssm\_get\_group\_config\_info

**函数原型：**

```
CssMonGroupConfigInfo
cssm_get_group_config_info(
    String            dcr_group_name
);
```

**功能说明：**

输出 dmdcr\_cfg.ini 中配置的组信息。

**参数说明：**

dcr\_group\_name：输入参数，输入要获取信息的组名。

**返回值：**

返回 CssMonGroupConfigInfo 对象，可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 CssMonGroupConfigInfo 的其他对象成员获取配置信息。

<0：执行失败。

#### 21\. cssm\_get\_ep\_config\_info

**函数原型：**

```
CssMonEpConfigInfo
cssm_get_ep_config_info(
    String            dcr_group_name,
    String            dcr_ep_name
);
```

**功能说明：**

输出 dmdcr\_cfg.ini 中配置的节点信息。

**参数说明：**

dcr\_group\_name：输入参数，输入节点所在的组名。

dcr\_ep\_name：输入参数，输入节点名称。

**返回值：**

返回 CssMonEpConfigInfo 对象，可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 CssMonEpConfigInfo 的其他对象成员获取配置信息。

<0：执行失败。

#### 22\. cssm\_get\_monitor\_info

**函数原型：**

```
CssMonitorInfo
cssm_get_monitor_info();
```

**功能说明：**

输出连接到主 CSS 上的所有监视器信息，如果主 CSS 故障或尚未选出，则任选一个 CSS 输出所有的连接信息。

**参数说明：**

无

**返回值：**

返回 CssMonitorInfo 对象，可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 CssMonitorInfo 的其他对象成员获取配置信息。

<0：执行失败。

#### 23\. cssm\_open\_force

**函数原型：**

```
int
cssm_open_force(
    String            group_name
);
```

**功能说明：**

强制 OPEN 指定的组。

使用场景：

在启动 ASM 或 DB 组时，如果某个节点故障一直无法启动，可借助此接口将 ASM 或 DB 组强制 OPEN。

接口会发送消息到主 CSS 执行，并且主 CSS 的监控需要处于打开状态，如果主 CSS 故障或尚未选出，则接口执行失败。

**参数说明：**

group\_name：输入参数，指定要强制 OPEN 的组名。

**返回值：**

0：执行成功。

<0：执行失败。

#### 24\. cssm\_ep\_startup

**函数原型：**

```
int
cssm_ep_startup(
    String            group_name
);
```

**功能说明：**

启动指定 ASM 或 DB 组的所有节点。

如果 CSS 已经配置了自动重启，并且 CSS 的监控处于打开状态，则接口不允许执行，需要等待 CSS 自动检测故障并执行重启操作。

每个 CSS 只负责重启和自己的 dmdcr.ini 中配置的 DMDCR\_SEQNO 相同的 ASM 或 DB 节点，因此需要所有 CSS 都处于活动状态，否则只通知当前活动的 CSS 重启相对应的节点。

> **注意**
> 
> **只有在ASM组正常启动到OPEN状态，并且所有活动的ASM节点都处于OPEN状态时，才允许启动DB组，否则执行DB组的启动操作会报错。**
> 
> **另外在接口执行时，如果CSS监控处于关闭状态，则会直接打开CSS监控，否则ASM或DB组无法正常启动到OPEN状态。**

**参数说明：**

group\_name：输入参数，指定要启动的组名。

**返回值：**

0：执行成功。

<0：执行失败。

#### 25\. cssm\_ep\_stop

**函数原型：**

```
int
cssm_ep_stop(
    String            group_name
);
```

**功能说明：**

退出指定的 ASM 或 DB 组，如果主 CSS 故障或尚未选出，则接口执行失败。

> **注意**
> 
> **在退出ASM组时，需要保证DB组已经退出，否则会报错处理。**
> 
> **另外如果退出时，CSS监控没有关闭，在退出完成后，达到CSS设置的重启间隔之后，CSS仍然会执行自动拉起，如果要正常退出集群，不需要自动拉起，则退出之前需要调用cssm\_css\_stop接口停止CSS的监控功能。**

**参数说明：**

group\_name：输入参数，指定要退出的组名。

**返回值：**

0：执行成功。

<0：执行失败。

#### 26\. cssm\_ep\_break

**函数原型：**

```
int
cssm_ep_break(
    String            group_name
);
```

**功能说明：**

此接口只允许在主 CSS 监控关闭的情况下使用。

ASM 组或 DB 组在正常运行时，如果某个节点出现故障，则需要调用此接口执行故障处理，将故障节点从组的 OK 节点数组中摘除。

> **注意**
> 
> **在主CSS监控关闭的情况下，如果ASM组的某个节点故障，和故障节点有相同DCR\_SEQNO的DB节点需要使用cssm\_ep\_halt接口执行强制退出，否则DB节点访问对应的ASM文件系统失败，也会自动HALT。**
> 
> **在ASM和DB节点都出现故障的情况下，需要先对ASM组执行故障处理，再对DB组执行故障处理，否则会报错不允许执行。**

**参数说明：**

group\_name：输入参数，指定要执行故障处理的组名。

**返回值：**

0：执行成功。

<0：执行失败。

#### 27\. cssm\_ep\_recover

**函数原型：**

```
int
cssm_ep_recover(
    String            group_name
);
```

**功能说明：**

此接口只允许在主 CSS 监控关闭的情况下使用。

执行过故障处理的节点重启成功后，可通过调用此接口将故障节点重加入指定的 ASM 或 DB 组，重新恢复组到 OPEN 状态。

> **注意**
> 
> **如果主CSS故障或尚未选出，则接口执行失败。另外只有在ASM组的故障节点重加入成功后，才允许重启对应的DB节点，并执行DB组的故障重加入。**

**参数说明：**

group\_name：输入参数，指定要执行故障恢复的组名。

**返回值：**

0：执行成功。

<0：执行失败。

#### 28\. cssm\_ep\_halt

**函数原型：**

```
int
cssm_ep_halt(
    String            group_name,
    String            ep_name
);
```

**功能说明：**

强制退出指定组的指定 EP。

此接口在 CSS 监控打开或关闭的情况下都允许使用，适用于下述场景：

a. 某个 ASM 或 DB 节点故障，CSS 的 DCR\_GRP\_DSKCHK\_CNT 配置值很大，在容错时间内，CSS 不会调整故障节点的 active 标记，一直是 TRUE，CSS 认为故障 EP 仍然处于活动状态，不会自动执行故障处理，并且不允许手动执行故障处理。

另外执行 cssm\_ep\_startup 或 cssm\_ep\_stop 接口时，会误认为故障 EP 仍然处于活动状态，导致执行结果与预期不符。

此时可以通过执行此接口，通知 CSS 再次 HALT 故障 EP，确认 EP 已经被 HALT 后，CSS 会及时调整 active 标记为 FALSE，在此之后，对自动/手动故障处理，启动/退出 EP 节点等操作都可以正常执行。

b. 需要强制 HALT 某个正在运行的 ASM 或 DB 节点，也可以通过此接口完成。

**参数说明：**

group\_name：输入参数，指定要强制退出的节点所在的组名。

ep\_name：输入参数，指定要强制退出的节点名称。

**返回值：**

0：执行成功。

<0：执行失败。

#### 29\. cssm\_deinit\_env

**函数原型：**

```
int
cssm_deinit_env();
```

**功能说明：**

销毁监视器执行环境。

**参数说明：**

无

**返回值：**

0：执行成功。

<0：执行失败。

#### 30\. cssm\_free\_handle

**函数原型：**

```
int
cssm_free_handle();
```

**功能说明：**

释放分配到的监视器句柄。

**参数说明：**

无

**返回值：**

0：执行成功。

<0：执行失败。

### 19.2.6 C 编程示例

这里给出 C 程序的编程示例，运行环境为 VS2010，通过配置项目属性，使用 dmcssm\_dll.lib 隐式加载 dll 的方式，注意此处仅为使用示例，实际使用时可以根据自己的需求再做调整。

```
#include "cssm_dll.h"
#include "stdio.h"
#include "stdlib.h"
#include "windows.h"
#include "process.h"

// 消息线程 
DWORD
WINAPI
cssm_get_msg_thread(
mhandle         handle
)
{
mschar          buf_msg[4097];
    muint4          msg_len_out;
    muint4          get_flag;
mbool           exit_flag;
    CSSM_RETURN     code;

while (TRUE)
    {
        //等待消息事件 
        cssm_msg_event_wait(handle);

        // 获取退出标记 
        cssm_get_msg_exit_flag(handle, &exit_flag);
if (exit_flag == TRUE)
        {
break;
        }

do
        {
            // 获取并打印消息 
code = cssm_get_exec_msg(handle, buf_msg, 4097, &msg_len_out, &get_flag);
if (code >=0 && msg_len_out > 0)
            {
fprintf(stdout, "%s", buf_msg);
            }

        } while (get_flag); // 判断是否还有未读消息 
    }

    // 设置退出事件 
    cssm_set_msg_exit_event(handle);

return 0;
}

// 清理环境
void
cssm_clear_env(
mhandle     handle
)
{
    //通知并等待dmmon_get_msg_thread消息线程退出 
    cssm_msg_event_deinit(handle);

    // 销毁监视器环境 
    cssm_deinit(handle);

    // 释放句柄
    cssm_free_handle(handle);
}

int
main()
{
CSSM_RETURN     ret;
mhandle         handle;
HANDLE          thread_handle;
char            msg[4097];
int             msg_len;
muint4             n_group;
mbyte           group_seqno[16];
mschar*         group_name[16];
mschar*         group_type[16];
msint2          offset;
mschar          mem[4096];
msint2          i;

    //分配操作句柄 
ret     = cssm_alloc_handle(&handle);
if (ret < 0)
    {
fprintf(stdout, "dmcssm alloc handle failed!\n");

        // 获取ret对应的错误描述信息
        cssm_get_error_msg_by_code(handle, ret, msg, 4097, &msg_len);
if (msg_len > 0)
        {
fprintf(stdout, "code:%d, error msg:%s", ret, msg);
        }
return ret;
    }
    // 创建消息线程
    thread_handle = (HANDLE)_beginthreadex(NULL, 0, cssm_get_msg_thread, handle, 0, NULL);
if (thread_handle == NULL)
    {
ret = GetLastError();
fprintf(stderr, "_beginthreadex error! desc:%s, code:%d\n", strerror(ret), ret);

return ret;
    }
    //初始化监视器环境，可以选择忽略-8错误（建立到所有CSS连接失败，可能当前CSS都还未启动） 
ret     = cssm_init(handle, "D:\\dmcssm\\dmcssm.ini", "D:\\dmcssm\\log");
if (ret < 0 && ret != -8)
    {
fprintf(stdout, "dmcssm init failed!\n");
        // 获取ret对应的错误描述信息 
        cssm_get_error_msg_by_code(handle, ret, msg, 4097, &msg_len);
if (msg_len > 0)
        {
fprintf(stdout, "code:%d, error msg:%s", ret, msg);
        }
        cssm_clear_env(handle);
return ret;
    }

offset      = 0;
for (i = 0; i < 16; i++)
    {
        group_name[i]   = mem + offset;
offset          += 129;

        group_type[i]   = mem + offset;
offset          += 65;
    }
    n_group     = 16;
ret         = cssm_get_n_group(handle, &n_group, group_seqno, group_name, group_type);
if (ret < 0)
    {
fprintf(stdout, "dmcssm get group info failed!\n");
        //获取ret对应的错误描述信息 
        cssm_get_error_msg_by_code(handle, ret, msg, 4097, &msg_len);
if (msg_len > 0)
        {
fprintf(stdout, "code:%d, error msg:%s", ret, msg);
        }
    }
else
    {
fprintf(stdout, "Get group info succeed, n_group: %d\n\n", n_group);
    }
    // 执行其他接口调用 
    //...
    // 清理环境 
cssm_clear_env(handle);
system("pause");

return 0;
}
```

### 19.2.7 Java 编程示例

这里给出 Java 程序的编程示例，运行环境为 Eclipse，使用加载监视器 jar 包的方式，jar 包名称为 com.dameng.jni\_7.0.0.jar，注意此处仅为使用示例，实际使用时可以根据自己的需求再做调整。

```
package com.dameng.test;
import com.dameng.cssm.*;
public class CssMonTest {
    public CssMonDLL monDll = null;
    public CssMonMsg monMsg = null;
    public Thread msgThread = null;
    public String ini_path = "D:\\dsc\\dmcssm.ini";
    public String log_path = "D:\\dsc\\log";
    //接收消息线程
    public void startThread()
    {
        msgThread = new Thread(new Runnable()
        {
            @Override
public void run()
            {
    while (true)
                {
        //等待消息事件
        monDll.cssm_msg_event_wait();
        //获取退出标记
        if (monDll.cssm_get_msg_exit_flag() == true)
            break;
    do
                    {
        //获取并打印消息
        monMsg = monDll.cssm_get_exec_msg();
        if(monMsg.getReturnCode() < 0)
            break;
        if(monMsg.getMsg().length() > 0)
        {
            System.out.print(monMsg.getMsg());
        }
        } while (monMsg.getMsgFlag() == 1); //是否还有未读消息
                }
    //设置退出标记
    monDll.cssm_set_msg_exit_event();
            }
        });
        //启动线程
        msgThread.start();
    }
    //退出线程
    public void endThread() throws InterruptedException
    {
        if (msgThread != null && msgThread.isAlive())
        {
            //通知并等待消息线程退出
            monDll.cssm_msg_event_deinit();
        }
    }
    public void test() throws InterruptedException
    {
        boolean    ret1 = false;
        int        ret2 = 0;
        CssMonMsg    retMsg = null;
        CssMonGrpNameArray grpArr = null;
        monDll = new CssMonDLL();
        //分配句柄
        ret1 = monDll.cssm_init_handle();
        if (ret1 == false)
        {
            System.out.println("dmcssm alloc handle failed!");
            return;
        }
        else
        {
            System.out.println("dmcssm alloc handle success!");
        }
        //启动消息接收线程
        startThread();
        //初始化监视器，可以选择忽略-7错误（建立到所有CSS连接失败，可能当前CSS都还未启动）
        ret2 = monDll.cssm_init_env(ini_path, log_path);
        if (ret2 < 0 && ret2 != -7) 
        {
            System.out.println("dmcssm init failed!");
            retMsg = monDll.cssm_get_error_msg_by_code(ret2);
            if (retMsg.getReturnCode() >= 0)
            {
                System.out.println("code:" + ret2 + "," + retMsg.getMsg());
            }
            //初始化失败，退出线程，销毁句柄
            endThread();
            monDll.cssm_free_handle();
            return;
        }
        else
        {
            System.out.println("dmcssm init success!");
        }
        grpArr    = monDll.cssm_get_n_group();
        if(grpArr.getReturnCode() < 0)
        {
            System.out.println("get dmcssm group info failed!");
            retMsg = monDll.cssm_get_error_msg_by_code(grpArr.getReturnCode());
            if (retMsg.getReturnCode() >= 0)
            {
                System.out.println("code:" + grpArr.getReturnCode() + "," + retMsg.getMsg());
            }
        }
        else
        {
            System.out.println("dmcssm get group info success, n_group:" + grpArr.getN_group());
        }
        //执行其他接口调用
        //...
        //退出消息线程
        endThread();
        //销毁监视器环境
        monDll.cssm_deinit_env();
        //销毁句柄
        monDll.cssm_free_handle();
        System.out.println("\ndmcssm deinit success!");
    }
    /**
     * @param args
     * @throws InterruptedException 
     */
    public static void main(String[] args) throws InterruptedException {
        CssMonTest test = new CssMonTest();
        test.test();
    }
}
```

## 19.3 DMASMAPIM 接口

DMASMAPIM 接口为配置了镜像的 DMASM 专用。

镜像环境中的大部分 DMASMAPIM 接口和非镜像环境中的 DMASMAPI 接口功能保持不变，只是接口名称发生改变。非镜像环境中接口名称为 DMASM\_XXX，镜像环境中接口名称为 DMASMM\_XXX，均在 DMASM 后面增加一个 M。

### 19.3.1 DMASMAPIM 接口介绍

DMASMAPIM 提供的接口如下：

#### 1\. dmasmm\_sys\_init

**函数原型：**

```
ASMRETURN
dmasmm_sys_init(
  sdbyte*   err_desc,
  udint4*   err_len,
  udint4    char_code,
  udint4    lang_id
)
```

**功能说明：**

环境初始化接口。使用 ASMAPIM 接口，必须第一个调用 dmasmm\_sys\_init 接口。

**参数说明：**

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

char\_code：输入参数，编码。0：PG\_INVALID\_CODE；1：PG\_UTF8；2：PG\_GBK；3：PG\_BIG5；4：PG\_ISO\_8859\_9；5：PG\_EUC\_JP；6：PG\_EUC\_KR；7：PG\_KOI8R；8:PG\_ISO\_8859\_1；9：PG\_SQL\_ASCII；10：PG\_GB18030；11：PG\_ISO\_8859\_11；12：PG\_UTF16。-1 表示使用默认编码。

lang\_id ：输入参数，语言。0：中文；1：英文；2：繁体中文。-1 表示使用默认语言。

#### 2\. dmasmm\_sys\_deinit

**函数原型：**

```
void
dmasmm_sys_deinit()
```

**功能说明：**

环境销毁接口。使用 ASMAPIM 接口结束时，调用 dmasmm\_sys\_deinit 销毁资源。

#### 3\. dmasmm\_alloc\_con

**函数原型：**

```
ASMRETURN
dmasmm_alloc_con(
  asmcon_handle* con,  
  sdbyte*     err_desc,
  udint4*     err_len
)
```

**功能说明：**

申请并初始化连接句柄。返回申请的连接句柄。

**参数说明：**

con：输入参数，连接句柄。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 4\. dmasmm\_close\_con

**函数原型：**

```
void
dmasmm_close_con(
  asmcon_handle  con_in
)
```

**功能说明：**

关闭连接。关闭连接句柄，释放资源。

**参数说明：**

conn\_in：输入参数，连接句柄。

#### 5\. dmasmm\_free\_con

**函数原型：**

```
void
dmasmm_free_con(
  asmcon_handle con_in  
)
```

**功能说明：**

释放连接句柄。

**参数说明：**

con\_in：输入参数，连接句柄。

#### 6\. dmasmm\_connect

**函数原型：**

```
ASMRETURN
  dmasmm_connect(
  asmcon_handle  con_in,   
  sdbyte*     username,  
  sdbyte*     password,  
  sdbyte*     hostname,  
  udint2     portnum,  
  asmbool*    con_is_local,  
  sdbyte*     err_desc,
  udint4*     err_len
)
```

**功能说明：**

登录接口。ASMSVRM 允许本地连接和远程连接，但是 DMSERVER 仅允许本地连接，依据 con\_is\_local 判断是否远程连接。

**参数说明：**

con\_in：输入参数，连接句柄。

username：输入参数，用户名。

password：输入参数，密码。

hostname：输入参数，主机 ip 或主机名。

portnum：输入参数，主机监听端口号。

con\_is\_local：输出参数，标识远程或本地登录。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 7\. dmasmm\_get\_n\_group

**函数原型：**

```
ASMRETURN
dmasmm_get_n_group(
  asmcon_handle  conn_in,  
  udint2*     num,   
  sdbyte*     err_desc,
  udint4*     err_len
)
```

**功能说明：**

获取 ASM Disk Group 个数。获取有多少个磁盘组。

**参数说明：**

conn\_in：输入参数，连接句柄。

num：输出参数，磁盘组个数。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 8\. dmasmm\_get\_group\_id\_arr

**函数原型：**

```
ASMRETURN
dmasmm_get_group_id_arr(
  asmcon_handle  con_in,
  udint2*     id_arr,
   udint4*     au_size_arr,
   udint4*     ex_size_arr,  
  udint2     arr_size,  
  udint2*     num,   
  sdbyte*     err_desc,
  udint4*     err_len
)
```

**功能说明：**

获取 ASM Disk Group ID 数组。配合 dmasmm\_get\_n\_group 使用，获取所有 Disk Group ID。

**参数说明：**

conn\_in：输入参数，连接句柄。

id\_arr：输出参数，磁盘 ID 数组。

au\_size\_arr：输出参数，磁盘组 AU 大小数组。

ex\_size\_arr：输出参数，无实际意义。

arr\_size：输入参数，数组最大长度。

num：输出参数，返回数组长度。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 9\. dmasmm\_get\_disk\_id\_arr\_by\_group

**函数原型：**

```
ASMRETURN
dmasmm_get_disk_id_arr_by_group(
  asmcon_handle  con_in,
  udint2     group_id,   
  udint2*     id_arr,   
  udint2     arr_size,  
  udint2*     n_disk,   
  sdbyte*     err_desc,
  udint4*     err_len
)
```

**功能说明：**

获取磁盘组内磁盘 ID 数组。根据磁盘组 ID 获取磁盘组内包含的所有磁盘 ID。

**参数说明：**

conn\_in：输入参数，连接句柄。

group\_id：输入参数，磁盘组 ID。

id\_arr：输出参数，磁盘 ID 数组。

arr\_size：输入参数，数组最大长度。

n\_disk：输出参数，返回数组长度。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 10\. dmasmm\_get\_disk\_info

**函数原型：**

```
ASMRETURN
dmasmm_get_disk_info(
  asmcon_handle   conn_in,
  udint2       group_id,   
  udint4       disk_id,   
  sdbyte*       path,     
  udint2       path_buflen,   
  sdbyte*       name,   
  udint2       name_buflen,
   sdbyte*      frp_name,  
   udint2        frp_buflen,   
   sdbyte*       status,  
   udint2       status_buflen,
  udint4*       size,     
  udint4*       free_auno,  
  sdbyte*       create_time,   
  sdbyte*       modify_time, 
  sdbyte*       uuid_str,
  sdbyte*       err_desc,
  udint4*       err_len
)
```

**功能说明：**

获取 ASM 磁盘详细信息。根据磁盘组 ID 和磁盘 ID 获取 ASM 磁盘详细信息。

**参数说明：**

conn\_in：输入参数，连接句柄。

group\_id：输入参数，磁盘组 ID。

disk\_id：输入参数，磁盘 ID。

path：输出参数，磁盘路径。

path\_buflen：输入参数，path 缓冲区长度。最长不能超过 256 字节。

name：输出参数，磁盘名称。

name\_buflen：输入参数，name 缓冲区长度。 最长不能超过 32 字节。

frp\_name：输出参数，磁盘所属故障组名称。

frp\_buflen：输入参数，frp\_name 缓冲区长度。最长不能超过 32 字节。

status：输出参数，磁盘状态

status\_buflen：输入参数，status 缓冲区长度。最长不能超过 32 字节。

size：输出参数，磁盘大小，单位 M。

free\_auno：输出参数，最大 AU 号。

create\_time：输出参数，磁盘创建时间。

modify\_time：输出参数，磁盘最近一次修改时间。

uuid\_str：输出参数，磁盘唯一标识。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。最长不能超过 32 字节。

#### 11\. dmasmm\_drop\_diskgroup\_by\_name

**函数原型：**

```
ASMRETURN
dmasmm_drop_diskgroup_by_name(
  asmcon_handle  conn_in, 
  sdbyte*     group_name,   
  sdbyte*     err_desc,
  udint4*     err_len
)
```

**功能说明：**

删除磁盘组。

**参数说明：**

conn\_in：输入参数，连接句柄。

group\_name：输入参数，磁盘组名。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 12\. dmasmm\_file\_create

**函数原型：**

```
ASMRETURN
dmasmm_file_create(
  asmcon_handle   conn_in,
  asmbool     p_flag,   
  sdbyte*      filepath_in,  
  udint8     filesize,  
  asm_fhandle_t* fil_handle, 
  asmbool      need_init,   
  udint2       striping_size,
  udbyte      redundancy_type,
  sdbyte*      err_desc,
  udint4*      err_len
)
```

**功能说明：**

创建 ASM 文件。在 ASM 文件系统中创建 ASM 文件，如果文件父亲目录不存在，并且 p\_flag 为 TRUE 的情况，会自动创建父目录，否则会报错。

**参数说明：**

conn\_in：输入参数，连接句柄。

p\_flag：输入参数，创建父目录标记。

filepath\_in：输入参数，文件路径。

filesize：输入参数，文件大小，单位 Byte。

fil\_handle：输出参数，文件句柄。

need\_init：输入参数，是否需要初始化。

striping\_size：输入参数，条带化粒度。

redundancy\_type：输入参数，镜像类型。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 13\. dmasmm\_file\_open

**函数原型：**

```
ASMRETURN
dmasmm_file_open(
  asmcon_handle   conn_in,  
  sdbyte*      filepath_in,  
  asm_fhandle_t* fhandle,  
  sdbyte*      err_desc,
  udint4*      err_len
)
```

**功能说明：**

打开 ASM 文件，获取 ASM 文件句柄。

DMASM 文件可以重复打开，但是建议用户在使用过程中，尽量避免反复打开同一个 DMASM 文件。如果用户反复打开同一个 DMASM 文件，并且没有及时关闭文件，有可能会降低 DMASM 文件的访问效率。

DMASM 文件句柄不保证全局唯一，只保证连接级别的唯一性，一个连接重复打开同一个 DMASM 文件，会返回不同的文件句柄；不同连接打开同一个 DMASM 文件，有可能返回相同的文件句柄。

**参数说明：**

conn\_in：输入参数，连接句柄。

filepath\_in：输入参数，文件路径。

fhandle：输入参数，文件句柄。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 14\. dmasmm\_file\_trunc

**函数原型：**

```
ASMRETURN
dmasmm_file_trunc(
  asmcon_handle  conn_in,
  asm_fhandle_t  fhandle,  
  udint8      truncate_size,   
  udint8*      real_size,   
  sdbyte*      err_desc,
  udint4*      err_len
)
```

**功能说明：**

截断 ASM 文件。将 ASM 文件截断到 truncate\_size，如果 truncate\_size 小于文件大小，文件会被截断到 truncate\_size；如果 truncate\_size 大于文件大小，文件大小不变，接口返回 EC\_SUCCESS。

**参数说明：**

conn\_in：输入参数，连接句柄。

fhandle：输入参数，文件句柄。

truncate\_size：输入参数，截断后的大小，单位 Byte。

real\_size：输出参数，执行后实际大小，单位 Byte。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 15\. dmasmm\_file\_extend

**函数原型：**

```
ASMRETURN
dmasmm_file_extend(
  asmcon_handle  conn_in,  
  asm_fhandle_t  fhandle,  
  udint8     offset,   
  udint8     extend_size, 
  udint4     need_init,  
  sdbyte*     err_desc,
  udint4*     err_len
)
```

**功能说明：**

扩展 ASM 文件。将文件从 offset 偏移处，扩展 extend\_size 大小，最终实际大小为 offset+extend\_size。如果 offset+extend\_size 大于文件大小，文件会被扩展到 offset+extend\_size 大小；如果 offset+extend\_size 小于文件大小，直接返回成功。

**参数说明：**

conn\_in：输入参数，连接句柄。

fhandle：输入参数，文件句柄。

offset：输入参数，起始偏移。

extend\_size：输入参数，扩展大小。

need\_init：输入参数，是否需要初始化。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 16\. dmasmm\_file\_close

**函数原型：**

```
void
dmasmm_file_close(
  asmcon_handle  conn_in,
  asm_fhandle_t  fhandle   
)
```

**功能说明：**

关闭 ASM 文件。关闭打开的 ASM 文件

**参数说明：**

conn\_in：输入参数，连接句柄。

fhandle：输入参数，文件句柄。

#### 17\. dmasmm\_file\_delete

**函数原型：**

```
ASMRETURN
dmasmm_file_delete(
  asmcon_handle  conn_in,
  sdbyte*      filepath_in,  
  sdbyte*      err_desc,
  udint4*      err_len
)
```

**功能说明：**

删除 ASM 文件。正在被使用的 ASM 文件不能被删除。

**参数说明：**

conn\_in：输入参数，连接句柄。

filepath\_in：输入参数，文件路径。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 18\. dmasmm\_file\_read\_by\_offset

**函数原型：**

```
ASMRETURN
dmasmm_file_read_by_offset(
  asmcon_handle  conn_in,
  asm_fhandle_t  fhandle,  
  udint8       offset,   
  sdbyte*      buffer,   
  udint4       bytes_to_read,   
  sdbyte*      err_desc,
  udint4*      err_len
)
```

**功能说明：**

从 ASM 文件读取数据。从 ASM 文件 offset 偏移读取 bytes\_to\_read 大小的内容到缓冲区 buffer，调用者保证缓冲区够用。因为块设备读写限制，offset, buffer, bytes\_to\_read 都必须能被 512 整除，否则会报错。

**参数说明：**

conn\_in：输入参数，连接句柄。

fhandle：输入参数，文件句柄。

offset：输入参数，起始偏移。

buffer：输入参数，缓冲区。

bytes\_to\_read：输入参数，读取数据大小，单位 Byte。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 19\. dmasmm\_file\_read\_by\_offset\_normal

**函数原型：**

```
ASMRETURN
dmasmm_file_read_by_offset_normal(
  asmcon_handle  conn_in,
  asm_fhandle_t  fhandle,  
  udint8       offset,   
  sdbyte*      buffer,   
  udint4       bytes_to_read,   
  sdbyte*     err_desc,
  udint4*     err_len
)
```

**功能说明：**

从 ASM 文件读取数据。从 ASM 文件 offset 偏移读取 bytes\_to\_read 大小的内容到缓冲区 buffer，调用者保证缓冲区够用。该接口支持 offset、buffer、bytes\_to\_read 不是 512 整数倍，但是性能比 dmasmm\_file\_read\_by\_offset 慢。

**参数说明：**

conn\_in：输入参数，连接句柄。

fhandle：输入参数，文件句柄。

offset：输入参数，起始偏移。

buffer：输入参数，缓冲区。

bytes\_to\_read：输入参数，写取数据大小，单位 Byte。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 20\. dmasmm\_file\_write\_by\_offset

**函数原型：**

```
ASMRETURN
dmasmm_file_write_by_offset(
  asmcon_handle  conn_in,
  asm_fhandle_t  fhandle,  
  udint8       offset,   
  sdbyte*      buffer,  
  udint4       bytes_to_write, 
  sdbyte*      err_desc,
  udint4*      err_len
)
```

**功能说明：**

将数据写入 ASM 文件。将缓冲区中的内容写入 ASM 文件，从 offset 偏移开始。因为块设备读写限制，offset，buffer 地址，bytes\_to\_write 都必须能被 512 整除。

**参数说明：**

conn\_in：输入参数，连接句柄。

fhandle：输入参数，文件句柄。

offset：输入参数，起始偏移。

buffer：输入参数，缓冲区。

bytes\_to\_write：输入参数，写数据大小，单位 Byte。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 21\. dmasmm\_file\_write\_by\_offset\_normal

**函数原型：**

```
ASMRETURN
dmasmm_file_write_by_offset_normal(
  asmcon_handle  conn_in,
  asm_fhandle_t  fhandle,  
  udint8     offset,   
  sdbyte*      buffer,   
  udint4       bytes_to_write,   
  sdbyte*      err_desc,
  udint4*      err_len
)
```

**功能说明：**

将数据写入 ASM 文件。将缓冲区中的内容写入 ASM 文件，从 offset 偏移开始。该接口支持 offset、buffer、bytes\_to\_write 不是 512 倍数，但是性能比 dmasmm\_file\_write\_by\_offset 慢。

**参数说明：**

conn\_in：输入参数，连接句柄。

fhandle：输入参数，文件句柄。

offset：输入参数，起始偏移。

buffer：输入参数，缓冲区。

bytes\_to\_write：输入参数，写数据大小，单位 Byte。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 22\. dmasmm\_file\_copy

**函数原型：**

```
ASMRETURN
dmasmm_file_copy(
  asmcon_handle  conn_in,
  sdbyte*      source_in,   
  sdbyte*      dest_in,  
  asmbool      bOverwriteIfExists,
  sdbyte*      err_desc,
  udint4*      err_len
)
```

**功能说明：**

文件拷贝操作。支持 ASM 文件拷贝到 ASM 文件；ASM 文件拷贝到普通文件系统文件；普通文件系统文件拷贝到 ASM 文件系统；不支持普通文件拷贝到普通文件。bOverwriteIfExists：0 或者 NULL 表示不覆盖，其他非 0 值表示覆盖。

**参数说明：**

conn\_in：输入参数，连接句柄。

source\_in：输入参数，源文件路径。必须是全路径，不能是相对路径。

dest\_in：输入参数，目标文件路径。必须是全路径，不能是相对路径。

bOverwriteIfExists：输入参数，如果目标存在是否删除。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 23\. dmasmm\_dir\_create

**函数原型：**

```
ASMRETURN
dmasmm_dir_create(
  asmcon_handle  conn_in, 
  asmbool      p_flag,   
  sdbyte*      fdir_in,  
  sdbyte*      err_desc,
  udint4*      err_len
)
```

**功能说明：**

创建目录。ASM 文件系统创建目录，当 p\_flag=TRUE 时会级联创建父目录，否则父目录不存在会报错。

**参数说明：**

conn\_in：输入参数，连接句柄。

p\_flag：输入参数，是否级联创建父目录。

fdir\_in：输入参数，目录路径。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 24\. dmasmm\_dir\_delete

**函数原型** ：

```
ASMRETURN
dmasmm_dir_delete(
  asmcon_handle  conn_in,
  sdbyte*      fdir_in,
  sdbyte*      err_desc,
  udint4*      err_len
)
```

**功能说明：**

删除目录，以及目录下面所有的文件。

**参数说明：**

conn\_in：输入参数，连接句柄。

fdir\_in：输入参数，目录路径。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 25\. dmasmm\_get\_file\_num\_by\_group

**函数原型：**

```
ASMRETURN
dmasmm_get_file_num_by_group(
  asmcon_handle    conn_in,
  udint2        group_id,
  udint4*        num,  
  sdbyte*        err_desc,
  udint4*        err_len
)
```

**功能说明：**

获取磁盘组内总的文件个数。根据磁盘组 ID 获取总的文件个数，包括文件和目录。

**参数说明：**

conn\_in：输入参数，连接句柄。

group\_id：输入参数，磁盘组的 ID 。

num ：输出参数，文件的个数。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 26\. dmasmm\_get\_file\_info

**函数原型：**

```
ASMRETURN
dmasmm_get_file_info(
  asmcon_handle  conn_in,
  asm_fhandle_t  file_id,
  ASM3_FILE_ATTR* fattr_out,
  sdbyte*      err_desc,
  udint4*      err_len
)
```

**功能说明：**

获取 ASM 文件详细信息。

ASM3\_FILE\_ATTR 包括：

type：目录标记，整型。1 表示文件，2 表示目录。

name：文件名称，字符型。

full\_path：完整路径，字符型。

size：文件大小，整型，单位 Byte。目录忽略此字段。

c\_time：创建时间，time\_t 类型。

m\_time：修改时间，time\_t 类型。

group\_id：所在磁盘组编号，整型。

disk\_id：inode 项所在磁盘 ID，整型。

disk\_auno：inode 项所在磁盘 AU 编号，整型。

offset：inode 项 AU 偏移，整型。

fil\_id：文件句柄，asm\_fhandle\_t 类型。

strip:文件条带化粒度，整型。

n\_copy:文件镜像类型，即副本数，整型。

fil\_id：文件句柄。

strip:文件条带化粒度。

n\_copy:文件镜像类型，即副本数。

**参数说明：**

conn\_in：输入参数，连接句柄。

file\_id：输入参数，打开的文件句柄。

fattr\_out：输出参数，文件属性结构。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 27\. dmasmm\_get\_group\_info\_by\_name

**函数原型：**

```
ASMRETURN
dmasmm_get_group_info_by_name(
  asmcon_handle  con_in,
  sdbyte*      group_name,
  udint2*      group_id,
  udint2*      status,  
  udint2*      n_disk,
  udint4*      total_size,
  udint4*      free_size,
  sdbyte*      err_desc,
  udint4*      err_len  
)
```

**功能说明：**

通过磁盘组名获取磁盘组详细信息。

**参数说明：**

con\_in：输入参数，连接句柄。

group\_name：输入参数，磁盘组名字。

group\_id：输出参数，磁盘组 ID。

status：输出参数，磁盘组状态。1：正在创建中；2：正常的；3：正在删除中。

n\_disk：输出参数，磁盘数。

total\_size：输出参数，磁盘组大小，单位 AU。

free\_size：输出参数，磁盘组空闲大小，单位 AU。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 28\. dmasmm\_get\_group\_info\_by\_id

**函数原型：**

```
ASMRETURN
dmasmm_get_group_info_by_id(
  asmcon_handle  con_in,
  udint2      group_id,
  sdbyte*      group_name,
  udint2      name_buflen,
  udint2*      status,  
  udint2*      n_disk,
  udint4*      total_size,
  udint4*      free_size,
  udint4*     au_size,  
  byte*       n_copy,   
  udint4*      redo_size, 
  udint2*      rbl_stat,
  udint2*      rbl_pwr,
  sdbyte*      err_desc,
  udint4*      err_len  
)
```

**功能说明：**

通过磁盘组 ID 获取磁盘组详细信息。

**参数说明：**

con\_in：输入参数，连接句柄。

group\_id：输入参数，磁盘组 ID。

group\_name：输出参数，磁盘组名字。

name\_buflen：输入参数，磁盘组的 buf 长度。

status：输出参数，磁盘组状态。1：正在创建中；2：正常的；3：正在删除中。

n\_disk：输出参数，磁盘数。

total\_size：输出参数，磁盘组大小，单位 AU。

free\_size：输出参数，磁盘组空闲大小，单位 AU。

au\_size：输出参数，磁盘组 AU 大小，单位 Byte。

n\_copy：输出参数，磁盘组镜像类型。

redo\_size：输出参数，磁盘组中 redo 日志文件大小。

rbl\_stat：输出参数，磁盘组重平衡状态。0：未启用；1：已启用。

rbl\_pwr：输出参数，磁盘组重平衡并行度。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 29\. dmasmm\_dir\_get\_first

**函数原型** ：

```
ASMRETURN
dmasmm_dir_get_first(
  asmcon_handle    conn_in,
  sdbyte*        path_in,
  sdbyte*        suffix,
  asm_dhandle_t*    dir_handle_out,
  ASM3_FILE_ATTR*   fattr_out,
  asmbool*       exist_flag,
  sdbyte*        err_desc,
  udint4*        err_len
)
```

**功能说明：**

获取目录下第一个文件信息。

**参数说明：**

conn\_in：输入参数，连接句柄。

path\_in：输入参数，目录路径。

suffix：输入参数，指定扩展名关键字，如：”.log”。用于取出以指定关键字作为扩展名的文件。

dir\_handle\_out：输出参数，打开的目录句柄。

fattr\_out：输出参数，文件属性结构。

exist\_flag：输出参数，是否存在。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 30\. dmasmm\_dir\_get\_next

**函数原型：**

```
ASMRETURN
dmasmm_dir_get_next(
  asmcon_handle    conn_in,
  asm_dhandle_t    dir_handle,
  sdbyte*        path_in,
  sdbyte*        suffix,
  ASM3_FILE_ATTR*    fattr_out,
  asmbool*       exist_flag,
  sdbyte*        err_desc,
  udint4*        err_len
)
```

**功能说明：**

获取目录下下一个文件信息，须配合函数 dmasmm\_dir\_get\_first 使用。

**参数说明：**

conn\_in：输入参数，连接句柄。

dir\_handle：输入参数，打开的目录句柄。

path\_in：输入参数，目录路径，须与目录句柄 dir\_handle 中打开的 path\_in 保持一致。

suffix：输入参数，指定扩展名关键字，如：”.log”。用于取出以指定关键字作为扩展名的文件。

fattr\_out：输出参数，文件属性结构。

exist\_flag：输出参数，是否存在。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 31\. dmasmm\_dir\_close

**函数原型：**

```
ASMRETURN
dmasmm_dir_close(
  asmcon_handle   conn_in,
  asm_dhandle_t   dir_handle,
  sdbyte*       err_desc, 
  udint4*       err_len 
)
```

**功能说明：**

关闭目录。

**参数说明：**

con\_in：输入参数，连接句柄。

dir\_handle：输入参数，打开的目录句柄。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 32\. dmasmm\_file\_attributes\_get

**函数原型：**

```
ASMRETURN
dmasmm_file_attributes_get(
  asmcon_handle    conn_in,
  sdbyte*        path,
  ASM3_FILE_ATTR*    fattr_out,
  sdbyte*        err_desc,
  udint4*        err_len
)
```

**功能说明：**

根据文件路径获取文件详细信息。

**参数说明：**

conn\_in：输入参数，连接句柄。

path：输入参数，路径。

fattr\_out：输出参数，文件属性结构。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

#### 33\. dmasmm\_file\_is\_exist

**函数原型：**

```
ASMRETURN
dmasmm_file_is_exist(
    asmcon_handle   conn_in,
    sdbyte*         path,
    sdbyte*         err_desc,
    udint4*         err_len
)
```

**功能说明：**

判断 ASM 文件系统中，以 path 为文件路径的文件是否存在。

**参数说明：**

conn\_in：输入参数，连接句柄。

path：输入参数，文件路径。

err\_desc：输出参数，错误描述信息。

err\_len：输入输出参数，错误描述信息长度。

### 19.3.2 返回值说明

返回值分为三种类型：正数，0 和负数。0 表示正常；正数为警告信息；负数为错误信息，对应的错误码请参考 19.3.3 错误码汇编 。

### 19.3.3 错误码汇编

DMASMAPIM 和 DMASMAPI 共用一套错误码。错误码值域从-11000 开始。具体可参考 V$ERR\_INFO。

### 19.3.4 编程示例

下面举一个简单的例子，展示 DMASMAPIM 的使用方法。若本示例在编译过程中出现实参过多或者变量未声明等问题，可查询相应版本的 DMASMAPIM 接口使用手册，适当增减参数或者将变量改为实际值。

```
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "asmapi3.h"

#define TRUE        1
#define FALSE       0

#define IS_SUCCESS(code)    ((sdint4)code >= 0)
#define RET_IF_ERR_EX(c, act) \
    { if (!IS_SUCCESS(c)) { {act;} return (c); }}

/*运行前修改file_name username passwd ip port
  镜像不支持远程写，示例程序需要和服务端在同一台机器
  LINUX下编译
  gcc -DLINUX -I/home/test/include test.c -L. -ldmasmapim -o demo
  -I:指定头文件目录，本例中需要指定asmapi3.h头文件所在目录
  -L(大写L):指定库搜索路径
  -l(小写L):指定库名
  -D:定义预处理宏*/
int
main(
    int             argc,
    char*           argv[]
)
{
    int             code = 0;
    char            err_desc[1024];
    int             err_len;
    asm_fhandle_t   fil_handle;
    void*           conn;
    char*           wbuf        = "hello asm";
    char            rbuf[10];
    int             len;
    int             file_size = 20;       //单位字节
int             offset = 0;
  int             strip_size  = 0;      //条带大小
    int             redundancy_type = 1;  //镜像类型
    char*           username = "ASMSYS";
    char*           passwd = "DCRpsd_123";
    char*           file_name = "+DATA/test1.dta";
    char*           ip = "192.168.1.118";
    int             port = 10060;

#ifdef WIN32
    /*windows环境需要添加附加依赖项ws2_32.lib*/
    WSADATA WsaData;
    if (SOCKET_ERROR == WSAStartup(0x0101, &WsaData))
    {
        fprintf(stderr, "WSAStartup Failed\n");
        exit(-1);
    }
#endif

    err_len         = sizeof(err_desc);
    len             = (int)strlen(wbuf);

    code = dmasmm_sys_init(err_desc, &err_len, -1, 1);
    if (!IS_SUCCESS(code))
    {
        fprintf(stderr, "dmasmm_sys_init error:[%s]\n", err_desc);
        return -1;
    }

    /* 分配连接句柄 */
    code = dmasmm_alloc_con(&conn, err_desc, &err_len);
    if (!IS_SUCCESS(code))
    {
        fprintf(stderr, "dmasmm_alloc_con error:[%s]\n", err_desc);
        return -1;
    }

    /* 登录asmsvr，本地登录不校验密码，可以输入任意字符串，远程登录会校验用户名密码*/
    code = dmasmm_connect(conn, username, passwd, ip, port, NULL, err_desc, &err_len);
    if (!IS_SUCCESS(code))
    {
        fprintf(stderr, "dmasmm_connect error:[%s]\n", err_desc);
        return -1;
    }

    /* 文件存在直接打开 */
    if (dmasmm_file_is_exist(conn, file_name, err_desc, &err_len) == TRUE)
    {
        code = dmasmm_file_open(conn, file_name, &fil_handle, err_desc, &err_len);
        RET_IF_ERR_EX(code, goto fun_end);
    }
    else
    {
        /* 在已有的磁盘组内创建asm文件， */
        code = dmasmm_file_create(conn, 1, file_name, file_size, &fil_handle, FALSE, strip_size, redundancy_type, err_desc, &err_len);
        if (!IS_SUCCESS(code))
        {
            fprintf(stderr, "dmasmm_file_create error code:%d [%s]\n", code, err_desc);
            goto fun_end;
        }
    }

    /* 写文件 */
    code = dmasmm_file_write_by_offset_normal(conn, fil_handle, offset, wbuf, len, err_desc, &err_len);
    if (!IS_SUCCESS(code))
    {
        fprintf(stderr, "dmasmm_file_write_by_offset_normal error code:%d [%s]\n", code, err_desc);
        goto fun_end;
    }

    /* 读文件 */
    code = dmasmm_file_read_by_offset_normal(conn, fil_handle, offset, rbuf, len, err_desc, &err_len);
    if (!IS_SUCCESS(code))
    {
        fprintf(stderr, "dmasmm_file_write_by_offset_normal error code:%d [%s]\n", code, err_desc);
        goto fun_end;
    }
    else
    {
        rbuf[len] = '\0';
        fprintf(stderr, "dmasmm_file_write_by_offset_normal succ buf:%s\n", rbuf);
    }

fun_end:
    // 文件存在就关闭删除
    if (dmasmm_file_is_exist(conn, file_name, err_desc, &err_len) == TRUE)
    {
        /* 关闭打开的文件句柄，否则删除会报错 */
        dmasmm_file_close(conn, fil_handle);

        /* 删除文件 */
        code = dmasmm_file_delete(conn, file_name, err_desc, &err_len);
        if (!IS_SUCCESS(code))
        {
            fprintf(stderr, "dmasmm_file_delete error:[%s]\n", err_desc);
        }
    }

    dmasmm_close_con(conn);
    dmasmm_free_con(conn);
    dmasmm_sys_deinit();
    return 0;
}
```
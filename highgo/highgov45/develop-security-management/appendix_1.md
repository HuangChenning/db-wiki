---
title: "附录1 安全功能相关的参数说明"
book: "HGDB 安全管理手册"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/develop/appendix_1.html"
tags:
  - highgo
  - highgo-v45
  - develop-security-management
---

## 附录1 安全功能相关的参数说明

仅安全版支持

| **安全参数** | **子参数名** | **参数说明** |
| --- | --- | --- |
| hg\_sepofpowers |  | 三权分立功能开关，默认on，开启三权功能；off为关闭三权分立，关闭后即无安全功能。参数值重启生效。 |
| hg\_macontrol |  | 强制访问控制功能开关，默认on，开启强制访问控制；参数值为min，表示强访功能最小化，即只有自主访问控制功能。参数值重启生效。 |
| hg\_rowsecure |  | 行级强制访问功能开关。该参数只在hg\_macontrol为on时生效。参数值为on |
| hg\_showlogininfo |  | 登入信息显示开关。（管理工具和psql客户端，参数值为on |
| hg\_clientnoinput |  | session不活动无操作自动断开的时间(有事务运行则不会断开)。参数范围值为0-1440分钟；默认30分钟，设置为0则不限制。参数值重启生效。  备注：hg\_clientnoinput受 hg\_idcheck.enable开关控制。关闭hg\_idcheck.enable后，hg\_clientnoinput参数不生效。 |
| hg\_idcheck.子参数名 | enable | 该参数相当于其他子参数的总开关。默认值为on，开启身份鉴别，其他子参数以默认值显示;off为关闭身份鉴别，所有身份鉴别相关参数均不生效。参数值重启生效。 |
|  | pwdlock | 密码连续输入错误多少次后账户被锁，默认5次。参数范围值为0-10次,设置为0表示不限制密码错误次数，重启后密码连续错误次数重新计算。参数值动态（不重启）生效。 |
|  | pwdlocktime | 密码连续错误次数超限被锁定的时间，默认24小时，参数范围值为0-240小时。设置为0则表示一直被锁定，但可以通过syssso解锁。参数值动态（不重启）生效。 |
|  | pwdvaliduntil | 参数功能为密码有效期，参数范围值为0-365天，默认7天，设置值为0表示不限制天数。参数值动态（不重启）生效。 |
|  | pwdpolicy | 参数有low、medium、high、highest四个参数值，设置为low时表示密码不受限制；设置为medium表示密码长度至少为8位，必须包含字母和数字；设置为high表示密码长度至少为8位，必须包含字母、数字和特殊字符。highest,包含常用密码、保留字、关键字等所有密码规则。默认为highest参数值动态（不重启）生效。 |
| hg\_sepv4 |  | 该选项的值可以为v4或者v45。默认值为v4，表示三权分立为V4版本。  可设置为v45，表示三权分立的版本为V45版本。  当hg\_sepofpowers为on时，此选项才会生效。  改变此选项的值后需要重启数据库生效。  注：该参数在HGDB-SEE V4.5.5及以后的版本中支持 |

**安全参数查询**

登录syssso用户，执行select show\_secure\_param(); 可以显示所有的安全参数。

**安全参数设置**

登录syssso用户，执行select set\_secure\_param(‘参数名’,’参数值’);来设置某个安全开关和安全参数值。

注：参数名和参数值都需要用西文单引号包括。

示例：

> select set\_secure\_param(‘hg\_showlogininfo’,’off’);

关闭登录信息的显示。

有的安全参数拥有子参数，语法为安全参数和子参数之间加一个.即可。

示例：

> select set\_secure\_param(‘hg\_idcheck.pwdlocktime’,’3’);
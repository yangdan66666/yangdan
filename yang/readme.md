# Django项目

我的工程代码将陆续开源并对外，更新在github，地址：
https://github.com/yangdan66666/yangdan

第一期：文件上传，下载，直接打开，共享功能实现


常见问题：

1、适用人群

使用人员：需具备python3.6.4的开发编程基础。了解django框架，了解web前端知识。

2、环境配置：
python3.6.4的开发编程基础，django1.8版本，需手动安装sqlite3数据库。

3、工程大体思维：
创建django项目yang，配置setting.py文件，创建子应用index接收页面跳转，在子应用中实现功能。
用户的注册完成时，将在子应用index/templates/文件 中创建注册用户名的文件夹，以便存储上传文件，以及区分不同用户上传相同文件名文件。
sqlite3数据库使用默认为yd.db库，如需更改，需在setting.py文件中更改DATABASES中的NAME的值。其中有数据表两张，分别为：
用户信息表Users和文件信息表wenjian，都是通过models.py文件映射至数据库。
其中默认页面urls为空。

4、项目欠缺：

如下载已上传文件或别人共享给自己账户的文件时，需下载的文件名为中文，下载后的文件名为默认文件名(下载1，...)，需手动更改文件名称以及文件名后缀。

工程是基于python3.6.4开发的，不支持py2.7及以下版本
如发现项目其他bug，或需求不能满足时；请联系：
微信：13256152910；邮箱：yangdan66666@sina.com

项目会在后期不断更新完善在github；更新地址：https://github.com/yangdan66666/yangdan

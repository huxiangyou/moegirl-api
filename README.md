# 萌娘百科API工具集

![python 3.8](https://img.shields.io/badge/python-3.8-blue.svg?logo=python)
![test: passed](https://img.shields.io/badge/test-passed-brightgreen.svg)
[![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/mit-license.php)

葫芦又写于2020年1月至3月。

利用[萌娘百科的API](https://zh.moegirl.org.cn/api.php)做些有用的没用的东西。

**此工具集中的程序已过期，并不再提供维护。**此repository已于2020年7月存档。

萌娘百科®、Moegirlpedia®是注册商标。此程序仅提供API功能。有关使用萌娘百科的内容时需遵守的版权协定，请参阅[萌娘百科的版权信息](https://zh.moegirl.org.cn/萌娘百科:版权信息)。

## 注意

这些程序全部“**按原样**”提供。请在运行之前按你的需要调整其中的内容。本人不负责提供教程等。

这些程序都是我闲得没事写的。只提供代码参考，不保证实际作用。

这些程序其实可以合并。只是因为我一般一次只需要使用其中一个功能，所以将它们拆分了。所以有部分程序的功能是重复或部分重复的。

本程序依赖萌娘百科的API。有关API的内容，参见[萌娘百科的API帮助](https://zh.moegirl.org.cn/api.php)。

在安装完成Python之后，需要额外安装`requests`包，用于网络连接。需要额外安装`openpyxl`包，用于读取和写入工作表文件。

## 文件列表

`PID` = Page ID，页面ID  
`RID` = Revision ID，历史版本ID

### 库文件

#### `second2days.py`

葫芦又写于2019年10月3日。

将秒数转换为时间表述。  
例：`second2days.main(114514)` → `'1 day 7 hours 48 minutes 34 seconds'`

### 列表文件

#### `PAGELIST.xlsx`

页面列表，分为条目(`主`)、模板(`Template`)、分类(`Category`)三页。  
第2列为`PID`。第3列为`RID`。第4列为页面标题。第5列为对应讨论页ID。第6列为到此页的重定向列表，以`set`格式放置。  
例：`73446`, `3299038`, `矢泽妮可`, `82097`, `{'矢泽仁子', '矢泽にこ', '矢泽日香', '矢泽妮歌'}`

#### `PAGELIST.txt`

页面列表。  
第1列为页面属性，由人工定义。第2列为`PID`。第3列为页面标题。中间用`\t`间隔。  
例：`[M___]	73446	矢泽妮可`

#### `imagelist.xlsx`

文件列表。  
第2列为`PID`。第3列为文件名。第4列为文件大小，单位是字节。  
例：`85830`, `File:LLhead.png`,`19370`

#### `imagelist.txt`

文件列表。  
只有文件名。  
例：`File:LLhead.png`

### 程序文件

以下文件名中，`moegirl`表示萌娘百科，第2部分表示其功能，第3部分表示其列表来源。

#### `moegirl_archive_txt.py`

将`PAGELIST.txt`列出的页面存档为文本文档。  
具体参见[moegirl-archive](https://github.com/huxiangyou/moegirl-archive)。

#### `moegirl_archive_xls.py`

将`PAGELIST.xlsx`列出的页面存档为文本文档。  
同上。

#### `moegirl_category_xls.py`

查找`PAGELIST.xlsx`中的分类收录的，但没有在`PAGELIST.xlsx`中列出的页面。  
输出例：``[类] [Cat] Categoty:LoveLive! [PID] 73446 [Title] 矢泽妮可``

#### `moegirl_edit.py`

函数库。登录，并编辑。包括替换页面内容、追加内容、替换字符串。  
运行程序前需要在代码中输入用户名和密码。

#### `moegirl_editbatch_txt.py`

使用`moegirl_edit.py`中的替换字符串功能，替换`PAGELIST.txt`的页面中的字符串。  
运行程序前需要在代码中输入用户名和密码。  
注意：在正式运行程序前，请务必先做测试，并保证测试通过。  
请优先考虑在[操作请求版](https://zh.moegirl.org.cn/萌娘百科_talk:讨论版/操作请求)请求批量替换，而不是擅自对条目进行大规模修改。  
输出例：``[替换] [√] [PID] 73446``

#### `moegirl_editorrevs_txt.py`

统计`PAGELIST.txt`中的页面，各用户的编辑次数及页面数。  
可以指定统计“最近一段时间”的编辑。  
输出例：``275 126 Bob1301``

#### `moegirl_editorrevsizes_txt.py`

统计`PAGELIST.txt`中的页面，各用户的编辑次数、页面数和添加字符数。  
可以指定统计“最近一段时间”的编辑。  
输出例：``275 126 -30904 Bob1301``

#### `moegirl_fileusage_txt.py`

统计`imagelist.xlsx`中的文件被`PAGELIST.txt`外的页面使用，及没有被任何页面使用的情况。  
输出例：``[图用][外] [File]File:Niconico ni.gif [Page]81515 偶像宅``  
``[图][没用] [File]File:Love Live!.jpg``

#### `moegirl_fileusage_xls.py`

统计`imagelist.xlsx`中的文件被`PAGELIST.xlsx`外的页面使用，及没有被任何页面使用的情况。  
输出例：``[图用][外] [File]File:Niconico ni.gif [Page]81515 偶像宅``  
``[图][没用] [File]File:Love Live!.jpg``

#### `moegirl_imagecontributors_txt.py`

统计用户上传或编辑`imagelist.txt`中的文件的个数。  
运行结果例：``{'胡祥又': 3220}``

#### `moegirl_imageinfo_xls.py`

统计`imagelist.xlsx`中的文件的大小、文件名等，并按文件格式区分。  
输出例：``[文件] [FID] 85830 [Size] 19370 [Title] File:LLhead.png``  
运行结果例：``[MIME] image/png [Pages] 4563 [Size] 1260052343``

#### `moegirl_imagelist_xls.py`

查找`PAGELIST.xlsx`中的页面使用了的，或给定分类包含的，但没有被`imagelist.txt`收录的文件。  
输出例：``[图][使用] [From] LoveLive! [File] File:LLhead.png``  
``[图][分类] [Cate] Category:LoveLive! [File] File:LLhead.png``

#### `moegirl_linklist_txt.py`

查找`PAGELIST.txt`中的页面包含的，但没有被`PAGELIST.txt`和`imagelist.txt`收录的页面或文件链接。  
输出例：``[链] [PID] 73446 [Title] 矢泽妮可 [Link] 贫乳``

#### `moegirl_linklist_xls.py`

查找`PAGELIST.xlsx`中的页面包含的，但没有被`PAGELIST.xlsx`和`imagelist.txt`收录的页面或文件链接。  
输出例：``[链] [PID] 73446 [Title] 矢泽妮可 [Link] 贫乳``

#### `moegirl_linkshere_txt.py`

查找包含链接到`PAGELIST.txt`中的页面的链接的，但没有被`PAGELIST.txt`收录的页面。  
输出例：``[链][外] [Linked] 73446 矢泽妮可 [From] 5052 贫乳``

#### `moegirl_linkshere_xls.py`

查找包含链接到`PAGELIST.xlsx`中的页面的链接的，但没有被`PAGELIST.xlsx`收录的页面。  
输出例：``[链][外] [Linked] 73446 矢泽妮可 [From] 5052 贫乳``

#### `moegirl_main_xls.py`

更新`PAGELIST.xlsx`中的`RID`、页面标题、讨论页ID、重定向列表。  
输出例：``[页][编辑] [PID] 74901 [Title] LoveLive! [Rev] 3217888``

#### `moegirl_pagecontributors_txt.py`

统计用户编辑`PAGELIST.txt`中的页面的个数。  
运行结果例：``{'胡祥又': 585}``

#### `moegirl_pageid.py`

列出给出的页面标题对应的`PID`。  
输出例：``74901 LoveLive!``

#### `moegirl_pageid_txt.py`

列出`PAGELIST.txt`的`PID`对应的页面标题。  
输出例：``74901 LoveLive!``

#### `moegirl_pagesize_txt.py`

统计`PAGELIST.txt`中的页面的长度。  
输出例：``[M___] [PID] 74901 [Size] 56449 [Title] LoveLive!``

#### `moegirl_prefix_txt.py`

搜索标题中包含给出的关键词的，但没有被`PAGELIST.txt`收录的页面。  
输出例：``[新] [PID] 74901 [Title] LoveLive!``

#### `moegirl_prefix_xls.py`

搜索标题中包含给出的关键词的，但没有被`PAGELIST.xlsx`收录的页面。  
输出例：``[新] [PID] 74901 [Title] LoveLive!``

#### `moegirl_prefixfile_xls.py`

搜索文件名中包含给出的关键词的，但没有被`imagelist.xlsx`收录的文件。  
输出例：``[新] [Find] LL [FID] 85830 [Title] File:LLhead.png``

#### `moegirl_samefile_xls.py`

列出与`imagelist.xlsx`中的文件相同的文件。  
输出例：``[图][同] [File] 234544 File:Tenpo03b.png [Same] File:LonelyTuning.png``

#### `moegirl_templatelist_txt.py`

查找`PAGELIST.txt`中的页面使用了的，但没有被`PAGELIST.txt`收录的模板。  
输出例：``[用][模板] [M___] [PID] 74901 [Template] Template:Lj``

#### `moegirl_templatelist_xls.py`

查找`PAGELIST.xlsx`中的页面使用了的，但没有被`PAGELIST.xlsx`收录的模板。  
输出例：``[用][模板] [M___] [PID] 74901 [Template] Template:Lj``

#### `moegirl_templateusage_txt.py`

查找使用了`PAGELIST.txt`中的模板，但没有被`PAGELIST.txt`收录的页面。  
输出例：``[模用][外] [Temp] 156827 Template:LoveLiveSongGai/SIF  [Page] 340870 伟大的决斗``

#### `moegirl_userimage_xls.py`

查找给定用户上传或编辑过的文件，但没有被`imagelist.xlsx`收录的页面。  
输出例：``[用贡][新图] [User] 胡祥又 [File] 85830 File:LLhead.png``

## 其他

如果有任何疑问，请在[Issues](https://github.com/huxiangyou/moegirl-archive/issues)提出。

## 有道云笔记5.x版本ynt备份文件解析

>使用Anaconda 2.7

### 功能介绍

- 解析有道云笔记备份文件(.ynt),并生成笔记的HTML文件.生成的HTML中包括原笔记的文字和图片.
- 生成的HTML可以导入到Wiz笔记(或其他笔记软件,未测试其他的).

### 功能限制
- 原笔记的附件并不能附在HTML中,同样也不能导入到Wiz中.
- **云协作**中笔记内容会出现多余的乱码.
- 原笔记本的层级结构丢失.

### How to use
- 打开有道云笔记win端,选择 导出 –> 有道云笔记
- 将后缀ynt的笔记备份文件解压缩,得到笔记备份文件夹(如解压失败,可参考[Issue](https://github.com/elitezhe/ynotebackparsing/issues/1))
- 修改myconfig.py中的路径(注意,如果有路径中存在\U,最好加一个反斜杠改成\\\U)
- 确认本机已安装好对应版本的Python和相应的包,如不确定Anaconda是一个很好的选择
- 运行rename_attachments.py





# HexoPubAssistant
本软件是为了那些使用Hexo搭建博客但又嫌发布博文麻烦的懒人而写的博客发布助手程序（兼个人PyQt练习），目前只提供Windows平台的预编译包，其他平台的用户请检查requirements.txt。

# 《HexoPubAssistant使用文档》

1. 介绍
   此软件是为了免去每次使用hexo发布博客时的繁琐流程，不用每次都手动hexo new，hexo g，hexo s。  
   使用前请进入程序目录根据你的hexo本地目录配置config.txt，不然程序会无法正常使用。    

   本软件使用“源云明体”字体：https://github.com/ButTaiwan/genwan-font     

   本软件的所有配置文件都不建议使用记事本进行编辑，如需修改，请备份或使用Notepad++   

2. 使用前的配置

   下面的目录结构是我的hexo本地目录:

   ```
   |-- node_modules
   |-- public
   |-- scaffolds
   |-- source
   |   |-- _posts
   |   |-- about
   |   |-- archives
   |   |-- categories
   |   |-- tags
   |   `-- \315\274\306\254\261\270\267\335
   |-- themes
   |   |-- hiker
   |   `-- landscape
   `-- vultrstaticsite
       |-- css
       |-- images
       `-- js
   ```

   首次使用你需要重新配置程序目录中的config.txt，location选项设置为hexo本地目录，参考程序自带的config的目录设置，
   posts_location设置为hexo本地目录的source\\_posts目录，里面存着的是hexo生成的markdown文件。  
   配置完毕重启程序即可。  
   如果配置文件读取失败、错误，将无法正常使用本软件。

3. 使用教程

   主界面的“博文信息”是不可编辑的，用于显示你刚创建的博文的基本信息。  
   “博文状态”是很重要的信息，具体请看软件的提示对话框。  
   “打开博文以编辑”只有创建了新博文才能使用，按下该按钮会使用用户Windows中.md文件的默认程序打开，我建议使用Typora进行博文编写。  
   “现有博文分类”用于显示你所有博客的categories项目，只读，便于用户参考。  
 
   “文件”-“新建博文”用于创建新博文，对话框里填入的内容只会当“一个值”记录到你刚创建的博文头部信息中。  
   “预览”、“发布”对应hexo server和hexo deploy。  

   “手动扫描全部分类”用于更新“现有博文分类”。  
   “打开配置文件”将使用用户系统中默认的程序打开该文件。  

# 祝使用愉快
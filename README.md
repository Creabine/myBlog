# myBlog

尝试写一个自己的博客，前后端都由自己起来完成，感觉是个很大的项目，准备一点一点来，功能方面也是先 从简单的开始，以后再慢慢迭代。

#预期将要使用的技术

后端: Python Django jinjia2 SQLite 

前端: vue sass gulp 


**以下是版本说明，按照倒序排列：**

# V1.1.3    2016.12.6
使用vue显示博客详情页中的内容，评论等；

完善了tag，category功能；

完善了提交评论的功能；

修正了显示日期格式的bug。

提交评论目前使用了表单提交，ajax一步提交尝试了很久，没成功，留在以后搞。


# V1.1.3    2017.01.11
修正了git无法上传node-modules的问题，提交了web文件夹，其中包含前端源码和gulp工作流。

# V1.1.2    2016.12.01
修正了css，js的引入路径，改为绝对路径（路径开头加'/'），避免因url跳转导致的引入文件失败；

blog首页增加了通过ajax与后台交互的功能，首页默认显示前n篇博客，每次点击加载，跟后台要m篇博客，动态增加在首页显示。

# V1.1.1    2016.11.29
修改了gulp配置，调整了web文件夹下的目录结构，使得html,css,js之间的相对路径保持一致，publish之后就不用修改js，css的引用路径了；

修改了后台python在blog-list页面的输出，改为json数据，输出给页面中的变量；

在前端引入了vue，来显示后台输出的json数据；

[输出json](http://blog.csdn.net/5iasp/article/details/23338039 "Title")

[date要先格式化再转](http://www.ziqiangxuetang.com/python/datetime_strftime.html "Title")


# V 1.1.0   2016.11.26
整理文件结构，增加了web文件夹，用于前端部分的开发；

遇到了子模块无法直接提交github的问题，[stackoverflow](http://stackoverflow.com/questions/8488887/git-error-changes-not-staged-for-commit "Title")说似乎是因为子模块的原因。要用git submodule才能提交。想了想这里不提交也没关系，最后决定用[git ignore](http://www.cnblogs.com/haiq/archive/2012/12/26/2833746.html "Title")忽略了，所以这里看不到web文件夹。

**技巧：**windows下无法直接创建文件名为 .ignore 的文件，可以写为 .ignore. 来创建它。

引入gulp，在web文件夹中构建了包含sass，compass的前端自动化工作流。实现了实时监控文件变化，自动刷新浏览器，js，css压缩以及文件分发的功能。

在web文件夹下使用，命令如下：
* gulp: 默认任务，重建dist文件夹并运行服务器打开index页面，监控html,css,js文件变化并自动刷新浏览器。
* redist: 重建redist文件夹，当app文件夹中文件名称变更时使用，避免dist中出现冗余文件。
* publish: 将dist文件夹中调试完毕的文件，分发到工程中对应的templates和static文件夹中。

**注意：**为了保证项目安全，gulp的删除功能限定在web文件夹中，若中途改变文件名，再publish，可能造成templates和static文件夹中产生冗余文件，此时要手动删除。

关于gulp具体用法可以参考[我的博客](http://blog.csdn.net/Creabine/article/details/52182772 "Title")





# V 1.0.2  2016.11.24
修复了详情页不能打开以及提交评论出错的问题；（根据报错猜测是数据库中email字段的问题，搜索到了pycharm能够可视化管理SQLite，打开之后发现确实少了email字段，手动添加表之后，问题解决。半猜半蒙的搞定了，我真机智啊哈哈哈哈哈(～￣▽￣)～）

参考资料：

[pycharm可视化管理数据库](http://www.thinksaas.cn/topics/0/499/499418.html "Title")





# V 1.0.1  2016.11.23
修复了博客创建日期的问题；

增加了static目录，能够在template中引入css，js；

修复了admin页面css缺失的问题(将Django的css复制到static文件夹，再修改一下路径即可)；

制造了博客详情页面打不开的新问题...OTL；





# V 1.0.0  2016.11.22
后端部分实现博客相关的内容在数据库的读写和储存

参考资料：

[Leo_wlCnBlogs](http://www.cnblogs.com/Leo_wl/p/5824541.html "Title")

[Danny's Blog](http://www.dannysite.com/blog/?cat=3 "Title")









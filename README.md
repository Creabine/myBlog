# myBlog

尝试写一个自己的博客，前后端都由自己起来完成，感觉是个很大的项目，准备一点一点来，功能方面也是先 从简单的开始，以后再慢慢迭代。

#预期将要使用的技术

后端: Python Django jinjia2 SQLite 

前端: vue sass gulp 

# V 1.0.0
后端部分实现博客相关的内容在数据库的读写和储存

参考资料：

[Leo_wlCnBlogs](http://www.cnblogs.com/Leo_wl/p/5824541.html "Title")

[Danny's Blog](http://www.dannysite.com/blog/?cat=3 "Title")


2016.11.22

# V 1.0.1
修复了博客创建日期的问题；

增加了static目录，能够在template中引入css，js；

修复了admin页面css缺失的问题(将Django的css复制到static文件夹，再修改一下路径即可)；

制造了博客详情页面打不开的新问题...OTL；

2016.11.23

# V 1.0.2
修复了详情页不能打开以及提交评论出错的问题；（根据报错猜测是数据库中email字段的问题，搜索到了pycharm能够可视化管理SQLite，打开之后发现确实少了email字段，手动添加表之后，问题解决。半猜半蒙的搞定了，我真机智啊哈哈哈哈哈(～￣▽￣)～）

参考资料：

[pycharm可视化管理数据库](http://www.thinksaas.cn/topics/0/499/499418.html "Title")

2016.11.24

# V 1.1.0
整理文件结构，增加了web文件夹，用于前端部分的开发；

引入gulp，在web文件夹中构建了包含sass，compass的前端自动化工作流。实现了实时监控文件变化，自动刷新浏览器，js，css压缩以及文件分发的功能。

在web文件夹下使用，命令如下：
* gulp: 默认任务，重建dist文件夹并运行服务器打开index页面，监控html,css,js文件变化并自动刷新浏览器。
* redist: 重建redist文件夹，当app文件夹中文件名称变更时使用，避免dist中出现冗余文件。
* publish: 将dist文件夹中调试完毕的文件，分发到工程中对应的templates和static文件夹中。

*注意：*为了保证项目安全，gulp的删除功能限定在web文件夹中，若中途改变文件名，再publish，可能造成templates和static文件夹中产生冗余文件，此时要手动删除。

关于gulp具体用法可以参考[我的博客](http://blog.csdn.net/Creabine/article/details/52182772 "Title")

2016.11.26